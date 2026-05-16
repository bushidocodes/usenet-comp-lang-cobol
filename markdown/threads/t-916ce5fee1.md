[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL and DB2 vs. Java and DB2

_102 messages · 18 participants · 2007-09 → 2008-01_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### COBOL and DB2 vs. Java and DB2

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-09-15T21:11:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13ep0krm3102m43@corp.supernews.com>`

```
At work they have done some testing (I have no access to the details) and 
they claim Java and DB2 are faster than COBOL and DB2.  They also claim that 
changing the existing COBOL programs to work with DB2 would require 99% of 
the code to be rewitten.  I strongly doubt it, but I have had no experience 
with DB2 although I think I have a good understanding of embedded SQL. They 
want to modernize the systems, i.e. get rid of COBOL, so I believe there is 
a built in bias and a distinct lack of interest in any measurements or facts 
that would contradict their view.  I would be interested in hearing from 
anyone that has had experience with this kind of conversion/rewrite.

What I find particularly interesting in this regard is that the 
specifications for the new system say 95% of the transactions must be 
processed in 30 seconds, and 99% of the transactions must be processed in 60 
seconds. Wow! To say I am underwhelmed is a gross understatement! Currently 
using COBOL and Datacomm/DB we process transactions in less than one second. 
This is from the time the transaction (a message) is removed from the queue 
(MQSeries is used) until the time when the reply is placed onto the outbound 
queue.  If this is modernization then I just don't see the point especially 
when it is costing 300+ million a year.  Or many making money is the point!
```

#### ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-09-16T02:00:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13ephmg3ool7nbb@corp.supernews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message
news:13ep0krm3102m43@corp.supernews.com...
> At work they have done some testing (I have no access to the details) and
> they claim Java and DB2 are faster than COBOL and DB2.  They also claim
that
> changing the existing COBOL programs to work with DB2 would require 99% of
> the code to be rewitten.  I strongly doubt it, but I have had no
experience
> with DB2 although I think I have a good understanding of embedded SQL.
They
> want to modernize the systems, i.e. get rid of COBOL, so I believe there
is
> a built in bias and a distinct lack of interest in any measurements or
facts
> that would contradict their view.  I would be interested in hearing from
> anyone that has had experience with this kind of conversion/rewrite.
…[3 more quoted lines elided]…
> processed in 30 seconds, and 99% of the transactions must be processed in
60
> seconds. Wow! To say I am underwhelmed is a gross understatement!
Currently
> using COBOL and Datacomm/DB we process transactions in less than one
second.
> This is from the time the transaction (a message) is removed from the
queue
> (MQSeries is used) until the time when the reply is placed onto the
outbound
> queue.  If this is modernization then I just don't see the point
especially
> when it is costing 300+ million a year.  Or many making money is the
point!

I have do not have the experience you requested; but
a search using Google with: performance cobol java,
provided some interesting information.

<
http://expertanswercenter.techtarget.com/eac/blog/0,295203,sid63_tax301393,0
0.html >
-----
15 MAR 2005

My IBM COBOL customers often tell me that even IBM is trying to
convince them to use Java on z/OS (the OS for IBM mainframes)
even though they have thousands of programs already written and
running in COBOL and hundreds of COBOL programmers on staff.
One customer even wrote some benchmark performance tests,
recreating some COBOL code as Java classes. The performance
numbers were stunning: Java was up to 30 times slower than
COBOL! Now, you have to understand that this is code doing what
COBOL does best: reading and writing files and processing dollars
and cents data. But the best example they had of Java code was
still 20 times slower than COBOL. So, if performance was
important then the choice was made before they even started!
-----

<
http://www-306.ibm.com/software/data/ims/presentations/four/javaperformance/
javaperformance.htm >
-----
Our experiments also showed the transaction pathlength (number
of instructions per transaction) increased by 2.6X when the
application was converted from COBOL to Java.
-----

<
http://www.ibm.com/software/htp/cics/library/whitepapers/Java_CICS_TS2_PSSC_
app_perform_technical.pdf >

This paper, from 2002, might have proved interesting since it
used CICS and DB2, the difference being Java versus COBOL;
but the IBM Partner who was conducting the test decided to
drop the COBOL part of the test.

The bottom line is that IBM's research using Java with IMS
versus COBOL with IMS showed that Java required more
instructions per transaction. This should mean that, all else
being equal, Java is slower than COBOL.

And, there have been undocumented reports that Java is slower
than COBOL when Java is used to do the same as COBOL.

And, I saw nothing, in my search, to suggest the reverse
might be true.
```

##### ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** Louis Krupp <lkrupp@pssw.nospam.com.invalid>
- **Date:** 2007-09-16T00:21:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13epir4iasqqjea@corp.supernews.com>`
- **In-Reply-To:** `<13ephmg3ool7nbb@corp.supernews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <13ephmg3ool7nbb@corp.supernews.com>`

```
Rick Smith wrote:
<snip>
> 15 MAR 2005
> 
…[11 more quoted lines elided]…
> important then the choice was made before they even started!

Could IBM be trying to sell more hardware by recommending slower software?

Louis
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-09-16T09:01:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jHaHi.95112$jH3.3966@bignews6.bellsouth.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <13ephmg3ool7nbb@corp.supernews.com> <13epir4iasqqjea@corp.supernews.com>`

```
"Louis Krupp" <lkrupp@pssw.nospam.com.invalid> wrote:
>
> Could IBM be trying to sell more hardware by recommending slower
> software?

If they thought of it, and believed they could get away with it, they would
definitely do it, you can be sure of that.
```

#### ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-16T06:15:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hS3Hi.219830$i91.54123@fe01.news.easynews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com>`

```
Although I question the testing that claimed that "in general" JAVA/DB2 was 
faster than COBOL/DB2, there may be an issue for IBM z/OS sites as to whether or 
not they have either zIIP or zAAP installed (or available).  I am QUITE ignorant 
on these, but do know they work for DB2 and "new workloads" (i.e. allowed for 
Java - not for COBOL).

You might want to verify what release of COBOL, z/OS, and DB2 is available and 
whether zIIP or zAAP (or both) are available.

If you want to email me privately, I could pass on your question to someone in 
IBM.  I don't know if I would get an "official" answer, but I might be able to 
find someone who could at least point you to the right place to look or send 
your questions.

P.S.  As far as how much code needs to be "rewritten" if moving from COBOL 
non-DB2 to DB2, that would depend upon how much of your existing code is already 
working for the user-interface that you want (or whether there will be a totally 
new interface) *and* how much of your application code is spent in 
"file/database-I/O" vs "business logic".

For example, if the application today is a CICS 3270 application using VSAM for 
file I/O - and you were planning on moving it to a web-based GUI with DB2, then 
I would agree that LOTS of the application would need rewriting.  (However, even 
in such cases the "back-end" code would probably require minimal changes to 
convert from VSAM to DB2.  Certainly CHANGES WOULD BE REQUIRED - but "only" the 
I/O portions <maybe>)
```

##### ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-09-16T10:43:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13eqg7lib5vsvce@corp.supernews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <hS3Hi.219830$i91.54123@fe01.news.easynews.com>`

```
Comments interspersed below.

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:hS3Hi.219830$i91.54123@fe01.news.easynews.com...
> Although I question the testing that claimed that "in general" JAVA/DB2 
> was faster than COBOL/DB2, there may be an issue for IBM z/OS sites as to 
…[6 more quoted lines elided]…
>

It is the latested release of COBOL and DB2. I know they have plenty of 
money but I am not informed on zIIP or zAAP usage.


> If you want to email me privately, I could pass on your question to 
> someone in IBM.  I don't know if I would get an "official" answer, but I 
> might be able to find someone who could at least point you to the right 
> place to look or send your questions.
>

I am a telecommuter and as such I have been largely kept out of the current 
process and I have little first hand information on what is going on.  I 
tried to attend some meeeting via teleconference but it is difficult when 
they don't tell you when the meetings are held and when the documents being 
referred to are supposed to be available on the LAN but in fact are the 
wrong documents. There is a consortium of contractors developing the new 
system and IBM is one of the leaders so I am sure contacting IBM about this 
would be politically incorrect even as my original post probably was. I tend 
to not say much especially to higher up managers so as to stay out of 
trouble as much as possible. I am frank with my team lead but nobody listens 
to guys on our level. If I were not eligible to retire I probably would not 
have posted about this.

> P.S.  As far as how much code needs to be "rewritten" if moving from COBOL 
> non-DB2 to DB2, that would depend upon how much of your existing code is 
…[3 more quoted lines elided]…
>

This code is "batch CICS" i.e. no terminal or GUI involved.  The incoming 
messages follow a strictly specified format as do the reply messages.  There 
is considerable database I/O and with DB2 and embedded SQL it would probably 
be better to use a different database processing strategy than the 
navigational style used by DatacommDB.  Still much of the code for 
processing the data could be reused.

> For example, if the application today is a CICS 3270 application using 
> VSAM for file I/O - and you were planning on moving it to a web-based GUI 
…[33 more quoted lines elided]…
>
```

#### ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-16T03:10:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2jmpe3hipuhh2pioigrv7tkgg4oippipo0@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com>`

```
On Sat, 15 Sep 2007 21:11:39 -0400, "Charles Hottel" <chottel@earthlink.net> wrote:

>At work they have done some testing (I have no access to the details) and 
>they claim Java and DB2 are faster than COBOL and DB2.  They also claim that 
>changing the existing COBOL programs to work with DB2 would require 99% of 
>the code to be rewitten.

Two obvious lies, so far.

> I strongly doubt it, but I have had no experience 
>with DB2 although I think I have a good understanding of embedded SQL. They 
…[3 more quoted lines elided]…
>anyone that has had experience with this kind of conversion/rewrite.

They'll do it. You're hosed.

>What I find particularly interesting in this regard is that the 
>specifications for the new system say 95% of the transactions must be 
>processed in 30 seconds, and 99% of the transactions must be processed in 60 
>seconds. Wow! To say I am underwhelmed is a gross understatement! Currently 
>using COBOL and Datacomm/DB we process transactions in less than one second. 

The evolution of acceptable response time:

1970 CICS, VSAM                         1.0 seconds
1980 CICS, DB2                            2.0 seconds
1990 Standalone Windows             .1 seconds
1990 Client/server, LAN                 .5 seconds
2000 Web based, C++                 1.0 seconds
2000 Web based, Java                 2.0 seconds

You could step back and watch the train wreck. Thirty seconds is completely unacceptable. 
That system will be replaced, along with those who approved it.

>This is from the time the transaction (a message) is removed from the queue 
>(MQSeries is used) until the time when the reply is placed onto the outbound 
>queue.  If this is modernization then I just don't see the point especially 
>when it is costing 300+ million a year.  Or many making money is the point! 

'We'd have a great company if it weren't for those damned users and customers.'

There won't be money to be made, because no one will use a system that slow.

Having having said that, I'm reminded of a major retailer converting its payroll system
from mainframe to Peoplesoft. The old system, written 100% in assembly language, was very
fast. A weekly check run produced 400K checks in 3 hours. A trial run of Peoplesoft on
Unix took 36 hours. Mainframers were giving each other high fives. 

Then they partitioned the database and ran Peoplesoft on 30 servers in parallel. It ran
the checks in 2 hours. Mainframers cleaned out there desks and left quietly.
```

##### ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-16T14:01:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcjcv0$jrq$1@reader1.panix.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <2jmpe3hipuhh2pioigrv7tkgg4oippipo0@4ax.com>`

```
In article <2jmpe3hipuhh2pioigrv7tkgg4oippipo0@4ax.com>,
Robert  <no@e.mail> wrote:

[snip]

>Then they partitioned the database and ran Peoplesoft on 30 servers in
>parallel. It ran
>the checks in 2 hours. Mainframers cleaned out there desks and left quietly.

This is similar to something that happened at my current site a few years 
back; it was taking a month of Sundays just to load up the tables and the 
maniframers were all aglow in the light of their own superiority.  (Never 
mind that this delay caused the consulting firm to need job orders 
extended to cover this time... just a coincidence, of course)  

My tech lead was a bit confused by this so I suggested he ask three/four 
simple questions during the next status meeting:

1) Were the loads being performed by system utilities or executed SQL?

2) Were the source databases on one set of physically separate disks and 
the targets on another... or were they trying to load 
partition-to-partition to the same physical disks?  If separate disks were 
being used... had the databases been partitioned, or at least the indices 
isolated to a different physical disk than the data?

3) Was archive logging turned on or off during the load?

After the meeting my lead came back and said 'I didn't really know what I 
was asking... but it must have been something good because they got 
*really* angry!'

(think back... think far, far back... and remember things like 'It is 
usually better, when possible, to use a utility rather than your own code' 
and 'Thou Shalt Not Compile to the Source Pack'... the terms may have 
changed o'er the decades but the fundamentals remain)

DD
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-16T13:50:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<visqe3p36kfv5vvmpu6664esqp891qm3q7@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <2jmpe3hipuhh2pioigrv7tkgg4oippipo0@4ax.com> <fcjcv0$jrq$1@reader1.panix.com>`

```
On Sun, 16 Sep 2007 14:01:04 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <2jmpe3hipuhh2pioigrv7tkgg4oippipo0@4ax.com>,
>Robert  <no@e.mail> wrote:
…[16 more quoted lines elided]…
>1) Were the loads being performed by system utilities or executed SQL?

>(think back... think far, far back... and remember things like 'It is 
>usually better, when possible, to use a utility rather than your own code' 
>and 'Thou Shalt Not Compile to the Source Pack'... the terms may have 
>changed o'er the decades but the fundamentals remain)

I found the exact opposite on a recent high volume (10 TB), high visability (it's in
Wikipedia) copy of data from one Oracle database to another. Embedded SQL was
sugnificantly faster than SQL*Loader. The reason was the SQL inserted arrays of 1,000 rows
at a time. Error correction is more complicated that way. If there is an error in any of
the 1,000 rows (there were many constraint errors), Oracle returns a single error code and
doesn't tell you which rows. When that happens, the program has to re-insert the rows
individually. 

The project required custom programs anyway, because 'sequences' had to be reassigned. It
wasn't as simple as adding to the end; reassigned sequences had to fit into gaps.

>2) Were the source databases on one set of physically separate disks and 
>the targets on another... or were they trying to load 
>partition-to-partition to the same physical disks?

That's difficult to determine when the disks are in a distant SAN. What appears to be one
disk might actually be two, or vice versa. 

>If separate disks were 
>being used... had the databases been partitioned, or at least the indices 
>isolated to a different physical disk than the data?

Right on. Partitioning allows parallel CPU operations. We did the inserts with 500
parallel processes running on 64 CPUs. The CPUs were only 50% loaded. It didn't go any
faster with 800 processes. 

>3) Was archive logging turned on or off during the load?

You're kidding, right?

>After the meeting my lead came back and said 'I didn't really know what I 
>was asking... but it must have been something good because they got 
>*really* angry!'

The usual angry esponse is 'If you know so much, let's see you do it faster.' That's your
opportunity. That's what you WANT to hear. I wish I had a nickel for every time I heard
that.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-17T09:34:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fclhni$lcn$1@reader1.panix.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <2jmpe3hipuhh2pioigrv7tkgg4oippipo0@4ax.com> <fcjcv0$jrq$1@reader1.panix.com> <visqe3p36kfv5vvmpu6664esqp891qm3q7@4ax.com>`

```
In article <visqe3p36kfv5vvmpu6664esqp891qm3q7@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sun, 16 Sep 2007 14:01:04 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[28 more quoted lines elided]…
>sugnificantly faster than SQL*Loader.

Situations such as these might be reasons for my stating 'it is usually 
better'.  All generalisations are worthless, including this one.

[snip]

>>2) Were the source databases on one set of physically separate disks and 
>>the targets on another... or were they trying to load 
…[4 more quoted lines elided]…
>disk might actually be two, or vice versa. 

As I have said before, both to myself and to others, 'If it were easy then 
*anyone* could do it... it isn't, that is why my/your skills are 
required.'

[snip]

>>3) Was archive logging turned on or off during the load?
>
>You're kidding, right?

Not in the least, Mr Wagner... I try to make as few assumptions as 
possible.

>
>>After the meeting my lead came back and said 'I didn't really know what I 
…[7 more quoted lines elided]…
>that.

That's not really what I want to hear, no.  What I want to hear is the 
person who signs the respondent's timesheet saying 'Ok, if you can do it 
by (date) then there's a project completion bonus for you of ($y)... I've 
had enough of my work and ideas absconded with, and seen others who have 
tried to use my suggestions to get me off-site, to fall for a schoolyard 
taunt as that line is.

DD
```

##### ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-09-16T11:40:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13eqjhhl9dp4daf@corp.supernews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <2jmpe3hipuhh2pioigrv7tkgg4oippipo0@4ax.com>`

```

"Robert" <no@e.mail> wrote in message 
news:2jmpe3hipuhh2pioigrv7tkgg4oippipo0@4ax.com...
> On Sat, 15 Sep 2007 21:11:39 -0400, "Charles Hottel" 
> <chottel@earthlink.net> wrote:
>

<snip>

> You could step back and watch the train wreck. Thirty seconds is 
> completely unacceptable.
> That system will be replaced, along with those who approved it.
>

This is the federal government and when you spend hundreds of millions of 
dollars you call it a success no matter what the outcome.  Those in charge 
will 'fail' upwards into higher positions. I base this on what happend in 
the past (early 1990's) on the first attempt to replace this system. Foe 300 
million they got something you could develop in COBOL/CICS in a few months. 
The project leader when on to become head of OIT and just retired to take up 
feeding at the contractor trough.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-16T14:01:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<53vqe357sk5ul7fthekqb66ter535vn3mi@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <2jmpe3hipuhh2pioigrv7tkgg4oippipo0@4ax.com> <13eqjhhl9dp4daf@corp.supernews.com>`

```
On Sun, 16 Sep 2007 11:40:19 -0400, "Charles Hottel" <chottel@earthlink.net> wrote:

>
>"Robert" <no@e.mail> wrote in message 
…[18 more quoted lines elided]…
>feeding at the contractor trough. 

That's why we have outsourcing .. because it's the easiest or only way to change the
organization's political dynamics. Sometimes it works, sometimes it replaces one set of
inefficiencies with another.
```

#### ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-17T01:06:39+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5l4o31F6f1i0U1@mid.individual.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com>`

```


"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:13ep0krm3102m43@corp.supernews.com...

> At work they have done some testing (I have no access to the details) and 
> they claim Java and DB2 are faster than COBOL and DB2.

This is extremely unlikely, although it is possible if the Java system is 
using parallel servers.

On a level playing field, results will be limited by DB performance and so 
we could expect about the same overall.

I would question why they don't publicise the results.

> They also claim that changing the existing COBOL programs to work with DB2 
> would require 99% of the code to be rewitten.  I strongly doubt it, but I 
> have had no experience with DB2 although I think I have a good 
> understanding of embedded SQL.

They MAY be assuming that there is no tier model in place and everything is 
integrated.


>They want to modernize the systems, i.e. get rid of COBOL, so I believe 
>there is a built in bias and a distinct lack of interest in any 
>measurements or facts that would contradict their view.

Yes, I agree with you. But, more importantly, if that is what they have 
decided, then there is absolutely nothing you can do about it. It really 
doesn't matter what reports, investigations, benchmarks, or tests they run, 
or what the results are; they will do what they want to do.


I would be interested in hearing from
> anyone that has had experience with this kind of conversion/rewrite.

I tried converting some of my stuff to Java from COBOL a few years back and, 
with the right tools, it wasn't difficult. However I gave it up because most 
of my stuff is components anyway and there is little advantage between a 
COM+ component written in COBOL and an EJB written in Java.

Now that I have opted for C# there is no need to convert this stuff anyway; 
it runs fine as unmanaged code under the DotNET Framework.

>
> What I find particularly interesting in this regard is that the 
…[4 more quoted lines elided]…
> one second.

I remember writing stuff to access Datacomm on a mainframe from a PC using 
ODBC. I was quite impressed with Datacomm. I suspect that there are more 
definitions of "transaction" than just the one, inherent in the above 
statement.

> This is from the time the transaction (a message) is removed from the 
> queue (MQSeries is used) until the time when the reply is placed onto the 
> outbound queue.  If this is modernization then I just don't see the point 
> especially when it is costing 300+ million a year.  Or many making money 
> is the point!

There are a number of factors at work here and the views in this forum will 
not figure in them. It has nothing to do with faster, or better, or 
transactions or even Java or COBOL; it has to do with simply stopping a 
process of system development that haemhorrages money like a tap, is 
unwieldy, slow, and inflexible, unresponsive, and unreliable, namely COBOL 
Programming as practised in most corporate shops.

It just isn't viable any more to produce and maintain thousands, even 
millions, of lines of labour intensive code, when there are other options.

Consider... some bean counter says: "We are spending $300 million a year on 
IT and we aren't even a computer company. We can buy the core service for 60 
million and spend another 20 million maintaining our network. However it is 
goingto cost us $500 million to convert."

Do you seriously think that arguments about COBOL being faster, or refuting 
the conversion costs, are going to change anything?

This company is doing what more and more companies all over the world are 
doing. They've had enough, and COBOL is NOT the only game in town any more.

Don't quit your Java homework if you plan to continue working there :-)

Pete.
```

#### ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-16T13:46:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcjc48$qnp$1@reader1.panix.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com>`

```
In article <13ep0krm3102m43@corp.supernews.com>,
Charles Hottel <chottel@earthlink.net> wrote:
>At work they have done some testing (I have no access to the details) and 
>they claim Java and DB2 are faster than COBOL and DB2.

Are the 'they' who make this claim ones who will benefit from the change?  
If so then rest assured that - at least according to my experience - the 
details of the testing will remain deep and dark.

DD
```

#### ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-09-16T08:59:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3FaHi.95110$jH3.4511@bignews6.bellsouth.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com>`

```
"Charles Hottel" <chottel@earthlink.net> wrote:
>
> What I find particularly interesting in this regard is that the specifications for the new system say 95% of the transactions must 
…[4 more quoted lines elided]…
> making money is the point!

In the situations I am familiar with, traditional mainframe databases blow
the doors off SQL type approaches. Whoever designed SQL must have
been entirely clueless, or indifferent, to machine efficiency.

Last year the State of Alabama went from a mainframe based driver's
license system to a client server based SQL system. Processing times went
from about a second to several *minutes*.

About seven years ago the local county commission decided to "dump the
mainframe and go strictly client/server and Oracle." After seven years and
nearly $100 million, the mainframe still does at least 95% of the processing.
Plans to scrap the mainframe have been abandoned for the foreseeable
future. I don't think it's because they learned anything, but the county is
having serious money problems, and they simply can't afford to keep
throwing money at it.
```

##### ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-16T16:08:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net>`

```
On Sun, 16 Sep 2007 08:59:05 -0500, "Judson McClendon" <judmc@sunvaley0.com> wrote:

>"Charles Hottel" <chottel@earthlink.net> wrote:
>>
…[9 more quoted lines elided]…
>been entirely clueless, or indifferent, to machine efficiency.

Everyone who's run a Google search knows that to be untrue. It displays the time it spent
searching three billion Web pages. I just did it with four wildcard words -- "for * * nail
the * was lost". It found 27,000 in .08 seconds. That's fast!

Interesting trivia: the Oracle FAQ at http://www.orafaq.com/ runs on MySQL, not Oracle. 


>Last year the State of Alabama went from a mainframe based driver's
>license system to a client server based SQL system. Processing times went
>from about a second to several *minutes*.

Slow performance was caused by a Federal requirement (Real ID) to verify the driver's
Social Security Number with a Federal computer. Alabama was the first state to use that
network, which was not ready at the time. It has since been speeded up. All must use it by
the end of 2008.
```

###### ↳ ↳ ↳ SQL and Google (was: COBOL and DB2 vs. Java and DB2

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-17T01:51:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a4lHi.173892$1J4.160059@fe06.news.easynews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com>`

```
"Robert" <no@e.mail> wrote in message 
news:iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com...
> On Sun, 16 Sep 2007 08:59:05 -0500, "Judson McClendon" <judmc@sunvaley0.com> 
> wrote:
>
>>"Charles Hottel" <chottel@earthlink.net> wrote:
<snip>
>>In the situations I am familiar with, traditional mainframe databases blow
>>the doors off SQL type approaches. Whoever designed SQL must have
…[7 more quoted lines elided]…
>

Serious question: Do Google searches actually use SQL "under the covers"?  I 
always assumed (with no evidence to back this up) that they used a "proprietary" 
system that didn't use any standard (SQL or otherwise) selection facility.
```

###### ↳ ↳ ↳ Re: SQL and Google (was: COBOL and DB2 vs. Java and DB2

_(reply depth: 4)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-16T21:42:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i4qre3heq2vci4e0goh3u701knu0ujoamk@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <a4lHi.173892$1J4.160059@fe06.news.easynews.com>`

```
On Mon, 17 Sep 2007 01:51:03 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>"Robert" <no@e.mail> wrote in message 
>news:iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com...
…[18 more quoted lines elided]…
>system that didn't use any standard (SQL or otherwise) selection facility.

Your intuition is correct. The search engine is proprietary. I have seen it said that the
Google database is MySQL. Not true. They use MySQL for peripheral things, but not for the
core search engine.
```

###### ↳ ↳ ↳ Re: SQL and Google (was: COBOL and DB2 vs. Java and DB2

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-09-17T07:52:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XMuHi.52091$Y7.39007@bignews3.bellsouth.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <a4lHi.173892$1J4.160059@fe06.news.easynews.com> <i4qre3heq2vci4e0goh3u701knu0ujoamk@4ax.com>`

```
"Robert" <no@e.mail> wrote:
> "William M. Klein" <wmklein@nospam.netcom.com> wrote:
>>
…[6 more quoted lines elided]…
> core search engine.

Then why did you use Google as an example in trying to refute my statement
that SQL is less efficient than traditional mainframe databases, moron? Duh!

No point in arguing with this guy, it's a waste of time. He clearly suffers from
severe cognitive dissonance.
```

###### ↳ ↳ ↳ Re: SQL and Google (was: COBOL and DB2 vs. Java and DB2

_(reply depth: 6)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-17T18:25:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vj2ue397iu9ruhiqo3riujtahrhlngmdbv@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <a4lHi.173892$1J4.160059@fe06.news.easynews.com> <i4qre3heq2vci4e0goh3u701knu0ujoamk@4ax.com> <XMuHi.52091$Y7.39007@bignews3.bellsouth.net>`

```
On Mon, 17 Sep 2007 07:52:48 -0500, "Judson McClendon" <judmc@sunvaley0.com> wrote:

>"Robert" <no@e.mail> wrote:
>> "William M. Klein" <wmklein@nospam.netcom.com> wrote:
…[13 more quoted lines elided]…
>severe cognitive dissonance.
 
Let us review what we've learned so far. 

1. Fast food is good
Action item: call Zagat, fire reviewers

2. Mainframes are better than Unix servers
Action item: call SABRE, rehire mainframers

3. SQL is too slow to be practical
Action item: call Daytona admins in Overland Park, stop SQL queries now, plan to migrate 3
trillion rows to IMS or VSAM, order 150 TB of IBM disk (check budget)
```

###### ↳ ↳ ↳ Re: SQL and Google (was: COBOL and DB2 vs. Java and DB2

_(reply depth: 7)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-20T09:58:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190307531.267012.26760@22g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<vj2ue397iu9ruhiqo3riujtahrhlngmdbv@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <a4lHi.173892$1J4.160059@fe06.news.easynews.com> <i4qre3heq2vci4e0goh3u701knu0ujoamk@4ax.com> <XMuHi.52091$Y7.39007@bignews3.bellsouth.net> <vj2ue397iu9ruhiqo3riujtahrhlngmdbv@4ax.com>`

```
On 18 Sep, 00:25, Robert <n...@e.mail> wrote:
> On Mon, 17 Sep 2007 07:52:48 -0500, "Judson McClendon" <ju...@sunvaley0.com> wrote:
> >"Robert" <n...@e.mail> wrote:
…[27 more quoted lines elided]…
>

Are you saying that DB2 storage is more efficient than VSAM or IMS?
```

###### ↳ ↳ ↳ Re: SQL and Google (was: COBOL and DB2 vs. Java and DB2

_(reply depth: 8)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-20T20:28:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0g76f352peluft9urubjqqhp3j6ht4bvl0@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <a4lHi.173892$1J4.160059@fe06.news.easynews.com> <i4qre3heq2vci4e0goh3u701knu0ujoamk@4ax.com> <XMuHi.52091$Y7.39007@bignews3.bellsouth.net> <vj2ue397iu9ruhiqo3riujtahrhlngmdbv@4ax.com> <1190307531.267012.26760@22g2000hsm.googlegroups.com>`

```
On Thu, 20 Sep 2007 09:58:51 -0700, Alistair <alistair@ld50macca.demon.co.uk> wrote:

>On 18 Sep, 00:25, Robert <n...@e.mail> wrote:
>> On Mon, 17 Sep 2007 07:52:48 -0500, "Judson McClendon" <ju...@sunvaley0.com> wrote:
…[30 more quoted lines elided]…
>Are you saying that DB2 storage is more efficient than VSAM or IMS?

No. Every mainframer knows in his heart that VSAM is the way god intended for data to be
stored.
```

###### ↳ ↳ ↳ Re: SQL and Google (was: COBOL and DB2 vs. Java and DB2

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-21T13:44:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5lglvtF83v37U1@mid.individual.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <a4lHi.173892$1J4.160059@fe06.news.easynews.com> <i4qre3heq2vci4e0goh3u701knu0ujoamk@4ax.com> <XMuHi.52091$Y7.39007@bignews3.bellsouth.net> <vj2ue397iu9ruhiqo3riujtahrhlngmdbv@4ax.com> <1190307531.267012.26760@22g2000hsm.googlegroups.com> <0g76f352peluft9urubjqqhp3j6ht4bvl0@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:0g76f352peluft9urubjqqhp3j6ht4bvl0@4ax.com...
> On Thu, 20 Sep 2007 09:58:51 -0700, Alistair 
> <alistair@ld50macca.demon.co.uk> wrote:
…[48 more quoted lines elided]…
> stored.

I'm glad you didn't take the bait, Robert :-)

Of course, both DB2 and IMS (in IBM mainframe environments) use VSAM 
organisations and access methods under the covers...

Pete.
```

###### ↳ ↳ ↳ Re: SQL and Google (was: COBOL and DB2 vs. Java and DB2

_(reply depth: 4)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-20T09:51:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190307118.761364.37850@d55g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<a4lHi.173892$1J4.160059@fe06.news.easynews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <a4lHi.173892$1J4.160059@fe06.news.easynews.com>`

```
On 17 Sep, 02:51, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> "Robert" <n...@e.mail> wrote in message
>
…[23 more quoted lines elided]…
>  wmklein <at> ix.netcom.com

And do Google searches search web pages? My understanding was that
they search indices extracted from web pages.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-09-17T07:46:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MGuHi.52087$Y7.9502@bignews3.bellsouth.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com>`

```
"Robert" <no@e.mail> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
>>
…[6 more quoted lines elided]…
> the * was lost". It found 27,000 in .08 seconds. That's fast!

Yes, and how many shared servers does it require to achieve that, eh?
My point was about hardware efficiency. If it takes 20 computers to
do what one could do using another approach, then it is less hardware
efficient.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 4)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-17T08:17:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k9vse35srrivese79qnqpf99j5cg73ajv3@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <MGuHi.52087$Y7.9502@bignews3.bellsouth.net>`

```
On Mon, 17 Sep 2007 07:46:13 -0500, "Judson McClendon" <judmc@sunvaley0.com> wrote:

>"Robert" <no@e.mail> wrote:
>> "Judson McClendon" <judmc@sunvaley0.com> wrote:
…[12 more quoted lines elided]…
>efficient.

A server with 20 CPUs costs about $40K. How much does a mainframe cost?
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-09-17T11:17:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pKxHi.61917$t9.54040@bignews7.bellsouth.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <MGuHi.52087$Y7.9502@bignews3.bellsouth.net> <k9vse35srrivese79qnqpf99j5cg73ajv3@4ax.com>`

```
"Robert" <no@e.mail> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
>
…[16 more quoted lines elided]…
> A server with 20 CPUs costs about $40K. How much does a mainframe cost?

What part of "hardware efficient" don't you understand?
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-18T04:39:17+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5l7otdF6tfukU1@mid.individual.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <MGuHi.52087$Y7.9502@bignews3.bellsouth.net> <k9vse35srrivese79qnqpf99j5cg73ajv3@4ax.com> <pKxHi.61917$t9.54040@bignews7.bellsouth.net>`

```


"Judson McClendon" <judmc@sunvaley0.com> wrote in message 
news:pKxHi.61917$t9.54040@bignews7.bellsouth.net...
> "Robert" <no@e.mail> wrote:
>> "Judson McClendon" <judmc@sunvaley0.com> wrote:
…[22 more quoted lines elided]…
> What part of "hardware efficient" don't you understand?

What is the point of "hardware efficiency" if it isn't cost effective?

Just because you COULD run everything on a Cray or Fujitsu super-computer 
and rest assured it was "hardware efficient", doesn't mean you would.

Pete.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 6)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-17T18:53:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vn4ue3hl0tq9s6q3jrhr1ie03fajgh18dc@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <MGuHi.52087$Y7.9502@bignews3.bellsouth.net> <k9vse35srrivese79qnqpf99j5cg73ajv3@4ax.com> <pKxHi.61917$t9.54040@bignews7.bellsouth.net>`

```
On Mon, 17 Sep 2007 11:17:31 -0500, "Judson McClendon" <judmc@sunvaley0.com> wrote:

>"Robert" <no@e.mail> wrote:
>> "Judson McClendon" <judmc@sunvaley0.com> wrote:
…[19 more quoted lines elided]…
>What part of "hardware efficient" don't you understand?

The part about economic efficiency.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-18T04:30:37+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5l7od6F6bn5iU1@mid.individual.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <MGuHi.52087$Y7.9502@bignews3.bellsouth.net>`

```


"Judson McClendon" <judmc@sunvaley0.com> wrote in message 
news:MGuHi.52087$Y7.9502@bignews3.bellsouth.net...
> "Robert" <no@e.mail> wrote:
>> "Judson McClendon" <judmc@sunvaley0.com> wrote:
…[15 more quoted lines elided]…
> efficient.

Judson, you may be over-reacting here (Robert's posts often have that effect 
on people :-)) and losing sight of the actual argument.

If those 20 computers each cost less than one twentieth the cost of the 
single computer, then your case is not made.

While I'm here, I would point out that your statement above regarding SQL is 
at best provocative, at worst, simply untrue.

If, by "traditional mainframe databases" you mean VSAM datasets connected 
together, or (I seem to recall your background is Unisys?) perhaps indexed 
random files in a FORTE style database, then it is very arguable whether 
these would "blow the doors off" an SQL type approach (by which I take it 
you mean Relational Database).

There was a time when this MIGHT have been true, but that time is long gone. 
Certainly, a well designed  "Traditional" DB benchmarked against a poorly 
designed RDB will not fare well (I know, because I used the performance 
argument to enable a certain company to hold onto their existing VSAM and 
resist RDB, but that was 20 years ago...)

I've had a bit to do with Relational Databases (and, indeed, traditional 
databases) and enhancing the performance of both. I don't think your 
statement stands against a modern Relational Database (even free ones like 
MySQL, and PostgreSQL, which are excellent products.)

RDBMS are much smarter than they used to be; the better ones can actually 
monitor their own performance and optimize storage for the statistically 
most likely accesses being experienced. If access patterns change, so does 
the physical organization of the data. Stored procedures can run as 
asynchronous tasks, and the latest models allow result sets to be obtained 
and processed in cache so that connections are freed instantly and there is 
no need to lock a connection while running a SQL cursor, for example.

Ironically, although today's SQL is running on much more powerful platforms 
than yesterday's did, it still not enough for the future and new ways of 
accessing data (not to mention new storage technologies) are already 
emerging

Just one such is the emerging technology of Query Expressions (LINQ) and 
Lambda functions for data, which is using the Relational model to set SQL on 
its head and support deferred execution, load levelling across servers, and 
parallel processing, all transparent to the application programmer. Some of 
this stuff (Lambdas) is showing incredible data transfers with terabytes 
transmitted instantly across country. (Try GOOGLE on the terms I've 
mentioned.)

Here's a video interview from 2005 with Anders Hejlberg, which explains why 
an Object approach to Data access can allow "across the board" access to 
tables in memory, XML files, Documents, as well as Relational DBs, using a 
single OO Query language. Most of what he talks about is now available: 
http://channel9.msdn.com/showpost.aspx?postid=114680

If you bring yourself up to date on database technology you may well find it 
blows the doors off traditional approaches...:-)

Personally, I find it very exciting and am beginning to use C# to run Query 
Expressions rather than SQL. It is very early days yet and I am still 
learning, but it is much more natural than SQL., and integrates seamlessly 
into the language.

With new storage technologies just around the corner we need to find smarter 
ways to access data. SQL, particularly embedded SQL, may be rendered 
redundant by these new approaches. It is a very long way away from 
"traditional mainframe databases".

Pete.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-09-17T11:59:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ElyHi.61944$t9.21954@bignews7.bellsouth.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <MGuHi.52087$Y7.9502@bignews3.bellsouth.net> <5l7od6F6bn5iU1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
>> "Robert" <no@e.mail> wrote:
…[18 more quoted lines elided]…
> If those 20 computers each cost less than one twentieth the cost of the single computer, then your case is not made.

Actually, it is. My point wasn't about cost, or "best", but simply that SQL
was not nearly as efficient (fast) as traditional mainframe databases. :-)

> While I'm here, I would point out that your statement above regarding SQL is at best provocative, at worst, simply untrue.
>
…[6 more quoted lines elided]…
> company to hold onto their existing VSAM and resist RDB, but that was 20 years ago...)

I don't mean relational databases, I mean SQL, period. I'm talking about the
way SQL is designed to operate and be used. The mainframe database I'm
most familiar with is DMSII, which I would call a traditional mainframe
database. Files (tables) are created with one or more specific keys to access
them. DMSII is a relational database. There are many applications, particularly
ad-hoc type queries, where SQL would provide a more flexible tool. But for
batch processing, or for static (pre-designed) queries, there is no way in this
universe that SQL can provide a faster, more efficient tool, than a well
designed database using something like DMSII, because there is a lot more
overhead in the way queries are made and processed with SQL. Saying that
enough hardware to do the job could be assembled misses the point I was
trying to make. The point of hardware efficiency is needing less hardware. :-)

That's not to say that SQL is bad, or that I don't like it for the things it's
good for. But using SQL for those particular types of applications I
mentioned above means you're going to use a whole lot more hardware to
do the same job.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-18T13:34:10+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5l8o8nF718pjU1@mid.individual.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <MGuHi.52087$Y7.9502@bignews3.bellsouth.net> <5l7od6F6bn5iU1@mid.individual.net> <ElyHi.61944$t9.21954@bignews7.bellsouth.net>`

```


"Judson McClendon" <judmc@sunvaley0.com> wrote in message 
news:ElyHi.61944$t9.21954@bignews7.bellsouth.net...
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote:
>> "Judson McClendon" <judmc@sunvaley0.com> wrote:
…[60 more quoted lines elided]…
> :-)

OK, that's a good explanation and I accept what you say, for that particular 
environment.

Nevertheless, there is a lot going on in the world of data access at the 
moment and SQL is probably going to be replaced by  "storage and processor 
independent" Query Expressions.  I accept, that in non OO environments this 
is unlikely to make much difference in the short term. In the long term it 
almost certainly will, especially when people realize that the new 
technology is many thousands of times cheaper and faster than existing 
spinning platters.
>
> That's not to say that SQL is bad, or that I don't like it for the things 
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 6)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-09-17T22:23:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EtOdnczZM5-2znLbnZ2dnUVZ_hadnZ2d@comcast.com>`
- **In-Reply-To:** `<ElyHi.61944$t9.21954@bignews7.bellsouth.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <MGuHi.52087$Y7.9502@bignews3.bellsouth.net> <5l7od6F6bn5iU1@mid.individual.net> <ElyHi.61944$t9.21954@bignews7.bellsouth.net>`

```
Judson McClendon wrote:
> I don't mean relational databases, I mean SQL, period. I'm talking about the
> way SQL is designed to operate and be used. The mainframe database I'm
…[9 more quoted lines elided]…
> trying to make. The point of hardware efficiency is needing less hardware. :-)

What's you've got with SQL, though, is what many (most?) consider an 
adequate trade-off of ease of setup and ease of use (I can retrieve data 
on *any* column, not just the key or an indexed field, although it will 
be significantly slower) versus that hardware efficiency.

Plus, when you talk hardware efficiency, now you're tying the product to 
  a particular type of hardware - what's efficient on one is less 
efficient on another.

I understand the point you're trying to make.  Unisys told us that for 
applications that went from DMS (their network database) to RDMS (their 
relational database), the time didn't increase, but processor 
utilization was 3x what it was with DMS.  However, you can change tables 
on the fly with RDMS, and the program chugs on.  With DMS, if you change 
the size of any of the record types, the programs will abort unless 
they're recompiled against the new schema.

Tradeoffs is the name of the game.  :)  How much more inefficient is a 
GUI interface?  How many people eschew them?
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 5)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-17T19:05:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m45ue3deuajvdu72tf730doddtk8e7g7dm@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <MGuHi.52087$Y7.9502@bignews3.bellsouth.net> <5l7od6F6bn5iU1@mid.individual.net>`

```
On Tue, 18 Sep 2007 04:30:37 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:


>Personally, I find it very exciting and am beginning to use C# to run Query 
>Expressions rather than SQL. It is very early days yet and I am still 
>learning, but it is much more natural than SQL., and integrates seamlessly 
>into the language.

The AT&T Daytona database translates SQL queries (actually a superset of SQL) into
well-written C, compiles it and then executes it on Many Parallel Processors. Speed is
eight times faster than the best of PL/SQL, PERL, Python, etc. It routinely queries
databases with more than a trillion rows.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-18T13:36:07+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5l8oc9F72du8U1@mid.individual.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <MGuHi.52087$Y7.9502@bignews3.bellsouth.net> <5l7od6F6bn5iU1@mid.individual.net> <m45ue3deuajvdu72tf730doddtk8e7g7dm@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:m45ue3deuajvdu72tf730doddtk8e7g7dm@4ax.com...
> On Tue, 18 Sep 2007 04:30:37 +1200, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[15 more quoted lines elided]…
> databases with more than a trillion rows.

I'm not in the least surprised, but it is nice to know there are already 
major applications looking at this approach.

Pete.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 5)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-20T09:54:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190307271.935987.17950@n39g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<5l7od6F6bn5iU1@mid.individual.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <MGuHi.52087$Y7.9502@bignews3.bellsouth.net> <5l7od6F6bn5iU1@mid.individual.net>`

```
On 17 Sep, 17:30, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:

> Just one such is the emerging technology of Query Expressions (LINQ) and
> Lambda functions for data, which is using the Relational model to set SQL on
…[4 more quoted lines elided]…
> mentioned.)

My pedanticism knows no bounds. Even at the speed of light it would
not be possible to transfer even one terabyte of data across country
INSTANTLY. You may care to try transferring one bit of data if you use
entangled photons but you that is one bit only.

>
> Here's a video interview from 2005 with Anders Hejlberg, which explains why
…[6 more quoted lines elided]…
>

This brings to mind the existance of Cache (OO database for Java) and
the post above. Why would somebody want to use DB2 with Java when
there are better database technologies optimised for use with Java?

> Personally, I find it very exciting and am beginning to use C# to run Query
> Expressions rather than SQL. It is very early days yet and I am still
> learning, but it is much more natural than SQL., and integrates seamlessly
> into the language.
>

My boozy chum came out with a good comment about SQL and DB2. He
wondered why commercial use SQL was so difficult to understand?

> - Show quoted text -
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-21T12:10:53+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5lgggjF7pr79U1@mid.individual.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <MGuHi.52087$Y7.9502@bignews3.bellsouth.net> <5l7od6F6bn5iU1@mid.individual.net> <1190307271.935987.17950@n39g2000hsh.googlegroups.com>`

```


"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1190307271.935987.17950@n39g2000hsh.googlegroups.com...
> On 17 Sep, 17:30, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[16 more quoted lines elided]…
>

You may be confusing "instantly" with "immediately". An instant can be a 
defined period of time, although it is usally considered to be a very short 
period.

"In an instant...", "On the third instant..."

Pedants should really keep dictionaries handy...:-)

>>
>> Here's a video interview from 2005 with Anders Hejlberg, which explains 
…[25 more quoted lines elided]…
> wondered why commercial use SQL was so difficult to understand?

Obviously, he needs to drink more... :-)

Pete.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 7)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-21T09:31:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190392277.739978.228280@57g2000hsv.googlegroups.com>`
- **In-Reply-To:** `<5lgggjF7pr79U1@mid.individual.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <MGuHi.52087$Y7.9502@bignews3.bellsouth.net> <5l7od6F6bn5iU1@mid.individual.net> <1190307271.935987.17950@n39g2000hsh.googlegroups.com> <5lgggjF7pr79U1@mid.individual.net>`

```
On 21 Sep, 01:10, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
>
…[7 more quoted lines elided]…
> period.

Perhaps I am interpreting your imprecise English in a fashion that
suits me. I did, indeed, take INSTANT to mean IMMEDIATELY with no
discernible delay. So how short is your instant? One picosecond?

>
> "In an instant...", "On the third instant..."
…[35 more quoted lines elided]…
> Obviously, he needs to drink more... :-)

I'll tell him that. He might take you up on that suggestion.

>
> Pete.
> --
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 6)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-20T20:03:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mv56f3pstr3280iifgaecdur3t2djj8n0g@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <MGuHi.52087$Y7.9502@bignews3.bellsouth.net> <5l7od6F6bn5iU1@mid.individual.net> <1190307271.935987.17950@n39g2000hsh.googlegroups.com>`

```
On Thu, 20 Sep 2007 09:54:31 -0700, Alistair <alistair@ld50macca.demon.co.uk> wrote:

>On 17 Sep, 17:30, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
>wrote:
…[12 more quoted lines elided]…
>entangled photons but you that is one bit only.

A command to a SAN can more terrabytes of data from one machine to another instantly.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 7)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-21T09:40:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190392840.133279.311490@d55g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<mv56f3pstr3280iifgaecdur3t2djj8n0g@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <3FaHi.95110$jH3.4511@bignews6.bellsouth.net> <iu3re35hkgn0ftltl8th3lvis4pr3pmojs@4ax.com> <MGuHi.52087$Y7.9502@bignews3.bellsouth.net> <5l7od6F6bn5iU1@mid.individual.net> <1190307271.935987.17950@n39g2000hsh.googlegroups.com> <mv56f3pstr3280iifgaecdur3t2djj8n0g@4ax.com>`

```
On 21 Sep, 02:03, Robert <n...@e.mail> wrote:
> On Thu, 20 Sep 2007 09:54:31 -0700, Alistair <alist...@ld50macca.demon.co.uk> wrote:
> >On 17 Sep, 17:30, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
…[16 more quoted lines elided]…
>

I suspect that that is a bigger instance of an INSTANT than either
Pete or myself would allow.
```

#### ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-09-16T11:49:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13eqni9sebfpod3@news.supernews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com>`

```
Charles Hottel wrote:
> At work they have done some testing (I have no access to the details)
> and they claim Java and DB2 are faster than COBOL and DB2.  They also
> claim that changing the existing COBOL programs to work with DB2
> would require 99% of the code to be rewitten.

Giggle.

Eliminate the constant (DB2) and they're saying JAVA is faster than COBOL.

More giggles.
```

#### ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-17T17:40:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4_yHi.195009$M%1.189538@fe10.news.easynews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com>`

```
Charles,
  I was able to get some information (a reply when I forwarded your original note) from one of my "usually reliable source" within IBM.  I don't know if the following will help - but it might, (*IF* you want to cause waves, you can refer "your" IBM people to the DB2 performance peope for additional input)

I am sending this as "Rich Text" because it has a table that doesn't convert well to plain text.  I hope that the NG can read it (I'll check after I send it)


    ****

Bill,

We do have performance data from DB2 performance that shows COBOL is the 
fastest of SQL, Java, C and COBOL. From the IBM DB2 performance department:

Here are the numbers for a simple stored procedure I wrote. The stored procedure does the
following:

1. Singleton Select
2. Select + Fetch of 50 rows
3. Searched Update

It was designed so that database lock contention is not an issue and pure API performance 
differences would be seen.

The following is a measurement with 5 DB2 Connect PE V7.1 clients calling the stored procedures
using and Embedded SQL 'C' program:

     Transactions Per Second OS/390 CPU Utilization Normalized TPS (ITR) 
      SQLJ (Java) 639.39 89.05 718.00 
      SQL/PSM 1275.51 86.53 1474.07 
      C 1347.71 82.37 1636.16 
      COBOL 1385.04 76.64 1807.20 

Looks like this translates into about 10% better normalized throughput for COBOL over C.
For COBOL-Java, you get about 150% better normalized throughput for COBOL over Java 
```

##### ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-09-17T19:23:33-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13eu325g442e533@corp.supernews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <4_yHi.195009$M%1.189538@fe10.news.easynews.com>`

```

  "William M. Klein" <wmklein@nospam.netcom.com> wrote in message news:4_yHi.195009$M%1.189538@fe10.news.easynews.com...
  Charles,
    I was able to get some information (a reply when I forwarded your original note) from one of my "usually reliable source" within IBM.  I don't know if the following will help - but it might, (*IF* you want to cause waves, you can refer "your" IBM people to the DB2 performance peope for additional input)

  I am sending this as "Rich Text" because it has a table that doesn't convert well to plain text.  I hope that the NG can read it (I'll check after I send it)


      ****

  Bill,

  We do have performance data from DB2 performance that shows COBOL is the 
  fastest of SQL, Java, C and COBOL. From the IBM DB2 performance department:

  Here are the numbers for a simple stored procedure I wrote. The stored procedure does the
  following:

  1. Singleton Select
  2. Select + Fetch of 50 rows
  3. Searched Update

  It was designed so that database lock contention is not an issue and pure API performance 
  differences would be seen.

  The following is a measurement with 5 DB2 Connect PE V7.1 clients calling the stored procedures
  using and Embedded SQL 'C' program:

       Transactions Per Second OS/390 CPU Utilization Normalized TPS (ITR) 
        SQLJ (Java) 639.39 89.05 718.00 
        SQL/PSM 1275.51 86.53 1474.07 
        C 1347.71 82.37 1636.16 
        COBOL 1385.04 76.64 1807.20 


  Looks like this translates into about 10% better normalized throughput for COBOL over C.
  For COBOL-Java, you get about 150% better normalized throughput for COBOL over Java 




  -- 
  Bill Klein
   wmklein <at> ix.netcom.com
  "Charles Hottel" <chottel@earthlink.net> wrote in message news:13ep0krm3102m43@corp.supernews.com...
  > At work they have done some testing (I have no access to the details) and 
  > they claim Java and DB2 are faster than COBOL and DB2.  They also claim that 
…[18 more quoted lines elided]…
  > 

  Thanks Bill I have forwarded this to my project leader.  It is nice to see some object measurements that give some realistic idea of what to expect.  I apprecite you going to this trouble and I also thank you IBM contact.  It may be too late to have any effect but you never know.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-18T14:05:55+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5l8q47F6uet3U2@mid.individual.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <4_yHi.195009$M%1.189538@fe10.news.easynews.com> <13eu325g442e533@corp.supernews.com>`

```
Charles,

It isn't "too late" or "too early" or too anything else. You folks are 
missing the point entirely (although I agree it does no harm to provide 
evidence backing your contention...).

These decisions are taken at a level that couldn't care less about 
performance, they care about having to spend a fortune developing and 
maintaining code for an obsolete paradigm. This is the "hard part" about the 
decline of COBOL. It simply isn't relevant or viable for large scale system 
development any more.

(See my previous post).

Some comments on Bill's post below...

Pete.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 4)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-09-18T08:37:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13evhjbhs89nide@corp.supernews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <4_yHi.195009$M%1.189538@fe10.news.easynews.com> <13eu325g442e533@corp.supernews.com> <5l8q47F6uet3U2@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:5l8q47F6uet3U2@mid.individual.net...
> Charles,
>
…[9 more quoted lines elided]…
>
<snip>

Well you are right about where the decisions are being made. They are not 
particulary tech savvy and are very dependent upon what they are told, but 
they are knowledgeable about the business.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 4)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-18T19:09:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hoo0f3p07cbp3tosjbjg49v3d1t265u30m@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <4_yHi.195009$M%1.189538@fe10.news.easynews.com> <13eu325g442e533@corp.supernews.com> <5l8q47F6uet3U2@mid.individual.net>`

```
On Tue, 18 Sep 2007 14:05:55 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>These decisions are taken at a level that couldn't care less about 
>performance, they care about having to spend a fortune developing and 
>maintaining code for an obsolete paradigm. This is the "hard part" about the 
>decline of COBOL. It simply isn't relevant or viable for large scale system 
>development any more.

Management can change the platform, thus the money going out, without changing the
paradigm. As a result, we have former mainframe shops how running on Unix that's set up to
clone the mainframe environment. Cobol programming standards are unchanged, scripts mimic
JCL, databases are designed to look like VSAM files. I have actually seen database tables
with a column named FILLER CHAR(200). 

Old Timers in such shops, I call them Keepers of the PERFORM THRU, are very sensitive to
challenges to their remaining hegemony. They will viciously fire anyone they see as a
threat. Even when the person follows their programming standards to the letter. 

This is not what management intended, but it goes on every day in countless medium sized
companies. I haven't seen it in large (F-100) companies because .. I don't know ..
employees are more talented, methodology is followed in spirit rather than letter, Cobol
is a tiny player in the big IT picture.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-19T13:27:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5lbc7oF7cbopU1@mid.individual.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <4_yHi.195009$M%1.189538@fe10.news.easynews.com> <13eu325g442e533@corp.supernews.com> <5l8q47F6uet3U2@mid.individual.net> <hoo0f3p07cbp3tosjbjg49v3d1t265u30m@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:hoo0f3p07cbp3tosjbjg49v3d1t265u30m@4ax.com...
> On Tue, 18 Sep 2007 14:05:55 +1200, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[18 more quoted lines elided]…
> with a column named FILLER CHAR(200).

That's very sad.

>
> Old Timers in such shops, I call them Keepers of the PERFORM THRU, are 
…[4 more quoted lines elided]…
> letter.

I guess time will take care of that.

>
> This is not what management intended, but it goes on every day in 
> countless medium sized
> companies.

Countless? I hope not, Robert.


>I haven't seen it in large (F-100) companies because .. I don't know ..
> employees are more talented, methodology is followed in spirit rather than 
> letter, Cobol
> is a tiny player in the big IT picture.

For the last year I have been relaxing at home and working from there, so I 
haven't been out at the coal face and can't confirm or deny whether my 
experience matches yours.

Around March next year (after the Summer here...:-)) I'll be back in the 
market place and will probably return to Europe for a while. It will be 
interesting to see whather what you are describing is world-wide or confined 
to the USA.

I guess it is part of the "transition" from one way of doing things to 
another.

Pete.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 6)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-09-18T21:51:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13f102jg676jp4d@corp.supernews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <4_yHi.195009$M%1.189538@fe10.news.easynews.com> <13eu325g442e533@corp.supernews.com> <5l8q47F6uet3U2@mid.individual.net> <hoo0f3p07cbp3tosjbjg49v3d1t265u30m@4ax.com> <5lbc7oF7cbopU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:5lbc7oF7cbopU1@mid.individual.net...
>
>
…[42 more quoted lines elided]…
>

Yes more than the number quarks in the known universe.  Or is it multiverse?
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 6)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-19T03:35:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f2n1f3t3elpp5fbhbhe71pck9sup2kui5b@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <4_yHi.195009$M%1.189538@fe10.news.easynews.com> <13eu325g442e533@corp.supernews.com> <5l8q47F6uet3U2@mid.individual.net> <hoo0f3p07cbp3tosjbjg49v3d1t265u30m@4ax.com> <5lbc7oF7cbopU1@mid.individual.net>`

```
On Wed, 19 Sep 2007 13:27:18 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>
>
…[34 more quoted lines elided]…
>I guess time will take care of that.

No. It is commonly thought that dinosaurs are old guys aged over 50. In my experience at
three out of three companies, they were aged 35-45. Old guys are flexible. The dogmatic
ones are middle-aged.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 5)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2008-01-15T22:18:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nipqo3dd6hd4794hnrq0ocak7v2thjr0k1@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <4_yHi.195009$M%1.189538@fe10.news.easynews.com> <13eu325g442e533@corp.supernews.com> <5l8q47F6uet3U2@mid.individual.net> <hoo0f3p07cbp3tosjbjg49v3d1t265u30m@4ax.com>`

```
On Tue, 18 Sep 2007 19:09:19 -0500, Robert <no@e.mail> wrote:

>On Tue, 18 Sep 2007 14:05:55 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
>wrote:
…[12 more quoted lines elided]…
>
I also have seen code like this in a shop where I was contracting.  It
was interesting to see the decisions made because they went from IBM
mainframe to Unix as a part of the Year 2000 remediation.  They
emulated VSAM using SQL and Oracle.  As someone who was 60+ at the
time I winced at some of the things I saw.  I also would like to have
seen a replacement of most of the systems I worked on.  I also would
like to have seen a decent IDE.  Uni-SPF wasn't even as powerful as
ISPF for the z/OS let alone what I believe the Microfocus IDE's
probably were capable of.  I wonder how much of the advantage C# or
the other OO languages have is the IDEs and repositories associated
with them.  If good repository tools were available for the procedural
languages, how much development time would be saved.  I know that when
I was on the SHARE/Guide Language Futures Task Force, we considered
that the development of a good repository tool where information about
all the components (record descriptions, fields, programs,
subroutines, business rules, etc.) was stored, kept current and was
accessible and searchable would give major productivity improvements.
Pete's description of the environment he has available when developing
in C# bears out what we said over 20 years ago. 

>Old Timers in such shops, I call them Keepers of the PERFORM THRU, are very sensitive to
>challenges to their remaining hegemony. They will viciously fire anyone they see as a
>threat. Even when the person follows their programming standards to the letter. 

As someone who fervently believes standards need to keep up to date
and we need easier ways of doing things, I would hope that I would be
embracing new technology that works.
>
>This is not what management intended, but it goes on every day in countless medium sized
>companies. I haven't seen it in large (F-100) companies because .. I don't know ..
>employees are more talented, methodology is followed in spirit rather than letter, Cobol
>is a tiny player in the big IT picture.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 6)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-16T00:10:13-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ur6ro3pkiku1gqohuiu4ff5rffvetqsrop@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <4_yHi.195009$M%1.189538@fe10.news.easynews.com> <13eu325g442e533@corp.supernews.com> <5l8q47F6uet3U2@mid.individual.net> <hoo0f3p07cbp3tosjbjg49v3d1t265u30m@4ax.com> <nipqo3dd6hd4794hnrq0ocak7v2thjr0k1@4ax.com>`

```
On Tue, 15 Jan 2008 22:18:52 -0400, Clark F Morris <cfmpublic@ns.sympatico.ca> wrote:

>On Tue, 18 Sep 2007 19:09:19 -0500, Robert <no@e.mail> wrote:
>

>>Old Timers in such shops, I call them Keepers of the PERFORM THRU, are very sensitive to
>>challenges to their remaining hegemony. They will viciously fire anyone they see as a
…[4 more quoted lines elided]…
>embracing new technology that works.

The version of Cobol in wide use has not changed in 22 years, since 1985. During that
time, the number of general purpose computers worldwide went from 30 million to 1 billion.

The 2002 Cobol Standard has been ignored, for the most part, because the 'Cobol community'
does not want change. The purpose of shop standards is to keep change out. It worked.
Problem is, it also excluded Cobol from tremendous growth in the computer industry. The
'Cobol community' was left behind.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 7)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2008-01-16T13:30:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5v6f7mF1l930sU1@mid.individual.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <4_yHi.195009$M%1.189538@fe10.news.easynews.com> <13eu325g442e533@corp.supernews.com> <5l8q47F6uet3U2@mid.individual.net> <hoo0f3p07cbp3tosjbjg49v3d1t265u30m@4ax.com> <nipqo3dd6hd4794hnrq0ocak7v2thjr0k1@4ax.com> <ur6ro3pkiku1gqohuiu4ff5rffvetqsrop@4ax.com>`

```
In article <ur6ro3pkiku1gqohuiu4ff5rffvetqsrop@4ax.com>,
	Robert <no@e.mail> writes:
> On Tue, 15 Jan 2008 22:18:52 -0400, Clark F Morris <cfmpublic@ns.sympatico.ca> wrote:
> 
…[15 more quoted lines elided]…
> does not want change. 

Of course, it might also be that th4e changtes bring nothing that was
needed to get the job done.  Why re-write an application because some
ivory-tower academic things you should do things differently when the
application has been doing its job for over two decades?

>                       The purpose of shop standards is to keep change out. It worked.

Pretty pessimistic view.  The purpose of shop standards is to keep people
from using bad coding practices as a way to promote job security.  Just
like the language, a local standard can be changed.  the difference usually
is that when trying to change a local standard someone is going to look
at the change with an eye towards cost of implementation and advantagr
provided.  The same is never true of standard bodies who rather than
trying to help the industry just want to be the one driving the bus.

> Problem is, it also excluded Cobol from tremendous growth in the computer industry. The
> 'Cobol community' was left behind.

Considering how much COBOL is still out there, that's pretty funny.  We
have a professor here who is always talking about how a certain local
company with millions of lines of COBOL is "going to re-write all of it
in JAVA".  Everytime I mention this to a manager in the COBOL shop they
end out rolling on the floor laughing!!

bill
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 8)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-16T19:38:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ll9to3lheanhhtlj5e5a5alihmd8okvour@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <4_yHi.195009$M%1.189538@fe10.news.easynews.com> <13eu325g442e533@corp.supernews.com> <5l8q47F6uet3U2@mid.individual.net> <hoo0f3p07cbp3tosjbjg49v3d1t265u30m@4ax.com> <nipqo3dd6hd4794hnrq0ocak7v2thjr0k1@4ax.com> <ur6ro3pkiku1gqohuiu4ff5rffvetqsrop@4ax.com> <5v6f7mF1l930sU1@mid.individual.net>`

```
On 16 Jan 2008 13:30:30 GMT, billg999@cs.uofs.edu (Bill Gunshannon) wrote:

>In article <ur6ro3pkiku1gqohuiu4ff5rffvetqsrop@4ax.com>,
>	Robert <no@e.mail> writes:

>>                       The purpose of shop standards is to keep change out. It worked.
>
…[5 more quoted lines elided]…
>provided.  

The Prisoner's Dilemma is often used in game theory. 

"Two suspects, A and B, are arrested by the police. The police have insufficient evidence
for a conviction, and, having separated both prisoners, visit each of them to offer the
same deal: if one testifies for the prosecution against the other and the other remains
silent, the betrayer goes free and the silent accomplice receives the full 10-year
sentence. If both remain silent, both prisoners are sentenced to only six months in jail
for a minor charge. If each betrays the other, each receives a five-year sentence. Each
prisoner must make the choice of whether to betray the other or to remain silent. However,
neither prisoner knows for sure what choice the other prisoner will make. So this dilemma
poses the question: How should the prisoners act?"

Shop programming standards are a real life instance of that game. Imagine a shop having
two programming teams. If they cooperate by writing good code, they have a good code base.
If one team 'defects' by writing a shop standard that cripples the other while the other
coopeates, all the shop's code looks like the 'bad' team. It wins and the 'nice' team
loses. If both 'defect' by issuing conflicting standards, both have a crappy code base to
work on.

The optimal strategy (Nash Equilibrium) in the Prisoner's Dilemma is to defect. This
illustrates that an optimal strategy for self-interest does not necessarily maximize
community interest (Pareto optimum). Thus, the optimal strategy for a programming team
manager is to write a shop standard, actually a team standard, that tries to cripple the
other teams. This explains why companies have multiple crippling standards and crappy
code.

>> Problem is, it also excluded Cobol from tremendous growth in the computer industry. The
>> 'Cobol community' was left behind.
…[5 more quoted lines elided]…
>end out rolling on the floor laughing!!

They all laughed when I told them we're still writing Cobol. Then I showed them green
screens we developed last week. They're not laughing now.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-17T01:55:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fmmci7$1qa$1@reader2.panix.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <ur6ro3pkiku1gqohuiu4ff5rffvetqsrop@4ax.com> <5v6f7mF1l930sU1@mid.individual.net> <ll9to3lheanhhtlj5e5a5alihmd8okvour@4ax.com>`

```
In article <ll9to3lheanhhtlj5e5a5alihmd8okvour@4ax.com>,
Robert  <no@e.mail> wrote:
>On 16 Jan 2008 13:30:30 GMT, billg999@cs.uofs.edu (Bill Gunshannon) wrote:
>
…[13 more quoted lines elided]…
>The Prisoner's Dilemma is often used in game theory. 

Theory is the same as practise... in theory. 

[snip]

>Shop programming standards are a real life instance of that game.  
>Imagine a shop having
…[8 more quoted lines elided]…
>work on.

So what you posit, Mr Wagner, is a shop where there may exist two kinds of 
programming, one bad and one good.  This situation seems to be less a 
matter of Game Theory and more a matter for Gresham's Law, so that when 
there exist in a shop two kind of programming, one Bad and one Good, then 
over time the Bad programming will drive out the Good.

So while Theory is the same as Practise, in theory... in Practise Theory 
gets trumped by Law.

(On a more serious note... perhaps we have worked in different shops; I've 
found that if you write code that does not conform to the shop standard 
the code does not get implemented into Prod.  Not many shops I've seen 
keep Programmers who cannot write Prod-implementable code... *some* of 
them get turned into Managers, sure, but there aren't *that* many corner 
cubicles around.

'I will not write code that way!'

'You will not use up desk-space to do otherwise... next?')

DD
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 10)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-16T20:48:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vgfto39e1ce697l2fet0vebul3he7dl5v2@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <ur6ro3pkiku1gqohuiu4ff5rffvetqsrop@4ax.com> <5v6f7mF1l930sU1@mid.individual.net> <ll9to3lheanhhtlj5e5a5alihmd8okvour@4ax.com> <fmmci7$1qa$1@reader2.panix.com>`

```
On Thu, 17 Jan 2008 01:55:19 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <ll9to3lheanhhtlj5e5a5alihmd8okvour@4ax.com>,
>Robert  <no@e.mail> wrote:
…[37 more quoted lines elided]…
>over time the Bad programming will drive out the Good.

Gresham's Law says bad money drives out good in two ways. First, on domestic sales,
customers would rather tender bad money having the same exchange rate as good money. That
doesn't apply here because programs are not sold to an employer. Second, on international
sales, customers would rather tender good money because it has higher purchasing power,
while bad money remains in the country. That's analogous to good programmers leaving for
greener pastures, while equally paid bad programmers remain with the company.

>So while Theory is the same as Practise, in theory... in Practise Theory 
>gets trumped by Law.

Are you saying the Theory of Relativity is trumped by Newton's Laws?

>(On a more serious note... perhaps we have worked in different shops; I've 
>found that if you write code that does not conform to the shop standard 
…[3 more quoted lines elided]…
>cubicles around.

Failed programmers become testers and production supporters.

>'I will not write code that way!'
>
>'You will not use up desk-space to do otherwise... next?')

More like, "There is an opening on the Java team. They don't believe in standards either."
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 11)_

- **From:** tim Josling <tejgcc_nospam@westnet.com.au>
- **Date:** 2008-01-17T06:44:59
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13otubb9mg6ne71@corp.supernews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <ur6ro3pkiku1gqohuiu4ff5rffvetqsrop@4ax.com> <5v6f7mF1l930sU1@mid.individual.net> <ll9to3lheanhhtlj5e5a5alihmd8okvour@4ax.com> <fmmci7$1qa$1@reader2.panix.com> <vgfto39e1ce697l2fet0vebul3he7dl5v2@4ax.com>`

```
On Wed, 16 Jan 2008 20:48:12 -0600, Robert wrote:


> Gresham's Law says bad money drives out good in two ways. First, on
> domestic sales, customers would rather tender bad money having the same
…[5 more quoted lines elided]…
> programmers remain with the company.

There is also issue of the "market for lemons". People will not pay for
quality if they think they probably won't get it.

Example: I can't tell if the way you are doing the project is good or not.
Do it as fast as possible for minimum cost.

Example: if managers cannot tell who is a good developer, they will only
pay for poor developers.

Tim Josling
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-17T13:34:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fmnlh9$6s4$1@reader2.panix.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <ll9to3lheanhhtlj5e5a5alihmd8okvour@4ax.com> <fmmci7$1qa$1@reader2.panix.com> <vgfto39e1ce697l2fet0vebul3he7dl5v2@4ax.com>`

```
In article <vgfto39e1ce697l2fet0vebul3he7dl5v2@4ax.com>,
Robert  <no@e.mail> wrote:
>On Thu, 17 Jan 2008 01:55:19 +0000 (UTC), docdwarf@panix.com () wrote:
>
>>In article <ll9to3lheanhhtlj5e5a5alihmd8okvour@4ax.com>,
>>Robert  <no@e.mail> wrote:

[snip]

>>>The Prisoner's Dilemma is often used in game theory. 
>>
…[22 more quoted lines elided]…
>Gresham's Law says bad money drives out good in two ways.

Do you happen to have a cite for this, Mr Wagner, or are you adhering to a 
Jacquard-like canard of weaving this yourself, whole cloth?  A source 
slightly closer to Gresham, chronologically, states nothing of the kind; 
see http://www.1911encyclopedia.org/Gresham's_Law .

[snip]

>>So while Theory is the same as Practise, in theory... in Practise Theory 
>>gets trumped by Law.
>
>Are you saying the Theory of Relativity is trumped by Newton's Laws?

That might be obvious, Mr Wagner, to anyone who has seen shops where 
Inertia is paramount and any Energy expended doesn't seem to Matter.

>
>>(On a more serious note... perhaps we have worked in different shops; I've 
…[6 more quoted lines elided]…
>Failed programmers become testers and production supporters.

Not in many shops I've seen, Mr Wagner... testing is, at times, reduced to 
'did it compile?' and Prod Support is, similarly, 'who touched it last?'

(The response of 'Doakes did... and Doakes got another (*never* 'a 
better') job/died/was fired/got promoted to Management' generates 'Well, 
it is *yours* now... and Prod doesn't come back up until it gets fixed.')

>
>>'I will not write code that way!'
…[4 more quoted lines elided]…
>standards either."

Ummmm... writing Java, last I looked, is still 'writing code'.

DD
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 12)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-17T19:20:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ngpvo31l1g5vtl3il2j6fhssh62vmlel0a@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <ll9to3lheanhhtlj5e5a5alihmd8okvour@4ax.com> <fmmci7$1qa$1@reader2.panix.com> <vgfto39e1ce697l2fet0vebul3he7dl5v2@4ax.com> <fmnlh9$6s4$1@reader2.panix.com>`

```
On Thu, 17 Jan 2008 13:34:33 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <vgfto39e1ce697l2fet0vebul3he7dl5v2@4ax.com>,
>Robert  <no@e.mail> wrote:
…[36 more quoted lines elided]…
>see http://www.1911encyclopedia.org/Gresham's_Law .

Gresham's Law was not discovered by Sir Thomas Gresham and is not a Law, because it is not
a mathematical formula that predicts outsomes. It is simply an explanation of why low
quality money prevails over higher quality money. People extend its applicability to other
situations where the quality of goods or services is declining. Like Murphy's Law, the
80/20 Rule and GIGO, it gives the impression that the speaker has a clue about what's
going on while avoiding the inconvenience of fact gathering and genuine analysis.

>>>So while Theory is the same as Practise, in theory... in Practise Theory 
>>>gets trumped by Law.
…[4 more quoted lines elided]…
>Inertia is paramount and any Energy expended doesn't seem to Matter.

That's called Mediterranean Malaise, the antithesis of Work Ethic. In another milieu,
unproductive workers are called slackers. 

>>>(On a more serious note... perhaps we have worked in different shops; I've 
>>>found that if you write code that does not conform to the shop standard 
…[8 more quoted lines elided]…
>'did it compile?' and Prod Support is, similarly, 'who touched it last?'

Compiling and testing are a drain on productivity. Those of us who don't make errors just
check the code in and submit a build ticket. 

>(The response of 'Doakes did... and Doakes got another (*never* 'a 
>better') job/died/was fired/got promoted to Management' generates 'Well, 
>it is *yours* now... and Prod doesn't come back up until it gets fixed.')

We outsourced production support. When it's 2am here, it's 2pm in Bangalore.

>>>'I will not write code that way!'
>>>
…[5 more quoted lines elided]…
>Ummmm... writing Java, last I looked, is still 'writing code'.

Nah. Wrting code is obsolete. They glue components together.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-18T08:02:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fmpmek$35$1@reader2.panix.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <vgfto39e1ce697l2fet0vebul3he7dl5v2@4ax.com> <fmnlh9$6s4$1@reader2.panix.com> <ngpvo31l1g5vtl3il2j6fhssh62vmlel0a@4ax.com>`

```
In article <ngpvo31l1g5vtl3il2j6fhssh62vmlel0a@4ax.com>,
Robert  <no@e.mail> wrote:
>On Thu, 17 Jan 2008 13:34:33 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[42 more quoted lines elided]…
>a mathematical formula that predicts outsomes.

Mr Wagner, leaving aside the fact that many statutes that have nothing to 
do with mathematics are Laws... how is it that you make an assertion about 
Gresham's Law ('Gresham's Law says bad money drives out good in two ways') 
and then, when asked for a cite, say it is neither Gresham's nor Law?

'There was no pot, it was broken when I borrowed it and I returned it in 
perfect condition.')

DD
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 14)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-18T07:53:13-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<olb1p3tbp82j3gahf7ci70blggcv0srlod@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <vgfto39e1ce697l2fet0vebul3he7dl5v2@4ax.com> <fmnlh9$6s4$1@reader2.panix.com> <ngpvo31l1g5vtl3il2j6fhssh62vmlel0a@4ax.com> <fmpmek$35$1@reader2.panix.com>`

```
On Fri, 18 Jan 2008 08:02:28 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <ngpvo31l1g5vtl3il2j6fhssh62vmlel0a@4ax.com>,
>Robert  <no@e.mail> wrote:
…[49 more quoted lines elided]…
>and then, when asked for a cite, say it is neither Gresham's nor Law?

Here's a citation:

"In an influential theoretical article, Rolnick and Weber (1986) argued that bad money
would drive good money to a premium rather than driving it out of circulation.

The experiences of dollarization in countries with weak economies and currencies (for
example Israel in the 1980s, Eastern Europe and countries in the period immediately after
the collapse of the Soviet bloc, or South American countries throughout the late twentieth
and early twenty-first century) may be seen as Gresham's Law operating in its reverse form
(Guidotti & Rodriguez, 1992)"

http://en.wikipedia.org/wiki/Gresham%27s_law
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 15)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-19T01:45:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fmrkn8$l3h$1@reader2.panix.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <ngpvo31l1g5vtl3il2j6fhssh62vmlel0a@4ax.com> <fmpmek$35$1@reader2.panix.com> <olb1p3tbp82j3gahf7ci70blggcv0srlod@4ax.com>`

```
In article <olb1p3tbp82j3gahf7ci70blggcv0srlod@4ax.com>,
Robert  <no@e.mail> wrote:
>On Fri, 18 Jan 2008 08:02:28 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[69 more quoted lines elided]…
>http://en.wikipedia.org/wiki/Gresham%27s_law

A theoretical article?  Theory is the same as practise... in theory.

DD
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-19T09:14:32+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vcfl6F1ltlt4U1@mid.individual.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <ll9to3lheanhhtlj5e5a5alihmd8okvour@4ax.com> <fmmci7$1qa$1@reader2.panix.com> <vgfto39e1ce697l2fet0vebul3he7dl5v2@4ax.com> <fmnlh9$6s4$1@reader2.panix.com> <ngpvo31l1g5vtl3il2j6fhssh62vmlel0a@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:ngpvo31l1g5vtl3il2j6fhssh62vmlel0a@4ax.com...
> On Thu, 17 Jan 2008 13:34:33 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[85 more quoted lines elided]…
>

ROFL!

You tell him, Robert... :-)

>>(The response of 'Doakes did... and Doakes got another (*never* 'a
>>better') job/died/was fired/got promoted to Management' generates 'Well,
…[14 more quoted lines elided]…
> Nah. Wrting code is obsolete. They glue components together.

I certainly do. But I write the odd component also... :-)

Pete.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-18T14:08:46+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5l8q9iF72og9U2@mid.individual.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <4_yHi.195009$M%1.189538@fe10.news.easynews.com> <13eu325g442e533@corp.supernews.com>`

```
Charles,

It isn't "too late" or "too early" or too anything else. You folks are 
missing the point entirely (although I agree it does no harm to provide 
evidence backing your contention...).

These decisions are taken at a level that couldn't care less about 
performance, they care about having to spend a fortune developing and 
maintaining code for an obsolete paradigm. This is the "hard part" about the 
decline of COBOL. It simply isn't relevant or viable for large scale system 
development any more.

(See my previous post).

Some comments on Bill's post below...

Pete.
```

#### ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** Bruce_E_Banks@hotmail.com
- **Date:** 2007-09-17T18:50:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190080230.801476.8280@n39g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<13ep0krm3102m43@corp.supernews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com>`

```
On Sep 15, 10:11 pm, "Charles Hottel" <chot...@earthlink.net> wrote:
> At work they have done some testing (I have no access to the details) and
> they claim Java and DB2 are faster than COBOL and DB2.  They also claim that
…[16 more quoted lines elided]…
> when it is costing 300+ million a year.  Or many making money is the point!

Hello Charles.
    Totaly Convert or Integrate - That is the question

    I recently retired from a Telephone company where I worked system
support for a large COBOL system. It used both On-line & Batch
processes with mixed IMS & DB2 databases - with web access to specific
(order system) applications . We use on-line (MFS + web) interfaces
for day-to-day changes & batch processes for cyclic (billing) or
timely (tech visit) activity. We were on an OS390 'mainframe' machine
so some things may not translate exactly.

     In our shop we had a lot of legacy applications using IMS
databases. Then IBM decided to grandfather IMS and standardize on DB2
so any new applications must use DB2. Of course, updating existing
applications mandated mixing IMS & DB2. The only 'rewrite' required
was to add the SQL calls and re-compile. You now have both a PSB & a
Plan and, of course, the Database Administrators now have 2 database
systems to monitor / re-fresh ; but day to day business office folks
saw no change in their MFS Screens (no re-training !).

     As to system resources, DB2 takes more horsepower than IMS, for a
number of reasons, so converting the whole database systems from IMS
to DB2 is going to increase storage/processing power requirements, as
well as raising referential integrity issues.

     If you are adding web access to the mix, there are additional
considerations to address. Can my legacy systems be accessable from
the web? Can I process multiple changes to the same record(s) the same
day, etc. You can merge this technology into your existing business
model with a minimum of changes / training

     If you are converting from COBOL to JAVA then you are replacing
the whole system, not just the interface / control portions, so you
are, effectively, back to square-one.  All new processes  interfaces,
business flow, training issues , etc. - not to mention legacy data
conversion, and so on.

     Of course, many things could be driving the switch to JAVA. For
example, if IBM has decided that they are doing the equivalent of
dumping Windows XP to force you to buy Vista, then what choice do you
have?
```

##### ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-09-17T19:11:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190081509.975299.215090@22g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<1190080230.801476.8280@n39g2000hsh.googlegroups.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com>`

```
On Sep 18, 1:50 pm, Bruce_E_Ba...@hotmail.com wrote:

> dumping Windows XP to force you to buy Vista, then what choice do you
> have?

Apple Mac, Linux (Ubuntu, PCLinuxOS, Mepis, Mandriva, ...), BSD.
```

##### ↳ ↳ IMS (was: COBOL and DB2 vs. Java and DB2

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-18T05:26:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AkJHi.193923$1J4.49386@fe06.news.easynews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com>`

```
<Bruce_E_Banks@hotmail.com> wrote in message 
news:1190080230.801476.8280@n39g2000hsh.googlegroups.com...
> On Sep 15, 10:11 pm, "Charles Hottel" <chot...@earthlink.net> wrote:
><snip>
>     Then IBM decided to grandfather IMS and standardize on DB2 so any new 
> applications must use DB2.

I just HAD to comment on this.  I don't read everything that IBM says 
everywhere, but I think you would be VERY hard pressed to find anywhere that 
says that IBM is "grandfathering" IMS (either DB or DC - to use their old 
nomenclature). I do suspect that IBM would LOVE for all IMS customers to move to 
DB2 (and possibly CICS).  However, they are regularly coming up with 
enhancements to new releases of IMS.  They continue with peformance enhancements 
(especially to fastpath IMS).  Having said all of this, I am talking 
particularly about on zOS.  I am not so certain about "DLI" and VSE.

If there has been any official "denegration" of IMS, I would love to know where 
it is (or where it is documented).
```

##### ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-09-18T08:33:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13evham1i75lt1e@corp.supernews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com>`

```

<Bruce_E_Banks@hotmail.com> wrote in message 
news:1190080230.801476.8280@n39g2000hsh.googlegroups.com...
> On Sep 15, 10:11 pm, "Charles Hottel" <chot...@earthlink.net> wrote:
>> At work they have done some testing (I have no access to the details) and
…[73 more quoted lines elided]…
>

Thanks. They are rplacing the whole system. It is too far along for it to 
change unless they stumble and Congress cuts off the money.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-18T19:20:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com>`

```
On Tue, 18 Sep 2007 08:33:17 -0400, "Charles Hottel" <chottel@earthlink.net> wrote:


>Thanks. They are replacing the whole system. It is too far along for it to 
>change unless they stumble and Congress cuts off the money. 

Bureaucrats are adept at concealing stuumbles. That's their job. 

Another Cobol shop down the tubes. Why? I submit it was easier to change language than to
battle the entrenched Cobol culture i.e. resistance to change.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-19T13:41:23+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5lbd25F6svobU1@mid.individual.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com...
> On Tue, 18 Sep 2007 08:33:17 -0400, "Charles Hottel" 
> <chottel@earthlink.net> wrote:
…[9 more quoted lines elided]…
> battle the entrenched Cobol culture i.e. resistance to change.

I don't think so. It is bigger than that. (Although that can certianly be a 
contributing factor. Not all COBOL shops are resistant to change.)

Put yourself in the place of an IT Director with responsibility for a large 
budget.

How can you justify keeping the organization tied to COBOL when systems are 
consistently late, fail to deliver what is needed, and cost a fortune to 
maintain?(Not only that, but even the CEO knows that COBOL has no 
credibility; he reads the airline magazines.. :-))

The increasing computer literacy in the population means that people will 
simply build their own solutions using spread sheets and databases and 
standard software. This means the information resource is out of control and 
you are responsible for it. Without a VIABLE coherent IT plan, you have 
failed in your job.

It is very tempting to install a package (SAP, Siebel,ORACLE, etc) to handle 
(and centralize) core processing and get modern quick build applications 
running on the edges of it. Move towards SOA with Java and/or Websphere and 
start showing money is being well spent. IT responsiveness to change and 
delivery of systems can be seen to improve. Consequently, organizational 
morale improves and the Business start to see IT as an asset, rather than 
the enemy...

There is no place for COBOL in such a world.

Pete.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 5)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-19T04:21:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1ao1f31elueulk012buejof2hnhdq8knnf@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net>`

```
On Wed, 19 Sep 2007 13:41:23 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>
>
…[19 more quoted lines elided]…
>budget.

I have been. 

>How can you justify keeping the organization tied to COBOL when systems are 
>consistently late,

This talk about missed deadlines doesn't agree with my experience. I've never (almost
never) worked on a project that missed it deadline nor budget.

At worst, maybe they didn't deliver what was desired, but that was a fault in the specs
rather than the delivery. 

>fail to deliver what is needed, and cost a fortune to 
>maintain?(Not only that, but even the CEO knows that COBOL has no 
>credibility; he reads the airline magazines.. :-))

Define fortune. Is $100K too much for a minor change that affects millions of customer
accounts? It seems high from a technical perspecive. All we did was add a few IF NOT
statements. Why should that take six months of planning and testing? 
>
>The increasing computer literacy in the population means that people will 
…[3 more quoted lines elided]…
>failed in your job.

The fear factor kicks in. Your job is on the line.

I think fear is an overused and ineffective management tool. It gets people's attention,
but it doesn't make them any smarter. After you fire them, the next batch is just as dumb.

>It is very tempting to install a package (SAP, Siebel,ORACLE, etc) to handle 
>(and centralize) core processing and get modern quick build applications 
…[4 more quoted lines elided]…
>the enemy...

Yep. That's what it says in airline magazines. That's why SAP and PeopleSoft are
successful. Technically, they're lame. Ask end users how they like it compared to the old
system. They'll tell you it can't handle situations that occur frequently. Like it won't
ship an order for 300 national flags because one of them is out of stock. The custromer
says they don't need Lesotho, ship the other 299. SAP says no.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-19T09:38:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcqqn6$adi$1@reader1.panix.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net> <1ao1f31elueulk012buejof2hnhdq8knnf@4ax.com>`

```
In article <1ao1f31elueulk012buejof2hnhdq8knnf@4ax.com>,
Robert  <no@e.mail> wrote:


>All we did was add
>a few IF NOT
>statements. Why should that take six months of planning and testing? 

You get time for planning and testing?  Pfah, they must be soft bunch over 
there... I get a request muttered to me while washing my hands in the 
men's room ('We need you to whooooossshhhhh and make sure it balances out 
with the flusssshhhhh... you can get that done by Thursday, right?') and 
if I'm lucky there'll be some scrawls made to 'clarify' things on the 
nearest perforated paper.  It then gets put into Prod for the weekend run 
and... and about three months later the guy who replaced the guy who made 
the request (promoted for his Brilliant Idea, you know) comes storming 
into my cube screaming about how the quarterlies are off.

Six months planning and testing?  Pfah... where did I mention this... 
ahhhh, back a mere eight years ago, wonderful thing, this Web.  From 
<http://groups.google.com/group/comp.software.year-2000/msg/7b0f478783b66534?output=gplain>

--begin quoted text:

A story:  years ago I was working in Hartford, CT, with a Major Insurance 
Company rewriting their long-term disability management system for a new 
database (IMS to DB2).  At one point early on I was called to attend a 
meeting... this miserable, stinkwad, two-bit, gut-crawling idiot who was 
so stupid he had to have his initials monogrammed on his cuffs in case he 
forgot who he was announced that there would be *no* period of parallel 
testing between the two systems.  Folks got a bit... upset and he 
squelched their complaints by announcing 'Nope, no way, costs too much 
money, the old system costs US$500,000 per month to run and we're just 
going to cut over.'

In the silence which almost always follows the Mentioning of a Large Sum 
of Money (note: I believed then, as now, that this sum was completely 
fictitious; very few IMS systems written fifteen years ago cost this much 
to run) I said 'That's a sum of money, true... has anyone calculated how 
much it will cost to fix things when six months after cutover folks 
discover that they've been pumping out bad checks for the past half-year?'

'That's a good question,' he intoned, '... I'll get back to you on that.'

I was never asked to attend a meeting with him ever again and I retained 
that particular gem for future use.

--end quoted text

>>
>>The increasing computer literacy in the population means that people will 
…[5 more quoted lines elided]…
>The fear factor kicks in. Your job is on the line.

So what?  There's always another job; if someone doesn't like your new 
haircut you can get fired.

>
>I think fear is an overused and ineffective management tool. It gets
>people's attention,
>but it doesn't make them any smarter. After you fire them, the next
>batch is just as dumb.

Mr Wagner, have you learned *nothing* in the Management World?  The goal 
is not to have smart, qualified people around so that you can allocate, 
co-ordinate and motivate them towards the accomplishment of a stated 
Executive goal; the goal is to have people smart enough to get things 
done, almost, but not so smart that they threaten your position.  The last 
person fired is the one who gets blamed for everything and Life goes on.

DD
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 7)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-19T22:22:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ogo3f350u25gm2devct07kvd6eshrq5j7v@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net> <1ao1f31elueulk012buejof2hnhdq8knnf@4ax.com> <fcqqn6$adi$1@reader1.panix.com>`

```
On Wed, 19 Sep 2007 09:38:46 +0000 (UTC), docdwarf@panix.com () wrote:


>>I think fear is an overused and ineffective management tool. It gets
>>people's attention,
…[8 more quoted lines elided]…
>person fired is the one who gets blamed for everything and Life goes on.

You're such a cynic. Medium sized companies DO work like it says in Dilbert, but very
large companies don't. They attract the best and brightest, mostly non-Americans, do
everything by the book and are pleasant places to work. 

My advice on looking for a contracting gig: avoid medium sized companies, go for
world-class. Exception: if they outsourced their IT to IBM, they're back in bush league.
I've seen it over and over. IBMers are the first to go simply because they're the most
expensive. IBM bills them at $200 and pays them $35. And IBM promises mean nothing. I had
an 8 month contract with IBM that lasted 2 months. It wasn't just me, a hundred others
were similarly screwed over. 

The best places to work are big pharmaceuticals and big telcos appearing on the Fortune
100. Avoid insurance companies, banks and any company that still has a mainframe. Whatever
you do, avoid IBM.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 8)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-09-19T21:14:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190261673.621184.286240@q3g2000prf.googlegroups.com>`
- **In-Reply-To:** `<ogo3f350u25gm2devct07kvd6eshrq5j7v@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net> <1ao1f31elueulk012buejof2hnhdq8knnf@4ax.com> <fcqqn6$adi$1@reader1.panix.com> <ogo3f350u25gm2devct07kvd6eshrq5j7v@4ax.com>`

```
On Sep 20, 3:22 pm, Robert <n...@e.mail> wrote:
>
> I had
> an 8 month contract with IBM that lasted 2 months.

That's what happens when you keep telling them they lack vision and
leadership.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 9)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-20T07:41:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<osp4f31bqvuicu5s25623457hq5gi0assj@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net> <1ao1f31elueulk012buejof2hnhdq8knnf@4ax.com> <fcqqn6$adi$1@reader1.panix.com> <ogo3f350u25gm2devct07kvd6eshrq5j7v@4ax.com> <1190261673.621184.286240@q3g2000prf.googlegroups.com>`

```
On Wed, 19 Sep 2007 21:14:33 -0700, Richard <riplin@Azonic.co.nz> wrote:

>On Sep 20, 3:22 pm, Robert <n...@e.mail> wrote:
>>
…[4 more quoted lines elided]…
>leadership.

Generally, IBM managers are very good. They are long-term IBM employees. IBM's techies on
outsource projects are often below average. They are subcontracted from any source; there
is no approved vendor list.  The IBM manager doesn't even interview them. Small
contracting companies operating from India love IBM.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-20T14:23:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fctvo5$1tj$1@reader1.panix.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1ao1f31elueulk012buejof2hnhdq8knnf@4ax.com> <fcqqn6$adi$1@reader1.panix.com> <ogo3f350u25gm2devct07kvd6eshrq5j7v@4ax.com>`

```
In article <ogo3f350u25gm2devct07kvd6eshrq5j7v@4ax.com>,
Robert  <no@e.mail> wrote:
>On Wed, 19 Sep 2007 09:38:46 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[13 more quoted lines elided]…
>You're such a cynic.

I may appear such to those who are unable to read sarcasm... but I'll take 
that risk.

>Medium sized companies DO work like it says in
>Dilbert, but very
>large companies don't. They attract the best and brightest, mostly
>non-Americans, do
>everything by the book and are pleasant places to work. 

Mr Wagner, I have no idea what you are calling 'medium' or 'large'... but 
the only companies I have worked with are, I believe, what many people 
would call 'large'.

>
>My advice on looking for a contracting gig: avoid medium sized companies, go for
>world-class.

Such... classism.  My advice is: find a place doing something that you 
enjoy that'll pay you rates you both believe to be fair... then Do Your 
Job.

DD
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 9)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-20T20:25:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8f66f3l6n21qa3gbu22b0r57paanasmjl5@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1ao1f31elueulk012buejof2hnhdq8knnf@4ax.com> <fcqqn6$adi$1@reader1.panix.com> <ogo3f350u25gm2devct07kvd6eshrq5j7v@4ax.com> <fctvo5$1tj$1@reader1.panix.com>`

```
On Thu, 20 Sep 2007 14:23:01 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <ogo3f350u25gm2devct07kvd6eshrq5j7v@4ax.com>,
>Robert  <no@e.mail> wrote:
…[28 more quoted lines elided]…
>would call 'large'.

Every company likes to think of itself as large. My standard is the same as Fortune 100,
where the cutoff is sales or revenues of $22B. If your company is smaller, it's second
tier.

Relatively unknown entries on the list are Valero (90B) and health care companies such as
Cardinal (82B) and AmerisourceBergen (61B). 

In terms of profit, in one year .. 2002 I think .. the top ten pharmaceuticals made more
than the other 490 combined. That's pretty remarkable. 


>
>>
…[7 more quoted lines elided]…
>DD
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 7)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-20T10:11:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190308308.143749.84960@22g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<fcqqn6$adi$1@reader1.panix.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net> <1ao1f31elueulk012buejof2hnhdq8knnf@4ax.com> <fcqqn6$adi$1@reader1.panix.com>`

```
On 19 Sep, 10:38, docdw...@panix.com () wrote:

> Six months planning and testing?  Pfah... where did I mention this...
> ahhhh, back a mere eight years ago, wonderful thing, this Web.  From
…[28 more quoted lines elided]…
>

I've been lurking here too long. I remember that story from the first
time around.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-20T17:14:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcu9pp$6f5$1@reader1.panix.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1ao1f31elueulk012buejof2hnhdq8knnf@4ax.com> <fcqqn6$adi$1@reader1.panix.com> <1190308308.143749.84960@22g2000hsm.googlegroups.com>`

```
In article <1190308308.143749.84960@22g2000hsm.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 19 Sep, 10:38, docdw...@panix.com () wrote:
>
…[4 more quoted lines elided]…
>> --begin quoted text:

[snip]

>> --end quoted text
>>
>
>I've been lurking here too long. I remember that story from the first
>time around.

Hmmmmm... perhaps not long enough so that the memory begins to fade.

DD
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 9)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-20T13:56:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190321778.615752.3990@19g2000hsx.googlegroups.com>`
- **In-Reply-To:** `<fcu9pp$6f5$1@reader1.panix.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1ao1f31elueulk012buejof2hnhdq8knnf@4ax.com> <fcqqn6$adi$1@reader1.panix.com> <1190308308.143749.84960@22g2000hsm.googlegroups.com> <fcu9pp$6f5$1@reader1.panix.com>`

```
On 20 Sep, 18:14, docdw...@panix.com () wrote:
> In article <1190308308.143749.84...@22g2000hsm.googlegroups.com>,
>
…[18 more quoted lines elided]…
> DD

That is senility that causes memory fade, Doc.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-21T01:00:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcv548$afl$1@reader1.panix.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190308308.143749.84960@22g2000hsm.googlegroups.com> <fcu9pp$6f5$1@reader1.panix.com> <1190321778.615752.3990@19g2000hsx.googlegroups.com>`

```
In article <1190321778.615752.3990@19g2000hsx.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 20 Sep, 18:14, docdw...@panix.com () wrote:
>> In article <1190308308.143749.84...@22g2000hsm.googlegroups.com>,
…[19 more quoted lines elided]…
>That is senility that causes memory fade, Doc.

Now I am confused... for a goodly while my memory had been, admittedly, 
porous.  If the porosity fades then will it hold things better?

DD
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 11)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-09-20T21:57:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13f695fln9kpkbb@corp.supernews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190308308.143749.84960@22g2000hsm.googlegroups.com> <fcu9pp$6f5$1@reader1.panix.com> <1190321778.615752.3990@19g2000hsx.googlegroups.com> <fcv548$afl$1@reader1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:fcv548$afl$1@reader1.panix.com...
> In article <1190321778.615752.3990@19g2000hsx.googlegroups.com>,
> Alistair  <alistair@ld50macca.demon.co.uk> wrote:
…[27 more quoted lines elided]…
>

Doc you have a mind like a steele seive.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 11)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-21T09:36:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190392589.030910.125560@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<fcv548$afl$1@reader1.panix.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190308308.143749.84960@22g2000hsm.googlegroups.com> <fcu9pp$6f5$1@reader1.panix.com> <1190321778.615752.3990@19g2000hsx.googlegroups.com> <fcv548$afl$1@reader1.panix.com>`

```
On 21 Sep, 02:00, docdw...@panix.com () wrote:
> In article <1190321778.615752.3...@19g2000hsx.googlegroups.com>,
>
…[30 more quoted lines elided]…
>

How will you be able to tell?
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-21T16:45:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fd0sfb$de6$1@reader1.panix.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190321778.615752.3990@19g2000hsx.googlegroups.com> <fcv548$afl$1@reader1.panix.com> <1190392589.030910.125560@k79g2000hse.googlegroups.com>`

```
In article <1190392589.030910.125560@k79g2000hse.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 21 Sep, 02:00, docdw...@panix.com () wrote:
>> In article <1190321778.615752.3...@19g2000hsx.googlegroups.com>,
…[5 more quoted lines elided]…
>> >> Alistair  <alist...@ld50macca.demon.co.uk> wrote:

[snip]

>> >> >I've been lurking here too long. I remember that story from the first
>> >> >time around.
…[9 more quoted lines elided]…
>How will you be able to tell?

Answering a question with a question, Mr Maclean, is no answer at all.

DD
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 13)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-21T19:01:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190426509.190259.304720@n39g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<fd0sfb$de6$1@reader1.panix.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190321778.615752.3990@19g2000hsx.googlegroups.com> <fcv548$afl$1@reader1.panix.com> <1190392589.030910.125560@k79g2000hse.googlegroups.com> <fd0sfb$de6$1@reader1.panix.com>`

```
On 21 Sep, 17:45, docdw...@panix.com () wrote:
> In article <1190392589.030910.125...@k79g2000hse.googlegroups.com>,
>
…[26 more quoted lines elided]…
> DD

Are you sure?
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 14)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-22T13:32:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fd35gi$ems$1@reader1.panix.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190392589.030910.125560@k79g2000hse.googlegroups.com> <fd0sfb$de6$1@reader1.panix.com> <1190426509.190259.304720@n39g2000hsh.googlegroups.com>`

```
In article <1190426509.190259.304720@n39g2000hsh.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 21 Sep, 17:45, docdw...@panix.com () wrote:
>> In article <1190392589.030910.125...@k79g2000hse.googlegroups.com>,
>>
>> Alistair  <alist...@ld50macca.demon.co.uk> wrote:
>> >On 21 Sep, 02:00, docdw...@panix.com () wrote:

[snip]

>> >> Now I am confused... for a goodly while my memory had been, admittedly,
>> >> porous.  If the porosity fades then will it hold things better?
…[5 more quoted lines elided]…
>Are you sure?

I believe I have had sufficient certain to attempt an explanation to that 
in the past, Mr Maclean; as needs be that might be dragged up, as well... 
perhaps causing another 'I've been lurking here so long that I remember 
the original' posting.

DD
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-19T22:14:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5lcb3uF7h7dmU1@mid.individual.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net> <1ao1f31elueulk012buejof2hnhdq8knnf@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:1ao1f31elueulk012buejof2hnhdq8knnf@4ax.com...
> On Wed, 19 Sep 2007 13:41:23 +1200, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[84 more quoted lines elided]…
> says they don't need Lesotho, ship the other 299. SAP says no.

That's what ABAP is for :-)

I have asked end users how they like it, and I've had them come and tell me 
how they like it. For the first six months, they HATE it. It isn't like the 
old system and there is a learning curve. Ask them again a year later. 
Completely different story. They make a request for a new report or screen 
and it is delivered within a couple of days, sometimes even the same day. 
They want to change functionality or enhance it; no problem. Usually within 
a couple of weeks and often much less than that.

They DON'T CARE whether it is "technically lame" (and that is very arguable 
also... the latest R3 is apparently "technically innovative" and has 
certainly excited attention from Citrix) as long as they get what they want.

You don't seriously believe the ongoing success of these packages is because 
of what Senior Managers read in airline magazines? (their public image 
certainly helps, but they wouldn't still be doing business after 30 years if 
the products were crap.) SAP was worth just under 67 billion yesterday 
(Yahoo! Finance statistics...); they must be doing something right :-).

Anyway, my point wasn't about SAP or Siebel or even a package solution. My 
point was that you have to do SOMETHING to stop hand carving code line by 
line.

OO is a step in the right direction because it empowers components, and 
these get the reuse that is a real corporate money/time saver. SOA is a good 
route for many companies because it enables them to leverage existing code 
into something more valuable, without necessarily having to re-develop it. 
(Legacy code can be rewrapped as components and served up as a Web Service, 
under the umbrella of an SOA architecture.)

There are now many options for companies. Evolutions in hardware have taken 
the focus off  "performance anxiety"; (if it doesn't perform, throw a few 
more processors at it, God knows, they're cheap enough...:-)), and placed it 
more squarely on delivery of functionality (which is where it should have 
been all along). Web Services are allowing facilities to be written once, 
and re-used from anywhere in the Corporate network, OO and components are 
minimising the costs of mantenance, and the time to deliver changes.

It is a different world than it was when COBOL was the only game in town.

Pete.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 5)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-20T10:07:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190308024.612346.313970@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<5lbd25F6svobU1@mid.individual.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net>`

```
On 19 Sep, 02:41, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
>
> How can you justify keeping the organization tied to COBOL when systems are
> consistently late, fail to deliver what is needed, and cost a fortune to
> maintain?(Not only that, but even the CEO knows that COBOL has no
> credibility; he reads the airline magazines.. :-))

So, no Java system has ever been delivered late or failed to be
delivered? No Java system has ever failed to deliver what is needed
and all Java systems cost nothing to maintain?
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-21T12:25:23+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5lghblF82kd0U1@mid.individual.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net> <1190308024.612346.313970@k79g2000hse.googlegroups.com>`

```


"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1190308024.612346.313970@k79g2000hse.googlegroups.com...
> On 19 Sep, 02:41, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[10 more quoted lines elided]…
>
The quoted paragraph above discusses COBOL. It makes no comment about Java 
or any other programming language. Your questions are therefore a 
non-sequitur.

Pete.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 7)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-21T09:33:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190392384.879157.226310@22g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<5lghblF82kd0U1@mid.individual.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net> <1190308024.612346.313970@k79g2000hse.googlegroups.com> <5lghblF82kd0U1@mid.individual.net>`

```
On 21 Sep, 01:25, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
>
…[19 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."

By IMPLICATION, Cobol is described as being at fault whereas Java, by
omission in the sentence but contained in the thread title, is
perfect.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 6)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-09-20T20:49:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13f657abq4vnhc0@corp.supernews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net> <1190308024.612346.313970@k79g2000hse.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1190308024.612346.313970@k79g2000hse.googlegroups.com...
> On 19 Sep, 02:41, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[11 more quoted lines elided]…
>

It is easy to write bad code in Java, much easier than in COBOL.  The book 
"Java Puzzlers" is chock full of code that looks like it does one thing but 
really does something else. There are "Java Pitfalls", "More JavaPitfalls", 
and "Effective Java" also mentions many Java flaws.  Those are just the one 
on my bookshelf.

In COBOL we have programs and subprograms. Some compilers allow multiple 
'Entry" points although I believe that the general recommendation is to 
avoid those (perhaps because they tend to be unrelated).  A Java class has 
constructor(s), static methods and class methods and they could be viewed as 
multiple entry points into the class, yet due to encapsulation that is 
deemed a good thing as they are all related to the class But Java classes 
are even more complicated as they can be public, private, protected or if 
the access specifier is left off they call it 'package-private'. All of 
these affect the access to the classes and their methods.  I won't go into 
all the details.  There is inheritance and overriding, there is overloading 
which looks a lot like overriding but is different/confusing.  Because  the 
possible interaction result in more complexity there are book on design 
patterns which advise how to solve certain problems and on other techniques 
that should be avoided.

Just look at the Java api libraries.  There have several attempts at I/O 
packages and Java I/O classes offer hundreds of cobinations of 
functionality.  At www.mindprod.com there is an applet you can use where you 
tell it the I/O characteristics you want and the applet shows you sample 
code.  Classes like Date and Calendar don't really give business programmers 
what they want.  You can code you own BusinessDate class for business using 
Java api classes but the fact that you have to shows it was not designed 
with business app in mind. IIRC the Double class has two rounding modes only 
and they are not what business programmers typically want or need or are 
sometimes required by law to use. Well BigDecimal will do what you want, but 
because there is no operator overloading you must call methos which are more 
cumbersome.

Probably most are not that interested so I will stop now, but this is just 
the tip of the iceberg.

AAt Work I there is a weekly systems availablity meeting and I get emails 
which show all of the outstanding production problems and it sometimes shows 
failed attempts at solutions and give an idea of how long it takes to 
resolve problems.  Even though only a small fraction of the new system is in 
production, that systems problems completely dominate the report.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 7)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-21T09:35:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190392542.870814.122690@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<13f657abq4vnhc0@corp.supernews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net> <1190308024.612346.313970@k79g2000hse.googlegroups.com> <13f657abq4vnhc0@corp.supernews.com>`

```
On 21 Sep, 01:49, "Charles Hottel" <chot...@earthlink.net> wrote:
> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
>
…[56 more quoted lines elided]…
> production, that systems problems completely dominate the report.

You have my sympathy. The drum I was banging was in support of Cobol.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 5)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2008-01-15T22:27:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9iqqo31fc36tq175r648ij7hdorv5jbskj@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net>`

```
On Wed, 19 Sep 2007 13:41:23 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>
>
…[24 more quoted lines elided]…
>credibility; he reads the airline magazines.. :-))

That is why Vista is years late and lacking many of the promised
features.
>
>The increasing computer literacy in the population means that people will 
…[3 more quoted lines elided]…
>failed in your job.

Will all of those spreadsheets meet Sarbanes Oxley requirements for
documentation and accountability?  
>
>It is very tempting to install a package (SAP, Siebel,ORACLE, etc) to handle 
…[8 more quoted lines elided]…
>
Since at least some in IBM are showing how COBOL code can be a part of
SOA and could be more so if IBM would ever implement the relevant
parts of the 2002 standard, I dispute that statement.  I would dispute
it even more heavily if the IDE's available for Websphere provide the
same fullness of support for COBOL that they do for C/C++ and Java.  

>Pete.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 6)_

- **From:** Alistair.J.L.Maclean@googlemail.com
- **Date:** 2008-01-16T13:56:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d257ba88-2726-4234-9f79-e60221f4414d@s13g2000prd.googlegroups.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net> <9iqqo31fc36tq175r648ij7hdorv5jbskj@4ax.com>`

```
On 16 Jan, 02:27, Clark F Morris <cfmpub...@ns.sympatico.ca> wrote:
> On Wed, 19 Sep 2007 13:41:23 +1200, "Pete Dashwood"
>
…[44 more quoted lines elided]…
>

A boozy chum of mine has had to support users who enter data on
spreadsheets before feeding the files to the mainframe. The users
frequently changed the layout of the spreadsheets with the result
being that the mainframe crashed. On each occasion he was forced to
change the mainframe to accomodate the changed format. He has even
been forced to debug user spreadsheets for the clients despite the
fact that the IT department did not provide expertise or support for
spreadsheets.

One very worrying point about such spreadsheets are the horror stories
about the errors people make with them.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 7)_

- **From:** Paul Knudsen <pknudsen@NOSPAMyahoo.com>
- **Date:** 2008-01-16T17:34:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n3cto3ttiig9u82f034vddfd0bn5h8bdv2@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net> <9iqqo31fc36tq175r648ij7hdorv5jbskj@4ax.com> <d257ba88-2726-4234-9f79-e60221f4414d@s13g2000prd.googlegroups.com>`

```
On Wed, 16 Jan 2008 13:56:49 -0800 (PST),
Alistair.J.L.Maclean@googlemail.com wrote:

>A boozy chum of mine has had to support users who enter data on
>spreadsheets before feeding the files to the mainframe. The users
…[5 more quoted lines elided]…
>spreadsheets.

Chuckle...  no wonder he is boozy.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 7)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-16T21:01:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qhgto3d5hclb82du9roe7grdknd2kkncqk@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net> <9iqqo31fc36tq175r648ij7hdorv5jbskj@4ax.com> <d257ba88-2726-4234-9f79-e60221f4414d@s13g2000prd.googlegroups.com>`

```
On Wed, 16 Jan 2008 13:56:49 -0800 (PST), Alistair.J.L.Maclean@googlemail.com wrote:


>A boozy chum of mine has had to support users who enter data on
>spreadsheets before feeding the files to the mainframe. The users
>frequently changed the layout of the spreadsheets with the result
>being that the mainframe crashed. On each occasion he was forced to
>change the mainframe to accomodate the changed format. 

That's what XML is for.

I wrote a program that FIGURES OUT the layout of spreadsheets without foreknowledge. It
handled thousands of different formats. You can see the results here. The symbols and
numbers were extracted and normalized from a free-form spreadsheet.
http://finance.yahoo.com/q/hl?s=FMAGX
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 8)_

- **From:** Alistair.J.L.Maclean@googlemail.com
- **Date:** 2008-01-17T07:54:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0e8ce374-cee0-4691-8b06-435cc2c76109@m34g2000hsf.googlegroups.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net> <9iqqo31fc36tq175r648ij7hdorv5jbskj@4ax.com> <d257ba88-2726-4234-9f79-e60221f4414d@s13g2000prd.googlegroups.com> <qhgto3d5hclb82du9roe7grdknd2kkncqk@4ax.com>`

```
On 17 Jan, 03:01, Robert <n...@e.mail> wrote:
> On Wed, 16 Jan 2008 13:56:49 -0800 (PST), Alistair.J.L.Macl...@googlemail.com wrote:
> >A boozy chum of mine has had to support users who enter data on
…[9 more quoted lines elided]…
> numbers were extracted and normalized from a free-form spreadsheet.http://finance.yahoo.com/q/hl?s=FMAGX

Thanks, I will take a look soon. Unfortunately, my boozy chum has
moved on to a better place so he won't be needing it now. Still, it
might come in handy for the future.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 9)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2008-01-17T11:01:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4SLjj.1232$1f.2@bignews9.bellsouth.net>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net> <9iqqo31fc36tq175r648ij7hdorv5jbskj@4ax.com> <d257ba88-2726-4234-9f79-e60221f4414d@s13g2000prd.googlegroups.com> <qhgto3d5hclb82du9roe7grdknd2kkncqk@4ax.com> <0e8ce374-cee0-4691-8b06-435cc2c76109@m34g2000hsf.googlegroups.com>`

```
<Alistair.J.L.Maclean@googlemail.com> wrote:
>
> Thanks, I will take a look soon. Unfortunately, my boozy chum has
> moved on to a better place so he won't be needing it now. Still, it
> might come in handy for the future.

Is "moved on to a better place" literal, or a euphemism for "passed away?"
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 10)_

- **From:** Alistair.J.L.Maclean@googlemail.com
- **Date:** 2008-01-19T04:13:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fd4fc7d-fe1d-449f-a36c-4d46f99a39b0@e6g2000prf.googlegroups.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net> <9iqqo31fc36tq175r648ij7hdorv5jbskj@4ax.com> <d257ba88-2726-4234-9f79-e60221f4414d@s13g2000prd.googlegroups.com> <qhgto3d5hclb82du9roe7grdknd2kkncqk@4ax.com> <0e8ce374-cee0-4691-8b06-435cc2c76109@m34g2000hsf.googlegroups.com> <4SLjj.1232$1f.2@bignews9.bellsouth.net>`

```
On 17 Jan, 17:01, "Judson McClendon" <ju...@sunvaley0.com> wrote:
> <Alistair.J.L.Macl...@googlemail.com> wrote:
>
…[9 more quoted lines elided]…
> whoever believes in Him should not perish but have everlasting life."

Literal. He was made redundant and got a job with a company called
Whistlebrook.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 9)_

- **From:** Alistair.J.L.Maclean@googlemail.com
- **Date:** 2008-01-17T10:15:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ca3a124c-9f63-4499-8a76-d66b4b386ddf@i29g2000prf.googlegroups.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net> <9iqqo31fc36tq175r648ij7hdorv5jbskj@4ax.com> <d257ba88-2726-4234-9f79-e60221f4414d@s13g2000prd.googlegroups.com> <qhgto3d5hclb82du9roe7grdknd2kkncqk@4ax.com> <0e8ce374-cee0-4691-8b06-435cc2c76109@m34g2000hsf.googlegroups.com>`

```
On 17 Jan, 15:54, Alistair.J.L.Macl...@googlemail.com wrote:
> On 17 Jan, 03:01, Robert <n...@e.mail> wrote:
>
…[15 more quoted lines elided]…
> might come in handy for the future.

Looked at it. Very pretty.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 10)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-17T21:07:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pt50p351kikaoh9ee3ra08tpqri1fssmb7@4ax.com>`
- **References:** `<1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <5lbd25F6svobU1@mid.individual.net> <9iqqo31fc36tq175r648ij7hdorv5jbskj@4ax.com> <d257ba88-2726-4234-9f79-e60221f4414d@s13g2000prd.googlegroups.com> <qhgto3d5hclb82du9roe7grdknd2kkncqk@4ax.com> <0e8ce374-cee0-4691-8b06-435cc2c76109@m34g2000hsf.googlegroups.com> <ca3a124c-9f63-4499-8a76-d66b4b386ddf@i29g2000prf.googlegroups.com>`

```
On Thu, 17 Jan 2008 10:15:48 -0800 (PST), Alistair.J.L.Maclean@googlemail.com wrote:

>On 17 Jan, 15:54, Alistair.J.L.Macl...@googlemail.com wrote:
>> On 17 Jan, 03:01, Robert <n...@e.mail> wrote:
…[18 more quoted lines elided]…
>Looked at it. Very pretty.

Yahoo gets credit for the pretty page; my software provided the raw data.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 4)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-09-18T21:49:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13f1000g98mcv3a@corp.supernews.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com>`

```

"Robert" <no@e.mail> wrote in message 
news:lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com...
> On Tue, 18 Sep 2007 08:33:17 -0400, "Charles Hottel" 
> <chottel@earthlink.net> wrote:
…[9 more quoted lines elided]…
> battle the entrenched Cobol culture i.e. resistance to change.

No you are wrong about that.  The majority of the employees are contractors 
making it much easier  for management to hire and fire.  Mnagagement 
definitely controls the shop. What we have now is what the old management 
wanted.  Most of those managers have retired and now the new managers are 
building the shop that they want.  Since they are less technically savy than 
the old managers, at least a part of what they want is based upon what the 
consortium of contractors has advised.
```

###### ↳ ↳ ↳ Re: COBOL and DB2 vs. Java and DB2

_(reply depth: 5)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-19T05:11:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ns1f3traifqg9md7h2qhrpgp6nfapoibp@4ax.com>`
- **References:** `<13ep0krm3102m43@corp.supernews.com> <1190080230.801476.8280@n39g2000hsh.googlegroups.com> <13evham1i75lt1e@corp.supernews.com> <lbq0f35g00rvcfvhlf5glspmnp9p2n07f6@4ax.com> <13f1000g98mcv3a@corp.supernews.com>`

```
On Tue, 18 Sep 2007 21:49:45 -0400, "Charles Hottel" <chottel@earthlink.net> wrote:

>
>"Robert" <no@e.mail> wrote in message 
…[15 more quoted lines elided]…
>making it much easier  for management to hire and fire.

My brothers.

> Management definitely controls the shop.

That's a good thing.

> What we have now is what the old management wanted. 

That's a bad thing.

> Most of those managers have retired and now the new managers are 
>building the shop that they want.  Since they are less technically savy than 
>the old managers, at least a part of what they want is based upon what the 
>consortium of contractors has advised. 

Cynics will denegrate contractor advice as self-interest. I think it's probably good
advice. 

Contractors say dump Cobol and replace it with Java. Why? The reasons are important to us
Cobol people.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
