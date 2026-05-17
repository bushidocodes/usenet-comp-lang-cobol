[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# "GO TO" the most powerful verb in COBOL

_48 messages · 30 participants · 1997-05 → 1997-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### "GO TO" the most powerful verb in COBOL

- **From:** "tea..." <ua-author-801459@usenetarchives.gap>
- **Date:** 1997-05-30T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19970531191401.PAA17715@ladder02.news.aol.com>`

```

GO TO is one of the most powerful verbs in COBOL...when a GO TO is
encountered there is no debate of what to do, or where to go! It is so
powerful in fact that most of your compilers have them Built in!!! Yes,
That's right Built-in... so even if you write a "GO TO" less program it is
riddled with "GO TO"s placed in the program by the compiler. The fact that
you as "programmer" use them allow your program to process faster and use
less CPU time, which used to be very critical.

My COBOL tutor used to tell me about COBOL..."Those who know do, Those who
Don't, TEACH"... he was just called out of retirement to save the
companies' butt.

Now the real issue is are you writing good code??? If your code is good
why are you wasting time??? Writing 6 lines of code to avoid using a "GO
TO" not only wastes time, it's poor programming.

"Even the best chain, is only as good as it's weakest link"


Robert "Diverdown" Titus

He prayeth best, who loveth best all things both great and small; For the dear God who loveth us, He made and loveth all. "Rime of the Ancient Mariner"
```

#### ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "steve wolfe" <ua-author-733217@usenetarchives.gap>
- **Date:** 1997-05-30T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19970531191401.PAA17715@ladder02.news.aol.com>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com>`

```

Teatus wrote:

› Now the real issue is are you writing good code??? If your code is good
› why are you wasting time??? Writing 6 lines of code to avoid using a "GO
› TO" not only wastes time, it's poor programming.

???? I think the problem I have here is that in the greater scheme of
how I spend my day, much more time is spent trying to understand all the
business rules and get firm committments from business partners on
requirements - not on whether or not I write a few more lines of code to
avoid a goto. In my mind, good code isn't nearly as much what I think of
my code as what does someone else think when they pick it up and need to
modify it quickly...

****************************************************************************
email  : prg··.@ep··x.net
url    : http://www.epix.net/â€¾prgsdw
****************************************************************************
```

#### ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1997-05-30T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p3@usenetarchives.gap>`
- **In-Reply-To:** `<19970531191401.PAA17715@ladder02.news.aol.com>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com>`

```

In message <<199··.@lad··l.com>> tea··.@a··.com writes:
[GO TO]
› encountered there is no debate of what to do, or where to go! It is so

Exactly. However at the paragraph label that is required to be
the target of the GO TO there may be considerable 'debate' of
how this position was arrived at.

Certainly when one sees:

[......]
GO TO random-paragraph-name
[.....]

it is blindingly obvious what is happening. However when one sees:

A-SIMPLE-LABEL.
[some code relating to problem].
ANOTHER-SIMPLE-LABEL.
[somemore code related to problem].

it is not easy to see how 'some code' relates to 'somemore'.
Some examples of code that may exist anywhere in the program:

GO TO A-SIMPLE-LABEL (with drop down into ANOTHER-.)
GO TO ANOTHER-SIMPLE-LABEL
PERFORM A-SIMPLE-LABEL
PERFORM ANOTHER-SIMPLE-LABEL

If code needs to be changed in these areas then it is necessary
to determine *every* path through this code and this will
require a search of the entire program for these possibilities.

GO TO is the simplest and most powerful way to make a program
unmaintainable.

Of course many site standards restrict the ways in which programs
are allowed to be constructed (eg only ever GO TO an EXIT-paragraph)
so that these issues can be easily resolved.
›
› Now the real issue is are you writing good code??? If your code is good
› why are you wasting time??? Writing 6 lines of code to avoid using a "GO
› TO" not only wastes time, it's poor programming.

Well that has just set back the art of programming 25 years.

I never write '6 lines of code to avoid a GO TO'. I use a style
where GO TOs are unnecessary, and 'extra' code to avoid then is
unnecessary too.
```

#### ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "d.s..." <ua-author-6569161@usenetarchives.gap>
- **Date:** 1997-05-31T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p4@usenetarchives.gap>`
- **In-Reply-To:** `<19970531191401.PAA17715@ladder02.news.aol.com>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com>`

```

On 31 May 1997 19:14:11 GMT, tea··.@a··.com (Teatus) wrote:

› GO TO is one of the most powerful verbs in COBOL...when a GO TO is
› encountered there is no debate of what to do, or where to go! It is so
…[19 more quoted lines elided]…
› He prayeth best, who loveth best all things both great and small; For the dear God who loveth us, He made and loveth all.                                      "Rime of the Ancient Mariner"

Obviously, 'powerful' is a relative term. I would identify the
PERFORM statement, EVALUATE statement, CONTINUE statement, and COMPUTE
statements as more powerful. After all, they control logic. The GOTO
is just a simple branch of no meaning and no value added. Yes, it's
direct and it works -- but so does the MOVE statement. If you
investigate the design approaches that make the GOTO undesirable, I
think you may change your thoughts. The only statement I can think of
that is as dangerous as GOTO is PERFORM---THRU.
david

David d.s··.@ix.··m.com
____________________________________
```

#### ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "alex romaniuk" <ua-author-5783842@usenetarchives.gap>
- **Date:** 1997-06-02T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p5@usenetarchives.gap>`
- **In-Reply-To:** `<19970531191401.PAA17715@ladder02.news.aol.com>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com>`

```

Teatus wrote:
› 
› GO TO is one of the most powerful verbs in COBOL...when a GO TO is
…[19 more quoted lines elided]…
› He prayeth best, who loveth best all things both great and small; For the dear God who loveth us, He made and loveth all.                                      "Rime of the Ancient Mariner"

Hi !

I agree, that GO TO statement is not a good example of powerfull
programming, but I use it
sometimes, when I need a fast execution routine, since PERFORM and
EVALUATE is much slower than
GO TO.

Example : Slower Faster
EVALUATE X GO TO A B C DEPENDING ON X
WHEN 1 PERFORM A
WHEN 2 PERFORM B
WHEN 3 PERFORM C
END-EVALUATE

Alex
```

##### ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "danny knaepen" <ua-author-17071640@usenetarchives.gap>
- **Date:** 1997-06-02T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p5@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap>`

```

Alex Romaniuk wrote:

› 
› Hi !
…[14 more quoted lines elided]…
› Alex

Alex,

I'm interested in knowing how much faster this executes. Can you give me
some idea ?

Danny
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "binyami..." <ua-author-932190@usenetarchives.gap>
- **Date:** 1997-06-03T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p6@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p6@usenetarchives.gap>`

```

On Tue, 03 Jun 1997 20:44:41 +0000 Danny Knaepen wrote:

:>Alex Romaniuk wrote:

:>> I agree, that GO TO statement is not a good example of powerfull
:>> programming, but I use it
:>> sometimes, when I need a fast execution routine, since PERFORM and
:>> EVALUATE is much slower than
:>> GO TO.

:>> Example : Slower Faster
:>> EVALUATE X GO TO A B C DEPENDING ON X
:>> WHEN 1 PERFORM A
:>> WHEN 2 PERFORM B
:>> WHEN 3 PERFORM C
:>> END-EVALUATE

:>> Alex

:>Alex,

:>I'm interested in knowing how much faster this executes. Can you give me
:>some idea ?

Danny,

A GOTO will run faster than a PERFORM. A GOTO does not require linkage thus
the routine A (or B or C) will not have to save the return information. I
really should do a compile with PMAP (or whatever it is called now) but I
would expect a GOTO DEPENDING would use a branch table thus the worst case of
invoking C would be a lot shorter path, perhaps as:

L Rx,X
SLL Rx,2
L Rx,branch_table-4(Rx)
BR Rx


while the PERFORM would (besides not faulting if X is neither 1, 2 or 3)
require:

CLC X,=F'1'
BNE skip1
BAL Rx,A
B end_evaluate
skip1 CLC X=F'2,
.
.
.

as well as entry logic in A, B and C

ST Rx,return_address

Of course, this entire issue is academic, as if there is a need to shorten the
code path, one should not be using COBOL. One would use assembler in such a
time critical application.

:>Danny
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 4)_

- **From:** "danny knaepen" <ua-author-17071640@usenetarchives.gap>
- **Date:** 1997-06-03T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p7@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p6@usenetarchives.gap> <gap-5c8eb7b1a0-p7@usenetarchives.gap>`

```

Binyamin Dissen wrote:
› 
› On Tue, 03 Jun 1997 20:44:41 +0000 Danny Knaepen  wrote:
…[24 more quoted lines elided]…
› Director, Dissen Software, Bar & Grill - Israel

Binyamin,

Thank you for your explanation, but what I was really interested in was to here (read) from Alex how much
faster it runs, so that I would have an idea if this gain in speed is really worthwile, and not academic as you
suggest (and I suspect).

Danny
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "j.s." <ua-author-88615@usenetarchives.gap>
- **Date:** 1997-06-04T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p6@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p6@usenetarchives.gap>`

```

Add 1 to BARFO always worked for me...
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "spa..." <ua-author-17072047@usenetarchives.gap>
- **Date:** 1997-06-04T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p6@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p6@usenetarchives.gap>`

```

I always thought that the results from a misplaced STOP RUN were
pretty powerful.

George Trudeau, gtrudeau at cape dot com
```

##### ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "curtis bass" <ua-author-9633319@usenetarchives.gap>
- **Date:** 1997-06-03T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p5@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap>`

```

Alex Romaniuk wrote:

-- snip --

› Hi !
› 
…[13 more quoted lines elided]…
› Alex

EVALUATE is "much slower" than GO TO? Perhaps. How much is "much?" A
hundred nanoseconds as opposed to ten? At such speeds, how much
difference does it make? Processing seven hundred thousand records takes
two hours and ten minutes instead of two hours and three minutes?

Also, your comparison isn't valid; the EVALUATE has a return mechanism
and the GO TO doesn't. After paragraph A (or B or C) is finished
executing, control returns to the statement following END-EVALUATE. Not
so with the GO TO. In that case, execution goes to Heaven knows where,
and that has been the bane of GO TOs since Day One.

Curtis
```

##### ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1997-06-03T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p5@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap>`

```

Alex Romaniuk wrote:
› 
 
› I agree, that GO TO statement is not a good example of powerfull
› programming, but I use it
…[9 more quoted lines elided]…
›                 END-EVALUATE

You are quite wrong for many compilers. It all depends on the
implementation. If the items in the WHEN were GO TOs, some compilers
would take such an EVALUATE and transform it into exactly the same
code as the GO TO DEPENDING ON. Also, both statements are not at all
equivalent. If you use the GO TO DEPENDING ON and want to get back
you have to have some mechanism in A, B, and C to do so. Probably
with a GO TO. This would probably take more time. However, the
supposed efficiency is so tiny that I really doesn't make much
difference. It is better to write code that can be read easily than
to try to save a microsecond here or there.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
No clever quotes here
```

##### ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "jim konert" <ua-author-10238491@usenetarchives.gap>
- **Date:** 1997-06-04T20:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p5@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap>`

```

Hi Wiley,
It is interesting that you should mention that the initialize is
inefficient on large tables. I was taught a method many years ago that
is amazing in its simplicity. Please no flames out there on how this
won't work, try it first. I have tried this method on three mainframe
compilers and it worked on all three.
code follows:

01 Table-values.
05 Filler pic x(10) value spaces.
05 Filler pic s9(8) comp value zeros.
05 Filler pic s9(7) comp-3 value zeros.
05 Table-initialize pic x(1800).
05 Table-definition redefines Table-initialize.
10 Table-array occurs 100 times
indexed by Table-index.
15 Table-text pic x(10).
15 Table-pointer pic s9(8) comp.
15 Table-counter pic s9(7) comp-3.

The table is initialized with the following statement.
MOVE TABLE-VALUES TO TABLE-INITIALIZE.

In the compile, this creates an assembler MVCL (move character long).
A compile tiome comment is also generated, but may be ignored. I can't
tell you how many bets I've won with System Programmers who said that
this would never work. But it does.
I've never tried this on a non-mainframe compiler, so I don't know if
they would handle the code the same.

Jim Konert
EDS/SLRSC/ Earthgrains

It isn't necessary to imagine the world ending in fire or ice -- there
are two other possibilities: one is paperwork, and the other is
nostalgia.
Frank Zappa (1940-1993)
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-06-04T20:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p13@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p13@usenetarchives.gap>`

```



Jim Konert wrote in article <339··.@e··.com>...
› Hi Wiley,
› It is interesting that you should mention that the initialize is
…[20 more quoted lines elided]…
› 
I take it back. It does work and it works well. This is because all
moves at the group level are from left to right and thus what you just
populated the item with is what will be moved next.

Thanks for the neat tip! I've been showing the guys here things I have
learned on the news group - calling them "stupid Cobol Tricks". I really
like this one - although it is not really "clear" at first - I would use
initialize unless performance becomes a real consideration - and if
initialize is slow in the particular environment.
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 4)_

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1997-06-04T20:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p14@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p13@usenetarchives.gap> <gap-5c8eb7b1a0-p14@usenetarchives.gap>`

```

Thane Hubbell wrote:
› 
›  >....
…[11 more quoted lines elided]…
› initialize is slow in the particular environment.


It may work now but may not work on the next system. This is called
an overlapping move operation and according to the standard all bets
are off. The standard says the results are undefined. You may find
that on many systems (especially risc systems) you will end up with
garbage. This is even more likely if the elements are quite small.
Even if it is fast, you are taking a big risk (or risc as the case may
be). Many compilers generate similar code for the INITIALIZE
statement. Since they know how the machine works, there will never be
a problem.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
No clever quotes here
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 5)_

- **From:** "r..." <ua-author-43843@usenetarchives.gap>
- **Date:** 1997-06-05T20:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p15@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p13@usenetarchives.gap> <gap-5c8eb7b1a0-p14@usenetarchives.gap> <gap-5c8eb7b1a0-p15@usenetarchives.gap>`

```

In article <339··.@tan··m.com> nel··.@tan··m.com "Don Nelson" writes:
› [re: overlapping MOVE instead of INITIALIZE]
› It may work now but may not work on the next system...
› Many compilers generate similar code for the INITIALIZE statement.
› Since they know how the machine works, there will never be a problem.

Don's answer applies to all attempts to outthink the compiler -
the effort spent in tricky COBOL coding (which makes maintenance
and conversion more difficult) would be better spent in persuading
the compiler writers to improve the compiler itself.

Richard Ross-Langley        +44 1727 852 801
Mine of Information Ltd, PO BOX 1000, St Albans AL3 5NY, GB
* Independent Computer Consultancy    Established in 1977 *
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 4)_

- **From:** "charles f hankel" <ua-author-1885209@usenetarchives.gap>
- **Date:** 1997-06-06T20:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p14@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p13@usenetarchives.gap> <gap-5c8eb7b1a0-p14@usenetarchives.gap>`

```

This is a multi-part message in MIME format.
--------------E373D699DC223CFBDDF2C1BA
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit

Thane Hubbell wrote:

› Jim Konert  wrote in article
› <339··.@e··.com>...
…[9 more quoted lines elided]…
› 
 
› I take it back.   It does work and it works well.  This is because
› all
› moves at the group level are from left to right and thus what you
› just
› populated the item with is what will be moved next.

Strangely enough, I had to explain this principle, of rolling a value
along the line, to a couple of younger chaps the other day, and they
were most impressed - once they understood it. It's good to
demonstrate that the old fart hasn't lost it completely. As with
jokes, the old ones are the best.

Actually it's all _character_ moves are left to right and because a
group-level move happens to be a character move that it works at that
level. The shorter initialisations (under 256 bytes) generate an MVC
(even more efficient). Before we had the MVCL instruction, it ised to
generate a series of MVCs which can, to a point, be more efficient
than the MVCL.

How do we describe this, though? Is it a trick or is a programming
technique? Personally, I think it is a technique that demonstrates an
understanding of how systems actually do things, rather than a trick
which shows what a clever-dick you are. I would think that most of us
who have been doing the job for many years learned this one quite
early on.

I have used this away from IBM mainframes with a similar degree of
success (AS/400, B-6500, B-7700, Honeywell 6000's, Tandem TNS,
HP-3000). As with Jon, I would not like to guarantee that it works on
every single compiler on every single system out there but I am always
willing to give it a go. It's also not private to COBOL since we used
it all the time in Assembler and PL/1 stuff. After all, if it does
the job, it is far more efficient than INITIALIZE.

Charles

--------------E373D699DC223CFBDDF2C1BA
Content-Type: text/x-vcard; charset=us-ascii; name="vcard.vcf"
Content-Transfer-Encoding: 7bit
Content-Description: Card for Charles Hankel
Content-Disposition: attachment; filename="vcard.vcf"

begin: vcard
fn: Charles Hankel
n: Hankel;Charles
org: Freedom Bird Ltd
adr: 38 Borough Way;;;Wallasey;Merseyside;L44 6QU;United Kingdom
email;internet: cha··.@han··o.uk
title: Director
tel;work: 0151-639 9839
tel;fax: 0151-200 1957
x-mozilla-cpt: ;0
x-mozilla-html: FALSE
end: vcard


--------------E373D699DC223CFBDDF2C1BA--
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 5)_

- **From:** "r..." <ua-author-43843@usenetarchives.gap>
- **Date:** 1997-06-07T20:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p17@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p13@usenetarchives.gap> <gap-5c8eb7b1a0-p14@usenetarchives.gap> <gap-5c8eb7b1a0-p17@usenetarchives.gap>`

```

In article <339··.@han··o.uk>
› cha··.@han··o.uk "Charles F Hankel" writes:
› [overlapping MOVE statement]
› ..if it does the job, it is far more efficient than INITIALIZE.

If the overlapping MOVE does *not* do the job, now or in the future,
it is not only less efficient it is not even correct. A company
with too many lawyers (NOT ZERO :-) might even sue the programmer.

The INITIALIZE verb emits code that always works correctly. It may
also result in very efficient code, as good as or better than your
assembly-oriented hand coded MOVE. What if your mainframe single
CPU were replaced by a parallel array of 100x100 processors?

Richard Ross-Langley        +44 1727 852 801
Mine of Information Ltd, PO BOX 1000, St Albans AL3 5NY, GB
* Independent Computer Consultancy    Established in 1977 *
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 5)_

- **From:** "jeff" <ua-author-939205@usenetarchives.gap>
- **Date:** 1997-06-09T20:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p17@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p13@usenetarchives.gap> <gap-5c8eb7b1a0-p14@usenetarchives.gap> <gap-5c8eb7b1a0-p17@usenetarchives.gap>`

```

Charles F Hankel wrote:

› How do we describe this, though?  Is it a trick or is a programming
› technique?  Personally, I think it is a technique that demonstrates an
…[12 more quoted lines elided]…
› 
In the dim and distant 60s when I was learning my craft, this was
known as a "sliding move", I was shown it by my chief programmer,
who explained how it worked on the machine that we had, explained how
it was not always going to work on other compilers and or machines,
and then threatened to sack me if he ever caught me using it!
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 6)_

- **From:** "charles f hankel" <ua-author-1885209@usenetarchives.gap>
- **Date:** 1997-06-12T20:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p19@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p13@usenetarchives.gap> <gap-5c8eb7b1a0-p14@usenetarchives.gap> <gap-5c8eb7b1a0-p17@usenetarchives.gap> <gap-5c8eb7b1a0-p19@usenetarchives.gap>`

```

Jeff York wrote:
› 
› Charles F Hankel  wrote:
…[13 more quoted lines elided]…
› 
OK you can tell us the truth, now. Was this like the experience of Dad
showing you how to use the car and telling you never to go over 30 mph?
So did you use it, even just the once? You can tell us in confidence
because we're all balanced, rational people out here.

Charles

=====================================================
Thus writes the virtual quill pen of Charles F Hankel
Dat veniam corvis, vexat censura columbas - Juvenal
=====================================================
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 6)_

- **From:** "jim konert" <ua-author-10238491@usenetarchives.gap>
- **Date:** 1997-06-12T20:00:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p19@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p13@usenetarchives.gap> <gap-5c8eb7b1a0-p14@usenetarchives.gap> <gap-5c8eb7b1a0-p17@usenetarchives.gap> <gap-5c8eb7b1a0-p19@usenetarchives.gap>`

```

› 
› Charles F Hankel  wrote:
…[3 more quoted lines elided]…
›› understanding of how systems actually do things, 
 
›› (snip)
 
›› I have used this away from IBM mainframes with a similar degree of
›› success (AS/400, B-6500, B-7700, Honeywell 6000's, Tandem TNS,
›› HP-3000).  
 
›› (snip )
››  It's also not private to COBOL since we used
…[3 more quoted lines elided]…
› -
Amazing I started this part of the discussion last week and its still
going strong. First let me state that I only used this method on
large tables when coding COBOLI. I have never used it in COBOLII,
never needed too (except as a test to see if it would work).
I agree with Mr Hankel, this is a technigue that takes advantage of
how a system works, rather than a *trick* as others believe.
Notice that Mr. Hankel has used this on multiple platforms and
compiler's, and it worked on all. That should indicate some
level of portability that is not always available, even for documented
features!
While I did not know it wopuld work in PL/1, I always assumed it would
work in Assy, since the compiler actually generated an MVCL (move
character long).
I have seen many *tricks* in COBOL including -fall through - logic,
undocumented use of working storage variables to -trick- the logic, ad
nauseum.


Jim Konert
EDS/SLRSC/ Earthgrains

It isn't necessary to imagine the world ending in fire or ice -- there
are two other possibilities: one is paperwork, and the other is
nostalgia.
Frank Zappa (1940-1993)
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 5)_

- **From:** "curtis bass" <ua-author-9633319@usenetarchives.gap>
- **Date:** 1997-06-11T20:00:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p17@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p13@usenetarchives.gap> <gap-5c8eb7b1a0-p14@usenetarchives.gap> <gap-5c8eb7b1a0-p17@usenetarchives.gap>`

```

Charles F Hankel wrote:

-- snip --

› How do we describe this, though?  Is it a trick or is a programming
› technique?  Personally, I think it is a technique that demonstrates an
› understanding of how systems actually do things, rather than a trick
›                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
› which shows what a clever-dick you are.

I must respectfully disagree; I consider this a trick, pure and simple.
The reason why is underlined above; it demonstrates an understanding of
*how a particular platform or implementation* does things, and this does
*not* generalize to all systems or platforms. Therefore, one cannot rely
on this trick to work on all systems. This, in addition to the fact that
it simply requires head-scratching to determine what in blazes is going
on (assuming that it works in the first place) is why I believe it
should be avoided.

I prefer simple, straight-forward code that does what it says.

-- snip --

Curtis
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "j.s." <ua-author-88615@usenetarchives.gap>
- **Date:** 1997-06-04T20:00:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p23@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p13@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p13@usenetarchives.gap>`

```

You are better off using an assembler module to the following code. You
can do it by exchanging registers alot eaiser. MUCH FASTER
Jim Konert wrote in article <339··.@e··.com>...
› Hi Wiley,
› It is interesting that you should mention that the initialize is
…[36 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-06-04T20:00:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p24@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p13@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p13@usenetarchives.gap>`

```



Jim Konert wrote in article <339··.@e··.com>...
› 
› 01  Table-values.
…[13 more quoted lines elided]…
› 

This will initialize the first element of the table fine, but all others
will have spaces in them.
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 4)_

- **From:** "alan russell" <ua-author-1025782@usenetarchives.gap>
- **Date:** 1997-06-04T20:00:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p25@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p24@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p13@usenetarchives.gap> <gap-5c8eb7b1a0-p24@usenetarchives.gap>`

```

Results of this depend on the type of computer/compiler being used. The
sending and receiving fields overlap (one is 1818 bytes, the other is
1800). If the assembler code generated from this moves one byte at a time
1800 times (the length of the receiving field is shorter) then by the time
you move byte 19 of the sending field it will have been filled from byte 1
because of the overlap and the 18 bytes will continue to cascade down. But
if you do the equivalent of a "move long" where intermediate results may be
elsewhere then you may end up with the first 18 bytes of the receiving
field being populated and the remaining 1782 [1800-18] being populated with
the original first 1782 bytes of the uninitialized table entries.

Moral -- don't use this technique. That's what the INITIALIZE verb is for,
and if you aren't using COBOL 85 then upgrade to it.
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 5)_

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-06-05T20:00:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p26@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p25@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p13@usenetarchives.gap> <gap-5c8eb7b1a0-p24@usenetarchives.gap> <gap-5c8eb7b1a0-p25@usenetarchives.gap>`

```



Alan Russell wrote in article
<01bc71e4$c3e6db60$8d2··.@RUS··i.com>...
› Moral -- don't use this technique. That's what the INITIALIZE verb is
› for,
› and if you aren't using COBOL 85 then upgrade to it.

Actually, I agree. I just didn't state it clearly. Anytime your code
could be ported to another platform (in todays world thats any time!) you
should try to think about that up front. Obviously when you change
compilers, you will probably have to change select statements, but the
actual CODE should still work. If you take advantage of "tricky" and
"questionable" functions of a particular compiler and implimentation, you
are taking a risk. It may actually be worth it, if the plusses outweigh
the minuses, but I would sure comment the heck out of it.
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 4)_

- **From:** "glenn gordon" <ua-author-6588862@usenetarchives.gap>
- **Date:** 1997-06-09T20:00:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p27@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p24@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p13@usenetarchives.gap> <gap-5c8eb7b1a0-p24@usenetarchives.gap>`

```



Thane Hubbell wrote in article
<01bc71dd$054ee960$f0752581@thane-hubbell>...
› 
› 
…[19 more quoted lines elided]…
› will have spaces in them.

Nope, will give a compile warning for overlaping move. When you move
Table-Values to Table-Initialize you are in essence moving an initialized
(by value clause) index '0' (the filler items) to element 1. So when the
move gets to element 1, it has been initialized in the source string and
moves it to the target, initializing index 2 in itself, which ends up in
index 2 of the target, initializing element 3 in the source, etc.

The storgage overlaps, the move ends up repeating the stuff between
Table-Values and Table Initialize in Table-Initialize.

Clever, obscure, compiler implementation dependent, and I'd never let into
production! A one time initialize in a program is no big deal. If you
need to do it more than once, like between every record for some unknown
reason, then trade memory for time. Put in two of the tables, one dummy
and the real one. Initialize the dummy. Whenever you need to initialize
the real table, move the group level of the dummy to the group level of the
real one.

Better yet, don't write programs that require more than one initialization
of a table in a run, or at least not in a low-level loop. It is not very
difficult to do.

gg
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "curtis bass" <ua-author-9633319@usenetarchives.gap>
- **Date:** 1997-06-06T20:00:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p28@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p13@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p13@usenetarchives.gap>`

```

Jim Konert wrote:
› 
› Hi Wiley,
…[5 more quoted lines elided]…
› code follows:
 
› -- [Code and explanation deleted] --
 
› I've never tried this on a non-mainframe compiler, so I don't know if
› they would handle the code the same.
…[3 more quoted lines elided]…
› EDS/SLRSC/ Earthgrains

Yes, it may have worked on three mainframe systems, but there's no
guarantee that it will work *on any system* -- your admission that you
don't know whether it will work outside of the mainframe environment is
a clue to it unreliability. This kind of "trick programming" died years
ago, or it should have. This technique, in fact, should *not* work on a
mainframe either.

This type of passe "trick" programming leads to code that's difficult to
debug and maintain, and many such "tricks" have been done using the GO
TO. I prefer code that's direct in its simplicity, meaning and purpose.
The code should do what it says it's going to do; it should not rely on
hidden, compile-time side effects that may or may not occur on a given
platform.

Curtis
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 4)_

- **From:** "curtis bass" <ua-author-9633319@usenetarchives.gap>
- **Date:** 1997-06-06T20:00:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p29@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p28@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p13@usenetarchives.gap> <gap-5c8eb7b1a0-p28@usenetarchives.gap>`

```

Curtis Bass wrote:

-- snip --

› This technique, in fact, should *not* work on a
› mainframe either.

Oops. I spoke too soon. There is no inherent reason why this shouldn't
work, but it does make assumptions that may be invalid on a given
platform. I recant this one statement, but stand by the remainder of my
post.

Curtis
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "nos..." <ua-author-17071789@usenetarchives.gap>
- **Date:** 1997-06-08T20:00:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p30@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p13@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap> <gap-5c8eb7b1a0-p13@usenetarchives.gap>`

```

Jim Konert wrote:

› Hi Wiley,
› It is interesting that you should mention that the initialize is
…[4 more quoted lines elided]…
› code follows:
 
› 01  Table-values.
›    05  Filler                pic x(10) value spaces.
…[8 more quoted lines elided]…
›            15  Table-counter pic s9(7) comp-3.
 
› The table is initialized with the following statement.               
› MOVE TABLE-VALUES TO TABLE-INITIALIZE.
 
› In the compile, this creates an assembler MVCL (move character long).
› A compile tiome comment is also generated, but may be ignored.  I can't
…[4 more quoted lines elided]…
› -- 
It certainly doesn't work on a Digital Alpha (RISC) running DEC COBOL,
and I didn't expect it to either. The last time I waded through all 90
or so "notes" on the MOVE verb I remember that it said that
overlapping operands are moved as if there were 2 separate moves -- a
move from the source to an intermediate field, then the intermediate
field to the final result. And that's what it did.

I wish we would quit trying to outguess the compiler. Does the
compiler really have to use move instructions that work from left to
right? Honeywell-200 COBOL sure didn't.

George Trudeau, gtrudeau at cape dot com
Programmer/Analyst for the Town of Falmouth, MA

"Currently on vacation, but annoyed enough to dial in to the Alpha and
try the code, which is what I'll grudgingly admit is what this group
is about -- try it, share it, learn, and... oh yes and MAKE $30,000 A
SECOND! THIS IS NOT A CHAIN LETTER..."
```

##### ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "charles f hankel" <ua-author-1885209@usenetarchives.gap>
- **Date:** 1997-06-05T20:00:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p31@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p5@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p5@usenetarchives.gap>`

```

This is a multi-part message in MIME format.
--------------E86E3FDF60AFC8C7F4615093
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit

Alex Romaniuk wrote:

› Teatus wrote:
›› 
…[19 more quoted lines elided]…
› 
Assuming that A, B and C are consecutive paragraphs (it's always
dangerous to assume, surely GO TO A is the fastest way there. Of
course, you don't mention anything about getting back, but then you
may not want to.

Charles

--------------E86E3FDF60AFC8C7F4615093
Content-Type: text/x-vcard; charset=us-ascii; name="vcard.vcf"
Content-Transfer-Encoding: 7bit
Content-Description: Card for Charles Hankel
Content-Disposition: attachment; filename="vcard.vcf"

begin: vcard
fn: Charles Hankel
n: Hankel;Charles
org: Freedom Bird Ltd
adr: 38 Borough Way;;;Wallasey;Merseyside;L44 6QU;United Kingdom
email;internet: cha··.@han··o.uk
title: Director
tel;work: 0151-639 9839
tel;fax: 0151-200 1957
x-mozilla-cpt: ;0
x-mozilla-html: FALSE
end: vcard


--------------E86E3FDF60AFC8C7F4615093--
```

#### ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "bi..." <ua-author-8405640@usenetarchives.gap>
- **Date:** 1997-06-07T20:00:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p32@usenetarchives.gap>`
- **In-Reply-To:** `<19970531191401.PAA17715@ladder02.news.aol.com>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com>`

```

In article <199··.@lad··l.com>,
tea··.@a··.com (Teatus) wrote:
› GO TO is one of the most powerful verbs in COBOL...when a GO TO is
› encountered there is no debate of what to do, or where to go! It is so
…[19 more quoted lines elided]…
› He prayeth best, who loveth best all things both great and small; For the 
dear God who loveth us, He made and loveth all.
"Rime of the Ancient Mariner"

Hi Robert,

I would never have guessed that GO TO was the most "powerful" verb in COBOL.
I would have volunteered SORT because you can write a useful program that
replaces dozens - maybe hundreds - of lines of COBOL code with just one SORT
statement. My definition of "powerful" means "capable of doing a lot with
minimal effort on my part" - all a GO TO does is change the order of statement
execution. PERFORM, IF, CALL, and EVALUATE all do that and more.

Hmmm, let's see if we can deduce what "powerful" means to you. "no debate on
what to do, where to go" ... "most compilers have them built in" ... "programs
riddled with" - you mean "a basic function that all programs must do"! In
which case, you are ABSOLUTELY WRONG!!! I can write a simple (but
non-trivial) program with either a PERFORM or a GO TO - just MOVEs, INSPECTs,
COMPUTEs, etc. in one paragraph. So not every program has "GO TO" logic.

But, Robert, do you remember the ONE function ALL programs must perform (hint:
stub program). That's right, all programs must have a "return" mechanism - a
STOP RUN, GOBACK, or EXIT PROGRAM (or CICS RETURN, etc.). Before you claim
that this is another "GO TO", note these differences:

1) the purpose of the statement is different; the program is terminating and
returning control to the calling program, not just executing different
instructions.
2) there is probably significant "hidden" instructions, such as restoring
registers, checking/closing files, etc.
3) The address of the "branch instruction" is determined by the calling
program or operating system, not the compiler/program.

This CALL and RETURN mechanism would seem to me to be the only "instructions"
that are absoluting necessary for any application program. If a program
does nothing else, it has to return to the "caller". NOTE: I said application
not system program, where some things never "die". Certainly, it is as clear
in meaning as GO TO and more necessary. So CALL/STOP RUN/GOBACK/EXIT PROGRAM
is more "powerful" that GO TO ... oh wait! (russling of pages from language
reference manual) ... HERE IT IS!!! P-E-R-F-O-R-M!! IT does the same
function; link to a paragraph (module) of instructions and return!! WOW,
maybe I can use this MOST POWERFUL verb - what about you, Robert? Or do you
prefer that 98lb weakling named GO TO?
```

#### ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "steveo" <ua-author-31016@usenetarchives.gap>
- **Date:** 1997-06-20T20:00:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p33@usenetarchives.gap>`
- **In-Reply-To:** `<19970531191401.PAA17715@ladder02.news.aol.com>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com>`

```

Teatus wrote:
›
› GO TO is one of the most powerful verbs in COBOL...
[snip]

In my 15 plus years in the industry I have been involved in
*many* hiring decisions. In all those years, no strong advocate
of GOTOs in *ANY* language (other than assembler) was hired.

Draw your own conclusions.
```

##### ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "tim nicholson" <ua-author-6589242@usenetarchives.gap>
- **Date:** 1997-06-22T20:00:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p34@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p33@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p33@usenetarchives.gap>`

```

I have been in the COBOL industry for 7 years working on other people's
code and developing my own. I have seen more uses of GO TO than I care to
mention. I use GO TO in my code. I feel it is a useful tool when used
correctly.

My COBOL professor in college was a strong advocate against the use of GO
TO. He would fail you for using GO TO. That is not only ridiculous, but
also plain dumb. I have been following this post off and on for a month
now, and I have seen several points made where a company would or would not
hire you based on your coding form. I would NEVER work for any shop that
forced me to follow a set form for coding. I feel coding (in any language)
is like writing a book. Every author has his own style. So long as the
code is understandable I don't have a problem with the coding method.
***********************************************************
Timothy Nicholson
Programmer/Analyst
Intelligent Information Systems
Durham, NC
***********************************************************

SteveO  wrote in article
<33A··.@pac··l.net>...
> Teatus wrote:
> > 
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "mike rochford" <ua-author-959623@usenetarchives.gap>
- **Date:** 1997-06-23T20:00:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p35@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p34@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p33@usenetarchives.gap> <gap-5c8eb7b1a0-p34@usenetarchives.gap>`

```

Tim Nicholson wrote:
› 
› I have been in the COBOL industry for 7 years working on other people's
…[19 more quoted lines elided]…
› 

Tim

Although I agree with your comments about the GO TO statement, I cannot
endorse what you say about coding standards. A set of coding standards
is essential for the following reasons.

1. Maintainability. It is far easier to follow a standardised logic
structure and paragraph / field naming structures than trying "to get in
to the programmers mind" before attempting to de-bug or enhance a
program.

2. Ease of Use. Each screen or user prompt has to "look and feel"
similar to others in an application. The keys used to update and delete
need to be the same. the layout of the screen has to look similar .....
This leads to an application that the users can easily understand and
use.

I not saying that each program has to be audited by a comittee to make
sure that it conforms to standards, but rather that a set of guidelines
must be laid down as to how programmers should go about writing a
program.

Mike.
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 4)_

- **From:** "support" <ua-author-179186@usenetarchives.gap>
- **Date:** 1997-06-23T20:00:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p36@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p35@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p33@usenetarchives.gap> <gap-5c8eb7b1a0-p34@usenetarchives.gap> <gap-5c8eb7b1a0-p35@usenetarchives.gap>`

```

Mike Rochford wrote:
› 
› Tim Nicholson wrote:
…[45 more quoted lines elided]…
› Mike.

Hi Mike,

I'd like to say that from a COBOL support desk view, I completely agree
with your comments.

We often recieve testcases from organisations when they have problems.
When 'common sense' standards were applied to the program's coding, we
can pick up the testcases and give fast efficient service. However, I
am continually amazed at some of the programs we receive. Admittedly,
some of the programs originate from days when COBOL was not so good at
assisting programmers to create easy-to-follow programs, but even so,
this can be no excuse.

Go Tos should be used sparingly and Perform Thrus should be sent to the
sin bin. In general, I believe that Go Tos should only be used for
exception and error handling and should only go to a paragraph at the
bottom of a section for processing the condition before exiting.

Gerald

PS Thanks in advance for easy to follow code if you need to send a
testcase!
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "kiy..." <ua-author-598721@usenetarchives.gap>
- **Date:** 1997-06-23T20:00:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p37@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p34@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p33@usenetarchives.gap> <gap-5c8eb7b1a0-p34@usenetarchives.gap>`

```

In <01bc801a$bdbe4680$9d9··.@W95··S.COM>, "Tim Nicholson" writes:
› I have been in the COBOL industry for 7 years working on other people's
› code and developing my own.  I have seen more uses of GO TO than I care to
› mention.  I use GO TO in my code.  I feel it is a useful tool when used
› correctly.  

Goto's have their uses. I generally don't use them but I don't
object to their sparing use.

› SteveO  wrote in article
› <33A··.@pac··l.net>...
…[9 more quoted lines elided]…
›› Draw your own conclusions.

My conclusion is that your shop is self-righteous.

I hope you are familiar with Structured Assembler. Loops,
If-then-else groups, begin-end. You probably mean BR or B
instructions, not Gotos.

I prefer not to use Gotos but wouldn't make an issue of it.

Cory Hamasaki
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "eugene a. pallat" <ua-author-501199@usenetarchives.gap>
- **Date:** 1997-06-23T20:00:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p38@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p34@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p33@usenetarchives.gap> <gap-5c8eb7b1a0-p34@usenetarchives.gap>`

```

Tim Nicholson wrote in article
<01bc801a$bdbe4680$9d9··.@W95··S.COM>...
› I have been in the COBOL industry for 7 years working on other people's
› code and developing my own.  I have seen more uses of GO TO than I care
…[13 more quoted lines elided]…
› code is understandable I don't have a problem with the coding method.

Well, Tim, I agree with your professor. First learn to program without GO
TOs. Then, in the real world, If you >>really<< need one, use it very
sparingly. The new compilers have verbs like EXIT-PERFORM, but the old
ones don't. In that case, I see no problem with a GO TO to break out of a
compound IF, for instance (used in only a forward direction, of course).

Many companies have program coding standards for ease of maintenance. That
doesn't mean you can't be creative. Just remember that too many GO TOs
lead to spaghetti code, and I've seen enough of that to choke a horse.

If you decide to become multi-lingual, you learn to avoid unneeded GO TOs
like the plague. I've had people remark that my assembler code is
structured almost like a compiler language because it's so clean.

Get a copy of Dykstra's paper about correctness of code and structured
programming. It's what GOOD programmers have been doing all along.

Remove the '-' from orion-data for sending email to me.

Gene eap··.@ori··a.com

Orion Data Systems

Solicitations to me must be pre-approved in writing
by me after soliciitor pays $1,000 US per incident.
Solicitations sent to me are proof you accept this
notice and will send a certified check forthwith.

› SteveO  wrote in article
› <33A··.@pac··l.net>...
…[9 more quoted lines elided]…
›› Draw your own conclusions.
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "d.s..." <ua-author-6569161@usenetarchives.gap>
- **Date:** 1997-06-24T20:00:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p39@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p34@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p33@usenetarchives.gap> <gap-5c8eb7b1a0-p34@usenetarchives.gap>`

```

On 23 Jun 97 21:17:57 GMT, "Tim Nicholson"
wrote:

› I have been in the COBOL industry for 7 years working on other people's
› code and developing my own.  I have seen more uses of GO TO than I care to
…[31 more quoted lines elided]…
›› 

Hey, if you're talking POWERFUL, i.e., a command that can do a lot,
then it's the ALTER verb. I mean, after all, all a GOTO does is go
to. Even a MOVE statement has more power. Yes, a GOTO is
efficient,but that's where it begins and ends. If you're really into
GOTO statements, then you should be using the ALTER verb often and
setting switches to control logic. After all, since 'good
programmers' can make systems efficient, why not use ALTER to keep the
gate swinging.... :-)

Seriously, we are KILLING ourselves. We log onto this NG to share
information and techniques. The continual discussion of outmoded
techniques does nothing for our future. We sound like a bunch of old
farmers arguing that tractors will never be as productive as
horse-drawn implements. Not a happy sight....

David d.s··.@ix.··m.com
____________________________________
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 4)_

- **From:** "troxle..." <ua-author-8415077@usenetarchives.gap>
- **Date:** 1997-06-25T20:00:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p40@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p39@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p33@usenetarchives.gap> <gap-5c8eb7b1a0-p34@usenetarchives.gap> <gap-5c8eb7b1a0-p39@usenetarchives.gap>`

```

d.s··.@ix.··m.com (David) wrote:



› Hey, if you're talking POWERFUL, i.e., a command that can do a lot,
› then it's the ALTER verb.  I mean, after all, all a GOTO does is go
…[5 more quoted lines elided]…
› gate swinging....    :-)    

YUCK!!!!

I'm an unfortunate sole that has worked on such monsters. Better
include Expeditor or Viasoft to assist you in walking through the
code, otherwise, you will get lost.


Tim Oxler -
TEO Computer Technologies Inc.
tro··.@i··.net
http://www.i1.net/~troxler
http://users.aol.com/TEOcorp
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 5)_

- **From:** "jim konert" <ua-author-10238491@usenetarchives.gap>
- **Date:** 1997-06-26T20:00:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p41@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p40@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p33@usenetarchives.gap> <gap-5c8eb7b1a0-p34@usenetarchives.gap> <gap-5c8eb7b1a0-p39@usenetarchives.gap> <gap-5c8eb7b1a0-p40@usenetarchives.gap>`

```

Tim Oxler retorted:
› 
› d.s··.@ix.··m.com (David) humurously expounded:
…[7 more quoted lines elided]…
› Tim Oxler -

BT DT Got the tee shirt, spent two years in therapy. Can
now face an ALTER statement and only break out in a cold sweat.
No more screaming fits, or projectile vomiting.


Jim Konert
EDS/SLRSC/ Earthgrains

It isn't necessary to imagine the world ending in fire or ice -- there
are two other possibilities: one is paperwork, and the other is
nostalgia.
Frank Zappa (1940-1993)
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 6)_

- **From:** "tro..." <ua-author-3877946@usenetarchives.gap>
- **Date:** 1997-07-07T19:24:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p42@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p41@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p33@usenetarchives.gap> <gap-5c8eb7b1a0-p34@usenetarchives.gap> <gap-5c8eb7b1a0-p39@usenetarchives.gap> <gap-5c8eb7b1a0-p40@usenetarchives.gap> <gap-5c8eb7b1a0-p41@usenetarchives.gap>`

```

In article ,
gma··.@iil··l.com wrote:
› 
› In article <33B··.@ea··r.com> Jim Konert  writes:
…[19 more quoted lines elided]…
› 

First off, the ALTER statement is unorthodox. ALTER statements (plural)
are complicated. When they intertwine, they're impossible.

I haven't seen a *modern* version of it's use. The programs that I had
to deal with, were written in the 70's, not structured and written to
increase performance.


› Ot perhaps I got it wrong: Can you come up with an ALTER example that
› cannot be re-written using a GO TO ... DEPENDING construct? I would
› think that the only real difference between the two is that the ALTER
› statement can be far far away from the branch it's altering.
› 

To be honest, I'm not a big fan of GO TO .... DEPENDING ON either. Unless
performance is a problem, I'll use EVALUATE.

› One point I've always found interesting: I've never seen a source
› level debugger for COBOL that would be sensitive to an ALTER
…[5 more quoted lines elided]…
› 

I could be wrong. But when I worked with ALTER laced programs some 5yrs
ago, Expeditor worked "Properly", at least the batch version did.

Tim Oxler

-------------------==== Posted via Deja News ====-----------------------
http://www.dejanews.com/ Search, Read, Post to Usenet
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 7)_

- **From:** "edward r. foley" <ua-author-17072908@usenetarchives.gap>
- **Date:** 1997-07-09T20:00:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p43@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p42@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p33@usenetarchives.gap> <gap-5c8eb7b1a0-p34@usenetarchives.gap> <gap-5c8eb7b1a0-p39@usenetarchives.gap> <gap-5c8eb7b1a0-p40@usenetarchives.gap> <gap-5c8eb7b1a0-p41@usenetarchives.gap> <gap-5c8eb7b1a0-p42@usenetarchives.gap>`

```

tro··.@i··.net wrote:

› lots of stuff deleted

Repeat after me: NEVER, NEVER, NEVER use the ALTER verb....

The reason for the above incantation is the fact that I will, in the
end, be the contractor brought in to debug the mess you have created. I
do not need the headaches.

Thanks,
Ed Foley
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 5)_

- **From:** "d.s..." <ua-author-6569161@usenetarchives.gap>
- **Date:** 1997-06-27T20:00:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p44@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p40@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p33@usenetarchives.gap> <gap-5c8eb7b1a0-p34@usenetarchives.gap> <gap-5c8eb7b1a0-p39@usenetarchives.gap> <gap-5c8eb7b1a0-p40@usenetarchives.gap>`

```

On Thu, 26 Jun 1997 13:56:24 GMT, tro··.@i··.net (Tim Oxler)
wrote:

› d.s··.@ix.··m.com (David) wrote:
› 
…[24 more quoted lines elided]…
› 
Sorry, folks. When I posted the suggestion to use ALTER, I did so in
jest, attempting to emphasize that power on a verb does not
necessarily make it's use desirable. The use of ALTER makes the flaws
in the GOTO just that much worse. However, if we revisit history, the
'need' for the ALTER verb grew out of a programmer's belief that the
ALTER and GOTO would increase efficiency. It was poor thinking then
and is still such today.

So, to all, my regrets for even introducing the verb. :-( It, along
with GOTO and PERFORM..THRU should all be banned.
david

David d.s··.@ix.··m.com
____________________________________
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 6)_

- **From:** "charles f hankel" <ua-author-1885209@usenetarchives.gap>
- **Date:** 1997-06-27T20:00:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p45@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p44@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p33@usenetarchives.gap> <gap-5c8eb7b1a0-p34@usenetarchives.gap> <gap-5c8eb7b1a0-p39@usenetarchives.gap> <gap-5c8eb7b1a0-p40@usenetarchives.gap> <gap-5c8eb7b1a0-p44@usenetarchives.gap>`

```

David wrote:
› 
› On Thu, 26 Jun 1997 13:56:24 GMT, tro··.@i··.net (Tim Oxler)
…[21 more quoted lines elided]…
› and is still such today.

Not exactly right. In terms of execution time performance, the ALTER/GO
TO combination _was_ usually more efficient, there being only a one-time
setup of the procedural branch. Of course, the problem with it is not
the verb itself but rather the horrendous way it was used by certain
programmers (and, of course, the fact that the resultant code is not
re-entrant). The amin problem area for maintainers is when the ALTER is
located nowhere near the altered paragraph.

I don't recommend it as normal thing, but I did use it the other day in
a program on my own system just for the devilment, and I was
half-provoked into it by Richard Plinston's horrified response to my
mention of it.

Charles

=====================================================
Thus writes the virtual quill pen of Charles F Hankel
Dat veniam corvis, vexat censura columbas - Juvenal
=====================================================
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

- **From:** "charles f hankel" <ua-author-1885209@usenetarchives.gap>
- **Date:** 1997-06-27T20:00:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p46@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p34@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p33@usenetarchives.gap> <gap-5c8eb7b1a0-p34@usenetarchives.gap>`

```

Tim Nicholson wrote:
› 
› I have been in the COBOL industry for 7 years working on other people's
…[6 more quoted lines elided]…
› also plain dumb. 

Exactly. Many years ago at school (I think I was about 8 at the time),
we had been taught about classical music and had listened to
Tchaikovsky's 1812. The
test we sat asked us to name a Russian composer and I was failed on my
answer of Rimsky-Korsakov because the teacher was looking for
Tchaikovsky as the answer.

I knew that I could spell Rimsky-Korsakov, and he had had a more
interesting life than Pyotr Ilyich, and my great-great-uncle had known
him. That wasn't good enough.

Charles

=====================================================
Thus writes the virtual quill pen of Charles F Hankel
Dat veniam corvis, vexat censura columbas - Juvenal
=====================================================
```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 4)_

- **From:** "tom mcfarland" <ua-author-3012834@usenetarchives.gap>
- **Date:** 1997-06-30T20:00:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p47@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p46@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p33@usenetarchives.gap> <gap-5c8eb7b1a0-p34@usenetarchives.gap> <gap-5c8eb7b1a0-p46@usenetarchives.gap>`

```

```

###### ↳ ↳ ↳ Re: "GO TO" the most powerful verb in COBOL

_(reply depth: 5)_

- **From:** "charles f hankel" <ua-author-1885209@usenetarchives.gap>
- **Date:** 1997-07-05T20:00:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c8eb7b1a0-p48@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c8eb7b1a0-p47@usenetarchives.gap>`
- **References:** `<19970531191401.PAA17715@ladder02.news.aol.com> <gap-5c8eb7b1a0-p33@usenetarchives.gap> <gap-5c8eb7b1a0-p34@usenetarchives.gap> <gap-5c8eb7b1a0-p46@usenetarchives.gap> <gap-5c8eb7b1a0-p47@usenetarchives.gap>`

```

Tom McFarland wrote:
› 
› --
…[26 more quoted lines elided]…
› Hardly analogous!

I thought it was. It's the demand to complete a task and then to tell
you that you were wrong because you didn't do it the way I liked,
regardless of whether the task was completed properly as asked. At
least with a Standards Manual you can flesh out the question with the
hidden agenda.

Charles

=====================================================
Thus writes the virtual quill pen of Charles F Hankel
Dat veniam corvis, vexat censura columbas - Juvenal
=====================================================
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
