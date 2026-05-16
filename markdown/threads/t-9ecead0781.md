[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# File Sort

_67 messages · 22 participants · 2000-10 → 2000-11_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### File Sort

- **From:** "The Tickster" <iain@beakplace.demon.co.uk>
- **Date:** 2000-10-28T15:32:11+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk>`

```
Can anyone tell me how to do a sort ascending on a file in Micro Focus
Cobol? This may seem like an easy question but I've only been doing Cobol
for a couple of days. I've tried using SORT Filename ASCENDING key, but the
compiler keeps saying that the operand must be a table.

Any suggestions?

Thanks in advance,

The Tickster.
```

#### ↳ Re: File Sort

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2000-10-28T15:44:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-cglxgit4KBcR@tcpserver>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk>`

```
On Sat, 28 Oct 2000 14:32:11, "The Tickster" 
<iain@beakplace.demon.co.uk> wrote:

> Can anyone tell me how to do a sort ascending on a file in Micro Focus
> Cobol? This may seem like an easy question but I've only been doing Cobol
…[9 more quoted lines elided]…
> 

Take a close look at the syntax for the sort statement.

You need a sort work file (both a select and an SD statement)

You will need a select and an FD for the input file to the sort
and the same for the output file.

sort sort-work-file ascending key xyz using input-file giving 
output-file

Without a sort work file and the input and output files the compiler 
is assuming the sort command is meant to sort a working storage table 
(another handy thing but not what you want)

The sort statement also provides for input and output procedures if 
you want to do additional processing for the data being sorted

sort sort-work-file ascending key xyz
input procedure para-1 thru para-2
output procedure para-3 thru para-4

With input procedures, the "release" verb is used to provide a record 
to the sort

With output procedure the "return" verb is used to obtain the next 
record from the sort in the requested sequence

You can mix "using" with "output procedure" and "giving" with "input 
procedure" if you want.
```

#### ↳ Re: File Sort

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-10-29T00:17:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tfqa6$fr1$1@nnrp1.deja.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk>`

```
In article <972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk>,
  "The Tickster" <iain@beakplace.demon.co.uk> wrote:
> Can anyone tell me how to do a sort ascending on a file in Micro Focus
> Cobol? This may seem like an easy question but I've only been doing
Cobol
> for a couple of days. I've tried using SORT Filename ASCENDING key,
but the
> compiler keeps saying that the operand must be a table.
>
> Any suggestions?

Hi:

Beats me. I wouldn't know where to begin.

If your boss, teacher, mother-in-law is insisting that you do a
sort for whatever reason, and if you don't do it you're up the
creek, fine. Go ahead and learn how to do it.

However, If I were your teacher, I would tell you to write an ISAM
file instead. The advantages are; it's easier, probably just as fast
although execution time is probably irrelevant; you can build in
a couple of extra keys for convenience or whatever; it can be
accessed in various ways, etc. And, you don't need to know how
to sort. In fact, the advantages are so great that I can't imagine
why anyone would do it any other way.

Of course, you might WANT to know how to sort and that is OK, too.
Remember, only 'Real Programmers' sort.

Thanks

Tony Dilworth




Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: File Sort

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-10-29T01:18:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1WKK5.1512$ZX2.68775@iad-read.news.verio.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com>`

```
In article <8tfqa6$fr1$1@nnrp1.deja.com>, Foodman  <foodman123@aol.com> wrote:

[snippage]

>However, If I were your teacher, I would tell you to write an ISAM
>file instead. The advantages are;

... that I know how to write to an ISAM file and I don't know how to code
a SORT.

>it's easier, probably just as fast
>although execution time is probably irrelevant; you can build in
…[3 more quoted lines elided]…
>why anyone would do it any other way.

Can you imagine a program coming back from a Prod Review with a note
saying 'You defined a KSDS, wrote to it, read from it and then deleted
it... in a strict chargeback environment this is an unnecessary use of
disk space, EXCPs and core.  Wasteful programs will not be implemented
into Production; your manager has been informed that you have presented us
with an unacceptable jobstream.'

Of *course* you couldn't imagine that... Prod Review would *never* be that
polite.

DD
```

###### ↳ ↳ ↳ Re: File Sort

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-10-28T22:36:33-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tg2ff0260m@enews3.newsguy.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <1WKK5.1512$ZX2.68775@iad-read.news.verio.net>`

```
I think what Doc was trying to say was...

Do your own homework.

Jeff

----------
In article <1WKK5.1512$ZX2.68775@iad-read.news.verio.net>,
docdwarf@clark.net (  NA) wrote:


> In article <8tfqa6$fr1$1@nnrp1.deja.com>, Foodman  <foodman123@aol.com> wrote:
>
…[25 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 4)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-10-29T13:32:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KFVK5.1577$ZX2.71208@iad-read.news.verio.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <1WKK5.1512$ZX2.68775@iad-read.news.verio.net> <8tg2ff0260m@enews3.newsguy.com>`

```
In article <8tg2ff0260m@enews3.newsguy.com>,
Jeff Baynard <union27@macconnect.com> wrote:
>I think what Doc was trying to say was...
>
>Do your own homework.

No, Mr Baynard, and I apologise for being so obscure; what I was
attempting to point out was that things in Other Places are *not* the same
as they are - and therefore might not benefit from suggestions generated -
- in the Dillworth Anomaly.

DD

>----------
>In article <1WKK5.1512$ZX2.68775@iad-read.news.verio.net>,
…[30 more quoted lines elided]…
>> DD
```

###### ↳ ↳ ↳ Re: File Sort

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-10-29T00:53:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tgdrl$ob6$1@slb3.atl.mindspring.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <1WKK5.1512$ZX2.68775@iad-read.news.verio.net>`

```
Just a "world view" comment.

The "use  ISAM instead of SORT" suggestion came from someone who used the
term "ISAM" to mean (I think) a COBOL "indexed file".

The response about "Prod Review" (which I assume means "production review")
uses terms like KSDS and EXCP.

From my view, this means (even if I didn't know the two posters from
previous posts) that one person runs in a PC (or "possibly" Unix/Linux)
environment while the other runs in an IBM mainframe environment.

Again, even if I didn't know the two posters, I would GUESS that the PC
person has never (or at least not in his/her current environment)
experienced a "production review" system and CERTAINLY has never experienced
a "user EXCP chargeback" system. On the other hand, the person mentioning
KSDS PROBABLY has never run a "production" system in an environment where
the person/application running the production program "owns" (completely -
and without sharing) the entire CPU and resources where the application
runs.

What this says to me is that what is appropriate for a program (much less a
programmer or an entire application) depends upon the "environment" where it
will be run (as well as the expected "development" and "maintenance"
environment).

Another way to look at this is that the "end user" pays for what they
want/expect.  The "programmer" should develop accordingly (which certainly
in a case like this - where the person said that they wanted to LEARN about
something) is to use the facility that they are trying to learn.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 4)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-10-29T13:47:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TTVK5.1580$ZX2.70851@iad-read.news.verio.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <1WKK5.1512$ZX2.68775@iad-read.news.verio.net> <8tgdrl$ob6$1@slb3.atl.mindspring.net>`

```
In article <8tgdrl$ob6$1@slb3.atl.mindspring.net>,
William M. Klein <wmklein@nospam.ix.netcom.com> wrote:
>Just a "world view" comment.

[snippage of *exquisite* diplomacy]

>What this says to me is that what is appropriate for a program (much less a
>programmer or an entire application) depends upon the "environment" where it
>will be run (as well as the expected "development" and "maintenance"
>environment).

Mr Klein... so close!  Given the task at hand (arranging the records of a
file in a given sequence), the two solutions offered (a SORT, internal or
external or a forcing of record sequence via an indexed file) and my
experience (small as it may be) that no mainframe shop in which I have
ever spent time has allowed this task (arranging the records) to be
accomplished by the latter method (sequencing via indexed file)...

... then it might be concluded that a SORT, either internal or external,
is 'appropriate' to *both* environments while the file-forcing method is
apropriate to one.  The question then changes from 'Why use method A
instead of method B?' to 'Why use a method restricted to one environment
when another method may be used in all?'

DD
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-10-29T17:51:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<csZK5.4218$_N4.630125@dfiatx1-snr1.gtei.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <1WKK5.1512$ZX2.68775@iad-read.news.verio.net> <8tgdrl$ob6$1@slb3.atl.mindspring.net> <TTVK5.1580$ZX2.70851@iad-read.news.verio.net>`

```
NA <docdwarf@clark.net> wrote in message
news:TTVK5.1580$ZX2.70851@iad-read.news.verio.net...
>
> ... then it might be concluded that a SORT, either internal or external,
…[4 more quoted lines elided]…
>

OK, I'll bite:

1. It's appropriate to use Method A when portability is not an issue.
2. It's appropriate to use Method A when in performance is an issue and in
the specific environment Method A offers better performance.
3, It's appropriate to use Method A when cost is an issue and in the
specific environment Method A offers an economic benefit.

It's not the paintbrush, it's the artist.

MCM
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-10-30T07:49:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39FD2823.59FE4EE9@Azonic.co.nz>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <1WKK5.1512$ZX2.68775@iad-read.news.verio.net> <8tgdrl$ob6$1@slb3.atl.mindspring.net> <TTVK5.1580$ZX2.70851@iad-read.news.verio.net>`

```
NA wrote:
> [snippage of *exquisite* diplomacy]
> 
…[16 more quoted lines elided]…
> when another method may be used in all?'

In one system that I develop that runs in a PC environment I changed all
the SORT verbs to writing and reading indexed files.  Because the ISAM
(EXTFH) module was already in use and the SORT module and buffers made
additional demands on the memory resourses the SORT verbs were
occationally failing and so the use of an indexed sequencing method was
both faster and more reliable.

I would also hazard that for PC based systems a design that avoids SORTs
by having the data already sequenced through the use of alternate keys
may be more appropriate for interactive systems.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-10-29T15:12:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ti0d0$qca$1@news.igs.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <1WKK5.1512$ZX2.68775@iad-read.news.verio.net> <8tgdrl$ob6$1@slb3.atl.mindspring.net> <TTVK5.1580$ZX2.70851@iad-read.news.verio.net> <39FD2823.59FE4EE9@Azonic.co.nz>`

```

Richard Plinston wrote in message <39FD2823.59FE4EE9@Azonic.co.nz>...
>NA wrote:
>> [snippage of *exquisite* diplomacy]
>>
>> >What this says to me is that what is appropriate for a program (much
less a
>> >programmer or an entire application) depends upon the "environment"
where it
>> >will be run (as well as the expected "development" and "maintenance"
>> >environment).
…[23 more quoted lines elided]…
>may be more appropriate for interactive systems.

Yes, I found that was true when I first started porting Cobol over to
micros's fifteen, twenty years back.  Nowadays, of course, I'd just
encapsulate
it in an object and worry about it later.<G>.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-10-30T07:51:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39FD8B04.BE897DAD@brazee.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <1WKK5.1512$ZX2.68775@iad-read.news.verio.net> <8tgdrl$ob6$1@slb3.atl.mindspring.net> <TTVK5.1580$ZX2.70851@iad-read.news.verio.net>`

```
NA wrote:

> Mr Klein... so close!  Given the task at hand (arranging the records of a
> file in a given sequence), the two solutions offered (a SORT, internal or
…[3 more quoted lines elided]…
> accomplished by the latter method (sequencing via indexed file)...

I was aware of a shop in the late 70's which used ISAM files because it never
bought a SORT utility.  When they got around to buying one, they freed up lots of
resources.
```

##### ↳ ↳ Re: File Sort

- **From:** "Cliff Peterson" <cliffpeterson@spamcop.net>
- **Date:** 2000-10-29T10:40:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D8TK5.13840$xJ4.552503@bgtnsc06-news.ops.worldnet.att.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com>`

```
"Foodman" <foodman123@aol.com> wrote in message
news:8tfqa6$fr1$1@nnrp1.deja.com...
> In article <972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk>,
>   "The Tickster" <iain@beakplace.demon.co.uk> wrote:
…[6 more quoted lines elided]…
> Remember, only 'Real Programmers' sort.

I'm totally and completely speechless.  As my grandmother used to say, "dear
God in heaven!".

Tickster, you WANT to know how to sort.  It's hard to be a programmer if you
don't know the language, and SORT is fundamental.
```

##### ↳ ↳ Re: File Sort

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2000-10-29T13:35:12+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com>`

```
On Sun, 29 Oct 2000 00:17:14 GMT Foodman <foodman123@aol.com> wrote:

:>In article <972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk>,
:>  "The Tickster" <iain@beakplace.demon.co.uk> wrote:

:>> Can anyone tell me how to do a sort ascending on a file in Micro Focus
:>> Cobol? This may seem like an easy question but I've only been doing
:>Cobol
:>> for a couple of days. I've tried using SORT Filename ASCENDING key,
:>but the
:>> compiler keeps saying that the operand must be a table.

:>> Any suggestions?

:>Beats me. I wouldn't know where to begin.

:>If your boss, teacher, mother-in-law is insisting that you do a
:>sort for whatever reason, and if you don't do it you're up the
:>creek, fine. Go ahead and learn how to do it.

:>However, If I were your teacher, I would tell you to write an ISAM
:>file instead. The advantages are; it's easier, 

Writing a ISAM file is easier than using the SORT verb???

:>                                               probably just as fast

I dread to think of a platform where the implementation of SORT requires even
10% of the time required to use ISAM.

:>although execution time is probably irrelevant; you can build in
:>a couple of extra keys for convenience or whatever; it can be
:>accessed in various ways, etc. And, you don't need to know how
:>to sort. 

One does not need to know how to sort in order to use the SORT verb.

:>         In fact, the advantages are so great that I can't imagine
:>why anyone would do it any other way.

There are no advantages to using a ISAM file approach.

Zero.

:>Of course, you might WANT to know how to sort and that is OK, too.
:>Remember, only 'Real Programmers' sort.

COBOL does support a SORT verb which does not require the programmer to know
anything about sorting, just like using the COMPUTE verb does not require the
programmer to be able to add, subtract, multiple, divide, exponentiate, etc.
```

###### ↳ ↳ ↳ Re: File Sort

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-10-30T08:01:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39FD2AED.5126FFEB@Azonic.co.nz>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com>`

```
Binyamin Dissen wrote:

> :>However, If I were your teacher, I would tell you to write an ISAM
> :>file instead. The advantages are; it's easier,
…[6 more quoted lines elided]…
> 10% of the time required to use ISAM.

'Using an ISAM file' may take zero time when the required sorted
sequence is already in one of the alternate keys.  While batch based
systems on mainframes may 'optimise' their file usage by collecting data
in sequential files and then sorting to produce batch reports (just like
I did a few decades ago with packs of cards and tape drives),
interactive systems on PCs tend to be immediate where, for example, a
customer enquirey may lead to the user wanting a list of that customers
orders, transactions, back orders, and other relevant items _without_
waiting for a sort.  The system design for PCs tends (or should tend) to
be quite different from mainframe systems, something that some mainframe
only programmers seem to not know.

 
> There are no advantages to using a ISAM file approach.
> 
> Zero.
> 

I would accept that there are none that you know of.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-10-29T13:17:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tht0j$qrs$1@slb6.atl.mindspring.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz>`

```
ACTUALLY - for both the mainframe and the PC programmer, my guess is that
the use of a "relational database" (or even a hierarchical one) would
probably be better for files where there is a need to access the data via
"multiple" sort sequences.  Furthermore, there may well be additional
built-in "security and recovery" features in such products that are SO
important to many "interactive" applications.

A VSAM (IBM mainframe) or ISAM (everywhere else) file with (multiple)
alternate keys may well be sufficient for some/many applications.  On the
other hand, if you have a "single program" that requires a file in a
specific order (that no other part of the application requires) it may WELL
be a better use of resources to use an INTERNAL sort than to create a
"temporary" ISAM/VSAM file - which is not kept after this single program
"runs". Furthermore, adding an alternate key MAY (in some systems) actually
slow down all the other applications using that file - that don't need that
specific sort sequence.

Bottom-line: (diplomacy again <G>)
  I would CERTAINLY hope that any COBOL programmer know how to use the
internal SORT feature of COBOL *and* how to create and read indexed files.
When to use which is NOT (IMHO) a "cut-and-dried" question - but is one
based on the application and expected environment.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 4)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2000-10-30T00:03:21+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz>`

```
On Mon, 30 Oct 2000 08:01:49 +0000 Richard Plinston <riplin@Azonic.co.nz>
wrote:

:>Binyamin Dissen wrote:

:>> :>However, If I were your teacher, I would tell you to write an ISAM
:>> :>file instead. The advantages are; it's easier,
 
:>> Writing a ISAM file is easier than using the SORT verb???
 
:>> :>                                               probably just as fast
 
:>> I dread to think of a platform where the implementation of SORT requires even
:>> 10% of the time required to use ISAM.

:>'Using an ISAM file' may take zero time when the required sorted
:>sequence is already in one of the alternate keys.  

If the file is already sorted, then there is no need to sort it.

:>                                                   While batch based
:>systems on mainframes may 'optimise' their file usage by collecting data
:>in sequential files and then sorting to produce batch reports (just like
:>I did a few decades ago with packs of cards and tape drives),
:>interactive systems on PCs tend to be immediate where, for example, a
:>customer enquirey may lead to the user wanting a list of that customers
:>orders, transactions, back orders, and other relevant items _without_
:>waiting for a sort.  

Anyone who designs such an online system where any frequent (or even not so
frequent) request requires a sort has really screwed up.

:>                     The system design for PCs tends (or should tend) to
:>be quite different from mainframe systems, something that some mainframe
:>only programmers seem to not know.

News flash - much data on mainframes is accessed on line. And with much higher
volumes that PC based programmers can even dream of.

And DBAs work hard to design keys in relational systems so that their
customers can get the data quickly.

In the PC environment, does one load a ISAM file without taking an initial
step (whether internal or external) of sorting on the primary key?

:>> There are no advantages to using a ISAM file approach.
 
:>> Zero.

:>I would accept that there are none that you know of.

For sorting data? 

Show one.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-10-30T20:21:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39FDD846.FD8B922B@Azonic.co.nz>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com>`

```
Binyamin Dissen wrote:
> 
> In the PC environment, does one load a ISAM file without taking an initial
> step (whether internal or external) of sorting on the primary key?

Well, I never bother.  For a start these are usually one-offs and
'optimising' the process is a usually a waste of programmer time. 
Secondly, where I have in the past made such comparisons, there is no
advantage to having sorted data - the ISAM structures are maintained as
a balanced tree and the best loading sequence _may_ be given by having
the data in a binary chop sequence.  Random data may emulate this well
enough, it reduces index rotations that would be _maximised_ by sorted
data.

Usually the files that I need to load have alternate keys and any
theoretical gain or loss on one key may be compensated for in other
keys.

Now, a few decades ago I had to worry about loading sequence and we even
used to plan out the disk tracks based on the data expected.  Much of
the DP world has moved on since then, I certainly have.

> :>> There are no advantages to using a ISAM file approach.
> :>> Zero.
> 
> :>I would accept that there are none that you know of.

> For sorting data?

You now seem to have an additional qualification.

> Show one.

Gee, I thought that I already had, go back and read my message where a
DOS system resulted in more reliable and faster sorting by using an
indexed file becasue the SORT module was choked by lack of memory.

The point is that one should not approach a problem, any problem, with
pre-conceived ideas about what the solution should be.  Certainly there
are needs for SORT verbs, in some cases this may be the best solution,
but in other cases it may be better to eliminate SORTs or use an indexed
file.
```

###### ↳ ↳ ↳ Deisng patterns

_(reply depth: 6)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-10-30T20:31:59+11:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39FD400F.561D5825@zip.com.au>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz>`

```
Richard Plinston wrote:

> The point is that one should not approach a problem, any problem, with
> pre-conceived ideas about what the solution should be.  Certainly there
> are needs for SORT verbs, in some cases this may be the best solution,
> but in other cases it may be better to eliminate SORTs or use an indexed
> file.

Now this I kind of disagree with.   We always go in with preconceived ideas on
how to do things.  We use prior art or previous solutions to work out the fast
way to apply to this solution.   This is what design patterns are all about.

These preconceived ideas are called experience.  Experience also teaches us to
distrust our own judgment a little and find other solutions or listen to other
ideas that come up.   (Well most of us do....)

Ken
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 6)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2000-10-30T13:42:21+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ublqvso3afpuueh41idll676g3h9h0g9vk@4ax.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz>`

```
On Mon, 30 Oct 2000 20:21:26 +0000 Richard Plinston <riplin@Azonic.co.nz>
wrote:

:>Binyamin Dissen wrote:
 
:>> In the PC environment, does one load a ISAM file without taking an initial
:>> step (whether internal or external) of sorting on the primary key?

:>Well, I never bother.  For a start these are usually one-offs and
:>'optimising' the process is a usually a waste of programmer time. 

Depends on the volume of data and the number of times it happens.

If your experience with PC's is limited to 1000 record files it pretty much
doesn't matter how you do it - hell, you could probably do it in interpreted
basic.

:>Secondly, where I have in the past made such comparisons, there is no
:>advantage to having sorted data - the ISAM structures are maintained as
:>a balanced tree and the best loading sequence _may_ be given by having
:>the data in a binary chop sequence.  Random data may emulate this well
:>enough, it reduces index rotations that would be _maximised_ by sorted
:>data.

Perhaps your ISAM implementation does not support a LOAD mode?

As a side point, are you claiming that your ISAM implementation tries to
dynamically maintain a balanced tree? Sounds good for a file which is mostly
accessed in input mode. You will pay the price if you have significant update
activity against the file.

:>Usually the files that I need to load have alternate keys and any
:>theoretical gain or loss on one key may be compensated for in other
:>keys.

What kind of volume are you referring to?

:>Now, a few decades ago I had to worry about loading sequence and we even
:>used to plan out the disk tracks based on the data expected.  Much of
:>the DP world has moved on since then, I certainly have.

What kind of volume are you referring to?

:>> :>> There are no advantages to using a ISAM file approach.
:>> :>> Zero.
 
:>> :>I would accept that there are none that you know of.

:>> For sorting data?

:>You now seem to have an additional qualification.

Refer to the Subject: File Sort

:>> Show one.

:>Gee, I thought that I already had, go back and read my message where a
:>DOS system resulted in more reliable and faster sorting by using an
:>indexed file becasue the SORT module was choked by lack of memory.

Sounds like a bad sort implementation.

If one does has a bad sort implementation and a great ISAM implementation I
could see your argument.

:>The point is that one should not approach a problem, any problem, with
:>pre-conceived ideas about what the solution should be.  Certainly there
:>are needs for SORT verbs, in some cases this may be the best solution,
:>but in other cases it may be better to eliminate SORTs or use an indexed
:>file.

Not if the object is to sort a file. 

If one wants to build a database, that is a different story.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 7)_

- **From:** riplin@kcbbs.gen.nz
- **Date:** 2000-11-01T19:17:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tpq8h$db5$1@nnrp1.deja.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz> <ublqvso3afpuueh41idll676g3h9h0g9vk@4ax.com>`

```


  Binyamin Dissen  wrote:

> :>> In the PC environment, does one load a ISAM
file without taking an initial
> :>> step (whether internal or external) of sorting
on the primary key?
>
> :>Well, I never bother.  For a start these are
usually one-offs and
> :>'optimising' the process is a usually a waste of
programmer time.
>
> Depends on the volume of data and the number of
times it happens.

An ISAM file is 'loaded' when a new system starts
running and there is existing data from an older
system or some other source. It is a one-off
(usually), once loaded it is added to and updated by
system procedures.  Do you have to do 'loads' on a
regular basis ?  Why is that ?

> If your experience with PC's is limited to 1000
record files it pretty much
> doesn't matter how you do it -

I have clients with tens and hundreds of megabytes of
data.  Their data do not need to be 'loaded' into
ISAM files though this was done some years ago when
their current systems started.

> hell, you could probably do it in interpreted
> basic.

Except that 'interpreted basic' does not have access
to the Cobol ISAM files.  Certainly though the speed
of execution of the code (ie being interpreted) would
have an almost zero effect on a file 'load'.

> :>Secondly, where I have in the past made such
comparisons, there is no
> :>advantage to having sorted data - the ISAM
structures are maintained as
> :>a balanced tree and the best loading sequence
_may_ be given by having
> :>the data in a binary chop sequence.  Random data
may emulate this well
> :>enough, it reduces index rotations that would be
_maximised_ by sorted
> :>data.
>
> Perhaps your ISAM implementation does not support a
LOAD mode?

Exactly right.  There is no need for one.  There is,
however, a REBUILD utility that can recreate an index
file from an existing ISAM data file.  Different ISAM
implementations have different utility functions and
different performance characteristics.

> As a side point, are you claiming that your ISAM
implementation tries to
> dynamically maintain a balanced tree? Sounds good
for a file which is mostly
> accessed in input mode. You will pay the price if
you have significant update
> activity against the file.

Actually, there is always a trade off between update
activity and access.  Loading an ISAM file with data
sorted on the primary key where the index is a b-tree
(multi-way binary tree) will tend to produce a
single, simple linked list down through the 'greater
than' branches.  This would result in a serial search
for every read if the index blocks were not rotated
to balance the tree.

How does your ISAM structure work ?  How does it
avoid degrading into a simple linked list when
presented with sorted data ?  Are you sure that
sorting the data actually helps or was this just an
assumption that you made years ago and never updated
or checked ?

Yes, keeping the tree balanced benefits the accessing
while giving an overhead to record inserts and adds
(to the end). There is _no_ overhead on record
'updates' (except when a key value is changed).  If,
however, the inserts are relatively random then no
additional rotations are required because the tree
will be added to evenly and this will not result in
an unbalance.  Adding to the end of a file (as in
loading sorted data) maximises the need to rotate to
maintain balance.

Maintaining the best access time at some expense of
insert is mostly a good trade-off as on any
reasonable system there will be several read accesses
for every insert.

Perhaps you could describe your systems and why
optimising for read access is not worthwhile.

> :>Usually the files that I need to load have
alternate keys and any
> :>theoretical gain or loss on one key may be
compensated for in other
> :>keys.
>
> What kind of volume are you referring to?

Several megabytes.  But what has the volume to do
with it ?  If two or more indexes exist the the data
cannot be in the best sequence for both or all.
Making one index build in the 'best' way (which is
unlikely to be ordered) may well be the worst way for
the other.

>
> :>Now, a few decades ago I had to worry about
loading sequence and we even
> :>used to plan out the disk tracks based on the
data expected.  Much of
> :>the DP world has moved on since then, I certainly
have.
>
> What kind of volume are you referring to?
>
> :>> :>> There are no advantages to using a ISAM
file approach.
> :>> :>> Zero.
>
> :>> :>I would accept that there are none that you
know of.
>
> :>> For sorting data?
…[3 more quoted lines elided]…
> Refer to the Subject: File Sort

Actually your direct response was to a message saying
that a reasonable system design option may have put
the data into the correct sequence by using an
alternate key thus making the SORT entirely
unnecessary.

> :>Gee, I thought that I already had, go back and
read my message where a
> :>DOS system resulted in more reliable and faster
sorting by using an
> :>indexed file becasue the SORT module was choked
by lack of memory.
>
> Sounds like a bad sort implementation.

No.  Just a lack of infinite resources.  The SORT has
to load a code module and work in whatever memory is
available.  With small memory the prestring phase can
only write small strings resulting in a large number
of merge ways, if these exceed the ability of a
memory pool it has to resort the multiple merge
passes.

> If one does has a bad sort implementation and a
great ISAM implementation I
> could see your argument.

I am not sure that you could.


> :>The point is that one should not approach a
problem, any problem, with
> :>pre-conceived ideas about what the solution
should be.  Certainly there
> :>are needs for SORT verbs, in some cases this may
be the best solution,
> :>but in other cases it may be better to eliminate
SORTs or use an indexed
> :>file.

> Not if the object is to sort a file.

You really need to expand you viewpoint beyond
preconceived ideas.  Actually, the object is _never_
to 'sort a file', the object is to have data in a
particular sequence.  One possible, crude solution is
to 'sort a file'.

Back when the mainframe that I used had 16Kwords of
memory, 4 tape decks and a pair of 4Megabyte drives
the solution often was 'sort a tape file'. For many
of us, even those on PCs, we can learn to apply
different, better design strategies.



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-11-01T14:16:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tptnh$gcs$1@nntp9.atl.mindspring.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz> <ublqvso3afpuueh41idll676g3h9h0g9vk@4ax.com> <8tpq8h$db5$1@nnrp1.deja.com>`

```
I really think that this entire thread has gotten to the point that no one
knows what we are talking about.

The *original* note was a note asking HOW to do a single file sort in COBOL.
This gave no idea of the reason WHY the file was to be sorted - but my
impression was that the person asking wanted to know how to use the COBOL
SORT verb.  That is a reasonable question (for a NEW/student programmer) and
there were some replies that answered this - with the information that
(IMHO) the person wanted.

Another response that was given mentioned reading the "input file" and
creating an ISAM (COBOL indexed - not MVS ISAM) file as output (possibly
then "reading" it sequentially).  Although that is a "valid" technique, I
did not think that it answered what the original person was asking.
HOWEVER, once it was explained that this was a technique that would provide
an "output file" (copy of the original unsorted file) in a method that many
programs/applications could "retrieve" data in a sorted method, that did
seem relevant to the discussion - but not truly responsive to the original
question.

OK - now we get into continuous usage of the sorted file versus load and
batch versus online questions.  The following are some "general" guidelines
that I can think of - and ALL of them are subject to "modification"
depending upon your compiler, operating system, and specific
application/shop needs.

1) When "loading" an indexed file, I believe that it is always "more
efficient" to do so from an already sorted input file.  HOWEVER, how much
this "efficiency" buys you may vary - and whether it leaves the output
indexed file as "more efficient" depends on the operating system and
environment. (Possibly, you should run a "reorg" or "rebuild" after your
initial "random load" of the indexed file.)

2) There are some systems (such as IBM mainframes) where "indexed files" and
"sort-utilities" have NOTHING to do with COBOL.  (The indexed file system is
available to ALL programming languages - and applications can "happily"
share files with no overhead at compile-time or run-time).  Whether you do a
"load" via a utility or COBOL program - may well depend upon how your
"system" handles such things and what tools are available.

3) It is ABSOLUTELY true that no "online" system wants to sort and resort
the same file over and over.  (This is true on mainframes, PCs, wherever -
as far as I know).  Therefore, if you have a file that you want to access
"randomly" and in a "sorted manner" in "real-time" you are almost certainly
going to want an indexed file - rather than an internal COBOL sort.
(However, the chances are that a "database" - possibly relational - will
probably be better yet.  This too will depend upon your environment and
resources available - and how many different "sort sequences" you need to
access the file thru.)

4) If you have a sequential file (as "input") and you have a single program
in your application that needs a "specific" sort of that file (and the
output is never useful for any other part of your application or system)
then considering an "internal sort" (or an external sort utility) seems a
reasonable OPTION to consider.  For example, having an INTERNAL sort with a
sequential file in a USING phrase and an output procedure with Report
Writer - would be a "single use" environment where converting the file to an
indexed file would almost certainly be "over-kill".

5) As a follow-up to the preceding issue - it is often (usually?) true that
if you have one program in your application that wants a file in a specific
"sequence" that chance are EVENTUALLY some other part of the system will
want it that way too.  Therefore, having a separate "step" to convert it to
an indexed file may become advisable eventually - and you may want to build
this in initially.

6) If your input is ALREADY an "indexed file" and you have a program that
needs to read it in a sequential order that is NOT the primary key, then you
have a few options - and which you select should ALSO depend upon your
environment:
 - Add a new alternate key (may have run-time overhead for ALL
applications - Will this overhead be "acceptable" to the other programs in
the application?)
 - Sort the indexed file via an internal sort (or sort utility) and produce
a "one-time" sequential file as output.  (certainly this would NOT be the
option that you select if you end up wanting this new order in an online
environment or for many different programs)
 - Create a second indexed file with this new sort order as the primary key.
(This might be useful if you performance sensitive applications that need
THIS order. However, you would then need to insure that the two files were
kept "in sync" which might include unacceptable overhead.)

7) I have seen NOTHING in this entire thread that has convinced me that
there is ever a "good reason" to create an indexed file from a sequential
input file - if the new "sorted" output is never used by any other program
or part of the application - and their are the resources to "run" an
internal sort.  If you really do have an environment that provides you with
a COBOL facility to create (load from random input) an indexed file that
will not be kept after the program has been run in a significantly more
efficient manner than running an internal sort on an indexed file, then I
think you should be looking at getting a better COBOL environment.

8) I have seen NOTHING in this entire thread that has convinced me that
there is ever a good reason to use a COBOL internal SORT on a file that is
used "interactively" (performance sensitive) with multiple updates and needs
to be "kept" in sequence - when creating (once and only once) and
maintaining it as an indexed file is a "valid" option.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 9)_

- **From:** riplin@kcbbs.gen.nz
- **Date:** 2000-11-02T04:11:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tqphr$8lt$1@nnrp1.deja.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz> <ublqvso3afpuueh41idll676g3h9h0g9vk@4ax.com> <8tpq8h$db5$1@nnrp1.deja.com> <8tptnh$gcs$1@nntp9.atl.mindspring.net>`

```


  "William M. Klein"  wrote:
>
> 1) When "loading" an indexed file, I believe that
it is always "more
> efficient" to do so from an already sorted input
file.  HOWEVER, how much
> this "efficiency" buys you may vary - and whether
it leaves the output
> indexed file as "more efficient" depends on the
operating system and
> environment. (Possibly, you should run a "reorg" or
"rebuild" after your
> initial "random load" of the indexed file.)

Does your 'always "more efficient"' include the reorg
or rebuild times ?

As I have already explained, with a balanced b-tree
system the pre-ordered data guarantees the maximum
number of index rotations are required.  This is the
most inefficient for these systems (including MF).
Random sequence of input is better.

With one system that I used briefly (RM Cobol on
CP/M) the system did not rotate indexes and
preordered data resulted in the index being a simple
linked list of 'greater' pointers.  This got
progressively slower as the load continued and later
data access was just a serial search.

Sorting the input data to random sequence resulted in
a _much_ faster load and reasonable access times.

You should be much more careful with your "always".

Perhaps you could explain the underlying mechanisms
of the indexed file systems that you have used and
explain what factors lead you to your belief of an
ordered load being more efficient.  This would be
useful so that others can know when to sort input
data and when not to, or what order to sort it into.

Also what effect does having alternate keys have when
these must be put out of sequence by a sort to
primary key order.


> 7) I have seen NOTHING in this entire thread that
has convinced me that
> there is ever a "good reason" to create an indexed
file from a sequential
> input file - if the new "sorted" output is never
used by any other program
> or part of the application - and their are the
resources to "run" an
> internal sort.

What about the example of the summary data where the
ISAM file is created with only the summary records
with matches adding.  This reduces the i/o of having
to write the whole file out and then read back the
whole file into the report ?

> If you really do have an environment that provides
you with
> a COBOL facility to create (load from random input)
an indexed file that
> will not be kept after the program has been run in
a significantly more
> efficient manner than running an internal sort on
an indexed file, then I
> think you should be looking at getting a better
COBOL environment.

There may be other factors that you haven't taken
into account in this rather sweeping generalisation.
For example in many cases it was not claimed that the
ISAM file was being especially created but was
suggesting the use of an appropriate alternate key on
an existing ISAM file that provided the correct
sequence without any creation or sorting, without the
file being discarded.  You do have alternate keys in
your Cobol system don't you ?




Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-11-01T23:36:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tqufs$hc1$1@nntp9.atl.mindspring.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz> <ublqvso3afpuueh41idll676g3h9h0g9vk@4ax.com> <8tpq8h$db5$1@nnrp1.deja.com> <8tptnh$gcs$1@nntp9.atl.mindspring.net> <8tqphr$8lt$1@nnrp1.deja.com>`

```
> > 7) I have seen NOTHING in this entire thread that
> has convinced me that
…[12 more quoted lines elided]…
> whole file into the report ?

Sounds like an OUTPUT procedure to me.  I would certainly NEVER do an
internal SORT with both USING/GIVING and then re-open the output file and
read it sequentially - that is EXACTLY what an OUTPUT procedure is all about

>
> > If you really do have an environment that provides
…[19 more quoted lines elided]…
>

Sorry, if I wasn't clear on my talking about cases where an existing indexed
file already existed.  I did talk about cases where you need to "add" a new
alternate key.  In the case where an alternate key already exists and there
is a need to process that file in the order of the alternate key - I would
certainly NOT expect to use a SORT.

However, I do repeat that in cases where such an alternate key does NOT
already exist - there are some issues (mentioned in my original note) with
creating a new alternate key versus using a SORT statement to create either
new sequential or ISAM file.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 11)_

- **From:** riplin@kcbbs.gen.nz
- **Date:** 2000-11-02T20:41:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tsjib$oad$1@nnrp1.deja.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz> <ublqvso3afpuueh41idll676g3h9h0g9vk@4ax.com> <8tpq8h$db5$1@nnrp1.deja.com> <8tptnh$gcs$1@nntp9.atl.mindspring.net> <8tqphr$8lt$1@nnrp1.deja.com> <8tqufs$hc1$1@nntp9.atl.mindspring.net>`

```
  "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:
> >
> > What about the example of the summary data where the
…[6 more quoted lines elided]…
> internal SORT with both USING/GIVING and then re-open the output file
and
> read it sequentially - that is EXACTLY what an OUTPUT procedure is
all about

True, but OUTPUT PROCEDURE doesn't even start until the whole set of
data is sorted with all the implications of work space i/o.  While this
may save the final file write (or may not depending of how the work
space is assembled) and xertainly would save the read back, the use of
an ISAM summary file will save all the sort work area i/o (at least) at
the expense of the use of the summary index file.

Whichever uses less i/o depends on too many factors to contemplate, but
on very large sets of data (rather than small sets as asserted) the
sort work space i/o saving may be considerable.



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 10)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2000-11-02T16:31:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tsmhg$3ib$1@news.hitter.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz> <ublqvso3afpuueh41idll676g3h9h0g9vk@4ax.com> <8tpq8h$db5$1@nnrp1.deja.com> <8tptnh$gcs$1@nntp9.atl.mindspring.net> <8tqphr$8lt$1@nnrp1.deja.com>`

```
Richard Plinston,

It appears to me that your comments concerning MF indexed
files might refer to the Level II file system and not to the file
system that has been in use since COBOL/2. I believe the
COBOL/2 system is B+ not B. AIUI, B+ is less sensitive to the
order of insertion.

I am concerned that much of the disagreement in this thread
is fueled by views that are technically correct in one context;
but not correct in another.

I will agree with some of your comments within the context of
real applications on PCs; but disagree in other contexts.
----------
Sorting versus Indexed File - MF-oriented. (AIUI)

There is little difference in overall efficiency between loading
a MF indexed file to create a file ordered by key and sorting
an input file to create an ordered sequential file. The underlying
operations are not that different.

Sort copies the input data twice. During the first copy operation,
it collects the data from the key fields together with the position
of the record in the work file. This data is stored in blocks of
memory which are written to disk as necessary. The data in
the blocks is sorted. During the second copy operation, the
records are read in order of the key from the work file and
output sequentially.

Loading an indexed file performs one copy operation. During
that copy operation, the data from the key fields together with
the position of the record in the data portion of the file are
stored in blocks which are written to the index portion of the
file. Reading the indexed file sequentially is similar to the
second copy operation of the sort.

Where memory is limited, using an indexed file may be
more efficient than sort. This is because portions of the
B+ tree index blocks are cached allowing more rapid
updating. The blocks containing sort keys must be paged.

The above comments may also apply to implementations,
other than MF, on PCs and Unix.
----------
Binyamin Dissen,

Earlier you stated, "I dread to think of a platform where the
implementation of SORT requires even 10% of the time
required to use ISAM."

As you may see from my explanation above, some
implementations of ISAM may be very efficient when loading
unordered data. The lack of a 10:1 differential does not imply
a inefficient implementation of SORT.

Elsewhere you said, "In the real world databases are not
constantly reloaded. They have transactions applied against
them. And when the transactions are batched, sorting the
transactions allows much less i/o against the database."
[The use of 'database' appears to refer equally to ISAM.]

While I accept that sorting transactions may reduce I/O for
VSAM, it may have little or no advantage on some ISAM
implementations on PCs. That is because the order of records
in the data file (as explained above) may be different than the
primary key and, in fact, the records may be unordered. This
means that whether the transactions are sorted or not, access
to the individual records will occur randomly.

The bottom line is that efficient processing on PCs tends
toward using more indexed files and fewer sorts.
----------

riplin@kcbbs.gen.nz wrote in message <8tqphr$8lt$1@nnrp1.deja.com>...
>
>  "William M. Klein"  wrote:
…[43 more quoted lines elided]…
>primary key order.
[...]
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 8)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2000-11-01T23:57:52+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38u00t850p3fplgtia14iqbj15vpndmvhq@4ax.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz> <ublqvso3afpuueh41idll676g3h9h0g9vk@4ax.com> <8tpq8h$db5$1@nnrp1.deja.com>`

```
On Wed, 01 Nov 2000 19:17:46 GMT riplin@kcbbs.gen.nz wrote:

:>  Binyamin Dissen  wrote:

:>> :>> In the PC environment, does one load a ISAM
:>file without taking an initial
:>> :>> step (whether internal or external) of sorting
:>on the primary key?

:>> :>Well, I never bother.  For a start these are
:>usually one-offs and
:>> :>'optimising' the process is a usually a waste of
:>programmer time.

:>> Depends on the volume of data and the number of
:>times it happens.

:>An ISAM file is 'loaded' when a new system starts
:>running and there is existing data from an older
:>system or some other source. It is a one-off
:>(usually), once loaded it is added to and updated by
:>system procedures.  Do you have to do 'loads' on a
:>regular basis ?  Why is that ?

You were the one suggesting the ISAM file approach when a sort is required.

I pointed the problems with it.

:>> If your experience with PC's is limited to 1000
:>record files it pretty much
:>> doesn't matter how you do it -

:>I have clients with tens and hundreds of megabytes of
:>data.  Their data do not need to be 'loaded' into
:>ISAM files though this was done some years ago when
:>their current systems started.

Ditto.

:>> hell, you could probably do it in interpreted
:>> basic.

:>Except that 'interpreted basic' does not have access
:>to the Cobol ISAM files.  Certainly though the speed
:>of execution of the code (ie being interpreted) would
:>have an almost zero effect on a file 'load'.

Which was my point.

:>> :>Secondly, where I have in the past made such
:>comparisons, there is no
:>> :>advantage to having sorted data - the ISAM
:>structures are maintained as
:>> :>a balanced tree and the best loading sequence
:>_may_ be given by having
:>> :>the data in a binary chop sequence.  Random data
:>may emulate this well
:>> :>enough, it reduces index rotations that would be
:>_maximised_ by sorted
:>> :>data.

:>> Perhaps your ISAM implementation does not support a
:>LOAD mode?

:>Exactly right.  There is no need for one.  There is,
:>however, a REBUILD utility that can recreate an index
:>file from an existing ISAM data file.  Different ISAM
:>implementations have different utility functions and
:>different performance characteristics.

An ISAM that supports a load mode will build the higher level indexes at the
same time, the current index blocks will be in storage, and the adjacent keyed
records will be created in the same and adjacent blocks. 

This reduces I/O as well when the records are later accessed sequentially
using the primary key (which is why one would use ISAM rather than a hashing
algorithm).

:>> As a side point, are you claiming that your ISAM
:>implementation tries to
:>> dynamically maintain a balanced tree? Sounds good
:>for a file which is mostly
:>> accessed in input mode. You will pay the price if
:>you have significant update
:>> activity against the file.

:>Actually, there is always a trade off between update
:>activity and access.  Loading an ISAM file with data
:>sorted on the primary key where the index is a b-tree
:>(multi-way binary tree) will tend to produce a
:>single, simple linked list down through the 'greater
:>than' branches.  This would result in a serial search
:>for every read if the index blocks were not rotated
:>to balance the tree.

:>How does your ISAM structure work ?  How does it
:>avoid degrading into a simple linked list when
:>presented with sorted data ?  Are you sure that
:>sorting the data actually helps or was this just an
:>assumption that you made years ago and never updated
:>or checked ?

Refer to my comments on load mode above.

:>Yes, keeping the tree balanced benefits the accessing
:>while giving an overhead to record inserts and adds
:>(to the end). There is _no_ overhead on record
:>'updates' (except when a key value is changed).  If,
:>however, the inserts are relatively random then no
:>additional rotations are required because the tree
:>will be added to evenly and this will not result in
:>an unbalance.  Adding to the end of a file (as in
:>loading sorted data) maximises the need to rotate to
:>maintain balance.

I guess I should have been more clear and explicitly specified adds/deletes
and record size changes.

:>Maintaining the best access time at some expense of
:>insert is mostly a good trade-off as on any
:>reasonable system there will be several read accesses
:>for every insert.

Agree.

:>Perhaps you could describe your systems and why
:>optimising for read access is not worthwhile.

When did I state otherwise?

:>> :>Usually the files that I need to load have
:>alternate keys and any
:>> :>theoretical gain or loss on one key may be
:>compensated for in other
:>> :>keys.

:>> What kind of volume are you referring to?

:>Several megabytes.  But what has the volume to do
:>with it ?  If two or more indexes exist the the data
:>cannot be in the best sequence for both or all.
:>Making one index build in the 'best' way (which is
:>unlikely to be ordered) may well be the worst way for
:>the other.

Several megabytes is a decent amount of data - not that big, but decent.

Typically one has a one index that is most often used for sequential access.
That is the one that should be optimized.

:>> :>Now, a few decades ago I had to worry about
:>loading sequence and we even
:>> :>used to plan out the disk tracks based on the
:>data expected.  Much of
:>> :>the DP world has moved on since then, I certainly
:>have.

:>> What kind of volume are you referring to?

:>> :>> :>> There are no advantages to using a ISAM
:>file approach.
:>> :>> :>> Zero.

:>> :>> :>I would accept that there are none that you
:>know of.

:>> :>> For sorting data?

:>> :>You now seem to have an additional qualification.

:>> Refer to the Subject: File Sort

:>Actually your direct response was to a message saying
:>that a reasonable system design option may have put
:>the data into the correct sequence by using an
:>alternate key thus making the SORT entirely
:>unnecessary.

The central computer gets daily batched updates from 1000 stores.

Your solution??

As I said, your approach is valid for small amounts of data. When you get to
real world amounts of data the sort pays for itself over and over.

:>> :>Gee, I thought that I already had, go back and
:>read my message where a
:>> :>DOS system resulted in more reliable and faster
:>sorting by using an
:>> :>indexed file becasue the SORT module was choked
:>by lack of memory.

:>> Sounds like a bad sort implementation.

:>No.  Just a lack of infinite resources.  The SORT has
:>to load a code module and work in whatever memory is
:>available.  With small memory the prestring phase can
:>only write small strings resulting in a large number
:>of merge ways, if these exceed the ability of a
:>memory pool it has to resort the multiple merge
:>passes.

I fail to see how an ISAM implementation with the same constraints does
better. In fact, one would expect the ISAM approach to have much more I/O.

:>> If one does has a bad sort implementation and a
:>great ISAM implementation I
:>> could see your argument.

:>I am not sure that you could.

Why would you say that?

:>> :>The point is that one should not approach a
:>problem, any problem, with
:>> :>pre-conceived ideas about what the solution
:>should be.  Certainly there
:>> :>are needs for SORT verbs, in some cases this may
:>be the best solution,
:>> :>but in other cases it may be better to eliminate
:>SORTs or use an indexed
:>> :>file.

:>> Not if the object is to sort a file.

:>You really need to expand you viewpoint beyond
:>preconceived ideas.  Actually, the object is _never_
:>to 'sort a file', the object is to have data in a
:>particular sequence.  One possible, crude solution is
:>to 'sort a file'.

True.

:>Back when the mainframe that I used had 16Kwords of
:>memory, 4 tape decks and a pair of 4Megabyte drives
:>the solution often was 'sort a tape file'. For many
:>of us, even those on PCs, we can learn to apply
:>different, better design strategies.

Your approaches are valid for small amounts of data.

Even so the sort approach will be very unlikely to cost more time/resources
than the ISAM approach.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-11-02T07:45:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A017E1F.F8CA015F@brazee.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz> <ublqvso3afpuueh41idll676g3h9h0g9vk@4ax.com> <8tpq8h$db5$1@nnrp1.deja.com> <38u00t850p3fplgtia14iqbj15vpndmvhq@4ax.com>`

```
Binyamin Dissen wrote:

> An ISAM that supports a load mode will build the higher level indexes at the
> same time, the current index blocks will be in storage, and the adjacent keyed
…[4 more quoted lines elided]…
> algorithm).

When one adds an index to avoid sorting, there are two choices - the file gets
sorted anyway as described above, or it is a secondary index, and the adjacent
keyed records will be all over the place physically.   Neither is an advantage if
the sorted file is going to be used only once.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 10)_

- **From:** "Warren Simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2000-11-02T18:19:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dfiM5.17583$xJ4.847600@bgtnsc06-news.ops.worldnet.att.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz> <ublqvso3afpuueh41idll676g3h9h0g9vk@4ax.com> <8tpq8h$db5$1@nnrp1.deja.com> <38u00t850p3fplgtia14iqbj15vpndmvhq@4ax.com> <3A017E1F.F8CA015F@brazee.net>`

```
Howard,  from my years in the COBOL committee, a canned reaction surfaced.

Methods of implementation are not assumed.

With different vendors discussing a new feature to the then COBOL, few were
acquainted with the methods used to do things on the vendors hardware. To
avoid extended discussion based upon method, the above was adopted.

Warren Simmons
"Howard Brazee" <howard@brazee.net> wrote in message
news:3A017E1F.F8CA015F@brazee.net...
> Binyamin Dissen wrote:
>
> > An ISAM that supports a load mode will build the higher level indexes
at the
> > same time, the current index blocks will be in storage, and the
adjacent keyed
> > records will be created in the same and adjacent blocks.
> >
> > This reduces I/O as well when the records are later accessed
sequentially
> > using the primary key (which is why one would use ISAM rather than a
hashing
> > algorithm).
>
> When one adds an index to avoid sorting, there are two choices - the file
gets
> sorted anyway as described above, or it is a secondary index, and the
adjacent
> keyed records will be all over the place physically.   Neither is an
advantage if
> the sorted file is going to be used only once.
>
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 9)_

- **From:** riplin@kcbbs.gen.nz
- **Date:** 2000-11-02T20:25:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tsijv$nch$1@nnrp1.deja.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz> <ublqvso3afpuueh41idll676g3h9h0g9vk@4ax.com> <8tpq8h$db5$1@nnrp1.deja.com> <38u00t850p3fplgtia14iqbj15vpndmvhq@4ax.com>`

```
  Binyamin Dissen  wrote:

> :>> :>> In the PC environment, does one load a ISAM
> :>file without taking an initial
> :>> :>> step (whether internal or external) of sorting
> :>on the primary key?

> :>system procedures.  Do you have to do 'loads' on a
> :>regular basis ?  Why is that ?
>
> You were the one suggesting the ISAM file approach when a sort is
required.

It seemed to me to be quite illogical to ask whether one sorted the
data first before loading an ISAM file in the context of replacing a
SORT with an ISAM create.  Perhaps it didn't occur to you that it was
illogical.

But I do feel that you are making a career out of completely missing
the point.

> :>Except that 'interpreted basic' does not have access
> :>to the Cobol ISAM files.  Certainly though the speed
…[3 more quoted lines elided]…
> Which was my point.

Spped of execution of code (eg being interpreted) has very little
effect on most Cobol programs, and certainly zero of the SORT verb.
What actually _was_ your point ?

> An ISAM that supports a load mode will build the higher level indexes
at the
> same time, the current index blocks will be in storage, and the
adjacent keyed
> records will be created in the same and adjacent blocks.

Well on my system the ISAM builds all indexes as the data is loaded
into the file without a special 'load' mode.  The question then arises:
what happens when your system is not in 'load mode' ?  Does it not
build indexes at all ?

> This reduces I/O as well when the records are later accessed
sequentially
> using the primary key

And what happens with alternate keys ?  Or don't you use such
complicated features ?

> (which is why one would use ISAM rather than a
hashing
> algorithm).

> Typically one has a one index that is most often used for sequential
access.
> That is the one that should be optimized.

Typically this 'one' has primary keys that is most often used for
_random_ access.  Given that one cannot use alternate key directly for
random access (in Cobol) and one must use START and sequential read to
access using these alternate keys then you probably need to revise your
idea of which are 'most often' used for sequential access in the light
of suggesting that a load should be sorted on the primary key.

What actual systems have you designed ? or is your ideas purely
theoretical ?

> The central computer gets daily batched updates from 1000 stores.
>
> Your solution??
>
> As I said, your approach is valid for small amounts of data. When you
get to
> real world amounts of data the sort pays for itself over and over.

What real world systems have you designed or written that deal with
1000 stores ?  What systems do you use or develop that would consider
my hundreds of megabytes 'small' ? or are you just quoting from some
1960s design manual ?

> :>No.  Just a lack of infinite resources.  The SORT has
> :>to load a code module and work in whatever memory is
…[6 more quoted lines elided]…
> I fail to see how an ISAM implementation with the same constraints
does
> better. In fact, one would expect the ISAM approach to have much more
I/O.

Yes, I agree that you fail to see.

> :>> If one does has a bad sort implementation and a
> :>great ISAM implementation I
…[4 more quoted lines elided]…
> Why would you say that?

See previous comment.

> Your approaches are valid for small amounts of data.

And the amount of data that you deal with is ?  I would agree that the
largest number of stores that I developed systems for was 84
communicating back to a central point.  I doubt that 1000 would present
any more problems.  No, we did not try to save a bit of i/o by just
having a 1960s style card deck equivalent plus sorts, it was necessary
to provide some features for accessing the data received from the
branches.

> Even so the sort approach will be very unlikely to cost more
time/resources
> than the ISAM approach.

You appear to consider cost of computer time very highly, especially of
i/o.  Been there, done that, in the 60s.



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-11-02T15:03:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tskqn$sq9$1@nntp9.atl.mindspring.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz> <ublqvso3afpuueh41idll676g3h9h0g9vk@4ax.com> <8tpq8h$db5$1@nnrp1.deja.com> <38u00t850p3fplgtia14iqbj15vpndmvhq@4ax.com> <8tsijv$nch$1@nnrp1.deja.com>`

```
Mostly I have been "staying out" of the fights between the two of you where
you both make "valid points" but hide them in the middle of "snide comments"
that simply show that you work in different environments.  HOWEVER, there
are a few things in this post that are simply WRONG or so MISLEADING as to
verge on "wrong".

See below:
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 11)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-11-03T21:56:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A033499.48E5FAD4@Azonic.co.nz>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz> <ublqvso3afpuueh41idll676g3h9h0g9vk@4ax.com> <8tpq8h$db5$1@nnrp1.deja.com> <38u00t850p3fplgtia14iqbj15vpndmvhq@4ax.com> <8tsijv$nch$1@nnrp1.deja.com> <8tskqn$sq9$1@nntp9.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> Check your COBOL's Language Reference Manual.  There is *no* restriction on
…[3 more quoted lines elided]…
> tell which key (primary - or which of the alternates) to use.

Quite right, except that when WITH DUPLICATES is used (and I must adnit
that most of my alternate key cater for duplicates) the random read only
accesses the first record of those with the same alternate key.  It is
_necessary_ to read the others sequentially.

> Having ONLY 1000 "stores" in an IBM mainframe environment can be considered
> a "mid-size" environment.  

Yes, but I was enquiring on his personal experience, his credability in
claiming absolute rightnes (such as zero use for ..)

> If you think of your bank (assuming you are in
> the US) getting transactions from multiple ATMs associated with multiple
> branches; 

Well here in NZ the ATMs and EFTPOS terminals run right into the core of
the banks' data systems.  If for example I take money out of one ATM, or
use an EFTPOS terminal to buy something, then run around the corner to
another ATM, even of another bank, and get a balance of my account it
will show that transaction.

I have no doubt that many systems do still work like card decks and
sorts and produce the results a few days later, but this does not make
these the _best_ system even if it does some lots of i/o.  

> or how many "branch offices" there are for your insurance company;
> or how many airports reporting on tickets that have been used.  Each of
…[3 more quoted lines elided]…
> batching and updating of "master files" in such environments.

All quite true, and many still may work as they were designed 30 or more
years ago around, say, 2780 batch terminal operation.  But this does not
stop the collected batch file being an ISAM file or a database file.  It
is not inherent (as was claimed) that dumping the collected data into a
sequential file and sorting is the _best_ mechanism even if it is still
used.  It may have been to only viable mechanism 30 years ago or so.

> > You appear to consider cost of computer time very highly, especially of
> > i/o.  Been there, done that, in the 60s.
…[6 more quoted lines elided]…
> is looked at "lightly".

Well, exactly. As I said I had been there.  There has, however, been a
marked reduction in processing and i/o cost, by several orders of
magnitude, while programmer costs have increased.  This changes the
balance of how much saving of hardware costs is worthwhile.  While
replicating the system designs of the 60s may well be useful if i/o time
is to be kept to a minimum, this may not result in an optimal solution
for the user (cf ATMs and EFTPOS in US with those in NZ).

> As a "corollary" to this, you should contact any of the "major" institutions
> that you deal with (utilities that do monthly billing, banks, insurance
…[6 more quoted lines elided]…
> restricted from ever moving into production.
I am sure that there still are very many companies still working that
way.  This is often seen as the 'normal' for the mainframe environment. 
However, it is not axiomatic that because this is the way it was done
'in my day' that this is how they _all_ still operate, nor that this is
the _best_ way to operate.

But even if a computer system does collect data and keeps it for 'batch
processing' it is not axiomatic (as was claimed) that it must therefore
be put into an emulation of a card pack and sorted.

You are partly correct that the differences in this discussion stem from
differences of environment.  It seems that many mainframers regard PCs
as terminals or as small, slow mainframes.  I work with many clients
from 'one man plus dog' to large corporates.  The trend over the last
couple of decades has been to change from overnight batch processing to
fully interactive and real time, here at least, with the mainframe
acting primarily as a database server.  20 years ago I was doing fully
interactive micro based systems for small companies (ie no "nightly
batch run" required).  Now big companies work that way too.

It is almost a 'generational' difference as well as mainframe/PC.

>  Similarly, if you introduce a
> new alternate index into an existing indexed file that changes "average"
…[3 more quoted lines elided]…
> instantaneously.

Why would they disallow something that improves response time ?    ;-)

Yes, I know what you actually meant.

However, changing an EFTPOS system so that it records the transaction
right into the account instead of doing a simple check and putting the
transaction into a serial file for later batch sort and update may be
such a benefit (to the bank, to the client, to the shop) that it
outweighs the additional i/o cost.  To sit back congratulating oneself
on how efficient the batch cycle is while bank customers change to a
different bank that provides better services seems to be self
defeating.  This may be why US banks have EFTPOS on a 3 day cycle (with
all the problems this causes) while here it is real time.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 12)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-11-03T11:29:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C8AC80252BB093A1.474405C19F5E3D3F.382D6A70DEA50AAE@lp.airnews.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz> <ublqvso3afpuueh41idll676g3h9h0g9vk@4ax.com> <8tpq8h$db5$1@nnrp1.deja.com> <38u00t850p3fplgtia14iqbj15vpndmvhq@4ax.com> <8tsijv$nch$1@nnrp1.deja.com> <8tskqn$sq9$1@nntp9.atl.mindspring.net> <3A033499.48E5FAD4@Azonic.co.nz>`

```
On Fri, 03 Nov 2000 21:56:41 +0000, Richard Plinston
<riplin@Azonic.co.nz> enlightened us:

>William M. Klein wrote:
>> 
…[113 more quoted lines elided]…
>all the problems this causes) while here it is real time.

Having written banking software for both the US and New Zealand banks,
I can tell you that EFTPOS is definitely not on a 3 day cycle in
either place (at least for the banks that run my companies software).
It is real time updated to a mirror image master file.  The
transaction is logged to an ESDS file.  The ESDS file is stripped by
aplication at night to create a sequential transaction file which is
then reposted to the real master files.  This is done to catch fraud
and produce reports as well as maintain a sequential history file.
The masters (both real and mirrored are VSAM).  And believe it or not
we actually sort the transaction file before posting.  The advantage
to our method is if there is ever a major crash of disk, we can
recover and recreate everything in a very short period of time.  That
is not always the case with real-time only processing.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

First guy (proudly): "My wife's an angel."
Second guy: "You're lucky, mine's still alive."


Boycott Mitsubishi Industries
For more info, please see:  
http://www.ran.org/ran/ran_campaigns/mitsubishi/background.html

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 13)_

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2000-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.g3h0q30.pminews@news.wanadoo.es>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz> <ublqvso3afpuueh41idll676g3h9h0g9vk@4ax.com> <8tpq8h$db5$1@nnrp1.deja.com> <38u00t850p3fplgtia14iqbj15vpndmvhq@4ax.com> <8tsijv$nch$1@nnrp1.deja.com> <8tskqn$sq9$1@nntp9.atl.mindspring.net> <3A033499.48E5FAD4@Azonic.co.nz> <C8AC80252BB093A1.474405C19F5E3D3F.382D6A70DEA50AAE@lp.airnews.net>`

```
On Fri, 03 Nov 2000 11:29:13 -0500, SkippyPB wrote:

>
>Having written banking software for both the US and New Zealand banks,
…[14 more quoted lines elided]…
>
I have been a Systems Programmer with a Spanish bank for many years, and we
did update the real database online during the day, but also logged every
transaction in both an ESDS and a KSDS on different disks. At the end of the
day, we closed for 5 minutes the process, copied the databases and re-opened.
The copy was used for batch processing, and early in the morning, we closed
again the online process and applied the movements from the online process to
the updated batch database. I once calculated that about 35% of the batch
shift was sorting data.
Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 12)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-11-03T22:30:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A033C78.5F22FC69@Azonic.co.nz>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz> <ublqvso3afpuueh41idll676g3h9h0g9vk@4ax.com> <8tpq8h$db5$1@nnrp1.deja.com> <38u00t850p3fplgtia14iqbj15vpndmvhq@4ax.com> <8tsijv$nch$1@nnrp1.deja.com> <8tskqn$sq9$1@nntp9.atl.mindspring.net> <3A033499.48E5FAD4@Azonic.co.nz>`

```
> William M. Klein wrote:
> 
…[5 more quoted lines elided]…
> > instantaneously.

Ignoring the typos, it is not axiomatic that adding an additional
alternate key will be detrimental to the average response time.  The
additional key will only incur an overhead (on most systems) on insert
and deletes and access via existing keys and updates will not (usually)
be affected at all.  However, if the alternate key provides an
improvement is some access path then there _may_ be an improvement in
the average response time.  If the new key provides an additional
required facility that improves the system then it may be put into
production in spite of a small overhead.

You seem to be pre-judging these situations.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 13)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tuv0a$11u$1@nntp9.atl.mindspring.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz> <ublqvso3afpuueh41idll676g3h9h0g9vk@4ax.com> <8tpq8h$db5$1@nnrp1.deja.com> <38u00t850p3fplgtia14iqbj15vpndmvhq@4ax.com> <8tsijv$nch$1@nnrp1.deja.com> <8tskqn$sq9$1@nntp9.atl.mindspring.net> <3A033499.48E5FAD4@Azonic.co.nz> <3A033C78.5F22FC69@Azonic.co.nz>`

```
First - sorry for the 2.2 to 2.1 - instead of 2.1 to 2.2 "example".

HOWEVER, that sentence was written explicitly to state that *IF* the
introduction of an alternate key made this difference, then it would not be
allowed (in some environments).  I am not claiming that it always would
cause any degradation.  Nor am I claiming that such a "minimal" degradation
in response time would always cause the alternate key to be "rejected".  For
example, if the transaction that is "slowed down" is one that is run once an
hour - and by a "few" users and the addition of the alternate key speed up a
"major" application, then it almost certainly WOULD be allowed.  What I was
trying to say was that any "axiomatic" addition of alternate keys is just as
"wrong" a solution as any other that is not judged by the environment in
which it is used and the resources available.

P.S.  Not related to this "part" of the thread - but another.  I do not
claim that ANY large institution in the US or elsewhere doesn't do much/most
of its "interactive" data updating in "real time".  However, I will repeat
that I don't think that there are many "large" institutions that don't still
have SOME "nightly batch applications".  This is a "tricky" thing to
maintain in today's 24x7 environment - especially for large international
companies (where "night" for one site is the middle of the business day in
others) - but I do think that most do maintain such systems.  Furthermore,
it is these systems where COBOL is still one of (if not the primary)
dominate programming language.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-11-02T07:37:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A017C22.BC4D5C12@brazee.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz> <ublqvso3afpuueh41idll676g3h9h0g9vk@4ax.com> <8tpq8h$db5$1@nnrp1.deja.com>`

```
There are a few trade offs in deciding between sorting a file or
indexing a file.

Doing a sort is usually quicker than putting on an index.

Doing a sort doesn't put the original data at risk.

Using an index means you have THE data - up to date, an current.  You're
not using a copy.

Doing a second sort is slower than using the already created index.

Having an index slows down writes and some updates.

Having an index generally is more work for systems programmers.

Sorts can fail more easily due to lack of temporary disk space.  But
when they do, the original data is not at risk of being corrupted.

Sorts can be more efficient when selection criteria are used to exclude
unneeded records.

Once you have the data, a sorted record is quicker to read than an
indexed record - your next record is next in virtual/disk memory and is
likely in your buffer.   This often isn't important, but occasionally
is.

I believe it is usually a question of programmer philosophy.  To some,
"slap an index on the data and continue" seems easier.  To others
(myself), this means you are creating a more complex environment for
anybody else who will ever use the file.    These different philosophies
will set your default action - but good programmers will vary their
default actions to fit the situation.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-11-02T07:40:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A017CE6.C9413644@brazee.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz> <ublqvso3afpuueh41idll676g3h9h0g9vk@4ax.com> <8tpq8h$db5$1@nnrp1.deja.com>`

```
riplin@kcbbs.gen.nz wrote:

>  Back when the mainframe that I used had 16Kwords of
> memory, 4 tape decks and a pair of 4Megabyte drives
> the solution often was 'sort a tape file'. For many
> of us, even those on PCs, we can learn to apply
> different, better design strategies.

And the method often was - sort the first 1000 records to one tape, sort
the next 1000 records to the next, etc.. and then merge the tapes
together to a third tape.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 6)_

- **From:** "Warren Simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2000-10-31T22:28:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sIHL5.12561$MR3.732546@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDD846.FD8B922B@Azonic.co.nz>`

```
And I remember an application on the Univac I that used two copies of the
same file concatenated as one file. Each copy had it's own sequence.
However, the file was much less than one tape full, and the program became
much simpler because a tape sort took about one hour. <G>

Warren Simmons


"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:39FDD846.FD8B922B@Azonic.co.nz...
> Binyamin Dissen wrote:
> >
> > In the PC environment, does one load a ISAM file without taking an
initial
> > step (whether internal or external) of sorting on the primary key?
>
…[36 more quoted lines elided]…
> file.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-10-30T20:32:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39FDDAFA.7700CFBD@Azonic.co.nz>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com>`

```
Binyamin Dissen wrote:

> :>> There are no advantages to using a ISAM file approach.
> 
…[6 more quoted lines elided]…
> Show one.

Actually I can think of a second one as well.  Where only totaled or
summary data is required in a particular sequence it can be _much_
faster (depending on several factors) to write an ISAM file of the
summary data by adding values where a record already exists and then
printing the report from the total records. This may be better than
sorting and outputting every record and reading these all back to add
them up and produce the report.

Back in the dim past one machine that I programmed has a sort program
generator that catered for an 'equal key' routine where records could be
added together and one dropped to produce this sort of summarising.  If
the Cobol SORT verb had an EQUAL KEY PROCEDURE option where, say, two or
more RETURNs could be done followed by a RELEASE of the total then this
may beat summarising via indexed file (in certain cases).
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 6)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2000-10-30T13:42:23+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5hnqvskgrclj0h8ol245elv74ee1ds7rdk@4ax.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDDAFA.7700CFBD@Azonic.co.nz>`

```
On Mon, 30 Oct 2000 20:32:58 +0000 Richard Plinston <riplin@Azonic.co.nz>
wrote:

:>Binyamin Dissen wrote:

:>> :>> There are no advantages to using a ISAM file approach.
 
:>> :>> Zero.
 
:>> :>I would accept that there are none that you know of.
 
:>> For sorting data?
 
:>> Show one.

:>Actually I can think of a second one as well.  Where only totaled or
:>summary data is required in a particular sequence it can be _much_
:>faster (depending on several factors) to write an ISAM file of the
:>summary data by adding values where a record already exists and then
:>printing the report from the total records. This may be better than
:>sorting and outputting every record and reading these all back to add
:>them up and produce the report.

That would depend on the volume of data, its ratio to the number of unique
records, clustering of records and the amount of resources available to the
program.

In some cases a pure memory approach will be the best.

:>Back in the dim past one machine that I programmed has a sort program
:>generator that catered for an 'equal key' routine where records could be
:>added together and one dropped to produce this sort of summarising.  If
:>the Cobol SORT verb had an EQUAL KEY PROCEDURE option where, say, two or
:>more RETURNs could be done followed by a RELEASE of the total then this
:>may beat summarising via indexed file (in certain cases).

As the output procedure can do this, I fail to see the advantage of an equal
key procedure.

It sounds like you have a real bad sort implementation, that costed a large
number of resources for each invocation of the procedure.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 6)_

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2000-10-31T07:56:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.g3as2q0.pminews@news.wanadoo.es>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDDAFA.7700CFBD@Azonic.co.nz>`

```
On Mon, 30 Oct 2000 20:32:58 +0000, Richard Plinston wrote:

>Binyamin Dissen wrote:
>
…[23 more quoted lines elided]…
>may beat summarising via indexed file (in certain cases).

On IBM mainframe sorts you can pass parameters to an internal sort with an
external file, invoking the OPTION EQUALS and the SUM FIELDS parameters.
Doing this, you'll just get your totals from your internal sort
Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-11-01T06:46:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39FFBC30.C37329E5@Azonic.co.nz>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <dj5pvsg3fiht0023vclcdu18748ogpm9pn@4ax.com> <39FDDAFA.7700CFBD@Azonic.co.nz> <jvyyrzubevmbagrfvasbezngvpnpbz.g3as2q0.pminews@news.wanadoo.es>`

```
Willem Clements wrote:
> >
> >Back in the dim past one machine that I programmed has a sort program
…[8 more quoted lines elided]…
> Doing this, you'll just get your totals from your internal sort

I am sure that there are many varied ways of using sort utilities on
various platforms, including PC systems.  But this is not standard
Cobol, nor is it platform independant (unless you view 'portable' as
being to all IBM Mainframes).

I think that additional Cobol syntax to cover EQUAL KEY may be useful,
but won't happen anytime soon.  In the meantime summarising to an
indexed file is a useful standard alternate.  

There may also be cases (this is a third instance against a claimed
zero) where there simply isn't sufficient sort-work disk space to
provide for a straight sort of a huge data file.  Even if there is an
OUTPUT-PROCEDURE the work area must (in many cases) be at least as large
as the data records being sorted before the first RETURN can be done. 
If a file output is specified then it may be necessary to be able to
provide for the complete output file size as well as the work area, both
of which would be at least the input data size.  In some cases the
output file may not require to be additional to the working space but
this depends on the implementation.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-10-30T07:55:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39FD8BEA.32F95B37@brazee.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz>`

```
Richard Plinston wrote:

> 'Using an ISAM file' may take zero time when the required sorted
> sequence is already in one of the alternate keys.

(near zero)
As long as there was a good reason for having that sort sequence, use it.  But
creating an alternative key to avoid a sort is virtually never cost effective.
They slow everything down.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 5)_

- **From:** riplin@kcbbs.gen.nz
- **Date:** 2000-11-01T20:17:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tptp2$gm8$1@nnrp1.deja.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <39FD2AED.5126FFEB@Azonic.co.nz> <39FD8BEA.32F95B37@brazee.net>`

```
In article <39FD8BEA.32F95B37@brazee.net>,
  Howard Brazee <howard@brazee.net> wrote:
> Richard Plinston wrote:
>
> > 'Using an ISAM file' may take zero time when the
required sorted
> > sequence is already in one of the alternate keys.
>
> (near zero)
> As long as there was a good reason for having that
sort sequence, use it.  But
> creating an alternative key to avoid a sort is
virtually never cost effective.
> They slow everything down.

That may be a valid point if SORTs took zero time and
resouces.  Having an alternate key _may_ take
additional time on record insert but does not 'slow
_everything_ down'.  It does not slow down record
access or update (rewrite, unless the key value
changes).

Accessing via an alternate key on the main data file,
rather than on a sorted copy also has implications
for file sharing and locking.  If two users want a
report in a particular sequence then they may find
that sort being done twice, whereas an alternate key
gives no further overhead.  The two users may also
find file clashes if the sort has a fixed name for
the output file and this may cause failures if they
occur at much the same time.

But then perhaps you don't have more than one user.






Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: File Sort

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-10-31T12:21:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tmdff$hbd$1@nnrp1.deja.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com>`

```

> There are no advantages to using a ISAM file approach.
>
> Zero.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 4)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2000-10-31T17:01:41+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<femtvss6a8oqhvg73sgtmvqo2r9o5fio93@4ax.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <8tmdff$hbd$1@nnrp1.deja.com>`

```
On Tue, 31 Oct 2000 12:21:06 GMT Foodman <foodman123@aol.com> wrote:

:>From: Foodman <foodman123@aol.com>
:>Subject: Re: File Sort
:>Newsgroups: comp.lang.cobol
:>Date: Tue, 31 Oct 2000 12:21:06 GMT
:>Lines: 96

:>> There are no advantages to using a ISAM file approach.

:>> Zero.


:>You need clarification, here it is.

:>A. The guy asked about SORT.

And was answered.

:>B. Knowing that there are dozens of dwarves in the CLC who know
:>   about that, I know that the guy will get an answer somehow.

And he has received answers.

:>C. Because the guy is a newcomer, and because the odds are that
:>   his instructor is hopeless, and because I think that presenting
:>   alternative methods to newcomers is a good idea, I posted my
:>   suggestion.  Note that I did NOT discourage the use of SORT,
:>   but merely presented an alternative.  Should I infer
:>   that you do not like presenting alternative methods to
:>   newcomers? I don't post these things for the dwarves of
:>   CLC but for open-minded newcomers and I do it in spite of
:>   continued criticism.

Feel free.

Unless the purpose of the sort was to load a database that will be used for
future inquiries, the SORT implementation is that bad and the ISAM
implementation is that good that ISAM can build the database with a balanced
index even though the data is in a random order .... I fail to see how using
ISAM to sort will be an approach in the real world.

:>D. I would guess that some newcomers might be happy to see an
:>   alternative method which might open up new ideas to them.
:>   I thought that's what forums were for, no? Do you disagree?

Feel free to present the ideas.

But if you feel that your ideas should not be criticized, perhaps you should
consider posting to clc.moderated.by.foodman

:>E. If no-one suggests alternative methods, the guy can grow up
:>   assuming that sorts are an everyday part of life in computerland
:>   and may never go beyond that. (Did this happen to you?)

It is a part of ordinary life of programmers who work with any significant
volume of data.

For minimal amounts of data, which are the applications that you seem to be
involved with, there is not much benefit from knocking down i/o times.

:>F. If an application programmer is assigned a task to create
:>   something from which a report can be produced, they should
:>   be required to do it in the fastest, least expensive way
:>   possible. 

Sometimes those cannot be combined.

Of the three constraints of a product, those being time, cost and features, I
allow the end user/client to specify two. I get to pick the third.

:>             Furthermore, that effort should produce the most
:>   usable output in consideration of current and future
:>   requirements. Creating an ISAM/DBMS file meets this requirement.

Your are assuming the purpose of the sort was to load a database that will be
used for future inquiries.

In the real world databases are not constantly reloaded. They have
transactions applied against them. And when the transactions are batched,
sorting the transactions allows much less i/o against the database. 

If all the transactions are on line there is nothing to sort.

:>G. Sorting is archaic and crude. First of all, what is this
:>   guy sorting? Where did it come from? How was it entered
:>   into the file that it is in? Was it typed into some
:>   flat file, or what? Was it edited? Don't talk to me about
:>   this being a course exercise either because course exercises
:>   should reflect the real world and if they are using a flat
:>   file the instructor should be shot.  Would people design systems in
:>   the business world which let people just type unedited data
:>   into a flat file? I would hope not, but suspect that they do.
:>   The data should have been typed directly into an ISAM/DBMS file
:>   and edited to the hilt at that time, this obviously eliminates
:>   the need to sort it. (Don't talk to me about generated data as
:>   from a phone system, that is not the topic.) (Flat file: a
:>   file with no keys accessed sequentially.)

In your world of all access being on line with secondary keys to all
appropriate fields, there is nothing to sort.

Real world companies with significant volumes of data have to trade off
against doing all updates on-line with higher i/o, storage and CPU
requirements (even though the data is not needed immediately) or batching
transactions for daily runs, with reduced i/o, storage and CPU requirements.

If your database has only 1000 records, you do not have to really care about
this.

:>H. As I said above, if a programmer is assigned a task to
:>   create something, it should be done in the fastest time
:>   and yield the greatest benefit. Sorting flat files just
:>   doesn't cut it especially when you need the same file
:>   sorted in nineteen different ways.

Your assumption above is only valid if the purpose of the sort was to load a
database that will be used for future inquiries.

:>   Some advantages to the ISAM/DBMS approach are:

:>   1. Records can be accessed individually, directly and randomly.
:>   2. Multiple keys allow different sequences for different reports.
:>   3. Records can be deleted and changed directly and randomly.
:>   4. Files can be started at any point to restrict reports to a subset.
:>   5. Sorting not required.

:>   But, you know all of this already, no?

And how does this apply to his original query?

:>I. If you still don't think that this makes SENSE, please explain.

Look at the comments.

:>J. If you don't think I should present alternative methods to newcomers,
:>   please explain.

If you don't think your ideas should be criticized, please explain.

:>K. If you think that the sort approach is the better of the two,
:>   Please explain why for the benefit of the newcomers.

Look at the comments.

:>(BTW, do you spend more time in the bar or the grill or at your
:>computer?)

I am busy researching bars and grills around the world before I really get
involved in developing that part of the business.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 5)_

- **From:** Jeffry Kennedy <jakcert@attglobal.net>
- **Date:** 2000-10-31T14:32:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39FF2C4E.F8C20287@attglobal.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <8tmdff$hbd$1@nnrp1.deja.com> <femtvss6a8oqhvg73sgtmvqo2r9o5fio93@4ax.com>`

```


Binyamin Dissen wrote:

>
> :>(BTW, do you spend more time in the bar or the grill or at your
…[3 more quoted lines elided]…
> involved in developing that part of the business

Binyamin when you get done with your research I sugest you sort them into a large
database.  ROFL
I agree with you 100% if we didn't sort our batches of data before we updated the
database  we would never get anything run.  I/O would kill us.

I think I am begining to se the "Dilworth Anomoly" in action

PatH

>

>
>
…[5 more quoted lines elided]…
> Director, Dissen Software, Bar & Grill - Israel
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 6)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-11-01T03:46:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BmML5.1877$5v6.23755@iad-read.news.verio.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tmdff$hbd$1@nnrp1.deja.com> <femtvss6a8oqhvg73sgtmvqo2r9o5fio93@4ax.com> <39FF2C4E.F8C20287@attglobal.net>`

```
In article <39FF2C4E.F8C20287@attglobal.net>,
Jeffry Kennedy  <jakcert@attglobal.net> wrote:
>
>
…[14 more quoted lines elided]…
>I think I am begining to se the "Dilworth Anomoly" in action

Now, now... do not confuse the Man and the Circumstances.  While Mr
Dilworth has had a hand in the shaping of his anomalous circumstances -
and while this Anomaly he has shaped and inhabited has, in turn, had an
effect on him - Mr Dilworth should not be confused with the Dilworth
Anomaly.

After all... oh, I *cannot* resist, I am so weak, I am so frail, I yield
to temptation!... after all, if one were to confuse the Man with the
Circumstances one might lose sight of the fact that - at least in this
situation - the Circumstances stand a chance of being changed, while the
Man...

DD
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 5)_

- **From:** riplin@kcbbs.gen.nz
- **Date:** 2000-11-01T19:52:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tps91$f68$1@nnrp1.deja.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <8tmdff$hbd$1@nnrp1.deja.com> <femtvss6a8oqhvg73sgtmvqo2r9o5fio93@4ax.com>`

```
  Binyamin Dissen wrote:
>
> :>> There are no advantages to using a ISAM file
approach.
> :>> Zero.

> For minimal amounts of data, which are the
applications that you seem to be
> involved with, there is not much benefit from
knocking down i/o times.

Define 'minimal' in the context of hundreds of
megabytes.

Show how SORTing is always guaranteed to reduce
overall i/o times against alternate mechanisms that
you seem not to be able to think of.

> Your are assuming the purpose of the sort was to
load a database that will be
> used for future inquiries.

No, DD wasn't.  He was contemplating that an existing
file in use may have an alternate key added to
provide for not having a SORT at all.


> In the real world databases are not constantly
reloaded. They have
> transactions applied against them. And when the
transactions are batched,
> sorting the transactions allows much less i/o
against the database.

In any real world situations the batch transaction
file may be maintained as an indexed file, without
needing any sorts at all, with alternate keys that
give the transactions the best sequence for applying
to the database.

This gives the ability to access the batch data (by
batch number eg) for other purposes.

Just because you can only think of sorting to give
this update i/o reduction does not mean that it is
the only way of achieving this.

> If all the transactions are on line there is
nothing to sort.

There are batch based interactive systems (for
several good reasons).  Usually these are
sophisticated enough to hold batched transactions in
indexed files eliminating the need for sorts and
providing access to the data that sequential (card
pack based) batch files that must be sorted cannot
achieve.


> Real world companies with significant volumes of
data have to trade off
> against doing all updates on-line with higher i/o,
storage and CPU
> requirements (even though the data is not needed
immediately) or batching
> transactions for daily runs, with reduced i/o,
storage and CPU requirements.

These are not the only two alternates.  There are
other approaches that may also provide better access
as well as batching transactions.

>
> :>   But, you know all of this already, no?

I think that the answer is .... No.


> If you don't think your ideas should be criticized,
please explain.

_All_ ideas should be intellegently and
constructively criticised and not just dismissed
because they don't fit into some pre-conceived
cubby-hole.



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 6)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2000-11-02T00:56:39+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tc510tc1uea6jpsjumrm6ip7vt8r7mf10m@4ax.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <8tmdff$hbd$1@nnrp1.deja.com> <femtvss6a8oqhvg73sgtmvqo2r9o5fio93@4ax.com> <8tps91$f68$1@nnrp1.deja.com>`

```
On Wed, 01 Nov 2000 19:52:06 GMT riplin@kcbbs.gen.nz wrote:

:>  Binyamin Dissen wrote:

:>> :>> There are no advantages to using a ISAM file
:>approach.
:>> :>> Zero.

:>> For minimal amounts of data, which are the
:>applications that you seem to be
:>> involved with, there is not much benefit from
:>knocking down i/o times.

:>Define 'minimal' in the context of hundreds of
:>megabytes.

Hundreds of megabytes would not be minimal.

:>Show how SORTing is always guaranteed to reduce
:>overall i/o times against alternate mechanisms that
:>you seem not to be able to think of.

????

Show how auto travel is better than travel methods that you seem not to think
of.

:>> Your are assuming the purpose of the sort was to
:>load a database that will be
:>> used for future inquiries.

:>No, DD wasn't.  He was contemplating that an existing
:>file in use may have an alternate key added to
:>provide for not having a SORT at all.

If it is not to load a database, what is the point of creating a ISAM file for
a one time sequential use?

:>> In the real world databases are not constantly
:>reloaded. They have
:>> transactions applied against them. And when the
:>transactions are batched,
:>> sorting the transactions allows much less i/o
:>against the database.

:>In any real world situations the batch transaction
:>file may be maintained as an indexed file, without
:>needing any sorts at all, with alternate keys that
:>give the transactions the best sequence for applying
:>to the database.

Explain how 1000 stores who daily send their batched inventory updates to
corporate headquarters can do this.

What resources will be required at each store?

With low volumes one can get away with solutions that will just not work for
high volumes of data.

:>This gives the ability to access the batch data (by
:>batch number eg) for other purposes.

It is not accessed from the collecting site.

:>Just because you can only think of sorting to give
:>this update i/o reduction does not mean that it is
:>the only way of achieving this.

We are waiting for your solution.

:>> If all the transactions are on line there is
:>nothing to sort.

What kind of hardware, software and personnel is required to maintain this
information in each store? 

How much longer will a consumer transaction take?

Since the individual store rarely need this data online, what is their trade
off for this additional time and expense?

:>There are batch based interactive systems (for
:>several good reasons).  Usually these are
:>sophisticated enough to hold batched transactions in
:>indexed files eliminating the need for sorts and
:>providing access to the data that sequential (card
:>pack based) batch files that must be sorted cannot
:>achieve.

How do you do the 1000 stores?

:>> Real world companies with significant volumes of
:>data have to trade off
:>> against doing all updates on-line with higher i/o,
:>storage and CPU
:>> requirements (even though the data is not needed
:>immediately) or batching
:>> transactions for daily runs, with reduced i/o,
:>storage and CPU requirements.

:>These are not the only two alternates.  There are
:>other approaches that may also provide better access
:>as well as batching transactions.

You don't seem to able to state them.

:>> :>   But, you know all of this already, no?

:>I think that the answer is .... No.

To repeat, with low volumes one can get away with solutions that will just not
work for high volumes of data.

:>> If you don't think your ideas should be criticized,
:>please explain.

:>_All_ ideas should be intellegently and
:>constructively criticised and not just dismissed
:>because they don't fit into some pre-conceived
:>cubby-hole.

I gave detailed criticism.

You merely suggested that there are better ways without specifying them.

This will probably be my last response to a post of yours in this thread as
you seem to be only interesting in defending yourself, suggesting that there
are better approaches which you fail to disclose.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-11-02T15:25:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A018774.D81211AC@Azonic.co.nz>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <5fnnvsg04eble43g2rip4vkec30jr9f4k3@4ax.com> <8tmdff$hbd$1@nnrp1.deja.com> <femtvss6a8oqhvg73sgtmvqo2r9o5fio93@4ax.com> <8tps91$f68$1@nnrp1.deja.com> <tc510tc1uea6jpsjumrm6ip7vt8r7mf10m@4ax.com>`

```
Binyamin Dissen wrote:
> 
> :>> :>> There are no advantages to using a ISAM file
…[6 more quoted lines elided]…
> :>knocking down i/o times.

> Hundreds of megabytes would not be minimal.

Thank you for correcting your previous mistaken assumptions.

> :>Show how SORTing is always guaranteed to reduce
> :>overall i/o times against alternate mechanisms that
…[5 more quoted lines elided]…
> of.

But then I am not the one claiming that 'Auto travel' or 'Sorting' is
the best method.  You had made the claim that SORTing the batch
transactions was the best or only way to reduce i/o times in updates.

> :>> Your are assuming the purpose of the sort was to
> :>load a database that will be
…[6 more quoted lines elided]…
> If it is not to load a database, 

What do you understand by the term 'load a database' ?

> what is the point of creating a ISAM file for
> a one time sequential use?

Why have you made futher unwarranted assumptions about the use of this
file ?

> :>> In the real world databases are not constantly
> :>reloaded. They have
…[12 more quoted lines elided]…
> corporate headquarters can do this.

Easily.  As the data arrives via ftp, EMail, direct communication or
otherwise the program that receives each batch verifies is as usual and
adds it into an ISAM batch file instead of adding it to the sequential
batch file - ie much the same process with just a change to the SELECT
ASSIGN.

Or would you sort each of the 1000 files separately ?  How would you
detect and report duplication of batches ? How would you detect and
report missing stores and/or batches ?

> What resources will be required at each store?

No more than exists now, probably.

Having clients with remote branches I do have experience with
transferring data in this way.

> With low volumes one can get away with solutions that will just not work for
> high volumes of data.

True.  This does not, however, make sequential data and sorts an
appropriate solution for large volumes, or even for small ones.  In the
case of your imaginary '1000 branches' there is a large amount of
checking required to ensure against loss of data or duplication, checks
which may be adequately done manually for small volumes.

> :>This gives the ability to access the batch data (by
> :>batch number eg) for other purposes.
> 
> It is not accessed from the collecting site.

Maybe not, but it may well be accessed in different ways at the
receiving site, for example for checking purposes prior to releasing the
batch for updating.

> :>Just because you can only think of sorting to give
> :>this update i/o reduction does not mean that it is
> :>the only way of achieving this.
> 
> We are waiting for your solution.

Then you have failed to comprehend what was posted.  SORTing is not the
only way of having data accessible in a particular sequence.  It has
been mentioned several times that accessing the data using an alternate
key giving the appropriate sequencing is a viable mechanism.  

Are you still waiting ?  Did you skip the previous paragraph ?

> :>> If all the transactions are on line there is
> :>nothing to sort.
…[3 more quoted lines elided]…
> How much longer will a consumer transaction take?

Why do you think that this need be any different ?  What mechanisms are
currently used for PLUs ? charge account lookups ?, credit
authorisations ?,  cancelling transactions ?  preparing batches for
transmitting ?  taking local reports ?

Is it all sequential files and sorts ?

> Since the individual store rarely need this data online, what is their trade
> off for this additional time and expense?

Why do you think that this need be any different ?

Why do you think that stores 'rarely need this data online' ?  My
client's stores want _all_ their data online all the time.

> :>There are batch based interactive systems (for
> :>several good reasons).  Usually these are
…[6 more quoted lines elided]…
> How do you do the 1000 stores?

Why do you think that this need be any different ?

> :>> Real world companies with significant volumes of
> :>data have to trade off
…[11 more quoted lines elided]…
> You don't seem to able to state them.

You don't seem to be able to imagine that there are even any beyond the
two: unsorted sequential transactions with multiple access (high i/o)
against the master files, or SORTing the transactions so that master
file access is ordered and thus reduced.

These are two of the standard approaches of any beginners course from
the 1960s.

I suspect that you haven't done any real systems as most transaction
based systems need to update several master records that are in
conflicting sequence: Debtor's balances, account sales, product sales,
stock levels.  Thus your reduced i/o must require sorting to several
different sequences and applying the transactions to each MF in turn. 
Hmmm that sounds like something I designed in the early 70s for running
on tape drives.  The hard part is when a transaction update needs to be
failed because, eg, there is no product master record for the sales item
and you have already updated the customer (or vice versa).

It _should_ not be necessary to state what other alternates are, you
should be familiar with others, but, in fact, I have stated alternates,
you just haven't noticed.

> To repeat, with low volumes one can get away with solutions that will just not
> work for high volumes of data.

Yes, I know you keep repeating that, but then you agreed that hundreds
of megabytes was not 'low volumes'. What volumes are _you_ actually
working with ?

 
> You merely suggested that there are better ways 

No.  Wrong. I have been suggesting that there are _other_ ways, and I
have claimed that whether they are better is dependant on many factors,
some of which I mentioned.

> without specifying them.

Actually I have been specifying them. It must be that you fail to notice
these.

> This will probably be my last response to a post of yours in this thread as
> you seem to be only interesting in defending yourself, 

The only 'defending' necessary is against the unwarranted assertions and
incorrect assumptions that you have made.

> suggesting that there
> are better approaches which you fail to disclose.

I cannot explain why you think that I 'failed to disclose' these. 
Perhaps you think that 'if it isn't a SORT it isn't a solution'.
```

##### ↳ ↳ Re: File Sort

- **From:** Calvin Crumrine <Calvin_Crumrine@dced.state.ak.us>
- **Date:** 2000-11-02T08:07:16-09:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A019F44.A1B9C584@dced.state.ak.us>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com>`

```
Foodman wrote:

> In article <972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk>,
>   "The Tickster" <iain@beakplace.demon.co.uk> wrote:
…[11 more quoted lines elided]…
> Beats me. I wouldn't know where to begin.

<snip>
And I think this says all that needs to be said about Foodman.
```

###### ↳ ↳ ↳ Re: File Sort

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-11-03T07:29:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A026944.3E46FE4D@Azonic.co.nz>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <3A019F44.A1B9C584@dced.state.ak.us>`

```
Calvin Crumrine wrote:
> 
> Foodman wrote:
…[17 more quoted lines elided]…
> And I think this says all that needs to be said about Foodman.

Did anyone give a realistic answer to this question that has drifted off
in many ways ?

I suspect that it may be he didn't have an SD for the filename and was
trying to 'SORT input-file' instead of 'SORT sort-file USING input-file
GIVING output-file'.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 4)_

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-11-02T21:15:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tt75107tg@enews3.newsguy.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <3A019F44.A1B9C584@dced.state.ak.us> <3A026944.3E46FE4D@Azonic.co.nz>`

```
I work in a medium size OS390 shop.  Using an indexed VSAM file to sort, for
the amount of data we handle, for most of our jobs, would be ridiculous.  I
have used DFSort and SyncSort and they are both amazingly fast.  Sorting is
cheap, indeed.  The algorithms in the SORT utilities must be virtually
perfect.  I can sort 4,000,000 500 byte records on a 77-byte key from
virtual tape to virtual tape in about 15 minutes, requiring maybe 1 CPU
minute while 30 other production jobs are running in the background.  I
couldn't imagine even trying to sort this using an indexed file.

I would imagine this would be much different for an online system, or for a
PC environment.  But where I work, SORT is king.

Jeff

----------
In article <3A026944.3E46FE4D@Azonic.co.nz>, Richard Plinston
<riplin@Azonic.co.nz> wrote:


> Calvin Crumrine wrote:
>>
…[25 more quoted lines elided]…
> GIVING output-file'.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 5)_

- **From:** riplin@kcbbs.gen.nz
- **Date:** 2000-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tv52q$rqs$1@nnrp1.deja.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <3A019F44.A1B9C584@dced.state.ak.us> <3A026944.3E46FE4D@Azonic.co.nz> <8tt75107tg@enews3.newsguy.com>`

```
  "Jeff Baynard" wrote:
> I work in a medium size OS390 shop.  Using an
indexed VSAM file to sort, for
> the amount of data we handle, for most of our jobs,
would be ridiculous.  I
> have used DFSort and SyncSort and they are both
amazingly fast.  Sorting is
> cheap, indeed.  The algorithms in the SORT
utilities must be virtually
> perfect.  I can sort 4,000,000 500 byte records on
a 77-byte key from
> virtual tape to virtual tape in about 15 minutes,

It must be nice to have a spare 2 Gigabytes that can
be used as a sort work area, does the sort require an
additional 2 Gb for the output file or can it fold
the output stream back into the work area ?

> requiring maybe 1 CPU
> minute while 30 other production jobs are running
in the background.

Hopefully these too are not concurrently demanding a
few Gigabytes for their work space, or do you really
have infinite resources ?

> I couldn't imagine even trying to sort this using
an indexed file.

Well, no, but could you imagine having a key on that
data ?  Does that data have keyed access in any
sequence ?  If that sort was being done daily then
how much time would it take on a daily average basis
to maintain an existing alternate key (ignoring the
one time cost of initially creating it) ?  Would it
be more than 15 minutes ?

If that sort was being done so that a report of
summary totals only was required (I can't imagine
that you wold produce a printout of every record, nor
that the sort was being done as an end in itself)
then how many individual records would be required to
produce the summary totals ?  How long would it take
to create an ISAM file of _that_ size and apply the
additions to it from each record ?  ie instead of
procucing a file of 2 Gb to be serially read to add
up to produce a summary why not read the original
data and add to a summary index.

Would this take more than or less than 15 minutes ?
If this indexed summary file also had other alternate
keys would it allow other summary reports to be
produced in other ways that would make it easier for
your users ?  Could the users get access to this
summary indexed file to produce reports the way
_they_ want them (using, say, Crystal Reports) ?

> I would imagine this would be much different for an
online system, or for a
> PC environment.  But where I work, SORT is king.

Exactly.  There are many different environments and
different solutions may apply.

It some cases, it seems, there are those who claim
theirs is the best way on the basis that this is the
way they have always done it, and so it shall always
be.



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tv9sa$3rs$1@slb1.atl.mindspring.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <3A019F44.A1B9C584@dced.state.ak.us> <3A026944.3E46FE4D@Azonic.co.nz> <8tt75107tg@enews3.newsguy.com> <8tv52q$rqs$1@nnrp1.deja.com>`

```
<riplin@kcbbs.gen.nz> wrote in message news:8tv52q$rqs$1@nnrp1.deja.com...
>   "Jeff Baynard" wrote:
 <snip>
>
> It must be nice to have a spare 2 Gigabytes that can
…[3 more quoted lines elided]…
>

If there was ever an example of how different the "PC" and "mainframe"
worlds are, this surely is one.  I haven't even heard of a mainframe shop
that would THINK about a mere 2Gigabyes as worth considering - when
evaluating the "resources required" to do something. Why 2G is the "virtual
address space" that is available (for the program - not its data) to every
IBM application since MVS/XA (circa 1984).  To consider this as an important
consideration for "working dasd storage" is almost funny.

Again, I am not saying that applications should be written to be "sloppy" or
waste resources; I am just trying to say that in such environments THIS type
of resource is "cheap" and not particularly important.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 7)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2000-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A03CC18.66F0EBF7@worldnet.att.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <3A019F44.A1B9C584@dced.state.ak.us> <3A026944.3E46FE4D@Azonic.co.nz> <8tt75107tg@enews3.newsguy.com> <8tv52q$rqs$1@nnrp1.deja.com> <8tv9sa$3rs$1@slb1.atl.mindspring.net>`

```
"William M. Klein" wrote:
> 
> <riplin@kcbbs.gen.nz> wrote in message news:8tv52q$rqs$1@nnrp1.deja.com...
…[23 more quoted lines elided]…
>  wmklein <at> ix.netcom.com

I support a small COBOL application of six programs.  It's a weekly
batch job that processes about 115 million records, each 285 bytes in
length.  Call it a 32 gigabyte input file.  We sort this file every
week, which takes about six hours.  Then one program reads each record
and generates about 15,000 summary records.  That step takes about 30-40
minutes.  Then another program prints about two million lines of reports
that are decollated and mailed to a few thousand customers. 

If I were to try to index a whole week's worth of new transactions I
would have some problems, since the file size exceeds VSAM limitations. 
Plus I would need about 40 alternate indexes to handle all the
summarization criteria.

That's not the biggest batch job I've seen.  Another department is
working on a new system that must process 50 to 80 million records a
day.

I think there's a place for SORT.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 6)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i5JM5.1013$h46.85768@nnrp2.sbc.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <3A019F44.A1B9C584@dced.state.ak.us> <3A026944.3E46FE4D@Azonic.co.nz> <8tt75107tg@enews3.newsguy.com> <8tv52q$rqs$1@nnrp1.deja.com>`

```

<riplin@kcbbs.gen.nz

> If that sort was being done so that a report of
> summary totals only was required (I can't imagine
…[8 more quoted lines elided]…
> data and add to a summary index.

Sounds like he came from my old shop.

Once I was asked to create a report and, when given the record layout,
asked: "In what order are these records on the tape?"

"It depends," said the manager, "on what was last done to it.'

Turns out that almost every program (within this system, and not just
'Report' programs) had to start with a sort (or ISAM equivalent) to
get the data in the right order for the program's purposes.

Now of course I, who grew up with the rule: 'Never Sort The Master
File,' was appalled.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 7)_

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tvutd015jn@enews3.newsguy.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <3A019F44.A1B9C584@dced.state.ak.us> <3A026944.3E46FE4D@Azonic.co.nz> <8tt75107tg@enews3.newsguy.com> <8tv52q$rqs$1@nnrp1.deja.com> <i5JM5.1013$h46.85768@nnrp2.sbc.net>`

```


----------
In article <i5JM5.1013$h46.85768@nnrp2.sbc.net>, "Jerry P" 
<jerryp@bisusa.com> wrote:


>
> Sounds like he came from my old shop.
…[4 more quoted lines elided]…
> "It depends," said the manager, "on what was last done to it.'

That is a function of system design, and age, and has nothing to do with
sorting.

>
> Turns out that almost every program (within this system, and not just
> 'Report' programs) had to start with a sort (or ISAM equivalent) to
> get the data in the right order for the program's purposes.

Now, is this so bad?  What's wrong with sorting the data?  Sort/Match/Merge
is the basis of COBOL code and I still stand by it.

>
> Now of course I, who grew up with the rule: 'Never Sort The Master
> File,' was appalled.
>

I bet those 'old' systems are still in production.

Jeff
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 8)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g1UM5.2402$2Y1.216701@nnrp1.sbc.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <3A019F44.A1B9C584@dced.state.ak.us> <3A026944.3E46FE4D@Azonic.co.nz> <8tt75107tg@enews3.newsguy.com> <8tv52q$rqs$1@nnrp1.deja.com> <i5JM5.1013$h46.85768@nnrp2.sbc.net> <8tvutd015jn@enews3.newsguy.com>`

```

"Jeff Baynard" <union27@macconnect.com> wrote in message
news:8tvutd015jn@enews3.newsguy.com...
>

> Now, is this so bad?  What's wrong with sorting the data?
Sort/Match/Merge
> is the basis of COBOL code and I still stand by it.
>

Because there's more data in the world than there is disk (or tape)
storage.

Well, maybe not anymore.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 6)_

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tvued01558@enews3.newsguy.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <3A019F44.A1B9C584@dced.state.ak.us> <3A026944.3E46FE4D@Azonic.co.nz> <8tt75107tg@enews3.newsguy.com> <8tv52q$rqs$1@nnrp1.deja.com>`

```
Very good points.  Read below...

Jeff

----------
In article <8tv52q$rqs$1@nnrp1.deja.com>, riplin@kcbbs.gen.nz wrote:


>   "Jeff Baynard" wrote:
>> I work in a medium size OS390 shop.  Using an
…[14 more quoted lines elided]…
> the output stream back into the work area ?

Don't know.  I have no problem getting UNIT=3390 5,000-10,000 cylinders for
sort work space.  And since I'm writing tape to tape, there are no space
problems (God bless UNIT=TAPE).  A 2 gig sort in our shop is reliable.


>
>> requiring maybe 1 CPU
…[5 more quoted lines elided]…
> have infinite resources ?

No, but using a good tape handling method, like our Virtual Tape (whatever
that means) is very fast and robust.  We have plenty of space in our WORK
dasd pool.  That is our biggest pool.


>
>> I couldn't imagine even trying to sort this using
…[8 more quoted lines elided]…
> be more than 15 minutes ?

I understand what you are saying.  I still insist, that having a jobstep
that performs consistenty, linearly, with the amount of work being processed
is the best way to go.  What if we wanted to do a full refresh on that
indexed file.  How long would that take?  I'm sure someone would get a call
after the job timed-out after 8 hours.  I don't want to get woken up at 4am
because our files won't update.

>
> If that sort was being done so that a report of
…[17 more quoted lines elided]…
> _they_ want them (using, say, Crystal Reports) ?

Well, bottom line is that I work in a batch environment.  It's much better
to have a job that performs consistently.

>
>> I would imagine this would be much different for an
…[14 more quoted lines elided]…
> Before you buy.

There is nothing better than a tight, well written system using VSAM files.
I admit.  But sorting is not something I would want to use an indexed file
for.

Jeff
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 7)_

- **From:** riplin@kcbbs.gen.nz
- **Date:** 2000-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8u2377$20m$1@nnrp1.deja.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <3A019F44.A1B9C584@dced.state.ak.us> <3A026944.3E46FE4D@Azonic.co.nz> <8tt75107tg@enews3.newsguy.com> <8tv52q$rqs$1@nnrp1.deja.com> <8tvued01558@enews3.newsguy.com>`

```
  "Jeff Baynard" <union27@macconnect.com> wrote:

> Very good points.  Read below...

> > keys would it allow other summary reports to be
> > produced in other ways that would make it easier
for
> > your users ?  Could the users get access to this
> > summary indexed file to produce reports the way
> > _they_ want them (using, say, Crystal Reports) ?
>
> Well, bottom line is that I work in a batch
environment.  It's much better
> to have a job that performs consistently.

Do you have any contact with users ?  Or are you
isolated by a stonewall of 'analysts' and 'no men' ?

You may find that some of the users may be taking the
reports and keying the data into access or a
spreadsheet, or even using a spooled version and
reading it into these directly so that they _can_ get
the reports they need.


> > It some cases, it seems, there are those who
claim
> > theirs is the best way on the basis that this is
the
> > way they have always done it, and so it shall
always
> > be.

> Well, bottom line is that I work in a batch
environment.  It's much better
> to have a job that performs consistently.

Did my words ring true then ?  What do your _users_
(the ones that pay the bills) think is 'better' ?
Are they planning a replacement interactive system
that could be web enabled ?



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 8)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-11-05T17:19:44+11:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A04FC00.26142911@zip.com.au>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <3A019F44.A1B9C584@dced.state.ak.us> <3A026944.3E46FE4D@Azonic.co.nz> <8tt75107tg@enews3.newsguy.com> <8tv52q$rqs$1@nnrp1.deja.com> <8tvued01558@enews3.newsguy.com> <8u2377$20m$1@nnrp1.deja.com>`

```
riplin@kcbbs.gen.nz wrote:

>
> Do you have any contact with users ?  Or are you
> isolated by a stonewall of 'analysts' and 'no men' ?

Generally maintenance people have much more direct access than
development.  The job is more reactive,  the users more direct.

> You may find that some of the users may be taking the
> reports and keying the data into access or a
> spreadsheet, or even using a spooled version and
> reading it into these directly so that they _can_ get
> the reports they need.

Is this nessecarily bad?

This happens with all the best intentions on most systems,  it is only
when the person wandering through the section asks what are you doing
this for that it comes to light.   This is where redevelopment wins,
because analysts do focus on the whole process.

Typically niaive users continue to do what they have always done
regardless.   Flexible user driven reporting, through a spreadsheet if
nessecary, is far better than static reports that only present one
picture of the world.

> Did my words ring true then ?  What do your _users_
> (the ones that pay the bills) think is 'better' ?
> Are they planning a replacement interactive system
> that could be web enabled ?

Web enabled is able to be done on the mainframe using the HTML version
of CICS without significant investment.   Why go the whole hog?

I personally believe in the web and web enabled applications however
I really believe there are too many snake oil salesmen telling us the
web is the answer to every ill that software has.    Did my words ring
true to you?

Batch processing is a wonderful tool,   I present and retrieve
information on the web but I crunch behind the scenes in batch.

Ken
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 9)_

- **From:** riplin@kcbbs.gen.nz
- **Date:** 2000-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8u49og$k4a$1@nnrp1.deja.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <3A019F44.A1B9C584@dced.state.ak.us> <3A026944.3E46FE4D@Azonic.co.nz> <8tt75107tg@enews3.newsguy.com> <8tv52q$rqs$1@nnrp1.deja.com> <8tvued01558@enews3.newsguy.com> <8u2377$20m$1@nnrp1.deja.com> <3A04FC00.26142911@zip.com.au>`

```


  waratah@spamcop.net wrote:
>>
> > You may find that some of the users may be taking
the
> > reports and keying the data into access or a
> > spreadsheet, or even using a spooled version and
> > reading it into these directly so that they _can_
get
> > the reports they need.
>
> Is this nessecarily bad?

No, not necessarily.  But it may be if the users
become more interested in developing their own little
systems rather than doing their actual job, and if
this effort is being duplicated in several
departments.

In some cases the users start collecting data
independantly to add to their extracts (I have seen
this happen) with consequent inefficiencies,
duplication of effort and inaccuracies in data.


> Typically niaive users continue to do what they
have always done
> regardless.   Flexible user driven reporting,
through a spreadsheet if
> nessecary, is far better than static reports that
only present one
> picture of the world.

Exactly, but if there is no access to the data
because all the DP department produces is a paper
report each week then users start taking alternate
mechanisms to get this rather than getting on with
what they are paid to do.


> Web enabled is able to be done on the mainframe
using the HTML version
> of CICS without significant investment.   Why go
the whole hog?

While that may allow the existing system and data to
be web enabled it only allows the existing terminal
system to be replicated on a different terminal.
Hardly a great leap forward.

I also don't think that a 15 minute 'sort and report'
is a useful response time to a web based enquirey,
especially when the actual data required may be just
a line or three of the summaries.


> Batch processing is a wonderful tool,   I present
and retrieve
> information on the web but I crunch behind the
scenes in batch.

It seems that some link 'batch processing' with
'serial files, sort and merge' as if it is axiomatic
that batch processing can only be done the way it was
done on mag tapes 30 years ago, and that interactive
access to the data must be excluded by continuing to
hold it as serial transactions.

It that is what the users (who pay for it) want then
there is no problem, but it appears that many just do
it as inaccessible serial files because 'that is how
we do it here' and has been since the system was
designed around boxes of cards.





Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: File Sort

_(reply depth: 10)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IuxN5.36$bb.18693@paloalto-snr1.gtei.net>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk> <8tfqa6$fr1$1@nnrp1.deja.com> <3A019F44.A1B9C584@dced.state.ak.us> <3A026944.3E46FE4D@Azonic.co.nz> <8tt75107tg@enews3.newsguy.com> <8tv52q$rqs$1@nnrp1.deja.com> <8tvued01558@enews3.newsguy.com> <8u2377$20m$1@nnrp1.deja.com> <3A04FC00.26142911@zip.com.au> <8u49og$k4a$1@nnrp1.deja.com>`

```
<riplin@kcbbs.gen.nz> wrote in message news:8u49og$k4a$1@nnrp1.deja.com...
>   waratah@spamcop.net wrote:
>
…[14 more quoted lines elided]…
>

If this application has changed - from 'sort and report' to 'Web Enquiry',
then it seems to me that the database should be changed to support the new
application. (In this case it just means maintaining a couple of summary
datasets/files).

This is a terrific exampple of why I look suspiciously on anything that
sounds like, "what's the best way to convert our code from language A to
language B..." -  it is seldom,,if ever, true that the only change is the
change in the language product.

"Web-enabling a program" is NOT the same thing as "web-enabling an
application."
```

#### ↳ Re: File Sort

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-10-29T00:18:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tfqcn$fru$1@nnrp1.deja.com>`
- **References:** `<972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk>`

```
In article <972743533.12577.0.nnrp-07.d4e45acf@news.demon.co.uk>,
  "The Tickster" <iain@beakplace.demon.co.uk> wrote:
> Can anyone tell me how to do a sort ascending on a file in Micro Focus
> Cobol? This may seem like an easy question but I've only been doing
Cobol
> for a couple of days. I've tried using SORT Filename ASCENDING key,
but the
> compiler keeps saying that the operand must be a table.
>
> Any suggestions?

Hi:

Beats me. I wouldn't know where to begin.

If your boss, teacher, mother-in-law is insisting that you do a
sort for whatever reason, and if you don't do it you're up the
creek, fine. Go ahead and learn how to do it.

However, If I were your teacher, I would tell you to write an ISAM
file instead. The advantages are; it's easier, probably just as fast
although execution time is probably irrelevant; you can build in
a couple of extra keys for convenience or whatever; it can be
accessed in various ways, etc. And, you don't need to know how
to sort. In fact, the advantages are so great that I can't imagine
why anyone would do it any other way.

Of course, you might WANT to know how to sort and that is OK, too.
Remember, only 'Real Programmers' sort.

Thanks

Tony Dilworth




Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
