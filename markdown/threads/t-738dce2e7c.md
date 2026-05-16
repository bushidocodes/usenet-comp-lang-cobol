[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Converting Cobol programs to pl/sql procedures or pakages

_18 messages · 5 participants · 2009-07_

**Topics:** [`Migration and conversion`](../topics.md#migration) · [`Databases and SQL`](../topics.md#databases)

---

### Converting Cobol programs to pl/sql procedures or pakages

- **From:** jmoore <jmoore207@gmail.com>
- **Date:** 2009-07-16T11:31:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43915d44-2d96-45d9-889a-f5b15f9ee463@y7g2000yqa.googlegroups.com>`

```
Does anyone have any example code of Cobol programs that were
converted to PL/sql procedures/packages? Our company is trying to
convert programs to pl/sql and they really haven't addressed many of
the challenges. First being batch programs that display/accept data
from the user. Our software runs thru a .net front end or batch
programs can be ran from a unix prompt. I have limited time to learn
this and other than reading books, I cuold use some great examples
that I could see what the Cobol program looks like and what the pl/sql
program lloks like. Even if it is a Cobol program that calls a
procedure would be great Any help would be greatly appreciated.
```

#### ↳ Re: Converting Cobol programs to pl/sql procedures or pakages

- **From:** docdwarf@panix.com ()
- **Date:** 2009-07-16T18:48:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h3nslo$hud$1@reader1.panix.com>`
- **References:** `<43915d44-2d96-45d9-889a-f5b15f9ee463@y7g2000yqa.googlegroups.com>`

```
In article <43915d44-2d96-45d9-889a-f5b15f9ee463@y7g2000yqa.googlegroups.com>,
jmoore  <jmoore207@gmail.com> wrote:
>Does anyone have any example code of Cobol programs that were
>converted to PL/sql procedures/packages? Our company is trying to
>convert programs to pl/sql and they really haven't addressed many of
>the challenges.

Depending on the application(s) involved and the data volume this can be a 
moderately intricate task; there are Conversion Companies which have 
entire divisions dedicated to just such efforts.

>First being batch programs that display/accept data
>from the user. Our software runs thru a .net front end or batch
…[3 more quoted lines elided]…
>program lloks like.

Let me get this straight... your company has given you an assignment to do 
something that you have not yet learned and must complete in a very 
limited time?

I would start by polishing up my resume and preparing to find another 
employer.  Without knowledge of both the (from) side and the (to) side the 
likelihood of success is, in my experience, diminished.

DD
```

##### ↳ ↳ Re: Converting Cobol programs to pl/sql procedures or pakages

- **From:** jmoore <jmoore207@gmail.com>
- **Date:** 2009-07-16T12:04:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c211947d-80fb-4784-bbcb-93a48ea029b9@k30g2000yqf.googlegroups.com>`
- **References:** `<43915d44-2d96-45d9-889a-f5b15f9ee463@y7g2000yqa.googlegroups.com> <h3nslo$hud$1@reader1.panix.com>`

```
On Jul 16, 2:48 pm, docdw...@panix.com () wrote:
> In article <43915d44-2d96-45d9-889a-f5b15f9ee...@y7g2000yqa.googlegroups.com>,
>
…[25 more quoted lines elided]…
> DD

You got it straight and it is very ridiculous! They haven't really
ironed out all the pitfalls that go along with converting these
programs or the fact that it may not be as effiecient if they are
going to store everything in procedures/packages. Some genius thought
let's convert to PL/sql and that was it. I have been reading up on pl/
sql and have a few poor examples already done here. But, if they want
all cobol programs whether batch or online converted, I really could
use a good example of how to structure the pl/sql. Loops etc to handle
how Cobol is looping thru the table now and exceptions that would make
it go back and read the next record. Also, we have many sort
routines.
```

###### ↳ ↳ ↳ Re: Converting Cobol programs to pl/sql procedures or pakages

- **From:** docdwarf@panix.com ()
- **Date:** 2009-07-16T22:42:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h3oad8$q3$1@reader1.panix.com>`
- **References:** `<43915d44-2d96-45d9-889a-f5b15f9ee463@y7g2000yqa.googlegroups.com> <h3nslo$hud$1@reader1.panix.com> <c211947d-80fb-4784-bbcb-93a48ea029b9@k30g2000yqf.googlegroups.com>`

```
In article <c211947d-80fb-4784-bbcb-93a48ea029b9@k30g2000yqf.googlegroups.com>,
jmoore  <jmoore207@gmail.com> wrote:
>On Jul 16, 2:48?pm, docdw...@panix.com () wrote:

[snip]

>> Let me get this straight... your company has given you an assignment to do
>> something that you have not yet learned and must complete in a very
…[3 more quoted lines elided]…
>> employer. 

[snip]

>You got it straight and it is very ridiculous!

Sometimes I just guess lucky... now, get to polishing.

DD
```

###### ↳ ↳ ↳ Re: Converting Cobol programs to pl/sql procedures or pakages

_(reply depth: 4)_

- **From:** jmoore <jmoore207@gmail.com>
- **Date:** 2009-07-28T06:59:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e299e138-392b-4659-9d37-d76fcc6a340a@z34g2000vbl.googlegroups.com>`
- **References:** `<43915d44-2d96-45d9-889a-f5b15f9ee463@y7g2000yqa.googlegroups.com> <h3nslo$hud$1@reader1.panix.com> <c211947d-80fb-4784-bbcb-93a48ea029b9@k30g2000yqf.googlegroups.com> <h3oad8$q3$1@reader1.panix.com>`

```
On Jul 16, 6:42 pm, docdw...@panix.com () wrote:
> In article <c211947d-80fb-4784-bbcb-93a48ea02...@k30g2000yqf.googlegroups.com>,
>
…[18 more quoted lines elided]…
> DD

Anyone? Anyone? Bueler? Bueler?
```

###### ↳ ↳ ↳ Re: Converting Cobol programs to pl/sql procedures or pakages

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-07-28T15:02:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h4n3tg$rte$1@reader1.panix.com>`
- **References:** `<43915d44-2d96-45d9-889a-f5b15f9ee463@y7g2000yqa.googlegroups.com> <c211947d-80fb-4784-bbcb-93a48ea029b9@k30g2000yqf.googlegroups.com> <h3oad8$q3$1@reader1.panix.com> <e299e138-392b-4659-9d37-d76fcc6a340a@z34g2000vbl.googlegroups.com>`

```
In article <e299e138-392b-4659-9d37-d76fcc6a340a@z34g2000vbl.googlegroups.com>,
jmoore  <jmoore207@gmail.com> wrote:
>On Jul 16, 6:42?pm, docdw...@panix.com () wrote:
>> In article
…[20 more quoted lines elided]…
>Anyone? Anyone? Bueler? Bueler?

Oh, I *cannot* resist... I'm not sure... there aren't multiple consonants 
or any -zy- combinations; Bueler would seem to be of more western-European 
derivation...

... than one resulting from Polish-ing.

DD
```

###### ↳ ↳ ↳ Re: Converting Cobol programs to pl/sql procedures or pakages

_(reply depth: 6)_

- **From:** jmoore <jmoore207@gmail.com>
- **Date:** 2009-07-28T09:42:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4a1e8a66-23ba-4b04-94ad-0c33015e291b@q35g2000vbi.googlegroups.com>`
- **References:** `<43915d44-2d96-45d9-889a-f5b15f9ee463@y7g2000yqa.googlegroups.com> <c211947d-80fb-4784-bbcb-93a48ea029b9@k30g2000yqf.googlegroups.com> <h3oad8$q3$1@reader1.panix.com> <e299e138-392b-4659-9d37-d76fcc6a340a@z34g2000vbl.googlegroups.com> <h4n3tg$rte$1@reader1.panix.com>`

```
On Jul 28, 11:02 am, docdw...@panix.com () wrote:
> In article <e299e138-392b-4659-9d37-d76fcc6a3...@z34g2000vbl.googlegroups.com>,
>
…[37 more quoted lines elided]…
> - Show quoted text -

You seem to be the only one answering any posts in here. Clever as you
are with the whole polish-ing thing I could really use some feedback
from anyone else who has been through this ridiculous exercise of
moving from Cobol to PL-SQL.
```

###### ↳ ↳ ↳ Re: Converting Cobol programs to pl/sql procedures or pakages

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-07-28T17:25:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h4nc9g$3kp$1@reader1.panix.com>`
- **References:** `<43915d44-2d96-45d9-889a-f5b15f9ee463@y7g2000yqa.googlegroups.com> <e299e138-392b-4659-9d37-d76fcc6a340a@z34g2000vbl.googlegroups.com> <h4n3tg$rte$1@reader1.panix.com> <4a1e8a66-23ba-4b04-94ad-0c33015e291b@q35g2000vbi.googlegroups.com>`

```
In article <4a1e8a66-23ba-4b04-94ad-0c33015e291b@q35g2000vbi.googlegroups.com>,
jmoore  <jmoore207@gmail.com> wrote:
>On Jul 28, 11:02?am, docdw...@panix.com () wrote:
>> In article
…[12 more quoted lines elided]…
>> >> >> limited time?

[snip]

>> >> >You got it straight and it is very ridiculous!

[snip]

>You seem to be the only one answering any posts in here. Clever as you
>are with the whole polish-ing thing I could really use some feedback
>from anyone else who has been through this ridiculous exercise of
>moving from Cobol to PL-SQL.

The exercise is not necessarily ridiculous; a few of the folks posting 
here, I believe, have some experience moving from a file-based system to a 
table-based one.  It is not a trivial thing to do and there are companies 
which employ very experienced people to make sure the transition is 
successful.

To entrust it to someone who knows little about it indicates - at least 
according to my minimal experience - that Someone Important wants to see 
it fail.  Try not to take it personally.

DD
```

###### ↳ ↳ ↳ Re: Converting Cobol programs to pl/sql procedures or pakages

_(reply depth: 8)_

- **From:** jmoore <jmoore207@gmail.com>
- **Date:** 2009-07-28T10:40:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<27ac8c36-9fa8-4382-8433-dee2a2fa0a66@z28g2000vbl.googlegroups.com>`
- **References:** `<43915d44-2d96-45d9-889a-f5b15f9ee463@y7g2000yqa.googlegroups.com> <e299e138-392b-4659-9d37-d76fcc6a340a@z34g2000vbl.googlegroups.com> <h4n3tg$rte$1@reader1.panix.com> <4a1e8a66-23ba-4b04-94ad-0c33015e291b@q35g2000vbi.googlegroups.com> <h4nc9g$3kp$1@reader1.panix.com>`

```
On Jul 28, 1:25 pm, docdw...@panix.com () wrote:
> In article <4a1e8a66-23ba-4b04-94ad-0c33015e2...@q35g2000vbi.googlegroups.com>,
>
…[44 more quoted lines elided]…
> - Show quoted text -

You may be right DD. or it may be just another assinine decision this
company is famous for. All I know is I want to get some experience
before our dept is thrown out the door. I think it would be awesome if
they hired someone experience moving from a file-based system to a
table-based one. That is why I came in here hoping to find someone who
may have some examples that might help me/us get started. Kind of hard
not to take it personally, when you have mouths to feed. I didn't come
in here to be a jerk, just looking for some help that's all.
```

###### ↳ ↳ ↳ Re: Converting Cobol programs to pl/sql procedures or pakages

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-07-28T18:17:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h4nfbs$nnm$1@reader1.panix.com>`
- **References:** `<43915d44-2d96-45d9-889a-f5b15f9ee463@y7g2000yqa.googlegroups.com> <4a1e8a66-23ba-4b04-94ad-0c33015e291b@q35g2000vbi.googlegroups.com> <h4nc9g$3kp$1@reader1.panix.com> <27ac8c36-9fa8-4382-8433-dee2a2fa0a66@z28g2000vbl.googlegroups.com>`

```
In article <27ac8c36-9fa8-4382-8433-dee2a2fa0a66@z28g2000vbl.googlegroups.com>,
jmoore  <jmoore207@gmail.com> wrote:
>On Jul 28, 1:25?pm, docdw...@panix.com () wrote:

[snip]

>> The exercise is not necessarily ridiculous; a few of the folks posting
>> here, I believe, have some experience moving from a file-based system to a
…[10 more quoted lines elided]…
>before our dept is thrown out the door.

It is one thing to want experience, it is another thing to want someone to 
part with the valuable skills and hard-earned lessons they've garnerd o'er 
the long decades - and by which they earn their living - to part with it 
for free.


>I think it would be awesome if
>they hired someone experience moving from a file-based system to a
>table-based one.

Until they do... they get what they pay for.

>That is why I came in here hoping to find someone who
>may have some examples that might help me/us get started.

I've tried to do just that but it seems to be in a direction other than 
that which you expected.  Funny how that works, especially with something 
you don't know, eh?

>Kind of hard
>not to take it personally, when you have mouths to feed.

So do others here, if only their own.

DD
```

###### ↳ ↳ ↳ Re: Converting Cobol programs to pl/sql procedures or pakages

_(reply depth: 9)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2009-07-28T14:41:42-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<boJbm.46219$nL7.21769@newsfe18.iad>`
- **In-Reply-To:** `<27ac8c36-9fa8-4382-8433-dee2a2fa0a66@z28g2000vbl.googlegroups.com>`
- **References:** `<43915d44-2d96-45d9-889a-f5b15f9ee463@y7g2000yqa.googlegroups.com> <e299e138-392b-4659-9d37-d76fcc6a340a@z34g2000vbl.googlegroups.com> <h4n3tg$rte$1@reader1.panix.com> <4a1e8a66-23ba-4b04-94ad-0c33015e291b@q35g2000vbi.googlegroups.com> <h4nc9g$3kp$1@reader1.panix.com> <27ac8c36-9fa8-4382-8433-dee2a2fa0a66@z28g2000vbl.googlegroups.com>`

```
jmoore wrote:
> On Jul 28, 1:25 pm, docdw...@panix.com () wrote:
> 
>>In article <4a1e8a66-23ba-4b04-94ad-0c33015e2...@q35g2000vbi.googlegroups.com>,

<snip>
> 
> You may be right DD. or it may be just another assinine decision this
…[6 more quoted lines elided]…
> in here to be a jerk, just looking for some help that's all.

jmoore,

Not sure if I have read you correctly, but do you know little or nothing 
about SQL ?

Like any new activity in this game, you have got to do some reading. SQL 
((R)DBMS or DBMS) is adequately covered by paperback texts; of course 
you can always shell out for the expensive hard-cover tomes. Perhaps 
some of those familiar can recommend texts that you should look at.

As regards syntax, go googling and you'll find interesting examples 
which may appeal to your particular requirement. Surprisingly, a 
PC-user, I found that the IBM site(s) have very good examples of SQL 
syntax using COBOL. Granted it probably is all based on DB2 and some 
'VERBs' you may not be able to use with your particular SQL Preprocessor 
- nevertheless you can probably do a fair amount of 'cut and paste' from 
their examples, obviously changing COBOL variable names.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Converting Cobol programs to pl/sql procedures or pakages

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-07-29T20:47:50+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7daglpF2as6eiU1@mid.individual.net>`
- **References:** `<43915d44-2d96-45d9-889a-f5b15f9ee463@y7g2000yqa.googlegroups.com> <e299e138-392b-4659-9d37-d76fcc6a340a@z34g2000vbl.googlegroups.com> <h4n3tg$rte$1@reader1.panix.com> <4a1e8a66-23ba-4b04-94ad-0c33015e291b@q35g2000vbi.googlegroups.com> <h4nc9g$3kp$1@reader1.panix.com> <27ac8c36-9fa8-4382-8433-dee2a2fa0a66@z28g2000vbl.googlegroups.com>`

```
jmoore wrote:
> On Jul 28, 1:25 pm, docdw...@panix.com () wrote:
>> In article
…[58 more quoted lines elided]…
> in here to be a jerk, just looking for some help that's all.

Fair enough. But please understand that there is a time and a place for free 
advice.

The problem here is that you have been asked to do something that your 
company should be paying for, and some of the people in this forum are the 
people who would be paid by them. Even with the kindest hearts in the world, 
this one goes against the grain...:-)

Nevertheless, moved by your situation, I'll try and help.

If you know absolutely nothing about SQL you can learn it pretty quickly 
from: http://www.w3schools.com/SQl/default.asp

By "quickly" I mean "in an afternoon" (Compared to other "languages", SQL 
has a limited command set and derives its power from being able to be 
recursively structured (that's what the "S" stands for in the name...)

PL/SQL is SQL on steroids.  Once you have mastered the basic SQL, given you 
have a programming background, the loop control and evaluations available in 
PL/SQL shouldn't be too difficult.

In the same way any computer program can be decomposed into "sequence", 
"evaluate" and "iterate" so PL/SQL has constructs to support all of these 
functions.

Why not take a small COBOL program (with a simple record layout) and analyse 
it along those lines, then apply the equivalent PL/SQL constructs and see 
what you end up with? You said you want to get experience at this, I can see 
no better way. If you tell your Boss you're doing a pilot "proof of concept" 
that should get him off your back long enough for you to successfully 
complete your first conversion.

Understand that there is a difference between the way in which flat files 
and COBOL perceive data and the way the Relational Database (ORACLE or any 
other) does. For your first cut, try and avoid a record layout that contains 
OCCURS and REDEFINES.  Fields defined as group levels in COBOL may or may 
not be needed on the database, depending on whether they are referenced 
frequently in code.

I have written at length about all of this and there are free articles you 
can browse from the cobol21 web site. The ISAM to RDB page is still 
incomplete, but there is a wealth of information on the PRIMA Toolset page.
(http://primacomputing.co.nz/cobol21/PRIMAToolset.aspx)

The "Pathway to Relational Database" document (click on the link just below 
the image of the Arctic winter...) has full explanations and an appendix 
that explains DB Normalization in very simple terms. I came to grips with 
all of these problems when I was building tools to automate the conversion 
from flat files to RDB, but whether you use the tools or not, the 
explanations will, hopefully, be useful. (You might at least get enough 
ammunition to persuade your employers that they need someone knowledgable to 
assist with this, even if for a few days...) Once you have a fair grasp of 
what is involved generally, conversion to PL/SQL becomes just a "special 
case", where the RDB is "smarter" than would normally be the case.

Starting with no knowledge of RDB or SQL is not a good position to be in but 
the task is not impossible. Give yourself a few days for "education" and 
read avidly. There is a great deal of material available and part of the 
difficulty is deciding what is relevant and what is not, for your particular 
purposes.

I tried a quick GOOGLE using "COBOL to PL/SQL" and received over a million 
hits, some of which looked very pertinent. There are companies who have 
automated this process (much as I have done with standard RDB) and I'm sure 
you can get the assistance you need, if your company is prepared to pay for 
it.

Good Luck!

Pete.
```

###### ↳ ↳ ↳ Re: Converting Cobol programs to pl/sql procedures or pakages

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-07-29T20:56:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7dah6oF2bmbjiU1@mid.individual.net>`
- **References:** `<43915d44-2d96-45d9-889a-f5b15f9ee463@y7g2000yqa.googlegroups.com> <e299e138-392b-4659-9d37-d76fcc6a340a@z34g2000vbl.googlegroups.com> <h4n3tg$rte$1@reader1.panix.com> <4a1e8a66-23ba-4b04-94ad-0c33015e291b@q35g2000vbi.googlegroups.com> <h4nc9g$3kp$1@reader1.panix.com> <27ac8c36-9fa8-4382-8433-dee2a2fa0a66@z28g2000vbl.googlegroups.com> <7daglpF2as6eiU1@mid.individual.net>`

```
Pete Dashwood wrote:
<snip>

> I have written at length about all of this and there are free
> articles you can browse from the cobol21 web site. The ISAM to RDB
> page is still incomplete, but there is a wealth of information on the
> PRIMA Toolset page.
> (http://primacomputing.co.nz/cobol21/PRIMAToolset.aspx)
The above link is correct but doesn't seem to work from within the post. It 
may be the parentheses...

Try this...

http://primacomputing.co.nz/cobol21/PRIMAToolset.aspx

Pete
```

###### ↳ ↳ ↳ Re: Converting Cobol programs to pl/sql procedures or pakages

_(reply depth: 11)_

- **From:** jmoore <jmoore207@gmail.com>
- **Date:** 2009-07-29T03:49:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fb5d61a7-83fa-4e43-bd58-90c35de8a83a@a26g2000yqn.googlegroups.com>`
- **References:** `<43915d44-2d96-45d9-889a-f5b15f9ee463@y7g2000yqa.googlegroups.com> <e299e138-392b-4659-9d37-d76fcc6a340a@z34g2000vbl.googlegroups.com> <h4n3tg$rte$1@reader1.panix.com> <4a1e8a66-23ba-4b04-94ad-0c33015e291b@q35g2000vbi.googlegroups.com> <h4nc9g$3kp$1@reader1.panix.com> <27ac8c36-9fa8-4382-8433-dee2a2fa0a66@z28g2000vbl.googlegroups.com> <7daglpF2as6eiU1@mid.individual.net> <7dah6oF2bmbjiU1@mid.individual.net>`

```
On Jul 29, 4:56 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Pete Dashwood wrote:
>
…[17 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."

I will check them all out! Thanks everyone for your help. We have been
embedded sql in alot of our cobol programs(Pro*Cobol), I think the
issue is how to do multiple cursors for or while loops etc. We have an
example program that does a sort and returns a report. The sort
basically takes table 1 reads until eof and then uses the mbrno to
read table 2 to get a few fields, then table 3 to get a few fields
releases the sort-rec and goes back to table 1. When done The return
reads sort and creates a report. We have many batch programs that do
this. I am keeping the cobol part to accept/display. I need to pass
the answers as variables to throw records away I do not need. I am
trying to figure out how to combine all 3 in the cursors and order by
the sort-key which is circuit and station then create the report all
inside a package or procedure. I have been reading pl/sql manuals
trying to figure out the best way to accomplish this. They seem to not
wnat us to use any temporary tables here. I know oracle has the utl-
file package and wasn't sure if I can use that. Maybe combine all the
cursors and do a hash group by. There are quite a few infastructure
issues that need to be worked out as well. Let me finish by saying I
really appreciate everyone's guidance here. I totally understand that
all of you have worked hard to attain your knowledge and to part with
it for free doesn't do you any favors. Unfortunately, with the job
market the way it is, I have to learn this fast. Without going into
detail the VP of development here has "farmed" out the pl/sql to India
and all of the sudden now the owner wants us to know it. So our whole
department, which has been promised to get training is now on its own.
There are alot of us who only know cobol here and I believe they
definitely want to get rid of Cobol. SO, DD you were right somebody
does want "us" to fail. But the "us" is the Cobol department. Pete,
James, DD thanks for your input! I wish I could go into more detail
about what is going on, but it wouldn't be politically correct.
```

###### ↳ ↳ ↳ Re: Converting Cobol programs to pl/sql procedures or pakages

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-07-29T13:05:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h4pheb$j7n$2@reader1.panix.com>`
- **References:** `<43915d44-2d96-45d9-889a-f5b15f9ee463@y7g2000yqa.googlegroups.com> <7daglpF2as6eiU1@mid.individual.net> <7dah6oF2bmbjiU1@mid.individual.net> <fb5d61a7-83fa-4e43-bd58-90c35de8a83a@a26g2000yqn.googlegroups.com>`

```
In article <fb5d61a7-83fa-4e43-bd58-90c35de8a83a@a26g2000yqn.googlegroups.com>,
jmoore  <jmoore207@gmail.com> wrote:

[snip]

>SO, DD you were right somebody
>does want "us" to fail.

I was right about something?  Quick, someone mark the calendar.

DD
```

###### ↳ ↳ ↳ Re: Converting Cobol programs to pl/sql procedures or pakages

_(reply depth: 11)_

- **From:** jmoore <jmoore207@gmail.com>
- **Date:** 2009-07-29T03:54:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<725ac0a7-14c7-488b-8e32-f96f1edc498e@h21g2000yqa.googlegroups.com>`
- **References:** `<43915d44-2d96-45d9-889a-f5b15f9ee463@y7g2000yqa.googlegroups.com> <e299e138-392b-4659-9d37-d76fcc6a340a@z34g2000vbl.googlegroups.com> <h4n3tg$rte$1@reader1.panix.com> <4a1e8a66-23ba-4b04-94ad-0c33015e291b@q35g2000vbi.googlegroups.com> <h4nc9g$3kp$1@reader1.panix.com> <27ac8c36-9fa8-4382-8433-dee2a2fa0a66@z28g2000vbl.googlegroups.com> <7daglpF2as6eiU1@mid.individual.net> <7dah6oF2bmbjiU1@mid.individual.net>`

```
On Jul 29, 4:56 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Pete Dashwood wrote:
>
…[17 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."

I bookmarked your site Pete!
```

###### ↳ ↳ ↳ Re: Converting Cobol programs to pl/sql procedures or pakages

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-07-30T01:16:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7db0dcF2ai115U1@mid.individual.net>`
- **References:** `<43915d44-2d96-45d9-889a-f5b15f9ee463@y7g2000yqa.googlegroups.com> <e299e138-392b-4659-9d37-d76fcc6a340a@z34g2000vbl.googlegroups.com> <h4n3tg$rte$1@reader1.panix.com> <4a1e8a66-23ba-4b04-94ad-0c33015e291b@q35g2000vbi.googlegroups.com> <h4nc9g$3kp$1@reader1.panix.com> <27ac8c36-9fa8-4382-8433-dee2a2fa0a66@z28g2000vbl.googlegroups.com> <7daglpF2as6eiU1@mid.individual.net> <7dah6oF2bmbjiU1@mid.individual.net> <725ac0a7-14c7-488b-8e32-f96f1edc498e@h21g2000yqa.googlegroups.com>`

```
jmoore wrote:
> On Jul 29, 4:56 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[21 more quoted lines elided]…
> I bookmarked your site Pete!

Thank you. :-)  (Always music to a Webmaster's ears... :-))

I hope you are able to get some benefit from looking at what's on it. I 
REALLY need to get this site completed but I'm just too busy at the moment. 
The next priority is the ISAM to RDB page and I hope to get onto finishing 
that in a week or so. Most of the nitty-gritty material is already on the 
Toolset page quoted above, but I have some more general "beginner 
background" and some better pictures to add, which are quite independent of 
the Toolset.

Pete.
```

###### ↳ ↳ ↳ Re: Converting Cobol programs to pl/sql procedures or pakages

_(reply depth: 13)_

- **From:** ribjo <ribeirolog@gmail.com>
- **Date:** 2009-07-30T02:57:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<82df9e18-8e58-4fe3-ba77-2cf0051fc5ed@n11g2000yqb.googlegroups.com>`
- **References:** `<43915d44-2d96-45d9-889a-f5b15f9ee463@y7g2000yqa.googlegroups.com> <e299e138-392b-4659-9d37-d76fcc6a340a@z34g2000vbl.googlegroups.com> <h4n3tg$rte$1@reader1.panix.com> <4a1e8a66-23ba-4b04-94ad-0c33015e291b@q35g2000vbi.googlegroups.com> <h4nc9g$3kp$1@reader1.panix.com> <27ac8c36-9fa8-4382-8433-dee2a2fa0a66@z28g2000vbl.googlegroups.com> <7daglpF2as6eiU1@mid.individual.net> <7dah6oF2bmbjiU1@mid.individual.net> <725ac0a7-14c7-488b-8e32-f96f1edc498e@h21g2000yqa.googlegroups.com> <7db0dcF2ai115U1@mid.individual.net>`

```

Moving COBOL with inline Oracle Pro*COBOL to PL/SQL is really
esoteric.

Since you and your company seem so lost, take what you know already
(Java, C#, C++, Ruby, ...) and make a proof of concept and change
"boss" minds.

Batch applications work best with COBOL, C++, Java, C# and PL/SQL is a
centralized resource or API for applications. How do you take a ISAM
file in PL/SQL and do operations with it?
How do you read/write BCD (decimal) in PL/SQL?
Is your PL/SQL code portable? What will you do when Oracle 12 breaks
your code?

Have you evaluated converting you COBOL code to Java packages inside
Oracle Database? That would make more sense to me.

Good luck
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
