[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Paragraphs vs Sections

_43 messages · 22 participants · 1998-09_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Paragraphs vs Sections

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com>`

```
I just thought I would put out a post with a subject line that reflects the
trend of a recent thread.  Now my question is,

  Which of the following is the most futile discussion?

     COBOL vs C
     COBOL vs Perl
     What is the best editor for creating COBOL source code?
     Should you use Paragraphs or Sections?

If you check DejaNews, I think each of these topics gets "beaten to death"
frequently (about every 3 to 6 months - although I will say that the "COBOL
vs Perl" discussion is new, but reads very similar to previous "COBOL vs
Rexx" discussions).

As far as the actual Section vs Paragraph discussion go, my PERSONAL opinion
is that if you follow this rules you will have an easily maintainable
program with minimal error possibilities,

1) Use ONLY paragraphs or ONLY sections - no combination of the two in the
same program

2) NEVER allow the THRU option of the PERFORM verb

3) Use the "EXIT SECTION" or "EXIT PARAGRAPH" syntax (if available) over the
GO TO <procedure-name-exit> statement.

This does nothing for maintaining existing code, but is sure what I would
recommend for new code.
```

#### ↳ Re: Paragraphs vs Sections

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298252.74566.25050@kcbbs.gen.nz>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com>`

```
In message <<6t7hhc$9g4@sjx-ixn3.ix.netcom.com>> "William M. Klein" <wmklein@ix.netcom.com> writes:
> 
>   Which of the following is the most futile discussion?
…[4 more quoted lines elided]…
>      Should you use Paragraphs or Sections?

I always enjoy discussions of this form because it is always
possible to _learn_ something (except for those with totally
closed minds).

> If you check DejaNews, I think each of these topics gets "beaten to death"
> frequently (about every 3 to 6 months - although I will say that the "COBOL
> vs Perl" discussion is new, but reads very similar to previous "COBOL vs
> Rexx" discussions).

I would expect that the language arguments in this group are
started by outsiders, usually those with little experience
beyond their newfound toy, posting here because they feel
their language is superior, mainly because they are clueless
about hoe Cobol is used.

However, I do learn new languages and believe that doing 
this does improve my Cobol programming, as well as 
being able to use them when they are more appropriate.


But technical issues on Cobol, such as GO TO or not, PERFORMs
or CALLs, OO, are in a completely different categorey and are
entirely on topic.

There are always 'better' ways to code.  Unfortunately there
seems to be several hardened coders who seem to feel
threatened by coding styles more modern than those of the
70s, they bemoan these discussions rather than just 
saying 'N' to the message.

> 
> As far as the actual Section vs Paragraph discussion go, my PERSONAL opinion
…[12 more quoted lines elided]…
> recommend for new code.

I entirely agree with you, except for ........        ;-)

What you have actually done with these guidelines is to
restrict the use of _labels_ (which is a good thing).
It is not the GO TO that is the problem with maintainability,
it is the labels that are the target.  In my view each
label should only ever be used for one thing.  In the
case of "Only use paragraphs" every label can only be
the target of a PERFORM, there cannot be GO TOs out to
another label (there can actually be GO TOs back to the
lable - discuss in less than 25 pages).  

In the case of "Only perform sections" there are two classes
of labels:  The sections that are only ever performed, and
the ~-Exit paragraphs that are only ever GO TOed. (In
fact with this style I advocate using a specific GO TO ~-Exit
immediately before the paragraph instead of drop-through
to emphasise the point.

Other styles allow the use of labels for mixtures of:
PERFORM, PERFORM THRU, GO TO, Drop-through.  Because
labels are used in more than one way the complexity 
increases.

One measure that I use for complexity is to count the
labels and, for each, the number of different ways 
these are used:  If a label is the subject of a GO TO,
a PERFORM and a drop-through then it has a count of 3.

The lower the total the better, the more easily 
maintainable it is (on this metric, other metrics
may apply too).
```

#### ↳ Re: Paragraphs vs Sections

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-2hkLMYkURC6d@Dwight_Miller.iix.com>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com>`

```
On Thu, 10 Sep 1998 03:16:44, "William M. Klein" 
<wmklein@ix.netcom.com> wrote:

> 1) Use ONLY paragraphs or ONLY sections - no combination of the two in the
> same program
> 

Now thats kind of tough to do if the compiler you are using complies 
with the current standard.  You have to have a paragraph title under a
section title.
```

##### ↳ ↳ Re: Paragraphs vs Sections

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35f81214.0@news2.uswest.net>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <Jl0PnHJ5PvPd-pn2-2hkLMYkURC6d@Dwight_Miller.iix.com>`

```
I think what he meant is, if you use SECTION, the each block of code should
be contained within the paragraph title at the start of that SECTION, and
there should be no _other_ paragraphs before the end of the SECTION.

do-stuff section.
do-stuff.
      read whoever
      perform whatever
      write whereever
      .
exit.

Or some such similar arrangement

Thane Hubbell wrote in message ...
>On Thu, 10 Sep 1998 03:16:44, "William M. Klein"
><wmklein@ix.netcom.com> wrote:
>
>> 1) Use ONLY paragraphs or ONLY sections - no combination of the two in
the
>> same program
>>
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

- **From:** "dumb n. ugly" <w@x.y>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t96r3$a71$1@news-1.news.gte.net>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <Jl0PnHJ5PvPd-pn2-2hkLMYkURC6d@Dwight_Miller.iix.com> <35f81214.0@news2.uswest.net>`

```
Seeing that I have missed the opener on this thread, is there one of you
kind gurus who can explain to me the value of PERFORMing sections instead
of paragraphs?  Maybe my 10 years and two degrees missed something, but I
have never seen it necessary to use sections except with an intrinsic sort.

Chris Osborne <chris_n_osborne@yahoo.com> wrote in article
<35f81214.0@news2.uswest.net>...
> I think what he meant is, if you use SECTION, the each block of code
should
> be contained within the paragraph title at the start of that SECTION, and
> there should be no _other_ paragraphs before the end of the SECTION.
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t9g27$p3k@sjx-ixn2.ix.netcom.com>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <Jl0PnHJ5PvPd-pn2-2hkLMYkURC6d@Dwight_Miller.iix.com> <35f81214.0@news2.uswest.net> <6t96r3$a71$1@news-1.news.gte.net>`

```

dumb n. ugly wrote in message <6t96r3$a71$1@news-1.news.gte.net>...
>Seeing that I have missed the opener on this thread, is there one of you
>kind gurus who can explain to me the value of PERFORMing sections instead
>of paragraphs?  Maybe my 10 years and two degrees missed something, but I
>have never seen it necessary to use sections except with an intrinsic sort.
>


FYI,
  Up until the '85 Standard, SORT input/output procedures needed to be
SECTIONS - but with the current (not just draft) Standard, you can use
paragraphs here too.
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 5)_

- **From:** "William R. Fink" <bfink@apci.net>
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tr8bc$n7d@mhstl1.monsanto.com>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <Jl0PnHJ5PvPd-pn2-2hkLMYkURC6d@Dwight_Miller.iix.com> <35f81214.0@news2.uswest.net> <6t96r3$a71$1@news-1.news.gte.net> <6t9g27$p3k@sjx-ixn2.ix.netcom.com>`

```

William M. Klein wrote in message <6t9g27$p3k@sjx-ixn2.ix.netcom.com>...
>
>dumb n. ugly wrote in message <6t96r3$a71$1@news-1.news.gte.net>...
…[3 more quoted lines elided]…
>>have never seen it necessary to use sections except with an intrinsic
sort.
>>
>

I have never used SECTIONS before (10 years in COBOL too). In fact, 90% of
the shops I have worked at say to do your sorts outside of your COBOL
program (i.e. syncsort or the such).  In any regard, I also teach COBOL at
the community college level for students in a 2 year degree program.  Do any
of you feel it is worth instructing the students on using SECTIONS?

Bill
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 6)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36012e1f.0@news1.ibm.net>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <Jl0PnHJ5PvPd-pn2-2hkLMYkURC6d@Dwight_Miller.iix.com> <35f81214.0@news2.uswest.net> <6t96r3$a71$1@news-1.news.gte.net> <6t9g27$p3k@sjx-ixn2.ix.netcom.com> <6tr8bc$n7d@mhstl1.monsanto.com>`

```

William R. Fink wrote in message <6tr8bc$n7d@mhstl1.monsanto.com>...
>I have never used SECTIONS before (10 years in COBOL too). In fact, 90% of
>the shops I have worked at say to do your sorts outside of your COBOL
>program (i.e. syncsort or the such).  In any regard, I also teach COBOL at
>the community college level for students in a 2 year degree program.  Do
any
>of you feel it is worth instructing the students on using SECTIONS?


If you do not tell them about DECLARATIONS or SORT/MERGEs, there
is no need to teach them SECTIONS. Just mention it as an obsolete
technique, that they might come across in real life (getting their first job
maintaining legacy code).
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 7)_

- **From:** scm@enterprise.net (Shaun C. Murray)
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6trgs5$euv$2@news.enterprise.net>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <Jl0PnHJ5PvPd-pn2-2hkLMYkURC6d@Dwight_Miller.iix.com> <35f81214.0@news2.uswest.net> <6t96r3$a71$1@news-1.news.gte.net> <6t9g27$p3k@sjx-ixn2.ix.netcom.com> <6tr8bc$n7d@mhstl1.monsanto.com> <36012e1f.0@news1.ibm.net>`

```
In article <36012e1f.0@news1.ibm.net>, leif@ibm.net says...
>
>If you do not tell them about DECLARATIONS or SORT/MERGEs, there
>is no need to teach them SECTIONS. Just mention it as an obsolete
>technique, that they might come across in real life (getting their first job
>maintaining legacy code).

Please don't. Some of us *only* use sections. I'm not going to go over the 
dangers of paragraph trickle again - look it up on Dejanews.
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 8)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298260.86152.24628@kcbbs.gen.nz>`
- **References:** `<6trgs5$euv$2@news.enterprise.net>`

```

 
> There is a potential (serious) maintenance problem with PERFORM
> paragraph.
 
> That is is if the performed paragraph is shortened by adding a
> paragraph label part way thru and all PERFORM references to it
…[3 more quoted lines elided]…
> original paragraph.
 
Why are you 'adding a paragraph label part way thru' ?  Is it
so you can do a GO TO to it ?  Of course any programmer can
break code if they are silly and add random changes to it.
 
> But of course your unit testing and regression testing would
> spot this :-)
 
> Performing sections is much safer and you don'r need a THRU
> statement.
 
The 'danger' arises from the possibility of a GO TO branching
off to the wrong place.  It is _much safer_ if you don't jump
out to an exit, then you don't need a THRU _or_ a SECTION.
 
> And if you're a "structured" person you'll probably only need
> one paragraph label in some sections to allow for quitting once
> uncertainty has been resolved.
 
Do you have 'uncertainty' in your programs ?
 
> If you do this it's also safer to use the same paragraph labels
> in all sections. I always use Z as the quit label in all
> sections. All my quits are GO TO Z. Unambiguous!
 
Unless you forget to put the Z paragraph in, then it
'unambiguously' goes to the wrong place.
 
> Otherwise if you mix your quit labels labels and copy chunks of
> code around for butchering it would be possible (if you're not
> careful) to branch to the quit routine in another section. Woops!
 
Exactly, but this can never happen if you don't use SECTIONs or
THRU, because there _aren't_ any 'branch to quit' of any sort.
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 4)_

- **From:** DOUG-PARTCH@WORLDNET.ATT.NET
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tc1ot$mc6$1@nnrp1.dejanews.com>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <Jl0PnHJ5PvPd-pn2-2hkLMYkURC6d@Dwight_Miller.iix.com> <35f81214.0@news2.uswest.net> <6t96r3$a71$1@news-1.news.gte.net>`

```
In article <6t96r3$a71$1@news-1.news.gte.net>,
  "dumb n. ugly" <w@x.y> wrote:
> Seeing that I have missed the opener on this thread, is there one of you
> kind gurus who can explain to me the value of PERFORMing sections instead
…[10 more quoted lines elided]…
>
IF Sections are used, you can just perform that section through the exit
point.  A benifit of this is trying to exit out of a paragraph(go to a000-
exit).  Also the code looks cleaner than performing a perform thru statement.

In any case use one or the other unless it the only choice.

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 4)_

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35f97fc0.0@news3.uswest.net>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <Jl0PnHJ5PvPd-pn2-2hkLMYkURC6d@Dwight_Miller.iix.com> <35f81214.0@news2.uswest.net> <6t96r3$a71$1@news-1.news.gte.net>`

```
dumb n. ugly wrote in message <6t96r3$a71$1@news-1.news.gte.net>...
>Seeing that I have missed the opener on this thread, is there one of you
>kind gurus who can explain to me the value of PERFORMing sections instead
…[9 more quoted lines elided]…
>

Up topic under RE:Ethical Question, several subthreads have gone into detail
on this.

A long time ago, when RAM (storage for us mainframers) was a precious
commodity, designing your code in SECTIONS could let your object code run in
considerably less space.
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 4)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298253.3898.16281@kcbbs.gen.nz>`
- **References:** `<6t96r3$a71$1@news-1.news.gte.net>`

```
In message <<6t96r3$a71$1@news-1.news.gte.net>> "dumb n. ugly" <w@x.y> writes:
> kind gurus who can explain to me the value of PERFORMing sections instead
> of paragraphs?  Maybe my 10 years and two degrees missed something, but I
> have never seen it necessary to use sections except with an intrinsic sort.

The only 'advantage' of a PERFORM section over a PERFORM 
paragraph is that in the former you can have a GO TO to
the exit paragraph for the section wheras this is not
possible with 'PERFORM paragraph' (unless you add THRU).
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 5)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298253.72220.27003@kcbbs.gen.nz>`
- **References:** `<3298253.3898.16281@kcbbs.gen.nz>`

```
In message <<3298253.3898.16281@kcbbs.gen.nz>> riplin@kcbbs.gen.nz  writes:
> > kind gurus who can explain to me the value of PERFORMing sections instead
> > of paragraphs?  Maybe my 10 years and two degrees missed something, but I
…[6 more quoted lines elided]…
> 

(talking to myself again)

Actually there is another reason for using SECTIONs and 
that is that paragraph names need only be unique within
each SECTION.  To refer to a particular paragraph you
would then:

         PERFORM paragraph IN/OF section-name

If the qualification is not added then resolution is to
the current section.

However, this is most likely a good reason for _not_
using sections.  If a paragraph is accidentally duplicated
then it may be that at some time one may be performed and
at others the other (depending entirely on where the
PERFORM statement is) yet the programmer may only know
of one of these and would be confused as to why the
program is not behaving 'correctly'.
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 5)_

- **From:** bruce.chris@hyder.com
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tb36p$8b3$1@nnrp1.dejanews.com>`
- **References:** `<6t96r3$a71$1@news-1.news.gte.net> <3298253.3898.16281@kcbbs.gen.nz>`

```
In article <3298253.3898.16281@kcbbs.gen.nz>,
  riplin@kcbbs.gen.nz (Richard Plinston) wrote:
> In message <<6t96r3$a71$1@news-1.news.gte.net>> "dumb n. ugly" <w@x.y> writes:
> > kind gurus who can explain to me the value of PERFORMing sections instead
…[7 more quoted lines elided]…
>

There is a potential (serious) maintenance problem with PERFORM paragraph.

That is is if the performed paragraph is shortened by adding a paragraph
label part way thru and all PERFORM references to it are not changed then
you've changed the way the program works: what was one paragraph is now two
or more and the perform statement will only execute the few remaining lines
in that original paragraph.

But of course your unit testing and regression testing would spot this :-)

Performing sections is much safer and you don'r need a THRU statement.

And if you're a "structured" person you'll probably only need one paragraph
label in some sections to allow for quitting once uncertainty has been
resolved. If you do this it's also safer to use the same paragraph labels in
all sections. I always use Z as the quit label in all sections. All my quits
are GO TO Z. Unambiguous!

Otherwise if you mix your quit labels labels and copy chunks of code around
for butchering it would be possible (if you're not careful) to branch to the
quit routine in another section. Woops!

-------


-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tbv1m$hnj@sjx-ixn10.ix.netcom.com>`
- **References:** `<6t96r3$a71$1@news-1.news.gte.net> <3298253.3898.16281@kcbbs.gen.nz> <6tb36p$8b3$1@nnrp1.dejanews.com>`

```

bruce.chris@hyder.com wrote in message <6tb36p$8b3
   <snip>
>
>There is a potential (serious) maintenance problem with PERFORM paragraph.
…[6 more quoted lines elided]…
>
  <more snip>

Anyone who goes around adding "labels" in the middle of what is supposed to
be a single (named) part of logic is going to break any type of program.  It
certainly would happen just as badly if they put a SECTION name in the
middle of an existing section (and the original section was performed).
There are certain "rules" that you can follow that make maintenance easier
and more fool proof BUT there is no way to avoid future logic errors if a
FOOL is really determined to break a functioning program.

Bottom-line:  People who only use paragraph names and Performs without
"THRU" simply NEVER would put a paragraph name in the middle of an existing
paragraph.
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 6)_

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35F9BD4D.DFDB5798@att.net>`
- **References:** `<6t96r3$a71$1@news-1.news.gte.net> <3298253.3898.16281@kcbbs.gen.nz> <6tb36p$8b3$1@nnrp1.dejanews.com>`

```
bruce.chris@hyder.com wrote:

(some snipping)
> > The only 'advantage' of a PERFORM section over a PERFORM
> > paragraph is that in the former you can have a GO TO to
…[9 more quoted lines elided]…
> in that original paragraph.

In any structured program, there is no need to insert a paragraph name
in the middle of what used to be a paragraph. The problem is with
PERFORM...THRUs (seriously). They may be clean when originally coded,
but the door is open (as in, stick a paragraph name in the middle) to
deteriorate into really dreadful spaghetti.

A paragraph is a block of code with a single entry and a single exit -
under what circumstances would you insert another paragraph name into a
working block of code? If you think of the software we write as though
it had a physical dimension, a paragraph would be a gear or a drive
shaft. It wouldn't make sense to paste something else onto it.

Just my $0.02,
Bill Lynch
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 7)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uIk7h8k39GA.231@upnetnews03>`
- **References:** `<6t96r3$a71$1@news-1.news.gte.net> <3298253.3898.16281@kcbbs.gen.nz> <6tb36p$8b3$1@nnrp1.dejanews.com> <35F9BD4D.DFDB5798@att.net>`

```

Bill Lynch wrote in message <35F9BD4D.DFDB5798@att.net>...
>bruce.chris@hyder.com wrote:
>
…[6 more quoted lines elided]…
>> There is a potential (serious) maintenance problem with PERFORM
paragraph.
>>
>> That is is if the performed paragraph is shortened by adding a paragraph
>> label part way thru and all PERFORM references to it are not changed then
>> you've changed the way the program works: what was one paragraph is now
two
>> or more and the perform statement will only execute the few remaining
lines
>> in that original paragraph.
>
…[8 more quoted lines elided]…
>working block of code?

Aha - a challenge <g>! Here is another $0.02 worth.  How about this
situation.  You have a program containing:

        perform paragraph
        .
        .
paragraph.
       statement1
       statement2
       statement3
       statement4
       statement5
       statement6
        .
        .

Then you see that 3 other places in the same program contain the identical
sequence of statements represented by statement4, statement5 and statement6.

In the interest of reducing duplicated code, you could insert:

        perform paragraph-split
        .
paragraph-split.

between statement3 and statement4 and, in the other 3 locations, replace the
duplicated series of statements with:

        perform paragraph-split

 >If you think of the software we write as though
>it had a physical dimension, a paragraph would be a gear or a drive
>shaft. It wouldn't make sense to paste something else onto it.


Analogies, huh? <g>  Then the program is a drive train, and we are just
adding a reduction gear (more torque?), or is it an overdrive gear (better
fuel economy and/or less engine wear?)



>Just my $0.02,
>Bill Lynch
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XXNK1.2521$p61.3933595@news4.mia.bellsouth.net>`
- **References:** `<6t96r3$a71$1@news-1.news.gte.net> <3298253.3898.16281@kcbbs.gen.nz> <6tb36p$8b3$1@nnrp1.dejanews.com> <35F9BD4D.DFDB5798@att.net>`

```
Bill Lynch wrote:
>
>In any structured program, there is no need to insert a paragraph name
…[9 more quoted lines elided]…
>shaft. It wouldn't make sense to paste something else onto it.


We enforce that with a simple code scanner which every production program
must pass.  We also use PERFORM ... THRU.  We do this because permitting
an early exit from a code block is important enough that almost all
languages provide one, except COBOL, and it is in the next COBOL standard.
The code scanner also enforces a 1:1 match between paragraph/exit and that
the PERFORM matches the THRU, and that there is no GO TO outside the
paragraph.  The use of this simple scanner eliminates all of the concerns
such as extra paragraphs, or putting the wrong EXIT on the THRU.  It also
has the advantage of flagging missing periods and periods in the middle of
a sentence.  Many, many program bugs have been caught this way.  However,
as soon as EXIT PARAGRAPH is available in the standard, PERFORM ... THRU
and GO TO become completely unnecessary in COBOL; there will no longer be
any reason to use either, except possibly in certain esoteric situations.
(It's pretty hard to say absolutely never, ever. :)
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 7)_

- **From:** bruce.chris@hyder.com
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tij2e$9k1$1@nnrp1.dejanews.com>`
- **References:** `<6t96r3$a71$1@news-1.news.gte.net> <3298253.3898.16281@kcbbs.gen.nz> <6tb36p$8b3$1@nnrp1.dejanews.com> <35F9BD4D.DFDB5798@att.net>`

```
In article <35F9BD4D.DFDB5798@att.net>,
  Bill Lynch <wblynch@att.net> wrote:
> bruce.chris@hyder.com wrote:
>
> (some snipping)
> > > The only 'advantage' of a PERFORM section over a PERFORM
<snip>
> > There is a potential (serious) maintenance problem with PERFORM paragraph.
> >
> > That is is if the performed paragraph is shortened by adding a paragraph
> > label part way thru and all PERFORM references to it are not changed then
<another snip>
> In any structured program, there is no need to insert a paragraph name
> in the middle of what used to be a paragraph. The problem is with
…[11 more quoted lines elided]…
> Bill Lynch
---
Hi Bill,

You write your code with single entries and exits; I write my code with
single entries and exits. Not everyone does. Ancient legacy code is another
problem. And beginners often welcome advice.

The point I was trying to make was that Sections are more foolproof than
Paragraphs. In fact some sites forbid Paragraphs for the reasons I have
discussed above.

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 8)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298256.68621.25700@kcbbs.gen.nz>`
- **References:** `<6tij2e$9k1$1@nnrp1.dejanews.com>`

```
In message <<6tij2e$9k1$1@nnrp1.dejanews.com>> bruce.chris@hyder.com writes:
> 
> The point I was trying to make was that Sections are more foolproof than
> Paragraphs. In fact some sites forbid Paragraphs for the reasons I have
> discussed above.

This is completely untrue, it is just that the problems are
different.  You may have been 'sensitised' to particular
modes of problems by your direct experience, I have been
sensitised to others by mine.

There are many ways in which a fool can break either style
of programming, but I completely reject the idea that
SECTIONs are 'more foolproof'.  For example it is difficult
to find a missing keyword SECTION because text editors are
not normally setup to find the adsence of a string (though
a macro may do this).  A missing section keyword means
that this paragraph is performed as part of the previous
section and this may give subtle problems.

In a program with no section keywords it is not hard to
demonstrate that one was not inadvertantly added by a
simple grep or search.

In general you are better with the style that you have
trained yourself to than to someone else's.  The brain
is very good at pattern recognition once patterns have
been 'programmed' in by training and experience.  Your
brain has been trained to recognise patterns of sections.
others recognise patterns of paragraphs, others need 
numbering to visualise the pattern from their paper
diagrams.

Now (surprisingly no doubt) I have no problem with
people working with different mechanisms, I have
used most of them at one time or another and can
apreciate the advantages that may be claimed for them.

What I dislike is when ficticious advantages are claimed
for particular styles.  Advantages which are easily
nullified by better development environments or only
apply because of particular training.
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 5)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eiWCHri39GA.169@upnetnews03>`
- **References:** `<6t96r3$a71$1@news-1.news.gte.net> <3298253.3898.16281@kcbbs.gen.nz>`

```

Richard Plinston wrote in message <3298253.3898.16281@kcbbs.gen.nz>...
>In message <<6t96r3$a71$1@news-1.news.gte.net>> "dumb n. ugly" <w@x.y>
writes:
>> kind gurus who can explain to me the value of PERFORMing sections instead
>> of paragraphs?  Maybe my 10 years and two degrees missed something, but I
>> have never seen it necessary to use sections except with an intrinsic
sort.
>
>The only 'advantage' of a PERFORM section over a PERFORM
>paragraph is that in the former you can have a GO TO to
>the exit paragraph for the section wheras this is not
>possible with 'PERFORM paragraph' (unless you add THRU).


I'm sure you realize that this is not an advantage welcomed by any shop that
tries to maintain no-GOTO standards.  PERFORM section almost invites
maintenance programmers to slip in GO TO paragraph (and not necessarily
last-paragraph-in-the-section) statements when that appears to them to be an
expedient solution to their instant problem.
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 6)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298254.74565.14738@kcbbs.gen.nz>`
- **References:** `<eiWCHri39GA.169@upnetnews03>`

```
In message <<eiWCHri39GA.169@upnetnews03>> "Dennis J. Minette" <dennis_minette@email.msn.com> writes:
> >
> >The only 'advantage' of a PERFORM section over a PERFORM
…[9 more quoted lines elided]…
> expedient solution to their instant problem.

Exactly, that is why I quoted the word 'advantage'  :-)

Having perform paragraph _only_ enforces no GO TO (except
it does allow looping back to the current paragraph for
repeating).  This is a disadvantage if you cannot design
programs correctly   :-)
```

#### ↳ Re: Paragraphs vs Sections

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t9ebv$iiu$1@juliana.sprynet.com>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com>`

```
Bill,

    FWIW, I had posted a problem several months ago that I was having using
the 'OPT' compiler option in a new program that performed SECTIONS
exclusively. The load module with 'OPT' active was larger than with 'NOOPT'.
Since then, I have been informed by a gentleman from IBM (upon your
reference) that 'OPT' is used for performance reasons NOT load module size.
The compiler used was COBOL2, release 4.1.

    Anyway, my point is that when I removed the word SECTION from the
paragraph labels, the load module was reduced by 5K using 'OPT' and the PMAP
was still about the same number of pages. Go figure....

Cheers,

WOB,
Atlanta

William M. Klein wrote in message <6t7hhc$9g4@sjx-ixn3.ix.netcom.com>...
>I just thought I would put out a post with a subject line that reflects the
>trend of a recent thread.  Now my question is,
…[13 more quoted lines elided]…
>As far as the actual Section vs Paragraph discussion go, my PERSONAL
opinion
>is that if you follow this rules you will have an easily maintainable
>program with minimal error possibilities,
…[6 more quoted lines elided]…
>3) Use the "EXIT SECTION" or "EXIT PARAGRAPH" syntax (if available) over
the
>GO TO <procedure-name-exit> statement.
>
…[4 more quoted lines elided]…
>
```

#### ↳ Re: Paragraphs vs Sections

- **From:** "G. van Vlimmeren" <gvlimmer@hoogenbosch.nl>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bddc8c$8d2b4fc0$2c050380@s70>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com>`

```


William M. Klein <wmklein@ix.netcom.com> schreef in artikel
<6t7hhc$9g4@sjx-ixn3.ix.netcom.com>...
> I just thought I would put out a post with a subject line that reflects
the
> trend of a recent thread.  Now my question is,
> 
…[6 more quoted lines elided]…
> 
Hmm, 

I would ask one more question....

Is it better to write 'GO TO' or to write 'GO' ?
Discussion please :)

Gerben 'JUSTIFY UP' van Vlimmeren
```

##### ↳ ↳ Re: Paragraphs vs Sections

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O#2ZbXi39GA.297@upnetnews03>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <01bddc8c$8d2b4fc0$2c050380@s70>`

```

G. van Vlimmeren wrote in message <01bddc8c$8d2b4fc0$2c050380@s70>...
>
>
…[19 more quoted lines elided]…
>
There is no 'better' here to be discussed.  How about: is it better to write
PIC or PICTURE?  Or, in conditional statements, is it better to use = or
EQUAL?  It is just a matter of choosing a style.  Let's just hope for
consistency in application of the style chosen so as to accommodate future
maintainability.
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

- **From:** mindock@theriver.com
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tdrvt$dkn$1@nnrp1.dejanews.com>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <01bddc8c$8d2b4fc0$2c050380@s70> <O#2ZbXi39GA.297@upnetnews03>`

```

> >>
>

Here's my 2 cents on this. I'd say it's confusing and personally prefer
PERFORM PARA-A1, PERFORM PARA-A2, etc.

Example: Current program
PERFORM SECTION-A.
...
SECTION-A.
PARA-A1.
...
PARA-A12.

SECTION-B.
...

So now a newby maintenance programmer gets assigned to add task 'Z' to the
code. They figure that task 'Z' should be invoked from PARA-A12.
 So they create PARA-A13 in SECTION A.
In PARA-A12 they code: IF THE-MOON-IS-BLUE PERFORM PARA-A13.

I confess I don't know offhand (not having used SECTIONs on purpose for many
years, since sort got improved) without a manual whether PARA-A13 gets
PERFORMED twice, once due to the IF in PARA-A12 and once because it is in
SECTION-A. But I do know the answer if there is no PERFORM SECTION strategy.

I'll try this when I get to work. But I suspect it gets done twice.

John



-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 4)_

- **From:** dxmixxer@netdirect.net (Doug Miller)
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tdv9j$eq4_001@p16-term1-and.netdirect.net>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <01bddc8c$8d2b4fc0$2c050380@s70> <O#2ZbXi39GA.297@upnetnews03> <6tdrvt$dkn$1@nnrp1.dejanews.com>`

```
In article <6tdrvt$dkn$1@nnrp1.dejanews.com>, mindock@theriver.com wrote:
+
+> >>
+>
+
+Here's my 2 cents on this. I'd say it's confusing and personally prefer
+PERFORM PARA-A1, PERFORM PARA-A2, etc.
+
+Example: Current program
+PERFORM SECTION-A.
+....
+SECTION-A.
+PARA-A1.
+....
+PARA-A12.
+
+SECTION-B.
+....
+
+So now a newby maintenance programmer gets assigned to add task 'Z' to the
+code. They figure that task 'Z' should be invoked from PARA-A12.
+ So they create PARA-A13 in SECTION A.
+In PARA-A12 they code: IF THE-MOON-IS-BLUE PERFORM PARA-A13.
+
+I confess I don't know offhand (not having used SECTIONs on purpose for many
+years, since sort got improved) without a manual whether PARA-A13 gets
+PERFORMED twice, once due to the IF in PARA-A12 and once because it is in
+SECTION-A. But I do know the answer if there is no PERFORM SECTION strategy.
+
+I'll try this when I get to work. But I suspect it gets done twice.
+
That is correct.
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 4)_

- **From:** "Warren G. Simmons" <warrens@inficad.com>
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35FAB65F.183E8C3A@inficad.com>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <01bddc8c$8d2b4fc0$2c050380@s70> <O#2ZbXi39GA.297@upnetnews03> <6tdrvt$dkn$1@nnrp1.dejanews.com>`

```
John points out that in his view, there is no perform section strategy.

If section names were for overlay purposes, and section numbers were specified
(long gone and ignored now I guess), then perform a section would include
planning to have the available memory allocated, and rolling out that area if
needed, then reading the section into ram for execution.

Reducing sections to a method for simplifying perform through, etc. in my view
has taken the wrong fork in the road. Perform, Perform through, and the new
perform (immediate) seem
easy enough to understand even for a slow learner like myself.

Warren Simmons

mindock@theriver.com wrote:

> > >>

snip to cut band width----

>
>
…[10 more quoted lines elided]…
> http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 4)_

- **From:** scm@enterprise.net (Shaun C. Murray)
- **Date:** 1998-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6thlcj$4ju$3@news.enterprise.net>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <01bddc8c$8d2b4fc0$2c050380@s70> <O#2ZbXi39GA.297@upnetnews03> <6tdrvt$dkn$1@nnrp1.dejanews.com>`

```
In article <6tdrvt$dkn$1@nnrp1.dejanews.com>, mindock@theriver.com says...
>
>I'll try this when I get to work. But I suspect it gets done twice.
>

That it does which is why I never, ever use paragraphs.

Shaun
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 5)_

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35fd5e46.0@news2.uswest.net>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <01bddc8c$8d2b4fc0$2c050380@s70> <O#2ZbXi39GA.297@upnetnews03> <6tdrvt$dkn$1@nnrp1.dejanews.com> <6thlcj$4ju$3@news.enterprise.net>`

```
Shaun C. Murray wrote in message <6thlcj$4ju$3@news.enterprise.net>...
>In article <6tdrvt$dkn$1@nnrp1.dejanews.com>, mindock@theriver.com says...
>>
…[6 more quoted lines elided]…
>

Ditto, except I never, ever use SECTIONs.
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

- **From:** Kitty Carr <kcarr1@bellsouth.net>
- **Date:** 1998-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35FC730E.7614@bellsouth.net>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <01bddc8c$8d2b4fc0$2c050380@s70> <O#2ZbXi39GA.297@upnetnews03>`

```
Dennis J. Minette wrote:
> 
> G. van Vlimmeren wrote in message <01bddc8c$8d2b4fc0$2c050380@s70>...
…[26 more quoted lines elided]…
> maintainability.

This is what irks me - programmers who've been around for a gazillion
years, and actually get ANGRY if anyone's 'style' is not his 'style',
because his 'style' is right; ergo, everyone else is wrong if they don't
conform to his 'style.'

Ten years ago, when I wrote my first little baby program for work, the
Procedure Division consisted of maybe 3 or 4 paragraphs, maybe 20 lines
of code.  

Basically, it read a tape and created an output tape.  No listings. 
Nothing accumulated.  Not even an IF statement.  I took the compiled
listing to our veteran-programmer-who-knows-everything and said "Look! 
It works and everything!"  He scowled at the listing and FLIPPED it back
at me.  "It's not right."  Why not?  "You've got to have PERFORM THRU
EXIT.  It's a standard here."  (It's not; it's HIS standard.)  "You have
to change it."  I'm NOT changing it.  One day when I wasn't there, he
got into my library and rewrote it HIS way, "and while I was at it," he
said, "I made it more structured."  So now my 4 paragraphs (which were
structured just fine,) became 10 paragraphs, like:

b000-initialization.
    perform c000-open-files
        thru c000-open-files-exit.
b000-exit.
    exit.

"Why not put the OPEN statements in the Initialization?"  "Yeah, you
could do that, but this is more structured."  

I HATE when this happens.  And I can't see WHY this made him so angry. 
(I KNOW why it made me angry.)  

Well, sorry to be so verbose.
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 4)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tj3f7$ndm$1@news.igs.net>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <01bddc8c$8d2b4fc0$2c050380@s70> <O#2ZbXi39GA.297@upnetnews03> <35FC730E.7614@bellsouth.net>`

```

Kitty Carr wrote in message <35FC730E.7614@bellsouth.net>...

>I HATE when this happens.  And I can't see WHY this made him so angry.
>(I KNOW why it made me angry.)


There was a good book called "Egoless Programming" written
several years back that should be required reading for all
programmers.  Interesting book. The author's premise was
that most stylistic conventions had more to do with the
programmer's ego than with reality.  A secondary premise
was that the actual utility of the convention went down in
direct relationship to the emphasis placed on it by the programmer.
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 5)_

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35FE0331.8C2CC2C5@att.net>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <01bddc8c$8d2b4fc0$2c050380@s70> <O#2ZbXi39GA.297@upnetnews03> <35FC730E.7614@bellsouth.net> <6tj3f7$ndm$1@news.igs.net>`

```
Donald Tees wrote:
> 
> Kitty Carr wrote in message <35FC730E.7614@bellsouth.net>...
…[10 more quoted lines elided]…
> direct relationship to the emphasis placed on it by the programmer.

Agreed, and I wouldn't limit this observation to programming, only.

Bill Lynch
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 4)_

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35FE02DE.77AF1F92@att.net>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <01bddc8c$8d2b4fc0$2c050380@s70> <O#2ZbXi39GA.297@upnetnews03> <35FC730E.7614@bellsouth.net>`

```
Kitty Carr wrote:
> 
(snip)
> 
> b000-initialization.
…[6 more quoted lines elided]…
> could do that, but this is more structured."

Did Mr. Veteran happen to explain just *how* his way was "more
structured"? I don't see it. 

> I HATE when this happens.  And I can't see WHY this made him so angry.
> (I KNOW why it made me angry.)
> 
> Well, sorry to be so verbose.

No need to apologize, this is a COBOL NG.

Bill Lynch :-)
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

_(reply depth: 5)_

- **From:** Charles F Hankel <charles@hankel.mersinet.co.uk>
- **Date:** 1998-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360564CC.5861B32B@hankel.mersinet.co.uk>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <01bddc8c$8d2b4fc0$2c050380@s70> <O#2ZbXi39GA.297@upnetnews03> <35FC730E.7614@bellsouth.net> <35FE02DE.77AF1F92@att.net>`

```
Bill Lynch wrote:
> 
> Kitty Carr wrote:
…[13 more quoted lines elided]…
> structured"? I don't see it.

What annoys me most about when some people spout forth about
"structured", they are actually talking of a particular method of
structuring and seem to feel that any other form of structuring is not
structuring.
```

#### ↳ Re: Paragraphs vs Sections

- **From:** Bob Berman <bberman@netbox.com>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35F7D95D.5346@netbox.com>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com>`

```
William M. Klein wrote:
> 
> I just thought I would put out a post with a subject line that reflects the
…[27 more quoted lines elided]…
> recommend for new code.

I agree strongly with item 1. Combining the two is terribly confusing to
read.
Without the availability of EXIT PARAGRAPH (or section), I'm not sure
that you can achieve #2, for the GO TO EXIT is the only other early exit
from a paragraph, and that then requires a Perform Thru.

Bob
```

##### ↳ ↳ Re: Paragraphs vs Sections

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t9f5h$t22@dfw-ixnews4.ix.netcom.com>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <35F7D95D.5346@netbox.com>`

```

Bob Berman wrote in message <35F7D95D.5346@netbox.com>...
  <snip>
>>
>> 1) Use ONLY paragraphs or ONLY sections - no combination of the two in
the
>> same program
>>
>> 2) NEVER allow the THRU option of the PERFORM verb
>>
  <snip>
>I agree strongly with item 1. Combining the two is terribly confusing to
>read.
…[4 more quoted lines elided]…
>Bob


If you use the
    conditional-statement
         on exception-phrase
               some logic
         not on exception-phrase
              lots more logic
    end-conditional-statement

structure, then you still should NOT have to use either a GO TO <exit> or an
Exit Paragraph/Section - and you still should be able to avoid those old
"repeated IF bad-flag-not-on" structures.   I still prefer the Exit
Paragraph/Section syntax, but the other does provide the required
functionality while still providing easy (in my opinion) source code to
maintain and understand.
```

##### ↳ ↳ Simulating EXIT PARAGRAPH with SECTION (was: Re: Paragraphs vs Sections)

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kEPJ1.134$Wc3.564438@news1.atlantic.net>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <35F7D95D.5346@netbox.com>`

```

One could use SECTIONs only by using using a single paragraph,
of the same name, at the end of each section, such as,
EXIT-SECTION. The resulting code would look like:

            ....
            PERFORM 0100-section-name
            ....

        0100-section-name SECTION.
            ...
            IF some-condition
                ....
                GO TO EXIT-SECTION.
            ....

        EXIT-SECTION.
            EXIT.

The GO TO EXIT-SECTION, without qualification, would always
branch to the EXIT-SECTION paragraph of the section containing
the GO TO. This would also be easy to modify later should one wish
to convert to EXIT SECTION.

Just a thought!

Bob Berman wrote in message <35F7D95D.5346@netbox.com>...
>William M. Klein wrote:
>>
>> As far as the actual Section vs Paragraph discussion go, my PERSONAL
opinion
>> is that if you follow this rules you will have an easily maintainable
>> program with minimal error possibilities,
>>
>> 1) Use ONLY paragraphs or ONLY sections - no combination of the two in
the
>> same program
>>
>> 2) NEVER allow the THRU option of the PERFORM verb
>>
>> 3) Use the "EXIT SECTION" or "EXIT PARAGRAPH" syntax (if available) over
the
>> GO TO <procedure-name-exit> statement.
>>
…[8 more quoted lines elided]…
>
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

##### ↳ ↳ Combining SECTIONs and PARAGRAPHs readably (was: Re: Paragraphs vs Sections)

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lEPJ1.135$Wc3.564438@news1.atlantic.net>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <35F7D95D.5346@netbox.com>`

```

Use SECTION as the primary organization and use a prefix, such as
a number, on all section names. Do not use prefixes on paragraph
names. Use paragraphs only to break up complicated logic in the
sections. With the exception of the "dummy" paragraph at the
beginning of the section, do not use paragraphs to perform other
paragraphs. For example,

           ...
           PERFORM 0100-section-name
           ...

       0100-section-name SECTION.
           ...
           EVALUATE TRUE
             WHEN condition-1
               PERFORM nested-paragraph-1
             WHEN condition-2
               PERFORM nested-paragraph-2
             ...
             WHEN condition-xx
               PERFORM nested-paragraph-xx
           END-EVALUATE
           ...
           GO TO EXIT-SECTION.

       nested-paragraph-1.
           ...

       nested-paragraph-2.
           ....

       nested-paragraph-xx.
           ....

       EXIT-SECTION.
           EXIT.

Just a thought!

Bob Berman wrote in message <35F7D95D.5346@netbox.com>...
>William M. Klein wrote:
>>
>> As far as the actual Section vs Paragraph discussion go, my PERSONAL
opinion
>> is that if you follow this rules you will have an easily maintainable
>> program with minimal error possibilities,
>>
>> 1) Use ONLY paragraphs or ONLY sections - no combination of the two in
the
>> same program
>>
>> 2) NEVER allow the THRU option of the PERFORM verb
>>
>> 3) Use the "EXIT SECTION" or "EXIT PARAGRAPH" syntax (if available) over
the
>> GO TO <procedure-name-exit> statement.
>>
…[8 more quoted lines elided]…
>
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

##### ↳ ↳ Re: Paragraphs vs Sections

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298253.2572.14975@kcbbs.gen.nz>`
- **References:** `<35F7D95D.5346@netbox.com>`

```
In message <<35F7D95D.5346@netbox.com>> Bob Berman <bberman@netbox.com> writes:
> > 
> > 2) NEVER allow the THRU option of the PERFORM verb
…[5 more quoted lines elided]…
> from a paragraph, and that then requires a Perform Thru.


Why do you think that you _need_ an 'early exit' from a performed
paragraph ?

It may be that you think of PERFORMs as necessarily being of a
large area, for example if you are used to having, say,
 
           PERFORM B000-Process-Transactions
               UNTIL End-Of-Transaction-File

Then it would seem reasonable that B000-... is more than half
the code, any need to 'bail out', such as end of file would
be a reasonable point to need a GO TO Exit.  Once the 
physical position of the B000-Start and B000-Exit are
established then all else goes between them.

This may well be a reasonable structure, but it is imposed
by the processes that leads to the need to have a 'bail out'
in the first place.

If, however, you start with the idea that a GO TO Exit is
_not_ required and PERFORM paragraph is the only structure
then the _cost_ of creating new blocks of code (paragraphs)
becomes much less and the structure can be much simplified.

As an extreme case it may be that you visualise (don't take
this as a criticism, it is only an observation):

        B000-Process-Transactions SECTION.
        B000-Start.
 
            READ Transaction-File
                 AT END GO TO B000-Exit
            .

             lots of code goes here

         B00-Exit.

But why is it necessary to 'bracket' the code ?

Typically a PERFORM paragraph only structure is:


          PERFORM Process-Transactions
               UNTIL some-end-marker


           .....
      Process-Transactions.

          READ Transaction-File
              AT END
                   set flag, or move HIGH-VALUES
              NOT AT END
              EVALUATE Transaction-Type
              WHEN "R"
                    PERFORM Process-Receipt
              WHEN "I"
                    ....
          END-READ.

      Process-Receipt.

The scope of (size of in lines) of each performed paragraph
is small, there is no need to 'bail out' to prevent wandering
down to the end of the block, because there is no 'end'.
The structuring is done in much smaller blocks.

The argument that without a 'GO TO Exit' or 'EXIT section'
there must necessarily be large indents of IF ... ELSE is
also based on performs of huge blocks.  These blocks are
imposed by the 'need' to have an Exit paragraph to GO TO
and are not the result of trying to avoid GO TO.

When a change is made in the mind-set from 'I am going to
PERFORM 1000 lines' to 'I am going to PERFORM 20 lines'
then the avoidance of deeply nested IF .. ELSE is 
automatic, the 'need' for a GO TO Exit is void, the
structure of the program changes, IMHO to beng far
more maintainable.
```

##### ↳ ↳ Re: Paragraphs vs Sections

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#$JGGri39GA.169@upnetnews03>`
- **References:** `<6t7hhc$9g4@sjx-ixn3.ix.netcom.com> <35F7D95D.5346@netbox.com>`

```

Bob Berman wrote in message <35F7D95D.5346@netbox.com>...
>William M. Klein wrote:
>>
>> I just thought I would put out a post with a subject line that reflects
the
>> trend of a recent thread.  Now my question is,
>>
…[7 more quoted lines elided]…
>> If you check DejaNews, I think each of these topics gets "beaten to
death"
>> frequently (about every 3 to 6 months - although I will say that the
"COBOL
>> vs Perl" discussion is new, but reads very similar to previous "COBOL vs
>> Rexx" discussions).
>>
>> As far as the actual Section vs Paragraph discussion go, my PERSONAL
opinion
>> is that if you follow this rules you will have an easily maintainable
>> program with minimal error possibilities,
>>
>> 1) Use ONLY paragraphs or ONLY sections - no combination of the two in
the
>> same program
>>
>> 2) NEVER allow the THRU option of the PERFORM verb
>>
>> 3) Use the "EXIT SECTION" or "EXIT PARAGRAPH" syntax (if available) over
the
>> GO TO <procedure-name-exit> statement.
>>
…[7 more quoted lines elided]…
>from a paragraph, and that then requires a Perform Thru.


#2 can be achieved if your shop standard do not allow any "early exit" from
a paragraph, but you have to design your algorithms a bit more studiously.

On the other hand, disregard of #2 allows future maintenance programmers to
slip in additional paragraphs, or additional GO TO's,  within the performed
range too easily.  Such modifications often lead to excessive debugging
practice.
```

###### ↳ ↳ ↳ Re: Paragraphs vs Sections

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298254.74211.14563@kcbbs.gen.nz>`
- **References:** `<#$JGGri39GA.169@upnetnews03>`

```
In message <<#$JGGri39GA.169@upnetnews03>> "Dennis J. Minette" <dennis_minette@email.msn.com> writes:
> >
> >I agree strongly with item 1. Combining the two is terribly confusing to
…[7 more quoted lines elided]…
> a paragraph, but you have to design your algorithms a bit more studiously.

Both styles: of allowing early exit via a GO TO, or of enforcing
paragraph only in performs are idiomatic.  The idiom just
happens to be different.  Moving from one to the other
requires learning and understanding that these are different
idioms and to apply them appropriately.

Many of the arguments against the 'other' style arises because
they want to use the idiom they are used to and cannot see
how it will fit (because it won't), and they can't adjust
to a different idiom without learning it first (naturally).

Once either idiom is correctly adjusted to there is no
further need to 'design more studiously', this is only
necessary if the algorithm is first designed in one idiom
and then has to be adjusted to the other (whichever way
it goes).

> 
> On the other hand, disregard of #2 allows future maintenance programmers to
> slip in additional paragraphs, or additional GO TO's,  within the performed
> range too easily.  Such modifications often lead to excessive debugging
> practice.


In many standards, the ability to use GO TO to an exit paragraph
should never be extended to allow a GO TO to any arbitrary
paragraph - such is the path to anarchy.  Thus each SECTION
should have at most two paragraphs, a Start immediately
after the section header and an Exit which may only be
followed by EXIT. and then the next SECTION header.

It would be nice to have a compiler option to enforce this
as I prefer to have the compiler tell me the program is
not going to work _before_ I waste my time testing.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
