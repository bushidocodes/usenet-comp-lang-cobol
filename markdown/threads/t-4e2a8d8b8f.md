[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Tiers before bedtime

_30 messages · 7 participants · 2009-07_

---

### Tiers before bedtime

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-07-20T13:36:52+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ci01fF27sg7vU1@mid.individual.net>`

```
I have been dealing with the generation of a COBOL Data Access Layer tier 
for some clients and it made me wonder  how prevalent the concept of a 
tiered architecture is on COBOL sites.

I suspect that most sites simply embed SQL in the applications and there is 
no attempt to provide a separation layer, but I obviously cannot know.

I am starting to get enquiries from people who are NOT planning on leaving 
COBOL (not yet, anyway...) but who ARE moving to RDB (or already have an 
established RDB) and like the idea of having a separation layer. If they can 
have this layer generated for them (in COBOL) at the time they set up their 
RDB, or subsequently, they are interested.(Obviously, I'd much prefer they 
built their RDB using the Toolset (because this process generates metadata 
which can be used effectively downstream in other proceses), but sometimes 
there is history involved and their RDB may have evolved historically.)

Currently, PRIMA can offer a facility which can analyse a relational table 
(or normalized tableset) and generate a COBOL record layout, Host Variables, 
and a "management object" which has invocable methods to carry out all 
possible access. This facility is provided as a COM server .DLL. The 
collection of these "DAL objects" provides a Data Access Layer tier that 
separates the data resource from the Business Logic.

Applications invoke the DAL objects instead of having SQL embedded in them. 
The DAL object contains some "smarts" for type conversion between the COBOL 
view and the database view (especially important when dealing with date 
fields), and, because it is an OO Class it can implement separate instances 
of itself for GET and PUT threading. Also, if the site later moves away from 
COBOL, these objects can still be utilised as they can run anywhere and are 
quite happy in a .NET environment or on a Windows desktop, or even from 
within a Web page. The fact that the objects are written in COBOL, is of no 
importance, as they are generated. However they COULD be manually amended to 
support stored procedures or views, for example...)

I'm still writing the user manual which includes sample code and conceptual 
background and it will be published on the cobol21 web site sometime soon.

In the meantime, I would be interested in some feedback and opinions from 
people currently working on COBOL sites as to how important the concept of a 
"multi-tiered" architecture is, to what degree it is implemented (if at 
all), and whether or not the future plans include moving to such an 
architecture (with or without COBOL).

Also, any opinion you might have personally. Is separation and layering just 
an unnecessary frippery, or can it provide real benefits? Is a tiered 
architecture unachievable in a mainframe environment, for instance?

Pete.
```

#### ↳ Re: Tiers before bedtime

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2009-07-19T22:55:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<adce8e5b-d3eb-4739-a6b9-2f878cd900bb@m7g2000prd.googlegroups.com>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net>`

```
>
> In the meantime, I would be interested in some feedback and opinions from
…[8 more quoted lines elided]…
>

At present, most of my clients (enterprise) who deploys 'online'
solution uses Windows OS running IIS as their presentation layer.
Embedded within the OS is COM server that handles OOCobol coded .DLL
files. These COM files are accessing data from a separate Data Servers
(some of them are remote data servers; even mainframes) using SQL-
engine based data.... extracting these data back into a 'temporary'
directories within the Windows OS and reads/display through ASP or
ASP.NET pages.

Embedding SQL command from within presentation layers (ASP page/PHP)
poses greater risk for a SQL-injection attacks and it is not
advisable. Though speaking of which, filtering is adopted in most
cases.

From these scenario... I could pretty well guess that this nth-tier
platform (or data layering) will still prevalent for 4 or more years
since some of them are 'just starting' to utilize online solutions. If
Google Chrome OS will popup later to be a famous online partner of
online solutions.... then online apps are a way to go.
```

##### ↳ ↳ Re: Tiers before bedtime

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-07-20T23:24:09+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cj2ekF25ji0lU1@mid.individual.net>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <adce8e5b-d3eb-4739-a6b9-2f878cd900bb@m7g2000prd.googlegroups.com>`

```
Rene_Surop wrote:
>> In the meantime, I would be interested in some feedback and opinions
>> from people currently working on COBOL sites as to how important the
…[17 more quoted lines elided]…
> ASP.NET pages.

That's a very interesting idea, Rene. I hadn't thought about doing it that 
way.
>
> Embedding SQL command from within presentation layers (ASP page/PHP)
…[8 more quoted lines elided]…
> online solutions.... then online apps are a way to go.

Excellent. Thanks for your post.

Pete.
```

#### ↳ Re: Tiers before bedtime

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-07-21T16:56:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FQq9m.419324$jp1.371634@en-nntp-06.dc1.easynews.com>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:7ci01fF27sg7vU1@mid.individual.net...
<much snippage>
> In the meantime, I would be interested in some feedback and opinions from 
> people currently working on COBOL sites as to how important the concept of a 
…[3 more quoted lines elided]…
>
Pete,
  I may be mistaken on this (as you know, I am NOT currently doing "production" 
COBOL work) but it would seem to me that what is used today may well depend upon 
what/where the production application is running.  Consider (for example)

1) IBM Mainframe CICS or IMS/TM - with VSAM (or IMS/DB hieracrical) data
2) IBM Mianframe CICS or IMS with SQL (DB2) data
3) IBM mianframe DB2 "data layer" with Workstation user interface
4) "Workstation" with "character based" (e.g. ACCEPT/DISPLAY) interfaces 
(particularly under Unix/Linux)
5) Workstation using Dialog System, PowerCOBOL, SP2, etc
6) Workstation with "native API calls for GUIs
7) and probably LOTS of variation of the above and different situations

All of the above ASSUME that at least part - if not most - of the application is 
in COBOL or some variation thereof.  The more "mixed" the application, the more 
likely (I think) it is to be "tiered".  The "Older" the application is (either 
"data layer" or "business logic") the more likely it is to be "monolithic" in 
nature.

I certainly could be mistaken on this, but my GUESS is that the "goal" of most 
(large) current applications is to separate user-interface from 
"data-access-layer" and both of these separated from "business logic" layer.
```

##### ↳ ↳ Re: Tiers before bedtime

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-07-22T13:34:58+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cn8lrF26r3bnU1@mid.individual.net>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <FQq9m.419324$jp1.371634@en-nntp-06.dc1.easynews.com>`

```
William M. Klein wrote:
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
> news:7ci01fF27sg7vU1@mid.individual.net...
…[30 more quoted lines elided]…
> from "business logic" layer.

Thanks Bill. As usual an informed response.

The reason for my question is that I have been using tiered architectures 
for some 25 years now and find them to be excellent. I have a lot invested 
in this concept and, while I know it works and is easily implementable on 
the network, before I could even consider presenting my offerings to 
mainframe sites I would like to get an idea of how receptive they would be 
to the concept of having a data access layer generated as OO components. I 
see two stumbling blocks:

1. Most mainframe sites are not using OO. (At least, I think they're not... 
it's been many years since I worked in that environment).
2. The concept of layers and separation may be foreign. I just don't know.

I take your point that there is already a degree of separation in the mixes 
you mentioned, but I'm not sure how "conscious" people are of this and 
whether they endorse the concept or not.

MANY years ago when I was a contract mainframe COBOL programmer for a 
living, working on various platforms in various industries, I was in a place 
where we had a major trauma just because there was new release of the 
Database software which happened to coincide with a new release of the 
Operating System. Hundreds of programs had to be amended and it seemed that 
this was a fairly normal occurrence every few years.

I finished the contract and came back to NZ for some R & R. Not far from 
where I live (about 10 minutes drive) there are thermal hot pools and it is 
great to get a private pool, strip off and be a starfish. Floating in the 
warm bubbles it is very easy to solve programming problems and it seems to 
refresh the mind as well as the body. Anyway, it came to me that if we could 
somehow separate data access from business logic and even displays in the 
same way, we could "insulate" programs against changes in the tech 
environment. Not only that, but programs written in such a manner could work 
across platforms because the actual database or presentation system would be 
irrelevant. All that was necessary was a standard interface. A new "process 
for interfacing to machines". I went back to Europe and started a company 
called "PRIMA" (PRocess for Interfacing to MAchines).

I designed the necessary interface and wrote the code to support it. 
Tentatively, and with some trepidation, I presented the concept to the place 
where I was on contract and they agreed to pilot it. It was a big success. 
British Aerospace were using a plethora of different platforms and I did a 
presentation and demo to them. The tech guys loved it but the accountants 
couldn't see the need ("You're already doing what is needed, why buy another 
tool?" (The tunnel vision of bean counters never ceases to amaze me...) I 
was crushed, but around that time I took a contract in Madrid with a major 
Bank. They were trying to use IMS and had only a few programmers who really 
understood it. I got them all together and explained how the interface 
solved a number of technical and conceptual problems. They ran a pilot, were 
delighted and standardised on the PRIMA interface. It was called "ACE" (I 
can't remember exactly how they came up with that... it might have been 
"across environments" or something like that.) A couple of years later they 
needed to move from IMS to DB2 and it was a doddle. All they had to change 
was the ACE support code, nothing in the applications.

Of course, by the time PCs arrived this concept was pretty widespread and 
most client/server applications are designed around tiered (or layered) 
architectures. For me, discovering that there was a standard interface that 
could work across platforms in the client/server environment was a delight. 
(Online Linking and Embedding was such an interface. It has evolved into the 
Component Object Model (COM) and it still amazes me how these components can 
run on the web or the desktop under Windows or .NET (or even with Unix if 
you broker them through CORBA).

For the Migration Toolset I obviously wanted to be able to generate a 
separation layer at the same time as the RDB tables were generated. This 
makes sense because all the information is present at that moment and it can 
be encapsulated into metadata for downstream use by the Toolset. It really 
isn't hard, if you are analysing COBOL file and record definitions, to 
construct a normalized DB tableset from them and then generate a module that 
can carry out all possible access to that tableset. Wrap this module as a 
COM server and you have an encapsulated component with a consistent 
interface for dealing with your database. Your applications need not (and 
should not) contain embedded SQL or DL/1 calls or anything else specific to 
a given Data Management System. They pass a single block that contains 
control, response, and data information, and whatever the actual DB system 
is, the components construct and deconstruct that layer, making sure the 
application buffer receives what the application expects, irrespective of 
the database subsytem. I have all of this working and available, and people 
are using it.(All current clients are client/server sites)

But would mainframe sites buy into it? Before I can even think about a 
campaign to reach them, it would be very useful to have some kind of inkling 
as to what the reaction is likely to be... :-)

I'm not quite ready to go there yet as I would want access to a mainframe 
before considering it and at the moment, I'm just too busy.

Nevertheless, the whole topic of tiers and layering is an interesting one.

There are advantages in separation which are not immediately obvious (Here's 
a quick half dozen, you can probably think of more...):

1. If you have a problem with a certain part of your database, it is 
isolated to one module that accesses it.
2. You can change the interface buffer (and the database) and regenerate the 
access module instantly. Programs which use it get recompiled and 
automatically pick up the new layout. If you have simply added some columns 
that will only be used by a few programs, you only need to recompile the 
programs which use the new columns; the old ones will still work without 
change.
3. The access module can be amended to include DB views and these just 
become another method in the module, invocable by programs that need the 
view. (Triggers for stored procedures can be included in the same way).
4.  Data access technology is changing. Using a Data Access Layer you are no 
longer limited to kludgy ESQL as a data access technology. The access 
modules can use LINQ, Lambdas, ADO, DAO or anything else that is desirable, 
and there is no impact on the applications. Instead of OPENing a SQL cursor 
and being consequently tied to that DB connection for the duration of your 
sequential accesses, the DAL object can use ADO to obtain a resultset and is 
only connected to the DB for milliseconds.
5. DAL objects can be generated in any language you want. (Currently, I 
generate them in OO COBOL and they use dynamic SQL, which is only marginally 
better than having ESQL in the applications, but the next step is to 
generate them in C# and use LINQ and Lambdas)
6. DAL objects are "smart" and handle all the type differences between COBOL 
and the RDB. Dates, decimals, even floats, are all dealt with by the DAL 
object. The COBOL buffer gets what it has defined (including REDEFINED and 
OCCURring fields) and the Database gets the types it expects. The "right" 
Host Variables are generated into the DAL object automatically, and loaded 
and unloaded by it into the application buffer.

Irrespective of whether you use my Toolset or not, layering your 
applications, if you don't already, could save you a lot of grief.

Pete.
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2009-07-21T23:04:26-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EJqdnTGQgccuHPvXnZ2dnUVZ_hqdnZ2d@earthlink.com>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <FQq9m.419324$jp1.371634@en-nntp-06.dc1.easynews.com> <7cn8lrF26r3bnU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:7cn8lrF26r3bnU1@mid.individual.net...
> William M. Klein wrote:
>> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[163 more quoted lines elided]…
>

I think most IBM mainframes are not using COBOL and Java together.  The ones 
that are using OO are using Java and Websphere, but I have no idea what 
percentage are using them. I do know that IBM is a strong advocate for Java.

The idea of layers and separation is not a foreign concept.  Some here have 
replaced Datacom DB calls with a DB layer that does DB2/SQL.  Most of our 
Datacom usage is a navigational/procedural style of processing, while SQL is 
more naturally set-at-a-time processing.  I did read and I can't remember 
where (I thought it was in DB2 Developers Guide by Mullen but with a quick 
look I could not locate the passage I remember) that using SQL to directly 
emulate a procedural style can sometimes result in poor performance.  I have 
no personal knowledge that this is true, and quite possibly it might have be 
true at sometime in the past but may no longer apply because of increase 
hardware performance.  Anyway I am sure that you have more firsthand 
knowlege of this than me, but I thought I would at least mention it.
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-07-23T00:07:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7codo8F2866utU1@mid.individual.net>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <FQq9m.419324$jp1.371634@en-nntp-06.dc1.easynews.com> <7cn8lrF26r3bnU1@mid.individual.net> <EJqdnTGQgccuHPvXnZ2dnUVZ_hqdnZ2d@earthlink.com>`

```
Charles Hottel wrote:
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
> news:7cn8lrF26r3bnU1@mid.individual.net...
…[174 more quoted lines elided]…
> strong advocate for Java.

I remember when they were strong advocates for COBOL... :-)

I guess they are coming to the realisation that they need OO.

>
> The idea of layers and separation is not a foreign concept.  Some
…[3 more quoted lines elided]…
> processing.

That's a pretty good start...


> I did read and I can't remember where (I thought it was
> in DB2 Developers Guide by Mullen but with a quick look I could not
> locate the passage I remember) that using SQL to directly emulate a
> procedural style can sometimes result in poor performance.

For random access using singleton selects it really isn't significant. The 
problem arises when you start to do sequential and skip-sequential 
processing, which requires a cursor if you are using ESQL. The Cursor opens 
and connects to the DB. But it holds that connection until you close it. If 
you have a busy DB with many people accessing, the number of connections 
available can be important. By comparison, if I define a resultset instead 
of a cursor (I can do this in C# or Java) then the connection only lasts 
while the resultset is loaded (usually a few milliseconds) and the resultset 
is stored in virtual memory, with rows being presented to me by a reader 
that gets them directly from memory. Any changes I make (or inserts/deletes) 
are deferred (unless I say they must be applied immediately) until I have 
completed processing the set. Then I replace it and the system automatically 
re-establishes contact with the DB and puts back all the amendments. (Again, 
a connection of milliseconds...) It is cleaner and faster and less intrusive 
into the RDB software.

Experiments I did when developing the DAL objects show that running separate 
GET and PUT threads considerably improves overall throughput, even with 
ESQL.


> I have no
> personal knowledge that this is true, and quite possibly it might
…[3 more quoted lines elided]…
> least mention it.

Thanks for your comment.

Pete.
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-07-22T13:04:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h472pb$k91$1@reader1.panix.com>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <FQq9m.419324$jp1.371634@en-nntp-06.dc1.easynews.com> <7cn8lrF26r3bnU1@mid.individual.net> <EJqdnTGQgccuHPvXnZ2dnUVZ_hqdnZ2d@earthlink.com>`

```
In article <EJqdnTGQgccuHPvXnZ2dnUVZ_hqdnZ2d@earthlink.com>,
Charles Hottel <chottel@earthlink.net> wrote:

[snip]

>Some here have 
>replaced Datacom DB calls with a DB layer that does DB2/SQL.  Most of our 
…[7 more quoted lines elided]…
>hardware performance.

Back in the Oldene Dayse one of the Standard Interview Questions was about 
this; I can't recall the question but the answer was 'cursor drag'.

This was what happened when a cursor was DECLARED for FETCH and the 
OPENed; the tables involved were scanned and a temporary table matching 
the cursor's definition was created... sometimes quite large.  Subsequent 
FETCHes were made against this result-set and the temp table was 
internally DROPped after the cursor was CLOSEd.

(when helping my Tech Lead learn SQL/PeopleSoft processing I said that 
COBOL dealt with data on the record-level while SQL dealt with data 
conditions across the tables involved... this seemed to help him with the 
transition)

DD
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-07-22T08:18:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ai7e6519dgho5hqgr9jlu6noe6jm2tuv2n@4ax.com>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <FQq9m.419324$jp1.371634@en-nntp-06.dc1.easynews.com> <7cn8lrF26r3bnU1@mid.individual.net>`

```
On Wed, 22 Jul 2009 13:34:58 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>The tech guys loved it but the accountants 
>couldn't see the need ("You're already doing what is needed, why buy another 
>tool?" (The tunnel vision of bean counters never ceases to amaze me...)

It isn't just accountants who fear to implement short term costs for
long term advantages.    Anybody whose next evaluation depends upon
short term success is motivated to keep current costs low.

This includes most any politician as well as anybody who has short
term stock options.   And certainly short-term employees.
```

##### ↳ ↳ Re: Tiers before bedtime

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-07-22T08:10:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eo6e655t5qon51qok268m7vua77b4145ok@4ax.com>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <FQq9m.419324$jp1.371634@en-nntp-06.dc1.easynews.com>`

```
On Tue, 21 Jul 2009 16:56:51 -0500, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

>I certainly could be mistaken on this, but my GUESS is that the "goal" of most 
>(large) current applications is to separate user-interface from 
>"data-access-layer" and both of these separated from "business logic" layer.

That's the way I see it as well.    I see the near term future IS
consisting of:

The Data.
Business logic.
User interface.

The Business logic can be distributed over multiple machines, but the
data are often on a highly secure database machine.
There's lots of communication stuff in between.    The percentage of
IS people who don't work with the business needs is growing.

The place where we would look for CoBOL first is in the business
logic.   But if the environment is an XML one, one might ask if CoBOL
is particularly well suited for turning SQL produced data into XML.

Let's assume that we convert an old system to the above model, using
XML (other alternatives have similar tools).    Let's use CoBOL for
the middle step.    Much of the business logic is moved to the SQL
(which can be run by most any language).    The formatting can be
skipped - except to move the data into XML (which other languages can
do at least as well).    How much business logic is left?  
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-07-23T12:09:28+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cpo1gF29d6j9U1@mid.individual.net>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <FQq9m.419324$jp1.371634@en-nntp-06.dc1.easynews.com> <eo6e655t5qon51qok268m7vua77b4145ok@4ax.com>`

```
Howard Brazee wrote:
> On Tue, 21 Jul 2009 16:56:51 -0500, "William M. Klein"
> <wmklein@nospam.ix.netcom.com> wrote:
…[11 more quoted lines elided]…
> User interface.

This is the standard "three tier model"

So it looks like it has permeated to mainframe sites.

Thanks for that.
>
> The Business logic can be distributed over multiple machines, but the
…[11 more quoted lines elided]…
> (which can be run by most any language).

Are you saying "programmed" in SQL or using stored proedures, or both?


> The formatting can be
> skipped - except to move the data into XML (which other languages can
> do at least as well).    How much business logic is left?

That's a very interesting idea. I have met some IT managers (not on COBOL 
sites) who see the business logic being subsumed into SQL. The argument is 
that the data drives the business so it makes sense to have "smart" data. 
I've never been persuaded but it looks like I should look at this again. 
They might have a point.

I'm not sure if it is a good idea to tie your business to SQL, any more than 
it is to tie it to COBOL or Java or anything else. I see separation as being 
about standard interfaces. These should be purely functional, not technical. 
(The same generalized interface should apply whether you are using SQL, or 
COBOL, or C# or whatever. The interface drives functional actions and 
transfers data to where it is needed; the code behind the interface could be 
in anything appropriate. For example, my DAL objects are in OO COBOL 
currently because they are designed for use on what are currently COBOL 
sites, and that makes them familiar to programmers on those sites. But I do 
plan on offering a C# option in the future so that more advanced data access 
technology than is natively available through COBOL can be utilised. I would 
not expect the interface to change in any way and I would consider the whole 
thing a failure if applications need to be changed. That is what I mean by 
"functional separation".)

Thanks for your post, Howard.

Pete.
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-07-23T12:40:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h49lo0$fkf$2@reader1.panix.com>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <FQq9m.419324$jp1.371634@en-nntp-06.dc1.easynews.com> <eo6e655t5qon51qok268m7vua77b4145ok@4ax.com> <7cpo1gF29d6j9U1@mid.individual.net>`

```
In article <7cpo1gF29d6j9U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>That's a very interesting idea. I have met some IT managers (not on COBOL 
>sites) who see the business logic being subsumed into SQL. The argument is 
>that the data drives the business so it makes sense to have "smart" data. 
>I've never been persuaded but it looks like I should look at this again. 
>They might have a point.

I have run into that as Standard Interview Question Number 875: 'Do the 
data drive the business or is the business reflected in the data?'

My answer has been 'Yes'.

DD
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-07-23T08:00:27-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i4rg6512nrpnnqf67hs0vhp995162h54pj@4ax.com>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <FQq9m.419324$jp1.371634@en-nntp-06.dc1.easynews.com> <eo6e655t5qon51qok268m7vua77b4145ok@4ax.com> <7cpo1gF29d6j9U1@mid.individual.net> <h49lo0$fkf$2@reader1.panix.com>`

```
One interesting contract I had was with an insurance company that
bought out another insurance company.   They both had data warehouses
that measured similar, but not identical data.    Our job was to
combine these in a meaningful and useful manner.
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-07-23T14:18:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h49rgh$h0i$1@reader1.panix.com>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <7cpo1gF29d6j9U1@mid.individual.net> <h49lo0$fkf$2@reader1.panix.com> <i4rg6512nrpnnqf67hs0vhp995162h54pj@4ax.com>`

```
In article <i4rg6512nrpnnqf67hs0vhp995162h54pj@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>One interesting contract I had was with an insurance company that
>bought out another insurance company.   They both had data warehouses
>that measured similar, but not identical data.    Our job was to
>combine these in a meaningful and useful manner.

Don't tell me, let me guess... 'meaningful and useful' had a way of 
changing depending upon who was speaking.

DD
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-07-23T09:23:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<800h65t6vk4pqjthh6deg3md2obquv3t0u@4ax.com>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <7cpo1gF29d6j9U1@mid.individual.net> <h49lo0$fkf$2@reader1.panix.com> <i4rg6512nrpnnqf67hs0vhp995162h54pj@4ax.com> <h49rgh$h0i$1@reader1.panix.com>`

```
On Thu, 23 Jul 2009 14:18:57 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <i4rg6512nrpnnqf67hs0vhp995162h54pj@4ax.com>,
>Howard Brazee  <howard@brazee.net> wrote:
…[8 more quoted lines elided]…
>DD

OK.

There are some experiences that are virtually universal for those of
us who have been working long enough. 
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-07-23T15:35:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h4a00p$a0p$1@reader1.panix.com>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <i4rg6512nrpnnqf67hs0vhp995162h54pj@4ax.com> <h49rgh$h0i$1@reader1.panix.com> <800h65t6vk4pqjthh6deg3md2obquv3t0u@4ax.com>`

```
In article <800h65t6vk4pqjthh6deg3md2obquv3t0u@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Thu, 23 Jul 2009 14:18:57 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[13 more quoted lines elided]…
>us who have been working long enough. 

'Before enlightenment, chop wood and carry water.  After enlightenment, 
chop wood and carry water.' - undated Zen axiom

DD
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-07-23T07:45:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6bqg655ngqdo587fho46sllcc7t3smqv9b@4ax.com>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <FQq9m.419324$jp1.371634@en-nntp-06.dc1.easynews.com> <eo6e655t5qon51qok268m7vua77b4145ok@4ax.com> <7cpo1gF29d6j9U1@mid.individual.net>`

```
On Thu, 23 Jul 2009 12:09:28 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> Let's assume that we convert an old system to the above model, using
>> XML (other alternatives have similar tools).    Let's use CoBOL for
…[3 more quoted lines elided]…
>Are you saying "programmed" in SQL or using stored proedures, or both?

I'd be interested in exploring the differences in all three
possibilities here in our discussion.
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-07-23T07:56:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7eqg65tl6kppdhb80rbink6alq147l25e2@4ax.com>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <FQq9m.419324$jp1.371634@en-nntp-06.dc1.easynews.com> <eo6e655t5qon51qok268m7vua77b4145ok@4ax.com> <7cpo1gF29d6j9U1@mid.individual.net>`

```
On Thu, 23 Jul 2009 12:09:28 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I'm not sure if it is a good idea to tie your business to SQL, any more than 
>it is to tie it to COBOL or Java or anything else.

I see your point.   But I also see this as the step that is occurring
as mainframe computers move to relational databases and the three tier
model.

Without actually observing it in real life, your ideas would indicate
that a subsequent step might be to encapsulate the SQL, followed by
independence from SQL.    Intriguing, but I don't know if the
independence will happen in large shops.    

It may be that by the time large shops Get Around To It, a new
paradigm will be around.   

=========================

Of course, each generation has the Final Right way of doing things.
Conservatives just have an older Final Right way than liberals do. Big
IS shops tend to be conservative.

Admittedly, there is considerable variation within a particular broad
philosophy - obviously with something like politics, but certainly
within information systems as well.
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-07-24T02:57:08+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7crc25F2948c8U1@mid.individual.net>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <FQq9m.419324$jp1.371634@en-nntp-06.dc1.easynews.com> <eo6e655t5qon51qok268m7vua77b4145ok@4ax.com> <7cpo1gF29d6j9U1@mid.individual.net> <7eqg65tl6kppdhb80rbink6alq147l25e2@4ax.com>`

```
Howard Brazee wrote:
> On Thu, 23 Jul 2009 12:09:28 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[11 more quoted lines elided]…
> independence will happen in large shops.

Thank you. That is exactly what I was trying to express, although I hadn't 
realised it myself until you wrote that :-)

It's not just SQL, of course. It could equally well be IDMS components 
walking member sets etc. WHATEVER it is, if you can encapsulate it and 
provide a truly separated interface to it that is generalised on FUNCTION 
and not on TECH stuff, then you can be free of it indeed...

I have published a lot more on this whole business of separation layers and 
DAL interfacing today, on cobol21.

http://primacomputing.co.nz/cobol21/PRIMAToolset.aspx



There are some browse links towards the bottom of the page.



If you browse the DAL Manual there is COBOL code describing the interface. 
The interface and the methods available reflect the FUNCTIONS you would 
expect to use when accessing an indexed dataset (VSAM/KSDS or ISAM), and yet 
they are being carried out against a Relational database which is accessed 
in SQL and does NOT have a COBOL defined structure. Soon the same functions 
will be available using LINQ and Lamdas. The interface will not change. It 
works because the interface is functional. You could use the same interface 
to get to IDMS or IMS or anything else. The interface provides Control, 
Response, and Data exchange. That is all you can ever need...



>
> It may be that by the time large shops Get Around To It, a new
> paradigm will be around.



That is always a possibility, but if you have true separation based on 
function, it wouldn't matter. The "code behind" would simply get rewritten 
to use the new paradigm. If you had asked me 10 years ago if I could see 
ESQL being replaced , I would have said "no". But it is already obsolete.



The race of technology is another reason why we need separation from it.
>
> =========================
…[3 more quoted lines elided]…
> IS shops tend to be conservative.



I don't believe anything is final or even "right". I think we do the best we 
can with what we have.


>
> Admittedly, there is considerable variation within a particular broad
> philosophy - obviously with something like politics, but certainly
> within information systems as well.



Yes, there are many ways you can be "not wrong" without being "right" 
either... :-)



Pete.
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-07-23T09:26:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k70h6513df1nvrmi8ikcpme36v4qf631fe@4ax.com>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <FQq9m.419324$jp1.371634@en-nntp-06.dc1.easynews.com> <eo6e655t5qon51qok268m7vua77b4145ok@4ax.com> <7cpo1gF29d6j9U1@mid.individual.net> <7eqg65tl6kppdhb80rbink6alq147l25e2@4ax.com> <7crc25F2948c8U1@mid.individual.net>`

```
On Fri, 24 Jul 2009 02:57:08 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>http://primacomputing.co.nz/cobol21/PRIMAToolset.aspx
>
>
>
>There are some browse links towards the bottom of the page.


Thanks.

I hope these links I saved will be more useful than just good reading.
Sometimes management surprises me.
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-07-24T04:55:32+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7crj05F28u0qlU1@mid.individual.net>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <FQq9m.419324$jp1.371634@en-nntp-06.dc1.easynews.com> <eo6e655t5qon51qok268m7vua77b4145ok@4ax.com> <7cpo1gF29d6j9U1@mid.individual.net> <7eqg65tl6kppdhb80rbink6alq147l25e2@4ax.com> <7crc25F2948c8U1@mid.individual.net> <k70h6513df1nvrmi8ikcpme36v4qf631fe@4ax.com>`

```
Howard Brazee wrote:
> On Fri, 24 Jul 2009 02:57:08 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[11 more quoted lines elided]…
> Sometimes management surprises me.

Thanks for your interest Howard. I have spent many hours writing these 
documents (primarily for clients of course) but having them available does 
help to crystallize the concepts behind them. I sometimes find that simply 
drawing a diagram can really make me see a process in a completely new way. 
And they definitely help people to get the idea of what I'm saying. (I've 
had some good feedback on the drawings and diagrams and that encourages me 
to do more... :-))

If you consider it "good reading" I am more than happy; if you actually get 
something useful then my time has been very well spent.

The most popular page on the site is the S2N component tester. I think it is 
the old 360-40 that tugs at the heart strings... :-)

Unfortunately the download of the Migration "package" is not working at the 
moment as I am waiting to put screen shots of the Toolset into it and I just 
haven't had time. Still, the browse links are a step in the right direction.

(My favourite is the shot of the MOSTAMD comparison, showing COBOL source 
being automatically amended to have all ISAM access replaced with DAL 
component invocation. That program never ceases to amaze me (even more than 
MOSTGEN, which actually writes the average 3000 lines of COBOL for each DAL 
object) and I get a buzz every time I run it :-)) All of the Toolset is 
written in C# but it uses some COBOL components, as well as C# ones.)

Just as a matter of interest, I have a requirement in the pipeline to 
produce 250 DAL objects for someone who plans to use them from VB. This 
represents around 750,000 lines of debugged working COBOL. How long would 
you estimate that to take if it was being done manually? I'm going to be 
watching that particular job with interest when we come to do it.I'll post 
here how long it takes.

Pete.
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-07-23T11:02:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ls5h65563okv15qtkk1d7845kktcg14des@4ax.com>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <FQq9m.419324$jp1.371634@en-nntp-06.dc1.easynews.com> <eo6e655t5qon51qok268m7vua77b4145ok@4ax.com> <7cpo1gF29d6j9U1@mid.individual.net> <7eqg65tl6kppdhb80rbink6alq147l25e2@4ax.com> <7crc25F2948c8U1@mid.individual.net> <k70h6513df1nvrmi8ikcpme36v4qf631fe@4ax.com> <7crj05F28u0qlU1@mid.individual.net>`

```
On Fri, 24 Jul 2009 04:55:32 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Just as a matter of interest, I have a requirement in the pipeline to 
>produce 250 DAL objects for someone who plans to use them from VB. This 
…[3 more quoted lines elided]…
>here how long it takes.

I never could estimate how long it takes unknown code to be converted
into anything.
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-07-24T12:09:46+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cscebF29jpouU1@mid.individual.net>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <FQq9m.419324$jp1.371634@en-nntp-06.dc1.easynews.com> <eo6e655t5qon51qok268m7vua77b4145ok@4ax.com> <7cpo1gF29d6j9U1@mid.individual.net> <7eqg65tl6kppdhb80rbink6alq147l25e2@4ax.com> <7crc25F2948c8U1@mid.individual.net> <k70h6513df1nvrmi8ikcpme36v4qf631fe@4ax.com> <7crj05F28u0qlU1@mid.individual.net> <ls5h65563okv15qtkk1d7845kktcg14des@4ax.com>`

```
Howard Brazee wrote:
> On Fri, 24 Jul 2009 04:55:32 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[9 more quoted lines elided]…
> into anything.

This is just like developing 250 modules with known function, each of which 
is around 3000 lines of COBOL.

I was always in trouble when I worked for IBM because I could never accept 
function points and lines of code as being an adequate way to predict 
effort. My Boss was always telling me to just do my own estimates then 
provide a standard one using function points and lines of code, that matched 
it. (I usually refused or didn't provide it on time and was carpeted for 
it...I was younger and more headstrong then; today I would handle it 
differently :-)) Many people there were doing the work estimates AFTER the 
code was written and making sure that their function point estimates matched 
reality, which simply propagates the myth of function point analysis. At 
that time, for COBOL, if 200 lines of code (fully tested and debugged) were 
produced per day, that was considered, acceptable. So the modules I'm 
talking about would be 15 man/days each. You can see how IBM developed a 
reputation for being expensive... Much worse is the fact that if you tell 
somebody he has 3 elapsed weeks to do a job that should be done easily in 
one week, then he will take three weeks...

In fairness, I should add that this was all a long time ago and IBM probably 
have better ways of estimating, nowadays.

There is really no substitute for experience at the coal face when it comes 
to estimating how long it will take to fill the next coal-cart.

Pete.
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-07-23T07:58:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72rg655pgsqsobrfmobrili39t019ielg8@4ax.com>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <FQq9m.419324$jp1.371634@en-nntp-06.dc1.easynews.com> <eo6e655t5qon51qok268m7vua77b4145ok@4ax.com> <7cpo1gF29d6j9U1@mid.individual.net>`

```
On Thu, 23 Jul 2009 12:09:28 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I would 
>not expect the interface to change in any way and I would consider the whole 
>thing a failure if applications need to be changed. That is what I mean by 
>"functional separation".)

However, business needs change.   So good design allows applications
to be changed as well.
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-07-24T03:03:29+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7crce2F29jhbvU1@mid.individual.net>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <FQq9m.419324$jp1.371634@en-nntp-06.dc1.easynews.com> <eo6e655t5qon51qok268m7vua77b4145ok@4ax.com> <7cpo1gF29d6j9U1@mid.individual.net> <72rg655pgsqsobrfmobrili39t019ielg8@4ax.com>`

```
Howard Brazee wrote:
> On Thu, 23 Jul 2009 12:09:28 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[7 more quoted lines elided]…
> to be changed as well.

Oh sure, I was talking about applications needing to be changed simply 
because of changes in technology. (The original post mentioned when I first 
started thinking about these things... it was when we needed to change 
hundreds of application programs because we simultaneously implemented a DB 
and OS upgrade. I remember my Boss being very angry because of what he 
considered the very cavalier attitude of IBM at the time: "No big deal. A 
few changed lines and recompile...")

ANYTHING you implement should allow applications to be easily changed. 
Proper separation does achieve this.

Pete.
```

#### ↳ Re: Tiers before bedtime

- **From:** "Richard Maher" <maher_rj@hotspamnotmail.com>
- **Date:** 2009-07-22T19:39:44+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h46tln$9k2$1@news-01.bur.connect.com.au>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net>`

```
Hi all,

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:7ci01fF27sg7vU1@mid.individual.net...

Wrote Blah>

The problem is you all say too much about too little and too often on the
same bloody subject :-(

Your myopic interperetation of the "Tiers" went out with the Ark/COBOL.

Anyway, here is where I see COBOL doing what it's good at: -

http://manson.vistech.net/t3$examples/demo_client_web.html

and

http://manson.vistech.net/t3$examples/demo_client_flex.html

All source can be found at:

http://manson.vistech.net/t3$examples/

You need JavaScript enabled, Applets enabled, Flah Player (bloody recent)
and other things that I can't be bothered cetifying

Cheers Richard Maher
```

##### ↳ ↳ Re: Tiers before bedtime

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-07-23T00:06:02+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7codl3F29irn7U1@mid.individual.net>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <h46tln$9k2$1@news-01.bur.connect.com.au>`

```
Richard Maher wrote:
> Hi all,
>
…[6 more quoted lines elided]…
> the same bloody subject :-(

Perhaps not reading it might help?
>
> Your myopic interperetation of the "Tiers" went out with the
> Ark/COBOL.

That might well be, as I have been using them in the way described for some 
time now.

I'm always interested to extend myeducation, but I can't access the site... 
see below.

>
> Anyway, here is where I see COBOL doing what it's good at: -
…[12 more quoted lines elided]…
> recent) and other things that I can't be bothered cetifying

You mean like a log in?  I am very interested to see this stuff but 
currently I can't...

Can you post some server credentials for us?

Pete.
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

- **From:** "Richard Maher" <maher_rj@hotspamnotmail.com>
- **Date:** 2009-07-22T22:48:52+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h478ob$gqf$1@news-01.bur.connect.com.au>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <h46tln$9k2$1@news-01.bur.connect.com.au> <7codl3F29irn7U1@mid.individual.net>`

```
Hi Pete,

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:7codl3F29irn7U1@mid.individual.net...
> Richard Maher wrote:
> > Hi all,
…[14 more quoted lines elided]…
> That might well be, as I have been using them in the way described for
some
> time now.
>
> I'm always interested to extend myeducation, but I can't access the
site...
> see below.
>
…[19 more quoted lines elided]…
> Can you post some server credentials for us?

Oops! That was pretty stupid of me - again :-)

Username: TIER3_DEMO
Password QUEUE

>
> Pete.

Cheers Richard Maher
> -- 
> "I used to write COBOL...now I can do anything."
>

PS Server Source is DEMO_UARS.COB

>
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

_(reply depth: 4)_

- **From:** "Richard Maher" <maher_rj@hotspamnotmail.com>
- **Date:** 2009-07-23T06:43:44+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h484in$6rf$1@news-01.bur.connect.com.au>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <h46tln$9k2$1@news-01.bur.connect.com.au> <7codl3F29irn7U1@mid.individual.net> <h478ob$gqf$1@news-01.bur.connect.com.au>`

```
HI Again,

"Richard Maher" <maher_rj@hotspamnotmail.com> wrote in message
news:h478ob$gqf$1@news-01.bur.connect.com.au...
> Hi Pete,
>
…[50 more quoted lines elided]…
> Password QUEUE

Looks like the server is now down :-(

The URL I gave you points to a crappy old "hobbiest" VAX in Florida so
performance isn't idylic anyway. (Beggars can't be choosers :-)

Please be patient and try again tomorrow. The Flex example uses the Adobe
FABridge to populate Flex-Charts from Javascript (and all fed from COBOL
DEMO_FLEX.COB)

>
> >
> > Pete.
>
 Cheers Richard Maher
>
```

###### ↳ ↳ ↳ Re: Tiers before bedtime

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-07-23T12:12:25+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cpo71F28v4fuU1@mid.individual.net>`
- **References:** `<7ci01fF27sg7vU1@mid.individual.net> <h46tln$9k2$1@news-01.bur.connect.com.au> <7codl3F29irn7U1@mid.individual.net> <h478ob$gqf$1@news-01.bur.connect.com.au> <h484in$6rf$1@news-01.bur.connect.com.au>`

```
Richard Maher wrote:
> HI Again,
>
…[61 more quoted lines elided]…
> from COBOL DEMO_FLEX.COB)

OK, I truly understand about server problems... :-)

I'll comment after I've seen it, and thanks.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
