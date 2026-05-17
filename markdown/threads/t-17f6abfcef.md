[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help on a Password Program

_12 messages · 12 participants · 1998-04 → 1998-05_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help on a Password Program

- **From:** "tj..." <ua-author-2348699@usenetarchives.gap>
- **Date:** 1998-04-20T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<353c23fe.58056366@news.mindspring.com>`

```

I am having a problem, I am working on a order entry program that has
a security enterance. I have the Password program working, but the
problem is the ID-Password file is a table. Now with a table you have


PASSWORD-TABLE OCCURS 15 TIMES

with the occurs being a fixed number I will not be able to add users
later on with out updating the program code. How do I get around
this? Any other way of doing this besides using a table?

Thanks ahead of time for any info.
```

#### ↳ Re: Help on a Password Program

- **From:** "mark0..." <ua-author-750539@usenetarchives.gap>
- **Date:** 1998-04-20T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-17f6abfcef-p2@usenetarchives.gap>`
- **In-Reply-To:** `<353c23fe.58056366@news.mindspring.com>`
- **References:** `<353c23fe.58056366@news.mindspring.com>`

```

In article <353··.@new··g.com>, tj··.@min··g.com
writes:

› I have the Password program working, but the
› problem is the ID-Password file is a table.

There are several possible approaches:

1. Allocate a large table (e.g., 100 occurrances if you are now dealing with
just 15) so that when you read the file of passwords, you would load just the
entries you need. You would also need to do something to prevent searching
beyond the last entry loaded (e.g., ... OCCURS 100 DEPENDING UPON
NUM-ENTRIES-LOADED, where NUM-ENTRIES-LOADED is someplace else in
WORKING-STORAGE, or load unused entries with HIGH-VALUES, either of these would
allow one to use SEARCH ALL to have COBOL do a binary search).

2. Make the file an indexed file (on mainframe, a VSAM KSDS or equivalent) with
the user-id being part of the key into the file. We use this method at work for
our CICS applications: the user-id and program-id are used together as the key
into our security file and the switches on the returned record identify what
the user can do in that application. (No record = the user cannot run that
application at all.) The advantage is that the program is not limited to any
arbitrary number of users or applications. The disadvantage is that an I/O is
required each time a user goes into a different application.

Mark A. Young
```

#### ↳ Re: Help on a Password Program

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-04-20T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-17f6abfcef-p3@usenetarchives.gap>`
- **In-Reply-To:** `<353c23fe.58056366@news.mindspring.com>`
- **References:** `<353c23fe.58056366@news.mindspring.com>`

```
The easiest way is to put the passwords into an
ISAM file,
and use the password as a key, either with or
without
duplicates. If it is a full COBOL system, then
there is
probably some sort of "PERSON" file indexed by a
customer
number or customer key as the primary key.

In the real world, there would be, anyway. Program
assignments
tend to be problematic that way.








The easiest way is to put the passwords into an
ISAM file,
and use the password as a key, either with or
without
duplicates.Â  If it is a full COBOL system,
then there is
probably some sort of "PERSON"; file
indexed by a customer
number or customer key as the primary
key.
Â 
In the real world, there would be, anyway.
Program assignments
tend to be problematic that way.
Â
```

#### ↳ Re: Help on a Password Program

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-04-20T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-17f6abfcef-p4@usenetarchives.gap>`
- **In-Reply-To:** `<353c23fe.58056366@news.mindspring.com>`
- **References:** `<353c23fe.58056366@news.mindspring.com>`

```

tj··.@min··g.com wrote:
› 
› I am having a problem, I am working on a order entry program that has
…[9 more quoted lines elided]…
› Thanks ahead of time for any info.

Hmmmmm... a password program limited to 15 users? Smells like homework,
to me... please do your own homework.

DD
```

##### ↳ ↳ Re: Help on a Password Program

- **From:** "css..." <ua-author-6589296@usenetarchives.gap>
- **Date:** 1998-04-20T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-17f6abfcef-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-17f6abfcef-p4@usenetarchives.gap>`
- **References:** `<353c23fe.58056366@news.mindspring.com> <gap-17f6abfcef-p4@usenetarchives.gap>`

```

Homework RTFM :-|

The Goobers (doc··.@er··s.com) wrote:
: tj··.@min··g.com wrote:
: >
: > I am having a problem, I am working on a order entry program that has
: > a security enterance. I have the Password program working, but the
: > problem is the ID-Password file is a table. Now with a table you have
: >
: > PASSWORD-TABLE OCCURS 15 TIMES
: >
: > with the occurs being a fixed number I will not be able to add users
: > later on with out updating the program code. How do I get around
: > this? Any other way of doing this besides using a table?
: >
: > Thanks ahead of time for any info.

: Hmmmmm... a password program limited to 15 users? Smells like homework,
: to me... please do your own homework.

: DD
```

##### ↳ ↳ Re: Help on a Password Program

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-04-23T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-17f6abfcef-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-17f6abfcef-p4@usenetarchives.gap>`
- **References:** `<353c23fe.58056366@news.mindspring.com> <gap-17f6abfcef-p4@usenetarchives.gap>`

```

The Goobers wrote:
› 
› tj··.@min··g.com wrote:
…[16 more quoted lines elided]…
› DD

He's concerned about getting past this limit, he's concerned about
future maintainability. Sounds like not homework to me. If it is
homework, that's a very good teacher to come up with a project like
this. In school, the only maintenance assignment was to modify the
program I just wrote. But the teacher told us the specs for the
modification before we wrote the original program.

I  |\   Randall Bart
L  |/   mailto:Bar··.@usa··m.net    Bar··.@wor··m.net
o  |\   1-310-542-6013                       Please reply without spam
v  | \      Todd McCormick released after 12 day illegal incarceration
e    |\ for using Marinol w/ prescription: http://www.freecannabis.org
Y    |/     http://www.marijuanamagazine.com/toc/articles/toddfree.htm
o    |\ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00  
u    |/ Is it easy yet?:http://members.aol.com/PanicYr00/Sequence.html
```

###### ↳ ↳ ↳ Re: Help on a Password Program

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-04-26T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-17f6abfcef-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-17f6abfcef-p6@usenetarchives.gap>`
- **References:** `<353c23fe.58056366@news.mindspring.com> <gap-17f6abfcef-p4@usenetarchives.gap> <gap-17f6abfcef-p6@usenetarchives.gap>`

```

In article <6hrlg0$j.··.@bgt··t.net>,
RandallBart wrote:
› The Goobers wrote:
›› 
…[20 more quoted lines elided]…
› future maintainability.  Sounds like not homework to me.

A point... now, a counter-point; getting past the limit/maintainability
also speak of an instructor who is building on previous assignments... a
moderately common practise.

› If it is
› homework, that's a very good teacher to come up with a project like
› this.

Goo dinstructors exist, aye... just as do students who ask others to do
their homework.

› In school, the only maintenance assignment was to modify the
› program I just wrote.
 
› ... as I mentioned above, building on a previous assignment.
 
› But the teacher told us the specs for the
› modification before we wrote the original program.

That's how that instructor did it, sure... but, truth be known, my
original evaluation was based on the imprecise 'science' of olfaction...
it 'smelled' like homework. Call me narrow-minded and suspicious but any
time I see what is obviously a rank amateur asking questions about things
like password systems my immediate response is not 'Oh, look... a major
brokerage firm/bank/manufacturer is entrusting the
coding/maintaining/upgrading of their User Secutiry System to someone who
has this level of skill and has to ask about it on the UseNet'... it is
more along the lines of 'do your own homework, please'.

... that and the fact that a password program seems to be a regular
feature in some books; I recall seeing similar questions coming from folks
who seemed to have similar (i.e., minimal) experience here previously...
but I'm just narrow-minded and suspicious, remember?

DD
```

##### ↳ ↳ Re: Help on a Password Program

- **From:** "allsoft technologies limied" <ua-author-17074697@usenetarchives.gap>
- **Date:** 1998-04-29T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-17f6abfcef-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-17f6abfcef-p4@usenetarchives.gap>`
- **References:** `<353c23fe.58056366@news.mindspring.com> <gap-17f6abfcef-p4@usenetarchives.gap>`

```

pUT THEM INDIVIDUALLY IN AN INDEXED FILE - NO LIMIT!

The Goobers wrote:
› 
› tj··.@min··g.com wrote:
…[16 more quoted lines elided]…
› DD
```

#### ↳ Re: Help on a Password Program

- **From:** "joseph lenz" <ua-author-17071704@usenetarchives.gap>
- **Date:** 1998-04-20T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-17f6abfcef-p9@usenetarchives.gap>`
- **In-Reply-To:** `<353c23fe.58056366@news.mindspring.com>`
- **References:** `<353c23fe.58056366@news.mindspring.com>`

```

› Any other way of doing this besides using a table?
›
› Thanks ahead of time for any info.

perhaps use a file
```

#### ↳ Re: Help on a Password Program

- **From:** "kalpataru barman" <ua-author-17071492@usenetarchives.gap>
- **Date:** 1998-04-21T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-17f6abfcef-p10@usenetarchives.gap>`
- **In-Reply-To:** `<353c23fe.58056366@news.mindspring.com>`
- **References:** `<353c23fe.58056366@news.mindspring.com>`

```

Try OCCURS DEPENDING ON

Format :

PASSWORD-TABLE OCCURS 1 TO 30 TIMES DEPENDING ON WS-NUM-USERS



tj··.@min··g.com wrote:

› I am having a problem, I am working on a order entry program that has
› a security enterance.  I have the Password program working, but the
…[8 more quoted lines elided]…
› Thanks ahead of time for any info.
```

#### ↳ Re: Help on a Password Program

- **From:** "pdu..." <ua-author-1262469@usenetarchives.gap>
- **Date:** 1998-04-28T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-17f6abfcef-p11@usenetarchives.gap>`
- **In-Reply-To:** `<353c23fe.58056366@news.mindspring.com>`
- **References:** `<353c23fe.58056366@news.mindspring.com>`

```

Why not use an indexed file with the password being the key? If you
got fancy, you could even limit acces for a user to specific menu
selections.

MicroFocus indexed files can even be encrypted, I think.

Paul

tj··.@min··g.com wrote:

› I am having a problem, I am working on a order entry program that has
› a security enterance.  I have the Password program working, but the
…[9 more quoted lines elided]…
› Thanks ahead of time for any info.
```

##### ↳ ↳ Re: Help on a Password Program

- **From:** "irene jacobsen" <ua-author-17074419@usenetarchives.gap>
- **Date:** 1998-05-04T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-17f6abfcef-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-17f6abfcef-p11@usenetarchives.gap>`
- **References:** `<353c23fe.58056366@news.mindspring.com> <gap-17f6abfcef-p11@usenetarchives.gap>`

```

› tj··.@min··g.com wrote:
› 
…[10 more quoted lines elided]…
›› Thanks ahead of time for any info.

Any file with a record definition equal to the records in your password
table would get you around the problem. But: anyway, if this is to be a
secure system, either the file (or table) must be scrambled with a key only
known by the program, or you must be able to save it on a place unreachable
for the users trying to get into the "holy parts" of your program....

Irene Jacobsen.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
