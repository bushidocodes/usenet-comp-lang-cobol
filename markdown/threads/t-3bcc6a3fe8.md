[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Warning! In-line PERFORM.

_10 messages · 5 participants · 2009-03_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Warning! In-line PERFORM.

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-03-07T02:17:40+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71cm3lFkg5ssU1@mid.individual.net>`

```
I just got bitten by somethng I never would have believed.

Apparently, you cannot use AFTER with an inline PERFORM.

PERFORM
     VARYING J
           FROM 1
                 BY 1
           UNTIL J > LIMIT
                 AFTER K
                  FROM 1
                        BY 1
                  UNTIL K > ANOTHER-LIMIT
                        <do stuff>
END-PERFORM

... is not legal.

I don't know whether this is a Fujitsu limitation or whether it is part of 
the '85 standard, but it certainly shocked me.

As this is code I generate from a tool and it could easily have 3 levels, 
and the code I wrote to detect when it is required and emit it is ... 
well... "non-trivial"... I was a bit non-plussed by this.

Dozens of programs use one level and compile successfully, one comes along 
that needs two levels, the tool generates it correctly, and the compile 
falls over because you're not allowed to do it :-).

I stared blankly at this for about 10 minutes thinking about the hassle of 
having to generate a performed section for it ... This code is just part of 
a stream of stuff that involves ESQL and other processing  (and the whole 
lot is wrapped in conditionals as well...)and it needs to be coherent in the 
program. I really don't want to have to start sectioning it when I have code 
that looks correct and is generated in the right place at the right time.

Then it struck me... change the AFTER K to be PERFORM VARYING K ( a very 
simple change of one emitted line) and it should work... Of course I have to 
indent and generate a second END-PERFORM but I reckon that will do it.

Tried it. (With some trepidation because if it won't accept nested performs 
inline I am in for a very long night...)

It worked.

While I am relieved that it worked, it strikes me as just senseless 
stupidity. From the compiler's point of view it would be no more difficult 
to accept AFTER than to require another PERFORM...

Any comments?

Pete.
```

#### ↳ Re: Warning! In-line PERFORM.

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-03-06T11:57:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gormet028ti@news1.newsguy.com>`
- **In-Reply-To:** `<71cm3lFkg5ssU1@mid.individual.net>`
- **References:** `<71cm3lFkg5ssU1@mid.individual.net>`

```
Pete Dashwood wrote:
> I just got bitten by somethng I never would have believed.
> 
…[3 more quoted lines elided]…
> the '85 standard, but it certainly shocked me.

Looks like it's a restriction of COBOL 85, though removed by the ISO
2002 standard. MF allows it as an extension.

I wasn't aware of this either, but then I've never used the AFTER
phrase. I learned COBOL after considerable experience with
ALGOL-derived languages (Pascal, C, etc) and functional languages
(LISP, SML, etc), so I have always just used nested PERFORMs without
looking for an abbreviated form.
```

##### ↳ ↳ Re: Warning! In-line PERFORM.

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-03-06T13:10:13-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ryesl.924$5Z3.129@en-nntp-05.dc1.easynews.com>`
- **References:** `<71cm3lFkg5ssU1@mid.individual.net> <gormet028ti@news1.newsguy.com>`

```
Correct, it was a restriction of the '85 Standard that was removed in the '02 
Standard.  ( know because I pushed for the removal. <G>

As Pete found out, it is possible to "code around it" by nesting inline 
PERFORMs, but that does seem (and always did seem) a "silly" restriction to m 
me.

I don't think that MF is the only compiler that has implemented this '02 
Standard feature (as an extension to the '85 Standard), so others should check 
their own vendor's documentation on whether it is or is not allowed.

(The other odd restriction is the requirement that there MUST be a statement, 
even if it is CONTINUE within an inline perform. That restriction remains.)
```

##### ↳ ↳ Re: Warning! In-line PERFORM.

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-03-07T12:29:02+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71dpttFkn20hU1@mid.individual.net>`
- **References:** `<71cm3lFkg5ssU1@mid.individual.net> <gormet028ti@news1.newsguy.com>`

```
Michael Wojcik wrote:
> Pete Dashwood wrote:
>> I just got bitten by somethng I never would have believed.
…[13 more quoted lines elided]…
> looking for an abbreviated form.

I have always used AFTER when iterating across multi-dimensional tables in 
COBOL.

(I always found the idea of "wheels within wheels" appealing and imagined 
little cogs spinning... :-) I agree that nesting provides the same idea...)

The "problem" (actually, it isn't, because nesting solves it...) is that it 
is no longer ONE construct.

If you are coding by hand, it doesn't matter. If you are generating code 
from an engine, then it might. Now it is necessary to recursively cater for 
nesting (not a big deal) BUT EACH verb you generate requires a scope 
delimiter and these could be a long way off after many lines of code have 
been generated. Where previously a single scope delimiter would have cut it, 
now you have to keep track of how much nesting you did and provide the right 
number of delimiters, appropriately indented. It is all work...

It's not that it "can't be done", it just seems silly to me when there 
already exists a perfectly good construct within the language.

Pete.
```

###### ↳ ↳ ↳ Re: Warning! In-line PERFORM.

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-03-09T10:47:37-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gp3b710mm0@news5.newsguy.com>`
- **In-Reply-To:** `<71dpttFkn20hU1@mid.individual.net>`
- **References:** `<71cm3lFkg5ssU1@mid.individual.net> <gormet028ti@news1.newsguy.com> <71dpttFkn20hU1@mid.individual.net>`

```
Pete Dashwood wrote:
> Michael Wojcik wrote:
>>
…[12 more quoted lines elided]…
> number of delimiters, appropriately indented. It is all work...

I suppose. The code generators I've written were also either for
ALGOL-derived languages or for functional languages, so they always
generated tree-structured programs recursively. The stack kept track
of nesting, scope delimiters, and indentation for me.

But I can see that AFTER might be useful for other approaches to code
generation.

> It's not that it "can't be done", it just seems silly to me when there 
> already exists a perfectly good construct within the language.

Sure. If AFTER is there, it ought to work identically for in-line and
out-of-line PERFORM. The restriction is silly.
```

#### ↳ Re: Warning! In-line PERFORM.

- **From:** riplin@Azonic.co.nz
- **Date:** 2009-03-06T09:56:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<696e733a-8e2f-44d6-a0db-3357248d34ba@f1g2000prb.googlegroups.com>`
- **References:** `<71cm3lFkg5ssU1@mid.individual.net>`

```
On Mar 7, 2:17 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> I just got bitten by somethng I never would have believed.
>
…[51 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."

"""Rules for format 4

When imperitive-statement-1 is written, the AFTER phrase must not be
written."""

From the programmer's point of view it would be no more difficult to
write PERFORM rather than to require the compiler to accept AFTER ...

With out-of-line PERFORMs nesting them with AFTER is a convenience
that is is not required with in-line PERFORMs.
```

##### ↳ ↳ Re: Warning! In-line PERFORM.

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-03-07T12:45:51+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71dqteFkbhmtU1@mid.individual.net>`
- **References:** `<71cm3lFkg5ssU1@mid.individual.net> <696e733a-8e2f-44d6-a0db-3357248d34ba@f1g2000prb.googlegroups.com>`

```
riplin@Azonic.co.nz wrote:
> On Mar 7, 2:17 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[63 more quoted lines elided]…
> write PERFORM rather than to require the compiler to accept AFTER ...

Apart from the fact that AFTER is already part of the PERFORM syntax and 
learned at the time you learned about PERFORM.

I also note in passing that is quicker to type AFTER than it is to type 
PERFORM VARYING K, so perhaps your "no more difficult" doesn't stand 
scrutiny?(it may be no more "difficult" but it DOES take more effort...)

At the end of the day, as you have observed on a number of occasions, 
whether AFTER or nested perform is more "comfortable" for someone, depends 
on personal preference.

Thanks for pointing out the manual reference.

These days I don't check the manual for constructs I believe I understand 
and have used successfully on numerous occasions in the past. Do you?

That was what led to my surprise when I found it was rejected. :-)

I outlined my objections in my response to Michael.

>
> With out-of-line PERFORMs nesting them with AFTER is a convenience
> that is is not required with in-line PERFORMs.

That's an interesting take on it. In effect it says that if you use inline 
PERFORM you cannot use the full power of it.  See, I don't see using AFTER 
as a "convenience"; any more than I see using REPLACING with INSPECT as a 
"convenience". The verbs have facilities which are optional and increase 
their power. Sometimes that extra power is needed, sometimes it isn't.

Fortunately, nested PERFORM inline is available, so there is no real 
problem.

Pete.
```

###### ↳ ↳ ↳ Re: Warning! In-line PERFORM.

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-09T19:03:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gp3p5d$fsn$1@reader1.panix.com>`
- **References:** `<71cm3lFkg5ssU1@mid.individual.net> <696e733a-8e2f-44d6-a0db-3357248d34ba@f1g2000prb.googlegroups.com> <71dqteFkbhmtU1@mid.individual.net>`

```
In article <71dqteFkbhmtU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip - attributions uncertain]

>Thanks for pointing out the manual reference.
>
>These days I don't check the manual for constructs I believe I understand 
>and have used successfully on numerous occasions in the past. Do you?

'The past', to me, is a rather amorphous, inconsistent thing... sometimes, 
yes, sometimes no.

>
>That was what led to my surprise when I found it was rejected. :-)

Reading The Fine Manual leads me to fewer surprises.

DD
```

###### ↳ ↳ ↳ Re: Warning! In-line PERFORM.

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-03-11T10:26:50+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71o48rFlb8u3U1@mid.individual.net>`
- **References:** `<71cm3lFkg5ssU1@mid.individual.net> <696e733a-8e2f-44d6-a0db-3357248d34ba@f1g2000prb.googlegroups.com> <71dqteFkbhmtU1@mid.individual.net> <gp3p5d$fsn$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <71dqteFkbhmtU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[17 more quoted lines elided]…
> DD

Sometimes a surprise or two can help you know you're alive... :-)

I certainly do Read The Fine Manual when something fails and I can't see 
why. But I don't do so for things I believe I understand (until they fail, 
which shows I believed wrong...)

I wasn't advocating in any way that people shouldn't read the manual.

Pete
```

###### ↳ ↳ ↳ Re: Warning! In-line PERFORM.

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-11T00:19:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gp702s$md$3@reader1.panix.com>`
- **References:** `<71cm3lFkg5ssU1@mid.individual.net> <71dqteFkbhmtU1@mid.individual.net> <gp3p5d$fsn$1@reader1.panix.com> <71o48rFlb8u3U1@mid.individual.net>`

```
In article <71o48rFlb8u3U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <71dqteFkbhmtU1@mid.individual.net>,
>> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>>> That was what led to my surprise when I found it was rejected. :-)
>>
>> Reading The Fine Manual leads me to fewer surprises.
>
>Sometimes a surprise or two can help you know you're alive... :-)

Can't say that I have much recollection of ever being anything *but* what 
I was taught to call 'alive', Mr Dashwood... but my memory is, admittedly, 
porous.

>
>I certainly do Read The Fine Manual when something fails and I can't see 
>why. But I don't do so for things I believe I understand (until they fail, 
>which shows I believed wrong...)

Your beliefs were contradicted by The Machine's behavior, Mr Dashwood... 
but every so often it is good, just for the sake of practise, to go back 
to the basics *without* the need of a 'what in the name of Saint 
Sebastian's pierced scrotum is going on here?!?' pushing one along.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
