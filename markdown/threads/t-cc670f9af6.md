[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# EXIT PERORM CYCLE

_10 messages · 5 participants · 1999-04_

---

### EXIT PERORM CYCLE

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370A313D.F27600BE@NOSPAMhome.com>`

```
In the new standard, there will be

EXIT PERFORM       (leaves a perform loop)
EXIT PERFORM CYCLE (goes to next test of perform loop)

& 
EXIT PARAGRAPH / EXIT SECTION

Why is in-line perform processing enhanced with this two way choice,
but  paragraph perform processing not enhanced this much?
```

#### ↳ Re: EXIT PERORM CYCLE

- **From:** "Robert M. Pritchett" <NewsCSIbus@rmpcp.com>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#$2rOhJg#GA.345@nih2naaf.prod2.compuserve.com>`
- **References:** `<370A313D.F27600BE@NOSPAMhome.com>`

```
I have mixed feelings about these. Sounds like encouraging sloppy
programming. On the other hand they'd be much better than GOTO's. If stuff
like this keeps getting added to the language, compilers should have
options to prohibit use of certain constructs in detail, not just certain
reserved words, so that e.g. a shop or project could prohibit Perform Thru
but Perform would still work, and Next Sentence could be prohibited without
interfering with other uses of the word Next.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmpcp@pobox.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!


Howard Brazee wrote in message <370A313D.F27600BE@NOSPAMhome.com>...
>In the new standard, there will be
>
…[4 more quoted lines elided]…
>EXIT PARAGRAPH / EXIT SECTION
```

##### ↳ ↳ Re: EXIT PERORM CYCLE

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370B5EA2.3F578F72@NOSPAMhome.com>`
- **References:** `<370A313D.F27600BE@NOSPAMhome.com> <#$2rOhJg#GA.345@nih2naaf.prod2.compuserve.com>`

```
Robert M. Pritchett wrote:
> 
> I have mixed feelings about these. Sounds like encouraging sloppy
…[5 more quoted lines elided]…
> interfering with other uses of the word Next.

That would be nice.  Maybe have a precompiler tool which enforces
standards.  It could also check record sizes  READ INTO, etc.  It could
examine the code and make sure we never drop through paragraphs.  
Someone on this forum has a tool which does some of these checking.
```

#### ↳ Re: EXIT PERORM CYCLE

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7edesq$i16@dfw-ixnews4.ix.netcom.com>`
- **References:** `<370A313D.F27600BE@NOSPAMhome.com>`

```
Howard Brazee wrote in message <370A313D.F27600BE@NOSPAMhome.com>...
>In the new standard, there will be
>
…[7 more quoted lines elided]…
>but  paragraph perform processing not enhanced this much?

I remember that it was discussed and rejected.  I don't remember the "logic"
when the original decision was made - but I do remember that the committee
said "we already discussed this" when the topic came up a 2nd time.  I think
(but am not at all certain) that this might be related to the fact that the
EXIT PARAGRAPH/SECTION syntax can occur in a "non-loop" environment - while
the inline EXIT PERFORM is *always* within a loop - even if that loop is
only a single iteration.

If you don't get an answer in the NG that you think is good enough, you
might want to send a note to the J4 chair at
    doncobol <at> mediaone.net
```

##### ↳ ↳ Re: EXIT PERORM CYCLE

- **From:** Don Nelson <don.nelson@compaq.com>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370A58E0.6F0@compaq.com>`
- **References:** `<370A313D.F27600BE@NOSPAMhome.com> <7edesq$i16@dfw-ixnews4.ix.netcom.com>`

```
William M. Klein wrote:
> 
> Howard Brazee wrote in message <370A313D.F27600BE@NOSPAMhome.com>...
…[11 more quoted lines elided]…
> I remember that it was discussed and rejected.

For a very good reason as shown below.

> I don't remember the "logic"
> when the original decision was made - but I do remember that the committee
> said "we already discussed this" when the topic came up a 2nd time.

And a third time and a fourth time and so on and so on.  Obviously, 
this is excactly what one should say. 

The "logic" was that you don't have the faintest idea what PERFORM any 
paragraph or section might be within.  Since a PERFORM can go all over 
the place (PERFORM a THROUGH b, PERFORM a-section, GO TO, etc.) and 
any paragraph or section can be under the influence of none, one, two, 
or a thousand.  One could pick the last one but then users would 
complain that that is not the one they want - they wanted the first 
one.  What do you do if there is no active PERFORM?  Anyone reading 
the program would not have the faintest idea what PERFORM was 
infolved.  Sort of like a computed come from and much worse than 
ALTER.  The EXIT PERFORM makes sense only for an inline PERFORM.

> I think
> (but am not at all certain) that this might be related to the fact that the
> EXIT PARAGRAPH/SECTION syntax can occur in a "non-loop" environment - while
> the inline EXIT PERFORM is *always* within a loop - even if that loop is
> only a single iteration.

Any PERFORM is a loop.  It only has to do with the PERFORM being 
inline.

> If you don't get an answer in the NG that you think is good enough, you
> might want to send a note to the J4 chair at
>     doncobol <at> mediaone.net

Please don't.  All it does is waste everyones time.  If you have a 
question, send something to me.
```

###### ↳ ↳ ↳ Re: EXIT PERORM CYCLE

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7edm9u$dvj@dfw-ixnews5.ix.netcom.com>`
- **References:** `<370A313D.F27600BE@NOSPAMhome.com> <7edesq$i16@dfw-ixnews4.ix.netcom.com> <370A58E0.6F0@compaq.com>`

```
Not disagreeing with most of Don's logic, but see below for one issue:
```

###### ↳ ↳ ↳ Re: EXIT PERORM CYCLE

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370b1463.51073878@netnews>`
- **References:** `<370A313D.F27600BE@NOSPAMhome.com> <7edesq$i16@dfw-ixnews4.ix.netcom.com> <370A58E0.6F0@compaq.com>`

```
'Twas Tue, 06 Apr 1999 11:56:32 -0700, when Don Nelson
<don.nelson@compaq.com> illuminated comp.lang.cobol thusly:

>The "logic" was that you don't have the faintest idea what PERFORM any 
>paragraph or section might be within.

That's why we need it.

>  Since a PERFORM can go all over 
>the place (PERFORM a THROUGH b, PERFORM a-section, GO TO, etc.) and 
…[3 more quoted lines elided]…
>one.

It should exit the most recent one, of course.  This brings up the
possiibility of EXIT PERFORM integer.

>  What do you do if there is no active PERFORM?

Abort unless it's trapped by a declarative.  Duh!

>  Anyone reading 
>the program would not have the faintest idea what PERFORM was 
>infolved.

The reader doesn't care, it's where the PERFORM is.  When you read GO TO
1999-EXIT you don't know where the PERFORM is either.

>  Sort of like a computed come from and much worse than 
>ALTER.  The EXIT PERFORM makes sense only for an inline PERFORM.

Then why do so many of the programmers want it?

-->>RANT
This is a perfect example of J4/AMSI/ISO arrogance toward the only true
audience of the COBOL Standard:  The Programmers.  The programmers want
it, the semantics are easy to define.  If a compiler has a well designed
PERFORM stack, it's very easy to implement.  If a compiler has any other
kind of PERFORM mechanism, this becomes impossible to implement, and they
will be forced to change their PERFORM mechanism.  

This also risks changing the semantics of the overlapping range case.  As
noted in CD 1.4 p 481, 14.10.27.3 GR 9, this case is undefined, but it is
possible to design a PERFORM stack mechanism which recreates the semantics
of any prior implementation.

It is only the implementors who are opposed to EXIT PERFORM; all the
programmers want it.

'Twas Tue, 6 Apr 1999 18:25:09 -0500, when "William M. Klein"
<wmklein@nospam.netcom.com> illuminated comp.lang.cobol thusly:

>The draft of the next Standard *was* available electronically.  I think (and
>this may be mis-stating the real issue) that there are ISO (not ANSI) rules
>about "drafts" between official CD (Committee Drafts) that are impacting J4
>and WG4 on their NOT making the current version available electronically.

Yet more of the arrogance toward the programmers.
-->>RANT OFF
```

###### ↳ ↳ ↳ Re: EXIT PERORM CYCLE

_(reply depth: 4)_

- **From:** Don Nelson <don.nelson@compaq.com>
- **Date:** 1999-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370BD6B3.2645@compaq.com>`
- **References:** `<370A313D.F27600BE@NOSPAMhome.com> <7edesq$i16@dfw-ixnews4.ix.netcom.com> <370A58E0.6F0@compaq.com> <370b1463.51073878@netnews>`

```
Randall Bart wrote:
> 
> It should exit the most recent one, of course. 

That may be what you think but I have heard others say it should do 
the one closest to this paragraph or the one that actually specified 
this paragraph as an exit (which may not be the latest one) and so on.

> This brings up the
> possiibility of EXIT PERFORM integer.

I can't even imagine that.

> >  What do you do if there is no active PERFORM?
> 
> Abort unless it's trapped by a declarative.  Duh!

You would be the first one to complain about this!  Many would want it 
to continue as if it was a no-op (that was suggested).

> >  Anyone reading
> >the program would not have the faintest idea what PERFORM was
> >infolved.
> 
> The reader doesn't care, it's where the PERFORM is.

This makes no sense to me.  The reader certainly does care.

> When you read GO TO
> 1999-EXIT you don't know where the PERFORM is either.

That's why I don't like that either.  You certainly do have a better 
idea in that case, however.

> >  Sort of like a computed come from and much worse than
> >ALTER.  The EXIT PERFORM makes sense only for an inline PERFORM.
> 
> Then why do so many of the programmers want it?

So many?  I've only heard a couple.  Everyone on the COBOL committee 
is a programmer.  About half write mainly COBOL.  Most of us write in 
lots of stuff including COBOL.  And nobody wants it.

> -->>RANT
> This is a perfect example of J4/AMSI/ISO arrogance

Talk abour arrogance - you are pretty good at it yourself.

>toward the only true
> audience of the COBOL Standard:  The Programmers.  The programmers want
> it, 

Some do and some don't.  You can't make such a generalization.  And, I 
wouldn't be surprised that those who said they wanted it did not know 
that it makes for unreadable programs.

> the semantics are easy to define.  If a compiler has a well designed
> PERFORM stack, it's very easy to implement.

So what?  Does making something easy to implement make it good?

>If a compiler has any other
> kind of PERFORM mechanism, this becomes impossible to implement, and they
…[8 more quoted lines elided]…
> programmers want it.

Absolutely wrong. Implementation never came up during any of the 
discussions.  Only how bad the idea was.  And, as I said, none of the 
full-time COBOL programmers on the committee thought it was a good 
idea either.

> 
> 'Twas Tue, 6 Apr 1999 18:25:09 -0500, when "William M. Klein"
…[7 more quoted lines elided]…
> Yet more of the arrogance toward the programmers.

Complete baloney.  ISO and ANSI have these copyright rules because 
they need to sell standards to support themselves.  They are looking 
into revising the rules - I'm not sure how.  I fail to understand why 
you think this has anything to do with arrogance and with programmers 
at all.
```

###### ↳ ↳ ↳ Re: EXIT PERORM CYCLE

_(reply depth: 5)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3723b7e4.16876035@netnews>`
- **References:** `<370A313D.F27600BE@NOSPAMhome.com> <7edesq$i16@dfw-ixnews4.ix.netcom.com> <370A58E0.6F0@compaq.com> <370b1463.51073878@netnews> <370BD6B3.2645@compaq.com>`

```
'Twas Wed, 07 Apr 1999 15:05:39 -0700, when Don Nelson
<don.nelson@compaq.com> illuminated comp.lang.cobol thusly:

>Randall Bart wrote:
>> 
…[4 more quoted lines elided]…
>this paragraph as an exit (which may not be the latest one) and so on.

I know of no language (including Cobol) where the standard is to exit
other than the most recent unexited invocation.

>> This brings up the
>> possiibility of EXIT PERFORM integer.
>
>I can't even imagine that.

You must have a small imagination.

>> >  What do you do if there is no active PERFORM?
>> 
>> Abort unless it's trapped by a declarative.  Duh!
>
>You would be the first one to complain about this!  

This is preposterous.  In Basic, if you have a RETURN without an active
GOSUB, the program aborts.  When have I ever complained about Cobol
behaving more like Basic?

>Many would want it 
>to continue as if it was a no-op (that was suggested).

Rather like EXIT PROGRAM, which I also gripe about.

>> -->>RANT
>> This is a perfect example of J4/AMSI/ISO arrogance
>
>Talk abour arrogance - you are pretty good at it yourself.

To quote Dr Science:  "There's a fine line between ignorance and
arrogance, and I have erased that line."

>>The programmers want
>> it, 
…[3 more quoted lines elided]…
>that it makes for unreadable programs.

It's the current PERFORM mechanism that contributes to program
unreadability.  PERFORM is a combination of GO TO and COME FROM.  Even the
compiler can't tell; the compiler needs to insert code to see if a COME
FROM (PERFORM) is active.  AFAIK, Cobol is the only computer language
where the spot where the code exits isn't explicitly marked.  Can you give
me an example in another language where there is code which might exit or
might fall through?

>> the semantics are easy to define.  If a compiler has a well designed
>> PERFORM stack, it's very easy to implement.
>
>So what?  Does making something easy to implement make it good?

No, but when something is hard to implement that usually means it's bad.

>ISO and ANSI have these copyright rules because 
>they need to sell standards to support themselves.

Which makes as much sense as the Gideons charging a rental fee to read
their bibles.  ISO and ANSI are supposed to promote standards, not keep
them secret.  They should be financed by the contributions of those who
want standardization.
```

###### ↳ ↳ ↳ Re: EXIT PERORM CYCLE

_(reply depth: 6)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37246A37.D30B2DCA@NOSPAMhome.com>`
- **References:** `<370A313D.F27600BE@NOSPAMhome.com> <7edesq$i16@dfw-ixnews4.ix.netcom.com> <370A58E0.6F0@compaq.com> <370b1463.51073878@netnews> <370BD6B3.2645@compaq.com> <3723b7e4.16876035@netnews>`

```
I would love to have the EXIT PARAGRAPH statement.  But realistically, I
see lots of mainframe shops only converting their ANSI 68 programs
because the Y2K problem forced them to.  Sure, new programs were ANSI 72
- but if IBM had anticipated next year, we would still be using 30 year
old compilers.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
