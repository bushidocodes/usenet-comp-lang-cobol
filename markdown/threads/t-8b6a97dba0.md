[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Should I learn COBOL?

_28 messages · 19 participants · 1997-11 → 1997-12_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### Should I learn COBOL?

- **From:** "alan c. hines" <ua-author-17073727@usenetarchives.gap>
- **Date:** 1997-11-15T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<346F5BBF.FC7BF0C3@io.com>`

```

Over the past few months I've been teaching myself Java through a
variety of self-training texts: Learn Java on the Macintosh, Teach
Yourself Java in 21 Days, Using Java, etc. I've picked it up fairly
well, for never having gone through any standardized instruction.

After all of this, I must say I have a certain fondness for Java - I
like its built-in support for multithreading, its huge class libraries,
totally object-oriented approach, automatic memory management and so
forth. Also, I chose Java as my first programming language because of
the promised career prospects that it offered, and the fact that you can
obtain Java "certification" directly from Sun microsystems - effectively
placing yourself on the same level as CS majors with Java competency.

After reading about the Y2K bug, however, I wonder whether I shouldn't
try to cash in by teaching myself Cobol. I have numerous reservations,
however:

ï¿½ Won't I be basically unlearning all of the approaches and OOP
structures of Java by learning COBOL?

ï¿½ I got into CS essentially in hopes of making a living through
(initially) website design. Now, some two years later, despite being
_extremely_ proficient in HTML, Javascript, Shockwave, all multimedia
authoring applications for the Mac, and many other web-design aspects
(now including some proficiency in Java), I've discovered that with the
arrival of WYSIWYG HTML editors, the market has essentially evaporated -
web design positions are increasingly rare, and those that appear are
subject to FIERCE competition, and require skill levels on the order of
NT System Administration.

What this all boils down to is this: Suppose I spend the next six
months obtaining some proficiency in COBOL - enough to at least perform
as a junior programmer on Y2K projects, for example. What's the
likelihood that the current market for COBOL programmers will be yanked
from beneath my feet by advances in Y2K conversion applications? In
other words, am I getting on-board too late to really capitalize on the
opportunities afforded by Y2K?

ï¿½ How could I, as a 28-y.o. self-taught programmer, establish my
competency among a huge field of established COBOL programmers and new
CS graduates? In the case of Java, because it's so new, Sun offers its
certification program (which I am VERY close to being able to attain).
This seems like my best option for breaking into the field. But what
about COBOL? In other words: Suppose I do become a competent COBOL
programmer - how do I go about proving that, and more importantly,
capitalizing upon it? Am I basically screwed if I don't go get a CS
degree?

I have other reservations, such as having to run a COBOL compiler under
Virtual PC on my 132Mhz PowerPC - I envision the year 2000 getting here
before I'm halfway through my first textbook... :-/ . I'm also very
partial to learning how to program with the Rhapsody RAD, which was
another reason for choosing Java (webObjects, etc). But the way I see
it, if I have a real shot at breaking into the industry by learning
enough COBOL to work productively on Y2K projects, then that would be my
best option for right now - it seems the market is really wide-open.

Finally, if you wonder about my motivations - I'd really like to marry
my girlfriend, get a house somewhere nice, start having kids with her,
and so forth. Currently I survive hand-to-mouth on freelance web design
contracts, but that's not going to sustain anything greater than what I
have now. I figure programming certainly will.

So, I thought I'd ask the experts what you thought. Are any of you guys
learning Java, or would it just be a waste of your time? How about
after Y2K - would you consider Java then? Are its prospects even
remotely comparable to COBOL? Could Y2K actually HELP prospects for
Java programmers? Or should I put Java aside, focus on COBOL for a few
months, and try to break in that way? Suppose I DO learn enough COBOL
to participate - what should my next step be? Are there any COBOL
proficiency certificates or the like?

Well, I appreciate your attention, as well as any advice,
recommendations or direction you could provide. Thanks.

- Alan Hines
a.··.@i··.com
```

#### ↳ Re: Should I learn COBOL?

- **From:** "michael c. kasten" <ua-author-6589049@usenetarchives.gap>
- **Date:** 1997-11-22T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p2@usenetarchives.gap>`
- **In-Reply-To:** `<346F5BBF.FC7BF0C3@io.com>`
- **References:** `<346F5BBF.FC7BF0C3@io.com>`

```

(posted and mailed)

Richard Tung wrote:
› 
› "Michael C. Kasten"  writes:
…[11 more quoted lines elided]…
› "encapsulated".

You can encapsulate by using subprograms. By using pointers, you
can even have opaque data types.

Suppose I want to use some kind of complex data structure to
represent, for example, a service order. I have a lot of processing
to do on that service order, and I want to spread it around among
several programs, but I don't want all of them to have to deal with
the messy innards of the data structure.

So I encapsulate the data structure in a subprogram. One entry
point creates a blank service order and returns a pointer to it.
Other entry points would perform various other operations on the
service order -- add a detail line, calculate totals, whatever.
Each such entry point would take a pointer-to-service-order as a
parameter, specifying the service order on which the operation was
to be performed. Finally I have another entry point -- also taking
a pointer-to-service-order parameter -- to deallocate the order
and release whatever resources are attached to it.

See? I have a constructor, a destructor, and methods. Since the
calling programs never access the innards directly, I have
encapsulation.

This approach is not just theoretical. I do this kind of thing a
lot, in real programs. It's a little clumsier than it would be in
a real OO language, but it works. Object orientation happens in
your head, not in your compiler.

›                  As for inheritence--you can sort of achieve it with
› includes and copybooks....and polymorphism can be faked by having a
› driver subroutine be your interface to the rest of the system.  Still,
› I wouldn't call them true inheritence or true polymorphism.

I would call them true -- but clumsy.

I'm not sure what you mean by a driver subroutine. What I had in
mind was that a polymorphic object would carry some kind of field
indicating its type. Then a subroutine would inspect that field
and branch accordingly.

However, because you don't have dynamic binding, this approach is
not readily extensible. If you need a new type, you have to
modify all the code which branches on type.

An alternative is for each polymorphic object to carry a list of
subroutine names -- or a pointer to such a list -- which would
be CALLed dynamically. (That's approximately how C++ works, under
the covers, but using function pointers instead of names.) This
approach would be extensible.

It can all be done. In most cases, though, it won't be worth the
trouble.

Michael C. Kasten mc··.@swb··l.net
http://home.swbell.net/mck9/cobol/cobol.html
```

#### ↳ Re: Should I learn COBOL?

- **From:** "psych..." <ua-author-650090@usenetarchives.gap>
- **Date:** 1997-11-23T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p3@usenetarchives.gap>`
- **In-Reply-To:** `<346F5BBF.FC7BF0C3@io.com>`
- **References:** `<346F5BBF.FC7BF0C3@io.com>`

```

I have learned COBOL recently and did very well in my classes and because of
the high-demand to resolve YR2K issues I am having a tough time breaking past
the front door. I have also noticed companies asking for CICS, DB2, VSAM and a
few others as well as at least 1 year experience and mostly 3+ years
experience. For an industry that appears from the outside to have more jobs
than prospective employees I am having a tough time getting a job. I keep
plugging along and one day someone will give me the chance to gain the
experience everyone else is demanding. Good luck.
Melanie
DHO··.@A··.COM
```

##### ↳ ↳ Re: Should I learn COBOL?

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-11-23T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p3@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p3@usenetarchives.gap>`

```

Companies can be reluctant to take on unproven people as employees, but may
be more willing to hire you on a contractual basis at a beginner's rate.
That will let them evaluate you with no risk. Try approaching some companies
with this proposal. Smaller companies are probably more likely to try you
this way.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)

PSYCHELUVS  wrote:
> I have learned COBOL recently and did very well in my classes and because
of
> the high-demand to resolve YR2K issues I am having a tough time breaking
past
> the front door.  I have also noticed companies asking for CICS, DB2, VSAM
and a
> few others as well as at least 1 year experience and mostly 3+ years
> experience.  For an industry that appears from the outside to have more
jobs
> than prospective employees I am having a tough time getting a job.  I keep
> plugging along and one day someone will give me the chance to gain the
…[3 more quoted lines elided]…
>
```

#### ↳ Re: Should I learn COBOL?

- **From:** "demian neidetcher" <ua-author-108735@usenetarchives.gap>
- **Date:** 1997-11-27T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p5@usenetarchives.gap>`
- **In-Reply-To:** `<346F5BBF.FC7BF0C3@io.com>`
- **References:** `<346F5BBF.FC7BF0C3@io.com>`

```

Depends on how long you want to be in the business... if you want to be
working in 10 years I'd stay away from COBOL. There is so much that's based
on C (C++, Java, JavaScript, CShell, ...) that that's the best way to go.
It's a bear to get used to it all, but once you do you've opened a lot of
doors.
```

##### ↳ ↳ Re: Should I learn COBOL?

- **From:** "troxle..." <ua-author-8415077@usenetarchives.gap>
- **Date:** 1997-11-29T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p5@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p5@usenetarchives.gap>`

```

"Demian Neidetcher" wrote:

› Depends on how long you want to be in the business... if you want to be
› working in 10 years I'd stay away from COBOL.


Gee, somethings never change. I remember someone telling me that 20
years ago. What was it then? PL/1 or was is Pascal that I was
suppose to learn instead?

Demian probably doesn't even realize that there is more than twice as
much Cobol code out there than C and C++ combined.


Tim Oxler
TEO Computer Technologies Inc.
http://www.i1.net/~troxler
http://users.aol.com/TEOcorp
```

###### ↳ ↳ ↳ Re: Should I learn COBOL?

- **From:** "gregory paul amos" <ua-author-17071352@usenetarchives.gap>
- **Date:** 1997-11-29T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p6@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p5@usenetarchives.gap> <gap-8b6a97dba0-p6@usenetarchives.gap>`

```

In article <348··.@new··1.net>,
tro··.@i··.net (Tim Oxler) wrote:

› "Demian Neidetcher"  wrote:
› 
…[15 more quoted lines elided]…
› http://users.aol.com/TEOcorp

And that with the release of the next standard (For better of worse) COBOL will be more C like
than ever. This combined with the lack of a true follow-up platform in maintainability and in
conversion of existing code in a cost effective manner, will see COBOL in use for a long time to
come.
Greg Amos
E-Mail amo··.@ix.··m.com removing .nospam
```

###### ↳ ↳ ↳ Re: Should I learn COBOL?

- **From:** "rtw..." <ua-author-6550399@usenetarchives.gap>
- **Date:** 1997-11-30T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p6@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p5@usenetarchives.gap> <gap-8b6a97dba0-p6@usenetarchives.gap>`

```

tro··.@i··.net (Tim Oxler) wrote:

› "Demian Neidetcher"  wrote:
› 
…[15 more quoted lines elided]…
› http://users.aol.com/TEOcorp

Tim:

Please note Demian's e-mail address. It explains a lot. It contains
the notorious extension of ".edu"

I hate to make assumptions about anyone, but I would be willing to bet
that Demian falls into one of the following categories:

1. BU Student and is convinced that he knows more than the people who
have 20 or more years of experience in the business.

2. BU Instructor who has never written a program used in any
commercial operation.

3. Dean of Virtual Reality & Other Technical Thingies at good old BU
(watches too much C-Net TV at 6:00 AM on Sunday morning).

4. Trekkie who hears the voice of Bones every night, saying, "Dammit
Jim, we've got to re-write these systems on the Enterprise! They're
still written in COBOL and we solved the year 2000 star date problem
centuries ago!!"

5. Bill Gates in disguise.

.....My bet is on number 1 or 2.



Bob Wolfe, flexus, rtwolfe at spammers-are-meat-heads flexus dot com
To reply, look at my e-mail address, get rid of the spammer insult and fix the address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Should I learn COBOL?

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-11-30T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p6@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p5@usenetarchives.gap> <gap-8b6a97dba0-p6@usenetarchives.gap>`

```

Kevin wrote:
› 
› tro··.@i··.net (Tim Oxler) wrote:
…[20 more quoted lines elided]…
› going back to 10 years ago....more supply than demand.

Perhaps, but consider these two facts. 1) Every year (here in the U.S.) we
produce about 10,000 LESS programmers than the increase in demand, causing
the supply/demand gap to steadily increase. 2) Development using other
languages is turning out to be much more expensive and time consuming than
anticipated (advertised), and some companies are beginning to back away from
the politically correct approach, more toward COBOL.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: Should I learn COBOL?

- **From:** "han..." <ua-author-8441900@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p6@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p5@usenetarchives.gap> <gap-8b6a97dba0-p6@usenetarchives.gap>`

```

On Sun, 30 Nov 1997 01:10:04 GMT, kk··.@air··l.net (Kevin) dreamed up
a literary gem, but posted this instead:

› On Sun, 30 Nov 1997 01:18:05 GMT, tro··.@i··.net (Tim Oxler)
› wrote:
…[20 more quoted lines elided]…
› going back to 10 years ago....more supply than demand.

I'm not sure where you're posting from but here in the UK (and I
assume in other EC countries) Y2K is only one exercise that will keep
our talents alive. The next one (and it is starting already) is the
Euro.

For our non-European cousins, I should explain that this is the name
(bloody stupid name too) for a Single European Currency unit based on
European Monetary Union. It rules are (to be) enshrined in law and
any currency conversions follow entirely different rules than those
used for traditional currency exchange. It also has an aspect od
duality where it will operate alongside the various national
currencies.

After that we have something else, but I've forgotten what that is at
this crucial moment when I need to mention it(!@#). And then, after
all of this, we've got all of those projects that never got under way
while we were taken up with these other three major exercises. I
don't see anything in this game as having a golden future but I think
we can look on COBOL as a safe bet for some time to come. Long enough
for my needs, anyway.

Charles

----------------
Old and past it?
Not any more
----------------
```

##### ↳ ↳ Re: Should I learn COBOL?

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p5@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p5@usenetarchives.gap>`

```

Demian Neidetcher wrote:
› 
› Depends on how long you want to be in the business... if you want to be
…[3 more quoted lines elided]…
› doors.


Sounds like the same old line I've heard over and over for years:
COBOL's gonna be dead, real soon now. Don't bet the ranch. The amount
of COBOL code out their running business is staggering and it is not
going to go away anytime soon, even if everyone wanted it to.

I'd say it would be lucrative to learn COBOL than trying to learn every
derivitive of C. These bobbles don't have a tendency to stay around too
long, until the next derivitive with a more catchy name comes along.

Mike Dodas

(Remove CUTTHEJUNK for e-mail replies)
```

###### ↳ ↳ ↳ Re: Should I learn COBOL?

- **From:** "news" <ua-author-13363@usenetarchives.gap>
- **Date:** 1997-12-04T19:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p11@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p5@usenetarchives.gap> <gap-8b6a97dba0-p11@usenetarchives.gap>`

```

Based on the below, I had to respond and ask a question :
COBOL is a workhorse in our shop,even though we also have cutting edge
everything:
customer access to the web, user interfaces galore,
fast and furious communications.
Ive watched and decided to become a programmer after many years of
designing, spec'ing, and testing business applications.

It seems to me is you build the front ends to handle the small tasks,
queries and such, and work them in conjunction with
the heavier powers of COBOL/CICS batch/online programs and their extract
files.

Language wise, having learned a little of each language. COBOL works
better in that there is less chance of cuteness
(read: unmaintainable). I like delivering a product. Ive been on product
development, marketing to systems.
Bottom line, it takes all types of tools to make a profit.

The question for comment:
When it comes to massive processing, do you think that you can simply rely
on any one program language?


Michael Dodas wrote in article
<348··.@CUT··n.com>...
› Demian Neidetcher wrote:
›› 
…[23 more quoted lines elided]…
›
```

#### ↳ Re: Should I learn COBOL?

- **From:** "volker bandke" <ua-author-6589342@usenetarchives.gap>
- **Date:** 1997-11-30T19:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p13@usenetarchives.gap>`
- **In-Reply-To:** `<346F5BBF.FC7BF0C3@io.com>`
- **References:** `<346F5BBF.FC7BF0C3@io.com>`

```



› Depends on how long you want to be in the business... if you want to be
› working in 10 years I'd stay away from COBOL. There is so much that's based
› on C (C++, Java, JavaScript, CShell, ...) that that's the best way to go.

Well, about 80% of all commercially used programs in the mainframe area are written in COBOL,
about 10 % in Assembler (yes, that much), and then some PLI . The rest is made up of the
"so much that is based on C etc....)"

About 25 years ago I heard a similar argument - just that it wasn't C at that time that would replace
Cobol, but s.th. else (I can't even remember what it was - PLI? PASCAL? Who cares...



Regards

Volker Bandke
```

##### ↳ ↳ Re: Should I learn COBOL?

- **From:** "rich benack" <ua-author-8520142@usenetarchives.gap>
- **Date:** 1997-11-30T19:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p13@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p13@usenetarchives.gap>`

```

The key question of course is how many NEW COBOL systems are being
developed.

If he is looking for a position as a maintenance program then COBOL
would be a very good choice. If he is looking for mostly new development
& especially leading edge technology then COBOL is not the place to be.
This does not mean COBOL is a "bad" language or that there is not a lot
of jobs.

Rich

›› 
› Well, about 80% of all commercially used programs in the mainframe area are written in COBOL,
…[9 more quoted lines elided]…
› Volker Bandke
```

###### ↳ ↳ ↳ Re: Should I learn COBOL?

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p14@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p13@usenetarchives.gap> <gap-8b6a97dba0-p14@usenetarchives.gap>`

```

I don't know about everywhere else, but from where I sit, there is a LOT of
new development going on in COBOL. I could over commit my time two or three
times over for 1998, and only one of the jobs is Y2k, though it is a biggie
(150k+).
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)

Rich Benack  wrote:
> The key question of course is how many NEW COBOL systems are being
> developed. 
…[5 more quoted lines elided]…
> of jobs.
```

###### ↳ ↳ ↳ Re: Should I learn COBOL?

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p14@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p13@usenetarchives.gap> <gap-8b6a97dba0-p14@usenetarchives.gap>`

```



Rich Benack wrote in article
<348··.@pop··m.com>...
› The key question of course is how many NEW COBOL systems are being
› developed. 
…[8 more quoted lines elided]…
› 

That's funny. I'm currently in salary negotiation with a company that
wants to hire people for a NEW system to be written in COBOL on an MVS
mainframe. Not Y2K work, not Maint - NEW development. It's out there.
It's happening, and it's frequent.
```

###### ↳ ↳ ↳ Re: Should I learn COBOL?

- **From:** "steve wolfe" <ua-author-733217@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p14@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p13@usenetarchives.gap> <gap-8b6a97dba0-p14@usenetarchives.gap>`

```

Rich Benack wrote:
› 
› The key question of course is how many NEW COBOL systems are being
…[21 more quoted lines elided]…
›› Volker Bandke

Well, let's see: We have a pretty interesting feature at my company, we
can take requests for prescriptions over the internet. Not that that's
leading edge or anything now, but definately not "back burned" either.
All of the HTML/CGI collected data is shipped to our mainframe where
good old CICS tasks are kicked off to handle placing the data into our
stores pending rx queue. Unfortunately the application of leading edge
technology is not solely the domain of the pc developers. We are
developing a few new systems in COBOL. As a matter of fact, some of our
critical systems are being rewritten in COBOL now, so I don't think that
from where I'm sitting that your comments are valid.

Steve

*****************************************************************

            Support the Western Bigfoot Research effort
                         for information:
             http://www.teleport.com/‾caveman/wbs.html

prg··.@ep··x.net
url http://www.epix.net/‾prgsdw
*****************************************************************
```

###### ↳ ↳ ↳ Re: Should I learn COBOL?

- **From:** "cha..." <ua-author-8441878@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p14@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p13@usenetarchives.gap> <gap-8b6a97dba0-p14@usenetarchives.gap>`

```

On Mon, 01 Dec 1997 20:28:32 -0800, Rich Benack
wrote:

› The key question of course is how many NEW COBOL systems are being
› developed.

There is plenty of new development going on in COBOL. The only thing
that's getting in the way of development at the moment are massive
projects like Y2K and the Euro.

› If he is looking for a position as a maintenance program then COBOL
› would be a very good choice. If he is looking for mostly new development
› & especially leading edge technology then COBOL is not the place to be.

Where do you get this idea from? Evidently not from my shop, nor from
many others.

› This does not mean COBOL is a "bad" language or that there is not a lot
› of jobs.

Patronising git.


Charles F Hankel
------------------------------------------------------
COBOLs: IBM D, E, F, ANS v4, VS, COBOL 2, LE/370, AIX
Honeywell GCOS, Burroughs 7000, Tandem, HP3000
all to varying degrees over the past 25 years
```

###### ↳ ↳ ↳ Re: Should I learn COBOL?

- **From:** "troxle..." <ua-author-8415077@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p14@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p13@usenetarchives.gap> <gap-8b6a97dba0-p14@usenetarchives.gap>`

```

Rich Benack wrote:

› The key question of course is how many NEW COBOL systems are being
› developed.
›

Plenty. NEW COBOL systems is what I've been doing. I've even been
fortunate enough to do all of my new development work from home as a
telecommuter. In fact, I shouldn't even be spending time writing this
because I've got way too much work to do!

You might be surprized, but Cobol is still, and always will be, the
preferred choice for business data processing. It was written for
business, and it is by far, much easier to maintain than other
languages. And that is why it is the dominant player.


› If he is looking for a position as a maintenance program then COBOL
› would be a very good choice. If he is looking for mostly new development
…[4 more quoted lines elided]…
› 		Rich

Because Cobol has proven itself as a work horse and it's reliability
there is a lot of code to maintain. People forget that the early
systems were written in FORTRAN and Assembler. Cobol came in, and
flat out replaced them.

Then PL/1 was suppose to replace Cobol, then Pascal. Now it's C, C++,
VB, and Java.

True, each of these languages have made inroads. But the one thing
that others cannot match is Cobol's reliability and maintainability.
In 1991, during the rush to client/server craze Cobol was left out in
the cold because of it's "legacy". Can't do new technologies with old
languages. Then, around 1995, after these c/s systems matured,
surprize, surprize, much of the "new technology" code got hard to
maintain. All of the sudden, people were interested in Cobol again.

In 1995, Sentry Market Research ask IS shops which languages they used
for NEW APPLICATION DEVELOPMENT on client/server, and guess what? The
number 2 language preferred was Cobol.

You miss the point Rich. We've seen it before, we've heard it before.
10 years from now there will be another language that will come along
that will be touted as the language of the future. And there will be
someone just like you who will disdain Cobol as a maintenance
language. And Cobol will be then as it is now, the world's most used
programming language.

Tim Oxler
TEO Computer Technologies Inc.
http://www.i1.net/~troxler
http://users.aol.com/TEOcorp
```

###### ↳ ↳ ↳ Re: Should I learn COBOL?

_(reply depth: 4)_

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p19@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p13@usenetarchives.gap> <gap-8b6a97dba0-p14@usenetarchives.gap> <gap-8b6a97dba0-p19@usenetarchives.gap>`

```

Tim Oxler wrote:
› 
› Rich Benack  wrote:
…[51 more quoted lines elided]…
› 

Bullseye, Tim!
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: Should I learn COBOL?

_(reply depth: 4)_

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1997-12-02T19:00:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p19@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p13@usenetarchives.gap> <gap-8b6a97dba0-p14@usenetarchives.gap> <gap-8b6a97dba0-p19@usenetarchives.gap>`

```

Tim Oxler wrote:

› You might be surprized, but Cobol is still, and always will be, the
› preferred choice for business data processing.  It was written for
› business, and it is by far, much easier to maintain than other
› languages.  And that is why it is the dominant player.

Always is a very long time, but for now and the foreseeable future you
are correct. Cobol's popularity will rise and fall with current
fashion, but Cobol will be a major force.

Yet I have always felt that if Pascal or C just implemented Cobol
PICTURE -- not something like it, but the exact syntax and semantics of
Cobol PIC -- they could replace Cobol. The string would have to be in
quotes or you'll bust you're scanner. Pascal has better data
declaration syntax than Cobol; if you added PIC, what would make Cobol a
better business language?

› Because Cobol has proven itself as a work horse and it's reliability
› there is a lot of code to maintain.  People forget that the early
› systems were written in FORTRAN and Assembler.  Cobol came in, and
› flat out replaced them.

Ummmm, I'm not sure about the historical order. Fortran is only about
two years older than Cobol. There were "assembler" languages pre-date
Cobol, but Cobol has about seven years on BAL. The IBM 360 had BAL
first, but it had Cobol and Fortran in about a year.

› You miss the point Rich. We've seen it before, we've heard it before.
› 10 years from now there will be another language that will come along
› that will be touted as the language of the future.

It's here: OOCobol
I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
L  |/   
o  |\        Bar··.@wor··m.net  Bar··.@hot··m.com
v  | \  1-818-985-3259                       Please reply without spam
e    |\ 
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ 
u    |/ Have you solved http://members.aol.com/PanicYr00/Sequence.html
```

###### ↳ ↳ ↳ Re: Should I learn COBOL?

_(reply depth: 5)_

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-12-02T19:00:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p21@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p13@usenetarchives.gap> <gap-8b6a97dba0-p14@usenetarchives.gap> <gap-8b6a97dba0-p19@usenetarchives.gap> <gap-8b6a97dba0-p21@usenetarchives.gap>`

```



RandallBart wrote in article
› Yet I have always felt that if Pascal or C just implemented Cobol
› PICTURE -- not something like it, but the exact syntax and semantics of
…[4 more quoted lines elided]…
› 

The Math. Decimal Math. It's available with BAL/ASM (Whatever you want to
call it) too.

The math, and indexed file structure make COBOL a superior business
language.
```

###### ↳ ↳ ↳ Re: Should I learn COBOL?

_(reply depth: 6)_

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-12-02T19:00:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p23@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p22@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p13@usenetarchives.gap> <gap-8b6a97dba0-p14@usenetarchives.gap> <gap-8b6a97dba0-p19@usenetarchives.gap> <gap-8b6a97dba0-p21@usenetarchives.gap> <gap-8b6a97dba0-p22@usenetarchives.gap>`

```

Thane Hubbell wrote:
› 
› RandallBart  wrote in article 
…[12 more quoted lines elided]…
› language.

*Scaled* decimal math.

Also add *lack* of pointers as a definite plus for easier debugging and
reliability.

And hierarchical data structures.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: Should I learn COBOL?

_(reply depth: 7)_

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1997-12-06T19:00:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p24@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p23@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p13@usenetarchives.gap> <gap-8b6a97dba0-p14@usenetarchives.gap> <gap-8b6a97dba0-p19@usenetarchives.gap> <gap-8b6a97dba0-p21@usenetarchives.gap> <gap-8b6a97dba0-p22@usenetarchives.gap> <gap-8b6a97dba0-p23@usenetarchives.gap>`

```

Judson McClendon wrote:
› 
› Thane Hubbell  wrote:
…[21 more quoted lines elided]…
› And hierarchical data structures.

Let's take Pascal, and add the full functionality of Cobol PIC. Pascal
already has hierarchical data. Pascal does have pointers, but their
much more limited than C pointers, and strong typing makes them a little
harder to abuse. (Any tool can be abused.)

So we add scaled decimal math to Pascal by implementing PIC

Cobol Pascal

01 in-rec. var in-rec : record
05 acct-num pic 9(10). acct-num : pic "9(10)";
05 curr-bal pic 9(7)v99. curr-bal : pic "9(7)v99";
05 int-rate pic p9999. int-rate : pic "p9999";
end;

Note: Quotes are used because I know what PIC strings do to the parser.
I'm not saying the implementation would be easy, but if Pascal had the
full syntax and semantics of Cobol PIC, what would Cobol have going for
it?

And then we must ask: Why has no language done this? Clearly no
language is intending to replace Cobol, until it replaces Cobol data
declarations.
I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
L  |/   
o  |\        Bar··.@wor··m.net  Bar··.@hot··m.com
v  | \  1-818-985-3259                       Please reply without spam
e    |\ 
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ 
u    |/ Have you solved http://members.aol.com/PanicYr00/Sequence.html
```

###### ↳ ↳ ↳ Re: Should I learn COBOL?

_(reply depth: 8)_

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-12-07T19:00:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p25@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p24@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p13@usenetarchives.gap> <gap-8b6a97dba0-p14@usenetarchives.gap> <gap-8b6a97dba0-p19@usenetarchives.gap> <gap-8b6a97dba0-p21@usenetarchives.gap> <gap-8b6a97dba0-p22@usenetarchives.gap> <gap-8b6a97dba0-p23@usenetarchives.gap> <gap-8b6a97dba0-p24@usenetarchives.gap>`

```

RandallBart wrote:
› 
› Let's take Pascal, and add the full functionality of Cobol PIC.  Pascal
…[8 more quoted lines elided]…
› declarations.

Well, PL/I pretty much did. But they also added everything else, including
the sink. And it sunk. And it had float too. Sigh.

Randall, why don't you introduce the language formally? You can call it
PasBOL. Or COkal. Its bound to be a hit.

I agree with you. I can't see businesses embracing any language without
scaled decimal math and powerful data formatting. We will be counting money
and printing business reports, even if ad hoc, for the foreseeable future.
Perhaps inflation will eventually eliminate everything less than a dollar and
mitigate the problem, but hopefully not soon.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: Should I learn COBOL?

_(reply depth: 6)_

- **From:** "cha..." <ua-author-8441878@usenetarchives.gap>
- **Date:** 1997-12-03T19:00:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p26@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p22@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p13@usenetarchives.gap> <gap-8b6a97dba0-p14@usenetarchives.gap> <gap-8b6a97dba0-p19@usenetarchives.gap> <gap-8b6a97dba0-p21@usenetarchives.gap> <gap-8b6a97dba0-p22@usenetarchives.gap>`

```

On 3 Dec 97 16:08:37 GMT, "Thane Hubbell" wrote:

› 
› 
…[14 more quoted lines elided]…
› 
Any file handling would be an improvement in C(++), and memory
allocation, and less opportunity for the applications programmer to
screw up the whole system when his program executes, and a greater
discipline forced on the programmer by the language structure, and not
so much stupid punctuation, and... nuff said.


Charles F Hankel
------------------------------------------------------------------
COBOLs: IBM D, E, F, ANS v4, VS, COBOL 2, LE/370, AIX, S/38, OS/2,
PC/MS-DOS, Honeywell GCOS, Burroughs 7000, Tandem, HP3000
all to varying degrees over the past 25 years or so.
```

###### ↳ ↳ ↳ Re: Should I learn COBOL?

- **From:** "gary drummond" <ua-author-7007584@usenetarchives.gap>
- **Date:** 1997-12-04T19:00:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p27@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b6a97dba0-p14@usenetarchives.gap>`
- **References:** `<346F5BBF.FC7BF0C3@io.com> <gap-8b6a97dba0-p13@usenetarchives.gap> <gap-8b6a97dba0-p14@usenetarchives.gap>`

```

Rich Benack wrote:
› 
› The key question of course is how many NEW COBOL systems are being
…[21 more quoted lines elided]…
›› Volker Bandke
To answer the question at the beginning, yes you should! It would
allow you to finish the development of an application after spending
2 years trying to do it in another language!

Gary
```

#### ↳ Re: Should I learn COBOL?

- **From:** "e=mc^3..." <ua-author-6589663@usenetarchives.gap>
- **Date:** 1997-12-02T19:00:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b6a97dba0-p28@usenetarchives.gap>`
- **In-Reply-To:** `<346F5BBF.FC7BF0C3@io.com>`
- **References:** `<346F5BBF.FC7BF0C3@io.com>`

```

On Sun, 16 Nov 1997 Alan C. Hines asked:

› Over the past few months I've been teaching myself Java ....
 
› After all of this, I must say I have a certain fondness for Java - I
› like its built-in support for multithreading, its huge class libraries,
› totally object-oriented approach, automatic memory management and so
› forth.  Also, I chose Java as my first programming language because of
› the promised career prospects that it offered, ....
 
› After reading about the Y2K bug, however, I wonder whether I shouldn't
› try to cash in by teaching myself Cobol.  I have numerous reservations,
› however: ....

Alan, my man, Java -- and C/C++, and Pascal/Delphi, and ... -- is
for moving poets. COBOL is for moving money. It's your choice.
Rick Anderson
Seattle
anderson aatt pobox fullstop com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
