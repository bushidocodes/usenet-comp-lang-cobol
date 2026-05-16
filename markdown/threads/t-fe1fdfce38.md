[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Efficiency and coding

_2 messages · 2 participants · 1998-09_

---

### Re: Efficiency and coding

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298268.80732.12776@kcbbs.gen.nz>`

```

 
Judson McClendon writes:
>
>Richard Plinston wrote:
…[3 more quoted lines elided]…
>> Anyone who knows Cobol should understand that.
 
> You view this is a completely technical question,
 
Not at all, I view it as an entirely pragmatic question to
which there is a real answer.
 
> which demonstrates a misunderstanding of human nature.
 
I don't think that I misunderstand your nature   ;-)
 
> It does not matter what the language manual says, in the final
> analysis it is a human being who will write the code, and you
> seem unaware of the significance of this.
 
Well, actually it _does_ matter what the manual says.  If the
writer is attempting to write _Cobol_ programs then they should
know the language adequately and not rely on folklore and half
remembered taboos from past decades.
 
> It is an absolute fact that ... [much hyperbolic supposition
> and speculation deleted]
 
> A practice such as you suggest is absolutely guaranteed to
> increase the probability of writing broken code,
 
_Wrong_.  Knowing the language better is guaranteed to increase
the probability of writing _correct_ code.
 
> and there is nothing in this world you can do to eliminate
> that, except avoid the practice altogether.
 
_Wrong_.  Keeping knowledge up to date plays a vital role
in improving the practice of writing programs.  There may
be _vast_ differences between various languages or large
similarities, but the convention that range checks should
be applied _first_ before using the index is universal.
 
In each language it is necessary to understand its particular
evaluation order, there is _no_ substitute.  In C, for example,
there are 15 levels precedence, each specifying the grouping, and
15 levels of associativity.  Do you write your Cobol with these
constantly in mind in case you pick up some bad habit that traps
you when you do some code in C ?
 
> This is a fact, not an opinion.
 
Yes, I think that I do understand your nature.
 
> Like I said, you can dangle over the edge all you want, but my
> intent is to write as rock solid code as I can manage.
 
Yet you seem to do so without fully knowing the language. Your
original message indicated that you did not know the ANSI85
standard for evaluation order in Cobol and now you blather on
about 'other languages' to cover up your apparently antiquated
practices based on seemingly obsolete knowledge.
```

#### ↳ Re: Efficiency and coding

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j4xP1.4234$R_4.3946298@news3.mia.bellsouth.net>`
- **References:** `<3298268.80732.12776@kcbbs.gen.nz>`

```
Richard Plinston wrote:
>
>Judson McClendon writes:
…[10 more quoted lines elided]…
>which there is a real answer.

You are just oblivious to the human element.  You can't believe
how that impresses me, Richard.  Both with your perception and
your willingness to learn.

>> which demonstrates a misunderstanding of human nature.
>
>I don't think that I misunderstand your nature   ;-)

I would agree with the first three words of that sentence.

>> It does not matter what the language manual says, in the final
>> analysis it is a human being who will write the code, and you
…[5 more quoted lines elided]…
>remembered taboos from past decades.

You misunderstand my statements either because you are obtuse, or
purposely because you just want to be obnoxious.  Actually, you
have given sufficient evidence in your posts recently to support
either hypothesis.

>> It is an absolute fact that ... [much hyperbolic supposition
>> and speculation deleted]
…[5 more quoted lines elided]…
>the probability of writing _correct_ code.

This is not about knowing the language better!  I *told* you that
you view this is a strictly technical issue.  You are obviously
so totally ignorant of the human element, that it blows right past
you without your even recognizing it, even after it is pointed out.
Very impressive, Richard, very impressive.

>> and there is nothing in this world you can do to eliminate
>> that, except avoid the practice altogether.
…[5 more quoted lines elided]…
>be applied _first_ before using the index is universal.

As I said, you obviously know little to nothing about human nature,
and how it applies to programming practice.  And you seem oblivious
to how obviously stupid that remark is, to anyone who does.  It's
okay with me that you are ignorant, Richard.  I think your remarks
are very enlightening, though not in the way that you imagine.

>In each language it is necessary to understand its particular
>evaluation order, there is _no_ substitute.  In C, for example,
>there are 15 levels precedence, each specifying the grouping, and
>15 levels of associativity.

It has escaped your notice (why am I not surprised?), but it is not
computer languages which establish evaluation order in mathematical
expressions, but universally recognized mathematical practice.  This
has absolutely nothing to do with what I was talking about.

>  Do you write your Cobol with these
>constantly in mind in case you pick up some bad habit that traps
>you when you do some code in C ?

No, I work hard at developing habits which will serve me, not trick
me.  This is because I am smart enough to know that I am not perfect.
Apparently you aren't that smart, because it is a sure bet you aren't
perfect.  Not that you would agree on that, of course.

>> This is a fact, not an opinion.
>
>Yes, I think that I do understand your nature.

Your remarks make it clear to everyone but you, what you understand
here.  And what you don't.  What I have said above is based on widely
known and easily demonstrable facts.  There is no doubt about it, to
anyone who knows.

>> Like I said, you can dangle over the edge all you want, but my
>> intent is to write as rock solid code as I can manage.
…[5 more quoted lines elided]…
>practices based on seemingly obsolete knowledge.

Only seemingly obsolete to someone who hasn't a clue about the real
issue here.  You are apparently unaware (as you are of so many other
things) that many, many MIS shops do *not* use the latest compiler?
Richard, I have been examining code from compilers for a long time.
I have been studying and programming in COBOL, and many other
languages, for a long time.  I am aware that every single COBOL
compiler I ever worked with generated code which evaluated logical
expressions in the strict order they were coded.  If all compilers
were required to do so, as they should have been from the beginning,
I would agree that you could test limits and end conditions in the
same statement.  But the fact is that there are still a lot of
compilers out there which do not guarantee that.  And once code is
written, who knows where it might end up?  You assume that I avoid
certain practices because I don't understand them.  The fact is
that I avoid them because I do understand them, and I understand
the ramifications of using them.  I also am more interested in
writing solid code than in trying to prove how great I am.  That
last area is one of many where you have a lot to learn.

You are so full of yourself, it never occurs to you that someone
else may know more about a subject than you.  I have met a number
of people like you over the years, who think they are so smart,
they are oblivious to how foolish some of their thinking is.  The
sad thing is, they seldom come to realize this until years later.
This practice is particularly associated with youth, though some
are so bone headed they carry it on for years.  Those people become
objects of ridicule, Richard.  And most get little sympathy, because
they are so obnoxious in their arrogance.  Not that I expect you to
receive this, of course.  What I have been trying to do here, up
until this post, is sharing ideas and experience to the benefit of
myself and others.  What you have been trying to do is to show that
you are smarter than me.  Let me tell you something, Richard.  No
one cares which of us is smarter, not even me.  But what you have
actually done, Richard, is to reveal your own arrogance, in far more
clarity than you realize.  In this post, I have taken the liberty of
making it even little clearer.  You earned it, I think you deserve
it.  I'm sure you can appreciate that. ;-)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
