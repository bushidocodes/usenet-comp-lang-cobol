[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OT (Maybe): ERPs

_93 messages · 15 participants · 2005-01 → 2005-02_

**Topics:** [`Off-topic and spam`](../topics.md#spam)

---

### Re: OT (Maybe): ERPs

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-26T05:06:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com>`

```
On 25 Jan 2005 16:45:22 -0800, "steve.t" <sthompson@ix.netcom.com>
wrote:

>I'm looking for a web site that I think exists that shows all the
>failed whoopie-wow projects. You know, like the attempted Siebel
…[13 more quoted lines elided]…
>months.

With 4,000 customers, HP/Siebel is a small fish in the ERP pond. SAP
has 18,000 customers, Oracle/Peoplesoft/JDE has 14,000, Lawson has
6,000 (guesstimate) and MS/Axapta 5,000. Adding small players such as
BAAN, the total number of ERP customers is about 50,000. 

If EVERY mainframe customer had a failure story on the Web site, the
ratio of success to failure would be 2:1. Using a realistic estimate
of 500 failures, a disproportionate number of them Lawson, the success
ratio is around 100:1.

In case you haven't heard, Oracle's acquisition of Peoplesoft was
completed last week. The price was $10B, which comes to $700K per
customer. Oracle quickly announced a layoff of 5,000 (10%), mostly
from the ranks of its own failed ERP products such as Oracle
Financials. They're keeping >90% of Peoplesoft developers and support
people. The percentage of  Peoplesoft customers already using the
Oracle database was 63%, so the motivation was not database sales; the
cash cow is maintenance. 

I've had lots of hands-on with SAP and Peoplesoft. They're ok but not
great.  Based on what I've read, Microsoft's Axapta is the best of the
ERPs. Many studies have shown that it returns the investment in less
than two years, reduces both total IT budget and clerical costs. Other
ERPs promise that but don't come close to delivering.
```

#### ↳ Re: OT (Maybe): ERPs

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-01-26T15:46:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ct8e37$rmf$1@peabody.colorado.edu>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com>`

```

On 25-Jan-2005, Robert Wagner <spamblocker-robert@wagner.net> wrote:

> In case you haven't heard, Oracle's acquisition of Peoplesoft was
> completed last week. The price was $10B, which comes to $700K per
…[5 more quoted lines elided]…
> cash cow is maintenance.

Apparently Oracle isn't interested hardly at all in the J.D. Edwards portion.
```

##### ↳ ↳ Re: OT (Maybe): ERPs

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-26T18:09:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k6mfv0lqin02ojms3vvhd5s5evo6svk77o@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <ct8e37$rmf$1@peabody.colorado.edu>`

```
On Wed, 26 Jan 2005 15:46:15 GMT, "Howard Brazee" <howard@brazee.net>
wrote:

>On 25-Jan-2005, Robert Wagner <spamblocker-robert@wagner.net> wrote:
>
…[9 more quoted lines elided]…
>Apparently Oracle isn't interested hardly at all in the J.D. Edwards portion.

Yes they are. The former JDE suite, now  Peoplesoft World , is
marketed to low-end customers -- medium sized businesses who cannot
afford to spend millions on consultants. It's often sold stripped down
and pre-configured for rapid startup. SAP has a similar offering
called AcceleratedSAP (ASAP). 

I worked in the same building with an ASAP customer featured on
billboards, and shared smoke-break discussions with the IT manager. He
said installation was painless, conversion from the old in-house
system  easy (with Oracle assistance). They got it up in less than six
months. His users complained about missing features such as inability
to make partial shipments; if one item is out of stock, the whole
order is held up. Sounds to me like a configuration option (to save on
freight), but I don't know.
```

#### ↳ Re: OT (Maybe): ERPs

- **From:** "steve.t" <sthompson@ix.netcom.com>
- **Date:** 2005-01-26T12:21:11-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106770871.029233.48300@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com>`

```
Define success.
* Is it the actual implementation and users using the new system?
* Is it that the end users actually like the new system and its
functioning?
* Is it that the DR/Plan can be tested and things work at the DR site?

Or, in the case of a certain Electric Utility (those folks that are
said to have brought you the NE power outage) is it that upper
management declared the new system to be a success regardless of what
the end users were complaining about?

The problem boils down to not being able to do all of the I/Os needed
for an application system. When you have to have one system running the
database, another running the web server, yet another running the
applications and they all have to communicate across the same network,
what do you think happens next? Add to this all the I/O that must be
done by each of those "hosts" for system servicing, and local file
processing.

Take any mainframe (Honeywell, IBM, Unisys, etc.) and look at how they
are able to run all of those functions within the same box. The
critical interprocess communications I/O is done within memory at
memory access speeds. The only physical I/O that needs be done in this
case is local file servcie I/O, data base I/O, O/S and communications
I/O with/to the end users. And all of those are basically done with
TRUE Parallel processes.
To that end me thinks your statistics are very skewed.

Steve.T
```

##### ↳ ↳ Re: OT (Maybe): ERPs

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-26T23:13:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com>`

```
On 26 Jan 2005 12:21:11 -0800, "steve.t" <sthompson@ix.netcom.com>
wrote:

>Define success.
>* Is it the actual implementation and users using the new system?
>* Is it that the end users actually like the new system and its
>functioning?
>* Is it that the DR/Plan can be tested and things work at the DR site?

It was just a customer count. No doubt a small percentage bought the
thing and never installed it. A comparable  small percentage of
mainframes are gathering dust. Neither alters the macroscopic fact
that there are more ERP customers than mainframe customers (the number
of shops/installations would be larger for both).

>Or, in the case of a certain Electric Utility (those folks that are
>said to have brought you the NE power outage) is it that upper
>management declared the new system to be a success regardless of what
>the end users were complaining about?

That's been happening in mainframe shops for 40+ years. Technology
doesn't change human nature.

>The problem boils down to not being able to do all of the I/Os needed
>for an application system. When you have to have one system running the
…[4 more quoted lines elided]…
>processing.

Mainframes also have to transport data from disk drive to CPU memory.
IBM's ESCON, which runs at 200mb/s, is slower than 2gb/s Fibre Channel
and 1.3gb/s SCSI-3.

>Take any mainframe (Honeywell, IBM, Unisys, etc.)

Honeywell stopped making or selling computers in 1991. 

> and look at how they
>are able to run all of those functions within the same box. The
…[4 more quoted lines elided]…
>TRUE Parallel processes.

Unix and Windows boxes also have multiple CPUs and pass data between
them at memory speed. Google on IPC (InterProcess Communication). 

To evaluate OLTP thruput, for example, a top-down measurement of
actual performance is more informative than bottom-up hand waving
about channel speed and the like. When Unix systems are configured by
professionals, as opposed to non-technical management, they deliver
about the same performance as mainframes for a fraction of the cost. 

Benchmark speed and cost per transaction data is publically available
for hundreds of platforms. Why are mainframes conspicuously absent?
Because they can't compete on cost.

>To that end me thinks your statistics are very skewed.

Kindly supply corrected statistics on number of ERP and mainframe
customers, or shops, or users. 

While you're at it, explain why most mainframe growth in the last ten
years involved Linux and Web serving .. both ideas borrowed from other
cultures.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

- **From:** "steve.t" <sthompson@ix.netcom.com>
- **Date:** 2005-01-26T20:19:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106799583.186458.156030@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com>`

```
Robert:

Define success rather than deflecting.

Next, if you want to argue architecture, I'm ready. Be forwarned that I
have other than mainframes in my tool box and that I actually have
written microcode.

Come to think of it, didn't you kinda get into this with me about 2
years ago when I was too busy to engage you in your drivel? But then,
what with me being in the industry for over 30 years, maybe I'm having
another of those senior moments.

Steve.T
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 4)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-27T08:01:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com>`

```
On 26 Jan 2005 20:19:43 -0800, "steve.t" <sthompson@ix.netcom.com>
wrote:

>Robert:
>
>Define success rather than deflecting.

A successful platform conversion is one where the organization ceases
being a user of the old platform, for the application(s) in question,
and becomes a 'permanent' user of the new platform.

It's not my definition; it comes from the worlds of investment and
marketing.

>Next, if you want to argue architecture, I'm ready. Be forwarned that I
>have other than mainframes in my tool box and that I actually have
>written microcode.

Your arguments for the superiority of mainframes are bottom-up. The
business world cited above looks at it top-down.

For instance, you think mainframes are 'inherently superior' for OLTP
because of channel design and operating system architecture. The
decision-making executive says, 'Don't tell me about technical
details. Run the same transactions through both, then tell me response
times and cost per transaction.' When the mainframe loses, you'll
claim the other side cheated by using a larger than normal cache or by
locking programs in memory. You'll be incapible of disengaging
bottom-up, incapible of thinking like the executive.

>Come to think of it, didn't you kinda get into this with me about 2
>years ago when I was too busy to engage you in your drivel? 

I don't recall but it's likely that happened.

>But then,
>what with me being in the industry for over 30 years, maybe I'm having
>another of those senior moments.

If longevity were the only criterion, I'd win. 

Lessons learned 30 years ago, when hardware was expensive, no longer
apply in today's world of cheap hardware. Worse, insisting on their
application can be counter-productive. Calcified thinking is WHY they
retire old farts. (Present company excluded, of course.)
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 5)_

- **From:** "steve.t" <sthompson@ix.netcom.com>
- **Date:** 2005-01-27T08:20:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106842807.711642.135610@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com>`

```
Again, as so many others have pointed out, you assume things. I am not
a mainframe bigot, and when on a mainframe, I'm not an MVS bigot. I
actually enjoy a good VM/CMS environment, and can operate rather well
under VSE (because I was a VSE sysprog at one time?).

For instance, in our facilities here, where I make the decisions as to
what hardware, O/S, etc, we run all Intel based systems. We are
currently running NT 4.0 workstations because they do the job. We see
no reason to migrate to anything Micro$**t offers. As a result, we are
going to migrate to Linux as soon as we solve certain of our backup
issues. Sun Office does everything we need, so good riddance to
MS/Office. BTW - we could be running MVS, DOS or VM if I so chose.

When you discuss OLTP tests you do realize that there is more to it
than just running a screen write/read and grab a line from a table. So
when the computations are done for cost per transaction, the models
given do not necessarily meet what a business actually does. All they
do is tell us what a specific configuration can do with a standard
test. It gives us the ability to compare apples to apples, sort of.

Can you, Mr. Wagner, tell me how fast an Itanium can process 5TB of
data v. a S/390 ESA system running OS/390 V2R10? Which one will finish
first? When is a MIP not a MIP? Yet this is the kind of comparision
that is attempted with OLTP numbers. Assuming that the one machine has
8 CPUs and 2GB of memory, can it also be doing a large amount of batch
oriented processing at the same time and still achieve its OLTP numbers
(and I was actually thinking of a Regatta runing AIX5L)?

Success of a migration/implementation: That an entity is up on the new
platform and the old one is gone does not a successful migration make.
When 30% of your people are unable to do their job adequately because
the new system can't produce a report you need in a reasonable time...
When companies are seeing Cxx being hauled off in chains...

So some years ago when someone told me that they wanted to migrate a
whole system from MVS to S/36 I thought they'd lost their marbles.
Turns out that what they wanted to do could easily be done by that S/36
*BECAUSE* the amount of data to be handled was within the capabilities
of that system. Everything was done in RPGII.

Years earlier I worked for Digital Systems Corp (not to be confused
with DEC). We had an ASCII based S/3 type machine. We could migrate
whole S/3 15D environments onto this box and use less floor space and
power. We used all dumb terminals and could still blow the doors of the
IBM box. Come to think of it, we even migrated a S/370 off to one of
the G/5 systems and they were able to do everything they had done
before in less time. Everything was done in either RPGII or their
assembly language.

I have migrated whole accounting systems off to NT from mainframe. It
worked because the amount of data to be processed was within the
capablilities of the design and equipment. However, I explained, and it
was accepted, what their growth path was and how they would know when
they got there. The amount of transactions to be processed per hour was
key. All the programming was being done in COBOL.

In these three cases it was far cheaper to go to the non-mainframe
platform. In the latter case, it was cheaper to use an NT 4.0 Server
than it was to use the smallest AS/400 (available at that time).

However, in my experience, when you start approaching the US$1.2M cost
for a processor, the cost per transaction starts to favor the mainframe
just on the basis of the hardware. When you get to where the
applications need 4 servers and the database needs 4 servers, then the
software costs start favoring a mainframe running Linux.

Now let us back up many years. Since you are older than me, and an old
fart (your definition), why did IBM, RCA, Honeywell, GE, Univac, NCR
and Burroughs select the internal architectures that they did (I refer
to Ibank/Dbank, memory v. bus centric, single I/O path v. multiple
channel processors, etc.)? And who ultimately won the battles and why?
Frankly, from what I know and remember, Burroughs should have beaten
IBM and the others to a pulp. But they didn't.

Why did all the other computer makers that got into this around
1977-1980 decide on bus centric and segmented memory? Why did they have
to change to the way mainframes looked at memory?

So why is it that all the makers of computer systems today are trying
to tell us that they are doing xxxx "which is very much like a
mainframe?"

If what you implied (calcified thinking) should be thrown out, why is
it then, that when I lived in SillyCone valley, did people I knew
working for an Intel based mother board maker come to me (and I'm no
great engineer) to ask how to get two CPUs to work together? Why did
things get changed about the processors to allow them to do interlocked
updates? Why are all these server manufacturers (regardless of who
makes the chip sets) working at doing the things that the S/390
architected machines were based on? And who had 64bit addressing
functioning and available first? [You might be surprised.]

And so when I point out that going from a mainframe to xxx will be a
mistake, do you think I do it lightly? And when I tell someone that we
can migrate your application off the mainframe to xxxx do you think I
do that without serious forethought?

Why do you think I do modeling to determine if the design can handle
the workload being placed on it? It's the same old calcified routines
that I used to determine if a mainframe system could handle the
workload.

Could my calcified thinking be why EVERYONE of the migrations I've done
have not only worked, but performed without having to throw more and
more resources at it?

I think we are done here.

Steve.T
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 6)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-28T03:39:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ae5jv0llfsqllivid0ogod8bohpp98odmv@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <1106842807.711642.135610@z14g2000cwz.googlegroups.com>`

```
On 27 Jan 2005 08:20:07 -0800, "steve.t" <sthompson@ix.netcom.com>
wrote:

>For instance, in our facilities here, where I make the decisions as to
>what hardware, O/S, etc, we run all Intel based systems. We are
>currently running NT 4.0 workstations because they do the job. 

"Do the job" is as amorphous as "successful". A rock can do the job of
a hammer.

>We see no reason to migrate to anything Micro$**t offers. 

No sign of bias there.

>As a result, we are
>going to migrate to Linux as soon as we solve certain of our backup
>issues. Sun Office does everything we need, so good riddance to
>MS/Office. 

Quoting from the Wine Web site:

"The dependency is not so much on Microsoft Windows as it is on
Windows applications. Boxed off-the-shelf applications, games,
in-house applications, vertical market applications, are what prevents
users, companies and governments from switching to another operating
system. Even if 90% of the needs of most users are taken care of if
you can provide them with an office suite, an email client, a browser,
and a media player, then there will still be a remaining 10% of their
needs, potentially critical needs, that are not met. Unfortunately
these remaining 10% are spread across a wide spectrum of applications:
thousands of applications running the gamut from games to specialized
accounting software for French farms, via Italian encyclopedias,
German tax software, child education software, banking software,
in-house software representing years of development, etc. It is the
availability of all this software that makes Windows so compelling and
its monopoly so strong. No platform will become mainstream unless it
runs a significant portion of that software and lets individuals,
companies and governments preserve their investments in that
software."
http://www.winehq.com/site/why

Lacking Wine or equivalent, you've locked your users into in-house
developed software. That's what most IT administrators want, but is
not what users want.

>When you discuss OLTP tests you do realize that there is more to it
>than just running a screen write/read and grab a line from a table. So
…[3 more quoted lines elided]…
>test. It gives us the ability to compare apples to apples, sort of.

The benchmarks are designed to model 'typical' applications. They do
more than a screen write/read followed by grab a line.

"TPC benchmarks also differ from other benchmarks in that TPC
benchmarks are modeled after actual production applications and
environments rather than stand-alone computer tests which may not
evaluate key performance factors like user interface, communications,
disk I/Os, data storage, and backup and recovery. 

The most frequent transaction consists of entering a new order which,
on average, is comprised of ten different items. Each warehouse tries
to maintain stock for the 100,000 items in the Company's catalog and
fill orders from that stock. However, in reality, one warehouse will
probably not have all the parts required to fill every order.
Therefore, TPC-C requires that close to ten percent of all orders must
be supplied by another warehouse of the Company. Another frequent
transaction consists in recording a payment received from a customer.
Less frequently, operators will request the status of a previously
placed order, process a batch of ten orders for delivery, or query the
system for potential supply shortages by examining the level of stock
at the local warehouse. A total of five types of transactions, then,
are used to model this business activity."
http://www.tpc.org/tpcc/detail.asp

>Can you, Mr. Wagner, tell me how fast an Itanium can process 5TB of
>data v. a S/390 ESA system running OS/390 V2R10? Which one will finish
>first? When is a MIP not a MIP? Yet this is the kind of comparision
>that is attempted with OLTP numbers.

The important question, from a management point of view, is how much
it costs to process all the company's transactions.

>Assuming that the one machine has
>8 CPUs and 2GB of memory, can it also be doing a large amount of batch
>oriented processing at the same time and still achieve its OLTP numbers
>(and I was actually thinking of a Regatta runing AIX5L)?

Here you're referring to Total Cost of Ownership. Since most costs are
labor rather than hardware/software, TCO is impossible to measure with
a benchmark. It's a function of management and organization. At first
glance, a centralized mainframe would have the advantage over hundreds
to thousands of decentralized servers. The issue of centralized vs.
decentralized has been examined extensively in the literature of
business. One concern, for example, is acquisitions and spin-offs.
Companaies that are centralized find it difficult to digest an
acquisition and nearly impossible to spin-off a division.

>Success of a migration/implementation: That an entity is up on the new
>platform and the old one is gone does not a successful migration make.
>When 30% of your people are unable to do their job adequately because
>the new system can't produce a report you need in a reasonable time...
>When companies are seeing Cxx being hauled off in chains...

F.U.D.

>Now let us back up many years. Since you are older than me, and an old
>fart (your definition), why did IBM, RCA, Honeywell, GE, Univac, NCR
…[4 more quoted lines elided]…
>IBM and the others to a pulp. But they didn't.

I worked extensively on and for Burroughs, Honeywell and RCA. Techie
wisdom at the time held that IBM won because of better marketing;
hardware had nothing to do with it. Personally, I LOVED the CII/Bull
machines marketed by Honeywell as Level-6x. They failed in the US
because few people knew they existed.

>Why did all the other computer makers that got into this around
>1977-1980 decide on bus centric and segmented memory? Why did they have
…[4 more quoted lines elided]…
>mainframe?"

Marketing? Surely not envy.

>If what you implied (calcified thinking) should be thrown out, why is
>it then, that when I lived in SillyCone valley, did people I knew
…[3 more quoted lines elided]…
>updates?

The answer is SMP. But that doesn't address the basic problem of how
to give applications parallelism. They'll be single-threaded so long
as the programming language assumes it's running on a Von Neumann
machine. Some back-door approaches to parallelism are AI, OO and
database.

>And who had 64bit addressing
>functioning and available first? [You might be surprised.]

Apple, running a PowerPC made by IBM?

>Why do you think I do modeling to determine if the design can handle
>the workload being placed on it? It's the same old calcified routines
>that I used to determine if a mainframe system could handle the
>workload.

I had experience with simulations working for Comress on SCERT. It
cost a fortune and didn't work very well. The fallacy, in my opinion,
was trying to solve top-down problems with a bottom-up model. Given
that it didn't work on single-task processors with minimal I/O
parallelism, the same approach doesn't stand a chance in today's
environment. I think benchmarks are the way to go.

>Could my calcified thinking be why EVERYONE of the migrations I've done
>have not only worked, but performed without having to throw more and
>more resources at it?

Congratulations. Did your plan deal with organization of support
staff, or was it only about hardware and software?
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 7)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-27T20:51:39-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106887899.311813.128520@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<ae5jv0llfsqllivid0ogod8bohpp98odmv@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <1106842807.711642.135610@z14g2000cwz.googlegroups.com> <ae5jv0llfsqllivid0ogod8bohpp98odmv@4ax.com>`

```
> Lacking Wine or equivalent, you've locked your users into in-house
> developed software.

Oh yeah, I had forgotten that Linux needed to use WINE to run Windows
based Browsers, Word Processors, Spreadsheets, and even simple editors
because there are no programs at all that run on Unix/Linux.  ... and
Bill Gates invented the Internet and MicroComputers.

> F.U.D.

Interestingly you claim this, but failed to notice your own FUDding.

> accounting software for French farms, via Italian encyclopedias,
> German tax software, child education software,

Those are _really_ good reasons for _me_ to keep Windows.

Now all you have to do is come up with a list of software that
steve.t's company might _actually_ care about, because I don't think it
is a French farm or a child educator.

Actually I remember school software was best served by BBC computers.
These BBCs were used as lab instruments (as well as the usual range of
class software) - I still have some.  Then MS convinced schools that
PCs should be used to train students as MS consumers.

> banking software,

Most banking software is on mainframes or Unix.

But what is your actual point ?

> That's what most IT administrators want, but is not what users want.

What is important is what the _Company_ wants.  The users probably want
to play games and send each other EMails with pictures of tennis stars.

>> And who had 64bit addressing
>> functioning and available first? [You might be surprised.]
> Apple, running a PowerPC made by IBM?

MIPS R4000 ?
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 8)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-28T08:36:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nutjv093r3d1dd35ikaidadar65b5sefp4@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <1106842807.711642.135610@z14g2000cwz.googlegroups.com> <ae5jv0llfsqllivid0ogod8bohpp98odmv@4ax.com> <1106887899.311813.128520@f14g2000cwb.googlegroups.com>`

```
On 27 Jan 2005 20:51:39 -0800, "Richard" <riplin@Azonic.co.nz> wrote:

>Now all you have to do is come up with a list of software that
>steve.t's company might _actually_ care about, because I don't think it
…[6 more quoted lines elided]…
>But what is your actual point ?

My point is that 95% (according to the Wine site) of shrink-wrap
software runs on Windows.

>>> And who had 64bit addressing
>>> functioning and available first? [You might be surprised.]
>> Apple, running a PowerPC made by IBM?
>
>MIPS R4000 ?

Good answer. It appears to be right.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 9)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-28T02:02:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106905799.233525.306940@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<nutjv093r3d1dd35ikaidadar65b5sefp4@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <1106842807.711642.135610@z14g2000cwz.googlegroups.com> <ae5jv0llfsqllivid0ogod8bohpp98odmv@4ax.com> <1106887899.311813.128520@f14g2000cwb.googlegroups.com> <nutjv093r3d1dd35ikaidadar65b5sefp4@4ax.com>`

```
> My point is that 95% (according to the Wine site) of
> shrink-wrap software runs on Windows.

99% of which is a waste of time.

Your comment would only be relevant to the actual shrink-wrap software
that was required by the business.  Given that most shrink wrap is
aimed at games and entertainment with a tiny amount at home and soho,
it isn't a loss to corporates.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 9)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-29T13:36:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107034604.112296.268610@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<nutjv093r3d1dd35ikaidadar65b5sefp4@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <1106842807.711642.135610@z14g2000cwz.googlegroups.com> <ae5jv0llfsqllivid0ogod8bohpp98odmv@4ax.com> <1106887899.311813.128520@f14g2000cwb.googlegroups.com> <nutjv093r3d1dd35ikaidadar65b5sefp4@4ax.com>`

```
> My point is that 95% of shrink-wrap software runs on Windows.

'Shrink-wrap' is the 'old' way of distributing software, very 80s.  Of
course most of it is Windows, before that it was DOS, before that CP/M.
Very little Unix or mainframe software was ever 'shrink wrap'.  Linux
does not use that distribution method (or not much), there are other
ways of distribution.

OTOH a quick survey shows about a third to be 'PS/2' and does not run
on Windows.  ;-)
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 10)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-30T04:57:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<espov0ldeik60l828mooh9ou9n4ehr0u69@4ax.com>`
- **References:** `<1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <1106842807.711642.135610@z14g2000cwz.googlegroups.com> <ae5jv0llfsqllivid0ogod8bohpp98odmv@4ax.com> <1106887899.311813.128520@f14g2000cwb.googlegroups.com> <nutjv093r3d1dd35ikaidadar65b5sefp4@4ax.com> <1107034604.112296.268610@c13g2000cwb.googlegroups.com>`

```
On 29 Jan 2005 13:36:44 -0800, "Richard" <riplin@Azonic.co.nz> wrote:

>> My point is that 95% of shrink-wrap software runs on Windows.
>
>'Shrink-wrap' is the 'old' way of distributing software, very 80s.  

I use 'shrink-wrap' to mean commercial packaged software sold retail
to a single end-user, installed with minimal configuration. It
includes packages distributed by mail order and download, excludes
open source and shareware because they're non-commercial.

I'm surprised at how much IS sold the old way. Last week my smallish
local Wal-Mart had a display with 500 copies of TurboTax.

>OTOH a quick survey shows about a third to be 'PS/2' and does not run
>on Windows.  ;-)

Yes, they do. There are good free emulators for PlayStation 2, XBox,
Atari, Nintendo and every other game box. 

More interesting, there are emulators running _on the XBox_  for every
game machine made, including a DOS PC. The XBox can do Samba shares
with Unix, and it can mount a console on Windows or Linux/KDE. Of
historic interest, it can emulate a Commodore 64. Apple ][, PET,
Amiga, Vic-20, etc. These emulators are developed on Windows, then
easily ported to the XBox.

If you think these machines are toys, consider this. It is illegal to
export 'supercomputers' from the US to certain countries, which
include India and China. When the PS2 came out in 2000, the threshold
for supercomputer was 2 gflops. The PS2 ran at 6.4 gflops. So they
raised the bar to 7, then 28. In 2001, it was raised to 85; in 2002,
to 195. I don't know where it stands now, on a guess 800. For
comparison, a typical Intel desktop runs 5 gflops, as does an IBM
mainframe, per processor. The fastest single processor today is an
Apple G5, which runs 15 gflops. High-end video cards go up to 40,
using multiple processors. When the PS3 is released later this year
(development machines are already in use), its rumored speed will be
1,000 gflops! If you want the speed of a mainframe with 200 CPUs,
don't call IBM, visit the 'toy' department at Wal-Mart. 

You'll be pleased to know XBox, PS2 and PS3 are already running Linux.
A home computer based on XBox with a big disk, high speed networking
and no Microsoft code can be built today for less than $500. Using
Wine, it can run Windows programs.

http://news.zdnet.com/2100-9584_22-948493.html?tag=nl
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 8)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-01-28T20:41:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Pi8NA1PflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <ae5jv0llfsqllivid0ogod8bohpp98odmv@4ax.com> <1106887899.311813.128520@f14g2000cwb.googlegroups.com>`

```
.    On  27.01.05
  wrote  riplin@Azonic.co.nz (Richard)
     on  /COMP/LANG/COBOL
     in  1106887899.311813.128520@f14g2000cwb.googlegroups.com
  about  Re: OT (Maybe): ERPs


>> accounting software for French farms, via Italian encyclopedias,
>> German tax software, child education software,

r> Those are _really_ good reasons for _me_ to keep Windows.

   German tax software is important for _me._

   The problem is, Elster, the ready-made software handed out free by  
the German tax office, for submitting tax declarations online, is  
available only or windows. There is a module for Java, which can be  
used by other software vendors to build similar functions into their  
own accounting software, but that has to be done first.

   I don't like this restriction, but I have to live with it.


>> banking software,

r> Most banking software is on mainframes or Unix.

   I thought that Robert W. talked about the software used to manage  
my bank account myself and communicate online with 'my' bank --  
getting statements and submitting transfer orders.

   I don't know if such software exists for Linux, and how good it is.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Man stattete ihm sehr heiï¿½en, schon etwas verbrannten Dank ab. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 9)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-28T16:20:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106958003.417437.75500@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<9Pi8NA1PflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <ae5jv0llfsqllivid0ogod8bohpp98odmv@4ax.com> <1106887899.311813.128520@f14g2000cwb.googlegroups.com> <9Pi8NA1PflB@jpberlin-l.willms.jpberlin.de>`

```
> for submitting tax declarations online, is available only or windows.

I would assume that it is not compulsory to submit on-line as that
would be discriminatory against people who do not have a computer at
all, let alone having to compulsory purchase a particular (alien)
vendors products.

>> banking software,

r>> Most banking software is on mainframes or Unix.

> I thought that Robert W. talked about the software used to
> manage my bank account myself and communicate online
> with 'my' bank --  getting statements and submitting transfer
> orders.

RW is infamous for adding 'I meants' when shown to be wrong.

> I don't know if such software exists for Linux, and how good
> it is.

Well, with _my_ Banks, I just use Mozilla on Mandrake Linux without any
problem.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 10)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2005-01-28T19:52:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<67BKd.10689$Yg6.1647409@news20.bellglobal.com>`
- **In-Reply-To:** `<1106958003.417437.75500@z14g2000cwz.googlegroups.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <ae5jv0llfsqllivid0ogod8bohpp98odmv@4ax.com> <1106887899.311813.128520@f14g2000cwb.googlegroups.com> <9Pi8NA1PflB@jpberlin-l.willms.jpberlin.de> <1106958003.417437.75500@z14g2000cwz.googlegroups.com>`

```
Richard wrote:
>>for submitting tax declarations online, is available only or windows.
> 
…[28 more quoted lines elided]…
> 

Yes, me too. I never go on the net on a Windows machine. They are too 
mission critical for me to risk net access, and Linux has far better 
browsers. If someone sends me a file that I need on a windows machine, I 
simply drag and drop it from mozzilla into a desktop folder for the 
approriate windows box, and it appears on that machine's desktop 
magically. But that is done by me, personally, after I have seen the 
mail, and looked at the attachment. Inside my firewall.

Donald
```

###### ↳ ↳ ↳ Online Tax and Banking (was: OT (Maybe): ERPs)

_(reply depth: 10)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-01-29T09:11:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9PmD5BjuflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <9Pi8NA1PflB@jpberlin-l.willms.jpberlin.de> <1106958003.417437.75500@z14g2000cwz.googlegroups.com>`

```
.    On  28.01.05
  wrote  riplin@Azonic.co.nz (Richard)
     on  /COMP/LANG/COBOL
     in  1106958003.417437.75500@z14g2000cwz.googlegroups.com
  about  Re: OT (Maybe): ERPs


>> for submitting tax declarations online, is available only or windows.

r> I would assume that it is not compulsory to submit on-line as that
r> would be discriminatory against people who do not have a computer at
r> all, let alone having to compulsory purchase a particular (alien)
r> vendors products.

   The annual income tax declaration can also be submitted on paper,  
but the VAT advance notice, which businesses have to submit monthly,  
has to be done online beginning this month. Very small businesses who  
do not have a computer at all, may be exempted.

>>> banking software,

r>>> Most banking software is on mainframes or Unix.

>> I thought that Robert W. talked about the software used to
>> manage my bank account myself and communicate online
>> with 'my' bank --  getting statements and submitting transfer
>> orders.

r> RW is infamous for adding 'I meants' when shown to be wrong.

>> I don't know if such software exists for Linux, and how good
>> it is.

r> Well, with _my_ Banks, I just use Mozilla on Mandrake Linux without
r> any problem.

  Sure, that can be done interactively, too, where the forms and  
processing logic is provided by the bank. But I'm talking about actual  
software, which runs on _my_ computer, and which communicates with the  
bank not via online forms made for interactive use, but by its own  
protocol, program to program, not human to remote computer.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Er liebte hauptsï¿½chlich die Wï¿½rter, die nicht in Wï¿½rterbï¿½chern vorzukommen pflegen. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 9)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-29T06:55:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1l7mv0dvjca77bpplm1g9d7ev4elcn4fie@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <ae5jv0llfsqllivid0ogod8bohpp98odmv@4ax.com> <1106887899.311813.128520@f14g2000cwb.googlegroups.com> <9Pi8NA1PflB@jpberlin-l.willms.jpberlin.de>`

```
On 28 Jan 2005 20:41:00 GMT, l.willms@jpberlin.de (Lueko Willms)
wrote:


>>> banking software,
>
…[6 more quoted lines elided]…
>   I don't know if such software exists for Linux, and how good it is.

I've been doing online banking, via CheckFree, for 15 years. All you
need is a Web browser. It complains about Mozilla being unsupported,
but works fine.

I think 'banking software' was a reference to back office processing,
not the customer interface.
```

###### ↳ ↳ ↳ Online Tax and Banking (was: OT (Maybe): ERPs)

_(reply depth: 10)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-01-29T09:12:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9PmD5OvuflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <9Pi8NA1PflB@jpberlin-l.willms.jpberlin.de> <1l7mv0dvjca77bpplm1g9d7ev4elcn4fie@4ax.com>`

```
.    On  29.01.05
  wrote  spamblocker-robert@wagner.net (Robert Wagner)
     on  /COMP/LANG/COBOL
     in  1l7mv0dvjca77bpplm1g9d7ev4elcn4fie@4ax.com
  about  Re: OT (Maybe): ERPs


RW> I think 'banking software' was a reference to back office processing,
RW> not the customer interface.

   No, what the bank runs on its computers would be "bank software";  
I'm actually referring the software which runs on _my_ computer and  
which administers my accounts with various banks. The interactive work  
is done with _my_ program, not the bank's one. My banking program then  
'talks' to the bank's software, getting statements and submitting  
transfer orders.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Vorstellungen sind auch ein Leben und eine Welt. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: Online Tax and Banking (was: OT (Maybe): ERPs)

_(reply depth: 11)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-29T13:53:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e95nv0llntd3jdprokgfmpdjdfdp21usht@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <9Pi8NA1PflB@jpberlin-l.willms.jpberlin.de> <1l7mv0dvjca77bpplm1g9d7ev4elcn4fie@4ax.com> <9PmD5OvuflB@jpberlin-l.willms.jpberlin.de>`

```
On 29 Jan 2005 09:12:00 GMT, l.willms@jpberlin.de (Lueko Willms)
wrote:

>.    On  29.01.05
>  wrote  spamblocker-robert@wagner.net (Robert Wagner)
…[13 more quoted lines elided]…
>transfer orders.

In the US, there is a Standard format for bank-to-bank transactions,
called ACH, but there is no standard for customer-to-bank. Some banks
have invented their own and provided their customers with proprietary
software. Because there is no standard, a single program cannot talk
to multiple banks. 

A key concept is "origination". Customers are not permitted to
originate a transaction (cash transfer to another bank or another
customer's account); only banks can do that. Why? If customers could
pay their bills by originating ACH transfers, banks would become
clearing houses and FLOAT would disappear. It's all about protecting
float.

Online bill-pay gives the illusion of electronic funds transfer, but
there is actually a delay between withdrawal and deposit.
```

###### ↳ ↳ ↳ Re: Online Tax and Banking

_(reply depth: 12)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-01-29T17:03:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9PmG5Z$eflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <9PmD5OvuflB@jpberlin-l.willms.jpberlin.de> <e95nv0llntd3jdprokgfmpdjdfdp21usht@4ax.com>`

```
.    On  29.01.05
  wrote  spamblocker-robert@wagner.net (Robert Wagner)
     on  /COMP/LANG/COBOL
     in  e95nv0llntd3jdprokgfmpdjdfdp21usht@4ax.com
  about  Re: Online Tax and Banking (was: OT (Maybe): ERPs)


RW> In the US,

   they still pay with cheques ... I know.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Ein Buch ist ein Spiegel, wenn ein Affe hineinsieht, so kann kein Apostel herausgucken. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: Online Tax and Banking

_(reply depth: 13)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-29T22:58:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k14ov0hj9out6m025ck2kjig1v5eqvbosq@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <9PmD5OvuflB@jpberlin-l.willms.jpberlin.de> <e95nv0llntd3jdprokgfmpdjdfdp21usht@4ax.com> <9PmG5Z$eflB@jpberlin-l.willms.jpberlin.de>`

```
On 29 Jan 2005 17:03:00 GMT, l.willms@jpberlin.de (Lueko Willms)
wrote:

>.    On  29.01.05
>  wrote  spamblocker-robert@wagner.net (Robert Wagner)
…[7 more quoted lines elided]…
>   they still pay with cheques ... I know.

Every checking account comes with a free debit card, free internet
queries and internet bill-pay that's either free or very inexpensive
($5/mo). Every supermarket checkout lane has a debit/credit card
reader, plus there's an ATM in front of the store. 

Yet, fat ladies CONTINUE holding up the line writing checks  (and
asking the clerk for today's date). I don't know why stores put up
with it. Some stores (Wal-Mart for one) have even installed check
scanners. The clerk grabs the blank check if possible, scans it to get
the account number, the computer does an ACH transfer out of the
customer's account like a debit card would, the clerk returns the
blank check saying 'It's paid. Don't forget to enter this check in
your journal.' The customer looks dumbfounded. I couldn't believe it
the first time I saw that.
```

###### ↳ ↳ ↳ Re: Online Tax and Banking (was: OT (Maybe): ERPs)

_(reply depth: 11)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-29T11:30:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107027048.388343.260770@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<9PmD5OvuflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <9Pi8NA1PflB@jpberlin-l.willms.jpberlin.de> <1l7mv0dvjca77bpplm1g9d7ev4elcn4fie@4ax.com> <9PmD5OvuflB@jpberlin-l.willms.jpberlin.de>`

```
> The interactive work is done with _my_ program,

That would come under Robert's """you've locked your users into
in-house developed software. """ then.   ;-)
```

###### ↳ ↳ ↳ Re: Online Tax and Banking

_(reply depth: 12)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-01-29T23:11:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9PqHnlluflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <9PmD5OvuflB@jpberlin-l.willms.jpberlin.de> <1107027048.388343.260770@z14g2000cwz.googlegroups.com>`

```
.     Am  29.01.05
 schrieb  riplin@Azonic.co.nz (Richard)
     bei  /COMP/LANG/COBOL
      in  1107027048.388343.260770@z14g2000cwz.googlegroups.com
   ueber  Re: Online Tax and Banking (was: OT (Maybe): ERPs)

>> The interactive work is done with _my_ program,

r> That would come under Robert's """you've locked your users into
r> in-house developed software. """ then.   ;-)

  "my" program not in the sense that _I_ have developed it, but the  
program which runs on _my_ computer, keeping a database of accounts,  
local users, recipients, periodical payments, and what have you.

  The program which I use (SFIRM32) is distributed by the savings  
banks organization, but there are other programs available.


Yours,
Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

"Regierung aus dem Volke, durch das Volk und fï¿½r das Volk"
   - Abraham Lincoln, Ansprache in Gettysburg, 19.11.1863
"... was in die revolutionï¿½re Sprache von heute ï¿½bersetzt heiï¿½t:
eine Regierung von Arbeitern, durch Arbeiter und fï¿½r Arbeiter"
                                  - Fidel Castro, November 1994
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 9)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-01-30T19:58:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fhgLd.23232$8j3.2389@fe40.usenetserver.com>`
- **In-Reply-To:** `<9Pi8NA1PflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <ae5jv0llfsqllivid0ogod8bohpp98odmv@4ax.com> <1106887899.311813.128520@f14g2000cwb.googlegroups.com> <9Pi8NA1PflB@jpberlin-l.willms.jpberlin.de>`

```
Lueko Willms wrote:
> 
>    The problem is, Elster, the ready-made software handed out free by  
…[3 more quoted lines elided]…
> own accounting software, but that has to be done first.

Have you tried using the Win version through wine on Linux?  You might 
find that it works.  :)
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 10)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-30T18:29:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107138571.295191.161310@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<fhgLd.23232$8j3.2389@fe40.usenetserver.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <ae5jv0llfsqllivid0ogod8bohpp98odmv@4ax.com> <1106887899.311813.128520@f14g2000cwb.googlegroups.com> <9Pi8NA1PflB@jpberlin-l.willms.jpberlin.de> <fhgLd.23232$8j3.2389@fe40.usenetserver.com>`

```
> Have you tried using the Win version through wine on Linux?  You
might
find that it works.  :)

Failing that there is Win4Lin which is commercial ($30 for 'Home
edition') but runs much more Windows software because it runs a real
Win98/ME in a window on the Linux desktop.

(and runs it faster than just having Win98/ME on that hardware because
the ext2/3 filesystem is faster than FAT32.)
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 10)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-01-31T07:19:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9PuROwouflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <9Pi8NA1PflB@jpberlin-l.willms.jpberlin.de> <fhgLd.23232$8j3.2389@fe40.usenetserver.com>`

```
.    On  30.01.05
  wrote  lxi0007@netscape.net (LX-i)
     on  /COMP/LANG/COBOL
     in  fhgLd.23232$8j3.2389@fe40.usenetserver.com
  about  Re: OT (Maybe): ERPs

   on Windows-only tax programs:

l> Have you tried using the Win version through wine on Linux?

   For one, I barely use Linux, and secondly, I have not yet used said  
program at all.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Mit dem Band das ihre Herzen binden sollte haben sie ihren Frieden stranguliert. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 11)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-01-31T17:51:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0wzLd.31025$8j3.8101@fe40.usenetserver.com>`
- **In-Reply-To:** `<9PuROwouflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <9Pi8NA1PflB@jpberlin-l.willms.jpberlin.de> <fhgLd.23232$8j3.2389@fe40.usenetserver.com> <9PuROwouflB@jpberlin-l.willms.jpberlin.de>`

```
Lueko Willms wrote:
> .    On  30.01.05
>   wrote  lxi0007@netscape.net (LX-i)
…[9 more quoted lines elided]…
> program at all.

Ah - you seemed dejected that it's only available for Windows.  I took 
that to mean that you normally liked using something other than that. 
(Of course, Linux isn't the only non-Windows OS out there...)

I've been pleasantly surprised by the number of apps that work with wine.
```

###### ↳ ↳ ↳ Linux, Windows, and taxes (was: OT (Maybe): ERPs)

_(reply depth: 12)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-02-01T07:58:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Q1ZKdhPflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <9PuROwouflB@jpberlin-l.willms.jpberlin.de> <0wzLd.31025$8j3.8101@fe40.usenetserver.com>`

```
.    On  31.01.05
  wrote  lxi0007@netscape.net (LX-i)
     on  /COMP/LANG/COBOL
     in  0wzLd.31025$8j3.8101@fe40.usenetserver.com
  about  Re: OT (Maybe): ERPs


>>    on Windows-only tax programs:

LXI>>> Have you tried using the Win version through wine on Linux?
>>
>>    For one, I barely use Linux, and secondly, I have not yet used said
>> program at all.

l> Ah - you seemed dejected that it's only available for Windows.

  No, I mentioned that only to show that not everything is available  
for Linux.

  BTW, shortly after having written that, I learned about a project to  
write an open source equivalent for Linux.

  The program distributed by the tax office is called Elster, and  
acronym giving the name of a bird: Magpie.

  The open source equivalent shall go by the name of another bird:  
Geier, in english: Vulture ....

  You know, we are talking about taxes...


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Der Mann hatte soviel Verstand, daï¿½ er zu fast nichts mehr in der Welt zu gebrauchen war. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: Linux, Windows, and taxes

_(reply depth: 13)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-02-01T17:42:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OtULd.35078$8j3.33197@fe40.usenetserver.com>`
- **In-Reply-To:** `<9Q1ZKdhPflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <9PuROwouflB@jpberlin-l.willms.jpberlin.de> <0wzLd.31025$8j3.8101@fe40.usenetserver.com> <9Q1ZKdhPflB@jpberlin-l.willms.jpberlin.de>`

```
Lueko Willms wrote:
> .    On  31.01.05
>   wrote  lxi0007@netscape.net (LX-i)
…[21 more quoted lines elided]…
> write an open source equivalent for Linux.

Cool... :)

>   The program distributed by the tax office is called Elster, and  
> acronym giving the name of a bird: Magpie.
…[4 more quoted lines elided]…
>   You know, we are talking about taxes...

That seems to be universal.  ;)
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 6)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-01-28T06:16:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PMkKd.2267$Q72.1888@tornado.tampabay.rr.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <1106842807.711642.135610@z14g2000cwz.googlegroups.com>`

```

"steve.t" <sthompson@ix.netcom.com> wrote in message 
news:1106842807.711642.135610@z14g2000cwz.googlegroups.com...

> Success of a migration/implementation: That an entity is up on the new
> platform and the old one is gone does not a successful migration make.
> When 30% of your people are unable to do their job adequately because
> the new system can't produce a report you need in a reasonable time...
> When companies are seeing Cxx being hauled off in chains...

The platform is not the hardware...it's the software solution running on 
hardware...could be on multiple servers, single server, end user pc 
etc...could even be an application running hosted on someone else's 
hardware.

I'm sure a significant number of transformations do not fail due to 
inadequate hardware for five simple reasons  -

Firstly, the requirements to move come from executives, yet the requirements 
for the application come from end users - super users if you want.   The end 
users goal - simplify my life - is not the same as the executives - make 
this cheaper.

Secondly, the end users are very good at capturing requirements with regards 
to "this is what I've wanted for 2 years" but are very poor at capturing 
requirement that express "this is what we need now" (they sometime manage to 
tell you what they have now which is not the same thing and unfortunately 
they seem to forget the things they do that are painless and refer only to 
those things that are painful).  They assume that everything they do will be 
provided by default so only share the blue sky future. They don't seem to 
want to realize that the migration is like the collective bargaining 
agreement in american sports - at the end of the contract it goes away and 
the negotiation starts from nada.   A transformation project starts with the 
end user having NOTHING.

Thirdly, a failure to recognize that the answer is not to transition the 
existing solution from one hardware platform to another.  The solution most 
likely works, in part, because of the hardware it is running on.  If there 
is a cost issue, there are always options to reduce the hardware costs 
without changing the solution architecture.  A migration to a new hardware 
should be coupled with the need to migrate to a new solution.  This is often 
not the case.  The transition is deemed necessary by consultants and IT 
branches...its an existence justification. IT departments are now in the new 
role of having to provide - and excuse the marketing slang - their own value 
proposition.

Fourthly, the time allowed to complete a migration is never sufficient.  I 
understand that in some instances the project is canned after 2-3 years, but 
the original project plan was I'm sure *not* that large.  It always starts 
at 6 months investment and this is just enough time to try and rush in a 
"executive demo" without actually considering the solution 
ramifications.....then it becomes a we've gone 6 months, we just need 3 
more......then you find the mistakes of the first 6 months .....and then you 
need just 3 more...until they finally realize that the business is 
suffering.

Fifthly, or lastly even, the platform (still software solution) change, but 
the roles and function of personel do not.  As the functional role of the 
employees does not change, the data cannot be changed significantly, and 
therefore not successfully re-architected, and then alas the problems (not 
all, but usually the more heinous ones) are also transformed.  It seems that 
the data migration plan and the process definitions are the last item to be 
discussed on a transition plan ?!  Unfortunately the success of any data 
processing area requires accurate data modelling.  Your functional areas are 
then are built around the data and not the other way around.   Perhaps what 
we miss is that in some instances the pieces of the mainframe solution being 
transformed relies in its original form on some high I/O throughput due to 
inadequacies in the data model or even poor code.

A great example is at my location before I arrived there was an IMS to DB2 
migration.  The old IMS code was rewritten to "work".  It runs like a dog 
because it still accesses the data in a hierarchical and not relational way. 
We are still finding instances of  open cursor a to get b...open cursor b to 
get c ....open cursor c to get the answer....where DB2 could handle this 
much more efficiently as a combination of joins.

I am a only a web bigot. I hate any web application that forces me to hit a 
"close window" button, or a "back" button or has to warn me with a "don't 
hit this button twice" button.

> I have migrated whole accounting systems off to NT from mainframe. It
> worked because the amount of data to be processed was within the
…[3 more quoted lines elided]…
> key. All the programming was being done in COBOL.

Ah...now you touch on it...it really isn't a hardware platform issue ...it's 
a software platform issue.....only a specific instance of a failed project 
knows why the project failed and I'd venture a guess that 75% of projects it 
is not the hardware...


JCE
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 7)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2005-01-28T14:50:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35vqceF4nsp1aU1@individual.net>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <1106842807.711642.135610@z14g2000cwz.googlegroups.com> <PMkKd.2267$Q72.1888@tornado.tampabay.rr.com>`

```
jce<defaultuser@hotmail.com> 1/27/2005 11:16:15 PM >>>
>A great example is at my location before I arrived there was an IMS to DB2

>migration.  The old IMS code was rewritten to "work".  It runs like a dog 
>because it still accesses the data in a hierarchical and not relational
way. 
>We are still finding instances of  open cursor a to get b...open cursor b
to 
>get c ....open cursor c to get the answer....where DB2 could handle this 
>much more efficiently as a combination of joins.

This bit is certainly discouraging.  Our new Chief Technology Officer (who
was in charge of the "distributed applications" and network side and is now
also over the mainframe side) has us to looking at converting from DL/I
(IMS, but for VSE) to a RDBMS.  On the surface it sounds great -- I'd love
to have a relational database system.  But I have a hard time imagining
coverting hundreds of programs.  First of all it seems pretty much
"impossible" on its surface, at least unless you stop all other development
on the system until the conversion is complete.  Second, do you really want
people who are used to only a hierarchical database doing the conversion? 
We'd probably end up in the same position your company did.

Anyway, with all of that said I'd be curious as to the effort involved at
your shop, and if in the end it was determined to be worth doing.


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-01-31T16:57:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ctlo55$h20$1@peabody.colorado.edu>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <35vqceF4nsp1aU1@individual.net>`

```

On 28-Jan-2005, "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote:

> Second, do you really want
> people who are used to only a hierarchical database doing the conversion?

If the database is designed right, what difference does this make?
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 7)_

- **From:** "steve.t" <sthompson@ix.netcom.com>
- **Date:** 2005-01-30T15:42:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107128575.221971.106350@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<PMkKd.2267$Q72.1888@tornado.tampabay.rr.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <1106842807.711642.135610@z14g2000cwz.googlegroups.com> <PMkKd.2267$Q72.1888@tornado.tampabay.rr.com>`

```
"Ah...now you touch on it...it really isn't a hardware platform issue
...it's
a software platform issue.....only a specific instance of a failed
project
knows why the project failed and I'd venture a guess that 75% of
projects it
is not the hardware... "

First, I generally deal with systems that process huge amounts of data.
In the accounting system's case, data was sent to it across the
internet. That data was processed to produce bills and statements.

It became obvious that at some point (within months) the laser printer
would not be able to print all the "reports" in a timely fashion. This
would cause a need for multiple printers, and a larger hard drive used
to spool the print output. This was on top of the number of electronic
billing statements/invoices being sent out.

So, yes it is a hardware issue. This is generally what I am talking
about when I speak of architecture and I do modeling to determine if
the system can handle the I/O load required of it. Again, the
accounting system moved to NT, all the users (<10) were able to access
the data across the LAN. Had there been a need for 100 users, the LAN
would have needed an upgrade, and that would have required going from a
single do it all server to 3-4 servers.

If they were to have more data coming in (I have forgotten how many MB
it would take), then the Telecommunications connections would have to
be upgraded (business level broadband - and at that time it was
recognized that the ISP had over sold its capacity). Once we surpassed
a certain point there, then the NT server handling the incoming data,
regardless of motherboard (single or multiple CPUs), clock speed, etc.,
would not be able to handle the data in a timely fashion.

As can be seen, there are many types of I/O processes that must be
looked at. CPU speeds are generally so much faster than I/O rates, that
software platform is not really an issue until you do an environment
migration. Had there been a migration to Linux from NT at that point,
it can now be argued (it wasn't available to argue then) that the Linux
system could do more in the same time. But the do more capability still
ran out of gas because the limitations imposed by simple physics.

And so the reason for COBOL being used on day one was to facilitate
moving from one environment to another as that company grew (COBOL
programmers are more available than are C++ and/or VB programmers --
therefore, less training would need to be done as the system grew).

Amazing what happens when a real architecture knowledgeable person is
in the room with the Board of Directors.

Later,
Steve.T
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 8)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-01-31T07:54:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RulLd.10911$JF2.9972@tornado.tampabay.rr.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <1106842807.711642.135610@z14g2000cwz.googlegroups.com> <PMkKd.2267$Q72.1888@tornado.tampabay.rr.com> <1107128575.221971.106350@f14g2000cwb.googlegroups.com>`

```

"steve.t" <sthompson@ix.netcom.com> wrote in message 
news:1107128575.221971.106350@f14g2000cwb.googlegroups.com...
> "Ah...now you touch on it...it really isn't a hardware platform issue
> ...it's
…[8 more quoted lines elided]…
> internet. That data was processed to produce bills and statements.
snip snip
> Steve.T

Fair points.

Initially you stated:

"I'm looking for a web site that I think exists that shows all the
failed whoopie-wow projects. You know, like the attempted Siebel
implementations (where they tried to take over something being done on
a mainframe)."

I think the issue here is migrating an existing CRM solution to Siebel. This 
is software not hardware - generally speaking.

With further explanation I see how your particular example was primarily 
hardware driven...

JCE
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 9)_

- **From:** "steve.t" <sthompson@ix.netcom.com>
- **Date:** 2005-01-31T09:04:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107188398.299913.187670@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<RulLd.10911$JF2.9972@tornado.tampabay.rr.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <1106842807.711642.135610@z14g2000cwz.googlegroups.com> <PMkKd.2267$Q72.1888@tornado.tampabay.rr.com> <1107128575.221971.106350@f14g2000cwb.googlegroups.com> <RulLd.10911$JF2.9972@tornado.tampabay.rr.com>`

```
Almost all of the failed Siebel migrations were attempts to move from a
mainframe oriented environment. As near as I can tell, they are all
destined to failure because the mainframe is more easily able to deal
with huge quantities of data and user I/O demand. Add to this the
intersystem communications, and the hardware thrown together to attack
the mainframe environment collapses under its own weight.

There is a significant difference in the internal design of a mainfame
over almost all other systems. When you are dealing with complex
transactions (database call, intersystem query, screen read/write, log
file updates, etc.) you can't easily set this up to work off the
mainframe because of the amount system interaction that needs be done
at memory speeds.

In order to solve some of these issues, mainframe O/S designs were
changed to use something called a Coupling Facility. This allows them
to "instantly" handle record/table/row locking (as well as fail-over)
between 2-? Images across n CECs (a CEC is a single computer system
that may or may not be running LPARs). Therefore, this massively
parallel design that is built into mainframes can't be easily achieved
using multiple servers interconnected with GiGE.

Like I said before, I'm not a mainframe bigot. I have several tools in
my tool box. Once you have identified the amount of work to be done by
a system, you can then identify the most economical way of processing
it. By the time you get to a mainframe and the amount of processing it
is doing, you generally can't move back to lesser hardware designs and
maintain the throughput without spending even more money on hardware.

But as I've shown, I've done it when it was possible and made sense to
do it.

Later,
Steve.T
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 10)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-31T18:45:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7htsv019bt1ea3d5t6uafh4jk2akb9tuvn@4ax.com>`
- **References:** `<1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <1106842807.711642.135610@z14g2000cwz.googlegroups.com> <PMkKd.2267$Q72.1888@tornado.tampabay.rr.com> <1107128575.221971.106350@f14g2000cwb.googlegroups.com> <RulLd.10911$JF2.9972@tornado.tampabay.rr.com> <1107188398.299913.187670@c13g2000cwb.googlegroups.com>`

```
On 31 Jan 2005 09:04:41 -0800, "steve.t" <sthompson@ix.netcom.com>
wrote:

>Almost all of the failed Siebel migrations were attempts to move from a
>mainframe oriented environment. As near as I can tell, they are all
…[3 more quoted lines elided]…
>the mainframe environment collapses under its own weight.

I worked on a project to move a payroll/HR system from mainframe
running assembly language to PeopleSoft. It was, by far, the largest
payroll that had been put on PeopleSoft -- 400,000 active employees
being paid weekly. Mainframers predicted failure.

The weekly check run took two hours on two fire-breathing mainframes
with about 60 processors each. The first test run on
PeopleSoft/Informix took about 28 hours. Mainframers laughed. We split
the database into 24 partitions running on 24 servers. The second run
took about two hours. Mainframers stopped laughing and started looking
worried. The new system went live on-time and on-budget. Computer
expense was drastically reduced.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 11)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-31T11:15:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107198924.019810.184170@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<7htsv019bt1ea3d5t6uafh4jk2akb9tuvn@4ax.com>`
- **References:** `<1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <1106842807.711642.135610@z14g2000cwz.googlegroups.com> <PMkKd.2267$Q72.1888@tornado.tampabay.rr.com> <1107128575.221971.106350@f14g2000cwb.googlegroups.com> <RulLd.10911$JF2.9972@tornado.tampabay.rr.com> <1107188398.299913.187670@c13g2000cwb.googlegroups.com> <7htsv019bt1ea3d5t6uafh4jk2akb9tuvn@4ax.com>`

```
> The weekly check run took two hours on two fire-breathing mainframes
> ...
> The new system went live on-time and on-budget.

It seems the story is rather different: previously you had:

RW> Tight assembly language, probably written in the '60s, runs very
FAST on a
RW> modern mainframe. That payroll system could plow through a 1G
master file and
RW> compute 200K paychecks in less than 15 minutes. The first attempt
on PeopleSoft
RW> took longer than 12 hours. Speeding it up required partitioning the
database
RW> over 30 disks and using lots of parallel processing. Thirty
high-end servers
RW> were still cheaper than two monster mainframes.

The numbers have changed, mainframe seems to have slowed from 15
minutes to 2 hours to suit the Unix result while originally it seemed
that the extra servers had to be added which would have increased the
budget.

That is always a problem with making things up, it is so hard to
remember how much you exagerated last time.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 12)_

- **From:** "steve.t" <sthompson@ix.netcom.com>
- **Date:** 2005-01-31T18:13:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107224027.535469.28430@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1107198924.019810.184170@z14g2000cwz.googlegroups.com>`
- **References:** `<1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <1106842807.711642.135610@z14g2000cwz.googlegroups.com> <PMkKd.2267$Q72.1888@tornado.tampabay.rr.com> <1107128575.221971.106350@f14g2000cwb.googlegroups.com> <RulLd.10911$JF2.9972@tornado.tampabay.rr.com> <1107188398.299913.187670@c13g2000cwb.googlegroups.com> <7htsv019bt1ea3d5t6uafh4jk2akb9tuvn@4ax.com> <1107198924.019810.184170@z14g2000cwz.googlegroups.com>`

```
I think his name in real life is Al Gore
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 12)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-02-01T03:07:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<naotv0tieskqcfhrhds6noj6s2tifgllen@4ax.com>`
- **References:** `<1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <1106842807.711642.135610@z14g2000cwz.googlegroups.com> <PMkKd.2267$Q72.1888@tornado.tampabay.rr.com> <1107128575.221971.106350@f14g2000cwb.googlegroups.com> <RulLd.10911$JF2.9972@tornado.tampabay.rr.com> <1107188398.299913.187670@c13g2000cwb.googlegroups.com> <7htsv019bt1ea3d5t6uafh4jk2akb9tuvn@4ax.com> <1107198924.019810.184170@z14g2000cwz.googlegroups.com>`

```
On 31 Jan 2005 11:15:24 -0800, "Richard" <riplin@Azonic.co.nz> wrote:

>> The weekly check run took two hours on two fire-breathing mainframes
>> ...
…[19 more quoted lines elided]…
>budget.

The program that computed paychecks did run in 15 minutes. It was one
of 20 programs in a jobstream that took 2 hours.

Now that you jogged my memory, there were 30 servers rather than 24. 

>That is always a problem with making things up, it is so hard to
>remember how much you exagerated last time.

Reality is the antedote to (your) solipsism.

Call Sears HQ in Hoffman Estates, Il, and ask the payroll system
manager to describe what they're running. Verify that it was installed
in 1998-9 by Deloitte Touche and Keane. Then, if you insist, I'll scan
and send a tax document showing I worked there during that period.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 10)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-01-31T20:41:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9PuX3BSeflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <RulLd.10911$JF2.9972@tornado.tampabay.rr.com> <1107188398.299913.187670@c13g2000cwb.googlegroups.com>`

```
.    On  31.01.05
  wrote  sthompson@ix.netcom.com (steve.t)
     on  /COMP/LANG/COBOL
     in  1107188398.299913.187670@c13g2000cwb.googlegroups.com
  about  Re: OT (Maybe): ERPs


s> Almost all of the failed Siebel migrations

   what is Siebel?

s>                                        were attempts to move from
s> a mainframe oriented environment. As near as I can tell, they are all
s> destined to failure because the mainframe is more easily able to deal
s> with huge quantities of data and user I/O demand.

   Why?

s>                                                    Add to this the
s> intersystem communications, and the hardware thrown together to attack
s> the mainframe environment collapses under its own weight.

   Well, the alternative is not only a PC with a PCI bus ...

   Have you seen e.g. the ES7000 servers from Unisys with several  
dozen 64-bit and 32-bit Intel processors, and corresponding I/O- 
channels? Running with Windows Data Center server software, or Linux?

   http://www.unisys.com/products/es7000__servers/index.htm
   http://www.unisys.com/products/es7000__linux/index.htm


s> There is a significant difference in the internal design of a mainfame

   maybe this typo is more telling than you intended

s> over almost all other systems. When you are dealing with complex
s> transactions (database call, intersystem query, screen read/write, log
s> file updates, etc.) you can't easily set this up to work off the
s> mainframe because of the amount system interaction that needs be done
s> at memory speeds.

   I think the main strength of the mainframes is the applications  
which run on them and which cannot easily ported to a different  
platform. Think of the airline reservations systems - large, complex  
systems which have grown over several decades and which cannot be  
rewritten in several months for Linux or Windows.

  On the other hand, in pure CPU-processing power, mainframes probably  
lag behind, at least in cost/performance ratio, since their processor  
designs dating from the 1960ies are not produced by the millions as PC  
CPUs are, so they tend to be at least more expensive.

  Without having hard data at hand, I think, there is a slow erosion  
of mainframe shops, even if some of them, and mostly the biggest ones,  
are adding more mainframe processing power.

  There are even some new customers -- I heard of one of the four  
mobile phone companies in Germany which tried to implement their voice  
mail (answering machine on the net) on a cluster or Unix boxes, but  
finally gave up and bought a ready made solution which runs on a  
Unisys mainframe of the A-Series line (Clearpath NX or LX they are  
called nowadays).

  Hardware is sold by applications ...

Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Er urteilt nach dem jedesmaligen Aggregatzustand seiner Empfindungen. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 11)_

- **From:** "steve.t" <sthompson@ix.netcom.com>
- **Date:** 2005-01-31T18:32:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107225160.661382.110210@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<9PuX3BSeflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <RulLd.10911$JF2.9972@tornado.tampabay.rr.com> <1107188398.299913.187670@c13g2000cwb.googlegroups.com> <9PuX3BSeflB@jpberlin-l.willms.jpberlin.de>`

```
SIEBEL (pronounced here as SEE BULL) is a software product that is
supposed to automate the creation of ERP/CRM etc. software.
Theoretically it is drop, load and go.

To answer your Why question, one needs to look at the platforms that
SIEBEL Corp is certified to run on/under. Then one has to look at the
overall design of a system that a group of consultants got paid to
re-write so that it works basically the same way as it does now.

Of course, they don't ask the right questions, make a bunch of
assumptions that flatly are wrong and then miss all their deadlines. Of
course the answer is to throw more hardware at the problem with the
resulting overheads...

Then there are the mainframe CPU designs which *ARE* on chips. It is
possible to take the 68030 (Motorola) and re-microcode it and three of
them done this way would make an old 4300 that would fit in a desk
drawer (done at Boca Raton by a few IBMers I'm told). All the CMOS
mainframes are on CHIPs such that if you have a CPU fail, the system
controller will take the failing CPU offline and bring online a good
CPU from the same CPU card (assuming there is only 1 CPU card in the
CEC).

Come to think of it, the IBM chip plant produced, on the same line, the
AIX, AS/400 and S/390 chips. Hmmmmm. Cost effective idea here.

And yes, I've heard of what UNISYS is doing. Notice that the way the
CPUs are plugged together that the bus is not central to all
processing. Again, one of those ideas used by mainframe designers.

Here is a question: What exactly is a mainframe? Some years ago I could
point to a large box and say that was a mainframe. But today my laptop
has more power than that S/370 architected 3033MP. So what is a
mainframe?

In 1996/7 IBM noticed that the number of MVS licenses had stopped
falling off and had started increasing for the first time in years. Not
a lot of noise is made about this little phenomena. But with IBM
running away from the small systems again, I can well imagine that the
numbers will start to fall off again as consolidations continue.

Imagine what would happen if IBM were to start licensing to HERC users.

Later,
Steve.T

ps. This may well be one of my last posts for a while. Looks like I may
be doing quite a few migrations of old installs to z/OS. Back in the
saddle again!
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 12)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-31T18:58:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107226707.335726.216480@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1107225160.661382.110210@f14g2000cwb.googlegroups.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <RulLd.10911$JF2.9972@tornado.tampabay.rr.com> <1107188398.299913.187670@c13g2000cwb.googlegroups.com> <9PuX3BSeflB@jpberlin-l.willms.jpberlin.de> <1107225160.661382.110210@f14g2000cwb.googlegroups.com>`

```
> What exactly is a mainframe?

Many different types of electronic equipment are built into frames (ie
steel frameworks that are cabinets when the covers are added): Radio
transmitters, Telephone exchanges, computers, ..

In many cases there is a main frame which holds the central controlling
equipment (or processing unit) usually in the middle of the romm,
around which are the peripheral frames around the edge of the room.

The term 'MainFrame Computer' refers to the electronics gubbins in the
cabinets in the centre of the room as distinct from the peripheral
equipment.  People who were not technicians did not know this and
thought that 'mainframe' was a class of computer.
Today the term should probably be replaced by RackMount.
```

###### ↳ ↳ ↳ What is a 'mainframe'? (was: OT (Maybe): ERPs)

_(reply depth: 12)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-02-01T08:26:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Q1ZL$GuflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <9PuX3BSeflB@jpberlin-l.willms.jpberlin.de> <1107225160.661382.110210@f14g2000cwb.googlegroups.com>`

```
.    On  31.01.05
  wrote  sthompson@ix.netcom.com (steve.t)
     on  /COMP/LANG/COBOL
     in  1107225160.661382.110210@f14g2000cwb.googlegroups.com
  about  Re: OT (Maybe): ERPs


  Thanks for your explanations re Siebel.

s> Here is a question: What exactly is a mainframe? Some years ago I
s> could point to a large box and say that was a mainframe. But today my
s> laptop has more power than that S/370 architected 3033MP. So what is a
s> mainframe?

   For me, as -- I think for many others, too -- "mainframe"  
designates the old architectures from the 1960ies, i.e. going back to  
IBM's S/360, Unisys Clearpath continuing the Sperry 1100 and Burroughs  
Large Systems, Siemens BS2000 (coming from RCA's TSOS), Bull GCOS,  
i.e. with proprietary operating systems running only on that type of  
processor.

   This does not include all machines which are called "enterprise  
servers" as in this report:

   http://mediaproducts.gartner.com/reprints/unisys/124352.html

   which sees e.g. the Sun machines in the top quadrant, which I would  
not understand as 'mainframe'.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Der Mann machte sehr viel Wind. B: O nein! Wenn es noch Wind gewesen  
wï¿½re, es war aber mehr ein wehendes Vacuum. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 11)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-02-01T03:39:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lcttv0t36hs9phmk9utodiabbhqrod6n9v@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <RulLd.10911$JF2.9972@tornado.tampabay.rr.com> <1107188398.299913.187670@c13g2000cwb.googlegroups.com> <9PuX3BSeflB@jpberlin-l.willms.jpberlin.de>`

```
On 31 Jan 2005 20:41:00 GMT, l.willms@jpberlin.de (Lueko Willms)
wrote:
>   I think the main strength of the mainframes is the applications  
>which run on them and which cannot easily ported to a different  
>platform. Think of the airline reservations systems - large, complex  
>systems which have grown over several decades and which cannot be  
>rewritten in several months for Linux or Windows.

The largest, American Airlines' Sabre system, is now being or has been
ported to Unix.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 5)_

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2005-01-27T12:38:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41F9353F.F21E948C@mb.sympatico.ca>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com>`

```
Robert Wagner wrote:
> 
> 
…[5 more quoted lines elided]…
> retire old farts. (Present company excluded, of course.)

That's rather too broad a generalization, I'd say.  Lessons learned 30
years ago about using minimum resources, about making sure that
un-necessary statements stay outside the perform loops, things like that
- still are useful and will make for better programming.

I'm sure you didn't mean to imply this, but there are those who would
interpret your statement as meaning "it doesn't matter if we write
horrible inefficient programs that use a hundred times the memory and
disk space they actually need becuase hardware is so fast and cheap that
nobody will ever notice, just as long as they work, somehow".  Did you
ever see the flight simulator hidden away as an easter egg in EXCEL?

Didn't structured programming come into existence about 30 years ago?

PL
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 6)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-28T03:39:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <41F9353F.F21E948C@mb.sympatico.ca>`

```
On Thu, 27 Jan 2005 12:38:55 -0600, Peter Lacey
<lacey@mb.sympatico.ca> wrote:

>Robert Wagner wrote:

>> Lessons learned 30 years ago, when hardware was expensive, no longer
>> apply in today's world of cheap hardware. Worse, insisting on their
…[5 more quoted lines elided]…
>- still are useful and will make for better programming.

It's now more a question of Art than Necessity.

>I'm sure you didn't mean to imply this, but there are those who would
>interpret your statement as meaning "it doesn't matter if we write
>horrible inefficient programs that use a hundred times the memory and
>disk space they actually need becuase hardware is so fast and cheap that
>nobody will ever notice, just as long as they work, somehow". 

That describes most Windows programs. Why does WeatherBug take 6 meg,
and FireFox take 12 meg? I can remember when only monster machines had
16 meg of memory. Now 128 meg isn't enough to run 2-3 simple apps
without thrashing. Serious servers have 16 gigabytes of memory, which
is more than the total DISK space we once had.

Yet, Cobol programmers are still using packed decimal to save space.
The saving is measured in  pennies; the cost to someone trying to
import the file is many hundreds of dollars.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 7)_

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2005-01-27T22:55:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41F9C5AB.F9B8DC2E@mb.sympatico.ca>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <41F9353F.F21E948C@mb.sympatico.ca> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com>`

```
Robert Wagner wrote:

> 
> Yet, Cobol programmers are still using packed decimal to save space.

Won't argue with you about that.  I actually lost a conversion job
because I tried to convince her that packed wasn't necessary.

PL
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-01-28T05:54:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%rkKd.281645$f47.55566@news.easynews.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <41F9353F.F21E948C@mb.sympatico.ca> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com> <41F9C5AB.F9B8DC2E@mb.sympatico.ca>`

```
I certainly will NOT speak to other compilers or operating systems, but the (or 
at least one of the) major reasons that Packed Decimal is used over "display" on 
IBM mainframes - is for performance not to "save space".  Obviously, this does 
not impact occasionally used data items or non-performance sensitive 
applications, but from page 31 of the

"IBM Enterprise COBOL Version 3 Release 1
Performance Tuning"

the following information seems pretty relevant to me (based on actual 
performance testing),

"DISPLAY compared to packed decimal (COMP-3)
     - using 1 to 6 digits: DISPLAY is 100% slower than packed decimal
     - using 7 to 16 digits: DISPLAY is 40% to 70% slower than packed decimal
     - using 17 to 18 digits: DISPLAY is 150% to 200% slower than packed 
decimal"

There are LOTS of "caveats" to these specific statistics (in the paper) so 
"YMMV".

To see this comparison in context (along with other comparisons of different 
compiler options, data types, etc), see the full paper from:

 http://www-1.ibm.com/support/docview.wss?rs=203&q=7001475&uid=swg27001475
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 9)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-27T22:17:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106893070.704270.82540@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<%rkKd.281645$f47.55566@news.easynews.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <41F9353F.F21E948C@mb.sympatico.ca> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com> <41F9C5AB.F9B8DC2E@mb.sympatico.ca> <%rkKd.281645$f47.55566@news.easynews.com>`

```
> is for performance not to "save space"

I did some tests many years ago with MF CIS Cobol comparing DISPLAY,
COMP and COMP-3.  When only computational verbs were used the fastest
was COMP, when edited numeric MOVEs and I/O (DISPLAY) was used DISPLAY
was the fastest, but when there was a realistic mixture of computation
and I/O with numeric edited COMP-3 was the fastest.
And this was on Intel CPU.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 9)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-28T08:29:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h3tjv01c4c0i5596hlmpca9h9it15rofck@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <41F9353F.F21E948C@mb.sympatico.ca> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com> <41F9C5AB.F9B8DC2E@mb.sympatico.ca> <%rkKd.281645$f47.55566@news.easynews.com>`

```
On Fri, 28 Jan 2005 05:54:04 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>I certainly will NOT speak to other compilers or operating systems, but the (or 
>at least one of the) major reasons that Packed Decimal is used over "display" on 
>IBM mainframes - is for performance not to "save space".  

IBM and Unisys mainframes support packed decimal hardware
instructions. On Intel, Sun and others, packed decimal is no faster
than display. 

On IBM mainframes (don't know about Unisys), converting display to and
from packed is very fast. When I work on mainframes, I put display in
files, packed in working-storage. I do arithmetic in working-storage,
not in the record area.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 10)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-01-28T09:12:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ctdrp2$2275$1@si05.rsvl.unisys.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <41F9353F.F21E948C@mb.sympatico.ca> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com> <41F9C5AB.F9B8DC2E@mb.sympatico.ca> <%rkKd.281645$f47.55566@news.easynews.com> <h3tjv01c4c0i5596hlmpca9h9it15rofck@4ax.com>`

```

"Robert Wagner" <spamblocker-robert@wagner.net> wrote in message
news:h3tjv01c4c0i5596hlmpca9h9it15rofck@4ax.com...

> IBM and Unisys mainframes support packed decimal hardware
> instructions.

Can't speak to the ex-Sperry mainframes, but what the MCP variety supports
is fast hardware instructions to pack and unpack items, as well as to
convert from both decimal formats into binary and back.   The arithmetic is
actually done in binary.

> On IBM mainframes (don't know about Unisys), converting display to and
> from packed is very fast.

True also on Unisys MCP, and often used in MOVE, but if you're retrieving
for arithmetic purposes it's that conversion to and from *binary* is very
fast that matters.

We investigated building decimal hardware into the early A Series back in
the mid-1980's.  The Burroughs Medium System was designed around "string"
arithmetic, and we had some experience with it.  The "string" model wouldn't
map very well to the "word-oriented" A Series, but the engineers thought
they could come up with a reasonable way to do this.  The argument that won
the day at the time was that decimal arithmetic hardware in the A Series
word-oriented environment (be it "operand-oriented" or "pointer-oriented")
would be decidedly expensive, and that we could get the same performance
benefit by improving the performance of the existing binary-to-decimal
(packed or display) and decimal-to-binary instructions at MUCH less cost.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 9)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2005-01-28T11:37:59-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10vku3nn1jfvi94@news.supernews.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <41F9353F.F21E948C@mb.sympatico.ca> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com> <41F9C5AB.F9B8DC2E@mb.sympatico.ca> <%rkKd.281645$f47.55566@news.easynews.com>`

```
William M. Klein wrote:
> I certainly will NOT speak to other compilers or operating systems,
> but the (or at least one of the) major reasons that Packed Decimal is
…[17 more quoted lines elided]…
> paper) so "YMMV".

Yeah, but the biggest caveat is "who cares?" Aside from the business about 
something being "100%" slower (which means, to me, that its speed is zero, I 
won't even attempt to define "200% slower"), the big question is 100% slower 
than WHAT?

A saving of 50 nanoseconds per transaction is so close to zero as to be 
indistinguishable.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-01-28T18:08:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ctdv61$s3b$1@peabody.colorado.edu>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <41F9353F.F21E948C@mb.sympatico.ca> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com> <41F9C5AB.F9B8DC2E@mb.sympatico.ca> <%rkKd.281645$f47.55566@news.easynews.com> <10vku3nn1jfvi94@news.supernews.com>`

```

On 28-Jan-2005, "JerryMouse" <nospam@bisusa.com> wrote:

> A saving of 50 nanoseconds per transaction is so close to zero as to be
> indistinguishable.

Usually.

But not always, especially in jobs that have to fit in a window, running
billions of transactions before the database goes down at midnight.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 11)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2005-01-28T17:18:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10vli1jd0vhopea@news.supernews.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <41F9353F.F21E948C@mb.sympatico.ca> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com> <41F9C5AB.F9B8DC2E@mb.sympatico.ca> <%rkKd.281645$f47.55566@news.easynews.com> <10vku3nn1jfvi94@news.supernews.com> <ctdv61$s3b$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> On 28-Jan-2005, "JerryMouse" <nospam@bisusa.com> wrote:
>
…[7 more quoted lines elided]…
> midnight.

I exaggerate for the purpose of emphasis.

Still, 10 billion transactions at a saving of 50 nanoseconds each is an 
overall saving of 500 seconds: ~ eight minutes.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 12)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-28T16:34:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106958861.623924.141560@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<10vli1jd0vhopea@news.supernews.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <41F9353F.F21E948C@mb.sympatico.ca> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com> <41F9C5AB.F9B8DC2E@mb.sympatico.ca> <%rkKd.281645$f47.55566@news.easynews.com> <10vku3nn1jfvi94@news.supernews.com> <ctdv61$s3b$1@peabody.colorado.edu> <10vli1jd0vhopea@news.supernews.com>`

```
> I exaggerate for the purpose of emphasis.

> Still, 10 billion transactions at a saving of 50 nanoseconds each is
an
> overall saving of 500 seconds: ~ eight minutes.

Of course you didn't establish that the saving was only of '50
nanoseconds' which was purely an exageratedly small figure that you
invented to make it easier to support your bias.

50 nanosec is around the figure for a single memory cycle (on machines
of 233 FSB).

So each and every memory cycle saved (where an instruction may take
several cycles) results in saving 8 minutes.  Save a handful of
instructions and it is soon measured in hours.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 7)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-28T01:41:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106905272.863816.274380@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <41F9353F.F21E948C@mb.sympatico.ca> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com>`

```
> the cost to someone trying to import the file is many hundreds of
dollars.

I don't think that one can EMail a zOS VSAM file raw dump, if one could
the packed fields would be the least of the problems.

With most systems attempting to use raw files is nonsense.  I know that
you used to do this with C-ISAM files which are _almost_ useful.
Data interchange must be done with well defined file structures.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 8)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-28T12:53:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <41F9353F.F21E948C@mb.sympatico.ca> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com> <1106905272.863816.274380@f14g2000cwb.googlegroups.com>`

```
On 28 Jan 2005 01:41:12 -0800, "Richard" <riplin@Azonic.co.nz> wrote:

>> the cost to someone trying to import the file is many hundreds of
>dollars.
…[6 more quoted lines elided]…
>Data interchange must be done with well defined file structures.

Every week or two someone asks here how to read a 'Cobol file',
because someone sent a raw file.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2005-01-28T08:03:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ctdd7a$3bb$1@panix5.panix.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com> <1106905272.863816.274380@f14g2000cwb.googlegroups.com> <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com>`

```
In article <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com>,
Robert Wagner  <spamblocker-robert@wagner.net> wrote:
>On 28 Jan 2005 01:41:12 -0800, "Richard" <riplin@Azonic.co.nz> wrote:
>
…[11 more quoted lines elided]…
>because someone sent a raw file. 

Really?  I have no idea, Mr Wagner, how you come to conclusions about what 
is sent or received... but it might be concluded with greater validity 
that people ask how to 'read a 'Cobol file'' because they never learned 
such minor details as the independence of programming languages and file 
structures... and that their management does not have the competence to 
realise that knowing such details, and others associated with them, might 
just possibly be beneficial in accomplishing a stated executive goal when 
said managers assign tasks.

DD
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 10)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-28T17:09:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<biokv0pn1tuns3kicugp4uei5bu3e9nhqc@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com> <1106905272.863816.274380@f14g2000cwb.googlegroups.com> <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com> <ctdd7a$3bb$1@panix5.panix.com>`

```
On 28 Jan 2005 08:03:38 -0500, docdwarf@panix.com wrote:

>In article <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com>,
>Robert Wagner  <spamblocker-robert@wagner.net> wrote:
…[16 more quoted lines elided]…
>is sent or received...

When someone says he has a pair of files named .IND and .INX, it's
obvious to most that he has a raw indexed file. 

> but it might be concluded with greater validity 
>that people ask how to 'read a 'Cobol file'' because they never learned 
>such minor details as the independence of programming languages and file 
>structures... 

Format is tied to the compiler, not the language. He should have asked
how to read a 'Micro Focus file'. Happy now?

>and that their management does not have the competence to 
>realise that knowing such details, and others associated with them, might 
>just possibly be beneficial in accomplishing a stated executive goal when 
>said managers assign tasks.

Assigning blame to a person might make you feel better, but doesn't
help with getting the file read.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2005-01-28T12:56:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ctducp$1n7$1@panix5.panix.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com> <ctdd7a$3bb$1@panix5.panix.com> <biokv0pn1tuns3kicugp4uei5bu3e9nhqc@4ax.com>`

```
In article <biokv0pn1tuns3kicugp4uei5bu3e9nhqc@4ax.com>,
Robert Wagner  <spamblocker-robert@wagner.net> wrote:
>On 28 Jan 2005 08:03:38 -0500, docdwarf@panix.com wrote:
>
…[21 more quoted lines elided]…
>obvious to most that he has a raw indexed file. 

When someone says 'he has' it is not obvious that 'he was sent' anything, 
Mr Wagner.

>
>> but it might be concluded with greater validity 
…[5 more quoted lines elided]…
>how to read a 'Micro Focus file'. Happy now?

Shoulda, coulda, woulda, Mr Wagner... what's there is there, perhaps you 
can deal with it.

>
>>and that their management does not have the competence to 
…[5 more quoted lines elided]…
>help with getting the file read.

Mr Wagner, you certainly appear to enjoy seeing things in terms of 
'blame'... I point out whose job it is, by definition, to do things, no 
more, no less.  The allocation, co-ordination and motivation of personnel 
and resources towards the accomplishment of a stated Executive goal is the 
responsibility of Management, or so the textbooks have said; are you 
saying that to state this is to 'assign blame'?

DD
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 12)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-28T21:11:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f28lv01qvq2qfbvqo3hvpk3tlkrc15c1qf@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com> <ctdd7a$3bb$1@panix5.panix.com> <biokv0pn1tuns3kicugp4uei5bu3e9nhqc@4ax.com> <ctducp$1n7$1@panix5.panix.com>`

```
On 28 Jan 2005 12:56:41 -0500, docdwarf@panix.com wrote:

>In article <biokv0pn1tuns3kicugp4uei5bu3e9nhqc@4ax.com>,
>Robert Wagner  <spamblocker-robert@wagner.net> wrote:

>>and that their management does not have the competence to 
>>realise that knowing such details, and others associated with them, might 
>>just possibly be beneficial in accomplishing a stated executive goal when 
>>said managers assign tasks.

>>Assigning blame to a person might make you feel better, but doesn't
>>help with getting the file read.
…[6 more quoted lines elided]…
>saying that to state this is to 'assign blame'?

When a problem arises, management instinctively asks who's guilty;
programmers work on a remedy. You offered an opinion about the
competence of management, and nothing about a remedy. So yes, you're
assigning blame.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 13)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-28T13:44:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106948667.066879.309510@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<f28lv01qvq2qfbvqo3hvpk3tlkrc15c1qf@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com> <ctdd7a$3bb$1@panix5.panix.com> <biokv0pn1tuns3kicugp4uei5bu3e9nhqc@4ax.com> <ctducp$1n7$1@panix5.panix.com> <f28lv01qvq2qfbvqo3hvpk3tlkrc15c1qf@4ax.com>`

```
> You offered an opinion about the competence of management,

I have seen you do that many, many times, as well as about all
mainframe programmers, system admins, and even doctors.

The difference is that the Doc referred to _their_ managers, the small
specific sample that directly related to where a programmer was given
the task of reading a file without the management providing the means
to know how to do that.

You, on the other hand, apply your opinions to 'all' or to the whole
group, such as here when you broadened doc's 'their management' to the
generalised 'management'.  And you never seem to notice the difference.

And, yes, he _did_ provide an implied remedy:

"""knowing such details, and others associated with them, might
just possibly be beneficial in accomplishing a stated executive goal
when
said managers assign tasks."""

Note the use of 'said managers', ie those specific ones that did not
supply such aids, as is evidenced by the programmers having to ask
here.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 14)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-29T12:36:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sc0nv057ba39g2kurqhh42brtg3j25tkvl@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com> <ctdd7a$3bb$1@panix5.panix.com> <biokv0pn1tuns3kicugp4uei5bu3e9nhqc@4ax.com> <ctducp$1n7$1@panix5.panix.com> <f28lv01qvq2qfbvqo3hvpk3tlkrc15c1qf@4ax.com> <1106948667.066879.309510@z14g2000cwz.googlegroups.com>`

```
On 28 Jan 2005 13:44:27 -0800, "Richard" <riplin@Azonic.co.nz> wrote:

>> You offered an opinion about the competence of management,
>
…[10 more quoted lines elided]…
>generalised 'management'.  And you never seem to notice the difference.

Doc doesn't know their managers. His comments were about managers in
general.

>And, yes, he _did_ provide an implied remedy:
>
…[6 more quoted lines elided]…
>here.

Every contract I work on involves technology I hadn't used before.
There's no hand-holding manager. If I can't get up to speed within
days, they'll find someone else who can. Doc has probably experienced
the same lack of foresight on his contracts.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2005-01-29T08:11:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ctg217$6fi$1@panix5.panix.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <f28lv01qvq2qfbvqo3hvpk3tlkrc15c1qf@4ax.com> <1106948667.066879.309510@z14g2000cwz.googlegroups.com> <sc0nv057ba39g2kurqhh42brtg3j25tkvl@4ax.com>`

```
In article <sc0nv057ba39g2kurqhh42brtg3j25tkvl@4ax.com>,
Robert Wagner  <spamblocker-robert@wagner.net> wrote:
>On 28 Jan 2005 13:44:27 -0800, "Richard" <riplin@Azonic.co.nz> wrote:

[snip]

>>The difference is that the Doc referred to _their_ managers, the small
>>specific sample that directly related to where a programmer was given
…[8 more quoted lines elided]…
>general.

Mr Wagner, perhaps it was your desire to make my words appear that way by 
a series of midsentence interruptions... but you might recall my response 
of:

'Really?  I have no idea, Mr Wagner, how you come to conclusions about 
what is sent or received... but it might be concluded with greater 
validity that people ask how to 'read a 'Cobol file'' because they never 
learned such minor details as the independence of programming languages 
and file structures... and that their management does not have the 
competence to realise that knowing such details, and others associated 
with them, might just possibly be beneficial in accomplishing a stated 
executive goal when said managers assign tasks.'

... and pay particular attention to what precedes 'management' in the 
phrase 'their management does not have the competence' as it appears to 
indicate a subset.

>
>>And, yes, he _did_ provide an implied remedy:
…[9 more quoted lines elided]…
>Every contract I work on involves technology I hadn't used before.

There is no evidence I can discern, Mr Wagner, indicating the original 
poster is anything other than an employee.

>There's no hand-holding manager.

There was no indication that such was needed, Mr Wagner... unless you 
consider management with the minimal competences I suggested to be 'hand 
holding'.

>If I can't get up to speed within
>days, they'll find someone else who can. Doc has probably experienced
>the same lack of foresight on his contracts.

Of course I have, Mr Wagner... but I did not consider that experience to 
be of relevance here.  It is one thing to use the right tool for the right 
job, as I indicated was not being done... quite another to expect an 
employee to be a consultant.

DD
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 16)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-29T19:26:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o8mnv0phfr7lr8m3qphincjk72fhmkmkpb@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <f28lv01qvq2qfbvqo3hvpk3tlkrc15c1qf@4ax.com> <1106948667.066879.309510@z14g2000cwz.googlegroups.com> <sc0nv057ba39g2kurqhh42brtg3j25tkvl@4ax.com> <ctg217$6fi$1@panix5.panix.com>`

```
On 29 Jan 2005 08:11:03 -0500, docdwarf@panix.com wrote:


>Mr Wagner, perhaps it was your desire to make my words appear that way by 
>a series of midsentence interruptions... but you might recall my response 
…[13 more quoted lines elided]…
>indicate a subset.

When people ask how to read a 'Cobol file', I'll let YOU tell them
their manager let them down. The tact you use mightl be instructive to
all.


>>Every contract I work on involves technology I hadn't used before.
>
>There is no evidence I can discern, Mr Wagner, indicating the original 
>poster is anything other than an employee.

I see. If a consultant asks, we'll just tell him or her how to read
the file.

>>If I can't get up to speed within
>>days, they'll find someone else who can. Doc has probably experienced
…[5 more quoted lines elided]…
>employee to be a consultant.

There are places willing to pay tens of thousands to consultants doing
it the hard way, but balk at paying a few hundred for the right tool.
It comes out of a different budget and goes through a different
approval process.  I typically mention the tool once, but if they're
not interested, I do it their way. If I insisted, they wouldn't be
grateful, they'd say someithing like 'That Wagner wouldn't shut up
until we got Toad Xpert. Then he used it for less than a week to
optimize the databases. What a waste of $2,000."
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 17)_

- **From:** docdwarf@panix.com
- **Date:** 2005-01-30T08:22:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ctin3b$9u5$1@panix5.panix.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <sc0nv057ba39g2kurqhh42brtg3j25tkvl@4ax.com> <ctg217$6fi$1@panix5.panix.com> <o8mnv0phfr7lr8m3qphincjk72fhmkmkpb@4ax.com>`

```
In article <o8mnv0phfr7lr8m3qphincjk72fhmkmkpb@4ax.com>,
Robert Wagner  <spamblocker-robert@wagner.net> wrote:
>On 29 Jan 2005 08:11:03 -0500, docdwarf@panix.com wrote:
>
…[19 more quoted lines elided]…
>their manager let them down.

Mr Wagner, I'm sure you have a Very Good Reason for thinking that someone 
might need your permission for such an activity... so, by all means, feel 
free to relate what it is that causes you to believe that anyone in this 
forum might require anything resembling your say-so for their actions for 
reasons outside of, say, amusement.

>The tact you use mightl be instructive to
>all.
…[3 more quoted lines elided]…
>>

>>There is no evidence I can discern, Mr Wagner, indicating the original 
>>poster is anything other than an employee.
>
>I see. If a consultant asks, we'll just tell him or her how to read
>the file.

No, Mr Wagner, if a consultant asks you'll be able to tell him that you 
have been in the same boat... what fun!

>
>>>If I can't get up to speed within
…[11 more quoted lines elided]…
>approval process.

The end-result is no different than if it came down of a mountain engraved 
on a stone tablet, Mr Wagner; the processes by which the organisation 
voluntarily chooses to run it'sself cause difficulties when it comes to 
accomplishing a task.  The Anciente Wisdome has it that:

'Doc, it hoits when I do dis!'

... is appropriately responded-to with

'So... don't do dat!'

>I typically mention the tool once, but if they're
>not interested, I do it their way. If I insisted, they wouldn't be
>grateful, they'd say someithing like 'That Wagner wouldn't shut up
>until we got Toad Xpert. Then he used it for less than a week to
>optimize the databases. What a waste of $2,000."

If you choose to work in places with this kind of vision, Mr Wagner, then 
you'll get all kinds of lovely stories to tell.  A classic has the 
punchline of:

Hitting maching:                  $25.00
Knowing where to hit machine: $99,974.00

DD
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 15)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-29T09:50:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107021010.345596.297120@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<sc0nv057ba39g2kurqhh42brtg3j25tkvl@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com> <ctdd7a$3bb$1@panix5.panix.com> <biokv0pn1tuns3kicugp4uei5bu3e9nhqc@4ax.com> <ctducp$1n7$1@panix5.panix.com> <f28lv01qvq2qfbvqo3hvpk3tlkrc15c1qf@4ax.com> <1106948667.066879.309510@z14g2000cwz.googlegroups.com> <sc0nv057ba39g2kurqhh42brtg3j25tkvl@4ax.com>`

```
> Doc doesn't know their managers.

Doc's comments show that he uses the evidence of the employees having
to ask here to conclude that _their_ managers did not act competently
in providing access to such information themselves when assigning the
task.

No more is needed to fit his _actual_ claim (rather than the one you
attempt to assign to him).

> His comments were about managers in general.

He has been quite specific with 'their'.  It may be that you have
difficulty in distinguishing between the specific and the general, to
the point where you extrapolate from your rather limited experience to
the completely general, but most of us restrict our comments to be
within our actual observation.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2005-01-28T19:53:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ctemq2$j79$1@panix5.panix.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <biokv0pn1tuns3kicugp4uei5bu3e9nhqc@4ax.com> <ctducp$1n7$1@panix5.panix.com> <f28lv01qvq2qfbvqo3hvpk3tlkrc15c1qf@4ax.com>`

```
In article <f28lv01qvq2qfbvqo3hvpk3tlkrc15c1qf@4ax.com>,
Robert Wagner  <spamblocker-robert@wagner.net> wrote:
>On 28 Jan 2005 12:56:41 -0500, docdwarf@panix.com wrote:
>
…[19 more quoted lines elided]…
>programmers work on a remedy.

That's curious... I have worked in shops, Mr Wagner, where the programmers 
instinctively asked 'who did this?' and the managers asked 'who can fix 
this?'; experience in such a place seems to be absent from your view of 
the world and thus might explain a particular shortsightedness.

>You offered an opinion about the
>competence of management, and nothing about a remedy. So yes, you're
>assigning blame.

Offering opinion about competence is assigning blame?  Interesting 
dictionary you have there, Mr Wagner... perhaps some day it might be other 
than a completely idiosyncratic one; I'll try to abide, for the nonce, by 
the definitions supplied by the OED.

DD
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 14)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-01-29T04:27:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZgEKd.3887$JO2.646@tornado.tampabay.rr.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <biokv0pn1tuns3kicugp4uei5bu3e9nhqc@4ax.com> <ctducp$1n7$1@panix5.panix.com> <f28lv01qvq2qfbvqo3hvpk3tlkrc15c1qf@4ax.com> <ctemq2$j79$1@panix5.panix.com>`

```
>> Robert Wagner  <spamblocker-robert@wagner.net> wrote:
>docdwarf@panix.com wrote:

> That's curious... I have worked in shops, Mr Wagner, where the programmers
> instinctively asked 'who did this?' and the managers asked 'who can fix
> this?'; experience in such a place seems to be absent from your view of
> the world and thus might explain a particular shortsightedness.

>>You offered an opinion about the
>>competence of management, and nothing about a remedy. So yes, you're
>>assigning blame.

> Offering opinion about competence is assigning blame?  Interesting
> dictionary you have there, Mr Wagner... perhaps some day it might be other
…[3 more quoted lines elided]…
> DD

Maybe you're not assigning blame, but you're assigning responsibility.  With 
that responsibility you have associated a level of incompetence.
It goes if you cannot perform your responsibilities in a competent manner, 
then there is a fault.  Anywhere there is a fault there is blame.

The blame has to be applied to management - that is where the incompetence 
lies.  It's Peter and his Principles again.

JCE
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2005-01-29T08:21:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ctg2kv$t7a$1@panix5.panix.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <f28lv01qvq2qfbvqo3hvpk3tlkrc15c1qf@4ax.com> <ctemq2$j79$1@panix5.panix.com> <ZgEKd.3887$JO2.646@tornado.tampabay.rr.com>`

```
In article <ZgEKd.3887$JO2.646@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
>>> Robert Wagner  <spamblocker-robert@wagner.net> wrote:
>>docdwarf@panix.com wrote:
…[19 more quoted lines elided]…
>then there is a fault.  Anywhere there is a fault there is blame.

Neatly spun... but not quite.  A fault can be a simple weakness, an 
absence or lack; as such it seems a matter of existence and outside of 
responsibility.  Consider the geographic use of the term.

>
>The blame has to be applied to management - that is where the incompetence 
>lies.  It's Peter and his Principles again.

In the sense of 'the competent person chooses a tool which is capable of 
accomplishing the task' there is no blame to be applied... unless the task 
does not get accomplished.

DD
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 16)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-01-30T07:19:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bU%Kd.8774$JF2.8393@tornado.tampabay.rr.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <f28lv01qvq2qfbvqo3hvpk3tlkrc15c1qf@4ax.com> <ctemq2$j79$1@panix5.panix.com> <ZgEKd.3887$JO2.646@tornado.tampabay.rr.com> <ctg2kv$t7a$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:ctg2kv$t7a$1@panix5.panix.com...
> In article <ZgEKd.3887$JO2.646@tornado.tampabay.rr.com>,
> jce <defaultuser@hotmail.com> wrote:
…[8 more quoted lines elided]…
> responsibility.  Consider the geographic use of the term.

I agree, but not quite. In the world of your comment on "their management" 
you stated that the fault was not recognizing the need for a specific skill 
in completing an assigned task.
When your job is to manage allocation of skills to match the task, and you 
fail, then this is a fault to which we *should* attach responsibility.

>>The blame has to be applied to management - that is where the incompetence
>>lies.  It's Peter and his Principles again.
…[3 more quoted lines elided]…
> does not get accomplished.

It is ironic that the opposite does not follow.  I see blame even when the 
task is accomplished!

JCE
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 17)_

- **From:** docdwarf@panix.com
- **Date:** 2005-01-30T08:41:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ctio6h$a26$1@panix5.panix.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <ZgEKd.3887$JO2.646@tornado.tampabay.rr.com> <ctg2kv$t7a$1@panix5.panix.com> <bU%Kd.8774$JF2.8393@tornado.tampabay.rr.com>`

```
In article <bU%Kd.8774$JF2.8393@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
>
><docdwarf@panix.com> wrote in message news:ctg2kv$t7a$1@panix5.panix.com...
…[14 more quoted lines elided]…
>in completing an assigned task.

I am not sure to what, exactly, you are referring... but in the 'world of 
my comment on 'their management' I stated:

--begin quoted text:

Really?  I have no idea, Mr Wagner, how you come to conclusions about what
is sent or received... but it might be concluded with greater validity
that people ask how to 'read a 'Cobol file'' because they never learned
such minor details as the independence of programming languages and file
structures... and that their management does not have the competence to
realise that knowing such details, and others associated with them, might
just possibly be beneficial in accomplishing a stated executive goal when
said managers assign tasks.

--end quoted text

... there's mention of competence, certainly, but not of fault.

>When your job is to manage allocation of skills to match the task, and you 
>fail, then this is a fault to which we *should* attach responsibility.

Perhaps so... but this is not a world in which 'should' equals 'is'... and 
managers get *their* assignments from someplace, last I looked; the plaque 
reading 'The Buck Stops Here' is well-known for being on an Executive's 
desk.

>
>>>The blame has to be applied to management - that is where the incompetence
…[7 more quoted lines elided]…
>task is accomplished!

Nothing new in that... from 
<http://groups.google.co.uk/groups?selm=34A85055.535%40erols.com&output=gplain>

--begin quoted text:

Hmmmm... decades back, when I got my First Job, my sainted Mother, may she 
sleep with the angels, gave me the following sage counsel:

'Then it comes to work remember two things:  you can be wrong about 
something... and be fired for it; you can be right about something... and 
be fired for it.'

Perhaps you are related to her... what was your grannie's milkman's name?

--end quoted text

(Note of interest - over seven years after first posting this I notice 
that I mis-typed her initial word of 'When' as 'Then')

DD
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 18)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-01-30T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<X8aLd.9033$JF2.4476@tornado.tampabay.rr.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <ZgEKd.3887$JO2.646@tornado.tampabay.rr.com> <ctg2kv$t7a$1@panix5.panix.com> <bU%Kd.8774$JF2.8393@tornado.tampabay.rr.com> <ctio6h$a26$1@panix5.panix.com>`

```
<docdwarf@panix.com> wrote in message news:ctio6h$a26$1@panix5.panix.com...
> In article <bU%Kd.8774$JF2.8393@tornado.tampabay.rr.com>,
> jce <defaultuser@hotmail.com> wrote:

>>When your job is to manage allocation of skills to match the task, and you
>>fail, then this is a fault to which we *should* attach responsibility.
…[4 more quoted lines elided]…
> desk.
This is the Peter and hit Principle...I interpret 'their management' with 
the implicit 'chain' (those in charge).
Perhaps another fine example of one not taking the exact literal of your 
meaning !

I also assumed that you - being of integrity - would attach blame where it 
*should* be thereby making it *is*.
Perhaps yet another fine example of one not taking the exact literal of your 
meaning !

>>>>The blame has to be applied to management - that is where the 
>>>>incompetence
…[22 more quoted lines elided]…
> Perhaps you are related to her... what was your grannie's milkman's name?
My gran lived in the WW II, she couldn't afford milk so she didn't have a 
milkman....maybe the same postman.

Also, if I wanted to DD you (don't go after me like the Tivo anti 
brand-as-verb execs) I would lustfully point out that I didn't say that you 
could be fired for being right.  I said you could receive blame for 
executing something successfully.  But, as the provided advice was sage, and 
predated this thread, I will let it go :-)

> --end quoted text
>
> (Note of interest - over seven years after first posting this I notice
> that I mis-typed her initial word of 'When' as 'Then')
And no one corrected you? Geez...the internet was no fun back then

> DD
I have to say that the sage counsel was made up of wise words indeed. 
Hmmm...the words are not wise....but the counsel was wise.....you know what 
I mean :)

JCE
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 19)_

- **From:** docdwarf@panix.com
- **Date:** 2005-01-30T21:59:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ctk6ue$lg4$1@panix5.panix.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <bU%Kd.8774$JF2.8393@tornado.tampabay.rr.com> <ctio6h$a26$1@panix5.panix.com> <X8aLd.9033$JF2.4476@tornado.tampabay.rr.com>`

```
In article <X8aLd.9033$JF2.4476@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
><docdwarf@panix.com> wrote in message news:ctio6h$a26$1@panix5.panix.com...
>> In article <bU%Kd.8774$JF2.8393@tornado.tampabay.rr.com>,
…[12 more quoted lines elided]…
>meaning !

Eh?  When one states 'a fish rots from the head' it might not an 
invitation to expound on refrigerating seafood, no.

>
>I also assumed that you - being of integrity - would attach blame where it 
>*should* be thereby making it *is*.

Your assumptions and my integrity aside... there are things about which I 
am unsure, hence my tendency to use the subjunctive.

>Perhaps yet another fine example of one not taking the exact literal of your 
>meaning !

Refrigeration is needed for seafood because a fish... oh, never mind.

>
>>>>>The blame has to be applied to management - that is where the 
…[25 more quoted lines elided]…
>milkman....maybe the same postman.

There's more than one way to make sure the male's delivered, aye.

>
>Also, if I wanted to DD you (don't go after me like the Tivo anti 
…[3 more quoted lines elided]…
>predated this thread, I will let it go :-)

How generous of you.

>
>> --end quoted text
…[8 more quoted lines elided]…
>I mean :)

As Wittgenstein puts it, 'I cannot know what you mean, only what you say'.

DD
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 14)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-29T12:36:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hipmv0djd3bcieikf0egbt193i35kagenq@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <biokv0pn1tuns3kicugp4uei5bu3e9nhqc@4ax.com> <ctducp$1n7$1@panix5.panix.com> <f28lv01qvq2qfbvqo3hvpk3tlkrc15c1qf@4ax.com> <ctemq2$j79$1@panix5.panix.com>`

```
On 28 Jan 2005 19:53:22 -0500, docdwarf@panix.com wrote:

>In article <f28lv01qvq2qfbvqo3hvpk3tlkrc15c1qf@4ax.com>,
>Robert Wagner  <spamblocker-robert@wagner.net> wrote:
…[26 more quoted lines elided]…
>the world and thus might explain a particular shortsightedness.

I _have_ seen that reversal of roles, typically from older programmers
who thought they had a sinecure. They're the ones who look like deer
in headlights when the company is acquired and I arrive to convert
mainframe systems to Unix.

>>You offered an opinion about the
>>competence of management, and nothing about a remedy. So yes, you're
…[5 more quoted lines elided]…
>the definitions supplied by the OED.

My definitions are influenced by real world experience .. at companies
that make Dilbert's employer look progressive. Places unfamiliar with
the word 'nepotism' but adept in its practice.
-------------------------------

While we're on the topoc of vocabulary, I compiled this list
describing netizens:

rectitudinarian: A person obsessed with personal sanctimony (also
tight-ass).
unco guid (scottish epithet): A prim-and-proper puritan.
antithalian: Against enjoyment.
wowser (Australian): A nagging puritan hung up on banning petty
    amusements that others enjoy.
peccatophobe: One who worries about having committed a sin or
imaginary crime. Has a strong sense of right and wrong, clean and
dirty.
atelophobe: A perfectionist unable to reconcile personal imperfections
    with his ideal vision.
asthenophobe: A person afraid to admit weakness of any sort. Usually
    found in the military and board rooms. Also macho men.
solifidian: One who believes that faith alone is sufficient for
salvation.
ablutomania: A mania for washing oneself.
facticide: One who twists facts, doctors data, tells half-truths &
white lies.
solipsist: One who places himself at the center of the universe. A
    solipsist does not necessarily think himself superior to others,
    he is impenetrably oblivious to others unless they annoy him.
sophomania: Delusion of exceptional intelligence.
morosoph: An over-educated pedantic jerk and erudite ass.
misologist: One who hates rational discussion and honest
agrumentation. Most misologists are stupider than they look.
hobberdehoy: A youth entering manhood.
hagiarchy: Government by religious types.
pornocracy: Government by prostitutes.
philodox: One who loves his own opinions.
Dogberry: A smug official who who is an bone-headed, inept busybody
    (from a constable in Shakespeare's "Much Ado About Nothing").
energumen: An individual who is fanatical about one issue.
marplot: The well-meaning interferer whose efforts only hinder a
project.
stormy petrel: One who starts arguments, fights, wars. A troublemaker.
polypragmatist: A busybody.
badaud: A self-confident ignoramus who believes and repeats anything.
gobemouche: A gullible rube who will believe anything.
kvetch: A constant complainer.
cacographer: A terrible speller whose English seems to be written
phonetically and modeled on restroom graffiti.
abacedarian: One learning the alphabet, a beginner.
logomachist: One who constantly asks for definitions of words.
parvanimity: A petty or mean person endowed with smallness of mind.
ferbissener (fem: ferbisseneh): A sour, embittered person. The only
time ferbisseners light up a room is when their clothes are on fire.
criticaster: A third-rate critic of others' ideas, has none of his
own.
catagelophobe: A thin-skinned person overly sensitive to criticism.
malapert: One who likes to shock with saucy, brasen, impudent
statements.
abuccinate: To proclaim, like a fanfare.
hierofastidia: Dislike of holy things.
mome: One who loves to use others' petty mistakes as an excuse to put
    them down. A hair-splitter.
psychasthenic: Neurotic weakling. Woody Allen without the talent.
mattoid: A semi-unhinged genius. Not quite around the bend but always
    has the turn signal on.
futilitarian: Quixotic Ralph Kramden type who embraces big ideas,
    get-rich-quick schemes, never quite making it.
ironist: One who is always saying the opposite of her words' meaning
    ("I'm SO impressed"). Has a gift for mockery. Usually female.

ultracrepidarian: One who tries to work outside his field of
knowledge, where he has no business being.
aristarch: A severe but fair critic.
lexiphane: Person with an inflated vocabulary.

Sources: "Dimboxes, Epopts and other Quidams", David Grambs
        "Mrs. Byrne's Dictionary", Josefa Heifetz Byrne
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2005-01-29T08:30:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ctg34v$cjr$1@panix5.panix.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <f28lv01qvq2qfbvqo3hvpk3tlkrc15c1qf@4ax.com> <ctemq2$j79$1@panix5.panix.com> <hipmv0djd3bcieikf0egbt193i35kagenq@4ax.com>`

```
In article <hipmv0djd3bcieikf0egbt193i35kagenq@4ax.com>,
Robert Wagner  <spamblocker-robert@wagner.net> wrote:
>On 28 Jan 2005 19:53:22 -0500, docdwarf@panix.com wrote:
>
…[31 more quoted lines elided]…
>who thought they had a sinecure.

Ahhhhh, so it *has* been in your experience, Mr Wagner, and you, for 
whatever reason, choose to ignore it when formulating your response.

>They're the ones who look like deer
>in headlights when the company is acquired and I arrive to convert
>mainframe systems to Unix.

How interesting... programmers who 'behave like management' act this 
way when the environment changes.

>
>>>You offered an opinion about the
…[9 more quoted lines elided]…
>that make Dilbert's employer look progressive.

Your definitions might be influenced by Space Aliens bombarding your head 
with alien brainwaves, Mr Wagner... but - no matter what one thinks of the 
man's politics - it might help to avoid idiosycratic definition by 
remembering the canine-amputee-ignoring riddle (often attributed to 
Abraham Lincoln) of:

'How many legs does a dog have if you call a tail a leg?'

'Four... calling a tail a leg does not make it one.'

DD
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 15)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-29T09:57:53-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107021473.412126.185440@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<hipmv0djd3bcieikf0egbt193i35kagenq@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <biokv0pn1tuns3kicugp4uei5bu3e9nhqc@4ax.com> <ctducp$1n7$1@panix5.panix.com> <f28lv01qvq2qfbvqo3hvpk3tlkrc15c1qf@4ax.com> <ctemq2$j79$1@panix5.panix.com> <hipmv0djd3bcieikf0egbt193i35kagenq@4ax.com>`

```
> They're the ones who look like deer in headlights when the company is
acquired and
> I arrive to convert mainframe systems to Unix.

No. There may be a completely different reason why they are dismayed to
see you arrive.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 16)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2005-01-29T13:17:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5rQKd.11869$Yg6.1849913@news20.bellglobal.com>`
- **In-Reply-To:** `<1107021473.412126.185440@z14g2000cwz.googlegroups.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <biokv0pn1tuns3kicugp4uei5bu3e9nhqc@4ax.com> <ctducp$1n7$1@panix5.panix.com> <f28lv01qvq2qfbvqo3hvpk3tlkrc15c1qf@4ax.com> <ctemq2$j79$1@panix5.panix.com> <hipmv0djd3bcieikf0egbt193i35kagenq@4ax.com> <1107021473.412126.185440@z14g2000cwz.googlegroups.com>`

```
Richard wrote:
>>They're the ones who look like deer in headlights when the company is
> 
…[7 more quoted lines elided]…
> 

Getting splattered over a grill is much the same on any hardware. When 
you happen to be the bunny, the finer details tend to be moot points.


Donald
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 16)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-29T22:58:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i73ov05js4h6fr9vuial3ih1gca8rj3qk6@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <biokv0pn1tuns3kicugp4uei5bu3e9nhqc@4ax.com> <ctducp$1n7$1@panix5.panix.com> <f28lv01qvq2qfbvqo3hvpk3tlkrc15c1qf@4ax.com> <ctemq2$j79$1@panix5.panix.com> <hipmv0djd3bcieikf0egbt193i35kagenq@4ax.com> <1107021473.412126.185440@z14g2000cwz.googlegroups.com>`

```
On 29 Jan 2005 09:57:53 -0800, "Richard" <riplin@Azonic.co.nz> wrote:

>> They're the ones who look like deer in headlights when the company is
>acquired and
…[3 more quoted lines elided]…
>see you arrive.

Could it be the hair? The earring? The CodeWarrior t-shirt?

Just kidding. I don't display any of those during the first month.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 11)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-28T10:26:53-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106936813.078022.148140@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<biokv0pn1tuns3kicugp4uei5bu3e9nhqc@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com> <1106905272.863816.274380@f14g2000cwb.googlegroups.com> <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com> <ctdd7a$3bb$1@panix5.panix.com> <biokv0pn1tuns3kicugp4uei5bu3e9nhqc@4ax.com>`

```
> When someone says he has a pair of files named .IND and .INX, it's
> obvious to most that he has a raw indexed file.

Your assertion was that it was 'sent'.  There is no evidence for that.

Most raw indexed files, even with MF, are incomprehensible binary.
They may have headers, deleted records, slack space, compression, and
other housekeeping data.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-01-28T21:18:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B_xKd.339405$f47.65115@news.easynews.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com> <1106905272.863816.274380@f14g2000cwb.googlegroups.com> <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com> <ctdd7a$3bb$1@panix5.panix.com> <biokv0pn1tuns3kicugp4uei5bu3e9nhqc@4ax.com>`

```
"Robert Wagner" <spamblocker-robert@wagner.net> wrote in message 
news:biokv0pn1tuns3kicugp4uei5bu3e9nhqc@4ax.com...
> On 28 Jan 2005 08:03:38 -0500, docdwarf@panix.com wrote:
<snip>>
>>Really?  I have no idea, Mr Wagner, how you come to conclusions about what
>>is sent or received...
…[3 more quoted lines elided]…
>

"have" versus "sent" is what I see as the difference.  I think that most of the 
posts (and this is just my GUESS) come from people at shops where an exsiting 
(old) COBOL program creates output - and they now want to do something 
"non-COBOL" with the file.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 9)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-01-28T14:34:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j4sKd.24208$by5.1167@newssvr19.news.prodigy.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <41F9353F.F21E948C@mb.sympatico.ca> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com> <1106905272.863816.274380@f14g2000cwb.googlegroups.com> <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com>`

```
"Robert Wagner" <spamblocker-robert@wagner.net> wrote in message
news:v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com...
> On 28 Jan 2005 01:41:12 -0800, "Richard" <riplin@Azonic.co.nz> wrote:
>
> Every week or two someone asks here how to read a 'Cobol file',
> because someone sent a raw file.

And every week or two I send them to my tutorial on this subject at:

http://www.talsystems.com/tsihome_html/downloads/C2IEEE.htm

It's old, it's visually unappealing, but by golly, it tells you what you
need to know.

(Oh, sorry, I forgot the most important thing considering the clientele
here: it's free).
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2005-01-28T09:45:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ctdj72$fvf$1@panix5.panix.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <1106905272.863816.274380@f14g2000cwb.googlegroups.com> <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com> <j4sKd.24208$by5.1167@newssvr19.news.prodigy.com>`

```
In article <j4sKd.24208$by5.1167@newssvr19.news.prodigy.com>,
Michael Mattias <michael.mattias@gte.net> wrote:

[snip]

>(Oh, sorry, I forgot the most important thing considering the clientele
>here: it's free).

... and worth at least double what you charge for it, too!

DD
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 11)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-01-28T15:32:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aWsKd.24218$by5.18572@newssvr19.news.prodigy.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <1106905272.863816.274380@f14g2000cwb.googlegroups.com> <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com> <j4sKd.24208$by5.1167@newssvr19.news.prodigy.com> <ctdj72$fvf$1@panix5.panix.com>`

```
<docdwarf@panix.com> wrote in message news:ctdj72$fvf$1@panix5.panix.com...
> In article <j4sKd.24208$by5.1167@newssvr19.news.prodigy.com>,
> Michael Mattias <michael.mattias@gte.net> wrote:
…[6 more quoted lines elided]…
> ... and worth at least double what you charge for it, too!

Well, I guess in a group this size one must expect at least one person of
dubious legitimacy of birth.

MCM
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2005-01-28T10:37:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ctdm7g$72r$1@panix5.panix.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <j4sKd.24208$by5.1167@newssvr19.news.prodigy.com> <ctdj72$fvf$1@panix5.panix.com> <aWsKd.24218$by5.18572@newssvr19.news.prodigy.com>`

```
In article <aWsKd.24218$by5.18572@newssvr19.news.prodigy.com>,
Michael Mattias <michael.mattias@gte.net> wrote:
><docdwarf@panix.com> wrote in message news:ctdj72$fvf$1@panix5.panix.com...
>> In article <j4sKd.24208$by5.1167@newssvr19.news.prodigy.com>,
…[10 more quoted lines elided]…
>dubious legitimacy of birth.

It was a cheap shot, Mr Mattias, I will agree... but I could *not* resist.

DD
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 9)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-28T10:19:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106936384.172406.113700@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <8v5ev090uc9u1i6jehg93urcjehoncesj6@4ax.com> <1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <41F9353F.F21E948C@mb.sympatico.ca> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com> <1106905272.863816.274380@f14g2000cwb.googlegroups.com> <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com>`

```
> Every week or two someone asks here how to read a 'Cobol file',
> because someone sent a raw file.

No.  I see no evidence that the files were 'sent'.  Mostly it is trying
to access the data in an existing system, possibly to replace it with
some VB they just knocked up.

With most systems, such as default MF on Windows, Fujitsu, RM, Accu,
mainframe; there is no point at all in trying to read the raw file, or
'send' it.  Packed would be the least of their problems.

Even with your 'mostly not junk' C-ISAM you didn't have 'sign separate'
so negatives were not easily processed.  There may only have been a few
of those so the result was probably only partly complete nonsense.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 10)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-28T21:11:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7u9lv0hlfjvjssod31ek4bl095pvak7de8@4ax.com>`
- **References:** `<1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <41F9353F.F21E948C@mb.sympatico.ca> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com> <1106905272.863816.274380@f14g2000cwb.googlegroups.com> <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com> <1106936384.172406.113700@c13g2000cwb.googlegroups.com>`

```
On 28 Jan 2005 10:19:44 -0800, "Richard" <riplin@Azonic.co.nz> wrote:

>> Every week or two someone asks here how to read a 'Cobol file',
>> because someone sent a raw file.
…[3 more quoted lines elided]…
>some VB they just knocked up.

That's true in this case. Others said the file had been sent, or is
being sent monthly.

>With most systems, such as default MF on Windows, Fujitsu, RM, Accu,
>mainframe; there is no point at all in trying to read the raw file, or
>'send' it.  Packed would be the least of their problems.

Reading the raw file with a MF program or tool is the only practical
solution (unless it's C-ISAM). Even though the format is obsolete, MF
is good about backward compatibility.

>Even with your 'mostly not junk' C-ISAM you didn't have 'sign separate'
>so negatives were not easily processed.  There may only have been a few
>of those so the result was probably only partly complete nonsense.

Negatives are easily fixed with a text editor. Mark the column, find
within scope, run macro to convert number and place dash in front of
field.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 11)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-28T14:03:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106949820.301971.81630@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<7u9lv0hlfjvjssod31ek4bl095pvak7de8@4ax.com>`
- **References:** `<1106770871.029233.48300@c13g2000cwb.googlegroups.com> <dg3gv0l2o2jecr3gu0k88r5utp0gablfm9@4ax.com> <1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <41F9353F.F21E948C@mb.sympatico.ca> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com> <1106905272.863816.274380@f14g2000cwb.googlegroups.com> <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com> <1106936384.172406.113700@c13g2000cwb.googlegroups.com> <7u9lv0hlfjvjssod31ek4bl095pvak7de8@4ax.com>`

```
> That's true in this case. Others said the file had been sent, or is
> being sent monthly.

You just make stuff up.

> Reading the raw file with a MF program or tool is the only practical
> solution (unless it's C-ISAM).

No. _Even_ if it is C-ISAM.  Apart from COMP or COMP-3 fields, there
are also deleted records and junk in slack space.  These will cause
records to be incorrectly read.

There also may be issues with negative numbers even if they are
display.

> Negatives are easily fixed with a text editor. Mark the column, find
> within scope, run macro to convert number and place dash in front of
> field.

Is this what your dumb users did when you sent them a C-ISAM file ?
Did you send a note explaining where the sign was and the values ?  Did
you write the macro for them ?  When the dash was 'added in front' did
this misalign the fields ?  or did it potentially overwrite the high
order digit ?

Given that you didn't seem to know about the problem with deleted
records (it took several messages before you realised there was a
problem) and you just made up this 'macro' I suspect your users just
gave up when you sent them a raw file that was to them 'junk'.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 12)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-29T06:55:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t7cmv0p0fg842ffl5jf5mkdod1mfoub4aq@4ax.com>`
- **References:** `<1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <41F9353F.F21E948C@mb.sympatico.ca> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com> <1106905272.863816.274380@f14g2000cwb.googlegroups.com> <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com> <1106936384.172406.113700@c13g2000cwb.googlegroups.com> <7u9lv0hlfjvjssod31ek4bl095pvak7de8@4ax.com> <1106949820.301971.81630@z14g2000cwz.googlegroups.com>`

```
On 28 Jan 2005 14:03:40 -0800, "Richard" <riplin@Azonic.co.nz> wrote:

>> That's true in this case. Others said the file had been sent, or is
>> being sent monthly.
>
>You just make stuff up.

Ordinarily, I might dig through the archives for substantiation. At
the moment I'm in the midst of a move to the frozen North
(Minneapolis) so don't have the time.

>> Negatives are easily fixed with a text editor. Mark the column, find
>> within scope, run macro to convert number and place dash in front of
…[6 more quoted lines elided]…
>order digit ?

I wouldn't send raw files. That's what I did when I was on the
receiving end.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 13)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-29T10:02:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107021300.258541.45550@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<t7cmv0p0fg842ffl5jf5mkdod1mfoub4aq@4ax.com>`
- **References:** `<1106799583.186458.156030@c13g2000cwb.googlegroups.com> <m82hv0plfks6lq3k2uheo3cqer9qfvs2u0@4ax.com> <41F9353F.F21E948C@mb.sympatico.ca> <prcjv098u8l00i1gcouau5fbh4v2gsb377@4ax.com> <1106905272.863816.274380@f14g2000cwb.googlegroups.com> <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com> <1106936384.172406.113700@c13g2000cwb.googlegroups.com> <7u9lv0hlfjvjssod31ek4bl095pvak7de8@4ax.com> <1106949820.301971.81630@z14g2000cwz.googlegroups.com> <t7cmv0p0fg842ffl5jf5mkdod1mfoub4aq@4ax.com>`

```
>>> That's true in this case. Others said the file had been sent, or is
>>> being sent monthly.

>>You just make stuff up.

> Ordinarily, I might dig through the archives for substantiation. At
> the moment I'm in the midst of a move to the frozen North
> (Minneapolis) so don't have the time.

Yeah, right.

Actually I _did_ have a search before I posted that 'you make stuff
up', and I did find a reference to 'a file being sent monthly', but
this was an aside and was not from someone who asked about how to
determine the format.
You were just confused, but it doesn't stop you being adamant.
```

###### ↳ ↳ ↳ Re: OT (Maybe): ERPs

_(reply depth: 9)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-01-28T20:53:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Pi8NGIeflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1106700322.262099.153590@c13g2000cwb.googlegroups.com> <1106905272.863816.274380@f14g2000cwb.googlegroups.com> <v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com>`

```
.    On  28.01.05
  wrote  spamblocker-robert@wagner.net (Robert Wagner)
     on  /COMP/LANG/COBOL
     in  v5dkv0d9c4c4fokh4goj9sqbu1cageuitp@4ax.com
  about  Re: OT (Maybe): ERPs


RW> Every week or two someone asks here how to read a 'Cobol file',
RW> because someone sent a raw file.

   But this is not for data exchange, but for conversion of the  
application from COBOL to some other environment.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Man stattete ihm sehr heiï¿½en, schon etwas verbrannten Dank ab. -G.C.Lichtenberg
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
