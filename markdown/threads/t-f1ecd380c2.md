[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What is a level 77

_34 messages · 18 participants · 1998-04_

---

### What is a level 77

- **From:** "mom..." <ua-author-889598@usenetarchives.gap>
- **Date:** 1998-04-02T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca>`

```

Can you help
I have a cobol program that has
77 COUNT PIC 999 Value 0.

What does the level 77 mean?
I checked three textbooks already and none of them have a 77.
I know that 66 is to rename, and what an 88 does, but can someone refresh me
on what a 77 does?

Thanks
```

#### ↳ Re: What is a level 77

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1998-04-01T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca>`

```

Mark OMeara wrote:
› 
› Can you help
…[6 more quoted lines elided]…
› on what a 77 does?

I checked COBOL for Dummies and another textbook I had lying around.
Neither one explained level 77.

Basically, a Level 77 data item is just like an 01 data item, except
that a Level 77 item must always be an elementary data item. It cannot
be subdivided with lower levels.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
"Y2K? Because Centuries Happen!" http://home.att.net/~arnold.trembley/
```

##### ↳ ↳ Re: What is a level 77

- **From:** "ken knowles" <ua-author-17074987@usenetarchives.gap>
- **Date:** 1998-04-07T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p2@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p2@usenetarchives.gap>`

```


Also, level 77 is an obsolete feature. You should use level 01 instead.
```

###### ↳ ↳ ↳ Re: What is a level 77

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-04-07T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p3@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p2@usenetarchives.gap> <gap-f1ecd380c2-p3@usenetarchives.gap>`

```

Ken Knowles wrote in message <01bd62bc$69b95810$63a120cc@cdtdb>...
›
› Also, level 77 is an obsolete feature. You should use level 01 instead.
›

If you mean "obsolete" in the ANSI sense of the term, then
NO,
77-levels, are NOT an obsolete feature in the current Standard or in the
draft of the next Standard.

If you mean "obsolete" in the sense of "old technology that you never need
to use" - then I totally agree.
```

###### ↳ ↳ ↳ Re: What is a level 77

_(reply depth: 4)_

- **From:** "do..." <ua-author-13503504@usenetarchives.gap>
- **Date:** 1998-04-09T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p4@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p2@usenetarchives.gap> <gap-f1ecd380c2-p3@usenetarchives.gap> <gap-f1ecd380c2-p4@usenetarchives.gap>`

```

Agree!

In article <6gfgjh$o.··.@dfw··m.com>, "William M. Klein"
wrote:
› Ken Knowles wrote in message <01bd62bc$69b95810$63a120cc@cdtdb>...
›› 
…[10 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: What is a level 77

_(reply depth: 5)_

- **From:** "colin" <ua-author-29168@usenetarchives.gap>
- **Date:** 1998-04-13T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p5@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p2@usenetarchives.gap> <gap-f1ecd380c2-p3@usenetarchives.gap> <gap-f1ecd380c2-p4@usenetarchives.gap> <gap-f1ecd380c2-p5@usenetarchives.gap>`

```

Tony wrote:

› Agree!
› 
…[14 more quoted lines elided]…
›› 

Disagree. At least in MVS, an 01 (and why aren't you just using the '1'?)
aligns the data on a doubleword boundary; a 77 is byte aligned. Why waste the
storage? (and tomorrow morning I'm going to check that assertion just to see
if I've been in this game far too long -:) ).
apart from declaring a structure, the only other required use of level 1,as
far as I can remember, is for GLOBAL data.
Colin West
```

###### ↳ ↳ ↳ Re: What is a level 77

_(reply depth: 6)_

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-04-13T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p6@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p2@usenetarchives.gap> <gap-f1ecd380c2-p3@usenetarchives.gap> <gap-f1ecd380c2-p4@usenetarchives.gap> <gap-f1ecd380c2-p5@usenetarchives.gap> <gap-f1ecd380c2-p6@usenetarchives.gap>`

```

colin wrote:

›   Disagree. At least in MVS, an 01 (and why aren't you just using the '1'?)
› aligns the data on a doubleword boundary; a 77 is byte aligned. Why waste the
…[4 more quoted lines elided]…
› Colin West


Well, I can't believe I succombed and posted on this thread - but -
Colin? What were your test results?
```

###### ↳ ↳ ↳ Re: What is a level 77

_(reply depth: 7)_

- **From:** "colin" <ua-author-29168@usenetarchives.gap>
- **Date:** 1998-04-14T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p7@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p2@usenetarchives.gap> <gap-f1ecd380c2-p3@usenetarchives.gap> <gap-f1ecd380c2-p4@usenetarchives.gap> <gap-f1ecd380c2-p5@usenetarchives.gap> <gap-f1ecd380c2-p6@usenetarchives.gap> <gap-f1ecd380c2-p7@usenetarchives.gap>`

```

Thane Hubbell wrote:

› colin wrote:
› 
…[9 more quoted lines elided]…
› Colin?  What were your test results?

Alas Thane, i was derailed trying to debug a cobol II to assembler problem, not
of my making I;m happy to add. I will try Wednesday a.m. and let you know.
```

###### ↳ ↳ ↳ Re: What is a level 77

_(reply depth: 7)_

- **From:** "colin" <ua-author-29168@usenetarchives.gap>
- **Date:** 1998-04-14T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p7@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p2@usenetarchives.gap> <gap-f1ecd380c2-p3@usenetarchives.gap> <gap-f1ecd380c2-p4@usenetarchives.gap> <gap-f1ecd380c2-p5@usenetarchives.gap> <gap-f1ecd380c2-p6@usenetarchives.gap> <gap-f1ecd380c2-p7@usenetarchives.gap>`

```

Thane Hubbell wrote:

› colin wrote:
› 
…[9 more quoted lines elided]…
› Colin?  What were your test results?

I'm wrong!! :-( . In truth, the manual (VS Cobol II R4 appl Pgm Lang REf
section 2.7.11) _does_ say that 01 levels are synchronized on a doubleword
boundary yet nary a word on level 77. So, by inspection of a compile, 77's are
similarly aligned. Egads...but I'm sure I once read that 77 was merely byte
aligned. Oh well, serves me right on two counts, appearing to be an idiot and then
responding to this subject and removing all doubt. (thankyou M. Twain).
regards,
Colin
```

###### ↳ ↳ ↳ Re: What is a level 77

_(reply depth: 6)_

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-04-14T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p6@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p2@usenetarchives.gap> <gap-f1ecd380c2-p3@usenetarchives.gap> <gap-f1ecd380c2-p4@usenetarchives.gap> <gap-f1ecd380c2-p5@usenetarchives.gap> <gap-f1ecd380c2-p6@usenetarchives.gap>`

```

colin wrote:

› (and why aren't you just using the '1'?)

It just looks wrong. When I found out that Cobol-74 allows levels 01
thru 09 to be represented in one digit, I started taking advantage of
it. I promptly grew to hate it. It's just wrong. A nicely formatted
listing has a two digit level number in a column which is a multiple of
four, followed by two spaces, followed by a dataname in a column which
is a multiple of four. Along with FD, SD, LD, and (on A Series) DB, the
indicator is always two characters. Anything else just looks sloppy to
my old Cobol eyes.

I  |\   Randall Bart
L  |/   mailto:Bar··.@usa··m.net    Bar··.@wor··m.net
o  |\   1-310-542-6013                       Please reply without spam
v  | \      Todd McCormick released after 12 day illegal incarceration
e    |\ for using Marinol w/ prescription: http://www.freecannabis.org
Y    |/     http://www.marijuanamagazine.com/toc/articles/toddfree.htm
o    |\ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00  
u    |/ Is it easy yet?:http://members.aol.com/PanicYr00/Sequence.html
```

###### ↳ ↳ ↳ Re: What is a level 77

_(reply depth: 7)_

- **From:** "colin" <ua-author-29168@usenetarchives.gap>
- **Date:** 1998-04-16T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p10@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p2@usenetarchives.gap> <gap-f1ecd380c2-p3@usenetarchives.gap> <gap-f1ecd380c2-p4@usenetarchives.gap> <gap-f1ecd380c2-p5@usenetarchives.gap> <gap-f1ecd380c2-p6@usenetarchives.gap> <gap-f1ecd380c2-p10@usenetarchives.gap>`

```
RandallBart wrote:

› colin wrote:
› 
…[19 more quoted lines elided]…
› u    |/ Is it easy yet?:http://members.aol.com/PanicYr

Just as I thoroughly appreciated it. Less eye clutter. In similar vein I
prefer to use mixed case for variable/paragraph/subroutine names and avoid
those ghastly hyphens. I do, however, stick to upper-case only for
variables that represent constant values, a technique much beloved in
C.Colin

RandallBart wrote:
colin wrote:

› (and why aren't you just using the '1'?)

It just looks wrong.  When I found out that Cobol-74 allows levels
01
thru 09 to be represented in one digit, I started taking advantage
of
it.  I promptly grew to hate it.  It's just wrong. 
A nicely formatted
listing has a two digit level number in a column which is a multiple
of
four, followed by two spaces, followed by a dataname in a column which
is a multiple of four.  Along with FD, SD, LD, and (on A Series)
DB, the
indicator is always two characters.  Anything else just looks
sloppy to
my old Cobol eyes.
```

#### ↳ Re: What is a level 77

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-04-02T19:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p12@usenetarchives.gap>`
- **In-Reply-To:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca>`

```

The following post does not have the "ring of truth" to it.

1) There is not now, nor has there ever been any rule requiring that
77-levels must be defined first. There was a "habit" of doing this with
some compilers and as shop standards, but it has never been required.

2) At least the '68 Standard has been perfectly happy doing arithmetic on
any-level items - as long as they were numeric. It is true that the most
efficient arithmetic (with some compilers) was done on 77-levels - but using
the SYNC clause on any elementary item should make that a non-issue too.

I hope this note doesn't sound too much like a "flame" - but the original
post just was not right.
```

##### ↳ ↳ Re: What is a level 77

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-04-03T19:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p12@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p12@usenetarchives.gap>`

```

William M. Klein wrote:
› 
› The following post does not have the "ring of truth" to it.
…[3 more quoted lines elided]…
› some compilers and as shop standards, but it has never been required.

I don't have a manual available, and I've been wrong before, but I am
sure that X3.23-1968 required all 77s to come before any 01s.
› 
› 2) At least the '68 Standard has been perfectly happy doing arithmetic on
› any-level items - as long as they were numeric.  
 
› Definitely.
 
› It is true that the most
› efficient arithmetic (with some compilers) was done on 77-levels - but using
› the SYNC clause on any elementary item should make that a non-issue too.

On Unisys A Series two fields defined identically except that one is
level 01 and one is level 77 may be allocated differently. On some
platforms 01s are alligned differently than 77s. There logically
shouldn't be differences, but for historical reasons there sre.


I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
L  |/   
o  |\        Bar··.@wor··m.net  Bar··.@hot··m.com
v  | \  1-310-542-6013                       Please reply without spam
e    |\ 
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ 33rd term revealed.  Is it easy yet?:
u    |/                 http://members.aol.com/PanicYr00/Sequence.html
```

###### ↳ ↳ ↳ Re: What is a level 77

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1998-04-03T19:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p13@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p12@usenetarchives.gap> <gap-f1ecd380c2-p13@usenetarchives.gap>`

```

RandallBart wrote:
› William M. Klein wrote:
›› 
…[7 more quoted lines elided]…
› sure that X3.23-1968 required all 77s to come before any 01s.


I don't have X3.23-1968, but I cannot find such a restriction in X3.23-1985.
If it's there, please point it out to me. On page VI-18 (and others) Working
Storage is defined as:

WORKING-STORAGE SECTION.
--------------- -------

+-- --+
| |
| 77-level-description-entry |
| | ...
| record-description-entry |
| |
+-- --+

Am I mistaken in thinking that syntax diagram permits selecting either option
repeatedly, in any order?
```

###### ↳ ↳ ↳ Re: What is a level 77

_(reply depth: 4)_

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-04-03T19:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p14@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p12@usenetarchives.gap> <gap-f1ecd380c2-p13@usenetarchives.gap> <gap-f1ecd380c2-p14@usenetarchives.gap>`

```

›    |  77-level-description-entry   |
›    |  record-description-entry     |
…[3 more quoted lines elided]…
› repeatedly, in any order?

Probably not. However, the first three COBOLS I worked on all required
77
level entries to come before any 01 level entries. Those were on the
PDP-10,
in the late 60's, the CYBER-73 in 1970, and the Honeywell H-200 in the
early 70's.

I may be wrong here, but my understanding was that 77 level entries were
designed
for some early machines that could only reference the first few k in
absolute terms. All
other references required pointers, as the instruction allocated less
bits in the opcode
than the address space.

That was why they had to be first. Later on, they were used for
pointers and counters.
The PDP-10, for example, was a 36 bit machine. Level 77 items were
stored as 36
bit words. In 1974, the COMP mechanism was developed to handle non-byte
data ...
I do not remember what happened to 77's, though I sat on that committee,
and we had
most of our meetings at DEC in Marlborough, I was working on Honeywell
equipment
by that time.

I think, in modern classes, I would recomend that everything but
standard byte data be
avoided like the plaque, unless absolutely required to interface to a
second language.
If the time is so critical that one has to use a non-standard usage,
then I prbably would
not write it in COBOL. I am begining to think even files are obsolete
... just read everything
into arrays and deal with it.

I spent my first year of programming attempting to keep 25000 lines of
COBOL within 28K
bytes of object. The 4k upgrade to 32k was $11,800 per month to rent.
Times change.

› Sun Valley Systems acceptance, that Christ Jesus came into the
› jud··.@min··g.com world to save sinners (1 Timothy 1:15)
› (please remove numbers from email id to respond)


If you expect everything you read in a manual to be correct, you are
going to get
into a lot of trouble. Sometimes manuals are just wishfull thinking.
```

###### ↳ ↳ ↳ Re: What is a level 77

_(reply depth: 5)_

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-04-03T19:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p15@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p12@usenetarchives.gap> <gap-f1ecd380c2-p13@usenetarchives.gap> <gap-f1ecd380c2-p14@usenetarchives.gap> <gap-f1ecd380c2-p15@usenetarchives.gap>`

```

Donald Tees wrote:
› 
 
› [snippage]
 
› 
›     I spent my first year of programming attempting to keep 25000 lines of
…[3 more quoted lines elided]…
› 

Oh dear, you've gone and done it... time for me to trot out my Favorite
Story.

It was during my first COBOL class, a night-course taught at NYU. Most
of the folks were already business-types of some sort or another... me,
I worked for a magazine transhipment firm in Hoboken... they wore suits,
I smelled bad. (some things never change)

Anyhow, the instructor, as all instructors do at times, got bored with
going over the structure of the SELECT for the nth time... so he did was
all instructors/teachers/professors do... he told A Story. He started
by saying 'Now this won't be on the exam, you don't have to remember
this, but...' and while everyone else caught forty winks I leaned
forward and listened; my time in Academia taught me that when the person
facing the class said such things Really Interesting Stuff followed.

He started by telling us that programs in Production *never* got
smaller... folks just kept adding bits and pieces. Well, back in the
early '60's, before the S/360 architecture, a bank in New York had just
such a program... in fact it got *so* large that it would not load into
core. Rather than sit down and properly re-write the fool thing they
called in... The Consultant.

The Consultant listened to their tale of woe, flipped through a greenbar
listing and said 'Alright, I can do this... but it'll take me two weeks
and it'll cost you US$5,000 (a bit of change in the early '60's). The
bank-folk cried 'Oh, wond'rous Consultant, the money will be yours...
please, please save us!'

They found him a desk and he immediately assumed the Programmer's
Position... feet up on the desk, cigarette in one hand, cup of coffee in
the other, staring at the ceiling and mapping out memory-locations on
the acoustic tiles. This he did for nine business days.

On the tenth day he went into the program's source; for each and every
SELECT he coded one additional line:

RESERVE NO ALTERNATE AREAS

... and the program compiled and loaded into core.

Ahhh, for the Olden Tymes, when a Consultant could write code such as
ten programmers cannot write now-a-days!.

DD
```

###### ↳ ↳ ↳ Re: What is a level 77

_(reply depth: 6)_

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-04-04T19:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p16@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p12@usenetarchives.gap> <gap-f1ecd380c2-p13@usenetarchives.gap> <gap-f1ecd380c2-p14@usenetarchives.gap> <gap-f1ecd380c2-p15@usenetarchives.gap> <gap-f1ecd380c2-p16@usenetarchives.gap>`

```

› Ahhh, for the Olden Tymes, when a Consultant could write code such as
› ten programmers cannot write now-a-days!.



Yes indeed. I have an entire General Lerdger Program here, still runs
under
DOS, totals 51k ... code, help file, everything. Of that, 45k is empty
tables that
are initialized on startup. Real code is about 4.5 K.

Goes like a bat out of hell on a 64K XT, and requires at least one 360k
floppy.
Written in assembler (2800 hours worth, according to my records), and
doing
nasty things like using base registers as the pointers for sorts.

Today, I would whack out the same system in three days, and use four or
five
megs.

Donald.
```

###### ↳ ↳ ↳ Re: What is a level 77

_(reply depth: 4)_

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-04-03T19:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p14@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p12@usenetarchives.gap> <gap-f1ecd380c2-p13@usenetarchives.gap> <gap-f1ecd380c2-p14@usenetarchives.gap>`

```

Judson McClendon wrote:
› 
› RandallBart wrote:
…[13 more quoted lines elided]…
› Storage is defined as:


I am 99.44% sure of the following: X3.23-1968 required 77s before 01s.
The ordering restriction was relaxed in X3.23-1974. Bill Klein said
"There is not now, nor has there ever been", which you two (Judson and
Bill) seem to use to mean since the 1983 (pink) draft of COBOL.

END-FLAME.
I  |\   Randall Bart, who read the 1981 (blue) draft of Cobol
L  |/   mailto:Bar··.@usa··m.net    Bar··.@wor··m.net
o  |\   1-310-542-6013                       Please reply without spam
v  | \  
e    |\ Todd McCormick jailed for using Marinol with prescription:
Y    |/        http://marijuanamagazine.com/toc/articles/toddheld.html
o    |\ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00  
u    |/ Is it easy yet?:http://members.aol.com/PanicYr00/Sequence.html
```

###### ↳ ↳ ↳ Re: What is a level 77

_(reply depth: 5)_

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1998-04-03T19:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p18@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p12@usenetarchives.gap> <gap-f1ecd380c2-p13@usenetarchives.gap> <gap-f1ecd380c2-p14@usenetarchives.gap> <gap-f1ecd380c2-p18@usenetarchives.gap>`

```

RandallBart wrote in message <6g6835$i.··.@bgt··t.net>...
› Judson McClendon wrote:
›› 
…[20 more quoted lines elided]…
› Bill) seem to use to mean since the 1983 (pink) draft of COBOL.


Not really. I was actually only seeking clarification, not trying to debate the
issue.
```

###### ↳ ↳ ↳ Re: What is a level 77

_(reply depth: 6)_

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-04-03T19:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p19@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p12@usenetarchives.gap> <gap-f1ecd380c2-p13@usenetarchives.gap> <gap-f1ecd380c2-p14@usenetarchives.gap> <gap-f1ecd380c2-p18@usenetarchives.gap> <gap-f1ecd380c2-p19@usenetarchives.gap>`

```

To correct my earlier position, I have verified that the '68 Standard did
require 77-levels to be first. However, not requiring this was identified
as a "substantive change" in the '74 Standard. Therefore, unless you have a
compiler that ONLY supports the '68 Standard, this should not be a problem.

FYI - for IBM mainframers, using LANGLVL(1) with OS/VS COBOL or DOS/VS
COBOL, does *not* mean that you have a '68 compiler - and you can use '74
features such as intermixing 01-levels and 77-levels.
```

###### ↳ ↳ ↳ Re: What is a level 77

_(reply depth: 5)_

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-04-04T19:00:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p18@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p12@usenetarchives.gap> <gap-f1ecd380c2-p13@usenetarchives.gap> <gap-f1ecd380c2-p14@usenetarchives.gap> <gap-f1ecd380c2-p18@usenetarchives.gap>`

```


› I am 99.44% sure of the following:  X3.23-1968 required 77s before 01s.
› The ordering restriction was relaxed in X3.23-1974.  Bill Klein said
› "There is not now, nor has there ever been", which you two (Judson and
› Bill) seem to use to mean since the 1983 (pink) draft of COBOL.
› 
The original purpose of the 77 level was for certain computers that had
less bits
in the opcode than were in the address space. With those computers, the
first
portion of memory was addressable from all memory space. The rest of
memory
was addressable only through a pointer that in turn was addressed with a
relative
address. This was very similar to the 8086 which could only address 64k
without
using an extra register. For that reason, the 77 level was always
placed first.

The computers I used COBOL on in th 60's and early 70's all had that
restriction. They
included the DEC-system10, the CYBER-73, and the Honeywell H200 series.

In 1974, Grace Hopper led the ANSII committee to clean up some of that
stuff. I
attended a few of those sessions in Marlborough, Mass., at the DEC
headquarters. It
was decided that 77 levels would be placed first by the compiler, and
word/byte
alligned. Aside from that, all the other "special" requirements would
be shuffled to
the "usage" area of the compiler.

I have no idea of what actually got written into the specs, but in
modern code, I would
avoid all of that stuff like the plaque. Ninety-nine percent of all
conversion problems
can be traced to code were somebody decided to be fiendishly clever to
save eight
bytes on a thirty-two megabyte computer, or to same a millisecond in a
two hour run.

If( you have to use it to make it work)then (ok), else (never).

Speaking of historical leftovers, can anybody tell me why every COBOL on
the market
still gives me error codes instead of the message? And why the tables
that explain those
codes HAVE to be spread out over seventeen manuals? It would seem that
putting an
manual on a CD, and leaving a 100k table of the most critical part in
the manual is simple
stupidity, but then COBOL has always suffered from the committee
approach to design.
```

###### ↳ ↳ ↳ Re: What is a level 77

_(reply depth: 6)_

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-04-04T19:00:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p21@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p12@usenetarchives.gap> <gap-f1ecd380c2-p13@usenetarchives.gap> <gap-f1ecd380c2-p14@usenetarchives.gap> <gap-f1ecd380c2-p18@usenetarchives.gap> <gap-f1ecd380c2-p21@usenetarchives.gap>`

```


Donald Tees wrote in message <6g85mj$3ub$1.··.@new··s.net>...
› 
›    >much snippage <
…[5 more quoted lines elided]…
›    codes HAVE to be spread out over seventeen manuals?

In the IBM mainframe (and Workstation) COBOLs, you can *only* get the
message - number plus text. with Micro Focus, there is an option to get the
code only, but I believe the default is to get the full message.

What compiler are you working with that still only gives "error codes"? Or
are you talking about at run-time? But even there, most of the
compilers/run-times that I know of NOW give useful (or fairly useful)
messages.
```

###### ↳ ↳ ↳ Re: What is a level 77

_(reply depth: 7)_

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-04-05T20:00:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p23@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p22@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p12@usenetarchives.gap> <gap-f1ecd380c2-p13@usenetarchives.gap> <gap-f1ecd380c2-p14@usenetarchives.gap> <gap-f1ecd380c2-p18@usenetarchives.gap> <gap-f1ecd380c2-p21@usenetarchives.gap> <gap-f1ecd380c2-p22@usenetarchives.gap>`

```



› What compiler are you working with that still only gives "error codes"?  Or
› are you talking about at run-time? But even there, most of the
› compilers/run-times that I know of NOW give useful (or fairly useful)
› messages.


I was speaking of run time, actually. I am using both MF and RM.
```

###### ↳ ↳ ↳ Re: What is a level 77

- **From:** "fbl..." <ua-author-17084102@usenetarchives.gap>
- **Date:** 1998-04-06T20:00:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p24@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p13@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p12@usenetarchives.gap> <gap-f1ecd380c2-p13@usenetarchives.gap>`

```


A Level 77 is a complete waste of compiler. There is no reason to use
a level 77. Some reformed Assembler progammer defined this.
```

#### ↳ Re: What is a level 77

- **From:** "mickey ben-tovim" <ua-author-17074116@usenetarchives.gap>
- **Date:** 1998-04-02T19:00:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p25@usenetarchives.gap>`
- **In-Reply-To:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca>`

```

A 77 level is an elementary item (not a group). It forces alignment on a
double word boundry.

mickey

Mark OMeara wrote:
› 
› Can you help
…[14 more quoted lines elided]…
› Web Site: http://www3.bc.sympatico.ca/soulcare
```

##### ↳ ↳ Re: What is a level 77

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-04-02T19:00:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p26@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p25@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p25@usenetarchives.gap>`

```


Mickey Ben-Tovim wrote in message <352··.@ho··e.com>...
› A 77 level is an elementary item (not a group). It forces alignment on a
› double word boundry.

All "forces on xxx boundary" statements are totally IMPLEMENTOR specific.
The doubleword boundary is true for (older?) IBM mainframe compilers. (I
don't know what the newer ones do with OPT specificed - where they can
"shuffle" around Working-Storage.) Micro Focus has a specific compiler
directive to tell what boundaries are used - and I assume other vendors have
their own rules as well.

› 
› mickey
…[19 more quoted lines elided]…
›› Web Site: http://www3.bc.sympatico.ca/soulcare
```

###### ↳ ↳ ↳ Re: What is a level 77

- **From:** "mickey ben-tovim" <ua-author-17074116@usenetarchives.gap>
- **Date:** 1998-04-02T19:00:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p27@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p26@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p25@usenetarchives.gap> <gap-f1ecd380c2-p26@usenetarchives.gap>`

```

William M. Klein wrote:
› 
› Mickey Ben-Tovim wrote in message <352··.@ho··e.com>...
…[4 more quoted lines elided]…
› The doubleword boundary is true for (older?) IBM mainframe compilers. 

Well, I'm an older IBM programmer??? :-)

mickey
› (I don't know what the newer ones do with OPT specificed - where they can
› "shuffle" around Working-Storage.)  Micro Focus has a specific compiler
…[24 more quoted lines elided]…
››› Web Site: http://www3.bc.sympatico.ca/soulcare
```

##### ↳ ↳ Re: What is a level 77

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1998-04-03T13:06:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p28@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p25@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p25@usenetarchives.gap>`

```



Mickey Ben-Tovim wrote:

› A 77 level is an elementary item (not a group). It forces alignment on a
› double word boundry.

Nope. That is entirely dependent on the implementation (the alignment). The
other reply that it is the same as an elementary 1 is closer to the truth.
```

#### ↳ Re: What is a level 77

- **From:** "jerry gailey" <ua-author-17072805@usenetarchives.gap>
- **Date:** 1998-04-02T19:00:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p29@usenetarchives.gap>`
- **In-Reply-To:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca>`

```

Level 77 - used for noncontiguous elementary data items not a part of a
record. Aligned on a full-word boundary.
```

#### ↳ Re: What is a level 77

- **From:** "joe zitzelberger" <ua-author-8235501@usenetarchives.gap>
- **Date:** 1998-04-02T19:00:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p30@usenetarchives.gap>`
- **In-Reply-To:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca>`

```

› Mark OMeara wrote in message <6g1sbe$e95$2.··.@nnt··c.ca>...
›› Can you help
…[7 more quoted lines elided]…
›› on what a 77 does?

It causes an elementry item to be treated as if it were a '01' level
group...having properties like its own address (instead of an offset in
a group) and allows treatment like a '01' level group....

For the life of me, I can't figure out why people don't just do
elementry '01's.....
```

##### ↳ ↳ Re: What is a level 77

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-04-02T19:00:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p31@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p30@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p30@usenetarchives.gap>`

```

In article <352··.@not··s.com>,
Joe Zitzelberger wrote:
›› Mark OMeara wrote in message <6g1sbe$e95$2.··.@nnt··c.ca>...
››› Can you help
…[14 more quoted lines elided]…
› elementry '01's.....


For reasons of Precious Space... at least when one compiles with IKFCBL00
a series of 77s wastes no space.

DD
```

###### ↳ ↳ ↳ Re: What is a level 77

- **From:** "joe zitzelberger" <ua-author-8235501@usenetarchives.gap>
- **Date:** 1998-04-02T19:00:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p32@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p31@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p30@usenetarchives.gap> <gap-f1ecd380c2-p31@usenetarchives.gap>`

```

doc··.@cl··k.net wrote:
› 
› In article <352··.@not··s.com>,
…[10 more quoted lines elided]…
› a series of 77s wastes no space.

But with IFKCBL00 (IBM OS/VS-Cobol) you will create a seperate BLW cell
for
each level-77 item? If space is tight, why not a single large group
item
with everything in it?
```

##### ↳ ↳ Re: What is a level 77

- **From:** "rene..." <ua-author-6375353@usenetarchives.gap>
- **Date:** 1998-04-04T19:00:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p33@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f1ecd380c2-p30@usenetarchives.gap>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca> <gap-f1ecd380c2-p30@usenetarchives.gap>`

```

All of a sudden, Joe Zitzelberger
wrote:

›› Mark OMeara wrote in message <6g1sbe$e95$2.··.@nnt··c.ca>...
››› Can you help
…[14 more quoted lines elided]…
› elementry '01's.....

Because a 77 does not cause the item to be boundry aligned (usually
double word). Personally, I use the 01, but it was meant to weed out
the "slack bytes"....

Dave


You may e-mail replies to: renegade at (@) dwx dot (.) com
```

#### ↳ Re: What is a level 77

- **From:** "mom..." <ua-author-889598@usenetarchives.gap>
- **Date:** 1998-04-06T20:00:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f1ecd380c2-p34@usenetarchives.gap>`
- **In-Reply-To:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca>`
- **References:** `<6g1sbe$e95$2@nntp.ucs.ubc.ca>`

```

Mark OMeara (mom··.@uni··c.ca) wrote:
: Can you help
: I have a cobol program that has
: 77 COUNT PIC 999 Value 0.

: What does the level 77 mean?
: I checked three textbooks already and none of them have a 77.
: I know that 66 is to rename, and what an 88 does, but can someone refresh me
: on what a 77 does?

: Thanks

Thanks for all the responses to the above question... never thought such
a question would generate so much discussion!

Thanks to all those who filled me in...


-----------------------------------------------------------------
Mark O'Meara | Author of "Here I Am: Finding Oneself
mom··.@uni··c.ca | Through Healing and Letting Go"
Web Site: http://www3.bc.sympatico.ca/soulcare
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
