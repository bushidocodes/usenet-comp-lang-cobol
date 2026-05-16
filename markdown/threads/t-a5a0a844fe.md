[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cics, db2, sql question

_13 messages · 6 participants · 2005-06_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Databases and SQL`](../topics.md#databases)

---

### cics, db2, sql question

- **From:** "charles hottel" <jghottel@yahoo.com>
- **Date:** 2005-06-15T18:37:05-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58bc3$42b0ad7f$43f2931b$2714@DIALUPUSA.NET>`

```
We currently use CICS, DatacommDB and COBOL.  Management is contemplating 
moving to DB2 and Java and SQL. I have no DB2  or Java experience and only a 
little SQL experience. So I have been reading up on these subjects to 
prepare myself for the future.

We have many programs called locates or browses that display N lines per 
screen where each line contains information from a single record.  The user 
can scroll forward or backward.  Backward scrolling is easy with DatacommDB 
as it has a read backward command, REDBR.

From reading "DB2 for the COBOL programmer Part2 2nd ed", chapter 8 "How to 
browse DB2 data in a CICS Program", page 214:

"when a pseudo conversational program ends DB2 drops the result table"

"conflict between the operating modes of CICS and DB2 is so serious that 
some shops prohibit CICS/DB2 browse programs or limit their number.  For 
applications that could involve huge numbers of rows, limiting CICS/DB2 
browsing is certainly reasonable.  If online tables contain millions of 
rows, for example, it would be unreasonable not to prohibit browse 
operations."

The book gives 3 strategies and calls them all costly:

1. do a separate query for each execution of the program

2. do a single query and browse in conversational style

3. do a single query and save the results in a temporary area between pseudo 
conversational executions

We have nine tables with over 1 million records.  From smallest to largest 
they contain 4.4M, 30.8M, 47M, 51.5M, 93M, 102.7M,129M, 158M, and 207M 
records.  We have 30 plus tables altogether and most of them have a browse 
function/transaction code.

Strategy number 2 is out of consideration as conversational programs are not 
allowed.

I can see how strategy number 1 works well for forward scrolling but how do 
you do backward scrolling with SQL?  Our keys are not sequential numbers so 
I cannot just take the key from the top line and subtract N-1 from it to get 
the starting record for a scroll back.

Strategy number 3 just seems to move the bottleneck to a new location.

So my question is , how would you write this kind of program.  The book I 
mentioned above is a little on the old side so I am hoping someone with more 
recent knowledge of DB2 and SQL can suggest a better way to implement this. 
Thanks in advance for your help.

Charlie Hottel
```

#### ↳ Re: cics, db2, sql question

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-06-16T14:04:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3hc515Fg3bflU1@individual.net>`
- **References:** `<58bc3$42b0ad7f$43f2931b$2714@DIALUPUSA.NET>`

```
Hi Charles,

good to see you are still here... :-)

(excellent description of the problem, BTW...)

Some comments below...

"charles hottel" <jghottel@yahoo.com> wrote in message
news:58bc3$42b0ad7f$43f2931b$2714@DIALUPUSA.NET...
> We currently use CICS, DatacommDB and COBOL.  Management is contemplating
> moving to DB2 and Java and SQL. I have no DB2  or Java experience and only
a
> little SQL experience. So I have been reading up on these subjects to
> prepare myself for the future.
>
> We have many programs called locates or browses that display N lines per
> screen where each line contains information from a single record.  The
user
> can scroll forward or backward.  Backward scrolling is easy with
DatacommDB
> as it has a read backward command, REDBR.
>
> From reading "DB2 for the COBOL programmer Part2 2nd ed", chapter 8 "How
to
> browse DB2 data in a CICS Program", page 214:
>
> "when a pseudo conversational program ends DB2 drops the result table"
>

Yes, that has always been true as I recall. You can save it by creating a
new temporary table with it. This will remain across dequeue boundaries
(interactions with the user).

> "conflict between the operating modes of CICS and DB2 is so serious that
> some shops prohibit CICS/DB2 browse programs or limit their number.  For
…[4 more quoted lines elided]…
>

I never knew that. Doesn't sound very 'user friendly' does it?

> The book gives 3 strategies and calls them all costly:
>
…[4 more quoted lines elided]…
> 3. do a single query and save the results in a temporary area between
pseudo
> conversational executions
>

3 is probably the one I just mentioned above...

> We have nine tables with over 1 million records.  From smallest to largest
> they contain 4.4M, 30.8M, 47M, 51.5M, 93M, 102.7M,129M, 158M, and 207M
> records.  We have 30 plus tables altogether and most of them have a browse
> function/transaction code.
>

Wow! (So you won't be running this on a desktop PC, then... ?<g>)

> Strategy number 2 is out of consideration as conversational programs are
not
> allowed.
>

And for very good reasons... :-)

> I can see how strategy number 1 works well for forward scrolling but how
do
> you do backward scrolling with SQL?  Our keys are not sequential numbers
so
> I cannot just take the key from the top line and subtract N-1 from it to
get
> the starting record for a scroll back.
>

Check out ORDER BY  and the use of cursors in your DB2 docs. RDBMS store
data without any regard to sequence (it is different from ISAM/VSAM
concepts, even though these access methods may be used to support the tables
physically.) The idea is that STORAGE (in as efficient a manner as possible)
is the responsibility of the RDBMS (it can put stuff anywhere it likes and,
as users, it is none of our business how or what it does...now you start to
understand why DBAs tend to have worried expressions.. :-)), but RETRIEVAL
SEQUENCE is a user responsibility; so it provides ORDER BY and what you need
is sequenced how you want it, at the time you retrieve it, rather than when
it was stored.


> Strategy number 3 just seems to move the bottleneck to a new location.
>
> So my question is , how would you write this kind of program.  The book I
> mentioned above is a little on the old side so I am hoping someone with
more
> recent knowledge of DB2 and SQL can suggest a better way to implement
this.
> Thanks in advance for your help.

I can't claim recent knowledge, but I have some ideas that may help.

1. Don't retrieve all of the data. Just the Keys, and use ORDER BY to get
the result set sequenced the way you want. Personally, I would use option 3
to save this result set in a temporary table. (Think of this as an index to
the real data, rather than a bottleneck moved somewhere else... <g>)

2. Write a CICS program that builds one screenful of data, starting from any
given key in the result set.

(It would access, say, 20 rows to get the data for each row on the screen,
using 20 keys in sequence from the result set, starting from the one you
gave it. (if the data for each key fits on one row... it is simple to use
the same concept for however many rows you need to display one item). Think
of it as a 'screen builder'. I would write a callable function that takes a
result set key and returns a screen data row, or several rows if it needs
several rows to display the data for one key. This would be the fundamental
building block for the screen builder.) To read the keys in sequence from
the result set, starting at a given key, open a cursor with WHERE
key-in-result-set > key-to-be-used ORDER BY key ASCENDING. Some
implementations of SQL allow you to limit the number of items returned
(check whether current DB2 implements TOP or SET ROWCOUNT), so you could use
the number you can accommodate on one screen. You then use the cursor to
fetch and build as many lines as fit on the screen. If backward browsing the
underlying data is required, you will need to know the keys previous to the
specified one. Use another cursor with WHERE key-in-result-set <
key-to-be-used ORDER BY key DESCENDING... (You probably won't actually build
the screen lines in reverse order, but this cursor lets you move 'back' as
many keys as you need to, to get a screenful.)

3. Store the start key for each screenful onto a CICS TS queue. (Might be
useful to add a number to them indicating the order in which the user
accessed these screens. If he wants to go back 4  screens, this would
facilitate it.) This is then an index to the screenfuls of data the user has
accessed (a history, if you like...). If he wants to review from history,
you can offer that.

4. The screen builder provides functionality to go anywhere in the result
set and build a screen from that point.  This would enable users to input a
key and get a screenful from that point, so the functionality would not just
be PREVIOUS and NEXT, but you could also add GET, with a user provided key.
The backward cursor on the result set lets you decide which key to use as
the screen 'root'  for a 'page back' request.

I don't have enough information about the details of what you are doing to
offer a detailed solution so the above is mainly conceptual. Sometimes
exploring ideas can generate other and better ideas.

Some points to keep in mind:

1. If you only return the keys of the real tables into your result set, DB2
can do it very quickly from its own indexes.
2. To randomly access underlying data for say, 20 keys, in order to build a
screen is very fast with DB2. Clustering, caching, indexing and optimization
are all taken care of by modern RDBMS, based on access patterns. You should
see no noticeable delay, despite the fact that the underlying data is
massive.

Hope this helps,

Pete.
```

##### ↳ ↳ Re: cics, db2, sql question

- **From:** "charles hottel" <jghottel@yahoo.com>
- **Date:** 2005-06-16T18:55:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2a8c$42b20354$43f29327$10064@DIALUPUSA.NET>`
- **References:** `<58bc3$42b0ad7f$43f2931b$2714@DIALUPUSA.NET> <3hc515Fg3bflU1@individual.net>`

```
Pete,

Thanks as always you gave me a lot to think about and helped me to clarify 
some of my thinking.

<snip>
```

#### ↳ Re: cics, db2, sql question

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-06-16T02:58:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-BBD22B.02581516062005@ispnews.usenetserver.com>`
- **References:** `<58bc3$42b0ad7f$43f2931b$2714@DIALUPUSA.NET>`

```
IIRC the book you quote was based on DB2 v2.1 or maybe v4.x -- either is 
a long dead version.

Current DB2 releases support cursors that can scroll backwards, return a  
limited number of rows (a screenful), and DB2 has ways to maintain a 
cursor across transactions in a pseudo-conversational mode.

I've never seen a limitation on browse functionality, nor do I consider 
millions of rows to be a large table these days.

If you are moving to Java will you be maintaining a 
pseudo-conversational style, e.g. 3270?  Or will you be using something 
like an http server that can maintain those states for you?

You have alot of things changing at once.  It might be a good time to 
step back and question if some design decisions make sense in the 
CICS/TS environment.

At the very lest, get the latest and greatest 'application programmers 
guide' from IBM's public book server.  Many of the cool cursor features 
have been added since that book was written and they might solve your 
problem handily.



In article <58bc3$42b0ad7f$43f2931b$2714@DIALUPUSA.NET>,
 "charles hottel" <jghottel@yahoo.com> wrote:

> We currently use CICS, DatacommDB and COBOL.  Management is contemplating 
> moving to DB2 and Java and SQL. I have no DB2  or Java experience and only a 
…[49 more quoted lines elided]…
> Charlie Hottel
```

##### ↳ ↳ Re: cics, db2, sql question

- **From:** "charles hottel" <jghottel@yahoo.com>
- **Date:** 2005-06-16T19:31:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80d7a$42b20eda$43f2936d$10296@DIALUPUSA.NET>`
- **References:** `<58bc3$42b0ad7f$43f2931b$2714@DIALUPUSA.NET> <joe_zitzelberger-BBD22B.02581516062005@ispnews.usenetserver.com>`

```
Joe,

Thanks I will check out the application programmer guide.

One comment below.

"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote in message 
news:joe_zitzelberger-BBD22B.02581516062005@ispnews.usenetserver.com...
> IIRC the book you quote was based on DB2 v2.1 or maybe v4.x -- either is
> a long dead version.
…[10 more quoted lines elided]…
> like an http server that can maintain those states for you?

Actually I do not know what the exact environment will be.  My best guess 
would be an http server. I am not 100% certain whether this will take place 
or not.  Other scenarios have been proposed in the past ( since 1992) but 
they never happened. Once they were going to have a tiered system with PCs, 
UNIX servers, and mainframes using C++, but they finally decided that they 
could not afford that architecture.  Don't ask how many millions were spent 
before they made that decision. Another proposal was to use SAP but they 
have abandoned that idea, at least for our stuff.  SAP just does not provide 
the functionality of our area's applications.  Some other groups will use 
SAP but in some cases where SAP functionality is appropriate the existing 
software currently processes transactions at a rate that may be  a problem 
for SAP to match. The whole thing is a lot bigger than just the area that I 
work in, which is just a small part of the overall system. One goal seems to 
be to be able to say that we have modernized and no longer use COBOL.  The 
guy in charge now (and their have been many others in the past) says that he 
asks this question: " If we were to build this system from scratch today 
would we use COBOL?"  Of course the guy he is asking does not know COBOL so 
the answer is "no".  I am afraid that they plan to use the existing programs 
as a basis for writing specifications for the new programs.  In fact, that 
is how I know that they don't know COBOL because they want us to write the 
specifications for them (them is a large contractor consortium).  The 
existing system was developed over a 20 year plus time frame but they want 
to replace it in a time frame much shorter than that.  I often hear things 
like "if we had x million dollars more we could cut the development by y 
years".  The existing system was evaluated by GAO in the past and four major 
deficiencies were found.  All of these deficiencies were fixed during the 
Y2K process.  This included Y2K dates and replacing an in house, unstable 
telecommunication facility with IBM's MQM and thus resolving issues of 
scalability.  We are currently undergoing our second reorganization this 
year and that does not count becoming part of the Department of Homeland 
Security last year. So as you can see the situation is very fluid.

>
> You have alot of things changing at once.  It might be a good time to
…[8 more quoted lines elided]…
>

<snip>
```

###### ↳ ↳ ↳ Re: cics, db2, sql question

- **From:** docdwarf@panix.com
- **Date:** 2005-06-16T20:30:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d8t5ih$s1o$1@panix5.panix.com>`
- **References:** `<58bc3$42b0ad7f$43f2931b$2714@DIALUPUSA.NET> <joe_zitzelberger-BBD22B.02581516062005@ispnews.usenetserver.com> <80d7a$42b20eda$43f2936d$10296@DIALUPUSA.NET>`

```
In article <80d7a$42b20eda$43f2936d$10296@DIALUPUSA.NET>,
charles hottel <jghottel@yahoo.com> wrote:

[snip]

>Once they were going to have a tiered system with PCs, 
>UNIX servers, and mainframes using C++, but they finally decided that they 
>could not afford that architecture.

[snip]

>Another proposal was to use SAP but they 
>have abandoned that idea, at least for our stuff.

Seems like they've been members of the Flavor Of The Month Club, aye.

>The 
>guy in charge now (and their have been many others in the past) says that he 
>asks this question: " If we were to build this system from scratch today 
>would we use COBOL?"  Of course the guy he is asking does not know COBOL so 
>the answer is "no".

The response of 'For what reason(s)?' was not asked, I noticed.

[snip]

>I often hear things 
>like "if we had x million dollars more we could cut the development by y 
>years".

A response might be 'If you had nine women working for one month could you 
make a baby, too?'

>We are currently undergoing our second reorganization this 
>year and that does not count becoming part of the Department of Homeland 
>Security last year. So as you can see the situation is very fluid.

I recall a Dilbert strip about the 'Bungee Boss'.

DD
```

###### ↳ ↳ ↳ Re: cics, db2, sql question

_(reply depth: 4)_

- **From:** Jeff York <ralf4@btinternet.com>
- **Date:** 2005-06-17T10:09:48+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pn45b19r507cb6s18ub0vtpjhvmttvd0is@4ax.com>`
- **References:** `<58bc3$42b0ad7f$43f2931b$2714@DIALUPUSA.NET> <joe_zitzelberger-BBD22B.02581516062005@ispnews.usenetserver.com> <80d7a$42b20eda$43f2936d$10296@DIALUPUSA.NET> <d8t5ih$s1o$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:

>In article <80d7a$42b20eda$43f2936d$10296@DIALUPUSA.NET>,
>charles hottel <jghottel@yahoo.com> wrote:
>
>[snip]

>>I often hear things 
>>like "if we had x million dollars more we could cut the development by y 
…[3 more quoted lines elided]…
>make a baby, too?'

Reminds me of the old definition of an "IBM Man-Year"... "500 blokes
trying to get something finished before lunch".  :-)
```

###### ↳ ↳ ↳ Re: cics, db2, sql question

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2005-06-17T05:19:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d8u4ir$9du$1@panix5.panix.com>`
- **References:** `<58bc3$42b0ad7f$43f2931b$2714@DIALUPUSA.NET> <80d7a$42b20eda$43f2936d$10296@DIALUPUSA.NET> <d8t5ih$s1o$1@panix5.panix.com> <pn45b19r507cb6s18ub0vtpjhvmttvd0is@4ax.com>`

```
In article <pn45b19r507cb6s18ub0vtpjhvmttvd0is@4ax.com>,
Jeff York  <ralf4@btinternet.com> wrote:
>docdwarf@panix.com wrote:
>
…[13 more quoted lines elided]…
>trying to get something finished before lunch".  :-)

In a similar vein, aye... the one about nine women-months making a baby 
has been around for at least forty years or so, one day it might become 
well-known.

DD
```

###### ↳ ↳ ↳ Re: cics, db2, sql question

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-06-18T00:14:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3hft4hFgrr3mU1@individual.net>`
- **References:** `<58bc3$42b0ad7f$43f2931b$2714@DIALUPUSA.NET> <80d7a$42b20eda$43f2936d$10296@DIALUPUSA.NET> <d8t5ih$s1o$1@panix5.panix.com> <pn45b19r507cb6s18ub0vtpjhvmttvd0is@4ax.com> <d8u4ir$9du$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:d8u4ir$9du$1@panix5.panix.com...
> In article <pn45b19r507cb6s18ub0vtpjhvmttvd0is@4ax.com>,
> Jeff York  <ralf4@btinternet.com> wrote:
…[8 more quoted lines elided]…
> >>>like "if we had x million dollars more we could cut the development by
y
> >>>years".
> >>
> >>A response might be 'If you had nine women working for one month could
you
> >>make a baby, too?'
> >
…[8 more quoted lines elided]…
>
I enjoyed Jeff's definition of IBM man year, and your definition of women
months. Never heard either before. The one I use, I acquired from an old,
much loved IT mentor now sadly, departed.

"If one ship can cross the ocean in three days, why can't three ships cross
it in one day..."

Although it is weaker than the other two, I'll probably retain it out of
respect for the operson who gave it to me.. :-)

Pete
```

###### ↳ ↳ ↳ Re: cics, db2, sql question

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2005-06-17T09:07:28-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d8uhug$4i0$1@panix5.panix.com>`
- **References:** `<58bc3$42b0ad7f$43f2931b$2714@DIALUPUSA.NET> <pn45b19r507cb6s18ub0vtpjhvmttvd0is@4ax.com> <d8u4ir$9du$1@panix5.panix.com> <3hft4hFgrr3mU1@individual.net>`

```
In article <3hft4hFgrr3mU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:d8u4ir$9du$1@panix5.panix.com...

[snip]

>> In a similar vein, aye... the one about nine women-months making a baby
>> has been around for at least forty years or so, one day it might become
…[3 more quoted lines elided]…
>months. Never heard either before.

I believe the nine women-months has been attributed to Werhner von Braun; 
see http://en.wikiquote.org/wiki/Wernher_von_Braun :

--begin quoted text:

Crash programs fail because they are based on theory that, with nine women 
pregnant, you can get a baby a month. 

--end quoted text

DD
```

##### ↳ ↳ Re: cics, db2, sql question

- **From:** "charles hottel" <jghottel@yahoo.com>
- **Date:** 2005-06-16T19:44:28-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5938c$42b20edc$43f2936d$10296@DIALUPUSA.NET>`
- **References:** `<58bc3$42b0ad7f$43f2931b$2714@DIALUPUSA.NET> <joe_zitzelberger-BBD22B.02581516062005@ispnews.usenetserver.com>`

```
Joe,

Thanks I will check out the application programmer guide.

One comment below.

"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote in message
news:joe_zitzelberger-BBD22B.02581516062005@ispnews.usenetserver.com...
> IIRC the book you quote was based on DB2 v2.1 or maybe v4.x -- either is
> a long dead version.
…[10 more quoted lines elided]…
> like an http server that can maintain those states for you?

Actually I do not know what the exact environment will be.  My best guess
would be an http server. I am not 100% certain whether this will take place
or not.  Other scenarios have been proposed in the past ( since 1992) but
they never happened. Once they were going to have a tiered system with PCs,
UNIX servers, and mainframes using C++, but they finally decided that they
could not afford that architecture.  Don't ask how many millions were spent
before they made that decision. Another proposal was to use SAP but they
have abandoned that idea, at least for our stuff.  SAP just does not provide
the functionality of our area's applications.  Some other groups will use
SAP but in some cases where SAP functionality is appropriate the existing
software currently processes transactions at a rate that may be  a problem
for SAP to match. The whole thing is a lot bigger than just the area that I
work in, which is just a small part of the overall system. One goal seems to
be to be able to say that we have modernized and no longer use COBOL.  The
guy in charge now (and their have been many others in the past) says that he
asks this question: " If we were to build this system from scratch today
would we use COBOL?"  Of course the guy he is asking does not know COBOL so
the answer is "no".  I am afraid that they plan to use the existing programs
as a basis for writing specifications for the new programs.  In fact, that
is how I know that they don't know COBOL because they want us to write the
specifications for them (them is a large contractor consortium).  The
existing system was developed over a 20 year plus time frame but they want
to replace it in a time frame much shorter than that.  I often hear things
like "if we had x million dollars more we could cut the development by y
years".  The existing system was evaluated by GAO in the past and four major
deficiencies were found.  All of these deficiencies were fixed during the
Y2K process.  This included Y2K dates and replacing an in house, unstable
telecommunication facility with IBM's MQM and thus resolving issues of
scalability.  We are currently undergoing our second reorganization this
year and that does not count becoming part of the Department of Homeland
Security last year. So as you can see the situation is very fluid.

>
> You have alot of things changing at once.  It might be a good time to
…[8 more quoted lines elided]…
>

<snip>
```

#### ↳ Re: cics, db2, sql question

- **From:** bo774@FreeNet.Carleton.CA (Kelly Bert Manning)
- **Date:** 2005-06-18T16:32:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d91ib4$1ro$1@theodyn.ncf.ca>`
- **References:** `<58bc3$42b0ad7f$43f2931b$2714@DIALUPUSA.NET>`

```

"charles hottel" (jghottel@yahoo.com) writes:
> We currently use CICS, DatacommDB and COBOL.  Management is contemplating 
> moving to DB2 and Java and SQL. I have no DB2  or Java experience and only a 
…[11 more quoted lines elided]…
> "when a pseudo conversational program ends DB2 drops the result table"

DB2 v8 introduced Materialized query tables which can be refreshed
under application control, but they seem to be intended for Decision 
Support Queries where data currency isn't critical.
 
In any case why use a large result table, rather than using MIN or MAX
and a singleton select for each row you want to display?

Column functions can be a recipie for an RDBMS performance disaster, eg. 
YEAR of date BETWEEN low AND high, but MAX and MIN are documented as
being indexable.

That is, get the lowest key with a 1 fetch access using MIN, then another
1 fetch access for the MIN key value  higher than that, until your screen
is full. DB2 will probably be doing found in buffer I/O for all of the
selects.

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/dsnapj11/6.4.3.2.6?SHELF=&DT=20040923112201&CASE=
   "6.4.3.2.6 One-fetch access (ACCESSTYPE=I1)
    ...
    Queries using one-fetch index access: Assuming that an index
    exists on T(C1,C2,C3), the following queries use one-fetch index scan: 
    SELECT MIN(C1) FROM T;
    SELECT MIN(C1) FROM T WHERE C1>5;"
 
The literal value 5 could be replaced with a host variable value retrieved
in the first select, or with a value saved to record to record the key 
values associated with a previous transaction's output.
```

##### ↳ ↳ Re: cics, db2, sql question

- **From:** "charles hottel" <jghottel@yahoo.com>
- **Date:** 2005-06-18T20:55:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49e1e$42b4c286$43f9c2af$26782@DIALUPUSA.NET>`
- **References:** `<58bc3$42b0ad7f$43f2931b$2714@DIALUPUSA.NET> <d91ib4$1ro$1@theodyn.ncf.ca>`

```
Thanks. I think I need to read the DB2 Programmers guide because the book I 
read is out of date. I would think that  only querying 17 to 20 records at a 
time would not cause too much overhead.  However I am no DB2 expert and DB2 
seems to have a lot of different locks and I do not yet understand them all 
completely.


"Kelly Bert Manning" <bo774@FreeNet.Carleton.CA> wrote in message 
news:d91ib4$1ro$1@theodyn.ncf.ca...
>
<snip>
>
> DB2 v8 introduced Materialized query tables which can be refreshed
…[25 more quoted lines elided]…
> values associated with a previous transaction's output.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
