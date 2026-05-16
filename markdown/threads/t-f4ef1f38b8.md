[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Java is becoming the new Cobol

_2 messages · 2 participants · 2008-01_

---

### Re: Java is becoming the new Cobol

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2008-01-11T15:46:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<47878F62.6F0F.0085.0@efirstbank.com>`

```
>>> On 1/11/2008 at 12:11 PM, in message
<13offrpnknc146@corp.supernews.com>,
tim Josling<tejgcc_nospam@westnet.com.au> wrote:
> On Fri, 11 Jan 2008 07:23:08 -0700, LX-i wrote:
> 
…[81 more quoted lines elided]…
> I hope this clarifies things.

(Note, try not to use two dashes followed by a space (not sure if you put
the space in or your email program did), because many email programs treat
things following it as part of a signature and cut them off when building
the reply.)

Anyway, interesting.  I recently implemented some changes in to our card
processing system that removed a lot of hard coding and made much of it
table driven.  It used to be that each time we implemented a new card type
(which granted, is not very often), we'd have to change dozens of programs
to handle the new card type.  Now we just add it to the "card type file" and
away we go!  All that has to change is situations that are new to this
particular card type, and aren't relevant to the other card types.  I did
this because I knew that this year (well, 2007/2008) we'd be adding two new
card types.  I did all of the work to convert to table driven processing for
the first card type, and the second one was an absolute snap to implement. 
Great stuff!

*However*, this does not always work.  We're lucky that in this card the new
card types act pretty much like the existing card types.  Just for a
different user base.  On the other hand, each time we implement a new type
of checking or savings account, or loan, there are many, many ways in which
the new type is different than existing types.  So it's not just a matter of
"selecting from a list of existing options".  Sure, that could work for many
things (is this an interest bearing account type, yes or no?, etc.).  But
each product is implemented to have a slew of new features, rather than just
a 'multiple choice' of existing features.  I suppose that if we had some
sort of vendor package that was only customizable via tables then our users
would have to live with that.  But the fact is we have an inhouse
development staff, so they are very used to asking for the moon!  :-)

Anyway, I am obviously not against table driven type processing.  I only
mention that it is not always feasible.  I do think they we should strive to
utilize it more than we do, in any case.  I personally hate writing pretty
much the same code over and over, with only minor changes!  :-)

In the defense of Java programmers, and without actually ever looking at
their code, I don't believe that the Java developers in our shop over-use
hard-coding.  I dare say that the Cobol programmers are more likely to do
that.  Of course I could be wrong on both points...

On thing that makes me bit nervous about large amounts of table driven
processing is the need to go to the database all the time for what is
generally very static data.  I know that the Java programmers are more
likely to go to databases for this type of data than the Cobol programmers
are.  I don't know what type of performance hit the Java side takes for
this, but I know that management is more sensitive to mainframe response
time than it is to web response time.  Not to say they don't care about the
web side, because they do.  Probably more and more as we 'webify'.

Frank
```

#### ↳ Re: Java is becoming the new Cobol

- **From:** tim Josling <tejgcc_nospam@westnet.com.au>
- **Date:** 2008-01-12T08:42:50
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13ogvcan7lc183@corp.supernews.com>`
- **References:** `<47878F62.6F0F.0085.0@efirstbank.com>`

```
On Fri, 11 Jan 2008 15:46:42 -0700, Frank Swarbrick wrote:

> 
> (Note, try not to use two dashes followed by a space (not sure if you put
> the space in or your email program did), because many email programs treat
> things following it as part of a signature and cut them off when building
> the reply.)

Yep, got it.

> *However*, this does not always work.  We're lucky that in this card the new
> card types act pretty much like the existing card types.

You are right. Flexibility comes at a price. That's why I would only put
in a DBMS/table if there was sufficient expectation that there could be a
need for change.

For example, I have seen some systems where interest rates are hard-coded.
These should probably be in tables as they often change.

Taking it to the other extreme, I have seen other systems where everything
is configurable in a set of tables. When a new product needs a new feature
that the tables don't support, they add that feature to the tables. 

>  Just for a
> different user base.  On the other hand, each time we implement a new type
> of checking or savings account, or loan, there are many, many ways in which
> the new type is different than existing types.  So it's not just a matter of
> "selecting from a list of existing options".

I know for a fact that it can be.

> Anyway, I am obviously not against table driven type processing.  I only
> mention that it is not always feasible.

Or desirable. Some things should be hard-coded. Some things should even be
in hardware!

> On thing that makes me bit nervous about large amounts of table driven
> processing is the need to go to the database all the time for what is
> generally very static data.

With appropriate caching techniques, this need not be a problem. You can
get a table look-up down to 100-150 instructions. 

Tim Josling

> 
> Frank
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
