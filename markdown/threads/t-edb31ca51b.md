[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Predict the future

_28 messages · 10 participants · 1999-12 → 2000-01_

---

### Predict the future

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 1999-12-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net>`

```
Many techniques we used to do for efficiency (ALTER), are no longer
used, as technology and costs change.  Others are less important, used
only where necessary (airline reservation systems).

I am thinking that many of our current techniques to reduce I-O will
become irrelevant as the OS finds safe ways of pulling whole files and
databases into RAM without us really knowing about it (or caring).

The concept we had with Cobol compilers that we wouldn't need to know
systems internals has had setbacks with languages such as C and
protocols such as TCP/IP.  Who thought we would need to understand
sockets in Cobol?  But will this level of detail be taken care of in the
future?

What are your predictions?
```

#### ↳ Re: Predict the future

- **From:** AnhMy Tran <anhmytran@hotmail.com>
- **Date:** 1999-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s6hsstll5k2102@corp.supernews.com>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net>`

```

Howard Brazee wrote:
> 
> Many techniques we used to do for efficiency (ALTER), are no longer
…[11 more quoted lines elided]…
> future?


COBOL is originally created for old mainframe. At that time, mainframe are
not powerful as today. Then COBOL is used in mid-size computers and then
PC as well. In PC, the way COBOL is written for mainframe cannot be applied
for PC cannot handle the huge amount of RAM as in lager machines.

Nowadays, mainframe is more powerful than before, handling more heavy load
from business. PC is more powerful than before, but LAN cannot handle the
load mainframe are doing now. LAN has SQL server and Oracle and powerful
servers that focus on Multimedia and internet rather than data processing
tasks. So, in the future, PC and mainframe will separate and each do each
expertise. COBOL will stay with mainframe, and LAN will say farewell to
COBOL. Mainframe will handle the data processing without Arts and Musics.
The data will download to Oracle and LAN, and Graphics and Musics will
add the favors to data without COBOL.
```

##### ↳ ↳ Re: Predict the future

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84avvo$c98$1@news.cerf.net>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com>`

```
"AnhMy Tran" <anhmytran@hotmail.com> wrote in message
news:s6hsstll5k2102@corp.supernews.com...
> COBOL is originally created for old mainframe. At that time, mainframe are
> not powerful as today. Then COBOL is used in mid-size computers and then
> PC as well. In PC, the way COBOL is written for mainframe cannot be
applied
> for PC cannot handle the huge amount of RAM as in lager machines.

I apologize for saying so, but this is wrong. For whatever reason you would
not apply Cobol to a PC, the amount of RAM is not one of them. First of all,
because the physical amount of RAM on mainframes actually used to be lower
than on todays modern PC's (like mine which has 256Mb installed and can be
extended to 1Gb). Second because virtual memory on PC's as on mainframes may
extend the available 'RAM' into a very, very huge number. Windows NT, for
instance, are able to address 16Gb of virtual memory. No current computer
application in the world are able to exhaust that amount.

Mainframes has other benefits, as you too point out in clustering technology
and not to forget the most important of it all; reliability.

I would like to add my prediction for the future. With the latest additions
to Microsoft Windows NT, now known as Win2000 and the Terminal services. We
will within the next 5 years see a huge jump in downscaling Cobol apps from
mainframes. Why? First of all because it is cheaper, second because it opens
up for a gradual evolution from character based applications to gui and
integration.

Disclaimer at end; I have always meant, and still has the opinion that OS/2
was/is a better OS then Windows NT is yet become. I have adopted to Windows
NT, as a result of market changes, but do not by any means adore the OS.
Hence, my prediction here is based on neutral observation and knowledge to
the OS, not because of blind love. I may be wrong, but I would be surprised
if I was.

Think about it, what would a company that practically "owns" the desktop
market do to continue their growt? They would of course expand into new
markets. Windows NT now has most of the features that the mainframes used to
be alone on. The only surprising issue here is that Microsoft yet has not
returned and provided their own Cobol.

This is the fourth reason for downscaling, modern and reliable Cobol tools
like Acucobol, Fujitus, MF, RM and more is there on the NT waiting for the
mainframe giants to step down.

Cheesle
```

###### ↳ ↳ ↳ Re: Predict the future

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386922DA.85E1DA66@home.com>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net>`

```


Cheesle wrote:
> 
> Think about it, what would a company that practically "owns" the desktop
…[4 more quoted lines elided]…
> 
Cheesle,

I don't think Microsoft will re-introduce COBOL. Remember they handed
over the ball to Micro Focus (Merant) - and as you pointed out in 
response to my query about Windowing - M/F just got too close to M/S -
mimicking the C and C++ approach to GUIs, hence Visoc and NetExpress.

More importantly, at least at this stage, Mr. Microsoft can't make bucks
with PC COBOL, (as WMK has pointed out several times with other PC
COBOLs), and I'm willing to bet he found our indeterminate 'Standards'
tiresome - he and his cohorts get an idea - they want to run with it NOW
- not wait for COBOL 2010 to coalesce.

Did you have a nice Xmas with the trolls <G>

Now back to the original message from Mr. Tran - anybody care to
elaborate on the following which I'll quote as I understood it, told me
by a family friend, a young tecchie :-

"Last Computer Show, (so I assume he meant COMDEX at Vegas) the Blue Boy
team having set up the stands for IBM had time to kill. For something to
do they contacted the guys from Sun Microsystems (?) borrowed a few
PCs/workstations and other gear and assembled them into a network - they
wrote a program which hived off modules of the program to separate
PCs to individually execute calculations - the net result they had
something more powerful than a CRAY...."

True or false ? - and if it has a modicum of truth - Goodbye mainframes.
 
Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 4)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 1999-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38692AE7.4E4BA073@NOSPAMwebaccess.net>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386922DA.85E1DA66@home.com>`

```
James J. Gavan wrote:

> "Last Computer Show, (so I assume he meant COMDEX at Vegas) the Blue Boy
> team having set up the stands for IBM had time to kill. For something to
…[7 more quoted lines elided]…
> 

Apparently they're building a tennis court sized machine to run a
program which is expected to take one year to run, instead of the 1,000
years it would run with a lesser machine.  

http://www.computerworld.com/home/print.nsf/all/991213D1AA
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38694F1F.B176E722@home.com>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386922DA.85E1DA66@home.com> <38692AE7.4E4BA073@NOSPAMwebaccess.net>`

```


Howard Brazee wrote:
> 
> James J. Gavan wrote:
…[5 more quoted lines elided]…
> http://www.computerworld.com/home/print.nsf/all/991213D1AA

Thanks for the cross-reference Howard. Sounds like it will be a SMASH
<G>. Not quite the story that was related to me, was it ?

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 5)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wtya4.247$_j1.4727@nnrp3.rcsntx.swbell.net>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386922DA.85E1DA66@home.com> <38692AE7.4E4BA073@NOSPAMwebaccess.net>`

```

Howard Brazee <brazee@NOSPAMwebaccess.net>

> Apparently they're building a tennis court sized machine to run a
> program which is expected to take one year to run, instead of the
1,000
> years it would run with a lesser machine.

Whoopie! For ONE example, look at

http://setiathome.ssl.berkeley.edu

which, when I looked a few minutes ago, had:
1,553,675 user computers, in 224 countries (including Mali,
Solomon Islands, Suriname, and the Gaza Strip) which
have accumulated
145,654.15 years of raw computing, or about
1.095067e+20 (give or take) floating point operations.

And, as I recall, a distributed computing effort cracked the 54-bit
Data Encryption Standard in less time (1 day) than it took to
write the program to do the cracking.
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 4)_

- **From:** "Gazaloo" <gaz@home.com>
- **Date:** 1999-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<J6aa4.14518$du4.360401@news1.frmt1.sfba.home.com>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386922DA.85E1DA66@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote in message
news:386922DA.85E1DA66@home.com...
> "Last Computer Show, (so I assume he meant COMDEX at Vegas) the Blue Boy
> team having set up the stands for IBM had time to kill. For something to
…[6 more quoted lines elided]…
> True or false ? - and if it has a modicum of truth - Goodbye mainframes.

IMHO: i think it's reasonably clear that as UNIX systems scale up
(multi-processors and clustering) and mainframes continue to get more
competitive (cost/performance ratio), that these two areas will converge
(two planets colliding). it should be an interesting battle for market
share. IBM would clearly love MVS to prevail as the leader but perhaps the
fact that they are heavily invested in other areas (such as AIX, NT & Linux)
shows that they are hedging their bets.
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 5)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84emc4$21s$1@news.cerf.net>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386922DA.85E1DA66@home.com> <J6aa4.14518$du4.360401@news1.frmt1.sfba.home.com>`

```
"Gazaloo" <gaz@home.com> wrote in message news:J6aa4.14518
> IMHO: i think it's reasonably clear that as UNIX systems scale up
> (multi-processors and clustering) and mainframes continue to get more
…[3 more quoted lines elided]…
> fact that they are heavily invested in other areas (such as AIX, NT &
Linux)
> shows that they are hedging their bets.

Very interesting prediction. I second this.

Cheesle
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 5)_

- **From:** Ralph Jones <leclay@ibm.net>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386AF53F.864CA159@ibm.net>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386922DA.85E1DA66@home.com> <J6aa4.14518$du4.360401@news1.frmt1.sfba.home.com>`

```
Just a side note:

Did a small project for Fermi Lab this summer.  The CDF, Collider Detector
Facility, is the experimental area that discovered the top quark.  The CDF is
undergoing a major overhaul.  When it comes back on line, the proton,
anti-proton beams will be collided every 356 nanoseconds.  Each collision will
generate 256k of data.  The data is filtered by the on-line system and then sent
to the PC farm.  The farm is 1,000 dual processor Pentium machines running
LINUX.  The pc's correlate the data and send it off the the tape storage
machines.  There will be 1 to 2 petabytes stored on tape, 1,000 terabytes in a
petabyte.  The off-line (analytical) systems will access the data through a
spooling sub-system that will have 1 to 2 terabytes of disk storage, 2% of the
data available.  The off-line system will have a SGI/Cray machine in the mix of
available systems.  Oh yes SGI is using LINUX as the OS of choice.  They are
moving away from their in-house UNIX.

The CDF is 3 stories high & weighs in at a mere 3,000 tons.  They are looking
for any number of phenomena.  The most talked about is the Higgs Boson.  But
think it's an off chance that it will be found.  The Tevatron does not have
enough energy for Higgs, at 1 trillion electron volts.  Higgs, if found could
lead to the theory of everything.  Lot's of interesting stuff on the site,
fnal.gov.  The Higgs page is
http://www.fnal.gov/directorate/public_affairs/higgs/higgs_fnews.html

If you travel anywhere close to Batavia IL, a far western Chicago 'burb, stop
in.  The visitor center is around 16 hours a day.  They have tours during the
day.  The facility is completely open.

Cheers,
Ralph

Gazaloo wrote:

> "James J. Gavan" <jjgavan@home.com> wrote in message
> news:386922DA.85E1DA66@home.com...
…[19 more quoted lines elided]…
> gaz@home.com
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 4)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84em8n$21g$1@news.cerf.net>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386922DA.85E1DA66@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote in message
>
> More importantly, at least at this stage, Mr. Microsoft can't make bucks
…[3 more quoted lines elided]…
> - not wait for COBOL 2010 to coalesce.

That is a good point, Cobol is too established for him to come in and grab
the market, force it into his standard. That is probably why!

> Did you have a nice Xmas with the trolls <G>

Yes indeed. Especially with to small ones :-) Funny thing, the oldest one
denies the existence of Santa, and the youngest lives for Santa. They almost
started fighting about it. But... War over when Santa came.

> "Last Computer Show, (so I assume he meant COMDEX at Vegas) the Blue Boy
> team having set up the stands for IBM had time to kill. For something to
…[6 more quoted lines elided]…
> True or false ? - and if it has a modicum of truth - Goodbye mainframes.

This is certainly true, as a matter of fact the University of my hometown
(NTNU) did back in the late eighties create a cluster using Intel 8086
processor and a specially designed parallel OS. The output of the pure
calculations were of course remarkable numbers. Their success never became
commercialized, but the techonoly of clustered computers are a live and
kicking. I saw in a magazine last summer about a north american oil company
that had replaced their leased (and expensive) AS400 with a cluster of 486
computers running Linux, and yes, the cluster had no problem keeping pace
with the AS400.

However, there is one thing to remember in this subject. The applications,
if not highly specialized will not gain as much improvement as these "tests"
do. One thing is that the OS can behave like a scheduler and separate
processes over a network, but it will never be as efficient as an
application designed for paralell processing, be it on the same computer or
in a network. I don't know for mainframes, but Microsofts solution to
distributed processing aka "Wolfpack" suffers of the same issue. Although NT
may take care of the dispatch, the overhead here causes so much loss that
the benefit is small. If the application itself may dispatch processes, and
is prepared for asynchronous processing, the improvement will be
significant.

A sidestep at end, the same tests at the university of my hometown, claimed
to experience that the computer "learned". The theory was that the special
cube construction for parallel processing had this side effect. Obviously
they were unable to prove anything, otherwise we would have known by now.

Cheesle
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386B6968.82A9D2C2@NOSPAMwebaccess.net>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386922DA.85E1DA66@home.com> <84em8n$21g$1@news.cerf.net>`

```
Cheesle wrote:
> 

> > Did you have a nice Xmas with the trolls <G>
> 
> Yes indeed. Especially with to small ones :-) Funny thing, the oldest one
> denies the existence of Santa, and the youngest lives for Santa. They almost
> started fighting about it. But... War over when Santa came.

My son always told us that he very much believed in the tooth fairy.  He
wasn't worried about Santa, as non-belief doesn't seem to effect the
amount of presents someone receives, but to not believe in the tooth
fairy seems to be foolish!!  Of course, things may change now that he's
a father.
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 6)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84g4q3$s16$1@news.cerf.net>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386922DA.85E1DA66@home.com> <84em8n$21g$1@news.cerf.net> <386B6968.82A9D2C2@NOSPAMwebaccess.net>`

```
"Howard Brazee" <brazee@NOSPAMwebaccess.net> wrote in message
> My son always told us that he very much believed in the tooth fairy.  He
> wasn't worried about Santa, as non-belief doesn't seem to effect the
> amount of presents someone receives, but to not believe in the tooth
> fairy seems to be foolish!!  Of course, things may change now that he's
> a father.

Probably not, just that he has become a tooth fairy himself :-) Both my wife
and I have inherited this from our parent generation to our kids.

It is a cute tradition.

Cheesle
```

###### ↳ ↳ ↳ Re: Predict the future

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386AB4A1.1B11F612@zip.com.au>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net>`

```
Cheesle wrote:
> 
> I would like to add my prediction for the future. With the latest additions
…[4 more quoted lines elided]…
> integration.

I personally do not believe that NT will be reliable enough for this
to occur. It is a large operating system and complex.  It will make
inroads but it will not be the only one.

Predictions:

Linux will become a standard second deliverable on desktops.  All
programs of worth will support Linux as a second option.

Mainframe will continue to support services.  It is the security
benchmark, and web services can be supported easily on it.

Internet will become available at high speed in all around the world
homes.  (as much as cable is in USA).

Internet commerce will destroy most other sorts of commerce with
active agents seeking the best deal for any item you want.  Businesses
will have to provide agent sockets or die of lack of business.

Single address space operating systems will become the talk of the
town.  A SASOS is a networked operating system without files you
allocate a chunk of storage and pass pointers around instead of
filenames.  The 'memory' the pointer points to will automatically be
moved to the requesting machine. Processes will run on any machine
automatically giving good load balancing across networks.  MUNGI is an
example of this sort of OS.  Will be used in example networks within
five years showing the power of this sort of stuff.

Yahoo share prices will crumple as people realize they are over
valued. Other internet companies follow suite.

OO cobol will be used in less than 30% of all Cobol applications in
five years.  It will not take over the world.  Sad but true.

All system designers will use a derivative of the Universal modelling
language (UML) to design their applications (OO or not it still
works).

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 4)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AgTa4.124$tc1.4409@nnrp2.rcsntx.swbell.net>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386AB4A1.1B11F612@zip.com.au>`

```

Ken Foskey <waratah@zip.com.au
>
> Predictions:
>
> Linux will become a standard second deliverable on desktops.  All
> programs of worth will support Linux as a second option.

Giggle, giggle.
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 4)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84g5h0$scc$1@news.cerf.net>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386AB4A1.1B11F612@zip.com.au>`

```
"Ken Foskey" <waratah@zip.com.au> wrote in message
news:386AB4A1.1B11F612@zip.com.au...
> I personally do not believe that NT will be reliable enough for this
> to occur. It is a large operating system and complex.  It will make
> inroads but it will not be the only one.

Reliability is the big issue, can't argue with you there. However, great
improvements has taken place over the last years. Todays Win NT 4.0 SP6 is
way more robust than NT 3.5 was in its time. As for Win2000 time will show.
Beta looks good.

> Linux will become a standard second deliverable on desktops.  All
> programs of worth will support Linux as a second option.

Sounds like a good point, however not entirely agreed. I believe the Linux
"support" will come as a Windows Terminal Server client. Cheaper, and means
that your application is there today.

> Internet will become available at high speed in all around the world
> homes.  (as much as cable is in USA).

Not within 5 years on a wide basis. Remember these things demands
infrastructure, which is there in the western hemisphaere, but the rest of
the world, there is still way to go.

> Internet commerce will destroy most other sorts of commerce with
> active agents seeking the best deal for any item you want.  Businesses
> will have to provide agent sockets or die of lack of business.

Interesting, but you don't think that this will delete competition? If
everyone were using agents to check the price next door, would'nt all end up
on the same price?

> Single address space operating systems will become the talk of the

Hmmm, maybe, maybe not. I am not convinced.

> Yahoo share prices will crumple as people realize they are over
> valued. Other internet companies follow suite.

Yepp, I am just waiting for the big bang. It is totally insane pricing of
these companies, and I feel sorry for those that eventually will loose in
this big raffle.

> All system designers will use a derivative of the Universal modelling
> language (UML) to design their applications (OO or not it still
> works).

I don't know. I see the beneficial factors, but I do also see the
bureaucracy, there is a middle line out there for when it is beneficial to
use UML and not. I suspect that line is higher than most people think.

Cheesle
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386BB31C.A2852B3C@home.com>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386AB4A1.1B11F612@zip.com.au> <84g5h0$scc$1@news.cerf.net>`

```


Cheesle wrote:
> 
> "Ken Foskey" <waratah@zip.com.au> wrote in message
…[8 more quoted lines elided]…
> on the same price?

Well you've commented on Ken's retail prediction. But all of you who are
partnered to the opposite sex; do you really think that you are going to
get your good lady to give up browsing shops, (particularly those damned
fashion stores), and opting for staring at a computer screen instead -
get real! I'm sure Ken, your good lady would provide some choice words
if you suggested this <G>

I'll accept that if I'm looking for, as an example, computer equipment -
yes I'll look at the Web for comparisons - but it's still nice to have
that 'touchy' feeling where you poke around the device in a store. No
doubt your answer to that is that they will provide me with a virtual
device to inspect.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 6)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386BB6C8.72B886AA@NOSPAMwebaccess.net>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386AB4A1.1B11F612@zip.com.au> <84g5h0$scc$1@news.cerf.net> <386BB31C.A2852B3C@home.com>`

```
James J. Gavan wrote:
> 
> > Interesting, but you don't think that this will delete competition? If
…[8 more quoted lines elided]…
> if you suggested this <G>

But shoppers also drive all across town to save a buck.  Retail will
change some - what happens when I use up a car dealer's time and money
to test drive a car, then order that car on the internet?   Travel
agents will have to offer me more than just the cheapest price.  They
will make their money in setting up packages for group travel.  

Right now, I would love to be able to log onto a web site, tell them the
size of my buttocks and my legs (I am a fairly small guy, but not as
small as airlines assume), give minimum legroom requirements and then
tell it to shop for the best price - or say I will give up an inch for
$40, etc.

The big winners in the internet shopping business are those who sell
rare items, those who sell very standard items, and those who deliver
items.

There really is a lot of room for improvement in the logistics of
delivery.  It is really irritating to order something to my home
address, go home after work, and find a note saying that I can't pick up
my object today, but after 3 delivery attempts, I can drive to the other
side of the city and pick up my package.  We are not a society full of
stay at home spouses.  Maybe those packaging stores need to re-market
themselves as full service send and receive shops.

But this all costs time and money.
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386BBA14.EF3A675C@home.com>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386AB4A1.1B11F612@zip.com.au> <84g5h0$scc$1@news.cerf.net> <386BB31C.A2852B3C@home.com> <386BB6C8.72B886AA@NOSPAMwebaccess.net>`

```


Howard Brazee wrote:
> 
> James J. Gavan wrote:
…[5 more quoted lines elided]…
> $40, etc.

Interesting what this NG reveals if you wait long enough. From above, am
I to assume, that like Judson, you are 'pear-shaped' <G>

Just so you know - I'm six feet, broad-build but slimming down because
of age <G>.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 8)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386BC563.54BEFAA8@NOSPAMwebaccess.net>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386AB4A1.1B11F612@zip.com.au> <84g5h0$scc$1@news.cerf.net> <386BB31C.A2852B3C@home.com> <386BB6C8.72B886AA@NOSPAMwebaccess.net> <386BBA14.EF3A675C@home.com>`

```
James J. Gavan wrote:
> 
> Howard Brazee wrote:
…[15 more quoted lines elided]…
> Jimmy, Calgary AB

Actually, I'm not.  Instead I am someone who went through pilot training
before the Air Force told me I would never fly - I kept throwing up.  I
still do everything I can to avoid air sickness, and like a little
squirming room.  I also like room to put my arms.  At any rate, if I
care about having butt and leg room, most people (most American men are
bigger than me, most women have bigger where I like them bigger) will
also care.

The airlines recently did a study of complaints.  There was a very
strong correlation between the amount of complaints and whether or not
there was an empty seat next to the customer.  The complaints were about
anything and everything except whether the adjoining seat was full - but
that was what made the difference.

At any rate, someday we will be able to put values on various criteria -
how much will you be willing to pay for decent food, how much will you
be willing to pay for window seats, how much will you be willing to pay
for 24" leg room, 27"?, how much will you be willing to pay to sit where
you can disembark easily, how much would you be willing to pay to carry
a larger suitcase on board, would you like the midnight flight if it was
mostly empty, etc.).  You could save a cookie or preference file with
the ability to override for tomorrow's flight - maybe you want to avoid
a stop over in Seattle during the World Trade Talks.  Your (computer)
agent makes some guesses and you have a dialog WITH ALL THE PERTINENT
FACTS, to pick your choice.
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84ibup$gc0$1@news.igs.net>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386AB4A1.1B11F612@zip.com.au> <84g5h0$scc$1@news.cerf.net> <386BB31C.A2852B3C@home.com>`

```
There is also the personal aspect ... I deal with people I trust.  Tough to
get to know a website to the point you can ask for help.  Certainly not
worth a one percent decrease in price.

The rule of thumb for the last forty years has been that you need a decrease
in price to 1/10 before a technology wipes out the previous technology.
That may happen with telephones ... I would not be surprised to see web
phone wipe out point-to-point telephone.  I have seen no net technology
other than that that I would bet money on.

James J. Gavan wrote in message <386BB31C.A2852B3C@home.com>...
>
>
…[10 more quoted lines elided]…
>> everyone were using agents to check the price next door, would'nt all end
up
>> on the same price?
>
…[13 more quoted lines elided]…
>Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 7)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386CBACB.C5E60FD4@NOSPAMwebaccess.net>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386AB4A1.1B11F612@zip.com.au> <84g5h0$scc$1@news.cerf.net> <386BB31C.A2852B3C@home.com> <84ibup$gc0$1@news.igs.net>`

```
donald tees wrote:
> 
> There is also the personal aspect ... I deal with people I trust.  Tough to
…[7 more quoted lines elided]…
> other than that that I would bet money on.

Or an improvement in capacity of x10.  Mobile capacity may do that. 
There have been arguments that PL/I failed to take over COBOL because it
was only twice as capable.

Of course, you could combine the cost and capacity together to achieve
the same benefit.
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 8)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84jgdm$67u$1@news.igs.net>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386AB4A1.1B11F612@zip.com.au> <84g5h0$scc$1@news.cerf.net> <386BB31C.A2852B3C@home.com> <84ibup$gc0$1@news.igs.net> <386CBACB.C5E60FD4@NOSPAMwebaccess.net>`

```
Howard Brazee wrote in message <386CBACB.C5E60FD4@NOSPAMwebaccess.net>...

>Or an improvement in capacity of x10.  Mobile capacity may do that.
>There have been arguments that PL/I failed to take over COBOL because it
…[3 more quoted lines elided]…
>the same benefit.

Yes, that is true.  But what do you mean by "Mobile capacity"?

I do see a place for web retailing, particularly in small towns that
traditionally have lacked "a decent bookstore", for example. What I do not
see is them replacing the Walmarts of this world.  Not only do most people
want to 'kick the tires first", but it is a delusion to think that there are
any savings. What is cheaper, and more efficient do  of:

1.  Take 500 orders over the net, and ship 500 televisions to 500 locations,
transferring all information over wire.

2. Deliver 500 televisions to a pile on a floor and hold a boxing day sale.
Everybody carries their television away from the pile, and all money is
transferred over wire.

Net commerce is only suitable for very specific things.  Books are about the
largest thing that ship cheaply enough to make it practical.

Certainly there are opportunities.  For example, I do not see the recording
industry lasting much longer.  Once we hit 100 gig disk drives, all music
will be sold producer-to-disk, direct, cash going the other way.  A lock on
*that* market would make Microsoft look small. Radio, recording companies,
television five years later, and movies about the same time.  They will all
become part of the "net" as the
cable companies convert to isp's.  You will download everything, and play it
jukebox style.  PC stereo equipment will be a huge new market.

But it will be sold at the future shop.  And therein lies the rub.  Many
people may choose to "order" from the local future shop over the net. The
existing companies have no net presence.  The net companies have no delivery
mechanism.  I see some tremendous changes in the market place as each
scrambles to buy out the other.  By the end of it all, it might be a moot
point over whether net commerce takes over retailing, or retailing takes
over net commerce.  I tend to think the latter will be true.  Take a look at
the ownership of "chapters" for example.
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 9)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386E3B77.6D9E64B2@NOSPAMwebaccess.net>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386AB4A1.1B11F612@zip.com.au> <84g5h0$scc$1@news.cerf.net> <386BB31C.A2852B3C@home.com> <84ibup$gc0$1@news.igs.net> <386CBACB.C5E60FD4@NOSPAMwebaccess.net> <84jgdm$67u$1@news.igs.net>`

```
donald tees wrote:
> 
> Howard Brazee wrote in message <386CBACB.C5E60FD4@NOSPAMwebaccess.net>...
…[8 more quoted lines elided]…
> Yes, that is true.  But what do you mean by "Mobile capacity"?

I was referring to switching from hard wired communication to mobile.
 
> I do see a place for web retailing, particularly in small towns that
> traditionally have lacked "a decent bookstore", for example. What I do not
…[9 more quoted lines elided]…
> transferred over wire.

This is probably cheaper, but it some people wouldn't be able to do it. 
On the other hand, I find it easier to pick up a product when I am free
than to be at home whenever the UPS man arrives.
 
> Net commerce is only suitable for very specific things.  Books are about the
> largest thing that ship cheaply enough to make it practical.

In large quantities.   Ordering a rare part can be very good over the
net.  Nobody wants to warehouse them near your house, but you know
exactly what you want, find out whether it is in stock in Timbuktu, and
then have them send it to you.
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 10)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ckwb4.209$3s2.4015@nnrp1.rcsntx.swbell.net>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386AB4A1.1B11F612@zip.com.au> <84g5h0$scc$1@news.cerf.net> <386BB31C.A2852B3C@home.com> <84ibup$gc0$1@news.igs.net> <386CBACB.C5E60FD4@NOSPAMwebaccess.net> <84jgdm$67u$1@news.igs.net> <386E3B77.6D9E64B2@NOSPAMwebaccess.net>`

```

Howard Brazee <brazee@NOSPAMwebaccess.net>
 >
> In large quantities.   Ordering a rare part can be very good over
the
> net.  Nobody wants to warehouse them near your house, but you know
> exactly what you want, find out whether it is in stock in Timbuktu,
and
> then have them send it to you.

Reminds me of the redneck poetry contest. "Use the word
'Timbuktu' in a poem."

The winner wrote:
"Me and Tim a huntin' went,
"Met three whores in a pop-up tent,
"Since we was three and they was two,
"I bucked one, and Tim bucked two."
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84gi6m$uku$1@aklobs.kc.net.nz>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386AB4A1.1B11F612@zip.com.au> <84g5h0$scc$1@news.cerf.net>`

```
Cheesle <cheesle@online.nospamplease.no> wrote:

: Reliability is the big issue, can't argue with you there. However, great
: improvements has taken place over the last years. Todays Win NT 4.0 SP6 is
: way more robust than NT 3.5 was in its time. As for Win2000 time will show.
: Beta looks good.

NT is still way down the list compared to what Mainframes, Netware
and Unix have been doing for years.  Typically mainframes only
get 'rebooted' when scheduled, Netware and Unix stay up for
months or years.  Netware has been upgradable in flight for
many years and so is not rebooted even when a new version is
installed.  Even Linux servers stay up for months at a time.

NT, it seems, is best scheduled to have reboots on a regular
basis for various reasons before they are needed.

SP6 is not recommended, revert to SP5.

Win2000 is almost all _new_ code.  It is a 1.0 release.  It
is also several times larger and more complex due to MS's
technique of making things 'simpler' by adding several
layers of complexity to hide underlying complexities (eg
Wizards, PnP, and other automatic mechanisms that get in
the way and stop me doing it the way _I_ want).

: Sounds like a good point, however not entirely agreed. I believe the Linux
: "support" will come as a Windows Terminal Server client. Cheaper, and means
: that your application is there today.

Windows TSE is a very poor multi-user system.  The underlying
Windows OS was never designed to have multiple concurrent users
and, more importantly, the Windows applications never catered
for multiple concurrent users in a rational way.  TSE was
merely a way of driving Citrix out of business when MS saw
revenue going to someone else.

EinFrame at least made an attempt to overcome the underlying
inherent problems of application sharing that TSE hasn't dealt
with.

Also, using Linux as a TSE client is _not_ cheaper due to the
way MS charges for NT/2000 and client support licences.  Even
though Linux may be free it will cost _more_ to use TSE than to
just put Win95 all around.  MS _needs_ the revenue.  If cheaper
is what you want don't use MS at all.

: Interesting, but you don't think that this will delete competition? If
: everyone were using agents to check the price next door, would'nt all end up
: on the same price?

Only if you think that price is everything.


: Yepp, I am just waiting for the big bang. It is totally insane pricing of
: these companies, and I feel sorry for those that eventually will loose in
: this big raffle.

No more so than the insane price of MS which is allegedly based
on false reporting of revenue and costs whereby the employees
are effectively being paid by stock options and the cost of
the payroll is reduced by the stock takeup.  Effectively,
so it is alleged, MS is printing more stock and using this as
if it were revenue.  If this were accounted for properly then
MS accounts would show an increasing loss over the last few
years.  They are being accused of fraud.
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 6)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j_db4.95$L82.5163@nnrp1.rcsntx.swbell.net>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386AB4A1.1B11F612@zip.com.au> <84g5h0$scc$1@news.cerf.net> <84gi6m$uku$1@aklobs.kc.net.nz>`

```

Richard Plinston <riplin@kcbbs.gen.nz
>
> No more so than the insane price of MS which is allegedly based
…[6 more quoted lines elided]…
> years.  They are being accused of fraud.

1. Microsoft does NOT price its products that way (cost+);
they use the "What the market will bear" model. Internal
documents show they could make a profit by selling Win98 at
less than $50 (cost+). They chose $108 as the point of
maximizing revenue.

2. If printing 'stock certificates' is the equivalent of printing
'money,'
why has the value of MS stock continually increased?
```

###### ↳ ↳ ↳ Re: Predict the future

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84id6g$h75$1@news.igs.net>`
- **References:** `<3860E184.3BF2D8B4@NOSPAMwebaccess.net> <s6hsstll5k2102@corp.supernews.com> <84avvo$c98$1@news.cerf.net> <386AB4A1.1B11F612@zip.com.au> <84g5h0$scc$1@news.cerf.net> <84gi6m$uku$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote in message

>No more so than the insane price of MS which is allegedly based
>on false reporting of revenue and costs whereby the employees
…[5 more quoted lines elided]…
>years.  They are being accused of fraud.


ROTFL.

Does anybody else see a pattern here?  Any banking experts in international
currencies in the crowd?

I predict MS will be gone in five years.  Bankrupt.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
