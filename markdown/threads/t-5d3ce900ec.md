[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Platform Independence (was: LE Runtime or COBOL Intrinsic? That is the Question.)

_9 messages · 6 participants · 1999-09_

---

### Re: Platform Independence (was: LE Runtime or COBOL Intrinsic? That is the Question.)

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37EF53C9.AE8B9DAB@zip.com.au>`
- **References:** `<7sdh88$ade$1@nnrp1.deja.com> <37ed9a4e@eeyore.callnetuk.com> <37EEB74C.46301887@att.net>`

```
William Lynch wrote:
> 
> peter dashwood wrote:
…[20 more quoted lines elided]…
> Bill Lynch

I will stand with a foot in both camps.

Where possible use the simplest portable constructs to perform the
function at hand.  For efficiency do use specific constructs where
they are necessary.  What is efficiency - run time and programmer
time.

The logic is simple keeping the capacity to move in the code costs
little in most cases.  The trick is to know what works and what does
not you really need a couple of compilers (PC and MVS for example) to
guarantee it, if you are testing with a PC this is not a great problem
though.

There is a cost to doing this cross platform stuff (I am doing a PC,
Unix, MVS solution now and it is 'fun').  This cost should not be
added to the project just because the programmer wants to do it. 
There must be a justification for it.

There you go just toss a coin and you have my opinion,
Ken
```

#### ↳ Re: Platform Independence (was: LE Runtime or COBOL Intrinsic? That is the Question.)

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37EFE945.D7009CD2@home.com>`
- **References:** `<7sdh88$ade$1@nnrp1.deja.com> <37ed9a4e@eeyore.callnetuk.com> <37EEB74C.46301887@att.net> <37EF53C9.AE8B9DAB@zip.com.au>`

```
Ken Foskey wrote:
> 
> William Lynch wrote:
…[43 more quoted lines elided]…
> Ken

Well, Ken has put his one cent in, (stingy bastards these Aussies). Pete
- are you just as thrifty on the two little islands SE of him ? 
(Still, I bet you haven't yet bought Stephen Gennard that pint you
promised him back on Compuserve - remember ? Anybody checking in from
Newbury - confirm with Stephen).

Was going to cover this from what you had written to me privately, but
as you have introduced the topic here, I'll also query here.

I agree with your comments about Platform Independence, and the other
comment you got, though probably not meant that way, did sound like
"Big-iron versus small-iron". You and I go back to Noah's time, me doing
the political bit talking to the users, and at least initially, you
'talking' to the machine. So it makes sense that you have built up a
considerable repertoire of coding routines over the years which can be
transferred to different compilers.

I know that both you and Thane have done the switcheroo from M/F to
Fujitsu - and though Bill Klein believes, probably also applies to a lot
of the current Merant clan, (if I read him right), that the cheap price
for Visoc was its downfall - admit it, both you and Thane were largely
influenced by the price for Fujitsu, and at the time Visoc was issued it
lacked Dialog System that you had both been using in the DOS version.

Correct me as necessary, but the only common elements that transfer from
COBOL to COBOL are syntax, COBOL file-handling and SCREEN SECTION. When
it comes to your statements about not using compiler specific stuff:-

- what alternatives do you offer me for the CBL_FILE routines if I
transfer from M/F - I use them extensively

- Logically, I shouldn't use N/E OO and GUI classes because they aren't
transferable. (Sorry, I haven't got the bucks to go out and buy a Big
Blue Mainframe to find out what OO is about).

- Thane is using SP2 but you are using Fujitsu routines - I doubt what
you are using is transferable.

- I note your enthusiasm for going data base as opposed to conventional
file handling. I really can't get a handle on this one. I tried to raise
the topic back in Compuserve days - and the only taker was Pat
Magee(Merant) who strongly supported SQL as a language and file system.
Similarly here, raised it as a topic again. Naturally our good friend
Warren Simmonds jumped in, (why not, he was on the original DB committee
back when....). The only other taker here was Thane Hubbell - he was
doing things in COBOL but could think of an instance where it might have
been better using DB. Also, interesting, Thane said it was SLOW - his
emphasis, not mine. Nobody jumped in to refute Thane's comment on speed.
So to scratch a few ticks, and get it started again, what gives with
this DB approach as being better than COBOL data files ? (I can think of
an obvious one, the DB approach makes it easier to work with other
languages). Re other languages, I recall you were 'underwhelmed' with
JAVA.

(Just a rider about DB - I recall Warren mentioning it was very
effective in a parts explosion type of application - but in effect I
achieved the same using RM/COBOL data-files on a Radio Shack Model 16 +
Xenix. Agricultural chemicals/liquids - they had two basic 'soups' to
which you added other ingredients - from the input recipe and
quantities/volumes, and the finished packaging,  I gave them the
manufacturing cost per unit)

Not disputing what you say, just trying to get a handle on it, and
hopefully it will cause others to jump in on merits/demerits of doing it
in various ways - and exactly what is transferable for platform
independence.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Platform Independence (was: LE Runtime or COBOL Intrinsic? That is the Question.)

- **From:** paulr@delphi.com
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37f153bf$1$cnhye$mr2ice@news.stonemedia.com>`
- **References:** `<7sdh88$ade$1@nnrp1.deja.com> <37ed9a4e@eeyore.callnetuk.com> <37EEB74C.46301887@att.net> <37EF53C9.AE8B9DAB@zip.com.au> <37EFE945.D7009CD2@home.com>`

```
In <37EFE945.D7009CD2@home.com>, on 09/27/99 
   at 09:53 PM, "James J. Gavan" <jjgavan@home.com> said:

Note that with a DB you can do things in COBOL that are 
deucedly difficult otherwise. For example,  combining the inputs from
say, 6 or 7 tables (files), selecting just the fields you are 
interested in is not difficult in DB2. In fact, it is one call.  Doing
the same with 6 or 7 VSAM files (or ISAM or whatever  native file system
you are use) is much more difficult. 

Along those same lines, a well optimized database, 
along with a well optimized hunk of SQL can usually outperform COBOL
file performance for searching and sorting and
certainly on joining. The big secret is to use static SQL,  and that
applies to just about ever DBMS that I am familiar  with. It certainly
applies to DB2. 

You get some other benefits too, though you don't often see those on PC
platforms. Scalability is the #1 benefit that comes to my mind. Client
server follows quickly, and limited transactional  capabilty WITHOUT a
third party transaction manager. DB2
and Oracle often provide all the transaction management needed within
some organizaitons. Of course, they work exceedingly well with CICS too,
albeit with some limitations. 

The COBOL coding is about the same level of complexity as
coding a base call to a VSAM file, requiring about the same amount of
setup. Compile time is a little longer though. 

Yours,
-Paul

[ Lots of good stuff clipped... ]
>- I note your enthusiasm for going data base as opposed to conventional
>file handling. I really can't get a handle on this one. I tried to
…[12 more quoted lines elided]…
>'underwhelmed' with JAVA.

>(Just a rider about DB - I recall Warren mentioning it was very
>effective in a parts explosion type of application - but in effect I
…[4 more quoted lines elided]…
>manufacturing cost per unit)


>Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Platform Independence (was: LE Runtime or COBOL Intrinsic? That is the Question.)

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F18D6A.AC3836DA@home.com>`
- **References:** `<7sdh88$ade$1@nnrp1.deja.com> <37ed9a4e@eeyore.callnetuk.com> <37EEB74C.46301887@att.net> <37EF53C9.AE8B9DAB@zip.com.au> <37EFE945.D7009CD2@home.com> <37f153bf$1$cnhye$mr2ice@news.stonemedia.com>`

```
paulr@delphi.com wrote:
> 
> In <37EFE945.D7009CD2@home.com>, on 09/27/99
…[5 more quoted lines elided]…
> interested in is not difficult in DB2.
<SNIP> plentyh of good stuff......

Thanks Paul - that's the sort of feedback I've been looking for quite a
while - bearing in mind this Joe Blow is sat at home doing his thing in
splendid isolation. Would you care to comment on Thane's "but it is
SLOW".

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Platform Independence (was: LE Runtime or COBOL Intrinsic? That is the Question.)

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F0C5CA.70707E6@zip.com.au>`
- **References:** `<7sdh88$ade$1@nnrp1.deja.com> <37ed9a4e@eeyore.callnetuk.com> <37EEB74C.46301887@att.net> <37EF53C9.AE8B9DAB@zip.com.au> <37EFE945.D7009CD2@home.com>`

```
"James J. Gavan" wrote:

> - Logically, I shouldn't use N/E OO and GUI classes because they
> aren't transferable. (Sorry, I haven't got the bucks to go out and buy
> a Big Blue Mainframe to find out what OO is about).

Sorry Jimmy but I have not got the GUI screen to work on a 3270
terminal yet so we will hold off on this one for a while.  :-}

> Similarly here, raised it as a topic again. Naturally our good friend
> Warren Simmonds jumped in, (why not, he was on the original DB 

You picked one of the LEAST portable of all.

When is a standard not a a standard, when it is SQL.  Each vendor
gives close but different results to SQL. How do you really optimise
Oracle SQL and how do you really optimise DB2 SQL there are subtle
differences.

How do you hook the database for Server X.  Some use an interface
routine, some use a pre-processor.   To my knowledge none actually
work using SQL implementations for another vendor.

If you write for server X (DB2 or oracle) you can get platform
independence.   Servers are great, you do not have to concern yourself
with file locking, you can process data 'sets' consolidating totals
and simplify your programming logic.

How much does this cost, traditional estimates place these costs at
about 10% overhead.

I really like databases they make my life easier,
Ken
```

###### ↳ ↳ ↳ Re: Platform Independence (was: LE Runtime or COBOL Intrinsic? That is the Question.)

- **From:** "peter dashwood" <dashwood@freewebaccess.co.uk>
- **Date:** 1999-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37f175c9@eeyore.callnetuk.com>`
- **References:** `<7sdh88$ade$1@nnrp1.deja.com> <37ed9a4e@eeyore.callnetuk.com> <37EEB74C.46301887@att.net> <37EF53C9.AE8B9DAB@zip.com.au> <37EFE945.D7009CD2@home.com> <37F0C5CA.70707E6@zip.com.au>`

```
What the Hell is this all about?!

When did a discussion on LE Runtime or COBOL intrinsic functions become a
garbled conversation on platform independence? Are you guys running another
server somewhere?

My system shows 4 messages in this thread since (and including) the message
by Bill Thompson on the 23rd, responded to by Bill Klein on the 23rd, and me
on the 26th. Now this message from Ken pops up dated the 28th, referring to
a message by Jimmy, which I cannot find anywhere in the Newsgroup, certainly
not in this thread.

What's going on? Are there different versions of comp.lang.cobol? Maybe my
ISP is not relaying it correctly...Any ideas?

Anyway, my comments to Ken are interspersed below. I'd like to have read the
full context, particularly Jimmy's posting...

Ken Foskey wrote in message <37F0C5CA.70707E6@zip.com.au>...
>"James J. Gavan" wrote:
>
…[15 more quoted lines elided]…
>differences.

The SQL standard is becoming ever more stable. It is NOT true as a sweeping
statement that "Each Vendor gives close but different results to SQL". It IS
true that SOME constructs and clauses vary by implementation.

How do you optimise ORACLE or DB2? You don't. (Not unless you are having
serious performance problems).

The problem is that in order to "optimise" you MUST use vendor-specific
clauses (we are not talking untrained user ignorance here, searching across
multiple keys that are not indexed, and all the other "silly" things users
do because the system says they can, etc.). It's no accident. The vendors
planned it that way. To lock you into their platform, just as vendors have
been doing with programming languages and DB access methods since commercial
computers became available. If you fall for it and start coding platform
specific SQL you can hear them shouting "Sucker!" all the way to the Bank.

The best compromise I've found so far is to use ODBC, write standard SQL,
and tell the vendor if it doesn't perform you'll move the lot to another
platform...you'd be amazed at how this gets their attention.

We write everything in standard embedded SQL in COBOL, for ODBC to
(initially) MS-ACCESS . We test and debug using ACCESS. We even implement
for smaller companies using ACCESS. THEN we port to ORACLE, INGRES, DB2,
UDB, or DATACOM. So far we never had a problem Excellent ODBC drivers are
available for all of the above and they allow cross platform, enterprise
wide data access.

In fact, it is so platform independent that I use an online, mainframe DB2
reference, as a quick lookup to obtain SQL statement formats, when I'm not
sure, or senility gets the better of me.... It seems to work for all of the
mentioned platforms, as long as I DON'T do anything DB2 specific. Yes, I
have MS-ACCESS SQL reference and I also have DELPHI's Borland Database SQL
reference, but I like the simplicity of the DB2 one from LEGENT.

We need to look ahead and future-proof our systems as much as possible.
Standard SQL and platform independence is the best way to do this.

>
>How do you hook the database for Server X.  Some use an interface
…[6 more quoted lines elided]…
>and simplify your programming logic.

Amen to that!


>
>How much does this cost, traditional estimates place these costs at
>about 10% overhead.

>
>I really like databases they make my life easier,

Me too Ken. And it's just as well. I believe within 10 years they will be
the ONLY data repositories available to us. (Of course, by then, standard
SQL will actually be a standard...<G>)

Pete.
```

###### ↳ ↳ ↳ Re: Platform Independence (was: LE Runtime or COBOL Intrinsic? That is the Question.)

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F194A5.AEC72099@home.com>`
- **References:** `<7sdh88$ade$1@nnrp1.deja.com> <37ed9a4e@eeyore.callnetuk.com> <37EEB74C.46301887@att.net> <37EF53C9.AE8B9DAB@zip.com.au> <37EFE945.D7009CD2@home.com> <37F0C5CA.70707E6@zip.com.au> <37f175c9@eeyore.callnetuk.com>`

```
peter dashwood wrote:
> 
> What the Hell is this all about?!
…[3 more quoted lines elided]…
> server somewhere?

I ROARED WITH LAUGHTER at your message - what makes you so damn
different? Let me spell a similar situation out to you :-

	1. Ray Leach writes to me about N/E
	2. Thane Hubbell replies to Ray
	3. Then I jump in and say 'What the Hell's going on'.
	   Based on Thane's message I reply to Ray
	4. I NEVER did see Ray's initial message # 1 

There are instances where I have replied to messages here before my copy
of the originator's message gets to me direct. I suppose the 'Net is
packaging it into 'delivery modules' ???

Want a scapegoat - call him Bill - no honest Bill, I'm kidding. Chances
are you will NEVER get my initial message, so I'll copy and send it to
you direct, (promise) - then you can reply through here on anything you
aren't currently covering.

Of course we've got separate NewsGroups, one for N.America, one for UK,
and that probably excludes people living in the Norfolk Broads. (AND -
BEFORE Michael or one of the others adds a quip 'Broads' is a
geographical location not somebody you say to "Voulez vous couchez avec
moi ce soir s'il vous plait ?")

Behind all that hurrumphh - you gotta be smiling mon Pierre <G> ?

Jimmy
```

###### ↳ ↳ ↳ Re: Platform Independence (was: LE Runtime or COBOL Intrinsic? That is the Question.)

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0noI3.99$ZV1.3778@dfiatx1-snr1.gtei.net>`
- **References:** `<7sdh88$ade$1@nnrp1.deja.com> <37ed9a4e@eeyore.callnetuk.com> <37EEB74C.46301887@att.net> <37EF53C9.AE8B9DAB@zip.com.au> <37EFE945.D7009CD2@home.com> <37F0C5CA.70707E6@zip.com.au> <37f175c9@eeyore.callnetuk.com> <37F194A5.AEC72099@home.com>`

```

>Of course we've got separate NewsGroups, one for N.America, one for UK,
>and that probably excludes people living in the Norfolk Broads. (AND -
…[3 more quoted lines elided]…
>


I thought the Norfolk Broads was the Virginia team in the new Women's
National Basketball Association.

MCM
```

###### ↳ ↳ ↳ Re: Platform Independence (was: LE Runtime or COBOL Intrinsic? That is the Question.)

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7suc6p$j12$4@news.igs.net>`
- **References:** `<7sdh88$ade$1@nnrp1.deja.com> <37ed9a4e@eeyore.callnetuk.com> <37EEB74C.46301887@att.net> <37EF53C9.AE8B9DAB@zip.com.au> <37EFE945.D7009CD2@home.com> <37F0C5CA.70707E6@zip.com.au> <37f175c9@eeyore.callnetuk.com> <37F194A5.AEC72099@home.com> <0noI3.99$ZV1.3778@dfiatx1-snr1.gtei.net>`

```

Michael Mattias wrote in message
<0noI3.99$ZV1.3778@dfiatx1-snr1.gtei.net>...
>
>>Of course we've got separate NewsGroups, one for N.America, one for UK,
…[10 more quoted lines elided]…
>MCM


Those the ones in the song?

The girls of Norfolk
Don't drink nor smoke,
Norfolk, Norfolk ...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
