[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# First time oncall...

_9 messages · 9 participants · 2000-01_

---

### First time oncall...

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-01-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8634ng0bik@enews4.newsguy.com>`

```
Well, this is my 2nd day of on-call.  I responded to 2 problems so far (is
that my phone ringing :-) ).

One was an ADS/O dialog (screen) that has a known quirk.  I passed the
problem from the help desk, to the programmer in charge of that area.  He
couldn't recreate the problem so that was the end of that.

The other was a recently modified batch COBOL IDMS program.  Well, I know
most people don't use IDMS.  IDMS is a generally a network style database.
I know they added the R for relational in v10 I think.  Anyways, a common
procedure is to obtain the first record in a set, process it, then keep
obtaining the next record in the set and processing it until you hit the
end.  Eventually you hit the END-OF-SET condition and then the code has to
deal with getting out of the loop.  Well for some reason, the person who
made the changes decided to code IF DB-REC-NOT-FOUND then go to exit or
whatever.  Duh, the program dies last night with an 0307 error (End of set,
area, or index).  This seemed like an oversight to me, so I coded OR
DB-END-OF-SET go to exit.  The code was not dropping through, and I did see
that the driver PERFORM was already correctly coded to recognize
DB-END-OF-SET. 20 minutes total, I'm compiling and submitted the library
move to production control's printer.

Fine, the job restarts and completes COND CODES=0.  Today, the lead
programmer of that team is talking to me and said they sent a whole bunch of
bad data to the accounts payable group.  He said I should have called him,
and next time, to do so.  He said he appreciated my valiant effort though
(this guy is like 40 or so and is a real smart ass like me.  He has kids so
I can understand).

Now, I understand some folks are very protective and proud of their code.
But he readily admitted that the changes were made with a style he "didn't
like".  Such as one of these:

If xxxxx
   If xxxxxx
      If xxxxxx
          iF xxxxxxxx
             if xxxxxxxxxx
                if xxxxxxxxxxx
                   if xxxxxxxxxxxxx
                      if xxxxxxxxxxxx
                         if xxxxxxxxxxx
                         end-if
                      end-if
                   end-if
                end-if
             end-if
          end-if
       end-if
    end-if
end-if.

Now, what is this, drawing class or something?  That's shite, sorry.  For
me, 4 levels is usually my limit, 5 occasionaly.  But this generally says
the data is not very streamlined running through the program.

So, anyways, I guess this whole e-mail is basically asking a question.  How
should or can I learn about this 'line' I have to draw between fellow
programmers while on-call?  What should I fix, and what shouldn't I?  What
is it, "people are like teabags; you have to put them in hot water to see
how strong they are?"   I guess I have to learn each person. I mean, missing
a DB-END-OF-SET is pretty trivial.  Maybe he was just mad not because my
'fix' was bad, but because the code sucked balls and did the wrong thing?
How possible is that?

Dunno, just asking.

Jeff
```

#### ↳ Re: First time oncall...

- **From:** William Reed <adamreed@bellsouth.net>
- **Date:** 2000-01-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38854A53.A8BCF6A6@bellsouth.net>`
- **References:** `<8634ng0bik@enews4.newsguy.com>`

```


Jeff Baynard wrote:

> Anyways, a common
> procedure is to obtain the first record in a set, process it, then keep
…[56 more quoted lines elided]…
> Jeff

I agree that the person who put in the change without testing it should get the
call, or at least take the blame for putting in code without testing it.

Code to process records in an IDMS set should be put in a separate paragraph,
NOT in the middle of a string of nested "IF"s.

I once saw code with an IF statement 8 pages long, but I'm sure there are others
who can tell you they saw longer ones.

Programming is no place to have a thin skin for criticism.
But there are no age boundaries on being a smart ass, 40 with kids or otherwise.
```

##### ↳ ↳ Re: First time oncall...

- **From:** stevenln@aol.comnospam (Steve Newton)
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000119011033.03564.00000194@ng-cj1.aol.com>`
- **References:** `<38854A53.A8BCF6A6@bellsouth.net>`

```
>How
>> should or can I learn about this 'line' I have to draw between fellow
>> programmers while on-call? 

To answer the specific question asked by Jeff, I follow these rules:
1).  If the run book (or equivalent) says to call the designee for the business
or application area, I do.
2).  If the run book does not say to call someone specified either by role or
by name, then, I am the one who needs to take the action necessary to get the
system up and running again.  If that produces unexpected results, then I
suggest that either to code needs documentation, or the run book needs update,
to prevent another untalented dofus like me from making a mess in the future.
3).  I never {well. almost never :) } criticise the coding of other
programmers, because, I probably do not know under what conditions the code was
produced, I probably do not know the business problems to be addressed in its
entirety, and I am sure that my successors could and would point to more
shameful examples on my part.  (use of ALTER is a significant exception, it is
always WRONG!).
4.  I always {well, sometimes :)} take criticism of my code as a constructive
attempt to prevent me from doing idiotic things in the future.
5.  Being in my 40's myself, I assume everybody in their 40's are being
smart-asses - after all, we're too old be whiz kids, and too young to be sages,
what else is left?

Jeff, does that help?
Asimov, Heinlein, and Zappa
Still the best
```

##### ↳ ↳ Re: First time oncall...

- **From:** alex@localhost.localdomain (Alex Flinsch)
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86607g$c64$1@bgtnsc02.worldnet.att.net>`
- **References:** `<8634ng0bik@enews4.newsguy.com> <38854A53.A8BCF6A6@bellsouth.net>`

```
On Tue, 18 Jan 2000 23:23:31 -0600, William Reed <adamreed@bellsouth.net> wrote:

>I once saw code with an IF statement 8 pages long, but I'm sure there are others
>who can tell you they saw longer ones.
>

I assume that you also worked at the same large insurance firm in Boston 
that I did, about 10 years ago.
```

#### ↳ Re: First time oncall...

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3885ABA7.650A4BC8@zip.com.au>`
- **References:** `<8634ng0bik@enews4.newsguy.com>`

```
Jeff Baynard wrote:

>
> How should or can I learn about this 'line' I have to draw
> between fellow programmers while on-call?

No programmer likes being told they can do better.  Wa all seem to
believe in ourselves too much.  Age burns this out of us when we least
need it due to experience.

>  What should I fix, and what shouldn't I?

What is broken with the least intrusive fix.  Leave a recommendation
for the code to be thoroughly reviewed with wide awake people.

Sometimes if it is really bad then the least intrusive can amount to a
rewrite but this should not happen often.

>  What is it, "people are like teabags; you have to
> put them in hot water to see how strong they are?"   I guess I have
> to learn each person. I mean, missing a DB-END-OF-SET is pretty
> trivial.

>  Maybe he was just mad not because my 'fix' was bad,

Bad fixes are bad news.  They can take an unholy amount of time to
correct the mess.  If you are not sure call in someone else.  IF you
have no one else and you are not 100% sure cancel the run.  If you do
this and it is important you should have someone to talk to very
shortly :-}

> but because the code sucked balls and did the wrong thing?
> How possible is that?

All code sucks, including the rubbish you wrote last week (if you do
not believe me take a peek at an old program you wrote and tell me
that it could not have been done better).  I hate my old code because
I could have always done better.  There is also the element that bad
code comes from work around that are no longer required.

It is dead easy to criticize, difficult to lead by example.  Make sure
you do not live in a glass house, if you do take criticism on the chin
and learn from it, otherwise shut up!

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

#### ↳ Re: First time oncall...

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Oo$NjspY$GA.270@cpmsnbbsa03>`
- **References:** `<8634ng0bik@enews4.newsguy.com>`

```

When I was oncall for pricing, I just used straight forward judgement calls
as to whether to call in the big guns.  Say, if the day before a mass group
of new data changes had been moved into production (not code, actual new
data), and a S0C7 occurs in code that's never taken that error before, I'll
suspect the data first and call the system owner..

If the S0C7 occurs, and I can determine that this is a result of an improper
code change (compare old code versus new), and I know that the pricing
system's configuration hadn't changed, I'd fix it myself (after running a
test to see if the data itself is, in fact, all right).

This is tempered by knowing a bit about the system, and reading the purpose
of the jobstep involved, the restart instructions, and the documentation in
the code (if any).

It's a balance between what you do know, what you don't, and what you can
figure out.



Jeff Baynard <union27@macconnect.com> wrote in message
news:8634ng0bik@enews4.newsguy.com...
> Well, this is my 2nd day of on-call.  I responded to 2 problems so far (is
> that my phone ringing :-) ).
…[13 more quoted lines elided]…
> whatever.  Duh, the program dies last night with an 0307 error (End of
set,
> area, or index).  This seemed like an oversight to me, so I coded OR
> DB-END-OF-SET go to exit.  The code was not dropping through, and I did
see
> that the driver PERFORM was already correctly coded to recognize
> DB-END-OF-SET. 20 minutes total, I'm compiling and submitted the library
…[3 more quoted lines elided]…
> programmer of that team is talking to me and said they sent a whole bunch
of
> bad data to the accounts payable group.  He said I should have called him,
> and next time, to do so.  He said he appreciated my valiant effort though
> (this guy is like 40 or so and is a real smart ass like me.  He has kids
so
> I can understand).
>
…[27 more quoted lines elided]…
> So, anyways, I guess this whole e-mail is basically asking a question.
How
> should or can I learn about this 'line' I have to draw between fellow
> programmers while on-call?  What should I fix, and what shouldn't I?  What
> is it, "people are like teabags; you have to put them in hot water to see
> how strong they are?"   I guess I have to learn each person. I mean,
missing
> a DB-END-OF-SET is pretty trivial.  Maybe he was just mad not because my
> 'fix' was bad, but because the code sucked balls and did the wrong thing?
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: First time oncall...

- **From:** "john doe" <someone@microsoft.com>
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8661ls$r33$1@news.smartworld.net>`
- **References:** `<8634ng0bik@enews4.newsguy.com> <Oo$NjspY$GA.270@cpmsnbbsa03>`

```
We do try to take it a step further in the cycle review meetings after we
get the code fixed.we relook who was in the group who reviewed and approved
the code,,Then we review the procedure they used to test,,then we fix both
and set new guidelines. Though this doesn't always works it sure helps,
especially the new programmers who can benefit most from "walkthroughs" both
their own and being in on others.
```

#### ↳ Re: First time oncall...

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KFNh4.265$JB.3964@nnrp2.rcsntx.swbell.net>`
- **References:** `<8634ng0bik@enews4.newsguy.com>`

```

Jeff Baynard <union27@macconnect.com>

Whoever 'owns' the busted program that needed fixing gets the
'on-call' job until the next program failure.
```

#### ↳ Re: First time oncall...

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86b3av$2uk$1@news.inet.tele.dk>`
- **References:** `<8634ng0bik@enews4.newsguy.com>`

```
Nested IF's are nice to look at, but not at 3.15 am. Unfortunately program
structure is like religion - you cannot discuss it.

When I am on call, I insist to be 'captain on the ship' and if anyone dare
to put an untested change to production level without informing me about it,
he will hear from me. We have a member for each day, where people can tell
the person on-call what to do if a new or changed program crashes. If
nothing is stated there, I feel free to do whatever possible to correct the
error. If some child at 40 is uncomfortable with changes I made, so what?

The reason for your change was a bug, and you didn't put i there. You were
called because someone else failed to do a proper piece of work.

An other thing I don't understand. When do our nice young fellow at 40 like
to be called? I mean, if he want a call, why not call him and take a nap? I
would really like a young dedicated person to call - especially after
midnight, and preferably 3-4 times before morning breaks.

As you can see, I'm older than 40. I am taking on-call myself when something
is critical - I took the Y2K duty just for the challenge, but it was no big
deal.

The best idea I can give you is the member per day, where people can give
helpful messages and phone numbers you can call if their new/changed
programs fails. We enter the actions done during the night as well. When a
job gives bad condition codes, you can search through the members to see
what was done last time the error ocurred.

The idea removes doubt about when to call help. Further more, people are in
daytime aware of the problems you might have during the night, and it gives
a nice team spirit.

I hope this helps you.

regards
Ib

Jeff Baynard skrev i meddelelsen <8634ng0bik@enews4.newsguy.com>...
>Well, this is my 2nd day of on-call.  I responded to 2 problems so far (is
>that my phone ringing :-) ).
…[21 more quoted lines elided]…
>programmer of that team is talking to me and said they sent a whole bunch
of
>bad data to the accounts payable group.  He said I should have called him,
>and next time, to do so.  He said he appreciated my valiant effort though
…[34 more quoted lines elided]…
>how strong they are?"   I guess I have to learn each person. I mean,
missing
>a DB-END-OF-SET is pretty trivial.  Maybe he was just mad not because my
>'fix' was bad, but because the code sucked balls and did the wrong thing?
…[5 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
