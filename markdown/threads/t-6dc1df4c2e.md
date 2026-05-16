[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Legacy migration to latest technologies!

_16 messages · 13 participants · 2003-05_

**Topics:** [`COBOL's future, legacy, and obsolescence`](../topics.md#future) · [`Migration and conversion`](../topics.md#migration)

---

### Legacy migration to latest technologies!

- **From:** cobolmig@yahoo.com (Mike)
- **Date:** 2003-05-01T09:09:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f972a42b.0305010809.af0cdee@posting.google.com>`

```
Hello,

What are the different options available to migrate mainframe based
Cobol applications to latest technologies?

What are the tools available to migrate data, screens, programs?

What is the best strategy?

Really appreciate your experience, knowledge and input on this matter.

Thanks in advance.

Mike
```

#### ↳ Re: Legacy migration to latest technologies!

- **From:** "Danny Maijer" <info@liveartists.com>
- **Date:** 2003-05-01T20:22:40+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8roio$gob$1@reader10.wxs.nl>`
- **References:** `<f972a42b.0305010809.af0cdee@posting.google.com>`

```
Wow Mike,

Such a simple (?) question and so many answers......

Migrate mainframe based Cobol applications to latest technology.....Like
porting mainframe Cobol to J2EE or C# in a W2K or later environment
including migration of the legacy data structures to a relational database
environment ? (Do you really want that ? If so, prepare yourself for
disaster).

COBOL applications can be hauled over to modern environments however, and
integrated with software developed using modern technology (is like a more
smooth and secure path). Even a GUI can be put over the old green-screens.
The least you win by doing so is reduction of maintenance costs on old hard-
and software (which, as you will be aware of, is HUGE). Not to mention a
higher acceptance level of the application with their users.

In time you can phase out the "old" software by gradually replacing parts of
it with new modules developed in <whatever is the latest technology then>
.....In several renewal projects we have used this approach to great
satisfaction of our customers.

Most legacy vendors (provided they still exist) offer a way to port software
to new OS's and databases. All depends upon what platform you are on right
now and where you want to go....(or where the vendor wants you to go, take
care on commercial advice on the subject....).

To make your question a little bit more easy to answer by this group, a
specification of what your platform is now (OS, DB Application type and
COBOL dialect) and where you want (or need) to go would be most welcome.

Regards, Danny.



"Mike" <cobolmig@yahoo.com> schreef in bericht
news:f972a42b.0305010809.af0cdee@posting.google.com...
> Hello,
>
…[11 more quoted lines elided]…
> Mike
```

#### ↳ Re: Legacy migration to latest technologies!

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-05-01T13:26:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cXSdnV4W5OpJ-yyjXTWJkQ@giganews.com>`
- **References:** `<f972a42b.0305010809.af0cdee@posting.google.com>`

```

"Mike" <cobolmig@yahoo.com> wrote in message
news:f972a42b.0305010809.af0cdee@posting.google.com...
> Hello,
>
…[11 more quoted lines elided]…
> Mike

Recompile your COBOL programs on the PC - make a few changes.

Now you have your applications running in a PC environment. All the rest is
enhancement.
```

#### ↳ Re: Legacy migration to latest technologies!

- **From:** "Thomas A. Li" <tli@corporola.com>
- **Date:** 2003-05-01T19:36:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SGesa.69083$kYH.27243@news01.bloor.is.net.cable.rogers.com>`
- **References:** `<f972a42b.0305010809.af0cdee@posting.google.com>`

```
What are the different options available to migrate mainframe based Cobol
applications to latest technologies?

There are a lot of options:
    keep Cobol code, recompile it on a new platform
    keep Cobol binary and the machine, call it by IPC, service, or wharever
application level interfae
    change Cobol source code into another kind of source code, like java
    compile cobol code into another kind of binary, like Java .class or C#
.dll
    maybe you can migrate from binary into binary
Our company do the source code to source code migration, because the code is
maintainable and we can go beyond Cobol.

What are the tools available to migrate data, screens, programs?

Search over the web, you will find some tools. We also provide both
automatic and manual tools for COBOL to Java source code migration.

What is the best strategy?

No best because different people have different requirements in different
environment.
Even the lastest technologies is not unique.


Thomas
"Mike" <cobolmig@yahoo.com> wrote in message
news:f972a42b.0305010809.af0cdee@posting.google.com...
> Hello,
>
…[11 more quoted lines elided]…
> Mike
```

#### ↳ Re: Legacy migration to latest technologies!

- **From:** Steve Thompson <n_o_spam.steve_t@ix.netcom.com>
- **Date:** 2003-05-01T17:20:28-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EB18F9C.60405@ix.netcom.com>`
- **References:** `<f972a42b.0305010809.af0cdee@posting.google.com>`

```
Mike wrote:
> Hello,
> 
…[11 more quoted lines elided]…
> Mike

First, before this is attempted, there are a few things that need 
to be examined.

1) If you are on the G6 chipset and above on the IBM mainframes, 
the CPU bus width is 256 bytes, not 16/32/64 bits.

2) The I/O capacity of ANY IBM mainframe (or similarly 
architected computer) is x channels having y devices. Each 
channel (ESCON & FICON) can transfer data bi-directionally 
to/from C-Store (RAM to the Intel crowd) at the SAME time the 
CPU(s) are accessing C-Store.

3) The IBM mainframe can have 1 to 16+ CPUs working against 
C-Store of up to 16GB (this actually depends on the model of the 
machine, number of LPARs and a few other things).

4) The mainframe is true 64 bit, not pseudo 64 bit. The only 
limitation on C-Store (RAM) is propagation speeds, which is why 
we can't go to the ExaByte level today.

5) The mainframe is rather stable, with old applications able to 
run under the new releases of the SCP (O/S) and communicate with 
new applications/systems w/o having to be modified for this to work.

What all this means is, GiGE connectivity does not give you 
anywhere near the interconnectivity of the internal bus of a 
mainframe. This means that you can put n AIX machines out there 
with y NT machines out there, each dedicated to some application, 
data base, web server, etc., and you will NEVER be able to handle 
the scalability of the mainframe. But you will pay for the 
privilege of proving me correct. And, you will join the ranks of 
companies that have spent > US$50M to realize that it just won't 
work.
```

##### ↳ ↳ Re: Legacy migration to latest technologies!

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2003-05-02T05:32:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EB2033E.99E31E4F@worldnet.att.net>`
- **References:** `<f972a42b.0305010809.af0cdee@posting.google.com> <3EB18F9C.60405@ix.netcom.com>`

```
Steve Thompson wrote:
> (snip)
> 3) The IBM mainframe can have 1 to 16+ CPUs working against
…[5 more quoted lines elided]…
> we can't go to the ExaByte level today.

I recently attended an internal seminar on zArchitecture and was told
that a z900 mainframe can support 64 gigabytes of real memory plus 128
gigabytes virtual memory right now.
```

#### ↳ Re: Legacy migration to latest technologies!

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-05-02T10:02:29+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb19985_2@127.0.0.1>`
- **References:** `<f972a42b.0305010809.af0cdee@posting.google.com>`

```

"Mike" <cobolmig@yahoo.com> wrote in message
news:f972a42b.0305010809.af0cdee@posting.google.com...
> Hello,
>
> What are the different options available to migrate mainframe based
> Cobol applications to latest technologies?
>

Depends...


> What are the tools available to migrate data, screens, programs?
>

Depends...

> What is the best strategy?
>

Depends...

> Really appreciate your experience, knowledge and input on this matter.
>

As this is an area where I sell my expertise, having done a number of such
migrations successfully for major corporations and developed tools to
specifically assist in the migration, you don't really think I'm going to
give you the answers for nothing do you <G>?

You will receive a lot of free advice here. It is worth the price.

Seriously, there are a number of things regarding your migration which you
CAN research via the web and in Newsgroups like this one. But in the final
analysis if you want to avoid the pitfalls and learn by other people's
experience you will need to get competent advice, pertinent to your specific
environment, business, and applications, from experienced consultants.

There is a cost in migrating, and this is part of it.

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

#### ↳ Re: Legacy migration to latest technologies!

- **From:** "Anon" <anon@anon.org>
- **Date:** 2003-05-01T17:10:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8s60u$66b$1@ngspool-d02.news.aol.com>`
- **References:** `<f972a42b.0305010809.af0cdee@posting.google.com>`

```
> What are the different options available to migrate mainframe based
> Cobol applications to latest technologies?

  Please explain first WHAT these "latest technologies" are and
  WHY you want to migrate to them?

  WHAT is it that makes these "latest technologies" better than
  what you currently have on the mainframe?

> What are the tools available to migrate data, screens, programs?

  Answer the above first. There are a zillion "tools".

> What is the best strategy?

  Nearly all of the supposed "latest technologies" are ALSO available
  on the mainframe with far superior performance, flexibility, security
  and at less cost. Investigate those options first. You're already on
  the mainframe. Ask yourself: Why is it better to take your applications
  off one mainframe and put them onto a whole room-full of who knows
  how many lower performing PC's and mid-ranges?

  This should be your first consideration and strategy:
  Think hard about WHY you want to this.
  What is your REAL reason and motive for this migration?
```

##### ↳ ↳ Re: Legacy migration to latest technologies!

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-02T14:31:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8tvfq$ig6$1@peabody.colorado.edu>`
- **References:** `<f972a42b.0305010809.af0cdee@posting.google.com> <b8s60u$66b$1@ngspool-d02.news.aol.com>`

```

On  1-May-2003, "Anon" <anon@anon.org> wrote:

>   Please explain first WHAT these "latest technologies" are and
>   WHY you want to migrate to them?

It doesn't matter what they are, migrate to them because they are the "latest
technologies".


>   WHAT is it that makes these "latest technologies" better than
>   what you currently have on the mainframe?

They are more modern.

>   What is your REAL reason and motive for this migration?

To be modern.
```

###### ↳ ↳ ↳ Re: Legacy migration to latest technologies!

- **From:** "Anon" <anon@anon.org>
- **Date:** 2003-05-02T16:23:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8unl0$42h$1@ngspool-d02.news.aol.com>`
- **References:** `<f972a42b.0305010809.af0cdee@posting.google.com> <b8s60u$66b$1@ngspool-d02.news.aol.com> <b8tvfq$ig6$1@peabody.colorado.edu>`

```
Well...  8-track tapes, BetaMax and The Edsel were once
the "latest technologies" too. And that's the point, both
mine and yours. Have good, well thought out business and
technical reasons for doing it. Not just because some
"latest technology" is your current favorite fad whoop-de-doo
toy to play with.


"Howard Brazee" <howard@brazee.net> wrote in message news:b8tvfq$ig6$1@peabody.colorado.edu...
>
> On  1-May-2003, "Anon" <anon@anon.org> wrote:
…[15 more quoted lines elided]…
> To be modern.
```

#### ↳ Re: Legacy migration to latest technologies!

- **From:** "anon" <no@no.com>
- **Date:** 2003-05-02T00:42:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ajsa.20591$yv1.1387268@news2.telusplanet.net>`
- **References:** `<f972a42b.0305010809.af0cdee@posting.google.com>`

```
Well, the funny thing is that the best strategy doesn't always get
implemented -- because it costs money ;)

Specifically what I've done so far:

-Moved COBOL business logic to Windows and called it as a .dll from <Windows
language x>.  This is a low cost solution.  But companies moving away from
mainframes also tend to move their employees away from mainframe
technologies (ie: COBOL); so the support for such .dlls can dwindle.
-Converted COBOL business logic to <Windows language x>.  When I do this,
the back-end is inevitably a database (ex: Oracle), so that's an added cost.

In my current contract, the entire 6 months will be spent a) converting
COBOL business logic to Java with an Oracle back-end and b) converting UNIX
C to Java.  I gave the client a Windows-COBOL/Windows C++ prototype option
but they didn't want it... even for a lower cost.

Probably doesn't help much but I thought I'd talk specifics.

--R




"Mike" <cobolmig@yahoo.com> wrote in message
news:f972a42b.0305010809.af0cdee@posting.google.com...
> Hello,
>
…[11 more quoted lines elided]…
> Mike
```

#### ↳ Re: Legacy migration to latest technologies!

- **From:** "Paul Barnett" <paul.barnett@nospam.microfocus.com>
- **Date:** 2003-05-02T10:26:16+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8tdch$k7$1@hyperion.microfocus.com>`
- **References:** `<f972a42b.0305010809.af0cdee@posting.google.com>`

```
Hi Mike,

This is a very open-ended question so I'll give brief answers to point you
in a direction to get more detailed answers:

> What are the different options available to migrate mainframe based
> Cobol applications to latest technologies?

You can take your cobol to Windows, Unix and Linux. Micro Focus has COBOL
products to support all of these.
Technologies supported include SQL, Java interoperability, COM, MTS, Web
Services, XML, EJB, HTML, etc etc.

> What are the tools available to migrate data, screens, programs?

For Windows, Net Express, for Unix and Linux, Server Express.

> What is the best strategy?

That really depends on what it is that you want to achieve.

> Really appreciate your experience, knowledge and input on this matter.
>
> Thanks in advance.
>
> Mike

www.microfocus.com
```

#### ↳ Re: Legacy migration to latest technologies!

- **From:** "Ira Baxter" <idbaxter@semdesigns.com>
- **Date:** 2003-05-02T09:07:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eb27a43$1@giga.realtime.net>`
- **References:** `<f972a42b.0305010809.af0cdee@posting.google.com>`

```

"Mike" <cobolmig@yahoo.com> wrote in message
news:f972a42b.0305010809.af0cdee@posting.google.com...
> What are the different options available to migrate mainframe based
> Cobol applications to latest technologies?

At one extreme, recompile and go depending on what OS support you
have used.

At the the other extreme, mass lanaguage change,
screen I/O paradigm change from green-screen to GUI,
DB change from network/hierarchical to RDBMS.

But you didn't provide anywhere near enough detail to
provide you a realistic list of choices.

> What are the tools available to migrate data, screens, programs?

*One* tool (ours :) is the DMS Software Reengineering Toolkit.
See http://www.semdesigns.com/Products/Services/LegacyMigration.html.

There are others, and you should consider them depending
on your circumstances.
```

#### ↳ Re: Legacy migration to latest technologies!

- **From:** "Thomas A. Li" <tli@corporola.com>
- **Date:** 2003-05-02T18:12:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Uxysa.76975$kYH.50939@news01.bloor.is.net.cable.rogers.com>`
- **References:** `<f972a42b.0305010809.af0cdee@posting.google.com>`

```
I think the problem with legacy applications on mainframes is the
maintenance and development cost:
    the cost for mainframes and accessories: small production volume and
high price
    the cost of operators and programmers: less newcomers and cost of
training
    the gap of legacy applications and modern applications requires more
workload: communication, web, db and standard issues

The facts are:
    PC is getting cheaper and more powerful
    Windows programmer is everywhere and cheap with experience
    Java programmers are even cheaper
    Windows and PC occupies majority of market

Is PC vs. mainframe = Windows vs. Unix? It is the big managers who will
decide who will win.
But in any way, someone will be the loser if only one of them is selected,
not both as now.

Get prepared with one-stone-two-bird tools.


Thomas Li




----- Original Message ----- 
From: "Ira Baxter" <idbaxter@semdesigns.com>
Newsgroups: comp.lang.cobol
Sent: Friday, May 02, 2003 10:07 AM
Subject: Re: Legacy migration to latest technologies!


>
> "Mike" <cobolmig@yahoo.com> wrote in message
…[30 more quoted lines elided]…
> ----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet
News==----
> http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000
Newsgroups
> ---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption
=---

"Mike" <cobolmig@yahoo.com> wrote in message
news:f972a42b.0305010809.af0cdee@posting.google.com...
> Hello,
>
…[11 more quoted lines elided]…
> Mike
```

##### ↳ ↳ Re: Legacy migration to latest technologies!

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-05-02T18:41:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8ue3u$p3e$1@peabody.colorado.edu>`
- **References:** `<f972a42b.0305010809.af0cdee@posting.google.com> <Uxysa.76975$kYH.50939@news01.bloor.is.net.cable.rogers.com>`

```

On  2-May-2003, "Thomas A. Li" <tli@corporola.com> wrote:

> The facts are:
>     PC is getting cheaper and more powerful
>     Windows programmer is everywhere and cheap with experience
>     Java programmers are even cheaper
>     Windows and PC occupies majority of market

That's not the comparison.

Don't compare the hardware, compare the data and the functions.   If you need a
lot of data, a lot of bandwidth, auditing, shared access, and control, you want
a truck or bus.   If you want nimble response, you want a sports car.

Enterprises need both.

After you determine your needs, buy the hardware that supports your needs the
best.
```

#### ↳ Re: Legacy migration to latest technologies!

- **From:** Ethan Schultz <ethans@RosebudUSA.com>
- **Date:** 2003-05-12T16:40:29-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EC006BD.E488306@RosebudUSA.com>`
- **References:** `<f972a42b.0305010809.af0cdee@posting.google.com>`

```
Mike,

You might also want to check out Eden Server at http://www.RosebudUSA.com


Thanks

Mike wrote:
> 
> Hello,
…[12 more quoted lines elided]…
> Mike
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
