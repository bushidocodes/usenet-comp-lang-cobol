[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PC COBOL - Cost of Compilers - Market for them, etc...

_21 messages · 15 participants · 1997-09_

**Topics:** [`Jobs, careers, recruiting, salary`](../topics.md#jobs) · [`Compilers and vendors`](../topics.md#compilers)

---

### PC COBOL - Cost of Compilers - Market for them, etc...

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-09-10T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bcbeb7$2ec53520$50752581@thane-hubbell>`

```


Bear with me, I'm about to go on a tirade. There's a large untapped
resource out here, and it is being ill served by the different COBOL
vendors. This post is a little long, but I think I will make some valid
points. I want you to answer the question at the end of the posting.

The basic premise is that there is a market for a PC based COBOL compiler -
not for resizing Maine Frame applications, nor for doing Mainframe
development offline, but for targeted PC applications. The compiler need
only support Windows, and does not NEED a ton of other things included.
Now, before the compiler vendors start screaming that they have this, let
me explain.

In 1991 I had an "idea" for a PC based computer program that I wanted to
sell. I'm a pilot, and something called DUAT was being introduced. It
allows pilots to call with their PC's and download aviation weather
information. The weather was in "FAAese" though- the old teletype method.
As a flight instructor (Part time - I've been a COBOL programmer full time
since 1983) , I was teaching my students to read this stuff. It's not very
clear sometimes and different abbreviations mean different things based on
context. I knew that I could write an application that would take this
weather and "translate" it into English - expanding all abbreviations and
making it clear and easy to understand. I had experience with several PC
based products for development. At work I had used Realia COBOL, BASIC,
Micro Focus COBOL and RM COBOL. I could develop my system in BASIC - but I
was much faster in COBOL and I could do a better job.

I purchased a PC, and decided to buy Realia COBOL - knowing how much faster
and reliable it was than the other COBOL compilers. I spend an arm and a
leg on the compiler, $900.00, plus $400.00 for the SCREENIO product so I
could have a good user interface. Yearly maintenance was $160.00 for the
compiler and $65.00 for SCREENIO. This was the "basic" version of Realia
offered from Realia itself - before the Panasophic or CA acquisition. This
was a LOT of money for me for a part time venture.

I developed my system. It was GREAT. Reliable and worked well. I started
to market it in the Aviation magazines, and have about 50 sales at $35.00 a
pop. The ads were costing just about what I was making on the software. I
had a problem in that the software was not fully integrated - it did not
make the phone call to the DUAT vendor, it relied on other communications
software and the user capturing the data file. I decided I needed to do
that for myself. I hunted on BBS's and found some communications routines
designed to be called from C. Realia has a robust calling convention
system for calling other languages, and while I barely knew C (I waa
running my own BBS with soucce code in C - I learned C so I could modify
the code), I was able , working with the author of the routines, to get
them to work from Realia. Everything was going fine - I still had not
recouped my $$ for the PC or the development tools, but I had a cool system
that was selling. Then the "unthinkable" happened - the FAA started
providing plain english briefings via the DUAT and my sales went in the
toilet. The lead time on the magazines I was advertising in was 3 months,
so I had 3 months of wasted advertising.

Well, since then I have continued to develop small systems for people on a
system by system basis. All in DOS using the Realia COBOL. I have a
friend, that runs a bowling center, and he had trouble with his little
inhouse database system, printing labels for marketing purposes. I told
him I could do something for him and wrote him a small system for tracking
coupon redemptions etc. He liked it, it worked, was suprised about "COBOL"
with the stigma it has for being a Mainframe only language, and has since
hired me to develop a full scale bowling center management system. It's
DOS based, runs on a LAN, and is slick. STABLE too. I never hear from him
with problems, only the occasional request for a new sub system or
enhancement.

I have devloped other systems over the years. There is a guy where I work
full time - on mainframes, and doing new devlopment for the PC with MF
COBOL both for DOS and Windows with Dialog System - that runs a sub
business that we have printing statements for dental offices. He was
having them mail in diskettes, then he went to trying to transmit them.
The variety of communications programs and the probelmes getting people to
connect and send were taking a lot of his time. On my own, to help him
out, I wrote a communications program just for transmitting that file here.
I invented my own protocol - that was fun - and made it so the braindead
can operate it. Just run it- it finds the modem, file, dials and sends.
It works great and never fails - again in COBOL. For another friend I
developed an Archery shoot tracking system - to handle registration and
scoring and reporting at archery shoots. I have numerous other small
systems, all targeted for the PC.

Over time I have always wanted to take them to Windows. The friend with
the bowling software would like to package it and sell it, but it needs to
be Windows to be marketable today. I tried the native windows support in
Realia - but it was very difficult to understand, especially since it was
not well documented at all.

After I got on the internet, I found something FANTASTIC for allowing me to
do this. That is COBOL SP2. They worked with me, and I purchased the
product so I could take my existing and any new systems to Windows. It
works great, and I can't recommend a company any more highly than Flexus
and their products, both for GUI development and for Windows based
printing.

I'm about to get to the point here. Trust me!

I have some other systems I want to write. I am writing some now. You
have to understand though, that I do this part time, in my spare time and I
don't make a lot of money at it. I bet there are some other people like me
out here! Private individuals who are excellent COBOL programmers, who
would like to develop, solid, reliable PC based applications.

Recently I decided that I probably need to go to a 32 bit compiler. My end
users are used to the Windows 95 features, long file names, and dislike the
degradation that occurs with Win 95 when you run a 16 bit application.

I started pricing compilers. My first stop - what I know and what works
well. CA-Realia. Their 32 bit version is only available in their full
workbench product. The price is $4000.00 with $600.00 a year maint fee.
It includes the CICS option, and a bunch or rehosting tools that, frankly I
don't need.

Microfocus is an option, but I know that most of my stuff will take a lot
of work to get to work under MF, and MF is dreadfully slow and a big PIG
with what must be included with the programs that are deployed. There are
also some runtime issues.

ACCUCOBOL has runtime fees.

Fujitsu - I'll save my comments for later - these people bear watching,
they are up and comers in this market and MAY be the answer.

All the PC based cobol compilers to get to 32 bit are around the same
price. MUCH MORE Than an individual can spend!!

There is a need for a PC based COBOL development system.

Here's the question I would like everyone to answer:

If it were available at reasonable cost, how much would you spend on a PC
based COBOL, Windows development system.

$100.00?
$200.00?
$1000.00? More?

Yearly fees? Runtime fees?

I just got a card in the mail from BORLAND. I can get thier latest and
greatest Visual developmetn suite for under $300.00. No yearly fee, no
runtime. I don't want to take the time to learn this. I don't HAVE the
time.

I don't have the MONEY for the COBOL compilers.

The compiler vendors tell me that they can't afford to sell their compilers
that cheap. There is no market they say, as people are not doing PC
development with COBOL. HOW MANY WOULD if they could afford it?!?

Speak up and tell these people you want an affordable compiler. Tell them
how many sales they will get! They all monitor this news group.

Now about Fujitsu -

This is the BEST deal I have seen. Even if you don't take advantage of
their "Free" offer, you can get JUST the compiler (Which is all most will
need) for $700.00 and $150.00 a year subscription fee. Even that Is HIGH I
think, but they have been very responsive to me. I have nothing bad to say
about them or their product. I don't have it all working for me yet but
they are very repsonsive to me, even though they know I am small time.
They are worth a look. HOWEVER, even their lowest priced package is too
expensive in my opinion.
```

#### ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

- **From:** "bi..." <ua-author-8405640@usenetarchives.gap>
- **Date:** 1997-09-09T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bcbeb7$2ec53520$50752581@thane-hubbell>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell>`

```

In article <01bcbeb7$2ec53520$50752581@thane-hubbell>,
"Thane Hubbell" wrote:
› Bear with me, I'm about to go on a tirade.  There's a large untapped
› resource out here, and it is being ill served by the different COBOL
…[9 more quoted lines elided]…
› 
 
› 
› Here's the question I would like everyone to answer:
…[9 more quoted lines elided]…
› 
 
› 

Thane,

I agree completely with what you have said. I work for a small software
business; we have a complete accounting system for small to medium size
businesses (particularily nursing homes). It's all written in COBOL,
developed on a mainframe. 3 years ago, I ported the system to the PC using MF
COBOL.

The fees are too high; particularily for the kind of technical support (bad)
we get.
```

##### ↳ ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

- **From:** "r..." <ua-author-43843@usenetarchives.gap>
- **Date:** 1997-09-10T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3636c8adbe-p2@usenetarchives.gap>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell> <gap-3636c8adbe-p2@usenetarchives.gap>`

```

In article <5v9cfi$k.··.@nuh··a.net>
› bi··.@AL··A.NET "William Murray" writes:
› In article <01bcbeb7$2ec53520$50752581@thane-hubbell>,
…[8 more quoted lines elided]…
› technical support (bad) we get.

I agree completely. It's like the British disease: "If we make
it too cheap there'll be too many customers and we can't cope".

The industry needs a Borland TurboCOBOL, student edition $50,
professional edition $250 with NO runtime fees. As it became
popular, good tech support would be available via the Internet.

Maybe if we persuade Bill Gates that the next version of Basic
should have object-oriented DATA & PROCEDURE DIVISIONs with a
visual PICTURE for each item of data and English-like verbs...
well, it worked for C didn't it :-?

Richard Ross-Langley        +44 1727 852 801
Mine of Information Ltd, PO BOX 1000, St Albans AL3 5NY, GB
* Independent Computer Consultancy    Established in 1977 *
```

##### ↳ ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

- **From:** "sno..." <ua-author-11012794@usenetarchives.gap>
- **Date:** 1997-09-11T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3636c8adbe-p2@usenetarchives.gap>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell> <gap-3636c8adbe-p2@usenetarchives.gap>`

```

bi··.@AL··A.NET (William Murray) wrote:

› In article <01bcbeb7$2ec53520$50752581@thane-hubbell>,
›   "Thane Hubbell"  wrote:
…[37 more quoted lines elided]…
› we get.

Our company has a proprietary component framework for compiler construction. At
the moment, we have Modula-2, Oberon-2, and some proprietary languages
front-ends, an ANSI C/C++ back-end, and Intel x86, Motorola m68k, and PowerPC
native code back-ends. It is possible to combine any front-end with any
back-end on any host platform (NT, 95, OS/2, Linux, HP-UX, Solaris, Ultrix,
etc.).

We also have some other development tools on Intel x86 platforms - IDEs,
debuggers, profilers, etc.

At the moment we are determining which component to develop next. We have the
following options:

- A Java Virtual Machine back-end
- A Java front-end
- A Cobol front-end

We sell Modula-2/Oberon-2 native-code compilers for $300. The next version will
cost about $450, as it incorporates a lot of new features. We could sell a
Cobol compiler for about the same price - $300-400. But before we start the
development, we want two things:

- to be sure that it will be profitable enough
- to find a partner in US or Europe with good Cobol experience - Cobol is not
used in our country, so we have nobody to ask questions here.

So, is anybody interested?

Dmitry Leskov

P.S. You may read about our company at http://www.xds.ru/

-----------------------------------
Dmitry V. Leskov
XDS Products Division Manager
sno··.@x··.ru

XDS Team Home Page is http://www.xds.ru/
```

###### ↳ ↳ ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

- **From:** "robert s. robbins" <ua-author-17071337@usenetarchives.gap>
- **Date:** 1997-09-11T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3636c8adbe-p4@usenetarchives.gap>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell> <gap-3636c8adbe-p2@usenetarchives.gap> <gap-3636c8adbe-p4@usenetarchives.gap>`

```

Hello World,
I only need a PC compiler for COBOL so that I can learn the
language at home. I would only be willing to pay $100 for any
professional software product. You can now study many computer languages
with inexpensive compilers and IDEs included on CD-ROM with a book. I've
bought two of the new Programming Starter Kits to learn Visual C++ and
Visual Basic for only $40.00. You get a prior version of the IDE in
these kits and one book. I think that is a real bargain! And you can get
the JAVA Development Kit even cheaper by buying a remaindered SunSoft
Press book. The most I paid for anything was $99
for Paradox 5.0 WIN3.1 which features ObjectPAL. I bought some books on
programming in ObjectPAL at the local grocery store for only $5 each!
Getting back to COBOL, you can download various shareware compilers as
well. And Dr. Jobbs sells a CD-ROM packed with "alternative language
compilers".
Robert Robbins
Budget Programmer Trainee
```

###### ↳ ↳ ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

_(reply depth: 4)_

- **From:** "steve wolfe" <ua-author-733217@usenetarchives.gap>
- **Date:** 1997-09-14T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3636c8adbe-p5@usenetarchives.gap>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell> <gap-3636c8adbe-p2@usenetarchives.gap> <gap-3636c8adbe-p4@usenetarchives.gap> <gap-3636c8adbe-p5@usenetarchives.gap>`

```

Robert S. Robbins wrote:
› 
› Hello World,
…[15 more quoted lines elided]…
›                                               Budget Programmer Trainee

I would be willing to pay the 300-400 for a QUALITY windows based
development environmnet/compiler for COBOL. I think that there is a huge
market waiting to be tapped. I don;t think that is too much to spend for
most professionals/novices. As Thane said, many already spend that range
for various microsoft, borland, powersoft, et al. There really is no
reason to believe that this would not be a profitable venture.

I think that the leadership will have to come from a big company that
can afford to take loses for a few years while an environment of
interest is cultivated in the popular media and with the "hobby"
programmers. If this is IBM or Fujitsu, who knows! BUT I hope SOMEONE
steps up to the plate and delivers this product.

*****************************************************************
prg··.@ep··x.net
url http://www.epix.net/â€¾prgsdw
*****************************************************************
```

###### ↳ ↳ ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

_(reply depth: 5)_

- **From:** "red..." <ua-author-9624@usenetarchives.gap>
- **Date:** 1997-09-17T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3636c8adbe-p6@usenetarchives.gap>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell> <gap-3636c8adbe-p2@usenetarchives.gap> <gap-3636c8adbe-p4@usenetarchives.gap> <gap-3636c8adbe-p5@usenetarchives.gap> <gap-3636c8adbe-p6@usenetarchives.gap>`

```

Here is another e-mail response I got on this subject, permission has
been granted for this posting. All the points here are good ones:

To: "Thane Hubbell"
Subject: Re: PC COBOL - Cost of Compilers - Market for them,
etc...
From: Mayer Goldberg
Date sent: 16 Sep 1997 18:38:06 +0200

I couldn't agree with you more.

I am picking up cobol part time. I purchased a $50 personal cobol toy
from MF, and that's all the cobol I have. I simply cannot spend the
kind of money these guys want for a full featured cobol system. And
don't think I don't have a queue full of projects waiting, just for
the right moment when I can afford a reasonable system.

Cobol vendors are making a dreadful mistake: They assume you're either
a student, and so you should be able to manage with some castrated
student version: bizzare limits, no gui, no support, no stand alone,
etc., or else that you're a full time developer that can afford to
purchace a several thousand dollar system. Now if you look at the
situation with C/C++/Pascal/Java, it's the exact opposite. You can
either buy a student version, if you're a student, for some $50, and
get a full features system and no phone support, or else pay ~$300 and
get the real thing, with no holding back. I mean, for $300 or so, you
can start producing useful code that can be sold. Some companies,
notably Borland, have some tricky rules as to what you can do with
their products, but if we're talking application programming, no one
will ask you for any royalties if you want to sell or give away the
code you write. Borland started this revolution with their cheap turbo
pascal. I'm no pascal fan, but for $50 you could actually start a
company and sell software. It was that simple.

But cobol vendors don't think like that, and that's why only real
companies can afford to purchase a real cobol compiler. This is a
dreadful shame. I believe it is this pricing policy that drives many
people away from cobol. The language is changing, is developing, is
getting neater and slicker by the day, cobol 97 is out with objects,
and local variables, and everything people have been wanting to see in
cobol, but it will never gain popularity, and all because of this
crazy pricing scheme. In the long run, cobol vendors are doing
themselves more harm than good.

Just my two cents,

Mayer

And a little more----->

Date sent: Wed, 17 Sep 1997 09:51:07 +0300
From: Mayer Goldberg
To: red··.@i··.net
Subject: Re: PC COBOL - Cost of Compilers - Market for them,
etc...
Send reply to: gma··.@iil··l.com

Actually this was a personal reply, but feel free to post it if you
like.

BTW: Let me add that writing a parser for a language is not a
catastrophe. There are programs like lex & yacc, that make writing
easier, and once the grammer is reasonably stable, you use it for all
the relevant language products you have. What I'm saying is that if
since student editions are available for $50 or so, and those
obviously incorporate the extremely detailed parser for cobol, it
cannot be the parsing that keeps the prices high. Of course, a
language with many language constructs is going to require a great
deal of effort to compile. But cobol 85 (cobol 97 not withstanding)
doesn't have many semantic complications, and is rather
straightforward to compile. The compiler is, as I said, huge, but each
construct is easy to compile in itself. This is especially true for
those cobol vendors that only compile away the control structures, and
call library procedures for everything else (rather than
inline). Still I'm not saying that writing a cobol compiler is an easy
task.

But neither is a C++ compiler! And the difference in the complexity of
the compiler between C and C++ is great, and yet the transition from C
to C++ was marked by no price increase. Borland C++/C sells for about
what Borland C used to sell, and the same goes for MS VC++.

While the sheer size of the cobol compiler can explain some increase
in price when compared to the standard C++/C/Pascal/Etc, I think the
real reason for the dramatic increase in price should be found in the
clues you gave in your original posting: By trying to package the
compiler with mainframe communication and databasing tools, what the
cobol vendors are really saying is they think you're either developing
for a mainframe or porting from a mainframe, or else just want to
maintain the same mainframe-like environment. But unless this is just
what you're doing, and for many PC programmers this is just the
opposite of what they're doing, you end up paying for all this
nostalgia you don't want, don't need, and may never use.

Most people who program on a PC are programming for the PC. Therefore
they want: A standard, simple, straightforward interface to
Windows. As for data processing, MS SQL is probably what most
PC programmers are looking for.

There is a whole world outside of mainframe computing, and cobol
vendors, by dragging along all those expensive mainframe tools
wherever they go, just re-enforce the dinosaur image of cobol. What we
need is an MS Cobol, or Turbo Cobol -- A light, inexpensive tool,
that's native to Windows, that allows for rapid Windows development,
and that doesn't tie the programmer down with licensing fees. There is
a whole market of PC data processing, and it's been developing for
years without cobol, and the fault for this is primarily with the
cobol vendors. The decision to price cobol at the same level as VC++
is a marketting decision, not a programming decision, and it cannot be
defended by pointing at the complexity of either the language or the
compiler.

Best regards,

Mayer Goldberg
```

###### ↳ ↳ ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

_(reply depth: 6)_

- **From:** "michael c. kasten" <ua-author-6589049@usenetarchives.gap>
- **Date:** 1997-09-16T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3636c8adbe-p7@usenetarchives.gap>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell> <gap-3636c8adbe-p2@usenetarchives.gap> <gap-3636c8adbe-p4@usenetarchives.gap> <gap-3636c8adbe-p5@usenetarchives.gap> <gap-3636c8adbe-p6@usenetarchives.gap> <gap-3636c8adbe-p7@usenetarchives.gap>`

```

Thane Hubbell wrote (quoting Mayer Goldberg):
[snip]
› Cobol vendors are making a dreadful mistake: They assume you're either
› a student, and so you should be able to manage with some castrated
› student version: bizzare limits, no gui, no support, no stand alone,
› etc., or else that you're a full time developer that can afford to
› purchace a several thousand dollar system.

What we have here is a textbook case of partitioning the market, a
classic technique for maximizing revenue. Charge high prices to
customers who are willing to pay them, but offer discounts to
others so that you don't lose those sales. For example:

There's a Six Flags park near my home. Every summer, local residents
(whose attendance is sensitive to price) can get discounts through
the local newspaper, public schools, and the like. Visitors from
out of town pay full price -- they've already spent a lot on motels
and gas or airfare, and they're not going to turn around and walk away
over a few extra bucks.

In the case of personal Cobol, it's clearly not the same product
as the full package, but it costs about the same to the vendor: a
few dollars for a CD, a box, and postage. Or whatever. They can
make a profit off impoverished students without losing many of the
more lucrative sales of the uncrippled product.

› BTW: Let me add that writing a parser for a language is not a
› catastrophe. There are programs like lex & yacc, that make writing
…[4 more quoted lines elided]…
› cannot be the parsing that keeps the prices high.
[snip]

Cobol was invented long before lex and yacc were. I am no compiler
maven but as I understand it Cobol is unusually difficult to fit into
the lex/yacc paradigm. Not impossible, perhaps, but difficult.

Agreed, for full-featured, high-end compilers the cost of developing
the parser probably does not dominate the cost of producing the whole
package. Where it matters is at the low end -- and I am not
referring to the student version you mentioned. Having developed
the parser for the full version, the vendor can reuse it in a cheap
student version at little cost or risk.

It is possible for a single person to write an entire C compiler
from start to finish, as a hobby or bootleg project. It would
probably be a pretty bare-bones compiler, but the writer could use
it, and could pass it around to her friends or try to sell it. I
suspect that this scenario has happened more than once.

It is difficult to imagine this mode of development for Cobol.
Pieter Hintjens of iMatix (http://www.imatix.com) wrote (though
I can't find the reference at the moment) that he once tried to
write a portable Cobol compiler but abandoned it. He remarked that
a Cobol compiler was the Mt. Everest of compilers, and he only got
as far as Heathrow airport. (For me that would be a long trip, but
Pieter lives in Antwerp, just a short hop from London.)

Parsing is not the only problem. An implementation of Cobol must
support SORT, MERGE, and indexed files. It's not trivial to provide
that functionality, quite apart from the parsing. C compilers don't
have to.

Yes, I know about Cobol650, but I don't know its history. Maybe it
disproves all of the above. Still, I doubt that we will ever see
the Cobol equivalent of the Mix C compiler, which sells for about
$30 US as I recall.

› But neither is a C++ compiler! And the difference in the complexity of
› the compiler between C and C++ is great, and yet the transition from C
› to C++ was marked by no price increase. Borland C++/C sells for about
› what Borland C used to sell, and the same goes for MS VC++.

C++ is a different story. Whereas Cobol became a monster by the
accretion of detail, C++ became a monster by the accretion of
subtleties.

Just as I don't expect to see a cheap Cobol compiler, I don't expect
to see a cheap C++ compiler, except where the vendor partitions the
market as described above.

The GNU products are an obvious exception. I'll never understand the
economics of GNU. However, I suspect that the GNU people are in no
hurry to produce a free Cobol compiler. They probably consider the
language to be lower than pond scum.

[snip the rest, which I mostly agree with]

Michael C. Kasten mc··.@swb··l.net
http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

_(reply depth: 7)_

- **From:** "tom morrison" <ua-author-1138665@usenetarchives.gap>
- **Date:** 1997-09-17T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3636c8adbe-p8@usenetarchives.gap>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell> <gap-3636c8adbe-p2@usenetarchives.gap> <gap-3636c8adbe-p4@usenetarchives.gap> <gap-3636c8adbe-p5@usenetarchives.gap> <gap-3636c8adbe-p6@usenetarchives.gap> <gap-3636c8adbe-p7@usenetarchives.gap> <gap-3636c8adbe-p8@usenetarchives.gap>`

```


The following are my opinions, and do not in any way represent any
official position of my company.
===

Michael C. Kasten wrote:


› Agreed, for full-featured, high-end compilers the cost of developing
› the parser probably does not dominate the cost of producing the whole
…[3 more quoted lines elided]…
› student version at little cost or risk.

Finally, someone gets it right. And, after another , Michael
continues to get it right.

› Parsing is not the only problem.  An implementation of Cobol must
› support SORT, MERGE, and indexed files.  It's not trivial to provide
› that functionality, quite apart from the parsing.  C compilers don't
› have to.

Yes, folks. There is more to COBOL than parsing. Go buy the COBOL
standard (which itself is priced beyond some of the numbers demanded in
this group) and determine just how much is parsing and how much runtime
behavior is dictated. For those that demand no runtime royalty (along
with a low "compiler" price), stop and think about the magical Microsoft
money engine of an almost bygone era - MS-DOS. Microsoft managed to get
a runtime royalty on virtually every machine sold for a set of code the
size of which compares to the typical PC/UNIX COBOL runtime support
library. DOS (or Windows) doesn't implement indexed files, nor does it
implement correct behavior for the other file types as defined by the
standard. The PC vendors didn't whine about these runtime royalties --
they weren't able to sell (very many) machines without it.

› Yes, I know about Cobol650, but I don't know its history.  Maybe it
› disproves all of the above.  Still, I doubt that we will ever see
…[3 more quoted lines elided]…
› 
 
› The GNU products are an obvious exception.  I'll never understand the
› economics of GNU.  However, I suspect that the GNU people are in no
› hurry to produce a free Cobol compiler.  They probably consider the
› anguage to be lower than pond scum.

GNU, like cobol650, are not products, but rather chunks of software.
Nor are they free; they just spread the costs out a diffferent way. Or
perhaps there is no cost to those who try to use cobol650, e.g. When
they need help, they just call up the vendor's technical support line:
comp.lang.cobol, so we all get to pay (in tiny increments) for their
support. Of course, I am assuming that the time used by those trying to
get cobol650 to work is worth very little.

If this is such a HUGE market, would one of the complainers please step
up with the business plan and financing? I think I know where you could
get a very fair hearing.
```

###### ↳ ↳ ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

_(reply depth: 8)_

- **From:** "red..." <ua-author-9624@usenetarchives.gap>
- **Date:** 1997-09-18T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3636c8adbe-p9@usenetarchives.gap>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell> <gap-3636c8adbe-p2@usenetarchives.gap> <gap-3636c8adbe-p4@usenetarchives.gap> <gap-3636c8adbe-p5@usenetarchives.gap> <gap-3636c8adbe-p6@usenetarchives.gap> <gap-3636c8adbe-p7@usenetarchives.gap> <gap-3636c8adbe-p8@usenetarchives.gap> <gap-3636c8adbe-p9@usenetarchives.gap>`

```


On Thu, 18 Sep 1997 09:04:48 -0500, Tom Morrison
wrote:


› If this is such a HUGE market, would one of the complainers please step
› up with the business plan and financing? I think I know where you could
› get a very fair hearing.
›

Tom,

If I wasn't so broke paying for compilers I would! . Seriously
though, the attitude amongst MOST compiler vendors (I cannot include
RM - they were FIRST at PC COBOL, geared specifically toward PC
development and not toward off mainframe development), is that the PC
COBOL is a way to work on your mainframe code. That's not what I want
or need. I would be entirely happy if CA-Realia would release a clone
of their 4.2 product in 32 bit. Just the plain PC Compiler for
Windows. But I don't want to pay $4000.00 for their full CICS
offmainframe development suite. I don't need it. Let's spilt out
the tools and let us buy what we want.
```

###### ↳ ↳ ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

_(reply depth: 7)_

- **From:** "drake coker" <ua-author-6589488@usenetarchives.gap>
- **Date:** 1997-09-22T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3636c8adbe-p8@usenetarchives.gap>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell> <gap-3636c8adbe-p2@usenetarchives.gap> <gap-3636c8adbe-p4@usenetarchives.gap> <gap-3636c8adbe-p5@usenetarchives.gap> <gap-3636c8adbe-p6@usenetarchives.gap> <gap-3636c8adbe-p7@usenetarchives.gap> <gap-3636c8adbe-p8@usenetarchives.gap>`

```

Michael C. Kasten wrote:
› 
› [snip]
…[13 more quoted lines elided]…
› 


I tried using circa-1986 versions of lex and yacc when writing Acucobol.
It did not work for a silly reason: yacc (or lex? - don't recall now)
could
not handle the > 256 reserved words in COBOL. That probably has been
fixed by now.


› Agreed, for full-featured, high-end compilers the cost of developing
› the parser probably does not dominate the cost of producing the whole
…[4 more quoted lines elided]…
› 


The parser part is pretty easy. By and large COBOL is a straightforward
language to parse. For Acucobol, I ended up writing a simple set of
tools to do the parsing - probably spent about 3 weeks on these tools.


› It is possible for a single person to write an entire C compiler
› from start to finish, as a hobby or bootleg project.  It would
…[16 more quoted lines elided]…
› 


For the record, I managed to complete Acucobol, including the file
system,
a decent debugger and windowing extensions, in about 18 months - by
myself.
It can be done. That was to the '74 standard. Add a few more months
for
the '85 standard. Of course, that was for version 1.0 ;)


[snip]


There has been lots of discusion here about the lack of a low-cost COBOL
compiler.
This is a topic we (Acucobol, Inc) discuss internally about once a
year. Here are the
kind of problems we think about:

* How do we handle support.

* How do we distinguish the low-cost version from the high-end version
(ie, how do we
not loose sales to our own product).

* For Acucobol, in particular, how do we deal with the loss of runtime
royalties (assuming
that we want to allow the software developed to be freely
distributable). Runtime
pricing is a big part of Acucobol's income - abondaning that would
require a big repricing
of all the products.

All of these problems are solvable, but present just enough of a
thought-barrier that the
whole problem gets put off (there is always plenty of other stuff to
work on). Particularly
since we don't expect to see much revenue from the low-end product.

In principle, Acucobol would love to see some low-cost solutions
available. We have, of course,
a long term interest in encouraging the use of COBOL! Maybe, someday,
we will solve these
issues and produce something.

Just thought it would be interesting to see the issue from a
manufacturer's viewpoint.

BTW - I should mention that these are just my thoughts, they do not
represent any official
position of Acucobol, Inc.

- Drake
```

###### ↳ ↳ ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

_(reply depth: 6)_

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1997-09-27T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3636c8adbe-p7@usenetarchives.gap>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell> <gap-3636c8adbe-p2@usenetarchives.gap> <gap-3636c8adbe-p4@usenetarchives.gap> <gap-3636c8adbe-p5@usenetarchives.gap> <gap-3636c8adbe-p6@usenetarchives.gap> <gap-3636c8adbe-p7@usenetarchives.gap>`

```

As I have been following the posts about the cost of COBOL compilers, I
agree that the pricing for them is higher than other language compilers.
I also agree that the pricing has a tendency to prevent individuals from
purchasing PC COBOL compilers. However, if you compare the costs of
C/C++ and others ($300-$400) dollars for the professional versions and
the **base** COBOL products (non-workbench), there are a few things you
have to take into consideration with COBOL.

A proper COBOL compiler must have built-in support for keyed files and
sorting. Since other languages do not support these natively, they are
generally purchased separately. These could cost several hundred
dollars. COBOL also contains a great deal of functionality that's built
into the language that would also have to be written by the user, or
libraries purchased. An $800-$900 base price of a COBOL product is not
really too out of line considering this added functionality. And these
prices (at least MicroFocus and CA-Realia) have been fixed for quite
some time.

I believe the greatest push for COBOL on the PC was to allow development
of mainframe applications on the PC to reduce costs. As time went by, I
have come to the conclusion it is better to develop and test the
applications in their native environments using tools designed for the
native environment. Duplicating a mainframe environment (from large
VSAM, databases, CICS, PL/I and Assembler) is just to complex and
time-consuming. Better to leave it where it is. Some smaller tasks
work O.K.

Personally, I would like to see the pricing more reasonable so more
people would have access to the COBOL language and products. Someone
indicated that COBOL would not gain popularity because of the pricing
schemes. COBOL is already popular, contrary to unpopular belief.
COBOL's main customer is still the corporate world, and it appears to do
well there. There have also been suggestions that Microsoft or Borland
do Cobol. Microsoft had a COBOL of their own and dumped it. They then
marketed Microfocus COBOL under the Microsoft name--dumped that too.
The simple truth is that Microfocus and Borland are not interested in
COBOL products. If anything, they problably wish they didn't exist.

I also read a post from a COBOL compiler company who indicated that the
subject of lower cost compilers comes up every year. They indicated
that it could cut into their royalties, which appears to be a large part
of their income. I dislike the idea of royalties more than anything.
It should be as welcomed as disk copy protection. You pay hundred of
dollars to purchase the development tools, spend thousands of dollars to
develop a product, and then you have to pay to use it? That's absured.
The legal hassles aren't worth it either. None of my products require
royalties.

A final issue that's worth mentioning is the discussion of GUI
capability in a product. I do not believe that a single company can do
everything well. For example, while I have the greatest respect for the
CA-Realia COBOL compiler, I do not care for CA's GUI solutions. I use
another product (Flexus Sp/II) for my GUI development.

I really don't know what the answer is. If I had to guess, the major
COBOL compilers are intentionally targeting their marketing and sales to
the corporate world. They know COBOL is used heavily there and they
will pay those prices. I really wonder if cheap COBOL would change the
market for COBOL and the perceptions about COBOL (in so much as COBOL
has been proclaimed dead so many times it is now immortal). I guess it
depends on your personal and professional need for these products to
determine if spending the money is worth it to you. I sure would like
to have to spend less, too. I spend a great deal more money on hardware
upgrades and software version upgrades than I have ever spent on COBOL
tools.


Mike Dodas

(Remove NOSPAM! for e-mail replies)
```

###### ↳ ↳ ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

_(reply depth: 7)_

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1997-09-27T20:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3636c8adbe-p12@usenetarchives.gap>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell> <gap-3636c8adbe-p2@usenetarchives.gap> <gap-3636c8adbe-p4@usenetarchives.gap> <gap-3636c8adbe-p5@usenetarchives.gap> <gap-3636c8adbe-p6@usenetarchives.gap> <gap-3636c8adbe-p7@usenetarchives.gap> <gap-3636c8adbe-p12@usenetarchives.gap>`

```

Michael Dodas wrote:
› 
›  There have also been suggestions that Microsoft or Borland
…[4 more quoted lines elided]…
› 


Sorry for the typo in the above statement. I indicated that Microfocus
and Borland are not interested in COBOL. I meant Microsoft--not
Microfocus. Now that's a real blunder on my part! Sorry Microfocus.


Mike Dodas

(Remove NOSPAM! for e-mail replies)
```

###### ↳ ↳ ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

_(reply depth: 7)_

- **From:** "bob findley" <ua-author-1999168@usenetarchives.gap>
- **Date:** 1997-09-30T20:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3636c8adbe-p12@usenetarchives.gap>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell> <gap-3636c8adbe-p2@usenetarchives.gap> <gap-3636c8adbe-p4@usenetarchives.gap> <gap-3636c8adbe-p5@usenetarchives.gap> <gap-3636c8adbe-p6@usenetarchives.gap> <gap-3636c8adbe-p7@usenetarchives.gap> <gap-3636c8adbe-p12@usenetarchives.gap>`

```

Michael Dodas wrote in article
<60n084$2.··.@hor··w.com>...
› As I have been following the posts about the cost of COBOL compilers, I
› agree that the pricing for them is higher than other language compilers.
…[14 more quoted lines elided]…
› some time.


This talk of COBOL and it's requirements (indexed files) being the reason
for the cost is HOGWASH!!!!!!!!!

VB, Delphi, and others may not require these things BUT THEY ARE INCLUDED
!!!!!!!
And ussually go above and beyond the BASE COBOL requirements.

Guess what... They cost between $250.00 and $500.00.

Just my opinion!!
Bob Findley
------------------------------------------------------------------
The new rules of the devlopment process:
Alpha Testing: A Clean Compile.
Beta Testing: Put it in Production.
------------------------------------------------------------------
```

#### ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

- **From:** "bi..." <ua-author-8405640@usenetarchives.gap>
- **Date:** 1997-09-09T20:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p15@usenetarchives.gap>`
- **In-Reply-To:** `<01bcbeb7$2ec53520$50752581@thane-hubbell>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell>`

```

Thane,

Your post got me so "fired" up I forgot to answer your question:

I think the $200 range is appropiate; competitive with other PC development
tools; that's just the "basic suite". I think they could charge more for
"add-on"s.

BTW, I am investigating Flexus's SP2 for windowing; I'm hoping it will help us
"pretty up" our DOS based product.
```

#### ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

- **From:** "michael c. kasten" <ua-author-6589049@usenetarchives.gap>
- **Date:** 1997-09-10T20:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p16@usenetarchives.gap>`
- **In-Reply-To:** `<01bcbeb7$2ec53520$50752581@thane-hubbell>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell>`

```

Thane Hubbell wrote:
›
› Bear with me, I'm about to go on a tirade. There's a large untapped

[tirade snipped: PC-based COBOL compilers cost too much, compared to
comparable C compilers]

In fairness to compiler vendors, we should recognize that Cobol is
a much larger and more complex language than C.

To begin with, the syntax is richer. Consider a crude measure:
Standard C has 32 reserved words, not counting a few compiler-specific
extensions like 'near' and 'far'. IBM COBOL II has over 500 reserved
words. I don't know how many of those are IBM extensions.

COBOL code tends to be easier for a human to understand, but harder
for a compiler to parse. Consider, for example, the zillion different
ways you can code an edited PICTURE clause, which the compiler has
to interpret. The most comparable thing in C is the printf() family
of functions for formatting output -- but the format is interpreted
at runtime, not at compile time.

COBOL must support a wide variety of numeric data types. C is
designed specifically to support only those numeric types which are
easy for the compiler to support.

Finally, COBOL must support SORT, MERGE, and indexed files. C
doesn't. (C has a qsort() function but it only sorts an array, not
an external file.)

All things considered, I'm not surprised if a COBOL compiler is
more expensive to develop -- hence to buy -- than a C compiler.

Having said all that, I too would like to see cheaper compilers.
I was quick to grab the Fujitsu offer (which expires in a few weeks,
as I recall).

Michael C. Kasten mc··.@swb··l.net
http://home.swbell.net/mck9/cobol/cobol.html
```

##### ↳ ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

- **From:** "red..." <ua-author-9624@usenetarchives.gap>
- **Date:** 1997-09-11T20:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3636c8adbe-p16@usenetarchives.gap>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell> <gap-3636c8adbe-p16@usenetarchives.gap>`

```

On Thu, 11 Sep 1997 17:57:32 -0500, "Michael C. Kasten"
wrote:

› Thane Hubbell wrote:
›› 
…[12 more quoted lines elided]…
› 

I don't really buy that as a problem. The "real" problem as I see it
is that they want us to buy ALL the TOOLS. The CA Realia Work bench
has a mainframe interface, CICS emulation, and a ton of other stuff I
frankly don't need to do PC development.

What I need is: Base 16 and 32 bit compiler.
Good indexed file structure built in
Easy access to the Windows API
Interactive debugger

Let us pay EXTRA for SQL, CICS, ODBC, etc...

COBOL compilers can be TIGHT. CA-Realia is such a complier. Very
small EXE, no extra DLL's or runtime to send, FAST and small.
Compiles quickly. I want the same thing as my 16 bit realia, in 32
bit without all the bells and whistles, at a decent price.

Most everyone e-mailing me has indicated 2-300 bucks is a good deal.
No runtime fees. Provide fixes, but updates to new versions could be
available for a fee.

Here are some comments I have from E-mail.

From: Tim Nicholson
To: "'red··.@i··.net'"
Subject: RE: PC COBOL compilers
Date sent: Thu, 11 Sep 1997 13:28:42 -0400

Thane,
I agree with you 100%. I have been a COBOL programmer for 7
years, and
I love developing COBOL on the PC. In fact, the last place I worked,
we did
all our COBOL development at the PC level (using AcuCOBOL). Ever
since I
learned COBOL, I have long sought for an affordable, personal COBOL
compiler. I knew there were the "freebies" available, but they did
not
offer the robust features that compilers like MicroFocus and AcuCOBOL
offered (Windows support, etc.). I, too, have recently discovered
Fujitsu's
compiler, but I have yet to do much with it. I would be willing to
pay
$200-$300 on a compiler just for my personal use. It's high time the
COBOL
compiler developers woke up and smelled the coffee. And their excuse
that
they can't afford to develop a compiler for a low price is hog-wash in
my
opinion.


Thane Hubbell wrote:

Bear with me, I'm about to go on a tirade. There's a large untapped
resource out here, and it is being ill served by the different COBOL
vendors. This post is a little long, but I think I will make some
valid
points. I want you to answer the question at the end of the
posting.

The basic premise is that there is a market for a PC based COBOL
compiler -
not for resizing Maine Frame applications, nor for doing Mainframe
development offline, but for targeted PC applications. The compiler
need
only support Windows, and does not NEED a ton of other things
included.
Now, before the compiler vendors start screaming that they have
this, let
me explain.

In 1991 I had an "idea" for a PC based computer program that I
wanted to
sell. I'm a pilot, and something called DUAT was being introduced.
It
allows pilots to call with their PC's and download aviation weather
information. The weather was in "FAAese" though- the old teletype
method.
As a flight instructor (Part time - I've been a COBOL programmer
full time

since 1983) , I was teaching my students to read this stuff. It's
not
very
clear sometimes and different abbreviations mean different things
based on
context. I knew that I could write an application that would take
this
weather and "translate" it into English - expanding all
abbreviations and
making it clear and easy to understand. I had experience with
several PC
based products for development. At work I had used Realia COBOL,
BASIC,
Micro Focus COBOL and RM COBOL. I could develop my system in BASIC
- but
I
was much faster in COBOL and I could do a better job.

I purchased a PC, and decided to buy Realia COBOL - knowing how much
faster
and reliable it was than the other COBOL compilers. I spend an arm
and a
leg on the compiler, $900.00, plus $400.00 for the SCREENIO product
so I
could have a good user interface. Yearly maintenance was $160.00
for the
compiler and $65.00 for SCREENIO. This was the "basic" version of
Realia
offered from Realia itself - before the Panasophic or CA
acquisition. This

was a LOT of money for me for a part time venture.

I developed my system. It was GREAT. Reliable and worked well. I
started
to market it in the Aviation magazines, and have about 50 sales at
$35.00 a
pop. The ads were costing just about what I was making on the
software. I
had a problem in that the software was not fully integrated - it did
not
make the phone call to the DUAT vendor, it relied on other
communications
software and the user capturing the data file. I decided I needed
to do
that for myself. I hunted on BBS's and found some communications
routines
designed to be called from C. Realia has a robust calling
convention
system for calling other languages, and while I barely knew C (I waa
running my own BBS with soucce code in C - I learned C so I could
modify
the code), I was able , working with the author of the routines, to
get
them to work from Realia. Everything was going fine - I still had
not
recouped my $$ for the PC or the development tools, but I had a cool
system
that was selling. Then the "unthinkable" happened - the FAA started
providing plain english briefings via the DUAT and my sales went in
the
toilet. The lead time on the magazines I was advertising in was 3
months,
so I had 3 months of wasted advertising.

Well, since then I have continued to develop small systems for
people on a

system by system basis. All in DOS using the Realia COBOL. I have
a
friend, that runs a bowling center, and he had trouble with his
little
inhouse database system, printing labels for marketing purposes. I
told
him I could do something for him and wrote him a small system for
tracking
coupon redemptions etc. He liked it, it worked, was suprised about
"COBOL"
with the stigma it has for being a Mainframe only language, and has
since
hired me to develop a full scale bowling center management system.
It's
DOS based, runs on a LAN, and is slick. STABLE too. I never hear
from him
with problems, only the occasional request for a new sub system or
enhancement.

I have devloped other systems over the years. There is a guy where
I work

full time - on mainframes, and doing new devlopment for the PC with
MF
COBOL both for DOS and Windows with Dialog System - that runs a sub
business that we have printing statements for dental offices. He
was
having them mail in diskettes, then he went to trying to transmit
them.
The variety of communications programs and the probelmes getting
people to
connect and send were taking a lot of his time. On my own, to help
him
out, I wrote a communications program just for transmitting that
file
here.
I invented my own protocol - that was fun - and made it so the
braindead
can operate it. Just run it- it finds the modem, file, dials and
sends.
It works great and never fails - again in COBOL. For another friend
I
developed an Archery shoot tracking system - to handle registration
and
scoring and reporting at archery shoots. I have numerous other
small
systems, all targeted for the PC.

Over time I have always wanted to take them to Windows. The friend
with
the bowling software would like to package it and sell it, but it
needs to
be Windows to be marketable today. I tried the native windows
support in
Realia - but it was very difficult to understand, especially since
it was
not well documented at all.

After I got on the internet, I found something FANTASTIC for
allowing me
to
do this. That is COBOL SP2. They worked with me, and I purchased
the
product so I could take my existing and any new systems to Windows.
It
works great, and I can't recommend a company any more highly than
Flexus
and their products, both for GUI development and for Windows based
printing.

I'm about to get to the point here. Trust me!

I have some other systems I want to write. I am writing some now.
You
have to understand though, that I do this part time, in my spare
time and
I
don't make a lot of money at it. I bet there are some other people
like me
out here! Private individuals who are excellent COBOL programmers,
who
would like to develop, solid, reliable PC based applications.

Recently I decided that I probably need to go to a 32 bit compiler.
My end
users are used to the Windows 95 features, long file names, and
dislike the
degradation that occurs with Win 95 when you run a 16 bit
application.

I started pricing compilers. My first stop - what I know and what
works
well. CA-Realia. Their 32 bit version is only available in their
full
workbench product. The price is $4000.00 with $600.00 a year maint
fee.
It includes the CICS option, and a bunch or rehosting tools that,
frankly I
don't need.

Microfocus is an option, but I know that most of my stuff will take
a lot
of work to get to work under MF, and MF is dreadfully slow and a big
PIG
with what must be included with the programs that are deployed.
There are

also some runtime issues.

ACCUCOBOL has runtime fees.

Fujitsu - I'll save my comments for later - these people bear
watching,
they are up and comers in this market and MAY be the answer.

All the PC based cobol compilers to get to 32 bit are around the
same
price. MUCH MORE Than an individual can spend!!

There is a need for a PC based COBOL development system.

Here's the question I would like everyone to answer:

If it were available at reasonable cost, how much would you spend
on a PC

based COBOL, Windows development system.

$100.00?
$200.00?
$1000.00? More?

Yearly fees? Runtime fees?

I just got a card in the mail from BORLAND. I can get thier latest
and
greatest Visual developmetn suite for under $300.00. No yearly fee,
no
runtime. I don't want to take the time to learn this. I don't HAVE
the
time.

I don't have the MONEY for the COBOL compilers.

The compiler vendors tell me that they can't afford to sell their
compilers
that cheap. There is no market they say, as people are not doing PC
development with COBOL. HOW MANY WOULD if they could afford it?!?

Speak up and tell these people you want an affordable compiler.
Tell them

how many sales they will get! They all monitor this news group.

Now about Fujitsu -

This is the BEST deal I have seen. Even if you don't take advantage
of
their "Free" offer, you can get JUST the compiler (Which is all most
will
need) for $700.00 and $150.00 a year subscription fee. Even that Is
HIGH I
think, but they have been very responsive to me. I have nothing bad
to say
about them or their product. I don't have it all working for me yet
but
they are very repsonsive to me, even though they know I am small
time.
They are worth a look. HOWEVER, even their lowest priced package
is
too
expensive in my opinion.
************************************************************************
***** Timothy Nicholson, KF4RTX Intelligent Information Systems
Phone: (919) 572-0901 x234 4915 Prospectus Drive Suite C2 Fax:
(919)
572-0783 Durham, NC. 27713 email:
ti··.@ren··s.com
************************************************************************
*****


Send reply to: B W Spoor
To: red··.@i··.net
Date sent: Thu, 11 Sep 1997 19:10:04 -0400
Subject: Re: PC COBOL - Cost of Compilers - Market for them,
etc...
From: bws··.@fri··k.net (B W Spoor)

Thane,

I am replying direct, rather than via the comp.lang.cobol because I
am not sure whether my comments will further your argument or not.
Please feel free to repost my comments if you wish.

I am a COBOL Developer with 20 years plus experience, starting on
ICL mainframes and then moving down to PC/Unix systems. I have been
working for myself for some 8 years writing custom systems, in
house using a PC/DOS/Novell environment.

I use Microsoft Cobol 4.5 (and 3.0) which are badged versions of
Micro Focus and were not too bad on price (about halfthe cost of MF
equivalent), but without the run time packages which require user
licences.

I have used various versions of MF Cobol, from 8-bit CP/M based CIS
COBOL, through COBOL Level II to COBOL 2 on Unix (as a contractor).

I too find the prices of COBOL compilers fantastic. The latest MF
offering NetExpress will set me back about ukp 3,600 plus annual
maintenance, plus run time licence fees (possibly not for single
user systems).

The good thing about this product is that I can take my existing
DOS code and end up with a 32-bit Windows binary - it does work, I
have an evaluation copy. This means that I can keep common source
streams for 3 environments (Windows 32bit, DOS & Unix) and keeps
the learning curve down

I have evaluated this product for a specific project, which will
cover my outlay and enable quick and easy conversion from the
existing DOS code, and of course once I have the compiler it can be
used for other projects.

I too have a copy of the Fujitsu compiler, but have had no success
with it, but will admit that I didn't set aside enough time to play
with it. I like my manuals on paper and find difficulty using
electronic documentation.

In contrast, the MF NetExpress loaded quickly and easily from the
issue CD and I found the product easy and intuative to use, bearing
in mind that I have never used the MF Workbench environment.

I expect to stay with the MF product, because I am familiar with it
which is important, learning time costs money. However, I would
still like to see an 'affordable' product.

One company that I do some part-time contract work for (MF COBOL 2 &
Unix) is having second thoughts about MF because of runtime licensing
costs, and they currently have ruled NetExpress out because of the
cost (the price I quoted above is SINGLE USER) athough they like the
idea of it. They are moving towards Visual Basic/SQL Server, but
finding the learning curve high (experienced programmers) and the
environment far from stable, each new compiler/SQL release seems to
set them back.

Sorry if I have rambled on for too long but you did ask for
feedback.

Regards,

Brian


-----------------------------------------------------------
Brian W Spoor MBCS
Chartered Information Systems Practitioner
Friday Computer Software Phone: +44-(0)1803 852625
bws··.@fri··k.net Fax: +44-(0)1803 854926
-----------------------------------------------------------
```

###### ↳ ↳ ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

- **From:** "eugene a. pallat" <ua-author-501199@usenetarchives.gap>
- **Date:** 1997-09-11T20:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3636c8adbe-p17@usenetarchives.gap>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell> <gap-3636c8adbe-p16@usenetarchives.gap> <gap-3636c8adbe-p17@usenetarchives.gap>`

```

Thane Hubbell wrote in article
<341··.@new··m.net>...
› On Thu, 11 Sep 1997 17:57:32 -0500, "Michael C. Kasten"
›  wrote:
…[4 more quoted lines elided]…
›› words.  I don't know how many of those are IBM extensions.

I'm going to say something that will drive some people ballistic --- but
here goes. There is absolutely no reason to have reserved words in a high
level language other than to make life easier for the compiler writers, and
their convenience isn't a high priority with me. I've written assemblers,
monitors, OSs, etc., and the convenience of the user was always a high
priority. Over the years, I've received updates on languages which added a
new reserved word which was the same as a variable or label I had been
using resulting in wasted time to change programs.

In a language such as COBOL, the verbs, etc., can always be determined by
syntax. But if you do want reserved words, then they shouldn't be the same
as programmers might want to use for labels and variables.

snip

Remove the '-glop-' for sending email to me.

Gene eap··.@ori··a.com

Orion Data Systems

Solicitations to me must be pre-approved in writing
by me after soliciitor pays $1,000 US per incident.
Solicitations sent to me are proof you accept this
notice and will send a certified check forthwith.
```

#### ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

- **From:** "rtw..." <ua-author-6550399@usenetarchives.gap>
- **Date:** 1997-09-17T20:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p19@usenetarchives.gap>`
- **In-Reply-To:** `<01bcbeb7$2ec53520$50752581@thane-hubbell>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell>`

```

"Thane Hubbell" wrote:

› Bear with me, I'm about to go on a tirade.  There's a large untapped
› resource out here, and it is being ill served by the different COBOL
…[22 more quoted lines elided]…
› 

Thane:

I don't know if the following numbers will be helpful, but I collect
the stats on downloads from our ftp site. The following numbers
surprised me a bit when I saw them. You're interested in a low-cost
COBOL compiler and want to know what the demand is. Well, I don't
have the answer to those questions, but I can contribute these stats
from our ftp site. Maybe they'll be helpful.

During the period from June 10, 1996 to September 17, 1997, we
automatically generated 430 file transfer reports from our ftp site.
Each report contains the stats from all downloads which took place
during the prior download period. These reports provide us with
information on who is downloading from our site and what software they
are downloading.

During the 15 month period, we have had 16,654 downloads of our
software or the shareware compiler. I separated out the shareware
compiler stats and came up with 9,792 downloads of the cob650
shareware compiler.

That's an average of 653 downloads each month of the shareware
compiler. Please keep in mind that there is nothing scientific about
these figures. I just thought it might be interesting for the
newsgroup folks to see what kind of activity we get on the shareware
compiler. Also please bear in mind that this is only one source for
the shareware COBOL compiler.

That number isn't really enough to convince the COBOL compiler
companies to sell a $50.00 or $99.00 product. Even selling a $300.00
product would only result in a revenue stream of about $195,900 per
month or $2,350,800 per year. I'm sure that most of the compiler
companies are already making some multiple of that.

I do agree with you that offering an unbundled version of the various
COBOL compilers would allow the customer to choose which toolset they
prefer instead of being forced to pay for something that they won't or
don't want to use.

I also believe that if more compiler companies which offer a low-cost
student version, it would help proliferate the COBOL language.

Just my two cents worth.


Bob Wolfe, flexus, rtw··.@FIL··s.com
Delete FILTER from my e-mail address to reply
Check out The Flexus COBOL Page at http://www.flexus.com
```

##### ↳ ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

- **From:** "e jon" <ua-author-17071971@usenetarchives.gap>
- **Date:** 1997-09-19T20:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3636c8adbe-p19@usenetarchives.gap>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell> <gap-3636c8adbe-p19@usenetarchives.gap>`

```

Bob Wolfe wrote:

›› 
›› The compiler vendors tell me that they can't afford to sell their
…[38 more quoted lines elided]…
› Check out The Flexus COBOL Page at http://www.flexus.com


It's a cool site Bob!

Just mho here...

I would think that one reason COBOL compiler vendors don't cut the
prices
or offer compilers for the PC at "student" prices is that
"proliferation"
isn't such a big issue when you already have over $1 trillion dollars of

double-digit billions of lines of code written and running applications
internationally. Let's review, why are we doing Y2k again?

Another point is that most "students" can find a COBOL class offering
access to a compiler and/or resources required to learn the language.

If you're a "consultant", then the cost of the compiler is an
"investment"
and a tax write-off [I hope!]--not to mention the deluge of
'evaluations'
you might receive [I'm still down about not seeing the Visual Age for
Cobol (tm)
demos].

Let's look at what low-cost C/C++ compilers really do: allow someone
to
"hack" code and ship it out over the Internet. Is any of it
"excellent"? Some,
but some shareware code lacks "production quality" (ie: it will run
with a
MTBF of years not hours). Do you really want someone "hacking"
COBOL code which will potentially power business applications and
other enterprise-critical software? or do you want someone who has been

trained to use this "tool" with the precision and artistic talent of a
finely-
trained specialist surgeon?

And, I would agree that COBOL compilers are not simply dropping a
parser-synthesizer into a C/C++ or PL/1 input-file and voilla! COBOL!
Unlike C/C++ which allow all sorts of shenanigans to happen with data
and pointers (and lack binary-coded decimal to support
business-precision
fractions), COBOL has extensive data-type checking and restrictive
type-conversions. Also, it follows a concise execution definition, as
laid
out by CODASYL/ANSI, so that a COMP-1 or PACKED-DECIMAL
field results in the same data format from machine to machine--not the
chaotic 1-word, 2-word, 3-word(?), maybe 4-word "int" on C/C++
[and, this is "portability"??]

COBOL also requires a basic set of file i/o methods--sequential,
relative and
indexed. And, now, it also defines certain database linkages via
"schemas"
or "relational tables" and SQL. Most personal computers, or laptop,
operating systems do not have the logical file systems required,
so the "vendor" must provide this service. Most mainframe compilers
only need to "link" to the operating system to gain these "extensions".

In terms of SORT/MERGE...you can't invoke the SORT command
with parms on data files, as most enterprise apps require, from even the

command line--how does a COBOL program handle this? You're
talking about building a complete environment/runtime to enable
COBOL to act/walk/talk like its mainframe cousins.

I would think that unbundling COBOL would be fairly/nearly nightmarish
task. You either have to include all of the CODASYL standard or go to
the skeletal ANSI standards. Is FIPS still doing this stuff? (around?)
*BM markets lots of ANSI compilers, I bet, but most info-tech functions
probably make the COBOL for MVS &...(tm) the standard--it's beefier.

You could disable the SORT/MERGE, throw out report-generator,
but would this really be COBOL?
```

###### ↳ ↳ ↳ Re: PC COBOL - Cost of Compilers - Market for them, etc...

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-09-22T20:00:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3636c8adbe-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3636c8adbe-p20@usenetarchives.gap>`
- **References:** `<01bcbeb7$2ec53520$50752581@thane-hubbell> <gap-3636c8adbe-p19@usenetarchives.gap> <gap-3636c8adbe-p20@usenetarchives.gap>`

```



E Jon wrote in article <342··.@i··.net>...
› I would think that unbundling COBOL would be fairly/nearly nightmarish
› task.  You either have to include all of the CODASYL standard or go to
…[6 more quoted lines elided]…
› 

No one is suggesting a crippled COBOL. BASE language - yes - But with each
of the available packages there are other things bundled in. ie: CICS
Emulation, Mainframe connectivity, etc. Unbundle those functions in order
to sell the compiler at a reasonable rate.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
