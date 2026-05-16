[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# All X'0D' lost during reading line sequential file using microfocus se

_100 messages · 12 participants · 2008-07 → 2008-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2008-07-30T11:31:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4890511A.6F0F.0085.0@efirstbank.com>`

```
One thing I think has been mentioned in passing but perhaps overlooked is
doing a database to database load, rather than an export followed by an
import.  I have only been partially paying attention, but is the goal to get
data that currently exists in DB2 for z/OS in to a DB2 AIX database?  If you
have DB2 9.1 or 9.5 on AIX you should be able to do something like the
following:


DECLARE load_curs CURSOR 
    DATABASE <sourcedb>
    USER <source_db_user_name>
    USING <source_db_user_password>
    FOR SELECT * FROM <source_table_name>;
LOAD FROM load_curs OF CURSOR
    REPLACE INTO <dest_table_name>;

I believe this feature (the DATABASE/USER/USING clauses) is available only
in version 9.  With prior versions you have to set up "data federation" on
your destination db and have nicknames for your source db tables.  More
complicated, but still possible.  Either way your AIX database must be able
to connect to your z/OS database.  If that is not an option then this will
not work.

I have no idea if this actually meets your requirements, but it's one
possible option.  No Cobol needed, and no export files needed.

Frank
```

#### ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-30T18:23:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1ls19495kpio33122t0fsl3v749fsum2ql@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com>`

```
On Wed, 30 Jul 2008 11:31:38 -0600, "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
wrote:

>One thing I think has been mentioned in passing but perhaps overlooked is
>doing a database to database load, rather than an export followed by an
…[22 more quoted lines elided]…
>possible option.  No Cobol needed, and no export files needed.

Oracle is simpler

create table <dest> as select * from <src>@<sourcedb>;

where sourcedb is defined once:

create database link <sourcedb>
    connect to <user> identified by <password> using 'service handle';

If you don't have permission to create a db link, you can use the sqlplus copy command:

copy from <user>/<password>@<sourcedb> create <dest> using select * from <src>;
```

#### ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-30T19:02:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b41ff8db-9fc2-4652-8b20-a103608884dc@k37g2000hsf.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com>`

```
On 7月31日, 午前2:31, "Frank Swarbrick" <Frank.Swarbr...@efirstbank.com>
wrote:
> One thing I think has been mentioned in passing but perhaps overlooked is
> doing a database to database load, rather than an export followed by an
…[23 more quoted lines elided]…
> Frank

Do you mean load data from mainframe DB to AIX DB directly if they can
be connected?
Yes there would be problems when migrating the data. But now what I
need to do is like that:

export 2 tables (or some fields of it);
sort the exported data by mfsort;
match the sorted file and only output the necessary records;
import the output file back to the table replacing the old ones.

The original sources are JCL and mainframe cobol which are to be
migrated to AIX shell and microfocus cobol.
I'm sorry I describe this whole image so late that maybe misleaded you
all.

Actually it also maybe possible to read the 2 tables in the cobol
program and delete the unmatched ones(almost writing a new source).
But I think it costs too much. Perhaps it's the last method we will
try.
```

##### ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-30T23:16:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sje2945ahjsv8fr7f82rcsfr06855g6amh@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <b41ff8db-9fc2-4652-8b20-a103608884dc@k37g2000hsf.googlegroups.com>`

```
On Wed, 30 Jul 2008 19:02:37 -0700 (PDT), taoxianfeng@gmail.com wrote:

>On 7ï¿½ï¿½31ï¿½ï¿½, ï¿½È«e2:31, "Frank Swarbrick" <Frank.Swarbr...@efirstbank.com>
>wrote:
…[33 more quoted lines elided]…
>sort the exported data by mfsort;

The database will sort them if you say ORDERED BY.

>match the sorted file and only output the necessary records;

That's a simple database join operation. There is no need to sort the tables.

create table temp_a as 
  select a.* from a, b
    where a.customer_id = b.customer_id;

or 

create table temp_a as
  select * from a 
    where customer_id in (select customer_id from b);

>import the output file back to the table replacing the old ones.

drop table a;
rename table temp_a to a;

>The original sources are JCL and mainframe cobol which are to be
>migrated to AIX shell and microfocus cobol.
…[6 more quoted lines elided]…
>try.

You might be doing it the hard way.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-30T21:52:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <b41ff8db-9fc2-4652-8b20-a103608884dc@k37g2000hsf.googlegroups.com> <sje2945ahjsv8fr7f82rcsfr06855g6amh@4ax.com>`

```
On 7月31日, 午後1:16, Robert <n...@e.mail> wrote:
> On Wed, 30 Jul 2008 19:02:37 -0700 (PDT), taoxianf...@gmail.com wrote:
> >On 7¤ë31¤é, ¤È«e2:31, "Frank Swarbrick" <Frank.Swarbr...@efirstbank.com>
…[69 more quoted lines elided]…
> - 引用テキストを表示 -

Well, I also know the basic SQL such as ORDER BY and JOIN.

But it's not me who chose to handle these data by export-match-import.

Just as I said before, it would be easier with some shell script but
it's not up to me.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-07-31T11:32:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g6s7sp$69d$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <b41ff8db-9fc2-4652-8b20-a103608884dc@k37g2000hsf.googlegroups.com> <sje2945ahjsv8fr7f82rcsfr06855g6amh@4ax.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com>`

```
In article <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com>,
 <taoxianfeng@gmail.com> wrote:
>On 7月31日, 午後1:16, Robert <n...@e.mail> wrote:

[snip]

>> You might be doing it the hard way.- 引用テキストを表示しない -
>>
…[4 more quoted lines elided]…
>But it's not me who chose to handle these data by export-match-import.

It seems that your knowledge of the tools required (COBOL and SQL) is 
rather basic and the choice of solution is being dictated elsewhere.

Either you are receiving some very expensive on-the-job training or your 
management deserves the results they are getting.

DD
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 5)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-31T08:02:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <b41ff8db-9fc2-4652-8b20-a103608884dc@k37g2000hsf.googlegroups.com> <sje2945ahjsv8fr7f82rcsfr06855g6amh@4ax.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com>`

```
On Thu, 31 Jul 2008 11:32:41 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com>,
> <taoxianfeng@gmail.com> wrote:
…[16 more quoted lines elided]…
>management deserves the results they are getting.

In the brave new world of contract programming, unreasonable assignments are semi-common.
I was once assigned to write a new program from scratch in a language (VB) I barely knew,
and given three days to get it done. It was a non-trivial program and there was no model I
could use as a starting point. If I hadn't gotten it done, there was an implied threat of
unemployment. I've seen worse, for example people assigned to work on huge
mission-critical mainframe assembly language programs with two weeks' training in Cobol
and no clue about assembly language on any machine. In that instance, three out of four
'failed' and were fired. The contracting company just shoveled more bodies onto the fire. 

There's no time or budget for 'professionalism' in this world. You get it done, or else.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-07-31T13:28:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g6sel7$sbf$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com>`

```
In article <fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com>,
Robert  <no@e.mail> wrote:
>On Thu, 31 Jul 2008 11:32:41 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[21 more quoted lines elided]…
>are semi-common.

Is that so, Mr Wagner?  Gosh and golly gee, one learns something new every 
day.

>I was once assigned to write a new program from scratch in a language
>(VB) I barely knew,
…[4 more quoted lines elided]…
>unemployment.

In the few short decades that I've been working as a 
consultant/contractor/hired gun I have been given such assignments; my 
response has been to state, in writing, that I have not, at any time, 
presented myself as already possessing the skills which the task appears 
to require and I cannot, in good professional faith, provide the same 
degree of certainty for the quality of product that will result.

In short: 'I am more than willing to give it a shot but I never said that 
I have done this sort of stuff before.  If it all goes kerflooie then it 
all goes kerflooie.'


>I've seen worse, for example people assigned to work on huge
>mission-critical mainframe assembly language programs with two weeks'
…[4 more quoted lines elided]…
>bodies onto the fire. 

The contracting company seems to have been aware that their status was not 
threatened by supplying inferior product.  If the person with 
signing-authority over the contract keeps pumping out checks for 
low-quality personnel then... it appears that checks keep getting signed.

>
>There's no time or budget for 'professionalism' in this world. You get
>it done, or else. 

I have no idea what 'professionalism' is in your book, Mr Wagner.  As 
noted above I will put in writing what I have done before and what I'm 
willing to do now; if the client disapproves of this... well, there's 
always another job.

DD
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 6)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-07-31T09:36:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<M5kkk.16863$mh5.2242@nlpi067.nbdc.sbc.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <b41ff8db-9fc2-4652-8b20-a103608884dc@k37g2000hsf.googlegroups.com> <sje2945ahjsv8fr7f82rcsfr06855g6amh@4ax.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com>`

```
"Robert" <no@e.mail> wrote in message 
news:fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com...
> In the brave new world of contract programming, unreasonable assignments 
> are semi-common.
> I was once assigned to write a new program from scratch in a language (VB) 
> I barely knew...

Pray, how on earth were you selected as the contractor?

And why on earth did you - as a professional contractor - accept such an 
assignment?

> I've seen worse, for example people assigned to work on huge 
> mission-critical mainframe assembly language programs with two weeks' 
> training in Cobol
> and no clue about assembly language on any machine....

Worse yet: someone who does know the 'language product(s) of choice' 
extremely well, but is clueless about the application.

I ran into this about ten years ago. I was doing some mapping of ANSI EDI 
data (that's about 70% of what I do) for a client in Janesville WI.  Part of 
this mapping required an application run against an ERP system's database, 
and since I was not (and still am not) familiar with the client's "language 
product of choice" (Microsoft Visual BASIC) and at that time not any good 
with Oracle/SQL, another contractor (from a 'major brand name consulting 
firm in Wisconsin') was engaged to create that application.

I laid out for him what I wanted... simple text file containing five or six 
delimited columns of data extracted from the ERP system's database, and the 
conditions under which a record was to appear in that file. I would then map 
that data into fully-enveloped ANSI X12 transaction sets. Simple, yes?

Well,  this "consultant" ( a misuse of the word if ever there was one) took 
it upon himself to try to map the data to ANSI himself. He had great 
difficulty (like, that was a surprise?).  But he did this without telling 
anyone.

Three weeks later, the project was due; and I mean DUE.  I had to tell the 
client I was waiting on the required input, but once I had it I could map 
the data in an afternoon. The other consultant was out that day, so I was 
asked to look at his 'work product to date' and see if I could use what he 
had and maybe make something out of what was done. (Did I mention, this 
project was REALLY DUE?) .

DISASTER!  Not only had the 'consultant' not been able to map the ANSI data, 
he had not even completed the extraction of the required data from the ERP 
database!

About 4:00 PM I sat down with the client's 'database guys' (employees of 
client) who both knew Oracle pretty well, but did not know the application. 
I showed them the text file I had orginally asked for, the tables in the 
database where the data were located, and asked if they could create the 
file using Oracle tools and utilities. They said they thought so .. so they 
went off to play with the database, whilst I created the mapping code based 
on their ability to create that input.

They succeeded in creating the data. I succeeded in creating the ANSI ASC 
X12 output. The required ANSI document was sent to the partner about 8:00 
PM.

Three weeks of consultant fees totally wasted by the client!  I see things 
like this and it drives me nuts: just like with lawyers, you get a couple of 
bad apples and we ("real" consultants) ALL look bad.

If  I can accomplish one thing before I go thru that final checkout line, I 
will see contractors and consultants regarded as true professionals - 
because we have EARNED that respect.

So, um, Robert.....  let's not accept any more contractor assignments for 
which are not qualified, OK?
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 7)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-31T20:15:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <b41ff8db-9fc2-4652-8b20-a103608884dc@k37g2000hsf.googlegroups.com> <sje2945ahjsv8fr7f82rcsfr06855g6amh@4ax.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com> <M5kkk.16863$mh5.2242@nlpi067.nbdc.sbc.com>`

```
On Thu, 31 Jul 2008 09:36:16 -0500, "Michael Mattias" <mmattias@talsystems.com> wrote:

>"Robert" <no@e.mail> wrote in message 
>news:fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com...
…[5 more quoted lines elided]…
>Pray, how on earth were you selected as the contractor?

The usual way -- for Cobol and SQL skills. Employers are overly selective during the
hiring phase. Once a contractor is on board, that goes out the window; the only thing that
counts is availability. 

"We need this program written in three days."
"So get one of those VB programmers to write it."
"They're busy on other assignments. You're the only one available."
"But I don't know VB well enough to write it."
"If you can't do it, we'll find someone who can."
"You just said no one else was available."
"We'll hire your replacement."

>And why on earth did you - as a professional contractor - accept such an 
>assignment?

They didn't ASK whether I wanted to do it. They said get it done or else.

>> I've seen worse, for example people assigned to work on huge 
>> mission-critical mainframe assembly language programs with two weeks' 
…[4 more quoted lines elided]…
>extremely well, but is clueless about the application.

Understanding the application is the analyst's job. 

>I ran into this about ten years ago. I was doing some mapping of ANSI EDI 
>data (that's about 70% of what I do) for a client in Janesville WI.  Part of 
…[9 more quoted lines elided]…
>that data into fully-enveloped ANSI X12 transaction sets. Simple, yes?

Yes. Sounds like a half-hour job. 

>Well,  this "consultant" ( a misuse of the word if ever there was one) took 
>it upon himself to try to map the data to ANSI himself. He had great 
>difficulty (like, that was a surprise?).  But he did this without telling 
>anyone.

That's not easy, unless he had third-party software to format EDI.

>Three weeks later, the project was due; and I mean DUE.  I had to tell the 
>client I was waiting on the required input, but once I had it I could map 
…[15 more quoted lines elided]…
>on their ability to create that input.

There's no need for tools and utilities. It can be done in straight SQL.

>They succeeded in creating the data. I succeeded in creating the ANSI ASC 
>X12 output. The required ANSI document was sent to the partner about 8:00 
…[4 more quoted lines elided]…
>bad apples and we ("real" consultants) ALL look bad.

Sounds like bad management. There should have been milestones. For such a simple task, two
day milestones sounds about right.

>If  I can accomplish one thing before I go thru that final checkout line, I 
>will see contractors and consultants regarded as true professionals - 
>because we have EARNED that respect.

You're pissing into a gale force wind. The contracting scene is full of low-paid
foreigners willing to try anything, and having NO bargaining power. Clients expect low
productivity and quality. They don't care because three contractors cost less than one
'professional'. A big plus is the fact they don't talk back, don't point out management
mistakes in public (you should hear what they say in private.)

>So, um, Robert.....  let's not accept any more contractor assignments for 
>which are not qualified, OK?

If I refused to do taks for which I'm not qualified, I'd be looking for a new job every
month or two. 

What's more difficult is following instructions to do things WRONG in an area where I'm
MORE knowledgable than the boss. This occurs often in version control, which is my
specialty.  Managers often want simple-minded solutions based how they did it with flat
files before they got version control. 'All ya gotta do is copy uncontrolled files over
controlled ones. What's so hard about that?' When I diplomatically try to explain version
control was created to STOP such abuse, it's like talking to the wall. Later, when they
learn changes were overwritten, they say 'See, I told you the version control doesn't
work. We even had an expert move the code.'
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 8)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-31T23:49:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83df5612-b65d-4541-957f-47d3fbf0df51@y38g2000hsy.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <b41ff8db-9fc2-4652-8b20-a103608884dc@k37g2000hsf.googlegroups.com> <sje2945ahjsv8fr7f82rcsfr06855g6amh@4ax.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com> <M5kkk.16863$mh5.2242@nlpi067.nbdc.sbc.com> <vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com>`

```
On 8月1日, 午前10:15, Robert <n...@e.mail> wrote:
> On Thu, 31 Jul 2008 09:36:16 -0500, "Michael Mattias" <mmatt...@talsystems.com> wrote:
> >"Robert" <n...@e.mail> wrote in message
…[118 more quoted lines elided]…
> - 引用テキストを表示 -

This post fits me perfectly...I'm just in such a "low-paid foreigner"
team that "willing to try anything".
We have dozens of people just available and no-qualified...
Most of us begin to learn shell just from May ,in such a JCL to shell
migration project...
Better with cobol and JCL,about a half members have several years
experience of mainframe cobol.
I think it's easier to find a Martian than a pro with 10 years
experience of mainframe cobol in CHINA, not to mention MicroFocus
SE...
That's also the big scene of Chinese software outsouring, my opinion.

Frankly again, I'm sitting in the customer's office("on site") just
because I can say better Japanese and English...
I learned Java,C#,C++,SQL...tons of courses in campus but mastered
nothing.
Chinese university education is becoming fast food and paper-making
machine...well,that's another topic again.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 9)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-01T21:51:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ekh79493hinehrdm92bomv3cg4gt0ntmf0@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <b41ff8db-9fc2-4652-8b20-a103608884dc@k37g2000hsf.googlegroups.com> <sje2945ahjsv8fr7f82rcsfr06855g6amh@4ax.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com> <M5kkk.16863$mh5.2242@nlpi067.nbdc.sbc.com> <vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com> <83df5612-b65d-4541-957f-47d3fbf0df51@y38g2000hsy.googlegroups.com>`

```
On Thu, 31 Jul 2008 23:49:34 -0700 (PDT), taoxianfeng@gmail.com wrote:

>On 8?1?, ??10:15, Robert <n...@e.mail> wrote:
>> On Thu, 31 Jul 2008 09:36:16 -0500, "Michael Mattias" <mmatt...@talsystems.com> wrote:
…[123 more quoted lines elided]…
>We have dozens of people just available and no-qualified...

You're like we were in the 1960s and 70s. We didn't 'know what we were doing,' we just did
the best we could. 

>Most of us begin to learn shell just from May ,in such a JCL to shell
>migration project...
…[4 more quoted lines elided]…
>SE...

How much would they pay for a VERY experienced SE programmer? :)

>That's also the big scene of Chinese software outsouring, my opinion.
>
>Frankly again, I'm sitting in the customer's office("on site") just
>because I can say better Japanese and English...

If our positions were reversed, if we had to speak fluent Nippongo and Mandarin, most
Americans wouldn't try. I envy adventurers like you. (I lived in Japan for two years when
I was your age.)

>I learned Java,C#,C++,SQL...tons of courses in campus but mastered
>nothing.
>Chinese university education is becoming fast food and paper-making
>machine...well,that's another topic again.

It's the same here.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 9)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-08-02T07:14:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgYkk.9066$vn7.505@flpi147.ffdc.sbc.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <b41ff8db-9fc2-4652-8b20-a103608884dc@k37g2000hsf.googlegroups.com> <sje2945ahjsv8fr7f82rcsfr06855g6amh@4ax.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com> <M5kkk.16863$mh5.2242@nlpi067.nbdc.sbc.com> <vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com> <83df5612-b65d-4541-957f-47d3fbf0df51@y38g2000hsy.googlegroups.com>`

```
<taoxianfeng@gmail.com> wrote in message 
news:83df5612-b65d-4541-957f-47d3fbf0df51@y38g2000hsy.googlegroups.com...
> I learned Java,C#,C++,SQL...tons of courses in campus but mastered
> nothing.
> Chinese university education is becoming fast food and paper-making
> machine...well,that's another topic again.


There are two important differences between school and Real Life:

1. In Real Life the answers are *not*  to be found in Appendix B.

2. In Real Life all problems are "story problems."


MCM
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 10)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-08-04T15:02:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0f269af9-20fa-4992-bf64-169467a039af@l42g2000hsc.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <b41ff8db-9fc2-4652-8b20-a103608884dc@k37g2000hsf.googlegroups.com> <sje2945ahjsv8fr7f82rcsfr06855g6amh@4ax.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com> <M5kkk.16863$mh5.2242@nlpi067.nbdc.sbc.com> <vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com> <83df5612-b65d-4541-957f-47d3fbf0df51@y38g2000hsy.googlegroups.com> <cgYkk.9066$vn7.505@flpi147.ffdc.sbc.com>`

```
On Aug 2, 8:14 am, "Michael Mattias" <mmatt...@talsystems.com> wrote:
>
> There are two important differences between school and Real Life:
…[5 more quoted lines elided]…
> MCM

Right you are, Mr. Mattias, and I say that though some may consider me
a bit of an "academic" (degree professional who also manages to teach
a bit at a community college.)

And the relevant "story problem" at hand is to determine The Real Need
of the client. For this, the formal posting and job/project
description provides only a partial set of clues, albeit important
ones. Submitting you resume, and the "match" it makes with the formal
job spec, should have as its goal not the job itself, but only the
granting of an interview. I still prefer face-to-face, though phone
screening is becoming increasingly prominent. It is during this
interview that you have to think quick on your feet, to determine what
The Real Need is. That is Dancing the Dance, and it should be, though
not always is, a bit fun. :-) It's nice to have a few months billings
salted away for these times, lest what should be a Dance of Delight
becomes a Dance of (Near) Desperation.

Ken
```

###### ↳ ↳ ↳ OT: Submitting your resume WAS Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-08-05T12:03:29+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6fpjmiFcmtjdU1@mid.individual.net>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <b41ff8db-9fc2-4652-8b20-a103608884dc@k37g2000hsf.googlegroups.com> <sje2945ahjsv8fr7f82rcsfr06855g6amh@4ax.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com> <M5kkk.16863$mh5.2242@nlpi067.nbdc.sbc.com> <vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com> <83df5612-b65d-4541-957f-47d3fbf0df51@y38g2000hsy.googlegroups.com> <cgYkk.9066$vn7.505@flpi147.ffdc.sbc.com> <0f269af9-20fa-4992-bf64-169467a039af@l42g2000hsc.googlegroups.com>`

```

```

###### ↳ ↳ ↳ OT: Submitting your resume WAS Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 12)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-08-04T18:09:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0c1ffeb7-e8ab-4175-8881-5773e8f5e726@s50g2000hsb.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <b41ff8db-9fc2-4652-8b20-a103608884dc@k37g2000hsf.googlegroups.com> <sje2945ahjsv8fr7f82rcsfr06855g6amh@4ax.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com> <M5kkk.16863$mh5.2242@nlpi067.nbdc.sbc.com> <vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com> <83df5612-b65d-4541-957f-47d3fbf0df51@y38g2000hsy.googlegroups.com> <cgYkk.9066$vn7.505@flpi147.ffdc.sbc.com> <0f269af9-20fa-4992-bf64-169467a039af@l42g2000hsc.googlegroups.com> <6fpjmiFcmtjdU1@mid.individual.net>`

```
On Aug 4, 8:03 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> --
> "I used to write COBOL...now I can do anything."<klsha...@att.net> wrote in message

Ahhhhhh, I'll not let you make us out to be "further apart" than we
actually are, Mr. Pete :-) ...

>
> [begin Pete]
…[8 more quoted lines elided]…
> all things are a nail.
[end Pete]

[begin ken]
I think it would be presumptuous of me to assume that I know what
their needs are just by my reading of the formal job post /
description. And no, I won't be able to identify all their Real Needs
within the first five minutes of meeting them, but if I ask the right
questions, I'll be a lot closer after say, thirty minutes, than I was
going in. And it may not be the case at all that "...they don't know
what they need." They may indeed REALLY know, and yet, they can't
quite put those Real Needs down on paper, for any number of reasons
(often Politically Correct kinds of reasons, but not always.)

And how do we do this? Why, you provided a lot of the answer yourself,
Mr. Pete, namely...
[end ken]


> [begin Pete]
> Far better to let them simply describe what they are doing and where they
…[5 more quoted lines elided]…
> [end Pete]

[begin ken]
Yeah, something along those lines. I ask them what THEIR goals are for
the project, what they are interested in, and how they see themselves
fitting into the project, and how do they see me fitting in to help
them accomplish that.
[end ken]

> [begin ken]
> For this, the formal posting and job/project
…[3 more quoted lines elided]…
> granting of an interview.
  [end ken]
>
> [Pete]
…[4 more quoted lines elided]…
> view, if you are applying for a job as a technician.
[end Pete]

[begin ken]
For some stuff, it is "job level independent". I believe it is
necessary to persuade the client manager that you have sufficient
"intersection" with him and the Project-at-Large. Sure, you have to
have the sufficient level of expertise, but more than that, there
needs to be sufficient commonality that the manager has confidence
that he/she can "direct" your work.
[end ken]

> [begin Pete]
> If I were going for a job I had seen advertised, and had no previous dealing
…[3 more quoted lines elided]…
> available at an interview.
[end Pete]

[begin ken]
Agreed. Several years ago I started going with "customized" resumes. I
keep several boilerplate versions, and then for a particular
submission, I boldface and re-arrange selectively.
[end ken]
>
[begin Pete]
> I agree that the interview should be the goal. You enter the interview as
> someone who has already established credibility and your approach is to
> explore solutions with them. You should leave them feeling you would be a
> useful person to have around.
[end Pete]

[begin ken]
Exactly. See, a lot of our differences are just *melting* away! :-)
[end ken]
>
[begin Pete]
> I don't recall ever failing an interview in my life, though I guess there is
> always a first time...
[end Pete]
>

[begin ken]
Hmmmm.... I've come to believe that the only failed interview is one
where I lied. Since I have come to believe that, I don't think I've
had a single failed interview... :-) ...

Yes, I've had interviews where I didn't get the job. But I always left
knowing more than I went in, and I nearly always left with another
"contact", and I believe I've always left knowing that I earnestly put
my best self forward. At some point one just has to trust other
people. If you didn't get the job, then you weren't meant to get it.
You might not know why right now; you might find out later. You may
never find out. This is why there is a place for Faith in the world.
[end ken]


> [begin ken]
> I still prefer face-to-face, though phone
…[4 more quoted lines elided]…
> [end Pete]

>  [begin Pete]
> This is where we part company, Ken. :-) If you attend an interview with the
> idea of being whatever they want you to be, or identifying The Real Need and
> selling to that, then I believe the outcome is likely to be a crap shoot.
  [end Pete]

 [begin ken]
Again, I an uncertain as to "how far part" we really are on this.
Pete, it is *always* a bit of a crap shoot ... the best that we can
hope for is that it is a round of Blackjack, and if we pay attention,
and count the cards, then we may tilt the odds every so slightly in
our favor.

And no, I would never recommend that anyone show up "with the idea of
being whatever they want to be" for to do so would amount to complete
Loss of Identity. After all, there are some things I *don't* want to
do, and some things I simply *won't* do, though they may be outweighed
by the things that I would find interesting to do. What I can do, to
help tilt the outcome toward me, is to help the manager/client uncover
the characteristics I have which *do* intersect with him. And those
are not always the ones that are on paper.
[end ken]


[begin Pete]
> For me, what works is to listen without even trying to presume what "The
> Real Need" is. Contribute past experience, suggest alternatives and examine
> pros and cons. THEN look at what specific contribution you can bring.
[end Pete]

[begin ken]
Well, again, *exactly*. The job spec is only a starting point for the
dialogue, it is *entry* through the doorway to listening without bias.
To determine, best you can, what their Real Need is :-). This is much
easier said than done. It is one of the skills I found harder to come
by than coding in any particular language. It is something I still
concentrate on. (CLC is a good laboratory to do that, by the
way :-) .)
[end ken]

> [begin Pete]
> See, the mystic secret is that "The Real Need" is a tenuous thing that
…[5 more quoted lines elided]…
> of coming away with an offer of employment, if you still want it.
[end Pete]

[begin ken]
Here we differ a bit. I already have a Job with the Needs described
above - it's called being a Husband :-).

So what I need to help balance me out is, uh, a little "invariance". I
_need_ someone, a client / manager, who has a pretty good handle on
what he needs, and has some authority to enforce it. Only if I have a
certain amount of stability in that regard will I be able to do a good
job. Perhaps I could do an *adequate* job in the environment you
described above, but probably not a *really good* job. Sometimes
*adequate*, is, well, *adequate*, so it may still be worth exploring.
[end ken]
>
> [some stuff snipped]
…[6 more quoted lines elided]…
> the Summer off and enjoy it. Sufficient unto 2009 the evils thereof...:-)
[end Pete]

[begin ken]
What? To the contrary, *autumn* is just around the corner, and for you
to suggest otherwise is a measure of how *different* we really
are! :-) But let us remember that opposites are like the ends of the
horseshoe, really closer to each other than the either is to the
"middle"...
[end ken]
>

[begin Pete]
> A balance between work and play is essential for the mental and physical
> health of most of us...
[end Pete]
>
[begin ken]
Yes, another thing easier said than done. After this post, there won't
be enough daylight to ride my bike. I'll have to do that tomorrow...
[end ken]

Ken
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-01T09:35:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g6ulct$ceo$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com> <M5kkk.16863$mh5.2242@nlpi067.nbdc.sbc.com> <vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com>`

```
In article <vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com>,
Robert  <no@e.mail> wrote:
>On Thu, 31 Jul 2008 09:36:16 -0500, "Michael Mattias"
><mmattias@talsystems.com> wrote:

[snip]

>>Pray, how on earth were you selected as the contractor?
>
…[12 more quoted lines elided]…
>"We'll hire your replacement."

'Now let me get this straight... you honestly believe that in three days 
you can review resumes, call pimps, interview consultants, weed out the 
deadwood, agree on a rate, get the guy through Security, assign him a 
logon ID and still have time to code the program?

'I hope you're very happy with whoever will be working with you on this... 
because it isn't going to be me.'

>
>>And why on earth did you - as a professional contractor - accept such an 
>>assignment?
>
>They didn't ASK whether I wanted to do it. They said get it done or else.

See above.  In my experience it was either a hollow threat or a place I 
did not want to work.

[snip]

>>Three weeks of consultant fees totally wasted by the client!  I see things 
>>like this and it drives me nuts: just like with lawyers, you get a couple of 
>>bad apples and we ("real" consultants) ALL look bad.
>
>Sounds like bad management.

I've been a consultant/contractor/hired gun for a few decades now, Mr 
Wagner, and I've yet to get a gig at a place which had what I would call 
'good management'... the nature of my work, perhaps, in the same way that 
physicians frequently see a lot more sick people than healthy ones.

[snip]

>>So, um, Robert.....  let's not accept any more contractor assignments for 
>>which are not qualified, OK?
>
>If I refused to do taks for which I'm not qualified, I'd be looking for
>a new job every month or two. 

Sometimes, Mr Wagner, it works out that one winds up having what one is 
willing to accept.  Our experiences, of course, may be different... I've 
been asked to do stuff ('we need it yesterday!') for which I did not have 
appropriate experience and my response has been 'I have stated, 
unambiguously and explicitly, that this does not fall within my existing 
skill-set; in order to get it done I will need (time/resources).  If those 
cannot be made available for me then I must, in all good conscience, 
refuse the task just as a plumber would have to refuse a job-order for 
rewiring a generator.'

Word gets around.

DD
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 9)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-01T22:20:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com> <M5kkk.16863$mh5.2242@nlpi067.nbdc.sbc.com> <vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com> <g6ulct$ceo$1@reader1.panix.com>`

```
On Fri, 1 Aug 2008 09:35:25 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com>,
>Robert  <no@e.mail> wrote:
…[24 more quoted lines elided]…
>logon ID and still have time to code the program?

Kelly says they can have someone on site tomorrow, at a very attractive rate.

>'I hope you're very happy with whoever will be working with you on this... 
>because it isn't going to be me.'
…[8 more quoted lines elided]…
>did not want to work.

It was not a hollow threat. Either you rise to the occasion or you're unemployed. 

>>>Three weeks of consultant fees totally wasted by the client!  I see things 
>>>like this and it drives me nuts: just like with lawyers, you get a couple of 
…[7 more quoted lines elided]…
>physicians frequently see a lot more sick people than healthy ones.

I concur. If it weren't for bad management, there would be no contractors. We'd have to
find Real Jobs, which don't pay as well.

>>>So, um, Robert.....  let's not accept any more contractor assignments for 
>>>which are not qualified, OK?
…[5 more quoted lines elided]…
>willing to accept.  

"People get and deserve what they settle for."

>Our experiences, of course, may be different... I've 
>been asked to do stuff ('we need it yesterday!') for which I did not have 
…[7 more quoted lines elided]…
>Word gets around.

Word gets around that you're a crochety old guy, which is the kiss of death outside the
mainframe world. I work with people in their 20s and 30s who think old people are too slow
and out of style. They'll fire you in a heartbeat. It takes an effort to wow them.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-02T12:10:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g71ir7$mtq$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com> <g6ulct$ceo$1@reader1.panix.com> <ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com>`

```
In article <ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com>,
Robert  <no@e.mail> wrote:
>On Fri, 1 Aug 2008 09:35:25 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[31 more quoted lines elided]…
>>because it isn't going to be me.'

It's your choice to believe a salesman over a programmer on a technical 
matter... but I hope you're very happy with whoever Kelly gives you 
because it isn't going to be me... oh, I said that already.

>>
>>>
…[9 more quoted lines elided]…
>unemployed. 

Managing to turn someone else's lack of planning or foresight into your 
own emergency is not what I would call 'rising to the occasion', Mr 
Wagner... it is what I would call 'paying for your own Vaseline'.  See 
above, in my experience it was either a hollow threat or a place I did not 
want to work.

>
>>>>Three weeks of consultant fees totally wasted by the client!  I see things 
…[10 more quoted lines elided]…
>I concur.

''We agree on something?  One of us must be wrong!', he cried, Wildely.'

>>>If I refused to do taks for which I'm not qualified, I'd be looking for
>>>a new job every month or two. 
…[4 more quoted lines elided]…
>"People get and deserve what they settle for."

Leaving out the 'sometimes it works out that' might be seen as changing 
the statement substantially.

>
>>Our experiences, of course, may be different... I've 
…[12 more quoted lines elided]…
>mainframe world.

Mr Wagner, you've made assertions about various 'worlds' in the past which 
have been shown to have a curious relationship - or lack thereof - with 
what others have experienced.

>I work with people in their 20s and 30s who think old
>people are too slow
>and out of style. They'll fire you in a heartbeat. It takes an effort to
>wow them.

Mr Wagner, rest assured that you're not the only one who manages to do 
such things... or so my experience shows me.

DD
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 11)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-02T21:08:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19v994510llhjjimheq9qclmmsp849j07s@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com> <g6ulct$ceo$1@reader1.panix.com> <ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com> <g71ir7$mtq$1@reader1.panix.com>`

```
On Sat, 2 Aug 2008 12:10:15 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com>,
>Robert  <no@e.mail> wrote:

>>>>>And why on earth did you - as a professional contractor - accept such an 
>>>>>assignment?
…[13 more quoted lines elided]…
>want to work.

Lack of planning creates OPPORTUNITIES for contractors. The owner of my contracvting
company says we should always be on the lookout "someone whose cart is stuck in a ditch."
We will offer to pull it out. 

When I was a manager, for 20 years, I never used a contractor and was puzzled why anyone
would pay twice as much for a programmer. Now, having been a contractor for ten years,
I've seen a variety of reasons;

1. Employees are spending nearly all their time in meetings, don't have time to do actual
work.

2. Employees don't want to do grunge work like testing.

3. Company politics makes hiring contractors easier than using employees. Hiring freeze.

4. Need sacrificial goats for the annual 10% cut.
   Aside: the word decimate came from the Roman Legion practice of punishing an army unit 
   by killing every tenth man. It doesn't mean destroy; it means reduce by 10%.

5. Kickbacks. 

6. Add real expertise to low-skilled team of outsourcers. Rescue them when they don't know
what to do. 

7. The manager has no authority to hire employees, can employ only 'vendors.'

8. The HR department is so inept that it cannot find competent people. 

9. Management is under pressure to reduce employees. Contractors don't count.

>>>>>Three weeks of consultant fees totally wasted by the client!  I see things 
>>>>>like this and it drives me nuts: just like with lawyers, you get a couple of 
…[11 more quoted lines elided]…
>''We agree on something?  One of us must be wrong!', he cried, Wildely.'

All the above are symptoms of mismanagement. 

>>>>If I refused to do taks for which I'm not qualified, I'd be looking for
>>>>a new job every month or two. 
…[7 more quoted lines elided]…
>the statement substantially.

"People get what they settle for" is a quotation from Telma and Louise. They don't got to
show you no wimpy qualifier like "sometimes it works out that."

>>>Our experiences, of course, may be different... I've 
>>>been asked to do stuff ('we need it yesterday!') for which I did not have 
…[15 more quoted lines elided]…
>what others have experienced.

I relate my experiences with Fortune 100 companies that are household names -- Wal-Mart,
Coca-Cola, IBM, Merrill Lynch, Sears, Sprint, etc.  If your mileage varies, kindly
identify the venues where you found more enlightenment. 

>>I work with people in their 20s and 30s who think old
>>people are too slow
…[4 more quoted lines elided]…
>such things... or so my experience shows me.

The VB task turned out be rewarding. It promoted the user (a department manager was the
only user) to enter a month an year (by default it filled in last month), called an Oracle
'stored procedure' to extract one customer's (Blue Cross) purchases to a comma delimited
file, then FTPd the file to the user's desktop. He sent it to the customer as an email
attachment. 

Oracle has two kinds of procedure. A classical Stored Procedure is written in PL/SQL and
stored in the database. An External Procedure is written in any language that compiles to
an executable. Both are called the same way; the client has no way of knowing how the
procedure was written. I wrote it in Cobol. It didn't work. It was loaded by Oracle
(technically by The Listener, for security reasons) and started executing, but fell over
on the first IO, even a DISPLAY statement. 

The reason was that Oracle loaded the program with default dlopen options of RTLD_NOW,
RTLD_LOCAL, which means discard the symbol table. That's inappropriate with Micro Focus
Cobol because it lazy loads its file system, extfh. A Micro Focus program must be loaded
with RTLD_LAZY, RTLD_GLOBAL, which retains the symbol table for secondary loads. 

Apparently, I was the first person who every wrote an Oracle External Procedure in Micro
Focus Cobol. The MF support manager I talked to had not heard of this problem. The
solution was a C wrapper that did nothing but call dlopen to load the Cobol program with
the right options. In retrospect, I wish I'd written it in Cobol. 

I wonder whether ANYone else has encountered this problem. If not, it means Cobol is
mortibund for serious development on Unix.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-03T08:56:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g73rsj$bf9$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com> <g71ir7$mtq$1@reader1.panix.com> <19v994510llhjjimheq9qclmmsp849j07s@4ax.com>`

```
In article <19v994510llhjjimheq9qclmmsp849j07s@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sat, 2 Aug 2008 12:10:15 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[20 more quoted lines elided]…
>Lack of planning creates OPPORTUNITIES for contractors.

Lack of dryness creates puddles, swimming-pools and oceans, Mr Wagner... 
not all situations are created equally.

>The owner of my
>contracvting
>company says we should always be on the lookout "someone whose cart is
>stuck in a ditch."
>We will offer to pull it out. 

Such a generous fellow... it makes me wonder whe he last pulled over to 
assist a guy standing outside of a hood-raised car and holding a set of 
jumper-cables.

>
>When I was a manager, for 20 years, I never used a contractor and was
…[3 more quoted lines elided]…
>I've seen a variety of reasons;

Not a bad start, Mr Wagner... you might want to include 'provide the 
appearance of support for a project that's intended to fail' and the 'try 
them before we buy them' contract-to-hire schemes.

Oh, and there's also the odd project where the amount of work actually 
overwhelms the indigineous fauna, a system comversion or the adding of a 
new interface, where for a short time a bunch o' folks with previously 
un-needed skills are necessary, too... you see, the list keeps growing.

>>>>>>Three weeks of consultant fees totally wasted by the client!  I see things 
>>>>>>like this and it drives me nuts: just like with lawyers, you get a couple of 
…[13 more quoted lines elided]…
>All the above are symptoms of mismanagement. 

Ahhhhhh... management is not the head of the fish, is it?  Given the old 
standby of 'The responsibility for allocation, co-ordination and 
motivation of personnel and corporate resources towards the accomplishment 
of a stated Executive goal is that of Management'... what about 
misExecution?

I spent some time on-contract at a place a few years back... must have 
started there in '96 or so... that was in the fourth year of a six-year 
'We'll Be Off The Mainframe and On To Client Server'.  Things had gotten 
to a point where they realised that maybe it would be a good idea to get a 
few extra hands on board to deal with the mainframe 
enhancement/maintenance backlog caused by the Hard Freeze they instituted 
when the project began...

... oh, and they were bought out, a year and a half later.

>
>>>>>If I refused to do taks for which I'm not qualified, I'd be looking for
…[12 more quoted lines elided]…
>show you no wimpy qualifier like "sometimes it works out that."

If 'nothing is always (including this statement)' then a qualifier of 
'sometimes' can be a succinct shorthand for 'under certain conditions and 
alignments of forces or planets'.  If you want to live your live by the 
Deep Wisdom found in a movie about two women who commit suicide that's 
your call.

>
>>>>Our experiences, of course, may be different... I've 
…[3 more quoted lines elided]…
>>>>skill-set; in order to get it done I will need (time/resources).

[snip]

>>>>Word gets around.
>>>
…[12 more quoted lines elided]…
>identify the venues where you found more enlightenment. 

On the Internet nobody knows you're a weenie-boy running at 1200 baud on 
an Apple ][e... are you offering to play 'my resume's bigger than yours', 
Mr Wagner?  Consider, if you will, how different experiences can be for 
different people working in different project area at each of the 
companies you've mentioned... it's possible that someone has had the exact 
same clients as you - or, of course, an equally Illustrious Set - and has 
come to conclusions not in accord with your own.

(I interviewed at Merrill, years on back... somewhere in the Bowels of 
Jersey, as I recall; they demanded an arrangement they called a 
'professional day' and I said that I hope they would be very happy with 
whoever they found to fill the slot... because it wasn't going to be me.)

[snip]

>>>I work with people in their 20s and 30s who think old
>>>people are too slow
…[6 more quoted lines elided]…
>The VB task turned out be rewarding.

Not all tasks turn out that way, or so I've seen... even if every cloud 
has a silver lining there might not be enough metal to extract to pay for 
the damage the hailstrom has wrought on your crops.

DD
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 13)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-03T21:19:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9oc94162hh7tu4iihne20lea41nt1qdjo@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com> <g71ir7$mtq$1@reader1.panix.com> <19v994510llhjjimheq9qclmmsp849j07s@4ax.com> <g73rsj$bf9$1@reader1.panix.com>`

```
On Sun, 3 Aug 2008 08:56:52 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <19v994510llhjjimheq9qclmmsp849j07s@4ax.com>,
>Robert  <no@e.mail> wrote:
>>On Sat, 2 Aug 2008 12:10:15 +0000 (UTC), docdwarf@panix.com () wrote:

>>>Mr Wagner, you've made assertions about various 'worlds' in the past which 
>>>have been shown to have a curious relationship - or lack thereof - with 
…[10 more quoted lines elided]…
>Mr Wagner? 

I named the companies in response to sceptics who say I'm describing atypical situations. 

> Consider, if you will, how different experiences can be for 
>different people working in different project area at each of the 
>companies you've mentioned... it's possible that someone has had the exact 
>same clients as you - or, of course, an equally Illustrious Set - and has 
>come to conclusions not in accord with your own.

I describe my experiences; they can describe theirs.

>(I interviewed at Merrill, years on back... somewhere in the Bowels of 
>Jersey, as I recall; they demanded an arrangement they called a 
>'professional day' 

Did you speak with an accent? They usually confine that scam to foreigners.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 14)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-04T09:18:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g76hhj$dp6$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <19v994510llhjjimheq9qclmmsp849j07s@4ax.com> <g73rsj$bf9$1@reader1.panix.com> <d9oc94162hh7tu4iihne20lea41nt1qdjo@4ax.com>`

```
In article <d9oc94162hh7tu4iihne20lea41nt1qdjo@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sun, 3 Aug 2008 08:56:52 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[19 more quoted lines elided]…
>atypical situations. 

Mr Wagner, you were not said to be describing 'atypical situations', it 
was pointed out that your description of 'worlds' was not in accord with 
other folks' experiences.

>
>> Consider, if you will, how different experiences can be for 
…[5 more quoted lines elided]…
>I describe my experiences; they can describe theirs.

They have... and they don't mention much about 'worlds', that I recall.

>
>>(I interviewed at Merrill, years on back... somewhere in the Bowels of 
…[3 more quoted lines elided]…
>Did you speak with an accent? They usually confine that scam to foreigners. 

Some people say they hear me as doing such... but in the words of the 
Firesign Theatre, 'How can *I* know what *you* hear?'

DD
```

###### ↳ ↳ ↳ CoBOL and Contracting (was: All X'0D' lost during...)

_(reply depth: 13)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-08-04T15:17:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f41b8629-274e-4c5e-9fbf-9cb54aea279e@8g2000hse.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com> <g71ir7$mtq$1@reader1.panix.com> <19v994510llhjjimheq9qclmmsp849j07s@4ax.com> <g73rsj$bf9$1@reader1.panix.com>`

```
On Aug 3, 4:56 am, docdw...@panix.com () wrote:
> In article <19v994510llhjjimheq9qclmmsp849j...@4ax.com>,
> (I interviewed at Merrill, years on back... somewhere in the Bowels of
> Jersey, as I recall; they demanded an arrangement they called a
> 'professional day' and I said that I hope they would be very happy with
> whoever they found to fill the slot... because it wasn't going to be me.)

Hmmmm... "professional day" ... is that the concept where they tell
you, "Sometimes a professional day is seven hours, sometimes it is
eight or nine, you work until you get that day's tasks done." and then
it turns out that what with deadlines and all you wind up working ten
hour days, and thus they got you for 25% less than what you thought
the rate was?

If so, yes, I have encountered that, but it does seem to be a
peculiarly East Coast phenomenon. It makes sense only if the daily
rate is, say, at least $500 and probably more. But then you are
playing in the Big Leagues, and it is incumbent upon you to know a
multitude of Business and Psychic Self Defense techniques.

Ken
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (was: All X'0D' lost during...)

_(reply depth: 14)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-04T22:53:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g7819a$lqe$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <19v994510llhjjimheq9qclmmsp849j07s@4ax.com> <g73rsj$bf9$1@reader1.panix.com> <f41b8629-274e-4c5e-9fbf-9cb54aea279e@8g2000hse.googlegroups.com>`

```
In article <f41b8629-274e-4c5e-9fbf-9cb54aea279e@8g2000hse.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:
>On Aug 3, 4:56�am, docdw...@panix.com () wrote:
>> In article <19v994510llhjjimheq9qclmmsp849j...@4ax.com>,
…[10 more quoted lines elided]…
>the rate was?

Hmmmmmm... wonderful thing, this Google.  From 
<http://groups.google.com/group/comp.software.year-2000/msg/cc3f9ac82f6a6749?dmode=source>

--begin quoted text:

'Professional day'?  Not to shoot the bearer of the news, mind you, but i 
thought this crap went out in the '80's.  The last place I got asked to do 
this was a Merrill in New Jersey; as I was unfamiliar with the term I 
asked for clarification and was told that 'if a job takes more than a 
standard 8 hours you behave professionally and work until it is done... 
without extra charge.' Overtime could be charged starting after 10 hours.

I then asked if the job took *less* than 8 might I then go home and charge 
for 8... and received a curt bark of a laugh and a frosty 'no, it doesn't 
work that way'.

*I* don't work that way, either.   work an hour, pay an hour.

--end quoted text

>
>If so, yes, I have encountered that, but it does seem to be a
…[3 more quoted lines elided]…
>multitude of Business and Psychic Self Defense techniques.

As I've said before: when dealing with someone who is paid on an hourly 
basis it is equally as reprehensible for one-who-pays to request time 
worked for money that will not be paid as it is for one-who-is-paid to 
request money paid for time that was not worked.

Both, I would say, are forms of theft.

DD
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (was: All X'0D' lost during...)

_(reply depth: 14)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-08-05T13:10:30+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6fpnk8FcrcdlU1@mid.individual.net>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com> <g71ir7$mtq$1@reader1.panix.com> <19v994510llhjjimheq9qclmmsp849j07s@4ax.com> <g73rsj$bf9$1@reader1.panix.com> <f41b8629-274e-4c5e-9fbf-9cb54aea279e@8g2000hse.googlegroups.com>`

```


<klshafer@att.net> wrote in message 
news:f41b8629-274e-4c5e-9fbf-9cb54aea279e@8g2000hse.googlegroups.com...
On Aug 3, 4:56 am, docdw...@panix.com () wrote:
> In article <19v994510llhjjimheq9qclmmsp849j...@4ax.com>,
> (I interviewed at Merrill, years on back... somewhere in the Bowels of
> Jersey, as I recall; they demanded an arrangement they called a
> 'professional day' and I said that I hope they would be very happy with
> whoever they found to fill the slot... because it wasn't going to be me.)

Hmmmm... "professional day" ... is that the concept where they tell
you, "Sometimes a professional day is seven hours, sometimes it is
eight or nine, you work until you get that day's tasks done." and then
it turns out that what with deadlines and all you wind up working ten
hour days, and thus they got you for 25% less than what you thought
the rate was?

If so, yes, I have encountered that, but it does seem to be a
peculiarly East Coast phenomenon. It makes sense only if the daily
rate is, say, at least $500 and probably more. But then you are
playing in the Big Leagues, and it is incumbent upon you to know a
multitude of Business and Psychic Self Defense techniques.

[Pete]

That is ONE view of it. Like most things, a "Professional Day" is what you 
make it.

I ALWAYS work on this basis (and have done for the last 20 years). It suits 
me. I don't charge less than $1000 a day, and usually it is more. I DO 
occasionally work 10 or 12 hours, but I see that as my failure, not theirs. 
I plan my own work, set daily goals and expect to achieve them before going 
home. I usually do. I don't watch clocks, take as long over a working lunch 
(often with others) as I need to, and am not interested in hourly rates or 
overtime. Only getting it done. Some days (not often) I work six and a half 
hours (though I don't recall ever working less than this...), but seven and 
a half would be the norm; it depends entirely on circumstances and how 
things are going. More often than not, I am the last to leave the Office, 
but I'm usually the last to arrive, also...(I don't like mornings and try to 
minimise them ... Of course, occasionally, I turn up early to avoid becoming 
predictable...:-)) I don't do timesheets and if I'm managing several 
projects, my time is billed equally to all of them UNLESS this would be 
blatantly unfair to one or more sponsors...then we negotiate.

I'm not interested in long term contracts (usually a year would be maximum, 
but if the agreement was to see something through to delivery and it was 
going to take longer, then, fine...). Once, I signed a contract on the basis 
of specific delivery, rather than time, but that was unusual. I give better 
deals to companies who are imaginative and prepared to negotiate, but I 
never try and rip anyone off; deals are fair.

"Professional Day" isn't for everybody, but it works for me. It is agencies 
who have gotten it a bad name. Fortunately, in my case, the agency is 
usually only responsible for an introduction. They take their "finders fee" 
(last job I did in Auckland it was $20,000 - outrageous...) and butt out. 
That was an 18 month contract which was cancelled due to politics, but there 
was never any question of fair recompense being paid, under the terms of the 
contract.(In fact my employer went further than they had to... a good 
company.)

As for Business and Pyschic Self Defense I am adequately covered... :-) 
(You'd be amazed at how powerful a trump "success" is... No one wants to 
(overtly) rock the boat when it is seen to be proceeding nicely. Of course 
covert hostility and politics all go with the territory... The secret is not 
to get unwrapped, just communicate directly and privately with the 
saboteurs...get them on board if possible, otherwise render them no threat 
:-)

Pete.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 10)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-08-02T07:20:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rgYkk.9068$vn7.832@flpi147.ffdc.sbc.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com> <M5kkk.16863$mh5.2242@nlpi067.nbdc.sbc.com> <vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com> <g6ulct$ceo$1@reader1.panix.com> <ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com>`

```
"Robert" <no@e.mail> wrote in message
news:ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com...
> On Fri, 1 Aug 2008 09:35:25 +0000 (UTC), docdwarf@panix.com () wrote:

> Word gets around that you're a crochety old guy, which is the kiss of
> death outside the
…[3 more quoted lines elided]…
> wow them.

The "problem"  with us "crochety old guys" is that we know from experience
when something a client requests simply will not work and we know
failure of any kind will invariably reflect poorly on us; and that we were
simply "following orders"  will protect our good name about as much as that
excuse worked at Nuremburg.

Which is the main reason this crochtey old guy does not contract, he
consults.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-02T15:42:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g71v9a$pjv$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <g6ulct$ceo$1@reader1.panix.com> <ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com> <rgYkk.9068$vn7.832@flpi147.ffdc.sbc.com>`

```
In article <rgYkk.9068$vn7.832@flpi147.ffdc.sbc.com>,
Michael Mattias <mmattias@talsystems.com> wrote:
>"Robert" <no@e.mail> wrote in message
>news:ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com...
…[7 more quoted lines elided]…
>> wow them.

[snip]

>Which is the main reason this crochtey old guy does not contract, he
>consults.

My experience, Mr Mattias, is that what is called a 'consultant' at one 
organisation is called a 'contractor' at another and a 'temporary 
resource' at a third... the last term I found to have a kind of chilling 
dehumanisation to it.

At any rate... it may be that a (mumblety)-year-old hired gun would be 
making better use of her time by *not* trying to be a better 30-year-old 
than the 30-year-olds are and, instead, just being a good 
(mumblety)-year-old hired gun.

To tie into another thread... enthusiasm is wonderful, yes, but as the 
deadline looms it might be better to have fewer 'wow, I never knew that 
before... no wonder I was havingso much trouble! for so long' moments and 
more 'all right, this piece works, just as it has since the days of 
ENIAC... what's the next milestone?' moments.

DD
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 12)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-08-02T11:49:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6d0lk.9080$vn7.4834@flpi147.ffdc.sbc.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <g6ulct$ceo$1@reader1.panix.com> <ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com> <rgYkk.9068$vn7.832@flpi147.ffdc.sbc.com> <g71v9a$pjv$1@reader1.panix.com>`

```
<docdwarf@panix.com> wrote in message news:g71v9a$pjv$1@reader1.panix.com...
> My experience, Mr Mattias, is that what is called a 'consultant' at one
> organisation is called a 'contractor' at another and a 'temporary
> resource' at a third... the last term I found to have a kind of chilling
> dehumanisation to it.

What's in a name?

That which we call a rose .... etc

The use and misuse of the words "contractor" and "consultant" is one of my 
longtime personal "issues."

In general my complaint is with the latter being used to describe the 
function of the former.

However,  both professional contractors and professional consultants should 
know the difference, regardless of what terms others may use.

MCM
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 13)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-02T17:59:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<22p99452rh1df8lr0hf1o6psbgvsu3id4g@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <g6ulct$ceo$1@reader1.panix.com> <ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com> <rgYkk.9068$vn7.832@flpi147.ffdc.sbc.com> <g71v9a$pjv$1@reader1.panix.com> <6d0lk.9080$vn7.4834@flpi147.ffdc.sbc.com>`

```
On Sat, 2 Aug 2008 11:49:33 -0500, "Michael Mattias" <mmattias@talsystems.com> wrote:

><docdwarf@panix.com> wrote in message news:g71v9a$pjv$1@reader1.panix.com...
>> My experience, Mr Mattias, is that what is called a 'consultant' at one
…[12 more quoted lines elided]…
>function of the former.

Contractor is a misnomer, because it implies a contractual obligation for duration of
employment. There is no such guarantee, all contracts say "employment at will," which
means the employer can terminate at any time for any reason or no reason. 

Contracts are terminated prematurely all the time. IBM is notorious for doing it. I signed
an eight month contract (and a six month apartment lease) that was terminated with no
notice after two months. IBM didn't lose their outsource contract with the client not was
the project cancelled. Some faceless bureaucrat, probably in another city, realized they
weren't hitting a profit target, so (s)he axed 100 contractors in one day.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 14)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-08-03T13:55:11+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6fkhg0Fc0ck4U1@mid.individual.net>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <g6ulct$ceo$1@reader1.panix.com> <ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com> <rgYkk.9068$vn7.832@flpi147.ffdc.sbc.com> <g71v9a$pjv$1@reader1.panix.com> <6d0lk.9080$vn7.4834@flpi147.ffdc.sbc.com> <22p99452rh1df8lr0hf1o6psbgvsu3id4g@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:22p99452rh1df8lr0hf1o6psbgvsu3id4g@4ax.com...
> On Sat, 2 Aug 2008 11:49:33 -0500, "Michael Mattias" 
> <mmattias@talsystems.com> wrote:
…[34 more quoted lines elided]…
>

Why would you sign a contract that allows them to do that? Escape clauses 
are fine, but there has to be cash in lieu of notice.

Why don't you negotiate your own contract with the agency and let them worry 
about IBM terminating it? Are experienced contractors so thick on the ground 
they can afford to treat people like that? If so, then maybe you should be 
looking at a different way to make a living.

In the days when I was contracting as a programmer/analyst I tried to build 
a good working relationship with one agency. It worked very well.They would 
have another contract waiting as soon as the current one was finished, if I 
didn't want to extend. They met me at the airport when I arrived back in the 
U.K. from visits home between contracts, and ensured I had accommodation for 
the first week or so until it was decided where I'd be working. In other 
words, they took good care of me and, as a result, I did not circulate my CV 
to other agaencies. (In fact, I ended up becoming a partner in the 
agency...). The agency was eventually sold and all concerned came out of it 
pretty well. By then I had established enough credibility not to really need 
an agency to get work and I was moving more towards management anyway.

These days I'm pretty happy working from home with occasional visits to 
client sites, but I believe I will still take on the odd on-site Project 
Management type role for assignments that look particularly interesing 
(difficult...). In these cases I have a standard contract that is fair to 
both parties and no-one has refused to sign it yet. It does not provide for 
immediate termination without recompense (except in the unimaginable case of 
me running berserk or otherwise misbehaving, or conducting myself 
improperly.) and it does offer a money back guarantee of satisfaction. So 
far, I have never had to pay out, although I came close once... :-)

As long as you accept having a gun held to your head, then people will be 
tempted to hold guns to your head.

I've been a free lance since 1975 and I've NEVER had the kind of treatment 
you describe. I treat people fairly, do not despise and denigrate managers, 
or programmers, or analysts, or anybody else... (even poor ones...instead, 
try and encourage them to be better), and apply the fifteen points I posted 
here a while back. As a result, even when working for managers half my age, 
I have no problem with them.  (I had one on a project a few years back who 
said to me: "Y'know Pete, you're old enough to be my father..." I replied: 
"Aren't you lucky to have someone that kind and wise, who you can trust, 
working for you... ? :-)"   We never had a problem.

The world you describe is foreign to me. Maybe it is just America.

Pete.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 15)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-02T22:09:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oh5a94djujajtek423m6e7rui63bfjsip3@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <g6ulct$ceo$1@reader1.panix.com> <ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com> <rgYkk.9068$vn7.832@flpi147.ffdc.sbc.com> <g71v9a$pjv$1@reader1.panix.com> <6d0lk.9080$vn7.4834@flpi147.ffdc.sbc.com> <22p99452rh1df8lr0hf1o6psbgvsu3id4g@4ax.com> <6fkhg0Fc0ck4U1@mid.individual.net>`

```
On Sun, 3 Aug 2008 13:55:11 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>
>
…[46 more quoted lines elided]…
>looking at a different way to make a living.

In my experience, getting a contractor job requires:

.. Talking to 20 recruiters, convincing them you have ALL the requirements.

.. Interviewing with 5 clients. 

At the end of the process, which can take 2 weeks to 5 months, I always get three 'offers'
the same day, a Friday. 

1. A solid offer, the one I accept. 

2. A more interesting assignment that's 'definitely interested' but the decision maker is
on vacation, or so they say. Or the contracting company is too greedy to pay enough. 

3. Another that wants me but is having internal political problems.  

>In the days when I was contracting as a programmer/analyst I tried to build 
>a good working relationship with one agency. It worked very well.They would 
…[8 more quoted lines elided]…
>an agency to get work and I was moving more towards management anyway.

It was like that in the US during the 90s. No longer. I've worked for the same contracting
company twice, but never consecutively. Every time a project ends, I'm starting from
scratch.

>These days I'm pretty happy working from home with occasional visits to 
>client sites, but I believe I will still take on the odd on-site Project 
…[21 more quoted lines elided]…
>The world you describe is foreign to me. Maybe it is just America.

You're describing a world that ended ten years ago .. at least in the US, probably in
India and China as well. Contractors are called 'resources.' They have zero bargaining
power. If they won't sign a 'standard contract,' there are a hundred Indian contractors
who will. 

The company where I'm working now has 40,000 IT workers, half of whom are contractors.
They can't possibly consider the talents of each individual. How would YOU manage a staff
that large? You'd have to decide the fate of people you'd never met based on generalities.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 16)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-03T14:20:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g74ero$bnd$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <22p99452rh1df8lr0hf1o6psbgvsu3id4g@4ax.com> <6fkhg0Fc0ck4U1@mid.individual.net> <oh5a94djujajtek423m6e7rui63bfjsip3@4ax.com>`

```
In article <oh5a94djujajtek423m6e7rui63bfjsip3@4ax.com>,
Robert  <no@e.mail> wrote:
>

[snip]

Mr Wagner and I seem to have remarkably similar experiences in this 
matter.

>In my experience, getting a contractor job requires:
>
>.. Talking to 20 recruiters, convincing them you have ALL the requirements.

First the recruiter must be caught, of course.  One fires up one's email 
(it used to be a fax machine) and sends an updated copy of the brag-sheet 
to everyone there...

... and then waits a bit for the flurry of 'RECIPIENT NOT FOUND' or 
'DOMAIN DOES NOT EXIST' replies.  Agencies come and go with all the 
permanence of wildflowers after a desert rain.

Then, after dealing with the 'pimples' (junior-level pimps) who have been 
assigned to 'New Contacts' ('Please, turn to page three and notice the 
date of that first technical certification... yes, that's right, the one 
that's before either of your parents were born.  What were you asking 
about experience?')  and the requests for 'Hairy Ears' interviews:

P: 'We'd like you to come in and talk to you about what Sell-ur-Assco is 
all about.'

M: 'No, you want me to come in so you can see if I know how to dress 
presentably or have hair coming out of my ears and then you can tick off 
another 'In Office Interview' on your weekly status report.  Are you going 
to at least buy me lunch?'

P: (nervous laugh) 'No, but we have a lovely coffee machine...'

M: 'That's nice... I'll tell you what, when you have a real, live client 
to submit me to then arrange the interview with them in the afternoon; 
I'll stop by in the morning and sign the appropriate paperwork and you can 
look me over then.'

>
>.. Interviewing with 5 clients. 
…[3 more quoted lines elided]…
>the same day, a Friday. 

That's interesting... I *never* get Good News on a Friday, in fact I have 
the category of 'Friday Afternoon Look Busy' call just for when the pimps 
are making such.  I've found that, in general, if I am not on site and 
working within 48 hours of the client receiving the fax/email of my papers 
then the slot is dead.

[snip]

>It was like that in the US during the 90s. No longer. I've worked for
>the same contracting
>company twice, but never consecutively. Every time a project ends, I'm
>starting from
>scratch.

I've never worked for the same company twice, even non-consecutively.  
I've had pimps beg and plead for me to hold off putting my papers on the 
streets for (a day, two days, until the next Wednesday status meeting, 
until the Account Reps' Group Meeting on the 15th, etc) but when I ask how 
much I'll be paid for keeping myself off the market they get awfully 
quiet.

I call the pimp and say 'I was just told my contract's coming down at tne 
end of the day/week/month... do you have anyone like up who might need my 
skills?'

The pimp is *always* surprised and *never* has anything... so they do 
their jobs (which is to find clients where I can work) and I do mine 
(which is find pimps who have clients where I can work).  It's a bit of a 
race and I've never seen a pimp 'win' it.

DD
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 17)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-03T21:19:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <22p99452rh1df8lr0hf1o6psbgvsu3id4g@4ax.com> <6fkhg0Fc0ck4U1@mid.individual.net> <oh5a94djujajtek423m6e7rui63bfjsip3@4ax.com> <g74ero$bnd$1@reader1.panix.com>`

```
On Sun, 3 Aug 2008 14:20:40 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <oh5a94djujajtek423m6e7rui63bfjsip3@4ax.com>,
>Robert  <no@e.mail> wrote:
…[13 more quoted lines elided]…
>to everyone there...

Posting it on DICE and maybe Monster is more efficient. 

>... and then waits a bit for the flurry of 'RECIPIENT NOT FOUND' or 
>'DOMAIN DOES NOT EXIST' replies.  Agencies come and go with all the 
>permanence of wildflowers after a desert rain.

Don't bother answering online ads. An estimated 50% of them are phony. I've seen ads that
I knew for certain were filled a year earlier, because I filled them.

>Then, after dealing with the 'pimples' (junior-level pimps) who have been 
>assigned to 'New Contacts' ('Please, turn to page three and notice the 
>date of that first technical certification... yes, that's right, the one 
>that's before either of your parents were born.  What were you asking 
>about experience?') 

They want RECENT experience. It is generally thought that experience more than ten years
ago is irrelevant. Some recruiters say five years. 

They don't want a similar match, they want an EXACT match with the brand name. If the
client wants Micro Focus Cobol, your experience with Fujitsu or mainframe Cobol is
worthless. If the client wants Oracle, don't bother talking about DB2 or Informix. When I
was new to the game, I tried explaining that Cobol and SQL are ANS Standard languages.
Recruiters didn't know what I was talking about. 

Applicants don't understand that recruiters have never seen a program written in any
language. They have no concept of what a compiler or database do. Their only skill is
matching keywords, like a search engine. 

>and the requests for 'Hairy Ears' interviews:
>
>P: 'We'd like you to come in and talk to you about what Sell-ur-Assco is 
>all about.'

Some spend half their ad selling the contracting company, telling you they're the largest,
fastest growing or have the highest level of certification. ALL Indian companies are CMM
Level 5. They don't seem to know the difference between a worker and a client. 

When a US contracting company is acquired by an Indian one, everything turns to shit.
Talking to such companies is a waste of time, because they don't have any jobs. 

They also know very little about the client, basically only what it says on the job req.

>M: 'No, you want me to come in so you can see if I know how to dress 
>presentably or have hair coming out of my ears and then you can tick off 
>another 'In Office Interview' on your weekly status report.  Are you going 
>to at least buy me lunch?'

I've encountered only twice, from old-line temp agencies like Robert Half and Kelly. Those
agencies are bottom feeders. Their clients are undesirable places to work and they don't
pay enough.

I once went to the contract company office, where I saw a whiteboard in a conference room
listing all the jobs they were trying to fill.  Both of them. 

>P: (nervous laugh) 'No, but we have a lovely coffee machine...'
>
…[16 more quoted lines elided]…
>then the slot is dead.

That's the pimp's requirement, not the client's. The pimp is afraid you'll get a better
offer. The same thing happened to me twice. 

-- Friday --
Pimp: The client insists you be there at 8am sharp on Monday.
Me: OK, I'll have to drive all weekend , but I'll be there.
Pimp: Remember, 8am sharp.
--- Saturday, cell phone rings while driving --
Pimp: How is the move going?
Me: I'm in Tulsa, should be in Overland Park Sunday afternoon.
Pimp: Uhhh .. it looks like the client won't be ready for you Monday. 
Me: You told me they insisted on 8am sharp. You didn't make that up, did you?
Pimp: There's been a change. Now they want you Wednesday at 9:30. 
Me: Will Monday and Tuesday be billable?
Pimp: Of course not. 
Me: You're my employer and you ordered me to be there. Will you at least pay for the
hotel?
Pimp: We don't pay your expenses. Your rate is all inclusive. 

The solution is simple. When interviewing with the client, ask whether your desired start
date would be ok. They usually say yes. 

>>It was like that in the US during the 90s. No longer. I've worked for
>>the same contracting
…[18 more quoted lines elided]…
>race and I've never seen a pimp 'win' it.

Tech Mahindra moves its people to other sites. I don't think they hire Occidentals.

In the 90s, there were two working arrangements: salaried and hourly. Salaried made $20K
less in exchange for paid bench time between projects. Now, salaried people are fired on
the last day. Anyone who elects salaried is a sucker for giving up $20K for an empty
promise.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 18)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-04T09:34:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g76iep$77r$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <oh5a94djujajtek423m6e7rui63bfjsip3@4ax.com> <g74ero$bnd$1@reader1.panix.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com>`

```
In article <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sun, 3 Aug 2008 14:20:40 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[17 more quoted lines elided]…
>Posting it on DICE and maybe Monster is more efficient. 

I prefer to deal with the people I've already dealt with, if only to make 
things easier on my references.  Have you ever gotten a good hit from so 
public a posting?

[snip]

>>Then, after dealing with the 'pimples' (junior-level pimps) who have been 
>>assigned to 'New Contacts' ('Please, turn to page three and notice the 
…[6 more quoted lines elided]…
>ago is irrelevant. Some recruiters say five years. 

If what they were asking about had anything to do with the job I might 
understand that... but, at times, they're asking about something else 
entire, perhaps they are trying to see if I fit, precisely, into another 
jigsaw-puzzle they have.  If they trot out the 'recent experience' saw 
I'll suggest that they sell it to the client differently... sometimes it 
works, sometimes no.

[snip]

>>and the requests for 'Hairy Ears' interviews:
>>
…[7 more quoted lines elided]…
>Level 5. They don't seem to know the difference between a worker and a client. 

My response is a simple 'I'm sure yours is a lovely company.  Tell me, 
what would I do if my paycheck were not deposited to my account by our 
usually agreed-upon date?'... and I base further conversations on the 
reply.

[snip]

>>That's interesting... I *never* get Good News on a Friday, in fact I have 
>>the category of 'Friday Afternoon Look Busy' call just for when the pimps 
…[17 more quoted lines elided]…
>Pimp: There's been a change. Now they want you Wednesday at 9:30. 

Me: 'Looks like you've promised them something they want but won't get.  
I'll be pulling over at the nearest Hourly Rates Motel and re-posting my 
availability.  This 'change' is costing me money and I am not in business 
to do that.  Please call the client on Monday and tell them to find 
someone else... oh, and take my bragsheet out of your database while 
you're at it; I don't see you as fulfilling the duties of an 'agent' and I 
see no reason why you should earn money from my billed hours as being 
one.'

DD
```

###### ↳ ↳ ↳ CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 19)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-08-04T13:11:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <oh5a94djujajtek423m6e7rui63bfjsip3@4ax.com> <g74ero$bnd$1@reader1.panix.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com>`

```
On Aug 4, 5:34 am, docdw...@panix.com () wrote:

Goodness, a veritable gem of dialogue deeply situated in the otherwise
Technical Discussion... And an opportunity to learn how to change the
Subject Line within the Google web interface. Have I succeeded?

>
> >>[snip]
>
> >>Mr Wagner and I seem to have remarkably similar experiences in this
> >>matter.

I have some bona fides to add to the mix - I've done only contracting
for about 35 years, with only a couple of short detours as a W-2, the
latest of which was during the Great IT Famine of 2001-2002, where I
had to accept "employee" status. One does what one needs to in order
to survive. When the opportunity presented itself, I returned to
"contracting".

> Mr. Wagner: >Posting it on DICE and maybe Monster is more efficient.
>Doc:
…[3 more quoted lines elided]…
>

I've used both Job boards. Yes, it is very efficient at obtaining
recruiter / agency inquiries. Sometimes "too" efficient, because the
agencies are not particularly adept at doing their "screening", so it
can be time-waster as well. Also, there can be multiple posts by
multiple agencies for the same client slots. What to do in "choosing"
the "right" agency? Such are the problems of "going back to square
one." Soliciting repeat business and polling your informal network of
past co-workers avoids some of those problems, but doesn't always
result in a "hit". So we all need to have as many different "arrows in
our quiver" as we can manifest. What works for others might not work
for me, but hearing of what works for others can compensate for a lack
of imagination on my part.

All worthwhile comments from everyone; thanks for all your
observations. Given time, I may Reply to some of the specifics.

Til then, I contribute this: I believe it worthwhile for one to think
about what your interaction style, your "boundaries", and "what is
important to you". This sounds trite, but I believe it to be true, and
transcending some of the mundane "technical" issues.

For me, it took about thirty years to distill all this down to what I
call my Rules of Engagement. I've gone minimalist, reducing them to
two:

Rule 1: Rate and Terms are negotiable; professional courtesy and
respect are not.

Rule 2: In consideration of my submission of my resume, you will keep
me informed of all progress, or lack thereof, of my submission to your
client.

I now "require" an Agency to verbally agree to these before I e-mail
them my resume. I believe it is okay to be _insistent_, if what you
are insisting upon is eminently reasonable.

What should be emphasized here is that Agencies may "use" your
Resume / CV in any number of ways: for a specific submission for
specific slot to a client, to build their resume database, to include
in a fat proposal to a client under a section Our People, trolling for
skills / rates (as duly noted by DD to the job posts without rates),
and other reasons. So offering your Resume to the Agency is giving
them _something of value_ - it is not only reasonable, it is almost a
_duty_ to your fellow Contractor Peers, to require _something_ in
return. That _something_ should be the promise to _keep you informed_.
Can we think of anything else we could require in the "exchange"?
(I've not come up with anything else.)

Insisting on these Rules of Engagement is one way I filter out the
trolls from the real job posts. It helps.

Ken
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 20)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-05T00:06:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g785ii$mj3$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com>`

```
In article <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:
>On Aug 4, 5:34�am, docdw...@panix.com () wrote:
>
>Goodness, a veritable gem of dialogue deeply situated in the otherwise
>Technical Discussion... And an opportunity to learn how to change the
>Subject Line within the Google web interface. Have I succeeded?

The Subject: line is changed, according to my newsreader (trn)... I'm 
still looking for gems, though.

[snip]

>> Mr. Wagner: >Posting it on DICE and maybe Monster is more efficient.
>>Doc:
…[9 more quoted lines elided]…
>multiple agencies for the same client slots.

One item at a time, then.  First, some agencies, at time, use the 'throw 
enough fertiliser at the wall and some of it will stick'; they do this 
with resumes sent to clients and they do this with calls to consultants to 
take jobs.  One can only hope to stick.

Different agencies posting the same client slot are, thanks to the 
Internet, becoming easier to spot, as well; the wording of the ads become 
similar to the point of identical.  If (n) agencies are all posting the 
same position how does one choose which agency is the best?  The only 
single solution is to realise that there is no single solution, including 
this one... so one just throws some fertiliser against the wall and see 
what sticks.

[snip]

>Til then, I contribute this: I believe it worthwhile for one to think
>about what your interaction style, your "boundaries", and "what is
…[8 more quoted lines elided]…
>respect are not.

Yes... and no.  Some rates and terms are, in themselves, insults; 
conversation beyond them would be (for the slot in question).  Countless 
times I've had the interchange:

Pimp: 'So, we need a dozen years of mainframe COBOL, a decade of CICS, a 
half-dozen years of DB2 and (industry-specific experience)... all that 
looks to be in your resume.'

Me: 'Multiples of all of those are in my resume.  Where's the job located 
and how long is the contract?'

Pimp: 'The location is (high cost-of-living area) and the initial duration 
is three months... but That's Going To Be Extended, of course.'

Me: 'Of course... but until it is extended is it not extended.  What kind 
of rate are they offering?'

(pause for dancing... but I Asked First)

Pimp: 'Well, on a corp-to-corp basis they're willing to pay... five times 
the Federal Minimum Wage Rate.'

Me: 'They expect that set of skills for that kind of money?  I hope they 
are very happy with whoever they get for the gig, it won't be me.'

Pimp: 'Well, what'll it take to make you happy?'

Me: 'It will take double that to make me happy.'

Pimp: 'You want double that rate?!?'

Me: 'No, I *want* triple it... but I'd be happy for double it... and 
starting as low as they are I don't think we'll get even close to it.'

Pimp: 'I can't tell the client that!'

Me: 'Then maybe you should just tell them that I hope they'll be very 
happy with whoever they get... because it isn't going to be me.'

>
>Rule 2: In consideration of my submission of my resume, you will keep
>me informed of all progress, or lack thereof, of my submission to your
>client.

Mr Shafer, my experience has told me that such a request would be met with 
an enthusiastic 'Yes!' and nothing more... *except* when the client says 
they want to see me in person.  Pimps are Very Busy People - just like 
Managers! - and they seem to exist in a part of space/time called 'just 
about to call you'.

[snip]

>What should be emphasized here is that Agencies may "use" your
>Resume / CV in any number of ways: for a specific submission for
…[7 more quoted lines elided]…
>Can we think of anything else we could require in the "exchange"?

I can think of many things... a corner office, a company car and a box of 
chocolates... *good* chocolates, too, not those cheap ones from the 
gas-station convenience store, those horrid chocolates that taste like 
stale cigarettes and brake-fluid... 

... but I have my doubts that such 'requirements' would be filled.  What 
happens is that the pimp gets my bragsheet, calls my references - and 
sometimes even manages to speak with them! - and then fires off my papers 
at anything that even vaguely seems to be fertile ground.

By the time I discover copies of my Curriculum Vitae littering the floor 
of the bus-terminal... the pimp has moved on to something else, the agency 
has a new person in the position and everything becomes The One Who's Just 
Left's Fault.

DD
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 21)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-08-04T18:31:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d93493b6-c84d-481a-b417-9b0470a9fded@j22g2000hsf.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <g785ii$mj3$1@reader1.panix.com>`

```
On Aug 4, 8:06 pm, docdw...@panix.com () wrote:
> In article <29f6a466-11d5-4953-9bcb-6e319e6f9...@2g2000hsn.googlegroups.com>,
>
…[8 more quoted lines elided]…
> still looking for gems, though.

Then I'll try to help. From a Snail's eye view, they will look like
boulders :-)...

>
> [snip]
…[12 more quoted lines elided]…
> what sticks.

Doc, this is really NOT helpful at all! I was expecting some kind of
stochastic process heuristic based upon a module-n function on the
Agency's name in hexadecimal, or similar... :-).

>
> [snip]
…[15 more quoted lines elided]…
> times I've had the interchange:

I've never been "offended" by the low rates. But sometimes they *are*
opportunities to have some *fun*, rather than "serious" negotiation,
to wit,

Pimp: The rate is x dollars per hour (where x is some absurdly low
number.)

Me: The rate is _what_? Hmmmm... if that's the rate, then how about
_you_ and your other recruits coming to work for *me*! (said with
laughter, because since no work will come of this, I'm at least due
some <grins>)

>
> >Rule 2: In consideration of my submission of my resume, you will keep
…[8 more quoted lines elided]…
>

Hmmm... my experience is a wee bit different, but that is why we talk
here, is it not? Sometimes my citation of the Rules of Engagement is
met by stony silence, as if the recruiter is in stark disbelief.
Sometimes it has actually worked :-), as the recruiter did his best to
"keep me informed." Other times it afforded me "license" to bug him at
will about where we stood, and to apply a bit of pressure for him to
find out if he didn't know. Where I come from, this is called
"pushback". Is there a similar concept in NYC? :-)

> [snip]
>
…[9 more quoted lines elided]…
> >Can we think of anything else we could require in the "exchange"?

>
> I can think of many things... a corner office, a company car and a box of
> chocolates... *good* chocolates, too, not those cheap ones from the
> gas-station convenience store, those horrid chocolates that taste like
> stale cigarettes and brake-fluid...

My saintly Father, may he sleep with the angels, to paraphrase the Doc
hisself, spent a lifetime in the petroleum industry, I'll have you
know. So that *taste*, that *smell*, Doc, is the *taste* and *smell*
of _money_, as recent corporate quarterly profit statements from Exxon-
Mobil will soundly attest. Them are *very good* chocolates indeed.

>
> ... but I have my doubts that such 'requirements' would be filled.  What
…[7 more quoted lines elided]…
> Left's Fault.

This I take it to mean that such Agency has fallen off our Preferred
Vendors List, does it not?

>
> DD

Ken
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 22)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-05T12:39:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g79hle$91l$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <g785ii$mj3$1@reader1.panix.com> <d93493b6-c84d-481a-b417-9b0470a9fded@j22g2000hsf.googlegroups.com>`

```
In article <d93493b6-c84d-481a-b417-9b0470a9fded@j22g2000hsf.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:
>On Aug 4, 8:06�pm, docdw...@panix.com () wrote:

[snip]

>> �If (n) agencies are all posting the
>> same position how does one choose which agency is the best? �The only
…[6 more quoted lines elided]…
>Agency's name in hexadecimal, or similar... :-).

The fewer one's expectations are, the fewer one's disappointments might 
be... or so I was taught.

[snip]

>> Yes... and no. �Some rates and terms are, in themselves, insults;
>> conversation beyond them would be (for the slot in question). �Countless
>> times I've had the interchange:
>
>I've never been "offended" by the low rates.

That something is a well, Mr Shafer, in no wise requires one to take water 
from it; similarly, that something is an insult does not require one to 
take offense from it.  To show that one is unaware of the insult can be a 
Good Thing, as it may lead one's opponent into a position where one 
might find greater advantage...

... and it can be a Bad Thing, since when the Emperor suddenly finds out 
how truly fine his New Clothes are he may have some strong words for his 
advisors.

[snip]

>> Mr Shafer, my experience has told me that such a request would be met with
>> an enthusiastic 'Yes!' and nothing more... *except* when the client says
…[12 more quoted lines elided]…
>"pushback". Is there a similar concept in NYC? :-)

As noted above, the concept I've encountered is 'we've submitted your 
papers to the client and if we even *think* we can make money off you then 
we'll be on you like the white on rice... until then please don't call 
us'.

[snip]

>> I can think of many things... a corner office, a company car and a box of
>> chocolates... *good* chocolates, too, not those cheap ones from the
…[7 more quoted lines elided]…
>Mobil will soundly attest. Them are *very good* chocolates indeed.

I do not expect the palates of others to be the same as mine, Mr Shafer... 
so when I want the taste of petroleum products in my candies I appreciate 
being given the choice to mix them to my own taste.  Granted that I've 
heard there's nothing like a couple of good, solid swigs out of the 
ethylene glycol jug... you'll just about die trying to find something like 
it.

[snip]

>> By the time I discover copies of my Curriculum Vitae littering the floor
>> of the bus-terminal... the pimp has moved on to something else, the agency
…[4 more quoted lines elided]…
>Vendors List, does it not?

Of course it doesn't... because there's Someone New there, everything that 
happened was the fault of the One Who's Just Left.  The turnover in 
personnel and agencies is rapid enough that it seems the Preferred Vendors 
List is occupied by the one whose checks are currently clearing the bank.

DD
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 21)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-05T00:13:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q0of94tj6t5c00qcd0siue3mvbo78tjj4o@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <g785ii$mj3$1@reader1.panix.com>`

```
On Tue, 5 Aug 2008 00:06:42 +0000 (UTC), docdwarf@panix.com () wrote:

>What happens is that the pimp gets my bragsheet, calls my references - and 
>sometimes even manages to speak with them! - and then fires off my papers 
>at anything that even vaguely seems to be fertile ground.

You should never give references before the first interview. If the referee is a manager
who hires contractors, agencies will it as a Sales Lead. If they reach the person, they'll
spend most of the conversation trying to sell him another body.
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 22)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-05T12:42:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g79hs0$gvi$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <g785ii$mj3$1@reader1.panix.com> <q0of94tj6t5c00qcd0siue3mvbo78tjj4o@4ax.com>`

```
In article <q0of94tj6t5c00qcd0siue3mvbo78tjj4o@4ax.com>,
Robert  <no@e.mail> wrote:
>On Tue, 5 Aug 2008 00:06:42 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[4 more quoted lines elided]…
>You should never give references before the first interview.

I try not to, Mr Wagner, but there have been more than a few times when a 
pimp has stated 'Your papers don't go out the door until I speak to your 
references.'

What I usually do is supply names from positions a few years old; if the 
pimps call they get a response along the lines of 'Mistah Kurz?  He 
dead!'... and I've been surprised by how a good recommendation from a dead 
reference is sufficient to allow a pimp to submit my papers.

DD
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 22)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-08-05T12:36:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cdcde734-5152-4e73-882d-ed71b8887f33@b1g2000hsg.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <g785ii$mj3$1@reader1.panix.com> <q0of94tj6t5c00qcd0siue3mvbo78tjj4o@4ax.com>`

```
On Aug 5, 1:13 am, Robert <n...@e.mail> wrote:
> On Tue, 5 Aug 2008 00:06:42 +0000 (UTC), docdw...@panix.com () wrote:
>
> You should never give references before the first interview. If the referee is a manager
> who hires contractors, agencies will it as a Sales Lead. If they reach the person, they'll
> spend most of the conversation trying to sell him another body.

I'm glad you reminded me of this one: there's one more thing you can
do when faced with a jerk recruiter - you can "revoke" the
references. :-)

One time I was working with a rep who insisted on references, and
being able to phone them, and I lined them up, and sent the contact
info over, but with the qualifier, "For reference A, please call only
after 4:00pm". This was at Reference A's request, for he was in a
tight spot at work, under the gun, and didn't want to be seen talking
on the phone during prime work hours. Of course, the rep didn't need
to know that, all he needed to know was "Call after 4:00pm".

Well, the rep called about 10:30am one morning, and Reference A, a
very decent fellow, let me know, though he wasn't angry with _me_. So
I called up the rep and revoked ALL THE REFERENCES, because by
breaking the Rules he was jeopardizing the jobs of my friends who were
sticking out the necks on my behalf to satisfy HIS request.

First the rep denied that I ever made such restriction, did I pointed
out his lie by citing the e-mail reference, where it was plain for all
to see. Then I got a sheepish apology. I believed it heartfelt, so I
forgave him. Never did do business with them though.

As far as using references as Sales Leads, I have heard of another
trick as equally or more devious. I am somewhat reluctant to post it
here, for fear that I unwittingly will perpeatuate this unscrupulous
practice, but what the hey, here goes...

Some agencies will post phantom job ads with descriptions like "AS/
400" or "Z/OS experience" in an effort to survey the area to find
those shops via respondents citing the company's name in their
Experience section. They're not trolling for resumes. They're trolling
for clients. They already have the recruits. They are using "new
recruits" to tell them two things -
1. where the clients are;
2. where the unhappy employees are :-), for maybe there will be
vacancies soon, and opportunities for business.

ken
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 21)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-08-05T07:06:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<InXlk.32498$co7.141@nlpi066.nbdc.sbc.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <g785ii$mj3$1@reader1.panix.com>`

```
<docdwarf@panix.com> wrote in message news:g785ii$mj3$1@reader1.panix.com...
> What happens is that the [recruiter] gets my bragsheet, calls my 
> references - and
> sometimes even manages to speak with them! - and then fires off my papers
> at anything that even vaguely seems to be fertile ground.

One cannot know if the ground is fertile lest he tills and sows.


MCM
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 22)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-08-05T08:14:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p0og9496nfv29ovudl1ha2u7p67fnhdbuf@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <g785ii$mj3$1@reader1.panix.com> <InXlk.32498$co7.141@nlpi066.nbdc.sbc.com>`

```
On Tue, 5 Aug 2008 07:06:41 -0500, "Michael Mattias"
<mmattias@talsystems.com> wrote:

>> sometimes even manages to speak with them! - and then fires off my papers
>> at anything that even vaguely seems to be fertile ground.
>
>One cannot know if the ground is fertile lest he tills and sows.

But it is often quite obvious that some ground is infertile.
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 23)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-08-05T10:14:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88_lk.20582$N87.12032@nlpi068.nbdc.sbc.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <g785ii$mj3$1@reader1.panix.com> <InXlk.32498$co7.141@nlpi066.nbdc.sbc.com> <p0og9496nfv29ovudl1ha2u7p67fnhdbuf@4ax.com>`

```
"Howard Brazee" <howard@brazee.net> wrote in message 
news:p0og9496nfv29ovudl1ha2u7p67fnhdbuf@4ax.com...
> On Tue, 5 Aug 2008 07:06:41 -0500, "Michael Mattias"
> <mmattias@talsystems.com> wrote:
…[7 more quoted lines elided]…
> But it is often quite obvious that some ground is infertile.

"Obvious"==> ASSUMPTION.

What do you think, resumes aren't tailored to a particular circumstance? I 
have on many occasions suprised my clients by telling them, "Oh, I can do 
that."  They didn't know, because they had never asked. And I had never 
perceived their potential use of said particular skill so I had never told 
them - my bad.

Then again, I think much of this discussion revolves around the mass-market 
"contracting" industry, in which I have not been for a long time.


MCM
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 24)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-08-05T12:58:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<502f1c39-8e01-44b0-82da-63cd5e8012f7@m36g2000hse.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <g785ii$mj3$1@reader1.panix.com> <InXlk.32498$co7.141@nlpi066.nbdc.sbc.com> <p0og9496nfv29ovudl1ha2u7p67fnhdbuf@4ax.com> <88_lk.20582$N87.12032@nlpi068.nbdc.sbc.com>`

```
On Aug 5, 11:14 am, "Michael Mattias" <mmatt...@talsystems.com> wrote:
> "Howard Brazee" <how...@brazee.net> wrote in message
>
…[19 more quoted lines elided]…
> them - my bad.

This is why it is good advice from Mr. Pete to keep an open mind
during the interview (or for that matter, on the job itself) to be
receptive to these opportunities when they pop up.

>
> Then again, I think much of this discussion revolves around the mass-market
> "contracting" industry, in which I have not been for a long time.

Funny how it never seemed a "mass" of opportunties available to me,
but then again, I was for many years in the Honeywell/Bull niche and
only relatively lately (the last 4-5 years) was able to beef up the
IBM line item.

And yet, I think I understand what Howard is pointing out - if a field
fails to yield crops year after year, it's better to look for a new
field.

ken
```

###### ↳ ↳ ↳ Honeywell Bull and other mainframes was Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 25)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2008-08-05T21:18:34-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sarh945q2dduh4ak4rogckb3obk66s69oo@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <g785ii$mj3$1@reader1.panix.com> <InXlk.32498$co7.141@nlpi066.nbdc.sbc.com> <p0og9496nfv29ovudl1ha2u7p67fnhdbuf@4ax.com> <88_lk.20582$N87.12032@nlpi068.nbdc.sbc.com> <502f1c39-8e01-44b0-82da-63cd5e8012f7@m36g2000hse.googlegroups.com>`

```
On Tue, 5 Aug 2008 12:58:30 -0700 (PDT), "klshafer@att.net"
<klshafer@att.net> wrote:

>On Aug 5, 11:14ï¿½am, "Michael Mattias" <mmatt...@talsystems.com> wrote:
>> "Howard Brazee" <how...@brazee.net> wrote in message
…[33 more quoted lines elided]…
>IBM line item.

Is Honeywell Bull still around and improving their mainframe offering
(if any)?  Does HP have any true mainframe offering?  How well are the
Unisys components doing?
>
>And yet, I think I understand what Howard is pointing out - if a field
…[3 more quoted lines elided]…
>ken
```

###### ↳ ↳ ↳ Re: Honeywell Bull and other mainframes was Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 26)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-08-05T18:32:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a283231f-7212-4859-9c60-e969a9281ff2@m36g2000hse.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <g785ii$mj3$1@reader1.panix.com> <InXlk.32498$co7.141@nlpi066.nbdc.sbc.com> <p0og9496nfv29ovudl1ha2u7p67fnhdbuf@4ax.com> <88_lk.20582$N87.12032@nlpi068.nbdc.sbc.com> <502f1c39-8e01-44b0-82da-63cd5e8012f7@m36g2000hse.googlegroups.com> <sarh945q2dduh4ak4rogckb3obk66s69oo@4ax.com>`

```
On Aug 5, 8:18 pm, Clark F Morris <cfmpub...@ns.sympatico.ca> wrote:
> On Tue, 5 Aug 2008 12:58:30 -0700 (PDT), "klsha...@att.net"
>
…[3 more quoted lines elided]…
>

About twenty-five or thirty years ago the Honeywell Large Scale Users
Association (HLSUA), their mainframe user group, had about 200-300
members nationwide (U.S.) Though I do not know for certain, my
impression is that it is less than 10% of that today. I know of a few
sites: State of New Jersey (I think), State of Michigan, and maybe
J.D. Edwards in St. Louis? I believe Bull still has a significant
facility in Phoenix which maybe has turned into a large service bureau
where many of their mainframe clients offloaded their processing.

(I know of a fellow, a Mr. Ed Weller, through another board (Yahoo's
SW-Improve) who was a heavyweight in the Honeywell/Bull GCOS (their
OS) development and support. A very, very smart guy. And a strong
advocate of formal software inspections, I do recall.)

Otherwise, Bull, or Groupe Bull as I think they are known, is now
pretty much only a European operation. Perhaps our European friends
here can provide more information?

I know even less of HP and Unisys. The old Burroughs plant is in
Plymouth, MI, and bears the Unisys logo, but there are very few cars
in their parking lot. I think it is a hardware support facility, but I
am not sure. I recall someone here discussing Unisys just a few weeks
ago (probably should have searched the group posts to provide you a
cite), and they are still HQ'd in Pennsylvania, I believe I read.

ken
```

###### ↳ ↳ ↳ Re: Honeywell Bull and other mainframes was Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 26)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-05T23:20:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3s8i94d82q6mbo0cjpn0844pjn31504ltr@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <g785ii$mj3$1@reader1.panix.com> <InXlk.32498$co7.141@nlpi066.nbdc.sbc.com> <p0og9496nfv29ovudl1ha2u7p67fnhdbuf@4ax.com> <88_lk.20582$N87.12032@nlpi068.nbdc.sbc.com> <502f1c39-8e01-44b0-82da-63cd5e8012f7@m36g2000hse.googlegroups.com> <sarh945q2dduh4ak4rogckb3obk66s69oo@4ax.com>`

```
On Tue, 05 Aug 2008 21:18:34 -0300, Clark F Morris <cfmpublic@ns.sympatico.ca> wrote:

>Is Honeywell Bull still around and improving their mainframe offering (if any)? 

Yes. It is now called Groupe Bull. 

> Does HP have any true mainframe offering? 

They make SuperDome servers that are bigger than many mainframes, and are used like
mainframes.  I work on them. A typical machine has 64-128 CPUs, 1TB of memory, sells for
several million dollars. They sit at the center of most US telecom companies. I think
they're used in airline reservations, but have never worked in that industry.

> How well are the Unisys components doing?

Not well. More than 80% of Unisys' revenue comes from services, not hardware. Incredibly,
Unisys is still making Burroughs-based machines.
```

###### ↳ ↳ ↳ Re: Honeywell Bull and other mainframes was Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 27)_

- **From:** bo774@FreeNet.Carleton.CA (Kelly Bert Manning)
- **Date:** 2008-08-12T06:11:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g7r9j7$khi$1@theodyn.ncf.ca>`
- **References:** `<elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <g785ii$mj3$1@reader1.panix.com> <InXlk.32498$co7.141@nlpi066.nbdc.sbc.com> <p0og9496nfv29ovudl1ha2u7p67fnhdbuf@4ax.com> <88_lk.20582$N87.12032@nlpi068.nbdc.sbc.com> <502f1c39-8e01-44b0-82da-63cd5e8012f7@m36g2000hse.googlegroups.com> <sarh945q2dduh4ak4rogckb3obk66s69oo@4ax.com> <3s8i94d82q6mbo0cjpn0844pjn31504ltr@4ax.com>`

```
Robert (no@e.mail) writes:
> 
> Yes. It is now called Groupe Bull. 

What is the architecture like these days?

The GCOS 2H to 4JS ones I worked on until 1980 had a 36 bit word size
with a byte size of 4, 6, 7, or 8 bits.

That had some interesting consequences in their interpretation of a group
move of a COMP-3 item to a mixed or character only item, among other gotchas.

It treated COMP-3 as 4 bit bytes and did 4 to big byte conversions. No
visible indication, unless you asked for a pseudo assembler listing of the
generated object code.

The compiler kept forgetting to write the last partial block, so I would
write the trailer record enough times to guarantee a full block.

One irony was that we could never get their PL/I compiler to work, even
though their COBOL compiler was written in PL/I. Go figure.
```

###### ↳ ↳ ↳ OT: IT Contracting WAS: Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 20)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-08-05T13:40:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6fppc6Fccpn1U1@mid.individual.net>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <oh5a94djujajtek423m6e7rui63bfjsip3@4ax.com> <g74ero$bnd$1@reader1.panix.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com>`

```


<klshafer@att.net> wrote in message 
news:29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com...
On Aug 4, 5:34 am, docdw...@panix.com () wrote:

Goodness, a veritable gem of dialogue deeply situated in the otherwise
Technical Discussion... And an opportunity to learn how to change the
Subject Line within the Google web interface. Have I succeeded?

[Pete]

Almost...  It needs to be preceded by "OT:"

>
> >>[snip]
>
> >>Mr Wagner and I seem to have remarkably similar experiences in this
> >>matter.

I have some bona fides to add to the mix - I've done only contracting
for about 35 years, with only a couple of short detours as a W-2, the
latest of which was during the Great IT Famine of 2001-2002, where I
had to accept "employee" status. One does what one needs to in order
to survive. When the opportunity presented itself, I returned to
"contracting".

[Pete]

Do you think that "Contracting" requires a different mind set from 
"Permanent"?

Discuss... :-)

> Mr. Wagner: >Posting it on DICE and maybe Monster is more efficient.
>Doc:
…[3 more quoted lines elided]…
>

I've used both Job boards. Yes, it is very efficient at obtaining
recruiter / agency inquiries. Sometimes "too" efficient, because the
agencies are not particularly adept at doing their "screening", so it
can be time-waster as well. Also, there can be multiple posts by
multiple agencies for the same client slots.

[Pete]

I sent some feedback to "JobServe UK" a couple of days ago, on this very 
subject.

Although I'm not currently looking for a job, I like to keep an eye on 
things. I reckon they should offer a tick box which causes only UNIQUE jobs 
to show. Where multiple Agencies had submitted the same job, only the entry 
for the  FIRST would show. Once you had found a job you were interested in, 
you could turn off the box and see if other agents had a better job 
description, rate, etc.

They came back and said it was technically impossible. (A limited vision, I 
thought...)
[/Pete]


What to do in "choosing"
the "right" agency? Such are the problems of "going back to square
one." Soliciting repeat business and polling your informal network of
past co-workers avoids some of those problems, but doesn't always
result in a "hit". So we all need to have as many different "arrows in
our quiver" as we can manifest. What works for others might not work
for me, but hearing of what works for others can compensate for a lack
of imagination on my part.

[Pete]

I haven't seen any demonstrated lack of imagination here, by you, Ken...:-)

I believe the idea is to find out what is needed and wanted, and then 
provide that.

It isn't any good saying: "I'm a COBOL programmer, look what an awful life I 
have as a contractor...pimps, and managers, and outsourcing, and yada yada 
yada". Maybe the days of COBOL contracting are coming to a close (Gosh, ... 
d'ja think?).

The world no longer buys hand made lace. Blame the cotton bushes.

Employment, whether contract or permanent (I hate that word, there's nothing 
"permanent" about it...), is a simple marketplace which follows the rules of 
supply and demand. If you can provide what is wanted, you can make a good 
living.

I started working as a contract programmer (in COBOL) in 1975.  I haven't 
done that for a living since 1995. The market changed and the consequent 
demand changed. I moved with it. Diversification is often a valid way to 
expand a business. No less so with COBOL programming.
[/Pete]


All worthwhile comments from everyone; thanks for all your
observations. Given time, I may Reply to some of the specifics.

Til then, I contribute this: I believe it worthwhile for one to think
about what your interaction style, your "boundaries", and "what is
important to you". This sounds trite, but I believe it to be true, and
transcending some of the mundane "technical" issues.

For me, it took about thirty years to distill all this down to what I
call my Rules of Engagement. I've gone minimalist, reducing them to
two:

Rule 1: Rate and Terms are negotiable; professional courtesy and
respect are not.

Rule 2: In consideration of my submission of my resume, you will keep
me informed of all progress, or lack thereof, of my submission to your
client.

[Pete]

Yes, these are excellent. But don't lose sight of the Marketplace...

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 21)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-08-05T11:12:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a99ef1b0-8071-4025-97ac-613e698a7617@b1g2000hsg.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <oh5a94djujajtek423m6e7rui63bfjsip3@4ax.com> <g74ero$bnd$1@reader1.panix.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <6fppc6Fccpn1U1@mid.individual.net>`

```
On Aug 4, 9:40 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> <klsha...@att.net> wrote in message
>
…[10 more quoted lines elided]…
>

I rather think not. It is a change of Subject to be sure. It is also
On Topic. Spot On Topic. And the topic is not just Contracting, it is
Contracting in the CoBOL world. Hence, CoBOL and Contracting.

>
>
…[15 more quoted lines elided]…
> "Permanent"?

I don't know if I would use the phrase "mind set" in this instance.
What I would say is that Contracting requires a different
"temperament". But I don't necessarily think that CoBOL contracting
requires a different temperament than Java or C++ contracting, but
maybe it does. I'm ready to be illuminated if others think so.

>
> Discuss... :-)
…[27 more quoted lines elided]…
> [/Pete]

And the duplicates also "skew" what I use as a very, very gross
measure of the robustness/demand in the marketplace - the total number
of jobs posted on DICE.

>
> What to do in "choosing"
…[10 more quoted lines elided]…
> I haven't seen any demonstrated lack of imagination here, by you, Ken...:-)

If I've shot all the arrows in quiver, and still haven't hit target,
it matters not how many I started with. I'm still left with zero. In
that case, I'm grateful for what other arrows (ideas) others might
lend to me.

>
> [snip]
…[3 more quoted lines elided]…
> d'ja think?).

I appreciate your heartfelt concern. Being aware of that, if some of
us choose to play out the CoBOL end game as we see fit, and best we
can, what is that to you?

>
> The world no longer buys hand made lace. Blame the cotton bushes.
…[4 more quoted lines elided]…
> living.

The marketplace, though it may resemble a sentient being, is not one.
I am. And I see enough evidence to believe that Robert, DD, and other
CLCers are too. (Either that, or there is a VERY good Eliza program
out there ;-) ).

>
> I started working as a contract programmer (in COBOL) in 1975.  I haven't
…[3 more quoted lines elided]…
> [/Pete]

I started about 1974. As a contractor. In FORTRAN. It was 1976 or so
before I had my first CoBOL opportunity.

There are many "markets" - some of them "mass", some of them "niche".
Some horizontal, some vertical. Some "proprietary", some "open
source". Some ethical, some less so. There is freedom of choice here.
And sentient agents are free to pursue the market(s) of their choice.

>
> All worthwhile comments from everyone; thanks for all your
…[21 more quoted lines elided]…
> Marketplace...

Thanks for the compliment. That was nice of you.

As for not losing sight of the marketplace, well, of course not. But
the following has also served me well: I embrace many things - my
wife, my family, my friends. But I have never embraced my insurance
agent, nor my accountant, nor my hardware salesman. These parties are
not my intimates, and they are to be kept, quite literally, at "arm's
length." That is sufficiently close to shake hands, and that is all
that is needed :-).

There are few exhortations more vulgar than the one to "embrace the
marketplace". And though you have not said that, Mr. Pete, your words
tiptoe so close that it causes me discomfort. And here I must
apologize, "I am sorry", sorry that I, somewhat playfully, posted
rejoinders, with the word "pimp" that has contributed to this
confusion. For to "embrace the marketplace" would make me a harlot, or
at best, a flirt, and I try hard to be neither.

I must keep in mind that you are taking time for me, serious time for
me, and that counts for so much. We are here to help each other. Thank
you. May you be blessed...

Ken
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 22)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-08-06T14:49:39+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6fshq4Fd7h3dU1@mid.individual.net>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <oh5a94djujajtek423m6e7rui63bfjsip3@4ax.com> <g74ero$bnd$1@reader1.panix.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <6fppc6Fccpn1U1@mid.individual.net> <a99ef1b0-8071-4025-97ac-613e698a7617@b1g2000hsg.googlegroups.com>`

```


<klshafer@att.net> wrote in message 
news:a99ef1b0-8071-4025-97ac-613e698a7617@b1g2000hsg.googlegroups.com...
On Aug 4, 9:40 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> <klsha...@att.net> wrote in message
>
…[10 more quoted lines elided]…
>

I rather think not. It is a change of Subject to be sure. It is also
On Topic. Spot On Topic. And the topic is not just Contracting, it is
Contracting in the CoBOL world. Hence, CoBOL and Contracting.

[Pete]

There are people here who have requested (on more than one occasion over the 
years) that on topic posts be confined to matters technical, as that is what 
they are interested in, and other posts should be marked "OT:" so they can 
be identified and ignored. It seems reasonable to me.
[/Pete]

<snip>
> [Pete]
>
> Do you think that "Contracting" requires a different mind set from
> "Permanent"?

I don't know if I would use the phrase "mind set" in this instance.
What I would say is that Contracting requires a different
"temperament". But I don't necessarily think that CoBOL contracting
requires a different temperament than Java or C++ contracting, but
maybe it does. I'm ready to be illuminated if others think so.

[Pete]

I believe successful contractors have a different attitude, approach, and 
perspective (mind set) from people who accept permanent employment.

I don't think they're "better", but I do think they are different. And it 
has nothing to do with the programming language being used.
[/Pete]

<snip>
>
> [snip]
…[5 more quoted lines elided]…
> d'ja think?).

I appreciate your heartfelt concern.

[Pete]
I'm not sure if you are being sarcastic here, but, in case you are, you 
should know I have had genuine concern for people making a living from COBOL 
for some 15 years now. It has worried me immensely to see the decline of 
COBOL and consequent erosion of COBOL jobs, but  what has been of most 
concern has been the general inertia and demonstrated reluctance to expand 
skill sets and move with the times. "Everything I want to do, I can do in 
COBOL." (The epitome of limited vision.)
[/Pete]


Being aware of that, if some of
us choose to play out the CoBOL end game as we see fit, and best we
can, what is that to you?

[Pete]
Given that it is a free forum and I have an opinion about it, there is 
little you can do to stop me expressing such opinion. However, I'll take 
your comment on board and reconsider my contribution here.
[/Pete]

>
> The world no longer buys hand made lace. Blame the cotton bushes.
…[6 more quoted lines elided]…
> living.

The marketplace, though it may resemble a sentient being, is not one.
I am.

[Pete]
I never suggested the market place was/is anything other than a... 
marketplace.  However, people who wish to profit from a marketplace do well 
to observe and understand it before essaying to trade there.
[/Pete]


And I see enough evidence to believe that Robert, DD, and other
CLCers are too. (Either that, or there is a VERY good Eliza program
out there ;-) ).

[Pete]

The humanity of regular posters to CLC is not in question (although there is 
a school of thought which suggests it SHOULD be... :-)) and has no relevance 
to the nature of marketplaces.
[/Pete]


>
> I started working as a contract programmer (in COBOL) in 1975. I haven't
…[3 more quoted lines elided]…
> [/Pete]

I started about 1974. As a contractor. In FORTRAN. It was 1976 or so
before I had my first CoBOL opportunity.

There are many "markets" - some of them "mass", some of them "niche".
Some horizontal, some vertical. Some "proprietary", some "open
source". Some ethical, some less so. There is freedom of choice here.
And sentient agents are free to pursue the market(s) of their choice.

[Pete]

Precisely. And exactly as many of those agents will show a profit, as the 
number who show a loss... The group you end up in depends on how well you 
read the market.

<snip>

I must keep in mind that you are taking time for me, serious time for
me, and that counts for so much. We are here to help each other. Thank
you. May you be blessed...

[Pete]

Thanks, and don't worry... after your "what's it to you" crack, I'll be 
spending less time on you... :-)

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 23)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-08-06T08:29:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cc7dd28-653d-4dd0-8f75-1d8a48af48e0@27g2000hsf.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <oh5a94djujajtek423m6e7rui63bfjsip3@4ax.com> <g74ero$bnd$1@reader1.panix.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <6fppc6Fccpn1U1@mid.individual.net> <a99ef1b0-8071-4025-97ac-613e698a7617@b1g2000hsg.googlegroups.com> <6fshq4Fd7h3dU1@mid.individual.net>`

```
On Aug 5, 10:49 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> <klsha...@att.net> wrote in message
> > Almost... It needs to be preceded by "OT:"
…[12 more quoted lines elided]…
>
[begin ken]

I was unaware that the directive for OT was for all matters non-
technical. I thought it was for all matters non-CoBOL. That seems
reasonable to me. And if the issue of contracting vs. permanent is
relevant to CoBOL's survival, I consider that Subject to be On Topic.
Sufficient disclosure is made in the subject line itself, "CoBOL and
Contracting, to allow disinterested parties to skip over.

[end ken]

<snip>
>
> > [Pete]
…[17 more quoted lines elided]…
> [/Pete]

[begin ken]
Well, yes, I agree. They probably also have greater tolerance for
"risk". Though, as Robert has pointed out, "permanent" employees are
not really permanent at all, and are assuming much, if not most or
all, of the same risk, without getting the pay premium for it.
[end ken]

> > [snip]
> > It isn't any good saying: "I'm a COBOL programmer, look what an awful life
…[11 more quoted lines elided]…
> for some 15 years now.

[begin ken]
The appreciation is genuine. Sometimes it is best to take statements
just at face value.
[end ken]

[begin Pete]
> It has worried me immensely to see the decline of
> COBOL and consequent erosion of COBOL jobs,
[end Pete]

[begin ken]
Ahh, yes, that is of great concern to me too...
[end ken]

[begin Pete]
> but  what has been of most
> concern has been the general inertia and demonstrated reluctance to expand
> skill sets and move with the times. "Everything I want to do, I can do in
> COBOL." (The epitome of limited vision.)
> [end Pete]

[begin ken]
I do not know, and I do not understand, why this is of even greater
concern to you. Hence, my question, "What is that to you?"
[end ken]

[begin ken]
>
> Being aware of that, if some of
> us choose to play out the CoBOL end game as we see fit, and best we
> can, what is that to you?
[end ken]
>
> [Pete]
> Given that it is a free forum and I have an opinion about it, there is
> little you can do to stop me expressing such opinion.
[end Pete]

[begin ken]
I realize this.
[end ken]

[begin Pete]
However, I'll take
> your comment on board and reconsider my contribution here.
> [endv Pete]

[begin ken]
Thanks.
[end ken]

>
> [Pete]
…[3 more quoted lines elided]…
> [/Pete]

[begin ken]
Sure. And if some of us choose a different market than you have
chosen, even after you have demonstrated success in your (new)
endeavors, and offered to help us to follow your Way, can you accept
the fact that given all of that, we still choose another Way, and can
you still appreciate us for who we are?
[end ken]

>[begin ken]
> And I see enough evidence to believe that Robert, DD, and other
> CLCers are too. (Either that, or there is a VERY good Eliza program
> out there ;-) ).
>[end ken]

> [Pete]
>
…[3 more quoted lines elided]…
> [/Pete]

[begin ken]
The relevance to me, with regard to marketplaces, is this. Robert, DD,
and I are all contractors. (I think you, Pete, have crossed over to
become a True Consultant.) And though the stormy seas of the
marketplace might toss us around a bit, as sentient humans, we are at
the tiller and actively engaged. That we choose to ride it out, rather
to follow the lighthouse to your safe port in the storm, is a business
decision that each of us makes. The marketplace is not our Master to
make that decision for us. It is only the sea upon which we sail, it
is only the wind upon which we fly.
[end ken]

>
>
…[14 more quoted lines elided]…
> [end ken]

> [Pete]
>
…[3 more quoted lines elided]…
> [end Pete]

[begin ken]
I do not understand your comment implying that the marketplace is a
zero-sum game. But let me address it this way: if some us choose a
group that does not do as well as you, but we are still happy, then
what is that to you?
[end ken]

> [begin ken]
> I must keep in mind that you are taking time for me, serious time for
> me, and that counts for so much. We are here to help each other. Thank
> you. May you be blessed...
> [end ken]

> [Pete]
>
…[3 more quoted lines elided]…
> Pete.
[end Pete]

[begin ken]
"What is that to you?" was intended as an earnest question. I am sorry
if I made it sound like a crack. I do not understand why you would
suffix a promise of spending less time on me with a smiley. It does
remind me of "good-bye with a smile", which I, like all sentient
humans, have experienced.
[end ken]
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 24)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-08-07T12:26:23+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6futpgFdf2mmU1@mid.individual.net>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <oh5a94djujajtek423m6e7rui63bfjsip3@4ax.com> <g74ero$bnd$1@reader1.panix.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <6fppc6Fccpn1U1@mid.individual.net> <a99ef1b0-8071-4025-97ac-613e698a7617@b1g2000hsg.googlegroups.com> <6fshq4Fd7h3dU1@mid.individual.net> <7cc7dd28-653d-4dd0-8f75-1d8a48af48e0@27g2000hsf.googlegroups.com>`

```


<klshafer@att.net> wrote in message 
news:7cc7dd28-653d-4dd0-8f75-1d8a48af48e0@27g2000hsf.googlegroups.com...
On Aug 5, 10:49 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> <klsha...@att.net> wrote in message
<snip>

[begin ken]
I do not know, and I do not understand, why this is of even greater
concern to you. Hence, my question, "What is that to you?"
[end ken]

[Pete]
Because it stops people going anywhere and causes them to end up in a job 
that has limited future.

I don't mind people choosing to do this, but they should be aware of and 
explore the options.

Some people simply don't.
[/Pete]


[begin ken]
>
> Being aware of that, if some of
> us choose to play out the CoBOL end game as we see fit, and best we
> can, what is that to you?
[end ken]
>
> [Pete]
> Given that it is a free forum and I have an opinion about it, there is
> little you can do to stop me expressing such opinion.
[end Pete]

[begin ken]
I realize this.
[end ken]

[begin Pete]
However, I'll take
> your comment on board and reconsider my contribution here.
> [endv Pete]

[begin ken]
Thanks.
[end ken]

>
> [Pete]
…[3 more quoted lines elided]…
> [/Pete]

[begin ken]
Sure. And if some of us choose a different market than you have
chosen, even after you have demonstrated success in your (new)
endeavors, and offered to help us to follow your Way, can you accept
the fact that given all of that, we still choose another Way, and can
you still appreciate us for who we are?
[end ken]

[Pete]

That is such rubbish it barely merits response.  I am not an Evangelist and 
I really have no vested interest in getting people to go contract or not, in 
COBOL or anything else. I do have concern for people who still believe there 
is a future in COBOL, but, if they are over 40 I guess it doesn't really 
matter.

It isn't about people following "my Way", it is about where IT is going and 
which current trends are likely to be lucrative, in terms of a long term 
future.

Judging from the posts here from people currently contracting in COBOL in 
the USA, it certainly doesn't look like an attractive proposition.

I simply don't see COBOL contract programming as being in that category. It 
was. Now it isn't.

It's a forum. Discussing it does not require Evangelism.

[/Pete]

[begin ken]
The relevance to me, with regard to marketplaces, is this. Robert, DD,
and I are all contractors. (I think you, Pete, have crossed over to
become a True Consultant.) And though the stormy seas of the
marketplace might toss us around a bit, as sentient humans, we are at
the tiller and actively engaged. That we choose to ride it out, rather
to follow the lighthouse to your safe port in the storm, is a business
decision that each of us makes. The marketplace is not our Master to
make that decision for us. It is only the sea upon which we sail, it
is only the wind upon which we fly.
[end ken]

[Pete.]
I disagree. But I respect your right to wreck your boat if you want you. I 
don't know if you've done much sailing. If you have, you would know that a 
salty sea dog always has an eye on the sea and the sky. That's all my posts 
here are.
[/Pete]

But let me address it this way: if some us choose a
group that does not do as well as you, but we are still happy, then
what is that to you?
[end ken]

[Pete]
Sure. It isn't a contest. As long as you are happy I have no beef...:-) Some 
of the posts did not reflect great happiness...that'sall.

Sorry, no more time now. I have a luncheon appointment.
[/Pete]
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 25)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-08-06T19:37:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<31c29c1c-8569-431a-b954-00a37bd5bd8d@r66g2000hsg.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <oh5a94djujajtek423m6e7rui63bfjsip3@4ax.com> <g74ero$bnd$1@reader1.panix.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <6fppc6Fccpn1U1@mid.individual.net> <a99ef1b0-8071-4025-97ac-613e698a7617@b1g2000hsg.googlegroups.com> <6fshq4Fd7h3dU1@mid.individual.net> <7cc7dd28-653d-4dd0-8f75-1d8a48af48e0@27g2000hsf.googlegroups.com> <6futpgFdf2mmU1@mid.individual.net>`

```
On Aug 6, 8:26 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> <klsha...@att.net> wrote in message
>
…[19 more quoted lines elided]…
> [/Pete]

On the contrary, "it" doesn't stop me, or them, from going "anywhere".
I am not really sure what the "it" is that you are referring to...
perhaps "it" is others', or my, refusal to heed your advice and to act
upon it? Can you accept that I listen to your advice, trying to
appreciate all of it, internalizing some of it, but passing on the
rest? Can you see that I still have a future that is worthwhile?

[snip]

> > [Pete]
> > I never suggested the market place was/is anything other than a...
…[14 more quoted lines elided]…
> That is such rubbish it barely merits response.

Then I feel that I have not been heard, and that I am not appreciated.

> I am not an Evangelist and
> I really have no vested interest in getting people to go contract or not, in
> COBOL or anything else. I do have concern for people who still believe there
> is a future in COBOL, but, if they are over 40 I guess it doesn't really
> matter.

If I may beg your indulgence for a moment, please, your posts did
leave *me* anyway with just a *wee* bit of feeling that you were
trying to "save us from ourselves." Is that Evangelism?

>
> It isn't about people following "my Way"...

Well, yes, I can readily agree with this...

>, it is about where IT is going and
> which current trends are likely to be lucrative, in terms of a long term
> future.

...but I don't think this is the "it" I have been talking about, where
"lucrative" is the operative word. And though I can't speak for the
Doc (he speaks for himself very well), I don't think your "it" is the
same "it" he was talking about either. (I am even less sure about
Robert :-), but perhaps he can enlighten me.)

The best way I knew how to put it was "playing out the end game",
lucrative or not.

For me anyway, life is a bit of a mix between the Invariant and the
Changing. And what to Preserve and what to Let Go Of are the issues at
hand.

I have said before that I didn't think "my puzzle" is the same as
"your puzzle". I'm jes' trying to find the right people to help me
work on my puzzle.


>
> Judging from the posts here from people currently contracting in COBOL in
> the USA, it certainly doesn't look like an attractive proposition.

Apparently, certainly not attractive to you. But equally apparently,
certainly sufficiently attractive to Doc, Robert, and me, or we would
be soliciting you to help us change our ways.

>
> I simply don't see COBOL contract programming as being in that category. It
> was. Now it isn't.

For you. For me; was, and still is, though changing.

>
> It's a forum. Discussing it does not require Evangelism.
…[20 more quoted lines elided]…
> [/Pete]

Well, for some still unknown and probably mystical reason, I don't
think I'll wreck it. :-) Got some extra life preservers just in case I
do, so much better equipped than in 2001-2002.

>
> But let me address it this way: if some us choose a
…[6 more quoted lines elided]…
> of the posts did not reflect great happiness...that'sall.

Hmmmm... I recall that you previously used the word "awful" in how we
described our experiences, and I do not recall any of us using that
word. And I know that Doc has said, more than once or twice, that what
he is doing "beats working on the loading dock." And to me, Robert
certainly seems plenty "happy enough" - for me, his posts veritably
*burst* with his exuberance. But after all, all this is filtered
through my own emotionally biased lenses.

So, I will ask, not rhetorically, and with understanding if this
question be met with Stony Silence, Doc, Robert - is your lot in life
with being a CoBOL contractor a happy one, or at least a satisfying
one? (This despite the pimps, er, the agents/reps, the uneasy
coexistence with offshoring, the declining CoBOL marketshare, and all
the other bumps we encounter on the ride?)

>
> Sorry, no more time now. I have a luncheon appointment.

No apology needed. You have already spent more time on me than I
probably deserve :-).

> [/Pete]

ken
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 26)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-07T00:16:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<320l9497kif80ih6pl1m6pa9hcd9pl537k@4ax.com>`
- **References:** `<elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <6fppc6Fccpn1U1@mid.individual.net> <a99ef1b0-8071-4025-97ac-613e698a7617@b1g2000hsg.googlegroups.com> <6fshq4Fd7h3dU1@mid.individual.net> <7cc7dd28-653d-4dd0-8f75-1d8a48af48e0@27g2000hsf.googlegroups.com> <6futpgFdf2mmU1@mid.individual.net> <31c29c1c-8569-431a-b954-00a37bd5bd8d@r66g2000hsg.googlegroups.com>`

```
On Wed, 6 Aug 2008 19:37:14 -0700 (PDT), "klshafer@att.net" <klshafer@att.net> wrote:

>So, I will ask, not rhetorically, and with understanding if this
>question be met with Stony Silence, Doc, Robert - is your lot in life
>with being a CoBOL contractor a happy one, or at least a satisfying
>one? (This despite the pimps, er, the agents/reps, the uneasy
>coexistence with offshoring, the declining CoBOL marketshare, and all

It isn't worse than being a contractor in another programming language. 

The best part is when the project is winding down and there's some idle time. They say
they've always wanted a tool that did so-and-so. Do I think I could write it? I LOVE
building tools. It's a chance to do Real Programming, unfettered by obsolete standards. I
get to design any way I want and write beautiful code.

My most enjoyable gigs were at very large companies, because the people I worked with were
smart and undogmatic. The least enjoyable were small IT departments in smallish companies,
where employees greatest interest was defended the low quality status quo.
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 27)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-08-08T01:21:28+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6g0b6qFd2gltU1@mid.individual.net>`
- **References:** `<elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <6fppc6Fccpn1U1@mid.individual.net> <a99ef1b0-8071-4025-97ac-613e698a7617@b1g2000hsg.googlegroups.com> <6fshq4Fd7h3dU1@mid.individual.net> <7cc7dd28-653d-4dd0-8f75-1d8a48af48e0@27g2000hsf.googlegroups.com> <6futpgFdf2mmU1@mid.individual.net> <31c29c1c-8569-431a-b954-00a37bd5bd8d@r66g2000hsg.googlegroups.com> <320l9497kif80ih6pl1m6pa9hcd9pl537k@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:320l9497kif80ih6pl1m6pa9hcd9pl537k@4ax.com...
> On Wed, 6 Aug 2008 19:37:14 -0700 (PDT), "klshafer@att.net" 
> <klshafer@att.net> wrote:
…[7 more quoted lines elided]…
> It isn't worse than being a contractor in another programming language.

How would you know, Robert? Given that the market in other languages is 
different, it may well be that the treatment of contractors is different 
also. Or then again, it may not be. I have experience working with Java and 
C# contractors as well as with COBOL, but, not in the United States and 
then, my experience of COBOL contracting does not generally match the 
experiences described here. (it does in some regards, but I would have 
stopped using agents years ago if I had regularly encountered what you guys 
have been describing, as a matter of course...).

>
> The best part is when the project is winding down and there's some idle 
…[3 more quoted lines elided]…
> building tools.

Yep, me too... This does not surprise me in the least. I have never had any 
doubt over your ability to code and I know from my own experience that 
writing tools is rewarding and satisfying.  I started doing it on mainframe 
sites in the 1980s and have never lost the taste for it. These days I find a 
number of people looking for help in migrating their existing COBOL systems, 
and so tools to help do this are in some slight demand. The pathway is 
usually away from the COBOL file system to RDB, initially, then to 
refactoring existing COBOL code for reuse in an Object Oriented environment, 
and finally to a  .NET solution using C#.

I have tools that deal with all of this and am currently extending them. It 
is very interesting work and I appreciate the opportunity to be able to stay 
home and do it. You remember a little while back saying you had never worked 
on a site where automation of migration was achieved? Well, I have a 
solution that does achieve it. It uses Object technology to provide 
generalized RDB access, and tools are provided to automatically convert ISAM 
actions in existing applications into invokes of the data object handlers, 
which are loaded to a Data Access Layer, so that the action of replacing 
ISAM access, simultaneously creates an n-tier architecture. I am currently 
optimizing it and trying various alternative approaches, but the tests are 
looking very good. I have managed to minimise the dynamic SQL access after 
considering advice from both yourself and Frederico. I don't think it would 
be a high volume solution (say more than 15 - 20 million DB rows), but this 
is plenty for small businesses with existing COBOL solutions written for 
Client/Server. I'd LOVE to be able to provide a solution for the 
presentation layer (particularly for Fujitsu PowerCOBOL), but, at least 
presently, that looks like being a completely separate problem. Fortunately, 
once the file system is converted to RDB, much of the reporting can be done 
by standard packages, (I've been experimenting with a Visual Russian one 
called StimulSoft and found it superb) so that immediately eliminates a good 
percentage of existing COBOL code.

Tools and automation are always good fun, and writing programs that write 
programs is a very satisfying activity.


>It's a chance to do Real Programming, unfettered by obsolete standards. I
> get to design any way I want and write beautiful code.
>

Exactly. Or, even better, generate beautiful code... :-)

My tools are written in C# but generate COBOL. They have been received with 
interest and enthusiasm by COBOL programmers. (Especially when they realise 
the hours of work they have been saved. They are also interested to see how 
the code does what it does, and there has been some excellent feedback. 
Because the code is in COBOL they can modify it for special cases if they 
need to (hooks are built into it) or add special data filters or validations 
easily before loading data to the new RDB.

> My most enjoyable gigs were at very large companies, because the people I 
> worked with were
> smart and undogmatic. The least enjoyable were small IT departments in 
> smallish companies,
> where employees greatest interest was defended the low quality status quo.

See, that's funny, because I found quite the reverse. In the smaller places 
people were looking to work smarter and generally improve practices. 
However, it isn't universally so and I can think of some exceptions. One 
thing I am sure of is that the "Corporate Culture" has a large bearing on 
the attitudes of the IT people, even if the size of the Organization may not 
be a reliable indicator.

I think it is also true that general corporate attitudes have changed in the 
40 years I've been in this game. We'd probably like to think that Management 
today is more enlightened than it was 30 years ago, although I know that is 
not always the case. I remember working on contract at a site in London 30 
years ago where you were not allowed to leave the premises without an 
authority from your Manager. (it was all about control and had nothing to do 
with productivity). I was off site for about 15 minutes collecting some 
dry-cleaning and received a formal reprimand on my return. I pointed out 
that I hadn't billed them for the time, and, in the absence of Alsatians, 
watch towers, and guards with machine pistols, I had no reasonable reason to 
believe that stepping out the front gate was a violation of Company Rules of 
Employment, but it made no difference.  Another employee was nearly fired 
for getting a haircut which caused his 30 minute lunch period to run over by 
about 10 minutes... I was amused when he pointed out that as his hair 
actually grew in the firm's time, it seemed perfectly reasonable for the 
company to contribute some time in order for him to get it cut...

These days, I can't imagine these situations arising. Certainly I do not 
require to know the exact whereabouts of every member of my team at every 
moment of the day, and trust them to do the job they are contracted for. If 
they didn't, I'd become aware of it very quickly. (I DO have the mobile 
numbers of all team members and reserve the right to call them at any time 
during working hours... I very rarely have exercised this right...)

Doc says a fish rots from the head. I don't know about that, but I suspect 
it may be true. I DO know that when a company is led by a person with flair, 
vision, and a genuine liking for people, it makes a huge difference to the 
productivity of everyone who works there.

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 28)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-07T19:24:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7k1n94dart6q3s2ie5jmo94hikmir9mfi8@4ax.com>`
- **References:** `<29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <6fppc6Fccpn1U1@mid.individual.net> <a99ef1b0-8071-4025-97ac-613e698a7617@b1g2000hsg.googlegroups.com> <6fshq4Fd7h3dU1@mid.individual.net> <7cc7dd28-653d-4dd0-8f75-1d8a48af48e0@27g2000hsf.googlegroups.com> <6futpgFdf2mmU1@mid.individual.net> <31c29c1c-8569-431a-b954-00a37bd5bd8d@r66g2000hsg.googlegroups.com> <320l9497kif80ih6pl1m6pa9hcd9pl537k@4ax.com> <6g0b6qFd2gltU1@mid.individual.net>`

```
On Fri, 8 Aug 2008 01:21:28 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>"Robert" <no@e.mail> wrote in message 
>news:320l9497kif80ih6pl1m6pa9hcd9pl537k@4ax.com...
…[11 more quoted lines elided]…
>How would you know, Robert? 

I know because my desk is surrounded by them. I talk to them every day and overhear their
conversations. I'm beginning to think Hindi should be a required language for IT.

>Given that the market in other languages is 
>different, it may well be that the treatment of contractors is different 
…[3 more quoted lines elided]…
>experiences described here.

Client companies treat all contractors pretty much the same.

> (it does in some regards, but I would have 
>stopped using agents years ago if I had regularly encountered what you guys 
>have been describing, as a matter of course...).

The problem is most contractors are foreigners, largely from India, who put up with
treatment that Americans would not. They are as intelligent and capable as us, perhaps
more so, but they come from a different culture. Indian managers mistreat workers worse
than American managers. 

>> The best part is when the project is winding down and there's some idle 
>> time. They say
…[3 more quoted lines elided]…
>

>I have tools that deal with all of this and am currently extending them. It 
>is very interesting work and I appreciate the opportunity to be able to stay 
…[12 more quoted lines elided]…
>Client/Server. 

You're putting a Porche body on a Morris Minor. Tables are still joined with procedural
logic, which is MUCH slower than a SQL join. There are probably arrays in some tables, and
possibly even redefines. 

You'd have a superior tool if it normalized the tables and used views to simulate the old
file system. It would add to each table a sequential join key and audit fields (user &
timestamp) updated by triggers, and add the join key to child tables. Then the client
would have the foundation of a real database. 

>>It's a chance to do Real Programming, unfettered by obsolete standards. I
>> get to design any way I want and write beautiful code.
>>
>
>Exactly. Or, even better, generate beautiful code... :-)

I wrote one that figured out dependencies and produced good looking MAKE files.

>My tools are written in C# but generate COBOL. They have been received with 
>interest and enthusiasm by COBOL programmers. (Especially when they realise 
…[4 more quoted lines elided]…
>easily before loading data to the new RDB.

Purists would say filters should be in views, validations in stored procedures and foreign
key constraints. I'm not sure I agree, but at least they should be in the data layer.

>> My most enjoyable gigs were at very large companies, because the people I 
>> worked with were
…[5 more quoted lines elided]…
>people were looking to work smarter and generally improve practices. 

Nah, they're looking for a sinecure, and lack of competition.

>However, it isn't universally so and I can think of some exceptions. One 
>thing I am sure of is that the "Corporate Culture" has a large bearing on 
>the attitudes of the IT people, even if the size of the Organization may not 
>be a reliable indicator.

I concur with that. A pluralistic culture is good; a homogeneous culture is bad.
Programming standards from the 1980s, the bane of Cobol, are unknown to people from India
and Asia. 

>I think it is also true that general corporate attitudes have changed in the 
>40 years I've been in this game. We'd probably like to think that Management 
>today is more enlightened than it was 30 years ago, although I know that is 
>not always the case.

Human nature doesn't change.

>Doc says a fish rots from the head. I don't know about that, but I suspect 
>it may be true. I DO know that when a company is led by a person with flair, 
>vision, and a genuine liking for people, it makes a huge difference to the 
>productivity of everyone who works there.

Black Hand CEOs and VPs cannot survive in very large companies. They can in smallish
companies, especially if family owned.
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 29)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-08T01:29:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g7g7i7$7ni$1@reader1.panix.com>`
- **References:** `<29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <320l9497kif80ih6pl1m6pa9hcd9pl537k@4ax.com> <6g0b6qFd2gltU1@mid.individual.net> <7k1n94dart6q3s2ie5jmo94hikmir9mfi8@4ax.com>`

```
In article <7k1n94dart6q3s2ie5jmo94hikmir9mfi8@4ax.com>,
Robert  <no@e.mail> wrote:

[snip of 'my anecdotes reflect my life more than your anecdotes do']

>Indian managers mistreat workers worse than American managers. 

So... Indian managers treat workers better than American ones?

[snip of more 'my anecdotes reflect my life more than yours do']

DD
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 30)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-08-08T07:51:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<338da75f-3940-43ac-8db4-627a7517778b@d45g2000hsc.googlegroups.com>`
- **References:** `<29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <320l9497kif80ih6pl1m6pa9hcd9pl537k@4ax.com> <6g0b6qFd2gltU1@mid.individual.net> <7k1n94dart6q3s2ie5jmo94hikmir9mfi8@4ax.com> <g7g7i7$7ni$1@reader1.panix.com>`

```
On Aug 7, 9:29 pm, docdw...@panix.com () wrote:
> In article <7k1n94dart6q3s2ie5jmo94hikmir9m...@4ax.com>,
>
> Robert  <n...@e.mail> wrote:
>
> [snip of 'my anecdotes reflect my life more than your anecdotes do']

[another snip]

> [snip of more 'my anecdotes reflect my life more than yours do']
>

Then in keeping with that Spirit of the Thread, I submit this, my own
anecdote:

About twenty years ago, a college buddy of mine and I were in a pizza
pub on the edge of a Great State University when he was surprised by a
couple fellows who, upon walking in, he recognized as friends of his
from the greater Chicago area.

Well, they joined us, these two, who were both steelworkers at the
Gary Steel Works, just across the state line from Chicago. They were
in town for some kind of Labor/Management conference at Great State
University. We ordered pizza and beer together, talked and talked,
about what, I can't exactly remember much, and everyone had a great
time.

Later, it came time to pay, and the steelworkers threw some money on
the table, and one went to the Men's room, while another distracted
himself by chatting up one of the lovely University coeds who just
happened to be pretty-fying the premises.

"Oh! Let me pay to this!" I said to my friend, out of earshot of the
steelworkers.

"No," my friend said, "let them pay for it."

"Well, at least I'll pay for my share," I argued.

"No, let them pay for _all_ of it," my friend insisted, this time
tugging on my sleeve for emphasis.

By the plaintive look on his face, I knew that somehow this small
thing was, well, it was an *important* thing. So I acquiesced, not
quite understanding at the time, for after all, this was my town, so I
felt like a host to our friends, and I was a computer professional,
probably making better money than them, and all of that just seemed to
speak that I should be the one to pay.

I was wrong, and my friend explained it a bit to me, though it would
be much later before I really understood.

"Don't you see?" my friend said, "they're getting the #!&%@ kicked out
of them. But they're hanging on, and they _can_ pay. So let them."

This would have been the late 80's or so, after the Plaza Accord was
signed, but before it was seen largely as a failure (http://
en.wikipedia.org/wiki/Plaza_accord), and certainly after I had
personally seen the shuttered Middletown/Steelton, PA mill, and the
Pittsburgh mills were already in decline.

Now maybe these fellows had a meal allowance on an expense account
from their "local". I don't know. Certainly pizza and beer for four
cost no more than thick porterhouse steaks for two. So they came out
OK.

I can't remember their names. I can't remember what we talked about,
though I don't remember it being about the Plaza Accord, or the unfair
competition from foreign producers, or even their conference.
Maybe we talked about how I remembered my mother telling me of my
grandfather working there for a while. Probably we talked about
basketball, and women :-).

What I remember is how they smiled at us on their way out, and how
their handshakes felt. I think they just wanted to be listened to for
a while.

Today, in 2008, the Gary Steel Works is still U.S. Steel's biggest
plant, in size and production, in the whole of the United States. This
despite the significant decline in employment, due in large part to
better and better automation.

http://www.ussteel.com/corp/facilities/gary.htm

I know at one time they were also the biggest "local". I think they
still are.

Though I can't know for sure, I choose to think that my friends help
make that possible.

I've been told that you can see the glow of the blast furnaces all the
way across Lake Michigan. Some say that, despite the slight haze, it
is a beautiful sight.

The connection to CoBOL is there, if you look hard enough.

Ken
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 29)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-08-08T15:59:16+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6g1uklFdrmrlU1@mid.individual.net>`
- **References:** `<29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <6fppc6Fccpn1U1@mid.individual.net> <a99ef1b0-8071-4025-97ac-613e698a7617@b1g2000hsg.googlegroups.com> <6fshq4Fd7h3dU1@mid.individual.net> <7cc7dd28-653d-4dd0-8f75-1d8a48af48e0@27g2000hsf.googlegroups.com> <6futpgFdf2mmU1@mid.individual.net> <31c29c1c-8569-431a-b954-00a37bd5bd8d@r66g2000hsg.googlegroups.com> <320l9497kif80ih6pl1m6pa9hcd9pl537k@4ax.com> <6g0b6qFd2gltU1@mid.individual.net> <7k1n94dart6q3s2ie5jmo94hikmir9mfi8@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:7k1n94dart6q3s2ie5jmo94hikmir9mfi8@4ax.com...
> On Fri, 8 Aug 2008 01:21:28 +1200, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[21 more quoted lines elided]…
>

Fair enough.

>>Given that the market in other languages is
>>different, it may well be that the treatment of contractors is different
…[53 more quoted lines elided]…
> logic, which is MUCH slower than a SQL join.

Er...actually, they're not, for the most part. I realized this when I first 
started testing and looked for ways to join attached tables to the base. It 
isn't easy because the attached tables use the multiple row logic we 
discussed some time ago, and that makes it difficult to join. I'm still 
working on this but have a reasonable compromise as a fallback position. The 
original ISAM definitions are split into a "Table Set" in 2NF(A "base table" 
with a series of connected RG tables, one for each OCCURS in the original 
definition. Some Table Sets have only a base table, the largest encountered 
so far has 8 attached tables but these are usually just one or a few 
columns. Repeating groups are connected by foreign key and when the 
equivalent data to the ISAM record is fetched there is an interface flag 
that joins the dependent tables on the same primary key as the base table 
(if possible), or doesn't, if the repeating groups are not required. It is 
retrieving (and building) around 100 ISAM equivalents a second, which will 
be adequate for most client server applications.



> There are probably arrays in some tables, and
> possibly even redefines.

Not in the RDB Tables, but certainly in the ISAM record definitions. These 
are handled by the tool set and it generates a RDB in 2NF.
>
> You'd have a superior tool if it normalized the tables and used views to 
> simulate the old
> file system.

It does normalize the tables (and it was very tricky to make it do so). I 
considered views, but you hit the same problem of joins on a base table and 
a multi-row attached table.


>It would add to each table a sequential join key and audit fields (user &
> timestamp) updated by triggers, and add the join key to child tables. Then 
> the client
> would have the foundation of a real database.

That's beyond where I want to go for initial conversion, but I agree that 
triggers could be useful. They are currently under consideration for dealing 
with group fields and redefines. There is no need for a sequential join key 
as the table set is joined on the Base table primary key. All rows (as in 
every RDB I have designed since 1983), have the possibility of audit 
timestamps. (For myself, I would always use it, but when writing for others 
you need to give them options and respect their right to work differently.)

>
>>>It's a chance to do Real Programming, unfettered by obsolete standards. I
…[7 more quoted lines elided]…
>

MAKE files are cool.

>>My tools are written in C# but generate COBOL. They have been received 
>>with
…[13 more quoted lines elided]…
> data layer.

I don't totally agree (because I can think of exceptions), although I can 
see this would be a useful approach in many cases. Certainly I have gone to 
a lot of trouble with the Toolset development to ensure that ALL SQL is in 
the data layer and not in the applications. This exercise has become a kind 
of hobby to me now. Although I am being paid to do it, I am doing far more 
than I am being paid for (if you know what I mean... :-))

The clients will get what they require (and more) but for me it is the 
satisfaction of knowing that something which many said could not be done and 
wouldn't even attempt, got done. It is also very satisfying to see work 
estimates of many months reduced to a few weeks and programmers buzzing with 
achieving man years of effort in what was previously an impossibly short 
time. Tools make a huge difference. A tool can generate a normalized 
database in seconds, that a person would take all day to write and check. 
Migration to the programmers is a necessary evil. "The Boss" wants 
everything running off a database; they, for the most part, couldn't care 
less. ("The Boss" is actually right; the RDB is the first step towards an 
Object based .NET system, and away from reliance on COBOL). The programmers 
are much more interested in enhancing their application and ensuring they 
have a future. The bright ones are already expanding their skill sets, the 
others are considering other options. (One guy, a COBOL programmer of 15 
years, quit the other day and decided to take a job on a help desk. He was 
fed up with programming, didn't want to move into an Object future, and was 
offered more money to work on a Help desk.) People have choices and they 
exercise them. Eventually it all works out and most people come out happier.

>
>>> My most enjoyable gigs were at very large companies, because the people 
…[12 more quoted lines elided]…
>

Not always...

>>However, it isn't universally so and I can think of some exceptions. One
>>thing I am sure of is that the "Corporate Culture" has a large bearing on
…[18 more quoted lines elided]…
> Human nature doesn't change.

Really?  So why aren't we still living in trees? Human Nature DOES change. 
BUT it changes slowly and almost imperceptibly over VERY long periods of 
time. We don't subject people to capital punishment, torture and mutilation 
for sport any more. Changed our minds about it. We accept that Human Beings, 
of whatever Class, Creed, or Colour, have certain inalienable rights which 
must be respected. (We didn't always feel that way, but, again, our minds 
were changed over time...)

Hundreds of thousands of people in affluent nations make donations and 
sponsor children in poorer nations because they feel it is the right thing 
to do. Such was not always the case. There are many examples of change 
(usually associated with "growth") in Human nature. I know it's hard to 
believe, but I have actually encountered managers who WANT to be better... 
:-)

In the microcosm of the Human condition, that is Industry and Commerce, 
changes occur too. I once worked in a place where, at 8:30 in the morning, a 
red line was ruled across the attendance register (which all employees were 
required to sign on arrival). Anyone whose name was found under that line 
three times, was on the mat and could be fined, formally reprimanded or even 
fired. I can't see us doing that today. Nowadays we operate glide time and 
accept that achievement is not necessarily about being in a certain place at 
a certain time.

The old concepts of task oriented management  with rigid control are 
gradually being replaced by goal oriented management, the waterfall is 
giving way to more agile approaches and the whole approach is being 
reconsidered. (At least, it is in the more progressive companies. Not every 
company is progressive...)

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 30)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-08T12:33:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gfvo949q5uimfmqotk8m0k96bdviq3qreg@4ax.com>`
- **References:** `<6fppc6Fccpn1U1@mid.individual.net> <a99ef1b0-8071-4025-97ac-613e698a7617@b1g2000hsg.googlegroups.com> <6fshq4Fd7h3dU1@mid.individual.net> <7cc7dd28-653d-4dd0-8f75-1d8a48af48e0@27g2000hsf.googlegroups.com> <6futpgFdf2mmU1@mid.individual.net> <31c29c1c-8569-431a-b954-00a37bd5bd8d@r66g2000hsg.googlegroups.com> <320l9497kif80ih6pl1m6pa9hcd9pl537k@4ax.com> <6g0b6qFd2gltU1@mid.individual.net> <7k1n94dart6q3s2ie5jmo94hikmir9mfi8@4ax.com> <6g1uklFdrmrlU1@mid.individual.net>`

```
On Fri, 8 Aug 2008 15:59:16 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>Er...actually, they're not, for the most part. I realized this when I first 
>started testing and looked for ways to join attached tables to the base. It 
…[12 more quoted lines elided]…
>be adequate for most client server applications.

I hope you are reading arrays with a single SELECT rather than a cursor. 
Why is it difficult to join? 

>>It would add to each table a sequential join key and audit fields (user &
>> timestamp) updated by triggers, and add the join key to child tables. Then 
…[5 more quoted lines elided]…
>with group fields and redefines. 

You can do group fields in PL/SQL. They are called records, which is the same as a struc
in C. Why do you need them outside Cobol?

If you use a 'record' or a Cobol group name in SQL, the precompiler should replace the
reference with a list of the elementary fields contained. PL/SQL lets you copy a record to
another record. 

>There is no need for a sequential join key 
>as the table set is joined on the Base table primary key. All rows (as in 
>every RDB I have designed since 1983), have the possibility of audit 
>timestamps. (For myself, I would always use it, but when writing for others 
>you need to give them options and respect their right to work differently.)

They are required by law (Sarbanes-Oxley) in the US.
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 31)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-08-09T11:48:25+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6g44aaFe73d3U1@mid.individual.net>`
- **References:** `<6fppc6Fccpn1U1@mid.individual.net> <a99ef1b0-8071-4025-97ac-613e698a7617@b1g2000hsg.googlegroups.com> <6fshq4Fd7h3dU1@mid.individual.net> <7cc7dd28-653d-4dd0-8f75-1d8a48af48e0@27g2000hsf.googlegroups.com> <6futpgFdf2mmU1@mid.individual.net> <31c29c1c-8569-431a-b954-00a37bd5bd8d@r66g2000hsg.googlegroups.com> <320l9497kif80ih6pl1m6pa9hcd9pl537k@4ax.com> <6g0b6qFd2gltU1@mid.individual.net> <7k1n94dart6q3s2ie5jmo94hikmir9mfi8@4ax.com> <6g1uklFdrmrlU1@mid.individual.net> <gfvo949q5uimfmqotk8m0k96bdviq3qreg@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:gfvo949q5uimfmqotk8m0k96bdviq3qreg@4ax.com...
> On Fri, 8 Aug 2008 15:59:16 +1200, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[23 more quoted lines elided]…
> I hope you are reading arrays with a single SELECT rather than a cursor.

Yes. See below.

> Why is it difficult to join?

Consider that ORACLE is not in use and PL/SQL is therefore not available.

Consider a base table  where a single row is being selected (not by cursor, 
by normal ESQL select).

SELECT col1, col2, col3
INTO :col1, :col2, :col3
FROM baseTable
WHERE basePK = :someVariable

Fine. Fetches base data no problem. (singleton select...1 row)


Consider an attached table that has 12 balance fields (connected on the same 
PK.)

(under HV declarations...)
01 multirow-values.
     12 balance pic s9(14)v9(4) comp-5 occurs 12.


I can access the 12 balances with a single select ...

SELECT balance
INTO :balance
FROM  RGtable01
WHERE RGtable01PK = :someVariable

This will correctly load the 12 balances attached to the base table into the 
defined HVs with a single SQL statement. (a single column across 12 rows 
fetched.)

BUT...

If I take the next logical step and JOIN the two tables...


SELECT x.col1, x.col2, x.col3, y.balance
INTO :col1, :col2, :col3, :balance
FROM baseTable x, RGtable01 y
WHERE x.basePK = :someVariable AND y.RGtable01PK = x.basePK

...it fails at compile time with a message saying "Host Variable is 
different..."  I think it is trying to say that it cannot load a single 
instance (base) at the same time as it loads 12 instances (attached).

Separately these calls work fine; as a single join, they don't. I also tried 
using INNER JOIN syntax and got exactly the same result. I cannot create a 
VIEW either.

I haven't given up on it as there are still a few possibilities I need to 
try, but I 'd be happy for any comments from anyone who feels they can shed 
some light on this...

>
>>>It would add to each table a sequential join key and audit fields (user &
…[12 more quoted lines elided]…
> in C. Why do you need them outside Cobol?

Er... because I am NOT using PL/SQL... ? :-)
>
> If you use a 'record' or a Cobol group name in SQL, the precompiler should 
…[3 more quoted lines elided]…
> another record.

What it SHOULD do and what it DOES are apparently, regrettably, disparate... 
:-)

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 32)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-08T21:10:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mfup94dm1gs03cu8ecoicbpdo8p50ninnq@4ax.com>`
- **References:** `<6fshq4Fd7h3dU1@mid.individual.net> <7cc7dd28-653d-4dd0-8f75-1d8a48af48e0@27g2000hsf.googlegroups.com> <6futpgFdf2mmU1@mid.individual.net> <31c29c1c-8569-431a-b954-00a37bd5bd8d@r66g2000hsg.googlegroups.com> <320l9497kif80ih6pl1m6pa9hcd9pl537k@4ax.com> <6g0b6qFd2gltU1@mid.individual.net> <7k1n94dart6q3s2ie5jmo94hikmir9mfi8@4ax.com> <6g1uklFdrmrlU1@mid.individual.net> <gfvo949q5uimfmqotk8m0k96bdviq3qreg@4ax.com> <6g44aaFe73d3U1@mid.individual.net>`

```
On Sat, 9 Aug 2008 11:48:25 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>"Robert" <no@e.mail> wrote in message 
>news:gfvo949q5uimfmqotk8m0k96bdviq3qreg@4ax.com...


>> Why is it difficult to join?
>
…[52 more quoted lines elided]…
>some light on this...

That's because the ISO SQL Standard doesn't support collection classes (arrays). It does
support result sets, but they must be two dimensional tables. The result of your SELECT
is a Cartesian join between baseTable and RGtable01. The result set has twelve instances
of col1, col2 and col3 -- the same data repeated next to each balance.  It will work if
you put OCCURS 12 on ALL of the host variables. 

I'm confident a single select will be faster in this simplified example. Two selects might
be faster if the base table has 200 columns.
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 33)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-08-09T16:49:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6g4lugFe7a1pU1@mid.individual.net>`
- **References:** `<6fshq4Fd7h3dU1@mid.individual.net> <7cc7dd28-653d-4dd0-8f75-1d8a48af48e0@27g2000hsf.googlegroups.com> <6futpgFdf2mmU1@mid.individual.net> <31c29c1c-8569-431a-b954-00a37bd5bd8d@r66g2000hsg.googlegroups.com> <320l9497kif80ih6pl1m6pa9hcd9pl537k@4ax.com> <6g0b6qFd2gltU1@mid.individual.net> <7k1n94dart6q3s2ie5jmo94hikmir9mfi8@4ax.com> <6g1uklFdrmrlU1@mid.individual.net> <gfvo949q5uimfmqotk8m0k96bdviq3qreg@4ax.com> <6g44aaFe73d3U1@mid.individual.net> <mfup94dm1gs03cu8ecoicbpdo8p50ninnq@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:mfup94dm1gs03cu8ecoicbpdo8p50ninnq@4ax.com...
> On Sat, 9 Aug 2008 11:48:25 +1200, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[75 more quoted lines elided]…
> you put OCCURS 12 on ALL of the host variables.

Ah, thank you for that. That was pretty much the conclusion I had come to. 
It is not attractive to do this, as the base table has 63 columns on it, 
plus their indicator variables...
>
> I'm confident a single select will be faster in this simplified example. 
> Two selects might
> be faster if the base table has 200 columns.

Do you really think so?  OK, I'll run some tests next week and try it.

You expect a single join (returning 11 x 63 redundant cols of base table = 
693 values I am not interested in, along with 12 values from the attached 
table), to be quicker than a singleton base select of 63 fields, followed by 
a multi-row select of the 12 balances? If you are right (and I have no idea 
what to expect) it is a pretty damning indictment of the overheads incurred 
by an embedded SQL call...

If this proves true I'll have to reconsider ESQL and maybe move to LINQ 
instead.

Thanks for your comments on this, Robert.

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 34)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-09T16:22:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<la2s94pj9s39k9qor693tiav8tok9vhl70@4ax.com>`
- **References:** `<6futpgFdf2mmU1@mid.individual.net> <31c29c1c-8569-431a-b954-00a37bd5bd8d@r66g2000hsg.googlegroups.com> <320l9497kif80ih6pl1m6pa9hcd9pl537k@4ax.com> <6g0b6qFd2gltU1@mid.individual.net> <7k1n94dart6q3s2ie5jmo94hikmir9mfi8@4ax.com> <6g1uklFdrmrlU1@mid.individual.net> <gfvo949q5uimfmqotk8m0k96bdviq3qreg@4ax.com> <6g44aaFe73d3U1@mid.individual.net> <mfup94dm1gs03cu8ecoicbpdo8p50ninnq@4ax.com> <6g4lugFe7a1pU1@mid.individual.net>`

```
On Sat, 9 Aug 2008 16:49:18 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>>>SELECT x.col1, x.col2, x.col3, y.balance
>>>INTO :col1, :col2, :col3, :balance
…[29 more quoted lines elided]…
>plus their indicator variables...

You must put the OCCURS on each of the 63 host variables and 63 indicators. 
You cannot put it on a group name over them.


>> I'm confident a single select will be faster in this simplified example. 
>> Two selects might
…[12 more quoted lines elided]…
>instead.

LINQ uses SQL under the covers. I has the same problem you have.
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 35)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-08-10T14:54:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6g73j1Fe7tf9U1@mid.individual.net>`
- **References:** `<6futpgFdf2mmU1@mid.individual.net> <31c29c1c-8569-431a-b954-00a37bd5bd8d@r66g2000hsg.googlegroups.com> <320l9497kif80ih6pl1m6pa9hcd9pl537k@4ax.com> <6g0b6qFd2gltU1@mid.individual.net> <7k1n94dart6q3s2ie5jmo94hikmir9mfi8@4ax.com> <6g1uklFdrmrlU1@mid.individual.net> <gfvo949q5uimfmqotk8m0k96bdviq3qreg@4ax.com> <6g44aaFe73d3U1@mid.individual.net> <mfup94dm1gs03cu8ecoicbpdo8p50ninnq@4ax.com> <6g4lugFe7a1pU1@mid.individual.net> <la2s94pj9s39k9qor693tiav8tok9vhl70@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:la2s94pj9s39k9qor693tiav8tok9vhl70@4ax.com...
> On Sat, 9 Aug 2008 16:49:18 +1200, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[40 more quoted lines elided]…
> You cannot put it on a group name over them.

Yes, I found that out some time ago... :-)
>
>
…[19 more quoted lines elided]…
> LINQ uses SQL under the covers. I has the same problem you have.

No, SQL is only ONE possibility for LINQ. Certainly, as I would be using 
LINQ to SQL in this instance, I will want generated SQL from it, but it may 
be able to use functions I am not aware of, and might even resolve this join 
problem. I have seen LINQ sample code for handling Entity Sets (which is 
what my Table set is really) and it seems quite straightforward.

However, there are some other implications in moving to LINQ, and I won't be 
considering it until we see how the tests stack up.

(So far I have only dabbled with LINQ but what I have seen has been very 
exciting. Furthermore, LINQ can defer execution and use multiple processors. 
There is no problem if the base and the attached tables are accessed in 
parallell on separate processors. I just don't know at this stage. I DO know 
that if a single SQL call invokes the kind of overheads we are talking 
about, then the sooner I get away from it, the better...)

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 28)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-08-08T08:32:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<05ae89f8-f111-4225-9aa9-dd979fad5596@k13g2000hse.googlegroups.com>`
- **References:** `<elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <6fppc6Fccpn1U1@mid.individual.net> <a99ef1b0-8071-4025-97ac-613e698a7617@b1g2000hsg.googlegroups.com> <6fshq4Fd7h3dU1@mid.individual.net> <7cc7dd28-653d-4dd0-8f75-1d8a48af48e0@27g2000hsf.googlegroups.com> <6futpgFdf2mmU1@mid.individual.net> <31c29c1c-8569-431a-b954-00a37bd5bd8d@r66g2000hsg.googlegroups.com> <320l9497kif80ih6pl1m6pa9hcd9pl537k@4ax.com> <6g0b6qFd2gltU1@mid.individual.net>`

```
On Aug 7, 9:21 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "Robert" <n...@e.mail> wrote in message
>
…[7 more quoted lines elided]…
> [end Robert]

[begin Pete}
> Yep, me too...
> [stuff deleted]
…[4 more quoted lines elided]…
> interest and enthusiasm by COBOL programmers.
[stuff deleted]
> Because the code is in COBOL they can modify it for special cases if they
> need to...
[end Pete]

My tools of choice are awk, sed, and grep, pulled together a bit with
the shell. I don't have the good fortune to have been in many Unix
shops like Robert, but I have used the same utilities that are
provided in MKS Toolkit a lot in Windows. (I that that gnu probably
has a similar set of utilities for Windows) Today it is more difficult
because the sysadmins don't like you to install "personal" software on
the corporate PC. I may have to start bringing in my own Notebook to
compensate. Every consultant or contractor should be able to bring his
own set of tools to the job.

If one can pull down all the source from the mainframe to a PC or
network drive, then running awk and sed and grep with pipes and the
like can be a powerful way to do some sophisticated and very focused
analysis of the source. That's what I usually use it for, for finding
things. Sometimes I do global replaces with sed, but I'm not as good
with the transformational aspects (actually modifying the code, as in
your "migration" strategy) as I am in the more "passive" analysis.

"Regular expressions" are very powerful things. Mastering their syntax
was/is a challenge to me, but worthwhile. It's been a while (several
years) since I've been able to use them. I hope to be able to do so
again soon.

Ken
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 29)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-08T11:55:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mcuo9453ufqr3io1ime1225h2f56qerm2d@4ax.com>`
- **References:** `<6fppc6Fccpn1U1@mid.individual.net> <a99ef1b0-8071-4025-97ac-613e698a7617@b1g2000hsg.googlegroups.com> <6fshq4Fd7h3dU1@mid.individual.net> <7cc7dd28-653d-4dd0-8f75-1d8a48af48e0@27g2000hsf.googlegroups.com> <6futpgFdf2mmU1@mid.individual.net> <31c29c1c-8569-431a-b954-00a37bd5bd8d@r66g2000hsg.googlegroups.com> <320l9497kif80ih6pl1m6pa9hcd9pl537k@4ax.com> <6g0b6qFd2gltU1@mid.individual.net> <05ae89f8-f111-4225-9aa9-dd979fad5596@k13g2000hse.googlegroups.com>`

```
On Fri, 8 Aug 2008 08:32:40 -0700 (PDT), "klshafer@att.net" <klshafer@att.net> wrote:

>My tools of choice are awk, sed, and grep, pulled together a bit with
>the shell. I don't have the good fortune to have been in many Unix
>shops like Robert, but I have used the same utilities that are
>provided in MKS Toolkit a lot in Windows. (I that that gnu probably
>has a similar set of utilities for Windows) 

"Ch" gives you a Unix command prompt on Windows without installing or booting Unix. 
All those utilities are available. In addition, it is a C interpreter, enabling you can
type C on the command line or use it as a scripting language.
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 23)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-08-08T08:08:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3pko94dlfqq9u0shhoeegeijrbq0i0r86f@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <oh5a94djujajtek423m6e7rui63bfjsip3@4ax.com> <g74ero$bnd$1@reader1.panix.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <6fppc6Fccpn1U1@mid.individual.net> <a99ef1b0-8071-4025-97ac-613e698a7617@b1g2000hsg.googlegroups.com> <6fshq4Fd7h3dU1@mid.individual.net>`

```
On Wed, 6 Aug 2008 14:49:39 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> Almost... It needs to be preceded by "OT:"
>>
…[3 more quoted lines elided]…
>Contracting in the CoBOL world. Hence, CoBOL and Contracting.

It seems pretty illogical to discriminate between "on topic" and "off
topic" by using the initials of those two terms.
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 20)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-05T00:02:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gulf9410ib66dilmmacjdccq7p2sgabc8m@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <oh5a94djujajtek423m6e7rui63bfjsip3@4ax.com> <g74ero$bnd$1@reader1.panix.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com>`

```
On Mon, 4 Aug 2008 13:11:22 -0700 (PDT), "klshafer@att.net" <klshafer@att.net> wrote:

> Also, there can be multiple posts by
>multiple agencies for the same client slots. What to do in "choosing"
>the "right" agency?

Apply to ALL the agencies. Maybe one will think you're suitable while the others don't.

I used to make that mistake. I'd see a good sounding job in Keokuk and think 'Oh, I
already applied for that job.' Yeah, but to a different agency. I once applied to five
agencies for the same job. One got me an interview; I didn't hear from the other four.

The agency will always call before submitting you. If another agency calls later, just
tell them you've already been submitted for that job. 

Agencies will tell you double-submission is a mortal sin. Nonsense. If a client DOES see
the same person from two agencies, he'll keep the cheaper of the two and discard the
other. THAT's why agencies don't want you to do it.

> Such are the problems of "going back to square
>one." Soliciting repeat business and polling your informal network of
…[4 more quoted lines elided]…
>of imagination on my part.

It's a numbers game. The more eyes see your resume, the higher the probability of a hit. 

>For me, it took about thirty years to distill all this down to what I
>call my Rules of Engagement. I've gone minimalist, reducing them to
…[3 more quoted lines elided]…
>respect are not.

How do you handle jerk recruiters? Do you hang up or do you play their silly game?

I don't know the right answer. 

>Rule 2: In consideration of my submission of my resume, you will keep
>me informed of all progress, or lack thereof, of my submission to your
>client.

Some advise calling every other day for a progress report. 

>I now "require" an Agency to verbally agree to these before I e-mail
>them my resume. I believe it is okay to be _insistent_, if what you
…[12 more quoted lines elided]…
>(I've not come up with anything else.)

Ask for the recruiter's direct phone number. If he can't or won't give it, he's either
working from a boiler room, fishing or calling from a shack in some third world country. 

Some recruiters are themselves contractors. They're not at the agency and are not involved
with submitting you. They simply don't know about your progress. In those cases, you'll
often get a second call from the account exec or other agency rep. He's the one to ask
about progress.
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 21)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-08-06T02:14:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6fr5hsFcr7ctU1@mid.individual.net>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <oh5a94djujajtek423m6e7rui63bfjsip3@4ax.com> <g74ero$bnd$1@reader1.panix.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <gulf9410ib66dilmmacjdccq7p2sgabc8m@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:gulf9410ib66dilmmacjdccq7p2sgabc8m@4ax.com...
> On Mon, 4 Aug 2008 13:11:22 -0700 (PDT), "klshafer@att.net" 
> <klshafer@att.net> wrote:
…[46 more quoted lines elided]…
> I don't know the right answer.

I handle jerk recruiters, the same way I handle any other jerk. (The actual 
treatment varies, depending on specific cases, but it is very much along the 
lines of: "...stop wasting my time, as it is obvious we are not going to do 
business.") They should get special treatment because they're in IT?  I 
don't think so.

You don't need to tolerate bad behaviour or bad manners from anyone, just 
because you think you need their "service".

The fact is that you don't need a substandard, one-sided, ripoff, of what is 
supposed to be a "service", from ANYBODY... Pandering to it simply 
perpetuates it.

Ever tried promoting yourself? You have a skill you need to market. 
Mistakenly, you believe you can't get a job without an agency, but you 
haven't thought about how you might go about promoting your own service.

If you want some ideas that have proven successful in the past, contact me 
privately.

You have a good problem solving mind. Use it on your own behalf.

You may be surprised at the results. Build your own personal business based 
on successful delivery, and you won't need to deal with jerks.

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (Was: All X'0D' lost during...)

_(reply depth: 21)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-08-05T12:21:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12c8f8ed-f1ee-4f9e-b498-d2787de7b510@w7g2000hsa.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <oh5a94djujajtek423m6e7rui63bfjsip3@4ax.com> <g74ero$bnd$1@reader1.panix.com> <elgc94hm5hsif2dhcbgmntnufc2eju2pvr@4ax.com> <g76iep$77r$1@reader1.panix.com> <29f6a466-11d5-4953-9bcb-6e319e6f9553@2g2000hsn.googlegroups.com> <gulf9410ib66dilmmacjdccq7p2sgabc8m@4ax.com>`

```
On Aug 5, 1:02 am, Robert <n...@e.mail> wrote:
> On Mon, 4 Aug 2008 13:11:22 -0700 (PDT), "klsha...@att.net" <klsha...@att.net> wrote:
> > Also, there can be multiple posts by
…[24 more quoted lines elided]…
> It's a numbers game. The more eyes see your resume, the higher the probability of a hit.

This is helping me. In the past, my need for "approval" ;-)
predisposed me to listen to their pleas to avoid the double
submission. Without agreeing entirely with you, I can now see that
granting an "exclusive" to an agency is something that they should
"earn" from me, by providing me, uh, _some_ kind of consideration. (To
be defined.)

Granting an "exclusive" to an Agency is part of making them a
Preferred Agency. Having successfully placed me elsewhere might
qualify them; certainly having placed me multiple times should quality
one.

Beyond that, I see your point: Absent such qualification, submit to
them all, and let THEM and the CLIENT sort it out. :-)

>
> >For me, it took about thirty years to distill all this down to what I
…[8 more quoted lines elided]…
> I don't know the right answer.

I don't know _the_ right answer, and I may not even know _a_ right
answer. I only know of some _vanilla_ answers. Do they work? Depends
on what you mean by "work." If we mean "Does it make me feel better?",
well then, yeah, here are some things that work -

1. Hang up on them (story below.)
2. Demote them (remove them from your Approved Agency list, and tell
them so.)
3. Tell all your friends/peers how jerky they are.
4. If otherwise un-engaged, bug them every day about the non-existent
position. This is an excellent opportunity to practice your "air of
incredulousness", a very useful tool.
5. Never bad-mouth them to a client or prospective client, for this
could be (albeit weak) grounds for a lawsuit. Instead, when asked by
the client, "What do you think of Agency X?", respond with "I've had
dealings with them, and there's really nothing I can say," and then
shrug. Practice doing that, in the one-in-a-thousand chance it will
happen.
6. Erase their phone messages. There is joy to be had in deletion.

The Story:

Several years ago, and it was after all, in the throes of the Great IT
Famine of 2001-2003, that I encountered an opportunity, and responded
over DICE, and was contacted by a Recruiter, for a position for which
I was a very good fit, according to the stated requirements. I set
forth my Rules of Engagement, and I recall she agreed, and then later
I heard nothing. Follow up e-mails and phone calls by me were in vain.

Then, a year later or so, the same Recruiter calls again, with exactly
the same Requirements. By this time I was working, and I so informed
her that I was no longer looking. She asked me for names and contact
info for anyone else I knew who was qualified, never offering me
anything, finders' fee, subscription to Dr. Dobbs, nada, in return. I
hung up on her.

Was I "educating her", or was I just *mean*? I'd like to think the
former, but sometimes I fear I was the latter...

>
> >Rule 2: In consideration of my submission of my resume, you will keep
…[3 more quoted lines elided]…
> Some advise calling every other day for a progress report.

This might be a bit more often than I would do, and yet, entirely
reasonable. It's hard for me to guauge the length of each "window of
opportunity." Some recruiters claim it is only 48 hours. And yet the
decisions sometime take months, literally.

>
> >I now "require" an Agency to verbally agree to these before I e-mail
…[13 more quoted lines elided]…
> >(I've not come up with anything else.)


Hadn't thought of that. It occurs to me that a "trade" could be in
order. To wit, post only your home/business landline phone on DICE/
Monster and your resume. Upon contact, express willingness to trade
your cell for their direct/cell.

> Ask for the recruiter's direct phone number. If he can't or won't give it, he's either
> working from a boiler room, fishing or calling from a shack in some third world country.
…[4 more quoted lines elided]…
> about progress.

It is increasingly difficult to find recruiters who have a face-to-
face relationship with the decision-makers. I usually ask, and I feel
I usually get an honest reply, which too often goes along the lines
of, "We work only off the list that their HR department faxes us every
week, and we submit only to their HR department. That's the way XYZ
Corp requires all the approves vendors to do it."

A recruiter/rep who golfs, bowls, fishes, or plays poker/bridge with
his client is now good as gold, even better. They are beyond Approved
Vendors. They are Platinum.

Ken
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 15)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-03T13:59:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g74djd$b2v$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <6d0lk.9080$vn7.4834@flpi147.ffdc.sbc.com> <22p99452rh1df8lr0hf1o6psbgvsu3id4g@4ax.com> <6fkhg0Fc0ck4U1@mid.individual.net>`

```
In article <6fkhg0Fc0ck4U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
>"Robert" <no@e.mail> wrote in message 
>news:22p99452rh1df8lr0hf1o6psbgvsu3id4g@4ax.com...

[snip]

>> Contractor is a misnomer, because it implies a contractual obligation for 
>> duration of
…[17 more quoted lines elided]…
>are fine, but there has to be cash in lieu of notice.

One might think so, Mr Dashwood, and it might be done that way in other 
places... but in the USA I have never been offered a contract which says 
that I will get US$N if the other party decides to terminate early.  A few 
years (decades?) back it used to be common for pimps to inclide a 
paragraph holding the consultant resonspible for any monies the pimp would 
have made if the consultant stopped working with the client before the 
client gave a 'Mother, May I'... *that* resulted in a rather curious 
exchange between me and the headhumter when I did not feel the job was a 
Good Fit:

Me: 'I can tell after a few weeks that this isn't going to work out; if 
you want I'll stay on for another two weeks to train my replacement but no 
longer than that.'

PIMP: 'WHAT ARE YOU TALIKING ABOUT? THE CONTRACT SAYS IF THEY WANT YOU TO 
STAY, YOU STAY, AN' THEY AIN'T SAID FOR YOU TO GO YET!!! YOU LEAVE NOW AND 
YOU'RE GONNA OWE ME MOMEY MOMEY MONEY MONEY!!!'

Me: 'Please... we can deal with this as Honorable Businessmen... or I can 
go into work tomorrow and tell - in perfectly acceptable, family-newspaper 
front-page English - the project leader what I think of his 'leadership' 
skills, the project manager what I think about his estimates, assignments 
and timelines for the work to be done and the project director what I 
think about his choice in subordinates, leadership-styles and 
secretaries...

... and you'll get a call about five minutes later, I'll get escorted out 
(dangerous threat that I am!) by Security and you will *never* place 
another body in that shop *ever* again.  How would you rather this turn 
out?'

>
>Why don't you negotiate your own contract with the agency and let them worry 
>about IBM terminating it?

In the Actors' World those are called 'play-or-pay' contracts... in other 
businesses they are, in my experience, reserved for instances not where a 
consultant negotiates with a client but where a lawyer for the party of 
the first part negotiates with the lawyer for the party of the second 
part.

In short... it ain't done that way here.

DD
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 16)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-03T21:19:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<frdc94185m9ar0gvhs4ifle15t5nhf4522@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <6d0lk.9080$vn7.4834@flpi147.ffdc.sbc.com> <22p99452rh1df8lr0hf1o6psbgvsu3id4g@4ax.com> <6fkhg0Fc0ck4U1@mid.individual.net> <g74djd$b2v$1@reader1.panix.com>`

```
On Sun, 3 Aug 2008 13:59:09 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <6fkhg0Fc0ck4U1@mid.individual.net>,
>Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[34 more quoted lines elided]…
>client gave a 'Mother, May I'... 

Big Five contracting companies bring in low-paid foreigners and make them sign contracts
in which they promise to repay the cost of training if they leave in less than two years.
Contractors get two weeks' training claimed to be worth $8K.

In other times and places, the practice is called debt bondage or peonage. It is used
primarily to force women into prostitution and children into sweatshops. In the US, it is
used to force Indians into programming.

Personal service contracts cannot be enforced by 'specific performance.' That would be
slavery. The workaround is a debt that cannot reasonably be paid.  

Actually, it can. I've pointed out  that by increasing their pay from $25 to $50/hr, they
could repay the debt and buy their freedom in two months (320 hrs * $25 = $8K). They
didn't believe me, or thought there must be a catch.

>>Why don't you negotiate your own contract with the agency and let them worry 
>>about IBM terminating it?

Employment At Will is law in all US states except Montana. A written contract overrides
that, but contracting companies are very reluctant to do so because they have no control
over the client's decisions.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 10)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-08-04T14:55:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8edcf9f9-cd9e-4712-ab3f-79df57beee4e@w7g2000hsa.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com> <M5kkk.16863$mh5.2242@nlpi067.nbdc.sbc.com> <vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com> <g6ulct$ceo$1@reader1.panix.com> <ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com>`

```
On Aug 1, 11:20 pm, Robert <n...@e.mail> wrote:

Robert: > >>If I refused to do taks for which I'm not qualified, I'd
be looking for
> >>a new job every month or two.

I would hazard that, based upon your immediately previous "track
record" with the client, that management deemed you "qualified"
because of your ability to produce. And that this fact trumped the
fact of your limited or non-existent experience with the new tool/
language. That this might be so is a Very Good Thing, and not a Bad
Thing at all. Such is the stuff of Opportunities to learn new things.
And yet, I agree with the Doc below...

Doc: > >Sometimes, Mr Wagner, it works out that one winds up having
what one is
> >willing to accept.  
> >Our experiences, of course, may be different... I've
…[6 more quoted lines elided]…
> >rewiring a generator.'

What I read here is how we have a professional obligation to provide
full disclosure to the client, and this means going beyond being
"honest" (which is where you answer questions truthfully), and to the
point of being "forthright", where you _volunteer_ information to the
client which is relevant to their decision-making. Where I differ a
wee bit from the 'Doc here is I consider it to be completely in the
client manager's domain whether or not to make that assignment to me,
provided I make full disclosure of facts about my history and ability.
Volunteering that one has almost no VB experience is forthright;
giving examples of other engagements where one had limited, or no,
experience with a new language, but had demonstrated ability to learn
and produce, and still one was able to complete the task in a
"reasonable" amount of time, is sufficient here. The only "refusal" I
see as necessary is to refuse to be boxed into a deadline corner. A
comment like, "Well, I haven't done this thing in this language Y
before, so I don't really know how long it will take me, but this is
how long it took me in a similar situation where I learned language X
on the fly blah blah blah" seems appropriate to me. Then let the
Manager _decide_. Deciding for him by _refusing_ is my doing his job
for him, and I don't get paid as well as him :-) ...


Robert: > Word gets around that you're a crochety old guy, which is
the kiss of death outside the
> mainframe world. I work with people in their 20s and 30s who think old people are too slow
> and out of style. They'll fire you in a heartbeat. It takes an effort to wow them.- Hide quoted text -

Question: What is the average velocity of the winner in each of the
Indianapolis 500 mile races?
Answer:   Zero.

The point being, the finish line is the same as the starting line,
just 200 laps later, and the car winds up in the same place where it
started.

Oh. Average "speed" is somewhat in excess of 200 mph.

In math/physics terms, "speed" is a scalar quantity; "velocity" is a
vector quanity: it has both scalar _and_ directional components.

How I care to "project" myself is thus: what others, especially those
in their 20's and 30's, might see as my "slowness" is my deficit in
the "scalar" quantity. I make up for that in "velocity". And it is
experience which helps one see out to the horizon to know what
direction one should take, and whether current, albeity speedy,
efforts are taking you in that direction or are simply spinning your
wheels.

Making such a distinction may cost you opportunities, and it may gain
you some. The important thing is that making others aware that this
distinction is important to you helps both parties (you and the
client) in the engagement selection process. That is some (but not
all) of the "fit" determination that we all go through.

My experience is that most decisions are not made on "optimum"
criteria (eg. the "best technical fit"), but rather, on adequacy of
fit plus the client and co-workers being "comfortable" with the
decision. If I have been successful, it is not because I was able to
"wow" either the client or the other staff (I may not be smart enough
or talented enough for that :-) ) - it is because I convinced them I
was adequate and they were comfortable with me.

Ken
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-05T12:18:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g79gdu$3fd$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <g6ulct$ceo$1@reader1.panix.com> <ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com> <8edcf9f9-cd9e-4712-ab3f-79df57beee4e@w7g2000hsa.googlegroups.com>`

```
In article <8edcf9f9-cd9e-4712-ab3f-79df57beee4e@w7g2000hsa.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:
>On Aug 1, 11:20�pm, Robert <n...@e.mail> wrote:

[snip]

>Doc: > >Sometimes, Mr Wagner, it works out that one winds up having
>what one is
…[29 more quoted lines elided]…
>for him, and I don't get paid as well as him :-) ...

One of the reasons I went the route of the consultant/contractor/hired 
gun, Mr Shafer, was because of the commandment - I think from the Book of 
Leviticus - of 'Thou Shalt Not Pay a Good Programmer more than a Bad 
Manager but a Consultant may'st thou pay more'... be that as it may:

My work goes out over my signature.  There are times when I disagree with 
what I told must be done and I make my disagreements known, at times to 
the point of commenting the code with words like 'chuckle-head'... but if 
the code is over my signature then it is my work.  There is a point where 
I have said 'This I Will Not Do'... now, how I determine that such a point 
has been reached is another matter, entire, and perhaps a better subject 
for consideration as Aesthetics... but some things I will not do.

There are some things I will not stand by and watch done, either; if He 
Who Signs My Timesheet says 'Wait here while I use this loaded pistol as a 
hammer' I go away, despite the Direct Order.

I chose the example of plumber and electrician carefully, Mr Shafer... a 
task, to my mind, includes a deadline; it might be difficult to get an 
Electrician's Certification Exam re-scheduled in time to get the plumber 
to study for it, pass it and then re-wire the generator... not impossible, 
just difficult.  Likewise, were I told 'You have three days to learn this 
particular chip's Assembley language and code this heart-pacemaker warning 
notification routine'... no.  This I will not do, there's always another 
job.

Years ago I worked with a fellow who had coded some of New York City's 
original emergency response telephone system.  He said that the gravity of 
the situation was such that afterwards he would only work with financial 
systems; his explanation was along the lines of:

'You screw up on a 911 call, the ambulance goes to the wrong street or the 
wrong block of the right street and somebody dies.  In finance... it's 
only money.'

Likewise, an error in rewiring a generator causes a building to go up in 
flames and an error in a pacemaker's firmware causes someone to die.  I 
cannot stop a Corner-Office Idiot from making such orders, I can only make 
sure that what I have signed off on does not, to the best of my own 
knowledge, cause a catastrophe.

[snip]

>Question: What is the average velocity of the winner in each of the
>Indianapolis 500 mile races?
>Answer:   Zero.

Really?  I would have said 'that depends on when and how the measurement 
was taken.'

DD
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 12)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-08-05T12:50:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32347f83-d9e2-4773-9488-dbf203ae16a2@2g2000hsn.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <g6ulct$ceo$1@reader1.panix.com> <ati794tbvu02k92t3od5t0u6g6culuscob@4ax.com> <8edcf9f9-cd9e-4712-ab3f-79df57beee4e@w7g2000hsa.googlegroups.com> <g79gdu$3fd$1@reader1.panix.com>`

```
On Aug 5, 8:18 am, docdw...@panix.com () wrote:
> In article <8edcf9f9-cd9e-4712-ab3f-79df57bee...@w7g2000hsa.googlegroups.com>,
>
…[32 more quoted lines elided]…
>

Well put, Mr. DD. I am glad that you pointed out that in Matters of
Public Safety, the bar is raised higher. And I cheerily second your
distinction between plumber and electrician. My saintly Father
likewise took umbrage at his occupation, that of a pipefitter, being
compared to that of a plumber. Fitting pipes running cherry hot at
some odd hundred degrees fahrenheit is not quite the same as turning
the wrench on the house sewage line.

It is a smart fellow who can see the distant horizon in these
implications. Like the ex-Marine I worked with on the Dept of Motor
Vehicles system, and who insisted on doing his finest work in the auto
registration lookup. His rationale: the plate number was the first
thing the state's finest called in when stopping a vehicle, and the
information returned to him, was indeed, potentially a matter of life
and death.

> Likewise, an error in rewiring a generator causes a building to go up in
> flames and an error in a pacemaker's firmware causes someone to die.  I
…[11 more quoted lines elided]…
> was taken.'

When the start-point and end-point are co-inciding, and the time
elapsed between start and finish be nonzero (though no matter how
small, any epsilon will do, as my calculus teacher taught me), the
answer is always zero. Or more precisely, the zero vector. (The zero
vector is that vector, which when added to any vector, returns said
vector unchanged. It is, therefore, the "additive identify" in vector
algebra. But that is so long ago, that I could stand to be corrected.)

Ken
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-06T09:46:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g7bruc$s9n$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <8edcf9f9-cd9e-4712-ab3f-79df57beee4e@w7g2000hsa.googlegroups.com> <g79gdu$3fd$1@reader1.panix.com> <32347f83-d9e2-4773-9488-dbf203ae16a2@2g2000hsn.googlegroups.com>`

```
In article <32347f83-d9e2-4773-9488-dbf203ae16a2@2g2000hsn.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:
>On Aug 5, 8:18�am, docdw...@panix.com () wrote:
>> In article <8edcf9f9-cd9e-4712-ab3f-79df57bee...@w7g2000hsa.googlegroups.com>,
>> klsha...@att.net <klsha...@att.net> wrote:
>>
>> My work goes out over my signature. 

[snip of my own words and I apologise for my midsentence interruption]

>> ... but some things I will not do.
>>
…[24 more quoted lines elided]…
>Public Safety, the bar is raised higher.

It may sound odd in these Days of Positive Thinking to say 'I refuse to 
even begin working on this task under these conditions'... but there's 
always a 'bar' and always a conscious decision to leap over/belly up to 
it.

[snip]

>It is a smart fellow who can see the distant horizon in these
>implications.

Shucks, you'se jes' easily impressed... but if you run across such a smart 
fellow I'd appreciate an introduction.

[snip]

>> >Question: What is the average velocity of the winner in each of the
>> >Indianapolis 500 mile races?
…[8 more quoted lines elided]…
>answer is always zero.

Now this is going back a few decades for me, as well... but as I recall 
the definition of velocity is 'rate of change in position over time'.  
('over time' may be a redundancy but I also recall something about 
deriving velocity from the tangent of an acceleration-curve and the point 
of tangency being called 'instantaneous velocity', the velocity of the 
instant... but, as I said, it has been a few decades.)

That being the case: the race-winner passes the finish-line and her car 
stops.  Her velocity (relative to the surface of the earth... a niggling 
point, to be sure, but for some it is a post-Einsteinian universe) is 
zero, certainly.  (Let it also be assumed, for simplicity's sake, that the 
mere act of crossing the finish-line makes her 'the winner' and this 
status is not dependent on other variables such as The Judges' 
Announcement.)

The winner then opens the car door and strides boldly to the Winner's 
Circle (or whatever they have).  During that transition the winner's 
position changes at a determinable rate; by definition the winner has a 
velocity.  The winner reaches the Circle and accepts awards and 
accolades... velocity's back to more-or-less zero.

Not to degrade the value of what your teacher taught, of course... it 
reminds me of A Story, when I was sitting in a lecture-hall in a 
university in Upper Manhattan and the physics-professor was trying to 
introduce the concept of 'displacement'.  He said 'Assuming that you live 
in The Grid section of the City and there's nothing like a park or a river 
that stops you... you exit your apartment building, turn left and walk 
three blocks.  You then turn right and walk four blocks.  How many blocks 
have you gone from your building?'

I was younger, in those days, and my responses were a bit sloppier, as 
those of Youth might be.  From the silent, seated ranks of students came 
my question of 'Which are uptown and which are crosstown?'

The professor smile and asked back 'Who's the New Yorker?'

DD
```

###### ↳ ↳ ↳ CoBOL and Contracting (was: All X'0D' lost during reading line sequential file)

_(reply depth: 14)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-08-06T09:07:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<907496cf-c59a-49cc-82ef-965fa27a3086@t54g2000hsg.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <8edcf9f9-cd9e-4712-ab3f-79df57beee4e@w7g2000hsa.googlegroups.com> <g79gdu$3fd$1@reader1.panix.com> <32347f83-d9e2-4773-9488-dbf203ae16a2@2g2000hsn.googlegroups.com> <g7bruc$s9n$1@reader1.panix.com>`

```
On Aug 6, 5:46 am, docdw...@panix.com () wrote:
> In article <32347f83-d9e2-4773-9488-dbf203ae1...@2g2000hsn.googlegroups.com>,
>
> klsha...@att.net <klsha...@att.net> wrote:
interruption]
> [snip]
>
…[4 more quoted lines elided]…
> fellow I'd appreciate an introduction.

Well, I was referring to the ex-Marine (also a contractor) as the
smart fellow ;-), so sure, when we call the Intergalactic CoBOL
Contractors Conference, I'll introduce you to him. You'd like him.
Once, when being hassled by a Manager on why stated tasks had not yet
been completed within the ex-Marine's own estimates, he said without
blinking, "When I made those estimates I was under the false
impression that the project was properly managed." :-)

>
> [snip]
…[32 more quoted lines elided]…
> accolades... velocity's back to more-or-less zero.

Hmmm... you refer to the winner as "her". Must be a reference to
Danika Patrick. Yes, she'll win the Big One (Indy 500) someday...
And oh, by the way, here's a fact probably largely unknown outside of
Indiana and Indy 500 fans - I believe it is actually the _car_ that is
the winner, at least as far as some legal payout and paperwork goes.
The driver goes along for the ride, and is handsomely paid as well.

You remember your introductory Calculus very well.

>
> Not to degrade the value of what your teacher taught, of course... it
…[13 more quoted lines elided]…
>

Ahhh, yes, you take me back... twenty-five years or more. I think it
was the first time I was in Manhattan. Got directions from somebody on
how to get somewhere, don't remember what. What I remember is that it
was just "a few Avenues" over, and then a few streets up. Naturally, I
thought it was only several blocks, a five minute walk.

It took forever to walk "across town." Probably seemed as long as you
spent in South Bend :-).

But in keeping with being On Topic, here is one of my New Yawk
stories...

Back before the Internet, back before even fax machines, back even
before hard drives were popular on PC's, and all you had were
typewriters, and PC's with floppies, IBM Proprinters, and photocopy
machines, I'd do my out-of-town (i.e., outside Indiana) job searches
by going to the County Library and reading the Sunday papers for their
classifieds. NYT, Boston Globe, Philly Inquirer, and the like.

Wow, there were a lots of ads in the NYT. I had some Honeywell Level 6
minicomputer experience (later called DPS 6), and Met Life was working
on a huge project with a whole slew of them, and experienced people
were hard to get. This was, oh, early 80's. I found a number of agency
ads soliciting Level 6 people, and yeah, by the wording, you could
tell they were all for the same Met Life slots, so I called a few of
them (three or four), vetted them, more or less, best as I could,
naive fellow that I am, and called back the one I liked best. The
conversation went like this:

Me: Well, I'd be new to the New York area, so I've checked out the
companies that are soliciting for this position, and because of your
competitive rate and how you've described your company and blah blah
other gratuitous and yet factual stuff blah blah, I've decided I want
to go with *you*.

Agent: (In the most pronounced New Yawk accent) I am so _flattered_!

Now, twenty-five years later, I can still hear her voice, and I am
still unsure if she was genuinely flattered or was just making fun of
me, a rube from Indiana. :-)

I didn't get that job. Didn't have the exact "forms package"
experience, though that is another story.

A few years later, after doing a stint in Washington, DC, and I still
desired a tour-of-duty in NYC, I was recruited by an Irishman, though
he later became a citizen, I think. He spent all day and all night in
Manhattan, selling, selling, selling (as one might think an Irishman
might do), before he took a late night train to Connecticut, where he
lived.

He sold me, and that was the job I _did_ get. CoBOL, Honeywell
mainframe DMIV/TP. In the WTC.

ken
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (was: All X'0D' lost during reading line sequential file)

_(reply depth: 15)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-06T17:26:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g7cmsr$mp5$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <32347f83-d9e2-4773-9488-dbf203ae16a2@2g2000hsn.googlegroups.com> <g7bruc$s9n$1@reader1.panix.com> <907496cf-c59a-49cc-82ef-965fa27a3086@t54g2000hsg.googlegroups.com>`

```
In article <907496cf-c59a-49cc-82ef-965fa27a3086@t54g2000hsg.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:
>On Aug 6, 5:46�am, docdw...@panix.com () wrote:
>> In article <32347f83-d9e2-4773-9488-dbf203ae1...@2g2000hsn.googlegroups.com>,
…[13 more quoted lines elided]…
>Contractors Conference, I'll introduce you to him.

Most greatly appreciated.

[snip]

>> [snip]
>>
…[10 more quoted lines elided]…
>> >answer is always zero.

[snip]

>> The winner then opens the car door and strides boldly to the Winner's
>> Circle (or whatever they have). �During that transition the winner's
…[5 more quoted lines elided]…
>Danika Patrick.

No, it is a reference to the Olde Joke of '... and the Emergency Room 
doctor looked at surviving boy and said 'Oh my God, that's my son!'

>Yes, she'll win the Big One (Indy 500) someday...
>And oh, by the way, here's a fact probably largely unknown outside of
>Indiana and Indy 500 fans - I believe it is actually the _car_ that is
>the winner, at least as far as some legal payout and paperwork goes.
>The driver goes along for the ride, and is handsomely paid as well.

Hmmmm... you might want to take a look at http://www.indy500.com/stats/ to 
see how consistently this is applied.  

According to 
http://www.indy500.com/images/stats/pdfs/pole_position_winners.pdf 
(category 'Qualifying Records', labelled 'Pole Position Winners') the 
driver is listed first, then the 'Entrant' (I assume the sponsor of the 
vehicle) and then the car/engine.

According to 
http://www.indy500.com/images/stats/pdfs/indianapolis_500_race_winners.pdf 
(category 'Race & All-Time States', labelled 'Race Winners') the car 
number is listed first, then the driver, then the car name/entrant 
chassis/engine.

According to http://www.indy500.com/images/stats/pdfs/ages_of_winners.pdf 
(category 'Winners', labelled 'Ages of Winners') the name is listed.

>
>You remember your introductory Calculus very well.

I don't remember very much calc beyond it, I would say... but I find it 
helpful to be able to see the world in that manner, at times... what do I 
know, anyhow?

[snip]

>> The professor smile and asked back 'Who's the New Yorker?'
>>
…[8 more quoted lines elided]…
>spent in South Bend :-).

But... what one can learn from such a stroll, what one sees, the drama, 
the comedy, the tragedy, the buffoonery... the Bronx is up and the 
Battery's down.  I was fortunate, in my youth, to spend time with a 
genuine Bronx Boy, one whose parents moved out there along the Third 
Avenue Elevated Train line (the 'El') from the Lower East Side after they 
were married in 1910; from him I learned how to get around The City, how 
to find Good Stuff and how to recognise when it was time to Get Out.

The area around the University Park Apartments in Mishawaka might be 
quieter and cleaner... but the Soup of Life needs a jolt of *spice* in 
some spoonsful.

[snip]

>Agent: (In the most pronounced New Yawk accent) I am so _flattered_!
>
>Now, twenty-five years later, I can still hear her voice, and I am
>still unsure if she was genuinely flattered or was just making fun of
>me, a rube from Indiana. :-)

The sincerity of an agent is never - or always - to be questioned.  I have 
a similar auditory smile-inducer from a secretary who was talking with her 
grandmother over the telephone about a ring her friend Anthony ('Tony') 
gave her... ya-ta-ta, ya-ta-ta, 'Y'oughta see it, Gran'maw, it's so noice 
and shi-ney... nah, it ain't nothin' like that, we're just friends, it's 
not like it's a doi-mond'r somethin'... GRAN-maw, it's *only* TOE-nee, 
c'mAA-AAHHhhhnnnn!'

[snip]

>He sold me, and that was the job I _did_ get. CoBOL, Honeywell
>mainframe DMIV/TP. In the WTC.

I did a brief gig there as well, in the mid-90s... an International Bank 
that was looking to move a trading limits system from something they'd 
cobbled together using a PC and DBase to an IBM mainframe using CICS.

They were shocked, *shocked* to discover that this would be Much More 
Expensive.

(It was one of the few Project Overview documents I ever generated... a 
Corner-Office Idiot said 'These numbers are just too high... what's all 
this 'BLS/FAD' stuff you've allocated time for?  It looks like... a 
quarter of the project!'

I replied 'Sir, the United States Bureau of Labor Statistics has noticed 
that twenty-five percent of a project's time is lost to 'fatigue, 
absenteeism and delay' and that an accurate Project Overview should make 
allowances for this; if you want the timelines to be written with a 
willful ignoring of Federal guidelines I'm sure I can include mention of 
that in the Introduction.')

DD
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (was: All X'0D' lost during reading line sequential file)

_(reply depth: 15)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-06T19:16:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1qek94tht2v2jq3ptgkj1ophc5a4fdfeel@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <8edcf9f9-cd9e-4712-ab3f-79df57beee4e@w7g2000hsa.googlegroups.com> <g79gdu$3fd$1@reader1.panix.com> <32347f83-d9e2-4773-9488-dbf203ae16a2@2g2000hsn.googlegroups.com> <g7bruc$s9n$1@reader1.panix.com> <907496cf-c59a-49cc-82ef-965fa27a3086@t54g2000hsg.googlegroups.com>`

```
On Wed, 6 Aug 2008 09:07:20 -0700 (PDT), "klshafer@att.net" <klshafer@att.net> wrote:

>On Aug 6, 5:46ï¿½am, docdw...@panix.com () wrote:
>> In article <32347f83-d9e2-4773-9488-dbf203ae1...@2g2000hsn.googlegroups.com>,
…[17 more quoted lines elided]…
>impression that the project was properly managed." :-)

I'm a former Marine (recon) and I wouldn't make such an insulting remark to a manager's
face. I'd present a detailed list of _facts_ about the delay. 

I'm also a former options trader. A typical remark on the floor to a 35 year old who's
lagging, "Hey old man, you're in the way. Iif you can't keep up, take your cane and go
trade stocks."
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (was: All X'0D' lost during reading line sequential file)

_(reply depth: 16)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-08-06T18:38:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1d1803b3-b7ba-46ff-bcab-91cbc7bd89f9@f63g2000hsf.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <8edcf9f9-cd9e-4712-ab3f-79df57beee4e@w7g2000hsa.googlegroups.com> <g79gdu$3fd$1@reader1.panix.com> <32347f83-d9e2-4773-9488-dbf203ae16a2@2g2000hsn.googlegroups.com> <g7bruc$s9n$1@reader1.panix.com> <907496cf-c59a-49cc-82ef-965fa27a3086@t54g2000hsg.googlegroups.com> <1qek94tht2v2jq3ptgkj1ophc5a4fdfeel@4ax.com>`

```
On Aug 6, 8:16 pm, Robert <n...@e.mail> wrote:
> On Wed, 6 Aug 2008 09:07:20 -0700 (PDT), "klsha...@att.net" <klsha...@att.net> wrote:
> >Well, I was referring to the ex-Marine (also a contractor) as the
…[8 more quoted lines elided]…
> face.

Well, it's not what I would say either, and didn't, though I have
probably said stuff nearly as bad a time or two, but that was long
ago :-)...

> I'd present a detailed list of _facts_ about the delay.

Well, yes, he did that. Repeatedly, he hold me afterward. So there had
been no redress of his grievances. And yet, the Manager tried to hold
him to his estimates. It may very well be that his statement should
have been taken literally, insult or not.

>
> I'm also a former options trader. A typical remark on the floor to a 35 year old who's
> lagging, "Hey old man, you're in the way. Iif you can't keep up, take your cane and go
> trade stocks."

Seems to me that, if Management was aware of this "hostile"
environment, they could have been in violation of the Americans with
Disabilities Act. But I'm not a lawyer.

ken
```

###### ↳ ↳ ↳ Re: CoBOL and Contracting (was: All X'0D' lost during reading line sequential file)

_(reply depth: 17)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-06T23:54:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sdvk949e5ieqigukjm6m2ia20mgqe9p30r@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <8edcf9f9-cd9e-4712-ab3f-79df57beee4e@w7g2000hsa.googlegroups.com> <g79gdu$3fd$1@reader1.panix.com> <32347f83-d9e2-4773-9488-dbf203ae16a2@2g2000hsn.googlegroups.com> <g7bruc$s9n$1@reader1.panix.com> <907496cf-c59a-49cc-82ef-965fa27a3086@t54g2000hsg.googlegroups.com> <1qek94tht2v2jq3ptgkj1ophc5a4fdfeel@4ax.com> <1d1803b3-b7ba-46ff-bcab-91cbc7bd89f9@f63g2000hsf.googlegroups.com>`

```
On Wed, 6 Aug 2008 18:38:02 -0700 (PDT), "klshafer@att.net" <klshafer@att.net> wrote:

>On Aug 6, 8:16ï¿½pm, Robert <n...@e.mail> wrote:

>> I'm also a former options trader. A typical remark on the floor to a 35 year old who's
>> lagging, "Hey old man, you're in the way. Iif you can't keep up, take your cane and go
…[4 more quoted lines elided]…
>Disabilities Act. But I'm not a lawyer.

There's no management on a trading floor. Anything goes, like Usenet. They do break up the
frequent fistfights.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 8)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2008-08-01T17:13:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6fguh4FbdddqU1@mid.individual.net>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <b41ff8db-9fc2-4652-8b20-a103608884dc@k37g2000hsf.googlegroups.com> <sje2945ahjsv8fr7f82rcsfr06855g6amh@4ax.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com> <M5kkk.16863$mh5.2242@nlpi067.nbdc.sbc.com> <vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com>`

```
In article <vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com>,
	Robert <no@e.mail> writes:
> On Thu, 31 Jul 2008 09:36:16 -0500, "Michael Mattias" <mmattias@talsystems.com> wrote:
> 
…[24 more quoted lines elided]…
> They didn't ASK whether I wanted to do it. They said get it done or else.

And you willingly worked for this flunky outfit?

bill
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 9)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-01T19:48:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tdb7949ojs15gu3kt2j6sraimchhaerpou@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <b41ff8db-9fc2-4652-8b20-a103608884dc@k37g2000hsf.googlegroups.com> <sje2945ahjsv8fr7f82rcsfr06855g6amh@4ax.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com> <M5kkk.16863$mh5.2242@nlpi067.nbdc.sbc.com> <vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com> <6fguh4FbdddqU1@mid.individual.net>`

```
On 1 Aug 2008 17:13:08 GMT, billg999@cs.uofs.edu (Bill Gunshannon) wrote:

>In article <vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com>,
>	Robert <no@e.mail> writes:
…[28 more quoted lines elided]…
>And you willingly worked for this flunky outfit?

This "flunky outfit" was one of the world's largest and most profitable pharmaceutical
companies. 

This is THE NORM in Fortune 100 companies. If you can't stomach it, you won't last in the
contract programming business. Indians put up with it without complaint.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 10)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-08-02T07:18:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dgYkk.9067$vn7.6189@flpi147.ffdc.sbc.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <b41ff8db-9fc2-4652-8b20-a103608884dc@k37g2000hsf.googlegroups.com> <sje2945ahjsv8fr7f82rcsfr06855g6amh@4ax.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <fhc3949gck3o6sp2p7rlh7echnbe9opbkt@4ax.com> <M5kkk.16863$mh5.2242@nlpi067.nbdc.sbc.com> <vgk494tjukl2l71smc3qd2bsjg1kk2kqau@4ax.com> <6fguh4FbdddqU1@mid.individual.net> <tdb7949ojs15gu3kt2j6sraimchhaerpou@4ax.com>`

```
"Robert" <no@e.mail> wrote in message 
news:tdb7949ojs15gu3kt2j6sraimchhaerpou@4ax.com...
> This is THE NORM in Fortune 100 companies. If you can't stomach it, you 
> won't last in the
> contract programming business. Indians put up with it without complaint.

I guess I am just S-O-L, then.

Oh, well, I'm sure there must be *some* opportunities for those of us of 
European ethnicity.

MCM
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 5)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-31T07:19:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6b77cbd3-b3eb-40ce-957f-1a977d60944c@b38g2000prf.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <b41ff8db-9fc2-4652-8b20-a103608884dc@k37g2000hsf.googlegroups.com> <sje2945ahjsv8fr7f82rcsfr06855g6amh@4ax.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com>`

```
On 7月31日, 午後8:32, docdw...@panix.com () wrote:
> In article <effb0602-5b9b-44cc-a258-12880abe9...@q5g2000prf.googlegroups.com>,
>
…[19 more quoted lines elided]…
> DD

You got it. I'm a pure novice who just graduated from university last
year,especially compared to the ones who replied my post with decades
of experiences.
You can also evaluate me and my company as you wish. Even myself is
thinking about 2 things:
1.the organization is really stupid;
2.try to find another job.

BUT THAT'S ANOTHER QUESTION.

I just want to find a technical solution here and try to do as much as
I can. And I'm not posting with some silly questions or doing nothing
but waiting for answer.

You may guess I'm Chinese from my mail address. We have an old saying
"Do one's best and leave the rest to God's will".
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-07-31T14:48:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g6sjcn$eic$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <6b77cbd3-b3eb-40ce-957f-1a977d60944c@b38g2000prf.googlegroups.com>`

```
In article <6b77cbd3-b3eb-40ce-957f-1a977d60944c@b38g2000prf.googlegroups.com>,
 <taoxianfeng@gmail.com> wrote:
>On 7$B7n(B31$BF|(B, $B8a8e(B8:32, docdw...@panix.com () wrote:

[snip]

>> It seems that your knowledge of the tools required (COBOL and SQL) is
>> rather basic and the choice of solution is being dictated elsewhere.
…[6 more quoted lines elided]…
>of experiences.

I have a few years in this business, myself... and I believe that what you 
are doing is attempting to translate hexadecimal strings from an EBDCIC to 
an ASCII encoding scheme.

This has been done easily for simple text and most punctuation marks... 
but anything else can get really, *really* complex.

>You can also evaluate me and my company as you wish. Even myself is
>thinking about 2 things:
>1.the organization is really stupid;
>2.try to find another job.

In my experience:

1) All organisations say that their conditions are different than those of 
all other organisations; if all organisations are different then all 
organisations are the same.

2) There's always another job.

>
>BUT THAT'S ANOTHER QUESTION.
…[3 more quoted lines elided]…
>but waiting for answer.

I have no argument with that whatsoever.  If you've followed this group 
for any time you may have noticed my tendency to ask people who post 
questions and do not show any of the work they've done towards the 
solution 'Please do your own job/homework'.

I don't believe I've made that request of you and I'm not about to.

>
>You may guess I'm Chinese from my mail address.

Eh?  I thought you were Gmailian.

>We have an old saying
>"Do one's best and leave the rest to God's will".

Other sayings from other places include 'Trust in Allah... but tie up your 
camels' and 'The gods help those who help themselves' and 'Always cut the 
cards, count the change and don't sit with your back to the door'.

If your company believes that you are worthy of all this very expensive 
on-the-job training they are giving you... then who are you to object?  As 
my Sainted Mother - may she sleep with the angels! - used to say, 'What 
you carry between your ears is the hardest thing to take from you'.

DD
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 7)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-31T23:17:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b810ab23-4d45-4e40-8577-0b9ec1907dce@u12g2000prd.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <6b77cbd3-b3eb-40ce-957f-1a977d60944c@b38g2000prf.googlegroups.com> <g6sjcn$eic$1@reader1.panix.com>`

```
On 7月31日, 午後11:48, docdw...@panix.com () wrote:
> In article <6b77cbd3-b3eb-40ce-957f-1a977d609...@b38g2000prf.googlegroups.com>,
>
…[68 more quoted lines elided]…
> DD

You sound like a philosopher...but really hit me.
Shall we stop talking about sayings?
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-01T09:39:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g6ulkh$qhg$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <6b77cbd3-b3eb-40ce-957f-1a977d60944c@b38g2000prf.googlegroups.com> <g6sjcn$eic$1@reader1.panix.com> <b810ab23-4d45-4e40-8577-0b9ec1907dce@u12g2000prd.googlegroups.com>`

```
In article <b810ab23-4d45-4e40-8577-0b9ec1907dce@u12g2000prd.googlegroups.com>,
 <taoxianfeng@gmail.com> wrote:
>On 7$B7n(B31$BF|(B, $B8a8e(B11:48, docdw...@panix.com () wrote:

[snip]

>> If your company believes that you are worthy of all this very expensive
>> on-the-job training they are giving you... then who are you to object?  As
…[3 more quoted lines elided]…
>You sound like a philosopher...but really hit me.

Me?  I am just a COBOL-coding fool, that's all... perhaps I have read the 
backs of a few breakfast-cereal boxes.

>Shall we stop talking about sayings?

As soon as we stop running into situations that are described by them, 
sure... but 'there is nothing new under the sun' is an old saying, too.

DD
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-07-31T14:26:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nYjkk.344927$fz6.306514@fe08.news.easynews.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <b41ff8db-9fc2-4652-8b20-a103608884dc@k37g2000hsf.googlegroups.com> <sje2945ahjsv8fr7f82rcsfr06855g6amh@4ax.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com>`

```
Coming up with another approach entirely to the problem.  (I know Micro Focus 
better on Windows than AIX, so this MAY take more work on AIX than it would on 
Windows).

It seems to me that some (possibly most) of the problems come from the 
"download" process of the unloaded file being created as "line sequential".  My 
assumption is that on the mainframe it is a DCB=RECFM=VB (i.e. "variable length 
QSAM) file.  If so, then it may be worth looking into the Micro Focus "VRECGEN" 
facility.  Run some jobs (on the mainframe and the AIX environment), it might be 
possible to get a
  Record Sequential - Variable Length
file on AIX - with ALL the data "as it is on the mainframe".

I am NOT saying that this is the "best" solution (or the only solution), but it 
might be the easiest - if the "mandate" has come in that the file must be a DB2 
unloaded file from the mainframe that is downloaded to AIX and processed there 
as a file that is THEN loaded into an AIX table.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-07-31T15:08:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g6skh7$mev$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <nYjkk.344927$fz6.306514@fe08.news.easynews.com>`

```
In article <nYjkk.344927$fz6.306514@fe08.news.easynews.com>,
William M. Klein <wmklein@nospam.netcom.com> wrote:
>Coming up with another approach entirely to the problem.

If he's allowed to to that, Mr Klein, it would seem to make life Much 
Easier.

[snip]

>It seems to me that some (possibly most) of the problems come from the 
>"download" process of the unloaded file being created as "line sequential".

I believe - and my memory might be as porous as usual - that the 
difficulty is twofold: the data being unloaded on the mainframe contain 
Japanese characters and the files are being transferred with an 
EBCDIC-to-ASCII translation.  Off the top of my pointy little head I'd 
suggest the following test for a small sample, no more than 10,000 rows:

1) Mainframe side - use IKJEFT01 to execute SQL and SELECT the sample of 
rows to an FB output file.

2) Transfer the file to the ASCII platform *as binary*.

3) Set up a MicroFocus program to read the transferred file in EBCDIC and 
INSERT each record as a row into a table defined exactly as the mainframe 
one is defined... using a copy of the mainframe DCLGEN would make life 
much easier.

4) See what happens... get a 'smell' of the results and the time it takes 
to get them.  If it works the way I believe it will then one might begin 
to consider ways to speed the process up so that decent amounts of data 
might be handled... 60,000,000 rows and the like.

(A major, somewhat hidden, advantage to this test is that it uses methods 
that are unsophisticated; as such they run less of a chance of creating 
the 'I don't understand it so I won't let you do it' response.)

DD
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 7)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2008-07-31T17:44:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4891F9F1.6F0F.0085.0@efirstbank.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <nYjkk.344927$fz6.306514@fe08.news.easynews.com> <g6skh7$mev$1@reader1.panix.com>`

```
Might I also suggest to the original poster that you post this to the
comp.databases.ibm-db2 newsgroup?  I just can't see why a Cobol solution
should be required.  Since this is DB2 to DB2, there should be a DB2 only
resolution.

In my opinion, of course!

Frank
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 8)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-31T23:24:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<da536ace-0676-4684-9c52-33281b55ef75@v13g2000pro.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <nYjkk.344927$fz6.306514@fe08.news.easynews.com> <g6skh7$mev$1@reader1.panix.com> <4891F9F1.6F0F.0085.0@efirstbank.com>`

```
On 8月1日, 午前8:44, "Frank Swarbrick" <Frank.Swarbr...@efirstbank.com>
wrote:
> Might I also suggest to the original poster that you post this to the
> comp.databases.ibm-db2 newsgroup?  I just can't see why a Cobol solution
…[5 more quoted lines elided]…
> Frank

Well,that's a good idea since the essential result is some records are
deleted from DB.
It also reminds that's even possible to do it with some DB2 procedure.

I just need some time to put my mind in order and conclude your posts.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 9)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-31T23:54:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4d278e1a-c044-4fa9-83a6-6b231d00b555@f63g2000hsf.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <nYjkk.344927$fz6.306514@fe08.news.easynews.com> <g6skh7$mev$1@reader1.panix.com> <4891F9F1.6F0F.0085.0@efirstbank.com> <da536ace-0676-4684-9c52-33281b55ef75@v13g2000pro.googlegroups.com>`

```
OK GUYS, THE 100TH POST!

LET'S STOP DISCUSSING HERE ,SHALL WE?

PLEASE GIVE SOME TIME TO CONCLUDE YOUR POSTS, AND SOLVE SOME... NON
TECHNICAL PROBLEMS.

MAYBE I WILL TALK TO YOU LATER.

THANK YOU FOR ALL YOUR POSTS.

THANK YOU FOR YOUR KINDNESS.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-08-01T09:45:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g6ulus$9ph$1@reader1.panix.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <4891F9F1.6F0F.0085.0@efirstbank.com> <da536ace-0676-4684-9c52-33281b55ef75@v13g2000pro.googlegroups.com> <4d278e1a-c044-4fa9-83a6-6b231d00b555@f63g2000hsf.googlegroups.com>`

```
In article <4d278e1a-c044-4fa9-83a6-6b231d00b555@f63g2000hsf.googlegroups.com>,
 <taoxianfeng@gmail.com> wrote:
>OK GUYS, THE 100TH POST!

Ahhh, just getting started, then... but look, all caps!  It must be old 
mainframe source code!

>
>LET'S STOP DISCUSSING HERE ,SHALL WE?

If you want less discussion then stop asking such interesting questions.

>
>PLEASE GIVE SOME TIME TO CONCLUDE YOUR POSTS, AND SOLVE SOME... NON
>TECHNICAL PROBLEMS.

Is it in a good neighborhood?  How many miles has it been driven?  Does 
she come from a good family?

>
>MAYBE I WILL TALK TO YOU LATER.

Take your time... that which has value is rarely done instantly.

DD
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 9)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-08-01T07:48:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g91694hjktgin0eo141spmls6t3klrto8f@4ax.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <nYjkk.344927$fz6.306514@fe08.news.easynews.com> <g6skh7$mev$1@reader1.panix.com> <4891F9F1.6F0F.0085.0@efirstbank.com> <da536ace-0676-4684-9c52-33281b55ef75@v13g2000pro.googlegroups.com>`

```
On Thu, 31 Jul 2008 23:24:38 -0700 (PDT), taoxianfeng@gmail.com wrote:

>On 8ï¿½ï¿½1ï¿½ï¿½, ï¿½È«e8:44, "Frank Swarbrick" <Frank.Swarbr...@efirstbank.com>
>wrote:
…[13 more quoted lines elided]…
>I just need some time to put my mind in order and conclude your posts.

You need only a tool that can run SQL, such as SQLPlus or TOAD.

delete from a where customer_id not in (select customer_id from b);
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 6)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-31T23:12:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ef836e25-22ec-4aba-a68e-048e641ed0d4@v26g2000prm.googlegroups.com>`
- **References:** `<4890511A.6F0F.0085.0@efirstbank.com> <b41ff8db-9fc2-4652-8b20-a103608884dc@k37g2000hsf.googlegroups.com> <sje2945ahjsv8fr7f82rcsfr06855g6amh@4ax.com> <effb0602-5b9b-44cc-a258-12880abe9038@q5g2000prf.googlegroups.com> <g6s7sp$69d$1@reader1.panix.com> <nYjkk.344927$fz6.306514@fe08.news.easynews.com>`

```
On 7月31日, 午後11:26, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> Coming up with another approach entirely to the problem.  (I know Micro Focus
> better on Windows than AIX, so this MAY take more work on AIX than it would on
…[18 more quoted lines elided]…
>  wmklein <at> ix.netcom.com

VRECGEN is the supplied on Microfocus mainframe and Net Express...at
least as I searched.
And the original system is IBM Z/OS running IBM cobol.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
