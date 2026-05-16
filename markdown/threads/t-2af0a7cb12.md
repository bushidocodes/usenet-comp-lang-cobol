[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# offload mainframe development

_9 messages · 6 participants · 2005-04_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### offload mainframe development

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2005-04-19T10:03:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ckodoF6n7u9kU1@individual.net>`

```
Is there anyone out there who uses Microfocus Mainframe Express or CA-Realia
II Workbench to "offload" mainframe COBOL development?  I think Fujitsu may
have a product also, but I don't know its name.

Specifically, we're wondering about...

CICS emulation
VSAM emulation
DL/I database emulation (IMS?)
VSE batch JCL emulation

Is it worthwhile looking at doing this?
Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

#### ↳ Re: offload mainframe development

- **From:** "Don Leahy" <leahydon@nospamplease.netscape.net>
- **Date:** 2005-04-19T19:55:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_Tg9e.4119$9G.360704@news20.bellglobal.com>`
- **References:** `<3ckodoF6n7u9kU1@individual.net>`

```

"Frank Swarbrick" wrote in message
> Is there anyone out there who uses Microfocus Mainframe Express or 
> CA-Realia
…[12 more quoted lines elided]…
> Frank

In my opinion, no.   The cost of maintaining test environments on other 
platforms outweigh the benefits of offloading from the mainframe.

Been there, done that.  We are now in the middle of moving our test 
environments *back* to the mainframe in order to save money.  Go figure.
```

##### ↳ ↳ Re: offload mainframe development

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2005-04-20T09:25:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cnailF6nqulmU1@individual.net>`
- **References:** `<3ckodoF6n7u9kU1@individual.net> <_Tg9e.4119$9G.360704@news20.bellglobal.com>`

```
One of our current programmers mentioned that the same thing happened at his
old shop.  Not too encouraging!
Thanks,
Frank

>>> Don Leahy<leahydon@nospamplease.netscape.net> 4/19/2005 5:55:34 PM >>>

"Frank Swarbrick" wrote in message
> Is there anyone out there who uses Microfocus Mainframe Express or 
> CA-Realia
…[12 more quoted lines elided]…
> Frank

In my opinion, no.   The cost of maintaining test environments on other 
platforms outweigh the benefits of offloading from the mainframe.

Been there, done that.  We are now in the middle of moving our test 
environments *back* to the mainframe in order to save money.  Go figure.
```

###### ↳ ↳ ↳ Re: offload mainframe development

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-04-20T21:07:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pwz9e.9994$5f.7981@tornado.tampabay.rr.com>`
- **References:** `<3ckodoF6n7u9kU1@individual.net> <_Tg9e.4119$9G.360704@news20.bellglobal.com> <3cnailF6nqulmU1@individual.net>`

```
We did this a long time ago.  It worked briefly.  What ended up happening 
was *NOT* a fault of the tool or the product support but of the 
organization.

Developers do not anticipate the effort involved in maintaining environments 
(that's right - those sysadm people that you think sit in their rooms 
hacking all day, and then they complain when you have a problem).

We had developers maintain the environment.  This turned into one 
developer - the most sysadm looking one ;-) maintaining the environment, and 
this in turn become one person being support and not developing.  This was 
not considered part if his role "why aren't you developing" was the 
management question to which he had no "right" answer.

Once the support started developing again, the support went away, the 
problems were "it doesn't quite work" .  Everyone returned to terminals, 
logging on and working as per the old method....the software got dusty, the 
licence renewal came around and it lapsed without anyone noticing..

Until that point I think people thought it went fairly well.  So my 
summation is, sounds like a good idea, get an understanding of what's 
involved before you move ahead. Preparation is nearly everything. 
Rationality is the rest : why are you planning this? Not enough mainframe 
resource?

I actually have lobbied to get IBM Websphere Enterprise because I think it 
would be an environment enhancement (plus an opportunity for people to see 
other IDEs and methodologies). But then when I'm realistic I don't think it 
really would serve that well - though having an enterprise wide debugger and 
a hook into CVS/Cloud9 would be nice.

JCE


"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
news:3cnailF6nqulmU1@individual.net...
> One of our current programmers mentioned that the same thing happened at 
> his
…[31 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: offload mainframe development

_(reply depth: 4)_

- **From:** "Don Leahy" <leahydon@nospamplease.netscape.net>
- **Date:** 2005-04-20T17:53:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ebA9e.11098$Jg5.757478@news20.bellglobal.com>`
- **References:** `<3ckodoF6n7u9kU1@individual.net> <_Tg9e.4119$9G.360704@news20.bellglobal.com> <3cnailF6nqulmU1@individual.net> <pwz9e.9994$5f.7981@tornado.tampabay.rr.com>`

```
Comments interspersed.
"jce" <defaultuser@hotmail.com> wrote in message 
news:pwz9e.9994$5f.7981@tornado.tampabay.rr.com...
> We did this a long time ago.  It worked briefly.  What ended up happening 
> was *NOT* a fault of the tool or the product support but of the 
> organization.

Absolutely right.  The technology works just fine, but.....

> Developers do not anticipate the effort involved in maintaining 
> environments (that's right - those sysadm people that you think sit in 
…[7 more quoted lines elided]…
> management question to which he had no "right" answer.

The problem is that *most* developers are not technically inclined (any more 
than the minimum required to do the job) and have no interest at all in 
maintaining test environments.

> Once the support started developing again, the support went away, the 
> problems were "it doesn't quite work" .  Everyone returned to terminals, 
> logging on and working as per the old method....the software got dusty, 
> the licence renewal came around and it lapsed without anyone noticing..

Ditto.  We haven't upgraded our toolset since about 1997.

>
> Until that point I think people thought it went fairly well.  So my 
…[9 more quoted lines elided]…
> debugger and a hook into CVS/Cloud9 would be nice.

That is the road we are on now.  We are evaluating IBM's Debug Tool, a 
source code debugger that runs on the host.  Once it is in place, the last 
justification for using the Microfocus toolset (namely the ability to 
animate code) will be gone.

>
> JCE
…[39 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: offload mainframe development

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-04-20T22:58:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e8B9e.530054$za2.81906@news.easynews.com>`
- **References:** `<3ckodoF6n7u9kU1@individual.net> <_Tg9e.4119$9G.360704@news20.bellglobal.com> <3cnailF6nqulmU1@individual.net> <pwz9e.9994$5f.7981@tornado.tampabay.rr.com> <ebA9e.11098$Jg5.757478@news20.bellglobal.com>`

```
"Don Leahy" <leahydon@nospamplease.netscape.net> wrote in message 
news:ebA9e.11098$Jg5.757478@news20.bellglobal.com...
> Comments interspersed.
> "jce" <defaultuser@hotmail.com> wrote in message 
> news:pwz9e.9994$5f.7981@tornado.tampabay.rr.com...
<snip>
>> I actually have lobbied to get IBM Websphere Enterprise because I think it 
>> would be an environment enhancement (plus an opportunity for people to see 
…[8 more quoted lines elided]…
>

Don,
  As someone who has been an IBM systems programmer and application programmer 
AND who has worked for ADS (when they sold Xpediter) and for Micro Focus 
(working on "mainframe compatibility") and who has handled both SHARE and 
formerly GUIDE requirements on WSED and Debug Tool,

  Can you tell me what you think is "new" with Debug Tool that WASN'T available 
previously
    - from IBM (with COBTEST and earlier Debug Tool releases)
            and
   - Xpediter (from ADS or Compuware)
           and
  - SmarTest (sp?) (formerly Viasoft and now ???)
           and
 -  Intertest (for CICS)

            ***

I do understand (especially with older versions of the IBM, Micro Focus, 
CA-Realia, and Fujitsu products) that there were issues about each programmer 
being required to be a "systems programmer".

But I don't understand thinking that Debug Tool would (NOW) provide a reason for 
dropping Micro Focus.
```

###### ↳ ↳ ↳ Re: offload mainframe development

_(reply depth: 6)_

- **From:** "Don Leahy" <leahydon@nospamplease.netscape.net>
- **Date:** 2005-04-20T20:14:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zfC9e.11195$Jg5.784612@news20.bellglobal.com>`
- **References:** `<3ckodoF6n7u9kU1@individual.net> <_Tg9e.4119$9G.360704@news20.bellglobal.com> <3cnailF6nqulmU1@individual.net> <pwz9e.9994$5f.7981@tornado.tampabay.rr.com> <ebA9e.11098$Jg5.757478@news20.bellglobal.com> <e8B9e.530054$za2.81906@news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:e8B9e.530054$za2.81906@news.easynews.com...
<snip>
>
> Don,
…[29 more quoted lines elided]…
>
The main reason we are looking at Debug Tool rather than its competitors is 
cost.  A secondary (but possibly strategic) consideration is its integration 
with the Websphere family of products.  So, to answer your question, there 
is nothing new with Debug Tool that is driving this process.

We went down a similar road about a year ago when we dropped Abendaid in 
favour of IBM's Fault Analyzer.  Fault Analyzer isn't as easy to use as 
Abendaid, but the price is many times lower.

Cost is also one of the factors that is driving us away from Microfocus.  We 
are several years behind, and would have to spend a lot of money to upgrade 
and configure all of the software.  Our LAN people are unwilling to do it 
(doesn't fit with the 'standard image'), so we would be on our own.

Ideally, I would like us to upgrade our desktop toolkit *and* acquire a host 
debugging tool.  There are sufficient differences between the platforms that 
you will always need (IMO) a robust set of tools on each of them.
```

###### ↳ ↳ ↳ Re: offload mainframe development

_(reply depth: 7)_

- **From:** "Brian Crane" <brian.crane@microfocus.com>
- **Date:** 2005-04-22T10:17:29+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4ael1$brr$1@hyperion.microfocus.com>`
- **References:** `<3ckodoF6n7u9kU1@individual.net> <_Tg9e.4119$9G.360704@news20.bellglobal.com> <3cnailF6nqulmU1@individual.net> <pwz9e.9994$5f.7981@tornado.tampabay.rr.com> <ebA9e.11098$Jg5.757478@news20.bellglobal.com> <e8B9e.530054$za2.81906@news.easynews.com> <zfC9e.11195$Jg5.784612@news20.bellglobal.com>`

```
Hi all,

I've read this thread with interest, and I'd like to make some comments 
based on my own experiences which I hope will contribute to the discussion.

A few years ago I worked at a major bank in the UK, with my roots in 
mainframe PL/I, Assembler and COBOL programming. I was responsible for a 
rollout of Micro Focus tools across 250 mainframe developers.

What started this was we were looking at ways to speed up development (and 
maintenance) without increasing the development mainframe capacity. The 
application in question was the largest DB2 implementation in Europe at that 
time, and we were pushing the boundaries of what DB2 was capable of. The 
system was extremely complex too (COBOL, IMS TM/DB, DB2, lots of Assembler, 
and lots of interdependencies).

We chose to use Micro Focus as they stood apart from the rest as having the 
most experience in helping move mainframe development down to the PC.

The projected benefits for us were clear. Even taking into account that we 
had to plan the project, buy new PCs for everyone (since this was before the 
486 and Pentium were commonplace), buy the software, overcome technical 
hurdles, transfer the development/test environment from the mainframe, train 
everyone and then sustain the dev/test environment, we thought that the cost 
savings on development turnaround alone would justify the investment. The 
main justification (bottom line) was really to avoid mainframe upgrade costs 
(which would have been severe due to the high number of mainframe software 
products installed). This we achieved very well. What we did not realise at 
the time was just how much this would change the way we worked (for the 
better!).

Why did it work so well for us? I think management really wanted this to 
happen. As a result, we were careful to understood what was involved. Back 
in the 90's the PC environment was lacking quite a few things that we take 
for granted today so we knew we would have to build new processes and tools 
around the base Micro Focus tools. For a start, there was no LAN back then, 
and we needed to ensure everyone had an up to date version of the source 
code and load modules to develop and test against. We found a way. There 
were elements of our mainframe environment that were not directly supported 
in the Micro Focus environment at the time, so we had to find solutions for 
these. We needed to communicate with our mainframe source control system, 
and bring whole DB2/IMS test packs down to people's PCs - we built automated 
processes to do this. There were no PC backup or PC software distribution 
procedures, so we built our own (in COBOL you'll be glad to hear!). When the 
automation was in place, we were able to support the environment with very 
few resources. Admittedly a lot of this effort was down to us but we had 
management support and resources to do this; as it turns out today a lot of 
these issues we solved are now solved by the improvements in LANs, PC's and 
the (Micro Focus) software products.

Of course there were some programmers who simply didn't want a new way of 
working - they were happy doing things the old way using the 3270 interface 
and traditional mainframe debugging tools. After a short time the 
programmers that learned how to use the Micro Focus tools really started 
enjoying their work more - it was much more like the rapid response enjoyed 
by those that had moved onto C++ or VB programming, with no mainframe 
response-time, job queue or file contention frustrations. In the end, even 
the greatest critics asked to be equipped with the Micro Focus tools since 
they could sense they were falling behind with their work and their 
knowledge. This was a good result.

The Workbench toolset we used back in the 90's was superseded in 1999. The 
latest product, Mainframe Express Enterprise Edition, now comes complete 
with many of the automated tools required to keep source code and test data 
up to date - these used to be a great concern. The accuracy of the mainframe 
support has had several years of continuous improvement, and lots of missing 
elements had been missing which are now in place (LE support, JCL, Rexx, 
mainframe pointer management to name but a few). The Micro Focus development 
environment now includes analysis tools, test reporting tools, open 
connectivity (for cross-platform testing) and the ability to integrate CICS 
and IMS transactions with MQ and WebSphere, which are important for many 
mainframe shops today. If we had to do the project all over again, it would 
be so much simpler today with what Micro Focus now provides. I happen to 
know this because after the project was complete I took a job at Micro Focus 
and I now work there on the mainframe tools side.

I appreciate this won't be for everyone but any large mainframe shop looking 
to improve its development and reduce its outgoings ought to look at this 
approach. Even if you've looked before, you should look again - so much has 
changed for the better. Think of it this way: is ISPF the best home for 
keeping mainframe development alive? Is the mainframe itself best used as a 
development platform or a production platform?

Feel free to send me an email if you have any specific questions about how 
we implemented this at the bank (overcoming technical obstacles, measuring 
success, continued justification to management etc.).

Brian Crane

"Don Leahy" <leahydon@nospamplease.netscape.net> wrote in message 
news:zfC9e.11195$Jg5.784612@news20.bellglobal.com...
>
> "William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
…[59 more quoted lines elided]…
>
```

#### ↳ Re: offload mainframe development

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2005-04-20T13:23:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d45l460smb@news4.newsguy.com>`
- **References:** `<3ckodoF6n7u9kU1@individual.net>`

```

In article <3ckodoF6n7u9kU1@individual.net>, "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> writes:
> Is there anyone out there who uses Microfocus Mainframe Express or CA-Realia
> II Workbench to "offload" mainframe COBOL development?  I think Fujitsu may
> have a product also, but I don't know its name.

There are offloading customer stories on our website.  Of course we
only include the success stories (or perhaps all of our customers are
successful...), but they may be useful to you.

I don't see anything on your list that I know MFE doesn't support,
but it's not my area of expertise (I work mainly on the server
products).  CICS and VSAM emulation are definitely there, as is IMS
emulation (but I don't know if there are any limitations regarding
what we support in the way of DL/I database emulation per se).  The
JCL support has recently been enhanced, but I don't know if there are
VSE-specific features you need which might not be available yet.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
