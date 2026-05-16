[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Homework - A Thought

_43 messages · 23 participants · 2000-05_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### Homework - A Thought

- **From:** docdwarf@clark.net ()
- **Date:** 2000-05-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net>`

```

As some folks might have gathered... I get kind of 'curt' with folks who
ask others to do their homework for them.  My response is a simple request
of 'Please do your own homework' and that's enough for me.

Others, I've noticed, cannot help themselves and just *have* to post
code... it has been pointed out that this harms the student, in the long
run.

Lately I've noticed another shift... one towards using techniques of
complexity and subtlety *far* beyond the capabilities of someone taking
Introdutory COBOL (101).  This is kind of... sly, as when a student
presents this kind of work as his/her own the instructor's first impulse
should be 'WHERE DID YOU LEARN TO DO THIS?!?'.

Not all instructors are so... diligent, though, and with that in mind I
make the following suggestion.  Some folks are capable of 'faking it above
their station', of fast-talking their way into a perception of
competence... so I'd suggest that if you *must* post code that you take it
in the *opposite* direction, to something which a 101-level student
*cannot* fake.

What might this be?  Simple.  Unless it is absolutely necessary use *no*
constructs beyond the COBOL '68.  Make sure you type in ALL CAPS and that
you use the most rigid, arcane naming conventions you've found... things
like:

01  B1577QHR-MSTR-REC.
    05  B1577QHR-MSTR-REC-KEY.
        10  B1577QHR-MSTR-REC-KEY-FIRST4 PIC X(004).
        10  B1577QHR-MSTR-REC-KEY-SEQNO  PIC 9(009).
        10  B1577QHR-MSTR-REC-KEY-NEXT4  PIC X(007).

... and ...

77  WS-WK-NUM-CHAR-NO-CHARACTERS PIC X(15).

... and ...

    PERFORM E92117B-FMT-HDR-REC-NUMERICS THRU E92117B-EX.

... and suchlike; make it like the worst code you ever saw run through a
restructuring engine.  Add a few more simple rules:

must contain at least two 66 RENAMES

must contain at least one GO TO DEPENDING ON

must freely intermingle paragraphs and sections

... and you're on the way to giving the poor student something that will
actually *work* - unlike, say, giving a few WRITE... AFTER POSITIONING -
but will more likely arouse the instructor's attention and *not* allow for
a fast talking-through.

Comments?  Suggestions?

DD
```

#### ↳ Re: Homework - A Thought

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8faajv$qpo$1@slb3.atl.mindspring.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net>`

```
My PERSONAL position on homework posts are:

1) If the person asking doesn't show us much in the way of what they have
done already, I have no problem telling them the "topic" to look under in
their own reference material.  (Certainly phrases like "reference
modification" and "tables" - rather than arrays - may be "strange" to a new
student, and I have NO problem giving them help finding the answer
themselves.)

2) If the person actually posts code (even an extract) and tells us what
problem he/she is having, I don't see much problem in pointing out where the
"bug" is.  There are time, however, for my OWN "ease," it is simpler to just
tell them how to fix the problem.  I know that this is "cheating" the student
of a valuable learning tool, but it does (sometimes) make my life simpler.
```

#### ↳ Re: Homework - A Thought

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-05-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fassu$ec0$1@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net>`

```
Ouch.   Remind me not to get you mad.



<docdwarf@clark.net> wrote in message
news:WL1S4.22368$0o4.237073@iad-read.news.verio.net...
>
> As some folks might have gathered... I get kind of 'curt' with
folks who
> ask others to do their homework for them.  My response is a
simple request
> of 'Please do your own homework' and that's enough for me.
>
> Others, I've noticed, cannot help themselves and just *have* to
post
> code... it has been pointed out that this harms the student, in
the long
> run.
>
> Lately I've noticed another shift... one towards using
techniques of
> complexity and subtlety *far* beyond the capabilities of
someone taking
> Introdutory COBOL (101).  This is kind of... sly, as when a
student
> presents this kind of work as his/her own the instructor's
first impulse
> should be 'WHERE DID YOU LEARN TO DO THIS?!?'.
>
> Not all instructors are so... diligent, though, and with that
in mind I
> make the following suggestion.  Some folks are capable of
'faking it above
> their station', of fast-talking their way into a perception of
> competence... so I'd suggest that if you *must* post code that
you take it
> in the *opposite* direction, to something which a 101-level
student
> *cannot* fake.
>
> What might this be?  Simple.  Unless it is absolutely necessary
use *no*
> constructs beyond the COBOL '68.  Make sure you type in ALL
CAPS and that
> you use the most rigid, arcane naming conventions you've
found... things
> like:
>
…[14 more quoted lines elided]…
> ... and suchlike; make it like the worst code you ever saw run
through a
> restructuring engine.  Add a few more simple rules:
>
…[6 more quoted lines elided]…
> ... and you're on the way to giving the poor student something
that will
> actually *work* - unlike, say, giving a few WRITE... AFTER
POSITIONING -
> but will more likely arouse the instructor's attention and
*not* allow for
> a fast talking-through.
>
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Homework - A Thought

- **From:** docdwarf@clark.net ()
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<V1oS4.22638$0o4.243956@iad-read.news.verio.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <8fassu$ec0$1@ssauraaa-i-1.production.compuserve.com>`

```
In article <8fassu$ec0$1@ssauraaa-i-1.production.compuserve.com>,
Russell Styles <RWSTYLES@COMPUSERVE.COM> wrote:
>Ouch.   Remind me not to get you mad.

Oh, don't worry about *that*... I am *very* slow to anger.

(... and besides... really, you'd *never* feel it... hee HEE Hee hee hee)

DD

><docdwarf@clark.net> wrote in message
>news:WL1S4.22368$0o4.237073@iad-read.news.verio.net...
…[79 more quoted lines elided]…
>
```

#### ↳ Re: Homework - A Thought

- **From:** Adrian Birkett <abirkett.@unnecessary.csc.com>
- **Date:** 2000-05-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391990CC.D5A621C1@unnecessary.csc.com>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net>`

```
Normally, I get annoyed at the people who post curt messages to
newsgroups - if a person wants help and is asking for it they we should
at least be civil about the reply. If the person is blatantly asking for
others to do their homework for them then it's their loss when it comes
to exam-time.

That said, I completely agree with your proposed method of reply.
Especially with COBOL. It is very easy to make a simple piece of code
LOOK a lot more complex than it actually is.

Ade

PS: It's been a while, do examiners still fail you for having 'GOTO' in
your code?

===== My own opinion, not that of my employer =====
```

##### ↳ ↳ Re: Homework - A Thought

- **From:** docdwarf@clark.net ()
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<M3oS4.22642$0o4.243546@iad-read.news.verio.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <391990CC.D5A621C1@unnecessary.csc.com>`

```
In article <391990CC.D5A621C1@unnecessary.csc.com>,
Adrian Birkett  <abirkett.@unnecessary.csc.com> wrote:
>Normally, I get annoyed at the people who post curt messages to
>newsgroups - if a person wants help and is asking for it they we should
>at least be civil about the reply.

'Curt' is not necessarily 'uncivil'... and I *always* use a 'please'.

>If the person is blatantly asking for
>others to do their homework for them then it's their loss when it comes
>to exam-time.

An Olde Proverbe has something like 'Borrowed clothes and borrowed brains
are always found out'.

>
>That said, I completely agree with your proposed method of reply.

Then, as Wilde said... one of us *must* be wrong!

DD
```

##### ↳ ↳ Re: Homework - A Thought

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391A7F8F.57A5963A@melbpc.org.au>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <391990CC.D5A621C1@unnecessary.csc.com>`

```
Once I has a mark taken off for not using a goto (too inefficient
I was told),

Tim Josling


Adrian Birkett wrote:
> 
> Normally, I get annoyed at the people who post curt messages to
…[14 more quoted lines elided]…
> ===== My own opinion, not that of my employer =====
```

##### ↳ ↳ Re: Homework - A Thought

- **From:** "Tom Wright" <twright@larimore.net>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0hzS4.7$X45.206837@news1.i1.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <391990CC.D5A621C1@unnecessary.csc.com>`

```
Thanks for the response guys...it was a question my teacher had asked me but
I didn't know the answer....thanks for the
help...............................................
..................................................Just joking :)

Tom Wright
twright@@@larimore.net
Adrian Birkett <abirkett.@unnecessary.csc.com> wrote in message
news:391990CC.D5A621C1@unnecessary.csc.com...
> Normally, I get annoyed at the people who post curt messages to
> newsgroups - if a person wants help and is asking for it they we should
…[14 more quoted lines elided]…
>
```

#### ↳ Re: Homework - A Thought

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-05-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fc96h$3cp$1@news.inet.tele.dk>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net>`

```
It's not my cup of tea.

Normally we should not send code.

We should never send code from outdated standards or give ugly code as help.
That is not help but terror.

Regards
Ib
docdwarf@clark.net skrev i meddelelsen ...
>
>As some folks might have gathered... I get kind of 'curt' with folks who
…[56 more quoted lines elided]…
>
```

#### ↳ Re: Homework - A Thought

- **From:** "Tom Wright" <twright@larimore.net>
- **Date:** 2000-05-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ealS4.10$mk.344323@news1.i1.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net>`

```
I thought we weren't supposed to use GO TO's in a structured programming
language??  :)
Tom Wright
twright@@@larimore.net
<docdwarf@clark.net> wrote in message
news:WL1S4.22368$0o4.237073@iad-read.news.verio.net...
>
> As some folks might have gathered... I get kind of 'curt' with folks who
…[56 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Homework - A Thought

- **From:** docdwarf@clark.net ()
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B5oS4.22643$0o4.243517@iad-read.news.verio.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net>`

```
In article <ealS4.10$mk.344323@news1.i1.net>,
Tom Wright <twright@larimore.net> wrote:
>I thought we weren't supposed to use GO TO's in a structured programming
>language??  :)

Plain, ordinary, unadorned GO TOs, no... but it is quite all right to use
a GO TO DEPENDING ON because it is really just a primitve antecedant to
the EVALUATE.

(... must ... keep... straight... face...)

DD

>Tom Wright
>twright@@@larimore.net
…[62 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Homework - A Thought

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<27xS4.36$cc6.16148@dfiatx1-snr1.gtei.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <B5oS4.22643$0o4.243517@iad-read.news.verio.net>`

```
<docdwarf@clark.net> wrote in message
news:B5oS4.22643$0o4.243517@iad-read.news.verio.net...
> In article <ealS4.10$mk.344323@news1.i1.net>,
> Tom Wright <twright@larimore.net> wrote:
…[6 more quoted lines elided]…
>

What we really need for you, Doc is a new flow control mechanism:

GO TO DEPENDING ON ALTERED STATE OF ....

MCM
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 4)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fgshn$n6u$1@nnrp1.deja.com>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <B5oS4.22643$0o4.243517@iad-read.news.verio.net> <27xS4.36$cc6.16148@dfiatx1-snr1.gtei.net>`

```
In article <27xS4.36$cc6.16148@dfiatx1-snr1.gtei.net>,> What we really
need for you, Doc is a new flow control mechanism:
>
> GO TO DEPENDING ON ALTERED STATE OF ....
>
> MCM

Or, GO TO ANOTHER-FORUM.

Thanks

TOny Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 4)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<inIS4.22789$0o4.251183@iad-read.news.verio.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <B5oS4.22643$0o4.243517@iad-read.news.verio.net> <27xS4.36$cc6.16148@dfiatx1-snr1.gtei.net>`

```
In article <27xS4.36$cc6.16148@dfiatx1-snr1.gtei.net>,
Michael Mattias <michael.mattias@gte.net> wrote:
><docdwarf@clark.net> wrote in message
>news:B5oS4.22643$0o4.243517@iad-read.news.verio.net...
…[12 more quoted lines elided]…
>GO TO DEPENDING ON ALTERED STATE OF ....

Needed?  Some might that it already exists!

DD
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 5)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391b91af.7523023@news.cox-internet.com>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <B5oS4.22643$0o4.243517@iad-read.news.verio.net> <27xS4.36$cc6.16148@dfiatx1-snr1.gtei.net> <inIS4.22789$0o4.251183@iad-read.news.verio.net>`

```
On Fri, 12 May 2000 00:37:34 GMT, docdwarf@clark.net () wrote:

>
>>
>>GO TO DEPENDING ON ALTERED STATE OF ....
>
>Needed?  Some might that it already exists!


We should ask my boss to post the full version of the current payroll
time card processing program.  I get woozy just thinking about it.
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 4)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fg08o$p8i$1@news.igs.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <B5oS4.22643$0o4.243517@iad-read.news.verio.net> <27xS4.36$cc6.16148@dfiatx1-snr1.gtei.net>`

```

Michael Mattias wrote in message
<27xS4.36$cc6.16148@dfiatx1-snr1.gtei.net>...
><docdwarf@clark.net> wrote in message
>news:B5oS4.22643$0o4.243517@iad-read.news.verio.net...
…[13 more quoted lines elided]…
>

Actually, all my my code goes to depending on the altered state of this
programmer.  Anybody trained in the sixties understands that sort of code
very well.

;<)
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 5)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fg2n4$rv6$1@newssvr03-int.news.prodigy.com>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <B5oS4.22643$0o4.243517@iad-read.news.verio.net> <27xS4.36$cc6.16148@dfiatx1-snr1.gtei.net> <8fg08o$p8i$1@news.igs.net>`

```

The 200 hour self-study COBOL course I learned from in 1974 included several
programs to be written.  One of them actually "instructed" us to use an
"ALTER GO TO" statement!  I personally don't mind seeing a well-written GO
TO DEPENDING ON statement.  I don't use them any more, but before the
EVALUATE statement became available, it was the next best thing.  GO TO
DEPENDING ONs aren't that bad as long as they all converge at a common exit
point.

donald tees <donald@willmack.com> wrote in message
news:8fg08o$p8i$1@news.igs.net...
> Actually, all my my code goes to depending on the altered state of this
> programmer.  Anybody trained in the sixties understands that sort of code
> very well.
>
> ;<)
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 6)_

- **From:** aflinsch <avflinsch@att.net>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391BFC88.561D1433@att.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <B5oS4.22643$0o4.243517@iad-read.news.verio.net> <27xS4.36$cc6.16148@dfiatx1-snr1.gtei.net> <8fg08o$p8i$1@news.igs.net> <8fg2n4$rv6$1@newssvr03-int.news.prodigy.com>`

```
Terry Heinze wrote:

> "ALTER GO TO" statement!  I personally don't mind seeing a well-written GO
> TO DEPENDING ON statement.  I don't use them any more, but before the
…[3 more quoted lines elided]…
> 
The last time I saw one of those was about 10 years ago. The actual
code was

GO TO WEEK1-PROCESS,
      WEEK2-PROCESS,
      WEEK3-PROCESS,
      WEEK4-PROCESS DEPENDING ON PHASE-OF-THE-MOON

which actually made sense in a twisted sort of way..
```

###### ↳ ↳ ↳ Re: Homework - A Thought

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391AB02F.72F9F2A7@cusys.edu>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <B5oS4.22643$0o4.243517@iad-read.news.verio.net>`

```
docdwarf@clark.net wrote:
> 

> >I thought we weren't supposed to use GO TO's in a structured programming
> >language??  :)
…[7 more quoted lines elided]…
> DD

OK, straight face on.  I used GO TO DEPENDING a couple of times, but not
in the last 30 years.  But unless my optimizer says no, I like doing a
GO TO ABORT-ROUTINE, because I like honesty.  If I'm not coming back, it
is a GO TO.  I abhor any and all GO TO statements which do not exit the
program, even though I have to live with them sometimes.
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 4)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EpDS4.22751$0o4.249495@iad-read.news.verio.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <B5oS4.22643$0o4.243517@iad-read.news.verio.net> <391AB02F.72F9F2A7@cusys.edu>`

```
In article <391AB02F.72F9F2A7@cusys.edu>,
Howard Brazee  <Please, do, not, e-mail, replies, to, Howard, Brazee, post,
 	them!!> wrote:
>docdwarf@clark.net wrote:
>> 
…[13 more quoted lines elided]…
>in the last 30 years.

I last used it about 7 - 8 years ago... but I've told that story here
before, if you want me to relate it to you then bounce me an email.

[snip of nascent GO TO war]

DD
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 4)_

- **From:** Eddie White <eddiewhite@hotmail.com>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fh54t$197$1@nnrp1.deja.com>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <B5oS4.22643$0o4.243517@iad-read.news.verio.net> <391AB02F.72F9F2A7@cusys.edu>`

```
In article <391AB02F.72F9F2A7@cusys.edu>,
  Please, do, not, e-mail, replies, to, Howard, Brazee, post, them!!
wrote:
> docdwarf@clark.net wrote:
> >
>
> > >I thought we weren't supposed to use GO TO's in a structured
programming
> > >language??  :)
> >
> > Plain, ordinary, unadorned GO TOs, no... but it is quite all right
to use
> > a GO TO DEPENDING ON because it is really just a primitve antecedant
to
> > the EVALUATE.
> >
…[4 more quoted lines elided]…
> OK, straight face on.  I used GO TO DEPENDING a couple of times, but
not
> in the last 30 years.  But unless my optimizer says no, I like doing a
> GO TO ABORT-ROUTINE, because I like honesty.  If I'm not coming back,
it
> is a GO TO.  I abhor any and all GO TO statements which do not exit
the
> program, even though I have to live with them sometimes.
>

When I was in school in '84 & '85, we were not allowed to use GO TO at
all.  When I got my first Cobol programming job in '86, the emphasis was
on clarity in the code.  I learned to use GO TO very sparingly, only to
jump to a specified exit point (PERFORM A-PARAGRAPH THRU ITS-EXIT).  I
did, over a dozen years as a programmer, maintain nearly every style of
COBOL program written since the 1960s, from straight-line fallthru code
to completely unstructured spaghetti code to pure structured code to a
total mishmash of styles in the same 15 year old program patched by a
cast of thousands.

There are really questions whose answers determine the quality of any
program:  First, does the program solve the business problem it was
written for?  Second, does the program run efficiently?  Third, is the
program easily maintained?  If the answer to all three questions is yes,
then the use of GO TO, or not, is a matter of applicable shop standards
(which do evolve over time) and the individual programmer's coding style
and preferences.

Just the two cents worth of a DBA who used to be a pretty fair COBOL
slinger.

Eddie White


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: Homework - A Thought

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391A12AF.AA24B4FE@home.com>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net>`

```


Tom Wright wrote:
> 
> I thought we weren't supposed to use GO TO's in a structured programming
> language??  :)

The word is if you do then you will get convoluted spaghetti code. But
there are lots of 'good' programmers who still use it in the following
type of tight loop :-

	READ-NEXT-PARAGRAPH.

	Read next record at end set FileFinished to true
			 Not at end
			  if record-type < 3
			     goto Read-Next-Paragraph
			  else process.........
			  End-if
	End-read.
     
Most times you don't need to use GO TO - but above tight loop could
hardly be considered ambiguous in such a short paragraph.

We would all probably agree don't use ALTER - that's like giving a
maniac a line-switch on a railway line :-). (Still, I think ALTER is or
will be dead - I don't know because I've never used it).

Jimmy
```

###### ↳ ↳ ↳ Re: Homework - A Thought

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391b9214.7624268@news.cox-internet.com>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <391A12AF.AA24B4FE@home.com>`

```
On Thu, 11 May 2000 01:54:58 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:


>We would all probably agree don't use ALTER - that's like giving a
>maniac a line-switch on a railway line :-). (Still, I think ALTER is or
>will be dead - I don't know because I've never used it).
>

It's not extinct yet.
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fg6b2$kfl$1@slb7.atl.mindspring.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <391A12AF.AA24B4FE@home.com> <391b9214.7624268@news.cox-internet.com>`

```
"Thane Hubbell" <thaneH@softwaresimple.com> wrote in message
news:391b9214.7624268@news.cox-internet.com...
> On Thu, 11 May 2000 01:54:58 GMT, "James J. Gavan" <jjgavan@home.com>
> wrote:
…[7 more quoted lines elided]…
> It's not extinct yet.

It may not be "extinct" - but it is "obsolete" and (happy to say) missing
from the draft revision of the Standard.

NOW, I do hear "rumors" of many vendors who plan on keeping it on as an
"extension" after the revision is approved - because they are afraid of
"breaking existing code".  It will be interesting to see what happens to this
(and the other OBSOLETE features).
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 5)_

- **From:** Charles F Hankel <nieuws@hankel.freedombird.net>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tn9oissh5q7li5q8iiplm14j8vsmh1glva@4ax.com>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <391A12AF.AA24B4FE@home.com> <391b9214.7624268@news.cox-internet.com> <8fg6b2$kfl$1@slb7.atl.mindspring.net>`

```
In an idle moment, "William M. Klein" <wmklein@nospam.ix.netcom.com>
wrote:

[ALTER...TO PROCEED TO]
>It may not be "extinct" - but it is "obsolete" and (happy to say) missing
>from the draft revision of the Standard.
…[4 more quoted lines elided]…
>(and the other OBSOLETE features).

I saw a whole bunch of them when I was doing some Y2K stuff - it was
almost like a homecoming, looking at code that had been born a quarter
of a century ago and that had never been altered by the ravages of
time.  It was Y2K compliant as well, and so continues to work - a
legacy to the 21st Century.

Coincidentally, I was one of the original programmers - the suite was
written in COBOL E.  It compiled under LE but to a much larger object
program which is paradoxical, considering that a rewrite/re-edit of
one of the modules produced a smaller source program[1].  Fortunately,
the recompiles weren't needed so I retained the original object code
as well - optimized by inactivity.

It was an odd experience, as was making the decision to leave them
alone - it felt almost like conserving a piece of antique furniture
OK some of the programs had been changed for the usual business
reasons but over half of the programs were in their original states.

[1] For those unfamiliar with COBOL E, it required the reserved words
and some clauses to be written in full such as COMPUTATIONAL-3 where
we now write COMP-3 without a second thought.
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 6)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393016A0.5C8CAE83@istar.ca>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <391A12AF.AA24B4FE@home.com> <391b9214.7624268@news.cox-internet.com> <8fg6b2$kfl$1@slb7.atl.mindspring.net> <tn9oissh5q7li5q8iiplm14j8vsmh1glva@4ax.com>`

```
The increased code may come from several things because the
optimizations now concentrate on speed of execution rather than program
size.  In specific, the IBM compilers may well replace multiple PERFORMs
of any paragraph that does not contain a GO TO with multiple instance of
that paragraph in line to optimize cache use.  Some of the code is
greater because the new default is RENT (re-entrant) as opposed to the
use of non reentrant code with the earlier compilers.  Replacing the
ALTERs and GO TOs with structured code may help both with compile times
and module sizes.  Also check the compile options to make sure of the
right optimization and results.  

I well remember inflicting code in the payroll and marketing systems
with ALTER statements and GO TO switches instead of PERFORMs.  Thank
heaven the payroll programs hit the bit bucket in the late 1980's
(replaced by a package) and I hope they finally killed the marketing
programs and replaced them with something that better meets the needs of
the organization.  Knowing what I know now, even with the same
constraints I faced then (16 - 24K partitions, 1600 BPI tape drives and
28 meg disks) I would make every effort to obtain the same efficiencies
with structured code and no ALTER verbs.

Clark Morris, CFM Technical Programming Services Inc. cfmtech@istar.ca
Charles F Hankel wrote:
> 
> In an idle moment, "William M. Klein" <wmklein@nospam.ix.netcom.com>
…[31 more quoted lines elided]…
> we now write COMP-3 without a second thought.
```

##### ↳ ↳ Re: Homework - A Thought

- **From:** "Paul M. Dorfman" <sashole@mediaone.net>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391A43E9.2269AD2B@mediaone.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net>`

```
Tom,

There is nothing wrong with GO TO per se in _any_ language, including COBOL. But
there is a lot of wrong about morons whose marginal thinking is confined between
the covers of a shop standard. Guns do not kill, people do. Getting the drift?
;-)

Another amazing misconception is the common notion (probably acquired from the
title of the obtuse Stern's book) that COBOL is a structured language. IT IS
_NOT_: COBOL is a totally, completely _unstructured_ language. This is exactly
the reason why COBOL students are taught to write COBOL programs in a way
emulating structured programming. A structured language is one that simply
_cannot_ be written in an unstructured manner. Ada is an example. PL/I is also
unstructured, only it goes a longer way to _impose_ a  structure upon a
programmer.

Having said that, I'm not trying to be judgemental by saying that structured
languages are somehow better than unstructured ones. Quite on the contrary. An
unstructured language gives me more freedom of creativity and expression. A
marginally enlightened programmer is fully able to make an educated decision
about using a GO TO or not by taking all the issues of clarity, efficiency, and
maintability into consideration, without a shop code censor leaning over his
shoulder.

Kind regards,
================
Paul M. Dorfman
Citibank Universal Card
Jacksonville, Fl
================

Tom Wright wrote:

> I thought we weren't supposed to use GO TO's in a structured programming
> language??  :)
…[62 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: Homework - A Thought

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fdrs9$g81$1@slb0.atl.mindspring.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <391A43E9.2269AD2B@mediaone.net>`

```
For those who "like" re-arguing the same old thing, even for those who like,
require, or otherwise "live" structured programming, one of the ongoing
debates is whether or not it is "structured" to "go to" a common (subsequent)
exit, e.g.

   Begin Structure
    If A = B
        Do loop 3 times
            do something
         End-Do
         go to structure-exit
   Else
      do something else
  End-If
  do still something else
 END STRUCTURE (aka "structure-exit")
 Do another structure

   ***

In COBOL this "translates" to a GO TO para-exit "statement" (or in the next
Standard the "exit paragraph" statement) and some people allow it in
structured code - and some do not.  If *no* other GO TOs are used, you do not
get "overlapping" GO TOs when you use this technique which is the (one of
the?) "goal" of writing structured COBOL code.
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 4)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391AB1BF.4324516C@cusys.edu>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <391A43E9.2269AD2B@mediaone.net> <8fdrs9$g81$1@slb0.atl.mindspring.net>`

```
My favorite language structures are Forth, or better yet, Action!.   

Action! was a language written by a theoretician and sold as a cartridge
for the Atari computer.  It made for fast non-compile programs, where
the very last line of code was the program (with definitions above).  It
sort of is an upside down version of a structured PROCEDURE DIVISION. 
Define the small stuff at the top and put them in memory, and then use
them by subsequent steps until you finally have a run command (I don't
remember the exact syntax - my book is at my son's house)

You can see how an interpreted language can be fast using Action! or
Forth structure.
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 5)_

- **From:** J M Pittman <jmpittmanii@mindspring.com>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391B8AB6.9C25F68F@mindspring.com>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <391A43E9.2269AD2B@mediaone.net> <8fdrs9$g81$1@slb0.atl.mindspring.net> <391AB1BF.4324516C@cusys.edu>`

```
Thats ALGOL.

Howard Brazee wrote:

> My favorite language structures are Forth, or better yet, Action!.
>
…[9 more quoted lines elided]…
> Forth structure.
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 5)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fgqc9$8d1$1@news.igs.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <391A43E9.2269AD2B@mediaone.net> <8fdrs9$g81$1@slb0.atl.mindspring.net> <391AB1BF.4324516C@cusys.edu>`

```
Howard Brazee wrote in message

>You can see how an interpreted language can be fast using Action! or
>Forth structure.

I have always liked Forth as well.  In fact, I am attempting to put together
a somewhat forth-like but very high level language written in Cobol.  The
basic idea is that a very high level system is constructed forth fashion
from low level system components. The components are fairly high level Cobol
objects, compiled as DLL's and interchangeable.
```

###### ↳ ↳ ↳ Re: Homework - A Thought

- **From:** Daniel Jacot <djacot@my-deja.com>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fe1ce$hpj$1@nnrp1.deja.com>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <391A43E9.2269AD2B@mediaone.net>`

```
In article <391A43E9.2269AD2B@mediaone.net>,
  "Paul M. Dorfman" <sashole@mediaone.net> wrote:
> Tom,
>
…[4 more quoted lines elided]…
> ;-)

<snip>

> Paul M. Dorfman
> Citibank Universal Card
> Jacksonville, Fl
> ================

Oh no, Paul, I do not agree. People almost never kill if they have to
use a knife or a hammer and they very often kill if they have a gun at
hand (intentionally or by accident).

Take them away their guns and their GOTOs and they will probably make
less faults.

Or - at least - teach them how to use guns and GOTOs and lock up both
from children and students &-)
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37xS4.37$cc6.16185@dfiatx1-snr1.gtei.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <391A43E9.2269AD2B@mediaone.net> <8fe1ce$hpj$1@nnrp1.deja.com>`

```
Daniel Jacot <djacot@my-deja.com> wrote in message
news:8fe1ce$hpj$1@nnrp1.deja.com...
> Oh no, Paul, I do not agree. People almost never kill if they have to
> use a knife or a hammer and they very often kill if they have a gun at
…[7 more quoted lines elided]…
>

Why not a compromise: child safety locks on GOTOs?

MCM
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 5)_

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ff284$7mc$1@news.inet.tele.dk>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <391A43E9.2269AD2B@mediaone.net> <8fe1ce$hpj$1@nnrp1.deja.com> <37xS4.37$cc6.16185@dfiatx1-snr1.gtei.net>`

```
And students safety locks on guns - oouch, sorry.
Regards
Ib
Michael Mattias skrev i meddelelsen
<37xS4.37$cc6.16185@dfiatx1-snr1.gtei.net>...
>Daniel Jacot <djacot@my-deja.com> wrote in message
>news:8fe1ce$hpj$1@nnrp1.deja.com...
…[16 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 5)_

- **From:** Eddie White <eddiewhite@hotmail.com>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fhmo8$krt$1@nnrp1.deja.com>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <391A43E9.2269AD2B@mediaone.net> <8fe1ce$hpj$1@nnrp1.deja.com> <37xS4.37$cc6.16185@dfiatx1-snr1.gtei.net>`

```
In article <37xS4.37$cc6.16185@dfiatx1-snr1.gtei.net>,
  "Michael Mattias" <michael.mattias@gte.net> wrote:
> Daniel Jacot <djacot@my-deja.com> wrote in message
> news:8fe1ce$hpj$1@nnrp1.deja.com...
> > Oh no, Paul, I do not agree. People almost never kill if they have
to
> > use a knife or a hammer and they very often kill if they have a gun
at
> > hand (intentionally or by accident).
> >
> > Take them away their guns and their GOTOs and they will probably
make
> > less faults.
> >
> > Or - at least - teach them how to use guns and GOTOs and lock up
both
> > from children and students &-)
> >
…[5 more quoted lines elided]…
>
If GO TOs are outlawed, only outlaws will have GO TOs.

Eddie


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fi7v0$433$1@news.igs.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <391A43E9.2269AD2B@mediaone.net> <8fe1ce$hpj$1@nnrp1.deja.com> <37xS4.37$cc6.16185@dfiatx1-snr1.gtei.net> <8fhmo8$krt$1@nnrp1.deja.com>`

```

Eddie White wrote in message <8fhmo8$krt$1@nnrp1.deja.com>...
>In article <37xS4.37$cc6.16185@dfiatx1-snr1.gtei.net>,
>  "Michael Mattias" <michael.mattias@gte.net> wrote:
…[25 more quoted lines elided]…
>

YES !!! I like that.  We outlaw programmers will be able to say  "GO TO",
and append any label we like, to anybody, anytime, anyplace.

     SO.
         GO TO YOU-KNOW-WHERE.

     YOU-KNOW-WHERE.
        ;<)
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 7)_

- **From:** Charles F Hankel <nieuws@hankel.freedombird.net>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ru9oisoqk94jmipe4s9v7ref4esd2qj3eh@4ax.com>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <391A43E9.2269AD2B@mediaone.net> <8fe1ce$hpj$1@nnrp1.deja.com> <37xS4.37$cc6.16185@dfiatx1-snr1.gtei.net> <8fhmo8$krt$1@nnrp1.deja.com> <8fi7v0$433$1@news.igs.net>`

```
In an idle moment, "donald tees" <donald@willmack.com> wrote:

>YES !!! I like that.  We outlaw programmers will be able to say  "GO TO",
>and append any label we like, to anybody, anytime, anyplace.
…[5 more quoted lines elided]…
>        ;<)

Rebel Without A Clause.
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 8)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gp6ss$l3f$1@news.igs.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <391A43E9.2269AD2B@mediaone.net> <8fe1ce$hpj$1@nnrp1.deja.com> <37xS4.37$cc6.16185@dfiatx1-snr1.gtei.net> <8fhmo8$krt$1@nnrp1.deja.com> <8fi7v0$433$1@news.igs.net> <ru9oisoqk94jmipe4s9v7ref4esd2qj3eh@4ax.com>`

```

Charles F Hankel wrote in message ...
>In an idle moment, "donald tees" <donald@willmack.com> wrote:
>
…[9 more quoted lines elided]…
>Rebel Without A Clause.


Just clause tro-phobic.
```

###### ↳ ↳ ↳ Re: Homework - A Thought

_(reply depth: 4)_

- **From:** "Paul M. Dorfman" <sashole@mediaone.net>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391B84CB.6447992D@mediaone.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <ealS4.10$mk.344323@news1.i1.net> <391A43E9.2269AD2B@mediaone.net> <8fe1ce$hpj$1@nnrp1.deja.com>`

```
Daniel Jacot wrote:

> In article <391A43E9.2269AD2B@mediaone.net>,
>   "Paul M. Dorfman" <sashole@mediaone.net> wrote:
…[17 more quoted lines elided]…
> hand (intentionally or by accident).

Needless to say, I disagree. Being kind of pragmatic because of my ex-trade
(physics) I only believe what the experiment shows, and it plainly shows
that in the places with less or no gun-banning laws violent crime is
dramatically lower. That is an experimental fact. Period.

> Take them away their guns and their GOTOs and they will probably make
> less faults.

The same pertains to them GO TOs. The word "probably" is crucial here - Its
Majesty Experiment tells otherwise. Never in the history of mankind any
prohibition failed to have the effect diametrically opposite to the one it
was intended to produce.

> Or - at least - teach them how to use guns and GOTOs and lock up both
> from children and students &-)

They will find them GO TOs, they will be looking for them the more eagerly,
the further you put them away, and they will find them before they try
their first mint julep. Homo sum, et nihil humanum me alienum essa puto.

Kind regards,
=================
Paul M. Dorfman
Jacksonville, FL
=================
```

#### ↳ Re: Homework - A Thought

- **From:** Charles Hammond <ceh1@cec.wustl.edu>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.SOL.3.96.1000511095943.3839C-100000@ritz.cec.wustl.edu>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net>`

```
I can understand the student's confusion while going to school.  Some of
the programming books I have seen that schools require a COBOL programming
student to buy look like they were written by geeks for geeks and almost
of no value to a student.  So far the only book I liked at all was a book
on COBOL 400 written for the AS400 by Wiley.  Most technical manuals for
COBOL are very short on usable examples and it is very hard to see the big
picture.

Maybe one of those learn COBOL in 24 hours books would be useful.

At the school I went to a single GO TO would get you in serious trouble
come grade time.  The school required each student to take a course in
structured programming logic as a prerequisite to taking a COBOL or other
programming course.

However the school I attend now uses a course in algorithms which is of
use if you know absolutely nothing.  They cared more about the ability to
write pseudocode than a structured technique.

Then I got a job and there were more go to statements then performs, oh
well!

Charles Hammond, BSIM Undergraduate Program

On Wed, 10 May 2000 docdwarf@clark.net wrote:

> 
> As some folks might have gathered... I get kind of 'curt' with folks who
…[58 more quoted lines elided]…
>
```

#### ↳ Re: Homework - A Thought

- **From:** "Aaron Cauley" <ac9595@sprynet.com>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fervp$d91$1@slb0.atl.mindspring.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net>`

```
I Knew you would'nt let me down. Came on looking for some of your COBOL
wisdom and here's more. I'd like to apologize for the punk comments i made
in reply to your post in reference to my asking others to *do my homework*
i've followed your advice and have been spending much more time on my
assignments and less trying to get others to do them for me.
I just recieved a grade for the last program very simple produce company
mailing list using logical file 46/50 ( lost 4pts for neatness on flow
chart)
the program produce company phone list was a bust-
 possible 200 points left  this semester program using multiple control
breaks
100pts and the final is Mon.for 100pts. - I'm sure i'll have ?'s  before
posting sure to exhaust all reference materials  and present the code i've
written
rumor has it that people in industry see graduates as being ill equipted for
todays * whatever it is* . seems like most people would be happy to show
students who are willing to learn the ropes.
by the way - *professors* seem to like different ways (things picked up)
from oth sources as long as they meet good programming standards. go tos are
not good. ac9595

<docdwarf@clark.net> wrote in message
news:WL1S4.22368$0o4.237073@iad-read.news.verio.net...
>
> As some folks might have gathered... I get kind of 'curt' with folks who
…[56 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Homework - A Thought

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fesok$2p4$1@slb6.atl.mindspring.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <8fervp$d91$1@slb0.atl.mindspring.net>`

```
If you care, "neatness in flow-charts" is NOT something that the "real world"
will care much about (or at least any sites that I know of).  In
comp.lang.cobol, we get occasional questions about these - and SOME (not
many) programmers do "sort-of" do these for their own planning when first
starting a new project.  However, NOT many shops still use them as part of
actual "application documentation".

I believe that there is "greater" interest in the real world in being able to
"convert" an analyst's or users "requirements" to decent "pseudo-code" - but
even that is (usually) more a matter of style than actual "production
requirement".

Good luck with your remaining work.
```

##### ↳ ↳ Re: Homework - A Thought

- **From:** docdwarf@clark.net ()
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3IIS4.22791$0o4.251311@iad-read.news.verio.net>`
- **References:** `<WL1S4.22368$0o4.237073@iad-read.news.verio.net> <8fervp$d91$1@slb0.atl.mindspring.net>`

```
In article <8fervp$d91$1@slb0.atl.mindspring.net>,
Aaron Cauley <ac9595@sprynet.com> wrote:
>I Knew you would'nt let me down. Came on looking for some of your COBOL
>wisdom and here's more. I'd like to apologize for the punk comments i made
…[5 more quoted lines elided]…
>chart)

A good start, aye... leaves a bit of room for improvement, of course.

Keep up the good work!

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
