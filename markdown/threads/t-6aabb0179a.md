[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How DO I make labels?

_27 messages · 14 participants · 1997-10 → 1997-11_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How DO I make labels?

- **From:** "joe shodan" <ua-author-17073795@usenetarchives.gap>
- **Date:** 1997-10-23T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34515DFD.6ED@cncnet.com>`

```

I'm struggling in my COBOL class at the college and I need to know how
to create a program that displays mailing labels in this format...

Name
Street Address
City State Zip

w/3 lines between each label.

If anyone can show me some code that would be great, thanks.

Joe
```

#### ↳ Re: How DO I make labels?

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-24T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34515DFD.6ED@cncnet.com>`
- **References:** `<34515DFD.6ED@cncnet.com>`

```

Sounds like a homework assignment, but I will give you a little help. I
assume by 'display' that you actually mean 'print'. I'm not sure why you
would want to display labels on the screen wasting 3 lines between them.

MOVE TO PRINT-RECORD.
WRITE PRINT-RECORD
BEFORE ADVANCING 1 LINE.
*
MOVE TO PRINT-RECORD.
WRITE PRINT-RECORD
BEFORE ADVANCING 1 LINE.
*
MOVE TO PRINT-RECORD.
WRITE PRINT-RECORD
BEFORE ADVANCING 4 LINES.

Historic aside: Years ago, some unthinking IBM engineer decided to create a
printer which was more efficient printing a line "AFTER ADVANCING" than
"BEFORE ADVANCING". To this day, many IBM and other COBOL shops are still
using this unnatural logic. If you doubt that printing AFTER ADVANCING is
illogical, consider that a page heading routine knows there should be extra
apace after the heading, but why should every detail print have to test if
it should add space before printing? There are probably a billion extra
lines of code out there because of this one unthinking (I hesitate to say
'stupid') decision.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)

Joe Shodan  wrote in article
<345··.@cnc··t.com>...
> I'm struggling in my COBOL class at the college and I need to know how
> to create a program that displays mailing labels in this format...
…[10 more quoted lines elided]…
>
```

##### ↳ ↳ Re: How DO I make labels?

- **From:** "fred mcarthur" <ua-author-12785235@usenetarchives.gap>
- **Date:** 1997-10-24T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p2@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap>`

```

Judson D. McClendon wrote:
› Historic aside: Years ago, some unthinking IBM engineer decided to create a
› printer which was more efficient printing a line "AFTER ADVANCING" than
…[12 more quoted lines elided]…
› 

I haven't used either one of these in a while, doing too much online
programming these days, but most shops I've worked at define report
output
as RECFM=FBA, then by moving a value to position 1 of the output record,
(space for single line, '0' for double space, '-' for triple space, '1'
for top of page), all you need to do is write the record.
```

###### ↳ ↳ ↳ Re: How DO I make labels?

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-24T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p3@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap> <gap-6aabb0179a-p3@usenetarchives.gap>`

```

Fred McArthur wrote:
› Judson D. McClendon wrote:
›› Historic aside: Years ago, some unthinking IBM engineer decided to
…[21 more quoted lines elided]…
› for top of page), all you need to do is write the record.

Fred, that's another construct that bugs me. Evidently that same engineer
decided to use the first character of the print buffer to specify
positioning. That in itself is okay, but it should never have been
reflected in high level language source code. It is contrary to good
structured principles (and COBOL compatibility) to involve the source code
in the mechanics of actually how an I/O is accomplished, particularly such
details of where and how buffers and parameters are passed to the I/O
controller. Those are system level details properly addressed in system
software written in assembly or C, not application software written in
COBOL. Any COBOL programmer will know what ADVANCING ... means. Only
those familiar with the peculiarities of IBM's particular I/O design would
understand what it means to MOVE "0" to the first character of the print
record. Just because it works and people are used to it (or even like it)
doesn't mean it's a correct or good idea. When first implementing
structured programming standards in the 70's, I had to practically threaten
to fire some programmers to get them to give up their spaghetti code. But
not one of them would have voluntarily gone back after six months. People
will often zealously defend what they're used to.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: How DO I make labels?

_(reply depth: 4)_

- **From:** "fred mcarthur" <ua-author-12785235@usenetarchives.gap>
- **Date:** 1997-10-24T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p4@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap> <gap-6aabb0179a-p3@usenetarchives.gap> <gap-6aabb0179a-p4@usenetarchives.gap>`

```

Judson D. McClendon wrote:
› Fred McArthur  wrote:
›› 
…[25 more quoted lines elided]…
› --

Interesting, but to tell you the truth I don't have a personal bias
toward
any of these constructs. I just follow whatever standards the client is
using.
More often than not there is no formal coding standard. Managers are
typically
more interested in the end-result than the how-to, but they do want
maintainable
code, which usually means code that is similar to what they already
have. So
whether their programs use BEFORE ADVANCING, AFTER ADVANCING, or
POSITIONING
is unimportant to me in terms of getting the job done.

Your last line is absolutely true, because people don't like to change
the
way they do things, even if you can prove you have a better mousetrap.

Just the other day I coded a GO TO that took me out of the current
paragraph.
Bad design? I would totally agree. But it adhered to the standard of
that
particular series of programs I was modifying. I could have
restructured
the program to eliminate the GO TO situation, but then that program
would
no longer resemble it's several skeleton siblings. Comprehension
suffers
when someone else has to maintain a set of similar programs, and finds
that one has been restructured and is dissimilar to the others.

Maybe Object COBOL will or does already address this problem.
```

###### ↳ ↳ ↳ Re: How DO I make labels?

_(reply depth: 4)_

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-10-24T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p4@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap> <gap-6aabb0179a-p3@usenetarchives.gap> <gap-6aabb0179a-p4@usenetarchives.gap>`

```

Judson D. McClendon wrote:
› 
› [snippage]
…[4 more quoted lines elided]…
› controller.

Hmmmm... is it just vaguely possible that these constructs were
generated and embedded into the hardware *before* the concept of
'structuring' was widely implemented? Who nowadays remembers that C01
is channel 01... more importantly, who cares, since one can usually
WRITE AFTER ADVANCING PAGE? How about the ever-popular RESERVE nn
AREAS... anyone remembers having to RESERVE NO ALTERNATE AREAS to cut
down on core usage? Yes, it is a pity that folks did not design things
for things which not exist at the time... but they did, such is Life.

› When first implementing
› structured programming standards in the 70's,

If I recall correctly the '70's had a fairly large installed base of
mainframes in place; should the hardware be redesigned or
backwards-compatibility forgotten?

DD
```

###### ↳ ↳ ↳ Re: How DO I make labels?

_(reply depth: 5)_

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-24T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p6@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap> <gap-6aabb0179a-p3@usenetarchives.gap> <gap-6aabb0179a-p4@usenetarchives.gap> <gap-6aabb0179a-p6@usenetarchives.gap>`

```

The Goobers wrote:
› Judson D. McClendon wrote:
›› 
…[16 more quoted lines elided]…
› for things which not exist at the time... but they did, such is Life.

These 'features' definitely were in place before structured design was well
understood. The problem is that people are still slavishly following the
same practice. At some point, don't you think, it would be wise to start
educating people AWAY from these archaic practices? Otherwise, we will be
stuck with them forever. Case in point is the COBOL ALTER verb. Even
though still in the COBOL 85 standard, it is classed as obsolete, and is
virtually never used. Programmers have been educated and encouraged (or
forced by standards) not to use it. Eventually it will be dropped from the
standard.

›› When first implementing
›› structured programming standards in the 70's,
…[3 more quoted lines elided]…
› backwards-compatibility forgotten?

Neither. How the hardware functions at the I/O interface level is
irrelevant; it should never have been accessible through COBOL syntax. We
should do exactly what was done with ALTER. Departmental coding standards
should be put in place to discourage or forbid new code using these
constructs. Programmers should be taught or retrained to use the proper
syntax. After a period of time, compilers begin flagging the outdated
syntax with a warning. Eventually, the standard is updated to drop the
outdated syntax, and compilers begin flagging it as an error. This could
take decades. It will never happen if the process isn't started. Why do
you think the rest of the programming world considers the COBOL community
dinosaurs? We can successfully defend the COBOL language on several
fronts. But we cannot defend hidebound conformance to obsolete practices.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: How DO I make labels?

_(reply depth: 6)_

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-10-24T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p7@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap> <gap-6aabb0179a-p3@usenetarchives.gap> <gap-6aabb0179a-p4@usenetarchives.gap> <gap-6aabb0179a-p6@usenetarchives.gap> <gap-6aabb0179a-p7@usenetarchives.gap>`

```

Judson D. McClendon wrote:
› 
› The Goobers  wrote:
…[21 more quoted lines elided]…
› understood.
 
› Gracious of you to admit that.
 
› The problem is that people are still slavishly following the
› same practice.  At some point, don't you think, it would be wise to start
› educating people AWAY from these archaic practices?

That depends... are we trying to have archaic and eat it, too? (sorry,
could *not* resist) Some folks say that due to the cheapness of core
and DASD that 'elegance' is an archaic concept yet you seem to rest your
argument on a kind of 'elegance'... curious, it seems.

› Otherwise, we will be
› stuck with them forever.  Case in point is the COBOL ALTER verb.  Even
…[3 more quoted lines elided]…
› standard.

That is because ALTERs have a tendency to be unmaintainable, or so I was
taught; there is no such inherent difficulty in the BEFORE/AFTER
distinction.

› 
››› When first implementing
…[7 more quoted lines elided]…
› irrelevant;

Not if one is trying to write efficient code... that is a Major Source
of Debate, I believe... the more that code caters to hardware functions
the more efficient it is... and the less
structured/maintainable/portable it is. You makes your choices, you
takes the results.

› it should never have been accessible through COBOL syntax.

This, sadly, is not a world where 'should have' equals 'is'... wallowing
in the endless mire of Shoulda Beens is rarely productive.

› We should do exactly what was done with ALTER.  Departmental coding standards
› should be put in place to discourage or forbid new code using these
› constructs.  Programmers should be taught  or retrained to use the proper
› syntax.
 
› We should all do many things; you run your shop and make your own rules.
 
› After a period of time, compilers begin flagging the outdated
› syntax with a warning.
 
› A compiler can be optioned to flag anything you desire, last I looked.
 
› Eventually, the standard is updated to drop the
› outdated syntax, and compilers begin flagging it as an error.
 
› As with the utterly unmaintainable ALTER?
 
› This could take decades.  It will never happen if the process isn't started.
 
› This is truly profound.
 
› Why do
› you think the rest of the programming world considers the COBOL community
› dinosaurs?

I do not know what you mean by 'the rest of the programming world'. ASM
jockeys consider any 3GL to be effete, the PC community is accustomed to
rapid change and rarely considers what is needed to keep up a
multiregion system 24/7. All that aside I rarely concern myself with
what others think... no matter what one does there are those who will
say that one is a hidebound dinosaur and others who will say that one is
a slave the the flavor-of-the-month. If program-runs perform
next-assignment else perform code-like-hell until damned-thing-works...
don't get much plainer than that. Joke 'em if they can't take a fork.

› We can successfully defend the COBOL language on several
› fronts. But we cannot defend hidebound conformance to obsolete practices.

Plural majestatus est... who am this 'we', anyhow?

DD
```

###### ↳ ↳ ↳ Re: How DO I make labels?

_(reply depth: 7)_

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-25T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p8@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap> <gap-6aabb0179a-p3@usenetarchives.gap> <gap-6aabb0179a-p4@usenetarchives.gap> <gap-6aabb0179a-p6@usenetarchives.gap> <gap-6aabb0179a-p7@usenetarchives.gap> <gap-6aabb0179a-p8@usenetarchives.gap>`

```

The Goobers wrote:
› Judson D. McClendon wrote:
›› The Goobers  wrote:
…[111 more quoted lines elided]…
› don't get much plainer than that.  Joke 'em if they can't take a fork.

Thanks. You illustrate, more graphically than I, why we can't get rid of
these archaic, inefficient constructs, even after nearly 40 years.

›› We can successfully defend the COBOL language on several
›› fronts.  But we cannot defend hidebound conformance to obsolete
› practices.
› 
› Plural majestatus est... who am this 'we', anyhow?

Hmmm. I would have thought the answer was obvious. But I'll spell it out:

We (the COBOL programming community) can successfully defend the COBOL
language on several fronts. But we (the COBOL programming community)
cannot defend hidebound conformance to obsolete practices.

Is that easier for you to understand?
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: How DO I make labels?

_(reply depth: 8)_

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-10-25T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p9@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap> <gap-6aabb0179a-p3@usenetarchives.gap> <gap-6aabb0179a-p4@usenetarchives.gap> <gap-6aabb0179a-p6@usenetarchives.gap> <gap-6aabb0179a-p7@usenetarchives.gap> <gap-6aabb0179a-p8@usenetarchives.gap> <gap-6aabb0179a-p9@usenetarchives.gap>`

```

Judson D. McClendon wrote:
› 
› The Goobers  wrote:
…[11 more quoted lines elided]…
› these archaic, inefficient constructs, even after nearly 40 years.

Perhaps my spectacles need re-grooving... how did I do so wondr'ous a
task? The core of that paragraph states 'no matter what one does there
are those who will say that one is a hidebound dinosaur and others who
will say that one is a slave the the flavor-of-the-month'... I cannot
see how this shows why anybody can or cannot do anything.

› 
››› We can successfully defend the COBOL language on several
…[11 more quoted lines elided]…
› Is that easier for you to understand?

'Easy' and 'valid' are two slightly different things... did I miss a
Constitutional Convention which designated a 'COBOL programming
community'? Did I miss a conference which generated a platform for it?
Did I miss an election which created a Spokesperson for this august
community? I have never been called upon to 'defend the COBOL
language'; it had a fair-sized installed base long before I started
coding in it... as such the only 'defense' one can muster is the implest
of 'seems to woork good enough, ayuh'. Next... if you recall
Wittgenstein's asking 'what is the difference between a symptom and a
criterion' in like manner I ask: what is the difference between
'hidebound conformance to obsolete practises' and 'using a technology
proven under diverse circumstances in international installations for
the bulk of mass-installed DP history'? Yes, there is always room for
improvement and Old Lady Hopper herself excoriated the school of 'but
we've always done it this way'... on the other hand it must be asked
'why throw out something which not only works but folks have been able
to be trained in (demonstrating that it can be learned) for decades?'...
or, in business, more fundamentally, 'The present system has proven
profitable... what proven profitability is there in your suppositions?'

DD

P.S. It is obvious that we approach this from two radically different
views... I am a coder, I write programs for money. You appear to
present yourself as a 'member of a programming community' with a
'responsibility unto the generations'... this might be where our
differences arise.

DD
```

###### ↳ ↳ ↳ Re: How DO I make labels?

_(reply depth: 9)_

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-27T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p10@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap> <gap-6aabb0179a-p3@usenetarchives.gap> <gap-6aabb0179a-p4@usenetarchives.gap> <gap-6aabb0179a-p6@usenetarchives.gap> <gap-6aabb0179a-p7@usenetarchives.gap> <gap-6aabb0179a-p8@usenetarchives.gap> <gap-6aabb0179a-p9@usenetarchives.gap> <gap-6aabb0179a-p10@usenetarchives.gap>`

```

The Goobers wrote:
› 
› P.S. It is obvious that we approach this from two radically different
…[3 more quoted lines elided]…
› differences arise.

Not quite. I've turned out several million lines of code in nearly 20
programming languages (mostly COBOL), and make my living primarily by doing
so. I've also had the experience (not recently) of managing twenty or so
programmers, so I have seen both sides of the issue. I've spent
considerable time and effort researching, experimenting with, developing
and teaching programming standards. Not for what's fashionable (who
cares?), but for what works in the trenches. I've owned my own consulting
company for 18 years, and clients come to me, at their own initiative, to
request documentation and instruction in my programming standards and
techniques. You can go into MIS departments all over this area, even in
those where I have never worked, and see standards which I developed being
used. People use them when they hear how well they work somewhere else. I
charge $75-$95 an hour (for the last 3 years; I have not yet raised my
rates for Y2k), and my completed projects, design through implementation
and training, generally cost my clients between $0.50 and $1.00 per line of
delivered code. After a new system is up and running the first 6-8 weeks,
I rarely get bug reports. They just call me when they want a revision, or
something new. I never advertise or solicit, and have had more work
offered than I could possibly do, for over 10 years. I really had to
struggle, doing my last resume update, just to get the list of projects I
have done to fit on three pages. I finally left some older ones out, but
with personal info and references the whole thing's still 5 pages; too
long. I place a lot of confidence in my judgment on these issues, because
I've been there, done that, and the tee-shirt has already been sold in a
garage sale. 8-)
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: How DO I make labels?

_(reply depth: 10)_

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-10-27T19:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p11@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap> <gap-6aabb0179a-p3@usenetarchives.gap> <gap-6aabb0179a-p4@usenetarchives.gap> <gap-6aabb0179a-p6@usenetarchives.gap> <gap-6aabb0179a-p7@usenetarchives.gap> <gap-6aabb0179a-p8@usenetarchives.gap> <gap-6aabb0179a-p9@usenetarchives.gap> <gap-6aabb0179a-p10@usenetarchives.gap> <gap-6aabb0179a-p11@usenetarchives.gap>`

```

Judson D. McClendon wrote:
› 
› The Goobers  wrote:
…[9 more quoted lines elided]…
› so.
 
› Same here but a slightly smaller scale.
 
› I've also had the experience (not recently) of managing twenty or so
› programmers, so I have seen both sides of the issue.
 
› I've not... avoided that route rather assiduously.
 
› I've spent
› considerable time and effort researching, experimenting with, developing
› and teaching programming standards.

I've not... I've never had the patience to teach by anything other than
'example'. If a Good Mind passes by I'll do my damndest to tweak a bit
of interest and point a direction or two... but anything else just tries
what little patience I have. (on my present assignment I am playing
'old man' to two younger fellows... rather difficult to break them of
the habit of trying to show how smart they are by trying to complete my
sentences while I am saying them... pfah)


› [snippage about Setting Standards]

As I said, old boy... seems like we approach this from two radically
different views... I code, you code and teach.

DD
```

###### ↳ ↳ ↳ Re: How DO I make labels?

_(reply depth: 4)_

- **From:** "ejones7" <ua-author-6589063@usenetarchives.gap>
- **Date:** 1997-10-31T19:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p4@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap> <gap-6aabb0179a-p3@usenetarchives.gap> <gap-6aabb0179a-p4@usenetarchives.gap>`

```

On the topic of backward compatibility and
WRITE/AFTER ADVANCING ...



When one considers that typically, carriage control precedes
data on mainframes, one learns why COBOL--born on a mainframe
and probably to die on one [if ever it does...]--is phrased
as it is. BEFORE ADV and AFTER ADV.

Even when one goes to that modern hybrid of 1950's language
FORTRAN, Visual Basic, control characters and screen controls
are specified, sometimes using the more antiquated method of
using CHR$(nnn) to achieve the print carriage manipulations.

But, going to a more modern language, C/C++ (actually a relic
of the 1970's and Ma Bell...will it run on anything that doesn't
have copper wiring?? I wonder...), we find that print control
is specified, not automatic. Why??? Why?? Why must the
programmer specify print controls???

Is it likely that the "clients" and users are not the
lobotomized persons with the same single-digit IQ who want
all reports to be alike and vertically spaced alike? So that,
given a choice, they'd rip out the stale "canned" headers and
titles from their Lotus123 and Excel sheets to be replaced by
customized headings and footings??

Is it possible? Is it possible that some shops have differing
report formats??
```

###### ↳ ↳ ↳ Re: How DO I make labels?

_(reply depth: 5)_

- **From:** "gary lee" <ua-author-1751270@usenetarchives.gap>
- **Date:** 1997-11-01T19:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p13@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap> <gap-6aabb0179a-p3@usenetarchives.gap> <gap-6aabb0179a-p4@usenetarchives.gap> <gap-6aabb0179a-p13@usenetarchives.gap>`

```

----------------- much nested snippage -----------------------
› Is it likely that the "clients" and users are not the 
› lobotomized persons with the same single-digit IQ who want
…[7 more quoted lines elided]…
› 
Personally, I thought we still had carriage control so that people who
bothered to learn how to control the machine would have a way to do it,
despite their managements' decrees that we all be brainless droids. That
is, since they won't let us play with assembler anymore, we have to use
what's left.
```

###### ↳ ↳ ↳ Re: How DO I make labels?

- **From:** "joseph lenz" <ua-author-17071704@usenetarchives.gap>
- **Date:** 1997-10-24T20:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p3@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap> <gap-6aabb0179a-p3@usenetarchives.gap>`

```

› I haven't used either one of these in a while, doing too much online 
› programming these days, but most shops I've worked at define report
…[3 more quoted lines elided]…
› for top of page), all you need to do is write the record.

This is know as WRITE AFTER POSITIONING, and has become obsolete as my
company moves from IBM DOS/VS COBOL to COBOL II to COBOL for VSE. So we
are converting the AFTER POSITIONING code to AFTER ADVANCING.

Joseph Lenz
TTI, Inc.
Fort Worth, TX
```

###### ↳ ↳ ↳ Re: How DO I make labels?

_(reply depth: 4)_

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-24T20:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p15@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap> <gap-6aabb0179a-p3@usenetarchives.gap> <gap-6aabb0179a-p15@usenetarchives.gap>`

```

Joseph Lenz wrote:
›› I haven't used either one of these in a while, doing too much online 
›› programming these days, but most shops I've worked at define report
…[8 more quoted lines elided]…
› are converting the AFTER POSITIONING code to AFTER ADVANCING.

It is the AFTER Vs BEFORE which I am concerned with.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: How DO I make labels?

- **From:** "han..." <ua-author-8441900@usenetarchives.gap>
- **Date:** 1997-10-27T19:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p3@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap> <gap-6aabb0179a-p3@usenetarchives.gap>`

```

On Sat, 25 Oct 1997 10:31:34 -0400, Fred McArthur
cast the runes and pronounced:

› Judson D. McClendon wrote:
›› Historic aside: Years ago, some unthinking IBM engineer decided to create a
…[14 more quoted lines elided]…
› for top of page), all you need to do is write the record.

Strictly speaking the '1' is a skip to Channel 1 on the print control
tape and is only top-of-form by general practice. Similarly, you can
skip any of twelve channels by using the single-digit hex value. As
the form designer, you can have your own control tape. Of course,
with these new-fangled laser things there is no physical tape but the
principle can still be applied.

Charles

----------------
Old and past it?
Not any more
----------------
```

##### ↳ ↳ Re: How DO I make labels?

- **From:** "joseph lenz" <ua-author-17071704@usenetarchives.gap>
- **Date:** 1997-10-24T20:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p2@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap>`

```


Judson D. McClendon wrote in article
<01bce14c$535d0360$4734b9ce@juddesk>...

** snip stuff **

› Historic aside: Years ago, some unthinking IBM engineer decided to create
› a
…[11 more quoted lines elided]…
› 'stupid') decision.

AFTER ADVANCING is easy for me to understand. I don't get your point???

Joseph Lenz
TTI, Inc.
Fort Worth, TX
```

###### ↳ ↳ ↳ Re: How DO I make labels?

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-24T20:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p18@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap> <gap-6aabb0179a-p18@usenetarchives.gap>`

```

Joseph Lenz wrote:
› 
› Judson D. McClendon  wrote:
…[19 more quoted lines elided]…
› AFTER ADVANCING is easy for me to understand.  I don't get your point???

Both BEFORE ADVANCING and AFTER ADVANCING are equally easy to understand.
But that isn't the issue. The issue is that BEFORE ADVANCING is simpler
and more efficient in practice, simply because the nature of report
formatting is such that you naturally know how much space should be after
the line you are currently printing more often than you know how much space
should be before the line you are printing. This fairly easy to
demonstrate, but is generally not obvious to programmers who have always
been taught to use AFTER ADVANCING. This includes most of the IBM and
derivative community. I discovered this unconscious bias by discussing it
with quite a few of them, and this thread should bear that out. The only
reason programmers started using AFTER ADVANCING in the first place (I was
around back then, and it was common knowledge) was because the standard IBM
1403 printer was designed to advance, then print. To print and then
advance took two I/O commands and was almost twice as slow. The
programming documentation told you this, even in other programming
languages. So why are programmers still using AFTER ADVANCING? Simply
because they have been taught to do it that way, and nobody seems to be
rethinking the issue. Outside the IBM and derivative programming
communities, I have seldom seen AFTER ADVANCING used, because other
vendor's hardware does either one equally well, and it was apparent to
anyone who studied the issue that BEFORE ADVANCING was cleaner and more
efficient to code. As I think about it, I can't remember meeting a single
programmer that used AFTER ADVANCING, who was not taught or influenced,
directly or indirectly, by someone from the IBM or derivative community.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: How DO I make labels?

_(reply depth: 4)_

- **From:** "joseph lenz" <ua-author-17071704@usenetarchives.gap>
- **Date:** 1997-10-24T20:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p19@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap> <gap-6aabb0179a-p18@usenetarchives.gap> <gap-6aabb0179a-p19@usenetarchives.gap>`

```

Demonstrate away.......I am not convinced.
```

###### ↳ ↳ ↳ Re: How DO I make labels?

- **From:** "kfo..." <ua-author-15004755@usenetarchives.gap>
- **Date:** 1997-10-25T20:00:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p18@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap> <gap-6aabb0179a-p18@usenetarchives.gap>`

```

The major point is that the advancing command is portable from IBM to
PC platform without code change.

If a programmer does not know FBA characters where do they start
looking but they can all read a manual or even good book on advancing.
Before I coded IBM I was very used to Form Feed characters and
carriage returns to do bold overstrike this also was not portable.

The other trick with this is the ADV and NOADV compiler option. If
you do not set this right and use 1 advance command then the
definition has an implicit ASI character added to the front of the
file record layout.

2.5 cents worth (exchange rate is awful)
Ken

On 25 Oct 1997 15:50:50 GMT, "Joseph Lenz"
wrote:

› 
› Judson D. McClendon  wrote in article
…[23 more quoted lines elided]…
› Fort Worth, TX
```

##### ↳ ↳ Re: How DO I make labels?

- **From:** "joel c. ewing" <ua-author-40228@usenetarchives.gap>
- **Date:** 1997-10-24T20:00:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p2@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap>`

```

Judson D. McClendon wrote:
› Historic aside: Years ago, some unthinking IBM engineer decided to create a
› printer which was more efficient printing a line "AFTER ADVANCING" than
…[6 more quoted lines elided]…
› 'stupid') decision.

Actually in terms of "efficiency" the opposite has now been true for IBM
mainframe printers since the 1960's. All IBM mainframe printers at
least from S/360 onward are capable of performing "Write & Space/Skip"
operations (equivalent to WRITE BEFORE ADVANCING) and are not capable of
performing "Space & Write", except as two separate channel commands. The
persistence of the AFTER ADVANCING mentality can probably be blamed on
the old ANSI carriage control standard, which directly supports only
AFTER ADVANCING functions. This probably comes from either the original
Fortran or the original COBOL standard, which may in turn have
originated with some early printer (which must have pre-dated the IBM
1403). Today, when output generated with AFTER ADVANCING and ANSI
carriage control is printed, IBM mainframe systems internally convert
the ANSI carriage control to equivalent sequences of "Space/Skip" and
"Write Before Space/Skip" commands when actually driving the printer.
Joel C. Ewing, Fort Smith, AR        jce··.@a··.org
Consulting Systems Programmer
```

###### ↳ ↳ ↳ Re: How DO I make labels?

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-10-24T20:00:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p23@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6aabb0179a-p22@usenetarchives.gap>`
- **References:** `<34515DFD.6ED@cncnet.com> <gap-6aabb0179a-p2@usenetarchives.gap> <gap-6aabb0179a-p22@usenetarchives.gap>`

```

Joel C. Ewing wrote:
› Judson D. McClendon wrote:
›› Historic aside: Years ago, some unthinking IBM engineer decided to
…[29 more quoted lines elided]…
› "Write Before Space/Skip" commands when actually driving the printer.

Though I don't work with IBM equipment these days, I suspected they would
have corrected that by now. You may be correct for later versions of the
1403, and for the 360. But, according to our documentation at the time, it
was not true for a 1403 attached to a 1401. Perhaps it was a controller
issue rather than the printer itself. As I recall, the controllers for
those older printers often did quite a bit, even timing the hammer firing
sequences.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

#### ↳ Re: How DO I make labels?

- **From:** "binyami..." <ua-author-932190@usenetarchives.gap>
- **Date:** 1997-10-24T20:00:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p24@usenetarchives.gap>`
- **In-Reply-To:** `<34515DFD.6ED@cncnet.com>`
- **References:** `<34515DFD.6ED@cncnet.com>`

```

On Fri, 24 Oct 1997 19:48:30 -0700 Joe Shodan wrote:

:>I'm struggling in my COBOL class at the college and I need to know how
:>to create a program that displays mailing labels in this format...

:>Name
:>Street Address
:>City State Zip

:>w/3 lines between each label.

:>If anyone can show me some code that would be great, thanks.

Here is some pseudo code for you.

Open files
While more-records
Retrieve name, street-address, city, state & zip
Write name
Write street-address
Write city state & zip
Write 3 blank lines
Repeat
Close files

:>Joe
```

#### ↳ Re: How DO I make labels?

- **From:** "fred..." <ua-author-28008@usenetarchives.gap>
- **Date:** 1997-10-26T19:00:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p25@usenetarchives.gap>`
- **In-Reply-To:** `<34515DFD.6ED@cncnet.com>`
- **References:** `<34515DFD.6ED@cncnet.com>`

```

Joe,
first print your three lines of text, one after the other, and then print three
blank lines one after the other.
```

#### ↳ Re: How DO I make labels?

- **From:** "chip ling" <ua-author-6589301@usenetarchives.gap>
- **Date:** 1997-10-28T19:00:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p26@usenetarchives.gap>`
- **In-Reply-To:** `<34515DFD.6ED@cncnet.com>`
- **References:** `<34515DFD.6ED@cncnet.com>`

```

Joe Shodan wrote:
› 
› I'm struggling in my COBOL class at the college and I need to know how
…[10 more quoted lines elided]…
› Joe


Dear Joe,

I think most people in the newsgroup will not tell you how to code
your assignment by giving you the code directly. But instead we will
help you thru if you find some problem when YOU CODE them YOURSELF.
But at least you need to show us you have done something on it.

Well in order to give you some guideline, please follow the instructions
below and it will help.

1. You must have a COBOL text book if you are new to the language.

2. Read through the book. Know what a COBOL program looks like. etc.

3. Before direct jump to coding, make sure you know the followings
a. where does the data coming from and in what form?
b. where does the output going to and in what form?
c. On what platform you are going to develop your program,
and what COBOL compiler you are going to use?
(You must have the COBOL compiler manual too)

4. If you know exactly what you are going. Start coding.

5. Whenever encounter problem, search thru your text book and
compiler manual. If you really cannot make it, leave message
on the newsgroup with all the information about. (together
with your segment of coding) I'm sure a lot of people will
help.

Good luck.

Rgds,
Chip LING
chi··.@sym··o.ca
```

#### ↳ Re: How DO I make labels?

- **From:** "bgwi..." <ua-author-599269@usenetarchives.gap>
- **Date:** 1997-10-28T19:00:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aabb0179a-p27@usenetarchives.gap>`
- **In-Reply-To:** `<34515DFD.6ED@cncnet.com>`
- **References:** `<34515DFD.6ED@cncnet.com>`

```

Joe Shodan wrote:

› I'm struggling in my COBOL class at the college and I need to know how
› to create a program that displays mailing labels in this format...
…[9 more quoted lines elided]…
› Joe

I don't know about the college assignment, but here is a production
program I had to whip up once. Extrapolate from this.

000100 IDENTIFICATION DIVISION.
000200 PROGRAM-ID. CBL0105.
000300 AUTHOR. BOYCE G WILLIAMS, JR.
000400 INSTALLATION. VIRGINIA COMMONWEALTH UNIVERSITY.
000500 DATE-WRITTEN. 08/07/96.
000600 DATE-COMPILED.
000700 ENVIRONMENT DIVISION.
000800* *------------------------------------------------*
000900* * MAKE MAILING LABELS FROM EXISTING HRS EMPLOYEE *
001000* *------------------------------------------------*
001100 CONFIGURATION SECTION.
001200*----------------------------------------------------------------*
001300*SOURCE-COMPUTER. IBM-370 WITH DEBUGGING MODE.
001400 SOURCE-COMPUTER. IBM-3081.
001500 OBJECT-COMPUTER. IBM-3081.
001600*----------------------------------------------------------------*
001700 INPUT-OUTPUT SECTION.
001800*----------------------------------------------------------------*
001900 FILE-CONTROL.
002000*----------------------------------------------------------------*
002100 SELECT PERSFILE-PERSONNEL-FILE
002200 ASSIGN TO PERSFILE.
002300 SELECT REPTFILE-REPORT-FILE
002400 ASSIGN TO REPTFILE.
002500 SELECT PERSSORT-PERSONNEL-FILE
002600 ASSIGN TO PERSSORT.
002700*----------------------------------------------------------------*
002800 DATA DIVISION.
002900*----------------------------------------------------------------*
003000 FILE SECTION.
003100*----------------------------------------------------------------*
003200 FD PERSFILE-PERSONNEL-FILE
003300 RECORD CONTAINS 290 CHARACTERS
003400 BLOCK CONTAINS 0 CHARACTERS
003500 LABEL RECORDS ARE STANDARD
003600 DATA RECORD IS PERSFILE-PERSONNEL-RECORD.
003700 01 PERSFILE-PERSONNEL-RECORD.
003800 05 FILLER PIC X(290).
003900*-----------------------------*
004000 FD REPTFILE-REPORT-FILE
004100 BLOCK CONTAINS 0 RECORDS
004200 RECORD CONTAINS 132 CHARACTERS
004300 LABEL RECORD ARE STANDARD.
004400 01 REPTFILE-REPORT-LINE.
004500 05 FILLER PIC X(132).
004600*-----------------------------*
004700 SD PERSSORT-PERSONNEL-FILE
004800 RECORD CONTAINS 290 CHARACTERS
004900 DATA RECORD IS PERSSORT-PERSONNEL-RECORD.
005000 01 PERSSORT-PERSONNEL-RECORD.
005100 05 PERSSORT-SSN PIC X(09).
005200 05 PERSSORT-NAME-LAST PIC X(25).
005300 05 PERSSORT-NAME-FIRST PIC X(25).
005400 05 PERSSORT-PHONE PIC X(08).
005500 05 PERSSORT-TITLE PIC X(30).
005600 05 PERSSORT-DEPARTMENT PIC X(30).
005700 05 PERSSORT-BOX-LABEL PIC X(07).
005800 05 PERSSORT-BOX PIC X(06).
005900 05 PERSSORT-ADDRESS PIC X(45).
006000 05 PERSSORT-EMAIL PIC X(30).
006100 05 PERSSORT-END PIC X(01).
006110 05 PERSSORT-DEPT-NAME PIC X(30).
006200 05 PERSSORT-DEPT-BOX PIC X(06).
006300 05 PERSSORT-DEPT-ADDRESS PIC X(30).
006400 05 PERSSORT-DEPT-PHONE PIC X(08).
006500*----------------------------------------------------------------*
006600 WORKING-STORAGE SECTION.
006700*----------------------------------------------------------------*
006800 01 WS-SWITCHES.
006900 05 WS-END-OF-FILE-SWITCH PIC X(01).
007000 88 WS-END-OF-FILE VALUE 'Y'.
007100 05 WS-HEADING-SWITCH PIC X(01).
007200 88 WS-HEADING VALUE 'Y'.
007300*-----------------------------*
007400 01 WS-SEQUENCE-CONTROLS.
007500 05 WS-PREV-KEY.
007600 10 WS-PREV-DEPARTMENT PIC X(30).
007700 10 WS-PREV-BOX PIC X(06).
007800 05 WS-CURR-KEY.
007900 10 WS-CURR-DEPARTMENT PIC X(30).
008000 10 WS-CURR-BOX PIC X(06).
008100*-----------------------------*
008200 01 WS-REPORT-CONTROLS.
008300 05 WS-LINE-SPACING PIC 9(01).
008400*-----------------------------*
008500 01 WS-LIST-UP-CONTROLS.
008600 05 WS-COLUMN-COUNT PIC S9(04) COMP SYNC.
008700 05 WS-COLUMN-LIMIT PIC S9(04) VALUE +2
008800 COMP SYNC.
008900 05 WS-ROW-COUNT PIC S9(04) COMP SYNC.
009000 05 WS-ROW-LIMIT PIC S9(04) VALUE +06
009100 COMP SYNC.
009200*-----------------------------*
009300 01 PERS-PERSONNEL-DATA.
009400 05 PERS-SSN PIC X(09).
009500 05 PERS-NAME-LAST PIC X(25).
009600 05 PERS-NAME-FIRST PIC X(25).
009700 05 PERS-PHONE PIC X(08).
009800 05 PERS-TITLE PIC X(30).
009900 05 PERS-DEPARTMENT PIC X(30).
010000 05 PERS-BOX-LABEL PIC X(07).
010100 05 PERS-BOX PIC X(06).
010200 05 PERS-ADDRESS PIC X(45).
010300 05 PERS-EMAIL PIC X(30).
010400 05 PERS-END PIC X(01).
010410 05 PERS-DEPT-NAME PIC X(30).
010500 05 PERS-DEPT-BOX PIC X(06).
010600 05 PERS-DEPT-ADDRESS PIC X(30).
010700 05 PERS-DEPT-PHONE PIC X(08).
010800*-----------------------------*
010900 01 LU-LIST-UP-PAGE.
011000 05 LU-LIST-ROW OCCURS 72 TIMES.
011100 10 LU-LIST-COLUMN OCCURS 2 TIMES.
011200 15 FILLER PIC X(02).
011300 15 LU-LINE PIC X(45).
011400 15 FILLER PIC X(01).
011500*----------------------------------------------------------------*
011600 PROCEDURE DIVISION.
011700*----------------------------------------------------------------*
011800 DECLARATIVES.
011900*----------------------------------------------------------------*
012000 AA-DEBUG SECTION.
012100*-----------------------------*
012200 USE FOR DEBUGGING ALL PROCEDURES.
012300 DISPLAY DEBUG-ITEM.
012400*----------------------------------------------------------------*
012500 END DECLARATIVES.
012600*----------------------------------------------------------------*
012700 000-START-OF-PROGRAM.
012800*-----------------------------*
012900 OPEN OUTPUT REPTFILE-REPORT-FILE
013000 SORT PERSSORT-PERSONNEL-FILE
013100 ASCENDING KEY PERSSORT-DEPT-NAME
013200 ASCENDING KEY PERSSORT-DEPT-BOX
013300 ASCENDING KEY PERSSORT-NAME-LAST
013400 ASCENDING KEY PERSSORT-NAME-FIRST
013500 ASCENDING KEY PERSSORT-SSN
013600 USING PERSFILE-PERSONNEL-FILE
013700 OUTPUT PROCEDURE 300-OP-PROCESS-FILE-PERSSORT
013800 CLOSE REPTFILE-REPORT-FILE
013900 STOP RUN
014000 .
014100*----------------------------------------------------------------*
014200 300-OP-PROCESS-FILE-PERSSORT.
014300*-----------------------------*
014400 MOVE ALL 'X' TO PERS-PERSONNEL-DATA
014500 MOVE 1 TO WS-COLUMN-COUNT
014600 MOVE 1 TO WS-ROW-COUNT
014700 SET WS-HEADING TO TRUE
014800 SET WS-END-OF-FILE TO TRUE
014900 PERFORM 320-FORMAT-RECORD-REPTFILE 12 TIMES
015000*
015010 MOVE SPACES TO PERS-PERSONNEL-DATA
015100 MOVE 1 TO WS-COLUMN-COUNT
015200 MOVE 1 TO WS-ROW-COUNT
015300 SET WS-HEADING TO TRUE
015400 MOVE 'N' TO WS-END-OF-FILE-SWITCH
015500 PERFORM 800-RETURN-RECORD-PERSSORT
015600 PERFORM 310-PROCESS-GROUP-DEPARTMENT
015700 UNTIL WS-END-OF-FILE
015800 IF WS-COLUMN-COUNT IS LESS THAN WS-COLUMN-LIMIT
015900 THEN
016000 IF WS-ROW-COUNT IS NOT LESS THAN WS-ROW-LIMIT
016100 THEN
016200 ADD 1 TO WS-COLUMN-COUNT
016300 MOVE 1 TO WS-ROW-COUNT
016400 END-IF
016500 PERFORM 320-FORMAT-RECORD-REPTFILE
016600 UNTIL WS-ROW-COUNT IS NOT LESS THAN WS-ROW-LIMIT
016700 AND WS-ROW-COUNT IS NOT LESS THAN WS-ROW-LIMIT
016800 END-IF
016900 .
017000*----------------------------------------------------------------*
017100 310-PROCESS-GROUP-DEPARTMENT.
017200*-----------------------------*
017300 PERFORM 320-FORMAT-RECORD-REPTFILE
017400 MOVE WS-CURR-KEY TO WS-PREV-KEY
017500 PERFORM 330-PROCESS-RECORD-PERSSORT
017600 UNTIL WS-END-OF-FILE
017700 OR WS-CURR-KEY NOT = WS-PREV-KEY
017800 .
017900*----------------------------------------------------------------*
018000 320-FORMAT-RECORD-REPTFILE.
018100*-----------------------------*
018200 IF WS-COLUMN-COUNT IS NOT LESS THAN WS-COLUMN-LIMIT
018300 AND WS-ROW-COUNT IS NOT LESS THAN WS-ROW-LIMIT
018400 THEN
018500 MOVE 1 TO WS-COLUMN-COUNT
018600 MOVE 1 TO WS-ROW-COUNT
018700 INITIALIZE LU-LIST-UP-PAGE
018800 END-IF
018900*
019000 IF WS-COLUMN-COUNT IS LESS THAN WS-COLUMN-LIMIT
019100 AND WS-ROW-COUNT IS NOT LESS THAN WS-ROW-LIMIT
019200 THEN
019300 ADD 1 TO WS-COLUMN-COUNT
019400 MOVE 1 TO WS-ROW-COUNT
019500 END-IF
019600*
019700 IF PERS-PERSONNEL-DATA IS GREATER THAN SPACES
019800 THEN
019900 MOVE 'HEAD OF DEPARTMENT'
020000 TO LU-LINE (WS-ROW-COUNT, WS-COLUMN-COUNT)
020100 END-IF
020200 IF WS-COLUMN-COUNT IS EQUAL TO WS-COLUMN-LIMIT
020300 MOVE LU-LIST-ROW (WS-ROW-COUNT) TO REPTFILE-REPORT-LINE
020400 IF LU-LINE (WS-ROW-COUNT, 1) IS GREATER THAN SPACES
020500 OR LU-LINE (WS-ROW-COUNT, 2) IS GREATER THAN SPACES
020600 THEN
020700 IF WS-HEADING
020800 THEN
020900 PERFORM 870-PRINT-HEADINGS-REPTFILE
021000 MOVE 'N' TO WS-HEADING-SWITCH
021100 ELSE
021200 PERFORM 890-WRITE-LINE-REPTFILE
021300 END-IF
021400 END-IF
021500 END-IF
021600 ADD 1 TO WS-ROW-COUNT
021700 MOVE 1 TO WS-LINE-SPACING
021800*
021900 MOVE FUNCTION UPPER-CASE (PERS-DEPT-NAME)
022000 TO LU-LINE (WS-ROW-COUNT, WS-COLUMN-COUNT)
022100 IF WS-COLUMN-COUNT IS EQUAL TO WS-COLUMN-LIMIT
022200 THEN
022300 MOVE LU-LIST-ROW (WS-ROW-COUNT) TO REPTFILE-REPORT-LINE
022400 IF LU-LINE (WS-ROW-COUNT, 1) IS GREATER THAN SPACES
022500 OR LU-LINE (WS-ROW-COUNT, 2) IS GREATER THAN SPACES
022600 THEN
022700 PERFORM 890-WRITE-LINE-REPTFILE
022800 END-IF
022900 END-IF
023000 ADD 1 TO WS-ROW-COUNT
023100 MOVE 1 TO WS-LINE-SPACING
023200*
023300 IF PERS-PERSONNEL-DATA IS GREATER THAN SPACES
023400 THEN
023500 STRING 'P O BOX ' DELIMITED BY SIZE
023600 PERS-DEPT-BOX DELIMITED BY SIZE
023700 INTO LU-LINE (WS-ROW-COUNT, WS-COLUMN-COUNT)
023800 END-IF
023900 IF WS-COLUMN-COUNT IS EQUAL TO WS-COLUMN-LIMIT
024000 THEN
024100 MOVE LU-LIST-ROW (WS-ROW-COUNT) TO REPTFILE-REPORT-LINE
024200 IF LU-LINE (WS-ROW-COUNT, 1) IS GREATER THAN SPACES
024300 OR LU-LINE (WS-ROW-COUNT, 2) IS GREATER THAN SPACES
024400 THEN
024500 PERFORM 890-WRITE-LINE-REPTFILE
024600 END-IF
024700 END-IF
024800 ADD 4 TO WS-ROW-COUNT
024900 MOVE 4 TO WS-LINE-SPACING
025000 .
025100*----------------------------------------------------------------*
025200 330-PROCESS-RECORD-PERSSORT.
025300*-----------------------------*
025400 PERFORM 800-RETURN-RECORD-PERSSORT
025500 .
025600*----------------------------------------------------------------*
025700 800-RETURN-RECORD-PERSSORT.
025800*-----------------------------*
025900 RETURN PERSSORT-PERSONNEL-FILE
026000 INTO PERS-PERSONNEL-DATA
026100 AT END SET WS-END-OF-FILE TO TRUE
026200 MOVE SPACES TO PERS-PERSONNEL-DATA
026300 WS-CURR-KEY
026400 .
026500 IF NOT WS-END-OF-FILE
026600 THEN
026700 MOVE PERS-DEPT-NAME TO WS-CURR-DEPARTMENT
026800 MOVE PERS-DEPT-BOX TO WS-CURR-BOX
026900 END-IF
027000 .
027100*----------------------------------------------------------------*
027200 870-PRINT-HEADINGS-REPTFILE.
027300*-----------------------------*
027400 PERFORM 880-WRITE-TOPLINE-REPTFILE
027500 .
027600*----------------------------------------------------------------*
027700 880-WRITE-TOPLINE-REPTFILE.
027800*-----------------------------*
027900 WRITE REPTFILE-REPORT-LINE
028000 AFTER ADVANCING PAGE
028100 .
028200*----------------------------------------------------------------*
028300 890-WRITE-LINE-REPTFILE.
028400*-----------------------------*
028500 WRITE REPTFILE-REPORT-LINE
028600 AFTER ADVANCING WS-LINE-SPACING LINES
028700 .
028800*--------------------------------------------------------------*
028900* END OF PROGRAM *
029000*--------------------------------------------------------------*

Hope this helps,

Boyce G. Williams, Jr.

.--------------------------------------------------------------------.
| "People should have two virtues: purpose- the courage to envisage |
| and pursue valued goals uninhibited by the defeat of infantile |
| fantasies, by guilt and the failing fear punishment; and wisdom- a|
| detached concern with life itself, in the face of death itself." |
| Norman F. Dixon|
'--------------------------------------------------------------------'
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
