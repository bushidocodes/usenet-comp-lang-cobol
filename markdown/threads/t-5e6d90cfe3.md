[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# A COBOL conundrum

_58 messages · 15 participants · 2010-10_

---

### A COBOL conundrum

- **From:** Arnold Trembley <arnold.trembley@att.net>
- **Date:** 2010-10-02T03:29:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com>`

```
I support a COBOL program that is used to read a COBOL source code file 
and analyze it for compliance with company coding standards.  Last 
Friday afternoon a project leader reported that it had a bug.

He was reviewing a contractor's program deliverables and he found a 
duplicate data name in working-storage.  He believed that my 
style-checker program should have flagged it.  But he was truly 
surprised that the IBM Enterprise COBOL compiler for zOS compiled the 
program without errors.

Here's a simplified example of the problem:

        IDENTIFICATION DIVISION.
        PROGRAM-ID.             HELLO6.
        ENVIRONMENT DIVISION.
        DATA DIVISION.
        WORKING-STORAGE SECTION.
        01  100-PROGRAM-FLAGS.
            05  100-CUST-ACCT-EOF-SW        PIC X(01)   VALUE 'N'.
                88  88-100-CUST-ACCT-NOT-EOF            VALUE 'N'.
                88  88-100-CUST-ACCT-EOF                VALUE 'Y'.
            05  100-CUST-ACCT-EOF-SW        PIC X(01)   VALUE 'N'.
                88  88-100-TRAILER-FOUND                VALUE 'Y'.
                88  88-100-TRAILER-NOT-FOUND            VALUE 'N'.
        PROCEDURE DIVISION.
        0000-MAINLINE.
            DISPLAY 'HELLO WORLD'.
            IF 88-100-TRAILER-NOT-FOUND
                DISPLAY 'TRAILER NOT FOUND'
            END-IF.


The sample program has 100-CUST-ACCT-EOF-SW defined twice in the same 01 
record, but with unique condition names for each instance.  IBM 
Enterprise COBOL for zOS compiles this successfully and the program 
displays the output you would expect.

But if you add one line to the procedure division, something as simple 
as "DISPLAY 100-CUST-ACCT-EOF-SW", then the compile fails because 
100-CUST-ACCT-EOF-SW is not a uniquely defined name.

It seems counter-intuitive for COBOL to allow duplicate data names in 
this context, but I assume it is not prohibited by the COBOL standard.

I could modify the style-checker program to issue warnings for duplicate 
data name definitions, but that would discourage using data name 
qualification for MOVE CORRESPONDING and ADD CORRESPONDING.  We don't 
actually use data name qualification, but it's valid COBOL code.

I am very curious to know if this sample program will compile and 
execute in other COBOL compilers.
```

#### ↳ Re: A COBOL conundrum

- **From:** foodman <foodman123@aol.com>
- **Date:** 2010-10-02T02:27:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5594cba8-b41d-413a-9499-4f2651057466@30g2000yqm.googlegroups.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com>`

```
The program compiles and runs OK with my ancient 16-bit compiler with
no errors.

But I put in a Display of 100-CUST-ACCT-EOF-SW and got a duplicate
name error message.

tony dilworth
```

#### ↳ Re: A COBOL conundrum

- **From:** foodman <foodman123@aol.com>
- **Date:** 2010-10-02T02:42:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d7134a81-ad15-4b20-b9b8-8200284a1676@l20g2000yqm.googlegroups.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com>`

```
After running the test,  I decided to put a couple of duplicate WS
items in one of my programs.

Apparently, the compiler will not flag the duplicates unless they are
referenced in the PD.

tony dilworth
```

##### ↳ ↳ Re: A COBOL conundrum

- **From:** Arnold Trembley <arnold.trembley@att.net>
- **Date:** 2010-10-02T14:23:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Fa6dndJnc_07GzrRnZ2dnUVZ5qednZ2d@giganews.com>`
- **In-Reply-To:** `<d7134a81-ad15-4b20-b9b8-8200284a1676@l20g2000yqm.googlegroups.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <d7134a81-ad15-4b20-b9b8-8200284a1676@l20g2000yqm.googlegroups.com>`

```
On 10/2/2010 4:42 AM, foodman wrote:
> After running the test,  I decided to put a couple of duplicate WS
> items in one of my programs.
…[4 more quoted lines elided]…
> tony dilworth

Tony, thanks for running those tests.  I have also tested with the 1990 
education version of Realia COBOL that runs in the DOSBOX emulator and 
gets the same results you report.

Just out of curiosity, which COBOL compiler(s) did you test with? 
Microfocus, or something else?

Regards,
```

#### ↳ Re: A COBOL conundrum

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-10-02T05:36:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com>`

```
Arnold, (and anyone else who didn't know this or who has forgotten it),

In the '85 Standard (which Enterprise COBOL comforms to) is the follow 
documented SUBSTANTIVE CHANGE (from the '74 Standard),

"(8) Uniaueness of reference (1 NUC). A user-defined word need not be unique 
or be capable of being made unique unless referenced."

For those interested in Enterprise COBOL specifically, see:
  http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/IGY3LR50/1.8.1

"To use a resource, a statement in a COBOL program must contain a reference 
that uniquely identifies that resource."

This enhancement has been available since (at least) VS COBOL II, R3 - and 
is completely portabable to any compiler that conforms to the '85 (or later) 
ANSI/ISO Standard.

Now, if the question is whether a "company standard" should dis-allow it, 
that is "up to you".  However, if you are getting packages (as source code) 
from other sources, I would think twice about disallowing it.

"Arnold Trembley" <arnold.trembley@att.net> wrote in message 
news:rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com...
>I support a COBOL program that is used to read a COBOL source code file and 
>analyze it for compliance with company coding standards.  Last Friday 
…[51 more quoted lines elided]…
> http://www.arnoldtrembley.com/
```

##### ↳ ↳ Re: A COBOL conundrum

- **From:** Arnold Trembley <arnold.trembley@att.net>
- **Date:** 2010-10-02T14:39:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com>`
- **In-Reply-To:** `<wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com>`

```
On 10/2/2010 5:36 AM, Bill Klein wrote:
> Arnold, (and anyone else who didn't know this or who has forgotten it),
>
…[14 more quoted lines elided]…
> ANSI/ISO Standard.

Bill, thanks for the reply.  I'm not too surprised that the COBOL 
standard specifically requires this behavior.  But it did surprise me 
when it showed up unexpectedly in a working program.  If anyone is 
interested, the project leader told the programmer to either name both 
05 items as FILLER, or give them unique names.  I think either choice 
would be a better practice than leaving the duplicate names in the code.

>
> Now, if the question is whether a "company standard" should dis-allow it,
> that is "up to you".  However, if you are getting packages (as source code)
> from other sources, I would think twice about disallowing it.

That's a much harder question to answer!  I have some input to the 
company's COBOL coding standards, or at least how the are enforced 
(somewhat loosely - we try to encourage what we think is good style, but 
nobody has ever been disciplined for including "GO TO 8000-EXIT".)

Our style-checker is used in code review meetings.  It is definitely not 
tied into our code management software, which is CA-Endevor.

Our data naming conventions would discourage using MOVE CORRESPONDING. 
The most I am considering doing is modifying the style-checker to issue 
a warning message that a data name is not uniquely defined, just as a 
suggestion.

I have only seen MOVE CORRESPONDING once or twice in 20 years at this 
shop, and then only in a throwaway file conversion program.  I don't 
want to tell any programmer they can't use a legal COBOL verb.  Well, I 
would strongly discourage using ALTER, but I haven't seen that many 
years.

Thanks very much!

>
> "Arnold Trembley"<arnold.trembley@att.net>  wrote in message
> news:rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com...
>> (snip)
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2010-10-03T03:17:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i88sji$hqu$1@news.eternal-september.org>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com>`

```
In article <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com>, arnold.trembley@att.net wrote:

>I have only seen MOVE CORRESPONDING once or twice in 20 years at this 
>shop, and then only in a throwaway file conversion program. 

IMHO, MOVE CORR is one of the most useful features of the language, and isn't 
used *nearly* as much as it should be.

> I don't
>want to tell any programmer they can't use a legal COBOL verb.  Well, I 
>would strongly discourage using ALTER, but I haven't seen that many 
>years.

Oh, I would. In a heartbeat. Use ALTER and you're fired. If it were up to me, 
that wouldn't *be* "a legal COBOL verb". I think it should have been removed 
from the standard years ago.
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-10-03T20:56:30+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gqr9gF5uqU1@mid.individual.net>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org>`

```
Doug Miller wrote:
> In article <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com>,
> arnold.trembley@att.net wrote:
…[17 more quoted lines elided]…
> from the standard years ago.

So you've had a lot of experience dealing with it and found it difficult?

Or are you just trotting out the perceived wisdom that "everybody knows"?

I worked on sites where ALTER was used for years. (We had to because it was 
more efficient than PERFORM. Setting an exit at the end of a PEFORM range 
(like a SECTION) and simply altering it to return to the next instruction, 
then branching to the beginning of the range, saved around 10 machine 
instructions, in the days when this mattered. (It was on Burroughs 
hardware...)

Here's an example to clarify:

(generally preferred "modern" code)

 Mainline-code.

    ....
* need to carry out subroutine-1 here...
   perform subroutine-1
   ...


  subroutine-1 section.
  sub-1.
         ...
  sub-1-end.
         exit.

  next-subroutine section.
  etc.

Now, implementing exactly the same code but WITHOUT PERFORM and using ALTER 
instead...

 Mainline-code.

    ....
* need to carry out subroutine-1 here...
   alter sub-1-end to proceed to main-1
   go to subroutine-1.
 main-1.
   ...


  subroutine-1 section.
  sub-1.
         ...
  sub-1-end.
         go to.

  next-subroutine section.
  etc.

Is it SO difficult that it should be BANNED? Just because it has a potential 
for misuse (as, indeed do MOST COBOL verbs...)?

Well, if you have people who write code in non-joined up writing by means of 
a crayon, perhaps, but to a trained professional who calls himself a 
"programmer"?

I don't think so, and, frankly, I'm tired of people who never coded an ALTER 
in their lives showing how passionate they are about  fighting spaghetti 
code, and beating the drum for BANNING this and BANNING that, so that the 
lowest common denominator can be comfortable without overtaxing their poor 
little brains.

(Sorry, it isn't personal; I don't know whether you have coded ALTERs or not 
and it really doesn't matter, the thing that's grinding my gears is the 
mindset behind dumbing down what was a beautiful and elegant language until 
it is so emasculated, that it can't do anything. (Whether you do this by 
imposing standards that stifle all original thinking and creativity, treat 
programmers as irresponsible idiots who must be controlled (then wonder why 
you get shit solutions) or whether you pressure the COBOL standards 
committee to remove a construct from the language (in the days when you 
COULD do that and people actually gave a rat's arse about COBOL standards.), 
it pisses me off equally. I was very upset when the standards people bowed 
to pressure and decided ALTER would become, first deprecated, then removed.)

I have seen some amazing solutions that used ALTER in some very innovative 
ways and were years ahead of their time. (Multithreading that used ONE set 
of code and simply set pathways through it like railway tracks with points 
being set by means of ALTER, before activating it, is just one example 
burned in my memory. (Mind you, I believe the guy who wrote it was not of 
this world... :-)) Nevertheless, at a time when multithreading was a 
strange, esoteric, concept, this guy wrote an application that serviced 32 
stations in 16KB of code, in COBOL! (Sadly, he has long since departed this 
world (and probably returned to his home one with a report on the state of 
computer programming on Sol 3...)

Just before I close out this rant, consider the following:

While few people today (self included) would implement the second solution 
above, in preference to the first, it did have some spin-offs that were not 
immediately obvious...

1. It ensured that code was consistent. You didn't need a standard to tell 
you that if you didn't keep to a consistent set of rules, things could get 
decidedly ugly very quickly. For example, Sections of code could NEVER be 
dropped into but must ALWAYS have their exits set before being branched 
into.

2. It encouraged programming discipline. Sets of conventions around the use 
of ALTERed GO TOs very soon evolved. Nobody coded GO TOs that pointed 
somewhere already. As in the example above, the "points" were initialized to 
nowhere. (cf. the post I made earlier today about 88 levels having 
indeterminacy at the start of a run.)

3. If you accepted the title of "Programmer" it meant you were confident in 
handling the language you claimed expertise in. That meant you could deal 
with bad code as well as good code. It meant that nothing NEEDED to be 
BANNED because professionals could handle it competently.

(We don't ban power drills from the local hardware store because a 4 year 
old made holes in the furniture with one, or some other kid cut his finger 
off...instead, we expect parents to be responsible and show kids how to use 
these things properly and safely (or keep them out of reach until such time 
as the kid is capable of handling it.- A locked cupboard is NOT the same as 
a BAN on sales...)

If you claimed to be a professional and actually were NOT able to unravel 
spaghetti code, or deal with nested IFs or complex PERFORMS, or handle 
ALTER, then you have no right to call yourself a "programmer". It is 
insulting to those of us who ARE programmers. Call youself a "script kiddy" 
or a "bunny" and I'll put away my keyboard and leave you in peace.

Anyone who advocates the BANNING of a construct in COBOL (or any other 
language, actually), in my book, is not fit to be called "programmer".

If you can't stand the heat, don't go in the kitchen.

By all means, campaign for better coding styles and standards, appreciate 
that the world has moved on and the priorities in computer programming today 
are not necessarily what they were 40 years ago, but PLEASE, don't tell ME I 
can't use a language element because YOU have a problem with it!

Pete.
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 5)_

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2010-10-03T13:57:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i8a24k$o1o$1@news.eternal-september.org>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net>`

```
In article <8gqr9gF5uqU1@mid.individual.net>, "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote:
>Doug Miller wrote:
>> In article <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com>,
…[38 more quoted lines elided]…
>* need to carry out subroutine-1 here...
[snip example of sensible coding]
>
>Now, implementing exactly the same code but WITHOUT PERFORM and using ALTER 
…[5 more quoted lines elided]…
>* need to carry out subroutine-1 here...
[snip example of awful coding]
>Is it SO difficult that it should be BANNED? Just because it has a potential 
>for misuse (as, indeed do MOST COBOL verbs...)?

No, because (a) it has a far higher potential for misuse than any other 
construct in the language, (b) anything that can be accomplished with ALTER 
can be accomplished far more easily and understandably using other constructs, 
and (c) the use of ALTER requires also the use of GO TO, which is another 
unnecessary construct.
>
>Well, if you have people who write code in non-joined up writing by means of 
…[7 more quoted lines elided]…
>little brains.

I've coded ALTER before, as a classroom exercise, and decided as a student 
that it was a pretty stupid idea. Debugging a few pieces of ALTERed spaghetti 
code on the job reinforced that belief.
>
>(Sorry, it isn't personal; I don't know whether you have coded ALTERs or not 
>and it really doesn't matter, the thing that's grinding my gears is the 
>mindset behind dumbing down what was a beautiful and elegant language until 
>it is so emasculated, that it can't do anything.

Good God! Do you seriously maintain that ALTER is "beautiful and elegant"? To 
the contrary, I would argue that its presence is the main feature of the 
language that *prevents* Cobol from being "beautiful and elegant."

[snip]
>
>I have seen some amazing solutions that used ALTER in some very innovative 
…[3 more quoted lines elided]…
>burned in my memory.

Wow. That's amazing. 

> (Mind you, I believe the guy who wrote it was not of 
>this world... :-)) 

Oh, I can believe that easily enough. :-b

>Nevertheless, at a time when multithreading was a 
>strange, esoteric, concept, this guy wrote an application that serviced 32 
>stations in 16KB of code, in COBOL! (Sadly, he has long since departed this 
>world (and probably returned to his home one with a report on the state of 
>computer programming on Sol 3...)

And I'll bet that he was the only one who could maintain it, too.
>
>Just before I close out this rant, consider the following:
…[9 more quoted lines elided]…
>into.

This doesn't improve your argument for the utility of ALTER: the use of 
SECTIONs in the Procedure Division is a very poor practice. It was necessary 
at one time, when segmentation was required due to tight memory constraints, 
but that hasn't been an issue for, oh, maybe the last twenty-five or thirty 
years.

>2. It encouraged programming discipline. Sets of conventions around the use 
>of ALTERed GO TOs very soon evolved. Nobody coded GO TOs that pointed 
>somewhere already. As in the example above, the "points" were initialized to 
>nowhere. (cf. the post I made earlier today about 88 levels having 
>indeterminacy at the start of a run.)

Nor does this improve your case at all. GO TO is a totally unnecessary 
construct in higher-level languages.
>
>3. If you accepted the title of "Programmer" it meant you were confident in 
>handling the language you claimed expertise in. That meant you could deal 
>with bad code as well as good code. It meant that nothing NEEDED to be 
>BANNED because professionals could handle it competently.

I disagree entirely.

If you accepted the title of "Programmer" it meant that you were capable of 
writing clean, efficient, understandable, and maintainable code. That meant 
that there was no *need* to deal with bad code, because you didn't write any. 
It meant that nothing needed to be banned because professionals would have the 
good sense to avoid use of such constructs.

Unfortunately, all too many programmers *aren't* professionals, and some of 
the worse features of the language do need to be banned to ensure that they 
won't use them.
[snip]
>
>If you claimed to be a professional and actually were NOT able to unravel 
…[3 more quoted lines elided]…
>or a "bunny" and I'll put away my keyboard and leave you in peace.

I never suggested that I was unable to deal with crap like that. The point is 
that we shouldn't *have* to, because it should never have been written in the 
first place: if you claimed to be a professional, and actually *wrote* 
spaghetti code, or coded ALTERs, then you have no right to call yourself a 
"programmer". You're just a coder.
>
>Anyone who advocates the BANNING of a construct in COBOL (or any other 
>language, actually), in my book, is not fit to be called "programmer".

Anyone who advocates the use of ALTER in COBOL, let alone actually uses it, in 
my book, is not fit to be called "programmer".
>
>If you can't stand the heat, don't go in the kitchen.

Indeed. If you can't stand the heat -- i.e. if you can't write code without 
using GO TO, ALTER, and SECTIONs in the Procedure Division -- then get out of 
the kitchen -- i.e., find some other career, or at least some other employer.
>
>By all means, campaign for better coding styles and standards, appreciate 
>that the world has moved on and the priorities in computer programming today 
>are not necessarily what they were 40 years ago, but PLEASE, don't tell ME I 
>can't use a language element because YOU have a problem with it!

I'm not telling you that you can't use a language elemenut because I have a 
problem with it -- I'm just saying that you can't use certain language 
elements *and* work for me.
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-10-04T06:35:39+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8grt7dFi59U1@mid.individual.net>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net> <i8a24k$o1o$1@news.eternal-september.org>`

```
Doug Miller wrote:
> In article <8gqr9gF5uqU1@mid.individual.net>, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[10 more quoted lines elided]…
>>>

Nonsense! Most people try it out at some point and find it is clumsy and 
lugubrious because you then have to qualify all the datanames.. It isn't 
used a lot because it simply increases the writing required. On a small 
structure in working-storage (like a date...) it is perfectly tolerable, but 
when you get a record layout with several hundred datanames in it, it is 
just tedious to have to qualify every reference to them throughout the 
program, just so you can reorganise the order of them with a single MOVE 
CORR.

>>>> I don't
>>>> want to tell any programmer they can't use a legal COBOL verb.
…[7 more quoted lines elided]…
>>> from the standard years ago.

I wonder, of the two views expressed above, who would be the most fun to 
work for?

>>
>> So you've had a lot of experience dealing with it and found it
…[20 more quoted lines elided]…
> [snip example of sensible coding]

.... that achieves exactly the same result as the alternative.

>>
>> Now, implementing exactly the same code but WITHOUT PERFORM and
…[6 more quoted lines elided]…
> [snip example of awful coding]

...despite the fact that it is pertinent to the discussion...

simple code reinstated:

    ....
* need to carry out subroutine-1 here...
   alter sub-1-end to proceed to main-1
   go to subroutine-1.
 main-1.
   ...


  subroutine-1 section.
  sub-1.
         ...
  sub-1-end.
         go to.

  next-subroutine section.
  etc.





>> Is it SO difficult that it should be BANNED? Just because it has a
>> potential for misuse (as, indeed do MOST COBOL verbs...)?
…[3 more quoted lines elided]…
> construct in the language,

No, statistically that would be the misplaced full stop. (The raison d'etre 
for scope delimiters.)



(b) anything that can be accomplished with
> ALTER
> can be accomplished far more easily and understandably using other
> constructs,

Not necessarily. It is a matter of opinion. Certianly PERFORM does the trick 
less laboriously in the example given, but there are other situations where 
ALTER is actually much better (First time switch for example)

> and (c) the use of ALTER requires also the use of GO TO, which is
> another
> unnecessary construct.

So why not get THAT banned as well?

>>
>> Well, if you have people who write code in non-joined up writing by
…[13 more quoted lines elided]…
> code on the job reinforced that belief.

And yet for many years before the advent of high level languages it was 
perfectly common practice for instructions to modify other instructions.
>>
>> (Sorry, it isn't personal; I don't know whether you have coded
…[6 more quoted lines elided]…
> elegant"?

Absolutely. It is very simple, extremely efficient and therefore elegant. 
However, I also recognise that beauty is in the eye of the beholder.


To
> the contrary, I would argue that its presence is the main feature of
> the
> language that *prevents* Cobol from being "beautiful and elegant."
>

Many people would agree with you. That's why it is no longer in the 
language. It's removal ahs made COBOL neither more nor less elegant.

> [snip]
>>
…[19 more quoted lines elided]…
> And I'll bet that he was the only one who could maintain it, too.

See, that is the perceived reaction... And it is based on prejudices and 
assumptions which are simply not true.

In actual fact, as a quite young programmer, I was required to maintain this 
program and did so without any problem at all. Once the fundamental idea was 
understood ("Railway tracks with points that could be switched" was the way 
the guy explained it to me and that was very accurate. I was not the only 
person who was required to amend this program and nobody had any problems 
with it. As has been remarked here before on numerous occasions, people are 
comfortable with what they are used to.
>>
>> Just before I close out this rant, consider the following:
…[13 more quoted lines elided]…
> SECTIONs in the Procedure Division is a very poor practice.

Perhaps you'd better let most of the COBOL world (outside the USA) know 
that. :-)

No, it isn't. It is just another coding style. Provided you don't go 
dropping through the sections and ONLY reference them with PERFORM it is a 
very adequate way of coding COBOL. I use sections in OO COBOL for each 
Object method. (It provides a convenient "partition" for encapsulated object 
methods). My programs work.


 It was
> necessary
> at one time, when segmentation was required due to tight memory
…[3 more quoted lines elided]…
> years.

We used sections BEFORE segmentation was introduced. Before disks were 
available we used sections.(Segment-limit was implemented by means of 
section priorty as a convenient way to implement overlaying, after disks 
became available and programs COULD be manually overlaid, but that isn't 
what sections were "invented" for. It was primarily a syntactic construct 
that simply fitted the concept of COBOL's hierachic structure: DIVISION > 
SECTION > PARAGRAPH > SENTENCE > STATEMENT

Again, you are trotting out what is perceived wisdom rather than actuality.

>
>> 2. It encouraged programming discipline. Sets of conventions around
…[6 more quoted lines elided]…
> construct in higher-level languages.

Maybe. I have never written one in C# or Java, but I have uised it on 
occasion in COBOL and all the time in certain assemblers. In fact One 
assembler I wrote used a 4 address system that ensured EVERY instruction was 
a "do something" and Branch. The world doesn't end if you code a GO TO, any 
more than it does if you code an ALTER. And GO TO (unconditional branch) is 
invariably the fastest instruction in most CISCs.


>>
>> 3. If you accepted the title of "Programmer" it meant you were
…[5 more quoted lines elided]…
> I disagree entirely.

Yes, I kind of picked up on that... :-)

It's fine. Your opinion about it is just as valuable as mine. :-)

>
> If you accepted the title of "Programmer" it meant that you were
…[4 more quoted lines elided]…
> write any.

Hmmmm.... so what was the point of havng constructs in a language if they 
were to be banned on aesthetic grounds? It's a bit like saying there can't 
be any bad music in the world because professional musicians don't play bad 
notes...




> It meant that nothing needed to be banned because professionals would
> have the
> good sense to avoid use of such constructs.

Thereby rendering them pointless and bringing the language down to a subset 
of what the designers of it intended.
>
> Unfortunately, all too many programmers *aren't* professionals, and
…[3 more quoted lines elided]…
> won't use them.

Ever thought about letting the power of an argument persuade somebody? Maybe 
putting your case and letting them make their own minds up? Treating them as 
responsible adults who are capable of acting responsibly if problems with a 
construct are pointed out? Doesn't that seem a better course of action than 
acting like Nanny and deciding what they can and cannot have because you are 
a tad worried that they might not go along with your own viewpoint on it?

There is nothing so demotivating to an intelligent person than to not be 
allowed to use his intelligence. If YOU can see how terrible things like GO 
TO and ALTER and performed SECTIONs are, do you honestly think that no-one 
else can? If someone like me DOESN'T think they are so terrible, do you 
think I am the ONLY one who feels that way? (OK, I'll give you that I may be 
the ONLY one for ALTER, but I spent over 40 years arriving at the other 
conclusions, and have had a very successful career as a computer programmer 
in spite of embracing these "heresies". :-))

Maybe things are not quite so black and white as you may think.

My experience (and it is somewhat extensive) has been that the best way to 
get the top performance from programming teams is NOT to lay down the law 
and BAN stuff, but rather to have the team discuss pros and cons of various 
styles and make a decision on what the guidelines are to be. You don't like 
a certain construct and think it is dangerous; fine, don't use it. But don't 
get unwrapped because someone else did. The fundamental immutable rule is 
that a given programmer is responsible for the code they write. If they take 
the option to override a standard they will have a sound reason for doing 
so, which they can explain if asked to.

I have picked up teams who were beaten into submission and where morale was 
approaching absolute zero. Six months later they are performing beyond the 
expectations of everybody and they are having fun doing it. You don't get it 
by enforcing and banning... you get it by encouraging and supporting. Being 
prepared to explain why you believe something is good or bad, and accepting 
that  they are persuaded or they aren't, but giving them the right to have 
an opinion which may differ from your own. It isn't life and death. It is 
just COBOL programming. It's OK if there is some controversy in it.



> [snip]
>>
…[13 more quoted lines elided]…
> yourself a "programmer". You're just a coder.

I have coded ALTERs. I don't call myself a programmer; other programmers who 
have maintained the code I wrote, do that. Sometimes they call me a guru (I 
discourage that). It is about an attitude. You have a program that is 
broken, it has bad code in it, bring it on. That's what I do. I'm a 
programmer. As a programmer who has worked in the real world, I know that 
code isn't always perfect. But you don't make it better by BANNING 
constructs. You educate, encourage, and show how to deal with stuff. And 
then encouraghe others to spread the word... Sometimes it comes back to you 
and you get support from someone else when you need it.
>>
>> Anyone who advocates the BANNING of a construct in COBOL (or any
…[6 more quoted lines elided]…
>>

Fortunately, I can continue programming without your approval, just as you 
can do so without mine. :-)

>> If you can't stand the heat, don't go in the kitchen.
>
…[5 more quoted lines elided]…
> employer.

Bit late for me, I'm afraid. Besides, I like the kitchen and the heat 
doesn't bother me a bit... :-)

This has been an interesting conversation.

I don't think I have anything to add.

>>
>> By all means, campaign for better coding styles and standards,
…[8 more quoted lines elided]…
> elements *and* work for me.

OK. I think we can both be agreed on that. :-)

Pete.
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 7)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-10-03T14:12:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<da6792ce-f9d7-4b1c-a151-13c409aae412@a4g2000prm.googlegroups.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net> <i8a24k$o1o$1@news.eternal-september.org> <8grt7dFi59U1@mid.individual.net>`

```
On Oct 4, 6:35 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:

> simple code reinstated:
>
…[14 more quoted lines elided]…
>   etc.

ALTER was an archaic construct used by assembler (and machine code)
programmers of the earliest machines. This was required for efficiency
reasons and because there wasn't a stack that could be used to push
down the return.

Without catering for existing (in the 1950s) coding styles COBOL would
have been ignored or rejected by the programmers (just as OO COBOL is
today).

The problem with GOTO is _not_ at the point of the GOTO verb. The
problem is one of localization. With OO, for example, the code is
entirely localised within the object. One can examine the class and
the methods without having to understand the workings of every program
that uses it. That localisation and isolation is what makes large
systems maintainable by teams.

If one is looking at the GOTO itself then it is very simple as to what
will happen. The programmer who wrote the code understands all the
ramifications of the GOTOs and the limits that apply to them.

However, the 'next programmer', given a program that needs changing
wants to not have to understand the whole program. To be efficient he
wants to get to the point where the change is needed and have that
isolated from the rest of the code so that the changes have a
localised effect.

The less localised the code constructs the more of the program will
have to be understood fully. That is, when looking at the _labels_ it
is necessary to know if they are the target of a PERFORM, THRU, GOTO
or drop down. Each of these could affect the logic flow. The mere
presence of THRU, GOTO and PD SECTION in the whole program means that
potentially any label could have logic flow which is not obvious.

Site standards reduce the risks and are intended to increase
localisation. For example "always PERFORM SECTION, only GO TO section -
EXIT" localises logic flow to be within each section. Other site
standards may achieve localisation differently but the aim is to
ensure that it is only necessary to understand smaller parts of the
complete program.

Using CALLed modules and OO classes do this too.

ALTER has the effect of reducing localisation not only spatially via
the GOTOs, but also temporally. In order to understand the logic flow
around a part of the code it is necessary to trace the execution of
the whole program from its starting to the point where the code to be
investigated is actioned. This is the only way to determine which way
the 'rail tracks' are set.

The original writer of the code understands the logic of the
switchings and probably can't understand why they are not obvious to
the 'next programmer'.

I am a lazy programmer. If I have to fix, or extend and enhance,
someone else's code (or even my own) then I don't want to have to
learn the whole picture. I want some small corner of the system and of
the program to be where the requirement lies, to change this and have
it all work correctly.

If it is in a class or a called module then, in theory, only that
needs to be understood and changed. If it is in a SECTION of a program
with GO TOs and THRUs then the whole program needs to be checked at
least to the level of compliance to site standards. If it has ALTERs
then it needs to be ceremonially burnt after a stake has been driven
through the author's heart.


> >> Is it SO difficult that it should be BANNED? Just because it has a
> >> potential for misuse (as, indeed do MOST COBOL verbs...)?

It is not that it is 'difficult' but that it is a complete waster of
programmer time. While it may have been the only way that coding could
be done in the 1950s, and may have saved a few microseconds of machine
time in the 1960s, it failed to meet the changing economics of machine
time vs programmer time (ie costs) in the 1970s and is now three
decades past its 'use by' date.

Arguing that GOTO and ALTER are 'not difficult' completely misses the
point. They are _not_ difficult at the point those verbs are used, the
'difficulty' is at the paragraph labels in the whole of the program
(or within the SECTION in the case of conforming to certain site
standards).

For example if a bare 'GO TO' is seen then there is no way of knowing
what happens without tracing through the code from the start with data
from an actual run. The original programmer may 'know', others may
make assumptions, but whether these match reality can only be
determined by tedious and pointless (and expensive) tracking through
the code, setting switches one way or another.

> No, statistically that would be the misplaced full stop. (The raison d'etre
> for scope delimiters.)

Modern language compilers can warn or error where statement
terminators or separators are missing. Even END-IF can lead to logic
errors which are difficult to see. It is necessary to count IFs and
END-IFs. OpenCOBOL seems to have an option that it will count them for
you while other compilers (MF) silently allow conditional statements
where the standard requires imperative.

> Not necessarily. It is a matter of opinion. Certianly PERFORM does the trick
> less laboriously in the example given, but there are other situations where
> ALTER is actually much better (First time switch for example)

'Better' in what way ? Better at being a 'bug trap' perhaps.

> > and (c) the use of ALTER requires also the use of GO TO, which is
> > another
> > unnecessary construct.
>
> So why not get THAT banned as well?

I have no particular interest in what code you write, as long as I
never have to see it, or pay for it. If I do pay for code or have to
work on it then I will set restrictions on how that code is written,
and that will include a ban on all forms of GO TO as well as other
constructs that I have found to be inefficient of my time (and money).

You may find that to be unnecessarily restrictive. I find it to be
necessary.

> >> Well, if you have people who write code in non-joined up writing by
> >> means of a crayon, perhaps, but to a trained professional who calls
> >> himself a "programmer"?

Insulting people does not produce convincing arguments.

> >> I don't think so, and, frankly, I'm tired of people who never coded
> >> an ALTER in their lives showing how passionate they are about
> >> fighting spaghetti code, and beating the drum for BANNING this and
> >> BANNING that, so that the lowest common denominator can be
> >> comfortable without overtaxing their poor little brains.

Insulting people does not produce convincing arguments.

> And yet for many years before the advent of high level languages it was
> perfectly common practice for instructions to modify other instructions.

When computers were built with valves and mercury tube delay lines for
memory it was necessary to do this. Indeed on some very early machines
the instructions included an implicit GOTO so that the next
instruction could be later in the memory cycle so that several
instructions could be done per cycle.

But then programs were small, limited by memory size, and easily
understood. The standards of engineering for a skate board are not
applicable to a container truck.


> >> (Sorry, it isn't personal; I don't know whether you have coded
> >> ALTERs or not and it really doesn't matter, the thing that's
…[8 more quoted lines elided]…
> However, I also recognise that beauty is in the eye of the beholder.

You continue to look at the wrong end. GO TOs are perfectly
understandable, when you see an ALTER its action is understandable. In
a small, simple, example program, written by yourself, it is _obvious_
what happens.

In a large system with the 'next programmer' ALTERs and GOTOs are
abominations that destroy the ability to maintain the program.

This is based on my experience with the source code of a complete
professional commercial package around 1972 that was investigated
where I worked (ICL in Caltex House). I am sure that the original
coders had no, or few, problems with it, but it wasn't worth the time
needed.

> >> I have seen some amazing solutions that used ALTER in some very
> >> innovative ways and were years ahead of their time. (Multithreading
> >> that used ONE set of code and simply set pathways through it like
> >> railway tracks with points being set by means of ALTER, before
> >> activating it, is just one example burned in my memory.

ALTER is unpure code. Multithreading is incompatible with that. You
may have been impressed by the cleverness of the code but I doubt that
I would have been.


> >> Nevertheless, at a time when multithreading was a
> >> strange, esoteric, concept, this guy wrote an application that
…[7 more quoted lines elided]…
> assumptions which are simply not true.

My 'prejudices and assumptions' are based entirely on working with
code. I was doing COBOL support for ICL in the mid to late 1970s so I
had to investigate customer's code to see why it did strange things.
This included multithreading code written for Wattie's 1904 system
driving their OCR machine.

> In actual fact, as a quite young programmer, I was required to maintain this
> program and did so without any problem at all. Once the fundamental idea was
…[4 more quoted lines elided]…
> comfortable with what they are used to.

Exactly, and thus they fail to move to 'better'.

Actually what you describe sounds like a 'state machine'. These can be
very effective for certain type of systems but ALTER is not the best
way of controlling them. As with all state machines the logic in the
program depends on the 'state' of its switches and this can only be
determined by tracking through the code with data.

> >> Just before I close out this rant, consider the following:
>
…[15 more quoted lines elided]…
> that. :-)

The use of SECTIONs (with GOTO ~EXIT) is better than what was done
before that site standard was imposed. But in the mid 80s even better
ways became available in COBOL with scope terminators removing the
'need' to GOTO ~EXIT. However the site standards were stuck because
the programmer who developed them in the late 70s to early 80s became
a manager and would not approve his 'baby' being defiled by changes he
didn't understand.

Meanwhile other languages, and OO, moved on and COBOL inefficiencies
and obsolete practices were bypassed.

It is irrelevant whether 'most of the COBOL world' knows it or not, it
is 'poor practice' when compared to what could be done (as is done by
some), and indeed when compared to other languages.


> No, it isn't. It is just another coding style. Provided you don't go
> dropping through the sections and ONLY reference them with PERFORM it is a
> very adequate way of coding COBOL. I use sections in OO COBOL for each
> Object method. (It provides a convenient "partition" for encapsulated object
> methods). My programs work.

Whether you use the syntactic sugar of an unnecessary SECTION header
for a method is irrelevant. The referenece was to 'PERFORM xxx SECTION
with GOTO ~EXIT.' which is poor practice when compared to more modern
methods.


> We used sections BEFORE segmentation was introduced. Before disks were
> available we used sections.(Segment-limit was implemented by means of
> section priorty as a convenient way to implement overlaying, after disks
> became available and programs COULD be manually overlaid, but that isn't
> what sections were "invented" for.

Actually disks were not required for overlaying. Overlaying (which
_is_ segmentation) was done on magnetic tapes or on papertape or even
card packs. A COBOL program could be compiled to a card pack and the
overlay system would load each section from the card reader as it was
referenced. It was vital to lay out the source code in the correct
sequence so that the card pack was correctly ordered. Magtape was much
better because it would search for the segment and rewind if
necessary. Disks were faster but not the only way.

The _ONLY_ reason for 'segment-limit' was for segmentation/overlaying.
It was added in ANS'74 to add a _third_ type of segment. Earlier (ie
'68) systems only had fixed or overlayed segments, '74 added 'fixed
overlayable' segments.


> It was primarily a syntactic construct
> that simply fitted the concept of COBOL's hierachic structure: DIVISION >
> SECTION > PARAGRAPH > SENTENCE > STATEMENT
>
> Again, you are trotting out what is perceived wisdom rather than actuality.

As you seem to do yourself on occasions (such as needing disks for
overlaying).


> >> 2. It encouraged programming discipline. Sets of conventions around
> >> the use of ALTERed GO TOs very soon evolved. Nobody coded GO TOs
> >> that pointed somewhere already. As in the example above, the
> >> "points" were initialized to nowhere. (cf. the post I made earlier
> >> today about 88 levels having indeterminacy at the start of a run.)

'encouraged' is not the word I would use. It _required_ discipline, it
_required_ site standards (and the BANNING of non-standard usage), it
_required_ code reviews to get the programmers into maintainable
styles.

"Nobody coded GO TOs that pointed somewhere already" _because_ they
were BANNED by the site standards and ripped out by code reviews.


> > Nor does this improve your case at all. GO TO is a totally unnecessary
> > construct in higher-level languages.
…[6 more quoted lines elided]…
> invariably the fastest instruction in most CISCs.

The reason for moving from archaic (4 address) to obsolete (GOTO) and
to modern is that these are better mechanisms that are catered for by
more modern computers with better capability.

4 address were required by mercury delay line systems to get several
instructions per memory cycle. Unpure code (ALTER) was required by
slow computers (and compilers) so that the program would run in less
than a day. GO TO was required by pre-85 COBOL compilers to avoid even
worse contructs (such as NEXT SENTENCE).

What you did in 1962 is irrelevant to the argument that GO TO is poor
practice today.

> >> 3. If you accepted the title of "Programmer" it meant you were
> >> confident in handling the language you claimed expertise in. That
…[6 more quoted lines elided]…
> Yes, I kind of picked up on that... :-)

I disagree too. Your argument is like saying that cars can be built
with beam front axles and rear wheel brakes only (as they were in the
1920s) because any 'driver' should be confident in handling the
problems. Any driver should cope with axle-tramp and failing to stop.

> It's fine. Your opinion about it is just as valuable as mine. :-)

Or more.


> Hmmmm.... so what was the point of havng constructs in a language if they
> were to be banned on aesthetic grounds? It's a bit like saying there can't
> be any bad music in the world because professional musicians don't play bad
> notes...

It is not an argument about aesthetics.


> > It meant that nothing needed to be banned because professionals would
> > have the
…[3 more quoted lines elided]…
> of what the designers of it intended.

You are talking nonsense. It may be a subset of what was done in the
50s and 60s but it is also a superset. The superset supersedes the
obsolete parts.


> Ever thought about letting the power of an argument persuade somebody? Maybe
> putting your case and letting them make their own minds up? Treating them as
…[3 more quoted lines elided]…
> a tad worried that they might not go along with your own viewpoint on it?

I, and he, don't care what code you write, the ban is on code that I
have to deal with.


> There is nothing so demotivating to an intelligent person than to not be
> allowed to use his intelligence. If YOU can see how terrible things like GO
…[17 more quoted lines elided]…
> so, which they can explain if asked to.

Unfortunately the problem is when that programmer is no longer part of
the team and thus is not there to explain it. This is the whole point
that you seem to fail to understand. The whole concept of the plight
of 'the next programmer' seems to be foreign to you.

We have all been presented code to work on where the author is no
longer available and the reasons for particular structures have been
lost. Site-standards originated to ensure that the author need no be
available. This included banning constructs that _needed_ explaining
by the author.



> I have coded ALTERs. I don't call myself a programmer; other programmers who
> have maintained the code I wrote, do that. Sometimes they call me a guru (I
…[6 more quoted lines elided]…
> and you get support from someone else when you need it.

As a contractor I can deal with bad code by explaining why it will
take a long time to deal with and consequently sending in a large bill
(ie equals my revenue). As a programmer on my systems, and a lazy one,
I don't write 'clever' or 'guru style' code because I know that I will
later take too long (unbilled) to add any changes.

Contractors and site programmers have different viewpoints on these
issues. Contractors can disappear and not deal with consequences or
can bill for the time to deal with them.

> >> Anyone who advocates the BANNING of a construct in COBOL (or any
> >> other language, actually), in my book, is not fit to be called
…[7 more quoted lines elided]…
> can do so without mine. :-)

Exactly. If he bans it on his site that is nothing to you.
```

###### ↳ ↳ ↳ Move Corresponding and qualification was Re: A COBOL conundrum

_(reply depth: 7)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2010-10-04T16:06:29-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cj8ka61q2bboi0oqqdav3pjh0vuv7npitg@4ax.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net> <i8a24k$o1o$1@news.eternal-september.org> <8grt7dFi59U1@mid.individual.net>`

```
On Mon, 4 Oct 2010 06:35:39 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Doug Miller wrote:
>> In article <8gqr9gF5uqU1@mid.individual.net>, "Pete Dashwood"
…[20 more quoted lines elided]…
>CORR.

The problem is with the brain dead way COBOL does qualification.
Instead of being able to say File-A.Record-1.Customer-number like most
good languages including DYL280 (now Vision something or another), you
have to write Customer-number OF Record-1 OF File-A.  This is awkward
to most English speakers who say Joe's book, NOT book of Joe most of
the time.  As part of my comments to the 1985 standard, I complained
about this to no avail.  This awkwardness makes it undesirable to copy
a record description in all of the places it should be (input file,
output file, working-storage, etc.).  I put up with the ^%&%$
awkwardness so that I know the same description is used everywhere and
that when it changes all instances of that record in a program are
changed.  Although I am going on 4 years being away from COBOL
programming this still rankles.  

Move Corresponding (also Add and Subtract) had another defect in that
it was difficult to tell from the listing what fields were affected
either by a listing all of the generated individual moves or an
informational message of fields not moved where there were
mis-matches.  This latter failing could have been addressed by the
various vendors which would have changed the CORRESPONDING option from
one that could lead to subtle errors to a very useful one.

Clark Morris 
>
>> rest snipped
>
>Pete.
```

###### ↳ ↳ ↳ Re: Move Corresponding and qualification was Re: A COBOL conundrum

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-10-04T13:50:20-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<stbka6l7k7dijt2frhd2u5s8mmmdn8m46p@4ax.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net> <i8a24k$o1o$1@news.eternal-september.org> <8grt7dFi59U1@mid.individual.net> <cj8ka61q2bboi0oqqdav3pjh0vuv7npitg@4ax.com>`

```
On Mon, 04 Oct 2010 16:06:29 -0300, Clark F Morris
<cfmpublic@ns.sympatico.ca> wrote:

>The problem is with the brain dead way COBOL does qualification.
>Instead of being able to say File-A.Record-1.Customer-number like most
…[3 more quoted lines elided]…
>the time.

I disagree.  It's the way English works.   Programmers with newer
languages think of dot notation, but programming languages aren't
"most English speakers".
```

###### ↳ ↳ ↳ Re: Move Corresponding and qualification was Re: A COBOL conundrum

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-10-05T11:38:16+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gv3aoF2rqU1@mid.individual.net>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net> <i8a24k$o1o$1@news.eternal-september.org> <8grt7dFi59U1@mid.individual.net> <cj8ka61q2bboi0oqqdav3pjh0vuv7npitg@4ax.com> <stbka6l7k7dijt2frhd2u5s8mmmdn8m46p@4ax.com>`

```
Howard Brazee wrote:
> On Mon, 04 Oct 2010 16:06:29 -0300, Clark F Morris
> <cfmpublic@ns.sympatico.ca> wrote:
…[10 more quoted lines elided]…
> "most English speakers".

Nevertheless, it would have been possible ot find something closer to "Joe's 
book" rather than "Book of Joe".

If they couldn't use dot notation (and given the importance of dots in 
COBOL, it is understandable why they'd be reluctant...) they could certainly 
have used a similar notation. The colon has been implented in OO CBOL to 
provide a shorthand notation; maybe they could use some other character that 
isn't already serving a specifc purpose (rules out currency signs), maybe # 
or something similar.

FileA#Record-1#Customer-Number     seems a reasonable alternative to 
Customer-number OF Record-1 OF File-A (at least, it does to me, but I may 
have become so accustomed to dot notation now that I would see it that 
way...) and is more natural (top down rather than bottom up).

Never mind, it didn't happen and it is now pretty moot...

Pete.
```

###### ↳ ↳ ↳ Re: Move Corresponding and qualification was Re: A COBOL conundrum

_(reply depth: 10)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-10-05T09:17:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j5gma69h20jnvlj1idu2tknscvb4d5ucqm@4ax.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net> <i8a24k$o1o$1@news.eternal-september.org> <8grt7dFi59U1@mid.individual.net> <cj8ka61q2bboi0oqqdav3pjh0vuv7npitg@4ax.com> <stbka6l7k7dijt2frhd2u5s8mmmdn8m46p@4ax.com> <8gv3aoF2rqU1@mid.individual.net>`

```
On Tue, 5 Oct 2010 11:38:16 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>>> The problem is with the brain dead way COBOL does qualification.
>>> Instead of being able to say File-A.Record-1.Customer-number like
…[17 more quoted lines elided]…
>or something similar.

It may have made a better language - but a colon would not have been
more English like.   And for better or worse, English-like was a
primary goal.

If they had used a colon, I would expect that we would have "colon
notation" today instead of dot notation.   Other languages that didn't
have the goal of being English like would have had something to copy
that worked.
```

###### ↳ ↳ ↳ Re: Move Corresponding and qualification was Re: A COBOL conundrum

_(reply depth: 11)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2010-10-05T12:07:28-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4OWdnXmrw_qz0DbRnZ2dnUVZ_uSdnZ2d@earthlink.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net> <i8a24k$o1o$1@news.eternal-september.org> <8grt7dFi59U1@mid.individual.net> <cj8ka61q2bboi0oqqdav3pjh0vuv7npitg@4ax.com> <stbka6l7k7dijt2frhd2u5s8mmmdn8m46p@4ax.com> <8gv3aoF2rqU1@mid.individual.net> <j5gma69h20jnvlj1idu2tknscvb4d5ucqm@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:j5gma69h20jnvlj1idu2tknscvb4d5ucqm@4ax.com...
> On Tue, 5 Oct 2010 11:38:16 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[40 more quoted lines elided]…
> - James Madison

Great! So as part of the debugging process of our COBOL programs we would 
have to give them a colonoscopy?
```

###### ↳ ↳ ↳ Re: Move Corresponding and qualification was Re: A COBOL conundrum

_(reply depth: 11)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-10-05T11:20:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<69f6f1af-2729-48ef-87cb-404d5bd31879@u4g2000prn.googlegroups.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net> <i8a24k$o1o$1@news.eternal-september.org> <8grt7dFi59U1@mid.individual.net> <cj8ka61q2bboi0oqqdav3pjh0vuv7npitg@4ax.com> <stbka6l7k7dijt2frhd2u5s8mmmdn8m46p@4ax.com> <8gv3aoF2rqU1@mid.individual.net> <j5gma69h20jnvlj1idu2tknscvb4d5ucqm@4ax.com>`

```
On Oct 6, 4:17 am, Howard Brazee <how...@brazee.net> wrote:
> On Tue, 5 Oct 2010 11:38:16 +1300, "Pete Dashwood"
>
…[26 more quoted lines elided]…
> primary goal.

In what way is Record:field:subfield 'English-like' ?


> If they had used a colon, I would expect that we would have "colon
> notation" today instead of dot notation.   Other languages that didn't
> have the goal of being English like would have had something to copy
> that worked.

The colon was already used in various languages. Algol, which predated
COBOL, used them as part of the assignment statement (eg: x := 1) to
distinguish it from equality, and this example was followed by Pascal
and its derivatives.

C copied prior languages (CPL, BCPL, B) and used it in an English like
way, it introduces a list, as the label indicator. eg:

         switch ( type ) {
         case NUMBER:    process_number();
                         break;
         case LETTER:    process..

PERL does use a double colon (eg Module::function() ) but I would hope
that no one copies what PERL does or how it does it.
```

###### ↳ ↳ ↳ Re: Move Corresponding and qualification was Re: A COBOL conundrum

_(reply depth: 12)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-10-05T13:29:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bvuma69m8cmsuv3ch9l4gtlo37bnspd6du@4ax.com>`
- **References:** `<34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net> <i8a24k$o1o$1@news.eternal-september.org> <8grt7dFi59U1@mid.individual.net> <cj8ka61q2bboi0oqqdav3pjh0vuv7npitg@4ax.com> <stbka6l7k7dijt2frhd2u5s8mmmdn8m46p@4ax.com> <8gv3aoF2rqU1@mid.individual.net> <j5gma69h20jnvlj1idu2tknscvb4d5ucqm@4ax.com> <69f6f1af-2729-48ef-87cb-404d5bd31879@u4g2000prn.googlegroups.com>`

```
On Tue, 5 Oct 2010 11:20:32 -0700 (PDT), Richard <riplin@Azonic.co.nz>
wrote:

>> It may have made a better language - but a colon would not have been
>> more English like. ï¿½ And for better or worse, English-like was a
>> primary goal.
>
>In what way is Record:field:subfield 'English-like' ?

That was my question.   I don't see it.

>> If they had used a colon, I would expect that we would have "colon
>> notation" today instead of dot notation. ï¿½ Other languages that didn't
…[6 more quoted lines elided]…
>and its derivatives.

ALGOL didn't have the wide acceptance CoBOL had.   Languages also had
dots (as decimal points).   Dot notation could easily have been colon
notation if there was a widely accepted precedent.
```

###### ↳ ↳ ↳ Re: Move Corresponding and qualification was Re: A COBOL conundrum

_(reply depth: 13)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-10-05T14:30:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b57eef57-0dae-4ebc-be36-47ac825c4b0b@l38g2000pro.googlegroups.com>`
- **References:** `<34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net> <i8a24k$o1o$1@news.eternal-september.org> <8grt7dFi59U1@mid.individual.net> <cj8ka61q2bboi0oqqdav3pjh0vuv7npitg@4ax.com> <stbka6l7k7dijt2frhd2u5s8mmmdn8m46p@4ax.com> <8gv3aoF2rqU1@mid.individual.net> <j5gma69h20jnvlj1idu2tknscvb4d5ucqm@4ax.com> <69f6f1af-2729-48ef-87cb-404d5bd31879@u4g2000prn.googlegroups.com> <bvuma69m8cmsuv3ch9l4gtlo37bnspd6du@4ax.com>`

```
On Oct 6, 8:29 am, Howard Brazee <how...@brazee.net> wrote:
> On Tue, 5 Oct 2010 11:20:32 -0700 (PDT), Richard <rip...@Azonic.co.nz>
> wrote:
…[17 more quoted lines elided]…
> >and its derivatives.

> ALGOL didn't have the wide acceptance CoBOL had.

Maybe not in the world dominated by COBOL but Algol was well used
outside of business programming and was very influential, more so that
FORTRAN. It led directly to Pascal (which was originally named Algol-
W) and indirectly to C and even Java. Simula (standardised in 1966)
was also Algol-like, enough to be classed as a derivative, and that
led to all modern OO languages.

> Languages also had
> dots (as decimal points).   Dot notation could easily have been colon
> notation if there was a widely accepted precedent.

COBOL adopted qualification in '68 by which time there were plenty of
precedents for using colon - as a label marker.

While Algol, Simula and C were used as precedents for dozens, possibly
hundreds, of later languages, you would have trouble finding any later
significant language that used COBOL as a precendent for anything.
```

###### ↳ ↳ ↳ Re: Move Corresponding and qualification was Re: A COBOL conundrum

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-10-05T11:30:01+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gv2raFvmbU1@mid.individual.net>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net> <i8a24k$o1o$1@news.eternal-september.org> <8grt7dFi59U1@mid.individual.net> <cj8ka61q2bboi0oqqdav3pjh0vuv7npitg@4ax.com>`

```
Clark F Morris wrote:
> On Mon, 4 Oct 2010 06:35:39 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[51 more quoted lines elided]…
>> Pete.

Yes, I'd have to agree that if the things you mention had been implemented, 
we'd probably see a lot more use of MOVE... CORR.

The IDEA is a good one; it simply suffered from the way it was implemented.

Pete.
```

###### ↳ ↳ ↳ Re: Move Corresponding and qualification was Re: A COBOL conundrum

_(reply depth: 9)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2010-10-05T12:02:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgima6dbd7r5578tin4me7ab2tctipch1e@4ax.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net> <i8a24k$o1o$1@news.eternal-september.org> <8grt7dFi59U1@mid.individual.net> <cj8ka61q2bboi0oqqdav3pjh0vuv7npitg@4ax.com> <8gv2raFvmbU1@mid.individual.net>`

```
On Tue, 5 Oct 2010 11:30:01 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Clark F Morris wrote:
>> On Mon, 4 Oct 2010 06:35:39 +1300, "Pete Dashwood"
…[59 more quoted lines elided]…
>Pete.

While it has been around 10 years, maybe more, since I used MOVE CORR,
I found it an invaluable and code saving technique that last time I
did use it.

Here was the situation.  We were tasked with created a file delimited
by Hex 09 (between each field) from a mainframe master file.  The
delimited file would be FTPed to a Unix Server.

The file contained around 100 different fields.  Certainly if you had
to write 100 (or more) move statements, it would be very time
consuming.  And if any new fields were created in the file or deleted
or moved, that would entail maintenance.

The solution.  the original file had a copybook associated with it.  I
copied that copybook to another name changing only the 01 level name.
I then tediously put a 1 byte filler field in between each field. But
the time spent here was time saved coding move statements.

One simple MOVE ALL X'09' to the 01 Level output file placed
delimiters in the file.  Then another simple MOVE CORR input 01 level
name to output 01 level name took care of filling in all of the
fields.  Write output and go read another record.

Regards,
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 7)_

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2010-10-05T02:44:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i8e3df$lk1$1@news.eternal-september.org>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net> <i8a24k$o1o$1@news.eternal-september.org> <8grt7dFi59U1@mid.individual.net>`

```
In article <8grt7dFi59U1@mid.individual.net>, "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote:
>Doug Miller wrote:
>> In article <8gqr9gF5uqU1@mid.individual.net>, "Pete Dashwood"
…[60 more quoted lines elided]…
>..... that achieves exactly the same result as the alternative.

It demonstrably does nothing of the kind.

You are looking *only* at the results of executing the code, and completely 
ignoring the cost of maintaining it.
>
>>>
…[53 more quoted lines elided]…
>ALTER is actually much better (First time switch for example)

Remove your blinders.

Once again, you are looking only at execution, and ignoring maintainability.
>
>> and (c) the use of ALTER requires also the use of GO TO, which is
…[3 more quoted lines elided]…
>So why not get THAT banned as well?

Good idea.
>
>>>
…[17 more quoted lines elided]…
>perfectly common practice for instructions to modify other instructions.

I know that -- but what you fail to realize is that for many years before the 
advent of high level languages, it was *still* a bad idea.
>>>
>>> (Sorry, it isn't personal; I don't know whether you have coded
…[9 more quoted lines elided]…
>However, I also recognise that beauty is in the eye of the beholder.

Wow. Simply amazing.
>
>
…[7 more quoted lines elided]…
>language. It's removal ahs made COBOL neither more nor less elegant.

Only in the sense that its removal made very little difference anyway, since 
no programmer with any good sense ever used it to begin with.
>
>> [snip]
…[50 more quoted lines elided]…
>that. :-)

I imagine most of the Cobol world has already figured that out.
>
>No, it isn't. It is just another coding style. Provided you don't go 
…[3 more quoted lines elided]…
>methods). My programs work.

I'm sure they do. But you seem to believe that to be the only criterion of a 
good program.

You are grossly mistaken.
>
>
…[29 more quoted lines elided]…
>occasion in COBOL and all the time in certain assemblers.

Assemblers are *by definition* NOT "higher-level languages".

> In fact One 
>assembler I wrote used a 4 address system that ensured EVERY instruction was 
…[29 more quoted lines elided]…
>notes...

Very poor analogy there. A better one: there can't be any bad music in the 
world because competent *composers* don't write bad music.

Unfortunately, the world contains both incompetent composers and incompetent 
programmers, and so we have both bad music and bad software.

>> It meant that nothing needed to be banned because professionals would
>> have the
…[3 more quoted lines elided]…
>of what the designers of it intended.

The designers of most things do at best an incomplete job of imagining how 
their designs will, can, or should be used in the real world, and the 
designer's intent is thus usually not a very good yardstick by which to 
measure the suitability of the uses to which the design may be put.

One simple example: the simple screwdriver. I have, as I'm sure most of us 
have, a number of straight-bladed screwdrivers. How often do you actually use 
one for turning a screw? They're much more frequently used as prying or 
scraping tools, and the handles make decent mallets, too.
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 8)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-10-05T12:30:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8h0k34F3bgU1@mid.individual.net>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net> <i8a24k$o1o$1@news.eternal-september.org> <8grt7dFi59U1@mid.individual.net> <i8e3df$lk1$1@news.eternal-september.org>`

```
In article <i8e3df$lk1$1@news.eternal-september.org>,
	spambait@milmac.com (Doug Miller) writes:
> 
> One simple example: the simple screwdriver. I have, as I'm sure most of us 
> have, a number of straight-bladed screwdrivers. How often do you actually use 
> one for turning a screw? They're much more frequently used as prying or 
> scraping tools, and the handles make decent mallets, too.

It's a poor workman who blames his tools.  I have numerous screwdrivers
in my toolbox.  I use them to insert and remove screws.   I also have
scrapers, prybars and several hammers of different weights and styles,
including wooden, brass and rubber mallets.  I apply the same rules to
my programming that I apply to my automotive, carpentry and any other
work I do.  Use the right tool for the job.  And, believe it or not,
that is why I am writing an administrative program for where I work
now in, wait for it, COBOL!!!  Why you might ask?  Because the problem
to be solved is totally record oriented.  I get a classlist from the
Registrar's Office and I need to use it to generate a file containing
colon separated records as input to the the new uswer program on our
servers.  Hmmmm....  Simple records in, simple records out.  What language
could possibly do this job better or easier?  And, while were on the
subject, anyone care to tell me what OO wold buy me in this case?  ;-)

bill
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-10-05T13:33:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i8f9g7$qj3$1@reader1.panix.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <8grt7dFi59U1@mid.individual.net> <i8e3df$lk1$1@news.eternal-september.org> <8h0k34F3bgU1@mid.individual.net>`

```
In article <8h0k34F3bgU1@mid.individual.net>,
Bill Gunshannon <billg999@cs.uofs.edu> wrote:

[snip]

>Simple records in, simple records out.  What language
>could possibly do this job better or easier?

Obviously... DFSORT, but if and only if the record format never, *ever* 
changes either on the input or output sides.

DD
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 10)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-10-05T19:12:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8h1bkbFln5U9@mid.individual.net>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <8grt7dFi59U1@mid.individual.net> <i8e3df$lk1$1@news.eternal-september.org> <8h0k34F3bgU1@mid.individual.net> <i8f9g7$qj3$1@reader1.panix.com>`

```
In article <i8f9g7$qj3$1@reader1.panix.com>,
	docdwarf@panix.com () writes:
> In article <8h0k34F3bgU1@mid.individual.net>,
> Bill Gunshannon <billg999@cs.uofs.edu> wrote:
…[8 more quoted lines elided]…
> 

And how many free implementations of DFSORT on how many low cost platforms
are there?  Did i fail to mention I have no budget tied to this operation?

bill
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-10-05T20:06:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i8g0gn$n90$1@reader1.panix.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <8h0k34F3bgU1@mid.individual.net> <i8f9g7$qj3$1@reader1.panix.com> <8h1bkbFln5U9@mid.individual.net>`

```
In article <8h1bkbFln5U9@mid.individual.net>,
Bill Gunshannon <billg999@cs.uofs.edu> wrote:
>In article <i8f9g7$qj3$1@reader1.panix.com>,
>	docdwarf@panix.com () writes:
…[13 more quoted lines elided]…
>are there?  Did i fail to mention I have no budget tied to this operation?

Not only did you fail to ask those questions or mention your budget, Mr 
Gunshannon... but you neglected to state that Bismarck is a herring, the 
capitol of North Dakota and an 'unsinkable' German battleship, as well.

You stated 'Simple records in, simple records out.  What language could 
possibly do this job better or easier?' and got an answer... have you 
become a fan of Scope Creep in your antiquity?

'... and in blue, the errors have to be highlighted in blue... how hard 
can that be, all ya gotta do is... '

DD
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 12)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-10-05T21:25:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8h1je2Fln5U12@mid.individual.net>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <8h0k34F3bgU1@mid.individual.net> <i8f9g7$qj3$1@reader1.panix.com> <8h1bkbFln5U9@mid.individual.net> <i8g0gn$n90$1@reader1.panix.com>`

```
In article <i8g0gn$n90$1@reader1.panix.com>,
	docdwarf@panix.com () writes:
> In article <8h1bkbFln5U9@mid.individual.net>,
> Bill Gunshannon <billg999@cs.uofs.edu> wrote:
…[26 more quoted lines elided]…
> can that be, all ya gotta do is... '

Well, one makes assumptions when one posts in a language specific newsgroup.
Now, where is comp.land.dfsort......

:-)

bill
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 9)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-10-05T16:05:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c0e05fec-13b9-4269-91b6-ff3977deabc5@i4g2000prf.googlegroups.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net> <i8a24k$o1o$1@news.eternal-september.org> <8grt7dFi59U1@mid.individual.net> <i8e3df$lk1$1@news.eternal-september.org> <8h0k34F3bgU1@mid.individual.net>`

```
On Oct 6, 1:30 am, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
> In article <i8e3df$lk...@news.eternal-september.org>,
>         spamb...@milmac.com (Doug Miller) writes:
…[19 more quoted lines elided]…
> servers.  Hmmmm....

> Simple records in, simple records out.  What language
> could possibly do this job better or easier?  

AWK, Python, ..

But this depends on whether 'easier' needs to include 'learning the
language'.


> And, while were on the
> subject, anyone care to tell me what OO wold buy me in this case?  ;-)

One of the reasons that COBOL programmers have a tendency not to move
to OO is that there is generally not much point in doing so. It is not
that they don't understand OO, which is generally alleged, but that
with much of the work done by COBOL programmers serial reusability is
required, not OO.

While OO does offer many features the main additional one that it
offers for COBOL is multiple objects. For example I have tried coding
the same problem in OO and non-OO COBOL. The non-OO used a called
module with a function code indicating the 'method' required. The
module held the data items. With OO the object held the data and the
methods were invoked. Apart from a different syntax the only real
difference was that with the called module I was stuck with only
having one instance whereas with OO I could have multiple instances.

Problems dealt with by COBOL tend to only need one instance of each
data item that is serially reused, even in interactive systems.
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-10-05T09:20:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pdgma69k3tsjm5110g6pee7vo8e1tt3qgj@4ax.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net> <i8a24k$o1o$1@news.eternal-september.org> <8grt7dFi59U1@mid.individual.net> <i8e3df$lk1$1@news.eternal-september.org>`

```
On Tue, 05 Oct 2010 02:44:02 GMT, spambait@milmac.com (Doug Miller)
wrote:

>>Many people would agree with you. That's why it is no longer in the 
>>language. It's removal ahs made COBOL neither more nor less elegant.
>
>Only in the sense that its removal made very little difference anyway, since 
>no programmer with any good sense ever used it to begin with.

I disagree.   At one time, "efficient" meant "use every trick you can
find to make the program run faster - even if it costs plenty in
programming and maintenance - because computing time was much more
expensive than programming costs, and even more expensive in business
delays to maintain the code".

Of course, criteria for measuring efficiency have changed, as the
input variables have different costs.
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-10-05T09:23:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vkgma6hn7rsc1sud6mdntma4047iutnc0o@4ax.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net> <i8a24k$o1o$1@news.eternal-september.org> <8grt7dFi59U1@mid.individual.net> <i8e3df$lk1$1@news.eternal-september.org>`

```
On Tue, 05 Oct 2010 02:44:02 GMT, spambait@milmac.com (Doug Miller)
wrote:

>One simple example: the simple screwdriver. I have, as I'm sure most of us 
>have, a number of straight-bladed screwdrivers. How often do you actually use 
>one for turning a screw? They're much more frequently used as prying or 
>scraping tools, and the handles make decent mallets, too.

I wouldn't guess your conclusion based upon my experience.    What is
the population that you used to determine this?
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-10-04T12:54:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ll8ka6t5u5qralvkm2g2tf9advu5u2s8hh@4ax.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net>`

```
On Sun, 3 Oct 2010 20:56:30 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>So you've had a lot of experience dealing with it and found it difficult?
>
…[7 more quoted lines elided]…
>hardware...)

I have used it, and seen problems with how it was maintained.
Redefining "efficiency" is important as values change.
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 6)_

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2010-10-05T02:51:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i8e3qk$lkl$1@news.eternal-september.org>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net> <ll8ka6t5u5qralvkm2g2tf9advu5u2s8hh@4ax.com>`

```
In article <ll8ka6t5u5qralvkm2g2tf9advu5u2s8hh@4ax.com>, Howard Brazee <howard@brazee.net> wrote:
>On Sun, 3 Oct 2010 20:56:30 +1300, "Pete Dashwood"
><dashwood@removethis.enternet.co.nz> wrote:
…[14 more quoted lines elided]…
>
Absolutely right. There was a time when the machine's time was more valuable 
than the programmer's. Now, the programmer's time is more valuable than the 
machine's. And it has been for a long, long time. We passed that point 
somewhere around thirty years ago.

Seems not everyone has gotten the memo yet.
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-10-05T09:24:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<apgma6hnq532q59562v8pi2ptvjqtgms2m@4ax.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net> <ll8ka6t5u5qralvkm2g2tf9advu5u2s8hh@4ax.com> <i8e3qk$lkl$1@news.eternal-september.org>`

```
On Tue, 05 Oct 2010 02:51:03 GMT, spambait@milmac.com (Doug Miller)
wrote:

>>I have used it, and seen problems with how it was maintained.
>>Redefining "efficiency" is important as values change.
…[4 more quoted lines elided]…
>somewhere around thirty years ago.

Don't forget the opportunity cost in not getting the user's
modifications completed in a timely manner.
```

###### ↳ ↳ ↳ ALTER with today's compilers was Re: A COBOL conundrum

_(reply depth: 5)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2010-10-04T16:33:22-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e9ka6hmietlbjs8tsjcg9htv6usq6qsdh@4ax.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <8gqr9gF5uqU1@mid.individual.net>`

```
On Sun, 3 Oct 2010 20:56:30 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Doug Miller wrote:
>> In article <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com>,
…[109 more quoted lines elided]…
>

As someone whose payroll programs used ALTER SW4050-PRINT-EX TO
PROCEED TO 3800-PROCESS-NEXT-LINE constructs extensively because of
the code generation difference on a DOS IBM360 model 30, I would
oppose the use of ALTER today both on clarity and performance bases.

The current z/OS compilers and at least the MVS/OS390/z series 1985
standard and beyond compilers have made PERFORM without the THRU
option and the inline PERFORM of the 1985 standard very efficient.
Depending on various things, the performed paragraph may be moved
in-line to eliminate the paragraph completely.  The setting of flags
and then testing them probably is as efficient on today's systems with
pipelining as the altered branch and may be more so on oz series if
the branch relative instruction is used.  A switch would be 
L R15,Address_of_Target  Load the full word Address of the Paragraph 
BR R15  Branch to the paragraph while the test would be 
Compare logical immediate truth-value-character to Switch-field
Branch Relative Not Equal around code or perform.

Eliminating the alter removes a number of the paragraph names needed
and also aids in creating re-entrant programs for compilers.

Thus because of the change in the technical environment and because it
is now easy to create the same type of utility that you mention with
greater clarity, I agree with the elimination of ALTER.  Any programs
that still use it should be cleaned up and will probably run with
slight but measurable performance improvement if done correctly. 

Clark Morris

PS, after I had moved to systems programming the person who had the
misfortune to inherit my payroll programs went to my boss at the time
and told him that he was worried because he was beginning to
understand my payroll programs.  This person was a sharp programmer
who I respected.  



>> rest snipped
>
>Pete.
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 4)_

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-10-03T03:57:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RzXpo.222681$MG3.59308@en-nntp-16.dc1.easynews.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org>`

```
"Doug Miller" <spambait@milmac.com> wrote in message 
news:i88sji$hqu$1@news.eternal-september.org...
> In article <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com>, 
> arnold.trembley@att.net wrote:
>
<snip>
> Oh, I would. In a heartbeat. Use ALTER and you're fired. If it were up to 
> me,
> that wouldn't *be* "a legal COBOL verb". I think it should have been 
> removed
> from the standard years ago.

It was removed fromt he language years ago.  It is NOT part of the 2002 
Standard.

Of course, many (most?) vendors still support it, but it was removed from 
the "official" language definition 8 years ago (with a warning that it was 
to be removed 25 years ago in the 1985 Standard)
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-10-04T00:05:28+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gr6bqF620U1@mid.individual.net>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <RzXpo.222681$MG3.59308@en-nntp-16.dc1.easynews.com>`

```
Bill Klein wrote:
> "Doug Miller" <spambait@milmac.com> wrote in message
> news:i88sji$hqu$1@news.eternal-september.org...
…[11 more quoted lines elided]…
> 2002 Standard.

And the manner of its removal was shameful... :-)

It was largely as a result of pressure from IBM mainframe User Groups that 
it was decided to phase it out.

People who were NOT working on IBM sites at the time really had no say in 
it; although most people had been brainwashed into believing it was a Bad 
Thing so there was little demurral.
>
> Of course, many (most?) vendors still support it, but it was removed
> from the "official" language definition 8 years ago (with a warning
> that it was to be removed 25 years ago in the 1985 Standard)

I'm probably the last person on the planet who supports the use of it... :-)

Pete.
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 6)_

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-10-03T08:19:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cp%po.214068$Bh.64528@en-nntp-12.dc1.easynews.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <RzXpo.222681$MG3.59308@en-nntp-16.dc1.easynews.com> <8gr6bqF620U1@mid.individual.net>`

```
Pete,
   I think that either your memory is incorrect or you weren't actually 
aware of what was happening at the time.

When the '85 Standard was still in development (c. 1980), the CODASYL group 
decided to REMOVE a number of featurss (including ALTER).  Knowing the IBM 
reps of the time and other thigns going on within CODASYL, it is VERY 
unlikely (IMHO) that IBM was a major player in this move. (My guess is that 
if you want to "blame" any COBOL vendors of the time, it was most likely 
this started with DEC and TANDEM reps on CODASYL)

It wa Hartford Insurance (and a  number of other larger IBM mainframe shops 
that SCREAMED AND YELLED *against* these removals).

X3J4 then (sort-of) "gave in" when these IBM mainframe shops threatened to 
sue ANSI.  The "compromise" that X3J4 came up with was NOT to remove these 
items in the 1985 Standard, but instead to mark them as "obsolete" with an 
indication that they would be removed in the NEXT Standard (which they were 
in 2002).

It is certainly true that many IBM mainframe shops were "impressed" by the 
arguments for "structured" programming in the late 1970's and early 1980's. 
Therefore, the use of GO TO, ALTER, and a number of other structures were 
"deprecated" as shop standards.  (IBM mainframe shops of that era - and to 
some extent the current era - were "in to" shop standards.  See the start of 
this thread).  However, if it weren't for large IBM mainframe shops, ALTER 
would have been REMOVED from the Standard in 1985, not 2002.

If you have some evidence that I am missing (or mis-remembering) that 
indicates that it was IBM mainframe shops trying to get rid of ALTER that 
caused CODASYL to do so, I would be very intererested in seeing such.

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:8gr6bqF620U1@mid.individual.net...
> Bill Klein wrote:
>> "Doug Miller" <spambait@milmac.com> wrote in message
…[34 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-10-04T04:57:49+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8grng2Fe2qU1@mid.individual.net>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <RzXpo.222681$MG3.59308@en-nntp-16.dc1.easynews.com> <8gr6bqF620U1@mid.individual.net> <cp%po.214068$Bh.64528@en-nntp-12.dc1.easynews.com>`

```
Bill Klein wrote:
> Pete,
>   I think that either your memory is incorrect or you weren't actually
> aware of what was happening at the time.

Possibly both... :-)

OK, let's hear your story...
>
> When the '85 Standard was still in development (c. 1980), the CODASYL
…[5 more quoted lines elided]…
> on CODASYL)

I believe the plot against ALTER happened well before that.

There was talk of removing ALTER at the time of the 1974 standard. My 
understanding (from memory) is that CODASYL was long gone, the 74 standard 
being the first ANSI one. Now, I would defer to your knowledge of these 
things, Bill, and it was a long time ago, but I remember having 
conversations with IBM people about this and they were all Gung-Ho to remove 
ALTER.  Admittedly, this was in NZ so your perspective from the USA would 
likely be more informed. At the time, I took a very keen interest in COBOL 
and was pretty much aware of what was happening, I think..

I'm not really looking for "someone to blame" (I generally don't do that...) 
I was simply calling it as I remember it. It is all academic now... :-) If, 
as you say, the IBM User Groups in the USA were in support of retaining it, 
that certainly didn't fit with their Antipodean colleagues...

I had a number of friends at IBM at the time and, although I was workng on 
non-IBM mainframes, I kept well abreast of the inside chatter..



>
> It wa Hartford Insurance (and a  number of other larger IBM mainframe
> shops that SCREAMED AND YELLED *against* these removals).
>

I certainly didn't know about that. There was not the same feeling in NZ.


> X3J4 then (sort-of) "gave in" when these IBM mainframe shops
> threatened to sue ANSI.  The "compromise" that X3J4 came up with was
> NOT to remove these items in the 1985 Standard, but instead to mark
> them as "obsolete" with an indication that they would be removed in
> the NEXT Standard (which they were in 2002).

Yes, I knew about that, but that was much later.
>
> It is certainly true that many IBM mainframe shops were "impressed"
…[6 more quoted lines elided]…
> from the Standard in 1985, not 2002.

It would have been removed in 1974 except that there were still enough 
people using it to make their presence felt. As you say, with the advent of 
structured programming it was on a hiding to nothing anyway... :-)
>
> If you have some evidence that I am missing (or mis-remembering) that
> indicates that it was IBM mainframe shops trying to get rid of ALTER
> that caused CODASYL to do so, I would be very intererested in seeing
> such.

I don't believe it was CODASYL, but I'm happy to be corrected. I remember 
obtaining a copy of the standard around that time and it was X21 or X23 or 
something like that, and it came from ANSI. The Conference On Data Systems 
Languages set up in 1959 I believe had handed it over to ANSI by 1974, but I 
could be wrong. Apart from that, I accept your point that SOME IBM users (in 
the USA at least...) were keen to retain ALTER.

Cheers,

Pete.
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 8)_

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-10-03T11:34:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ng2qo.228039$pX3.12511@en-nntp-11.dc1.easynews.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <RzXpo.222681$MG3.59308@en-nntp-16.dc1.easynews.com> <8gr6bqF620U1@mid.individual.net> <cp%po.214068$Bh.64528@en-nntp-12.dc1.easynews.com> <8grng2Fe2qU1@mid.individual.net>`

```
Just to answer one part of this note
   CODASYL continued until about the time of the 2nd amendment to the '85 
Standard.  Both the Intrinsic Function Amendment and the Correction 
Amendment were done while CCC (CODASYL COBOL Committe) was still doing its 
thing.  (I could check on what the date is of my last JOD, but I dfon't 
think you really care).

The '85 Standard (as documented in its "history" section) still had all 
"development" done by CODASYSLand then X3J4 "took" its work and adopted and 
adjusted it to become the new Standard.

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:8grng2Fe2qU1@mid.individual.net...
> Bill Klein wrote:
>> Pete,
…[84 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-10-04T06:42:15+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8grtjpFkk3U1@mid.individual.net>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <RzXpo.222681$MG3.59308@en-nntp-16.dc1.easynews.com> <8gr6bqF620U1@mid.individual.net> <cp%po.214068$Bh.64528@en-nntp-12.dc1.easynews.com> <8grng2Fe2qU1@mid.individual.net> <Ng2qo.228039$pX3.12511@en-nntp-11.dc1.easynews.com>`

```
Bill Klein wrote:
> Just to answer one part of this note
>   CODASYL continued until about the time of the 2nd amendment to the
…[7 more quoted lines elided]…
> adopted and adjusted it to become the new Standard.

OK, thanks.

Are you saying that the 74 standard was not issued by ANSI? I could have 
sworn that it was. I remember one of the IBM guys being very excited about 
it (maybe he had it wrong...)

Never mind. As you observed, I'm not really worried about it :-)

Pete.
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 10)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-10-03T11:00:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<be407487-cb04-4bf8-b11d-e4c7d5b5822d@g21g2000prn.googlegroups.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <RzXpo.222681$MG3.59308@en-nntp-16.dc1.easynews.com> <8gr6bqF620U1@mid.individual.net> <cp%po.214068$Bh.64528@en-nntp-12.dc1.easynews.com> <8grng2Fe2qU1@mid.individual.net> <Ng2qo.228039$pX3.12511@en-nntp-11.dc1.easynews.com> <8grtjpFkk3U1@mid.individual.net>`

```
On Oct 4, 6:42 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Bill Klein wrote:
> > Just to answer one part of this note
…[14 more quoted lines elided]…
> it (maybe he had it wrong...)

He didn't say that at all.

ANSI 'sub-contracted' the work on the standard to CODASYL. Or actually
ANSI adopted as a standard the CODASYL JOD for COBOL 1968 and COBOL
1973 (while not adopting 1969 and 1970).

In much the same way ISO 'sub-contracted' work on the standard to
ANSI.
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-10-04T22:09:40+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gtjupFq7oU1@mid.individual.net>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <RzXpo.222681$MG3.59308@en-nntp-16.dc1.easynews.com> <8gr6bqF620U1@mid.individual.net> <cp%po.214068$Bh.64528@en-nntp-12.dc1.easynews.com> <8grng2Fe2qU1@mid.individual.net> <Ng2qo.228039$pX3.12511@en-nntp-11.dc1.easynews.com> <8grtjpFkk3U1@mid.individual.net> <be407487-cb04-4bf8-b11d-e4c7d5b5822d@g21g2000prn.googlegroups.com>`

```
Richard wrote:
> On Oct 4, 6:42 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[25 more quoted lines elided]…
> ANSI.

OK, thanks.

Pete.
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 6)_

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2010-10-03T07:02:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cd1df37e-14c5-4949-b338-7b58ba42c567@f25g2000yqc.googlegroups.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com> <i88sji$hqu$1@news.eternal-september.org> <RzXpo.222681$MG3.59308@en-nntp-16.dc1.easynews.com> <8gr6bqF620U1@mid.individual.net>`

```

> > Of course, many (most?) vendors still support it, but it was removed
> > from the "official" language definition 8 years ago (with a warning
…[7 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."

No, I thought it was good for routing down first time processing then
amending the GO TO so that you didn't have to check switches all the
time.
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-10-04T12:52:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2e8ka6p6hfn8td8jsna7dnsq81cna1n9t3@4ax.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <wWDpo.213048$Bh.187055@en-nntp-12.dc1.easynews.com> <34idnSF6de3jFzrRnZ2dnUVZ5gSdnZ2d@giganews.com>`

```
On Sat, 02 Oct 2010 14:39:42 -0500, Arnold Trembley
<arnold.trembley@att.net> wrote:

>Our data naming conventions would discourage using MOVE CORRESPONDING. 
>The most I am considering doing is modifying the style-checker to issue 
>a warning message that a data name is not uniquely defined, just as a 
>suggestion.

I'm glad it's only discouraged.   The last time I used it, I had the
same copy statement twice.   Then I used a MOVE CORRESPONDING. 

I have seen it used recently for time/date moves as well.
```

#### ↳ Re: A COBOL conundrum

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2010-10-02T06:22:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<63516719-31e5-497a-9cb1-f43e4fc0805f@30g2000yqm.googlegroups.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com>`

```
Micro Focus NET Express 5.1 Personal Edition of Cobol happily compiles
without error. It does error when the Display is changed to show the
data item.
```

##### ↳ ↳ Re: A COBOL conundrum

- **From:** Arnold Trembley <arnold.trembley@att.net>
- **Date:** 2010-10-02T14:41:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34idnSB6de1xFzrRnZ2dnUVZ5gQAAAAA@giganews.com>`
- **In-Reply-To:** `<63516719-31e5-497a-9cb1-f43e4fc0805f@30g2000yqm.googlegroups.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <63516719-31e5-497a-9cb1-f43e4fc0805f@30g2000yqm.googlegroups.com>`

```
On 10/2/2010 8:22 AM, Alistair Maclean wrote:
> Micro Focus NET Express 5.1 Personal Edition of Cobol happily compiles
> without error. It does error when the Display is changed to show the
> data item.

Thanks very much!  This confirms what Bill Klein says about the COBOL 
standard.
```

#### ↳ Re: A COBOL conundrum

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2010-10-02T14:14:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i87eo3$9ij$1@news.eternal-september.org>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com>`

```
In article <rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com>, arnold.trembley@att.net wrote:
>I support a COBOL program that is used to read a COBOL source code file 
>and analyze it for compliance with company coding standards.  Last 
…[33 more quoted lines elided]…
>displays the output you would expect.

What happens if you change the initial value of the first definition of 
100-CUST-ACCT-EOF-SW from 'N' to 'Y', and then add this to the Procedure 
Division?

   IF 88-100-CUST-ACCT-NOT-EOF
      DISPLAY 'Account not at EOF'
   END-IF
   IF 88-100-CUST-ACCT-EOF
      DISPLAY 'Account at EOF'
   END-IF
   IF 88-100-TRAILER-FOUND
      DISPLAY 'Trailer found'
   END-IF
```

##### ↳ ↳ Re: A COBOL conundrum

- **From:** Arnold Trembley <arnold.trembley@att.net>
- **Date:** 2010-10-02T15:17:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GYedndEQr8juDjrRnZ2dnUVZ5vSdnZ2d@giganews.com>`
- **In-Reply-To:** `<i87eo3$9ij$1@news.eternal-september.org>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <i87eo3$9ij$1@news.eternal-september.org>`

```
On 10/2/2010 9:14 AM, Doug Miller wrote:
> In article<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com>, arnold.trembley@att.net wrote:
>> (snip)
…[13 more quoted lines elided]…
>     END-IF

Now that's an interesting suggestion!  Since I'm at home today, I tested 
this with the 1990 educational version of Realia COBOL for MS-DOS:

        IDENTIFICATION DIVISION.
        PROGRAM-ID.             HELLO6.
        ENVIRONMENT DIVISION.
        DATA DIVISION.
        WORKING-STORAGE SECTION.
        01  100-PROGRAM-FLAGS.
            05  100-CUST-ACCT-EOF-SW        PIC X(01)   VALUE 'Y'.
                88  88-100-CUST-ACCT-NOT-EOF            VALUE 'N'.
                88  88-100-CUST-ACCT-EOF                VALUE 'Y'.
            05  100-CUST-ACCT-EOF-SW        PIC X(01)   VALUE 'N'.
                88  88-100-TRAILER-FOUND                VALUE 'Y'.
                88  88-100-TRAILER-NOT-FOUND            VALUE 'N'.
        PROCEDURE DIVISION.
        0000-MAINLINE.
            DISPLAY 'HELLO WORLD'.
            IF 88-100-CUST-ACCT-NOT-EOF
                DISPLAY 'ACCOUNT NOT AT EOF'
            END-IF.
            IF 88-100-CUST-ACCT-EOF
                DISPLAY 'ACCOUNT AT EOF'
            END-IF.
            IF 88-100-TRAILER-FOUND
                DISPLAY 'TRAILER FOUND'
            END-IF.
            IF 88-100-TRAILER-NOT-FOUND
                DISPLAY 'TRAILER NOT FOUND'
            END-IF.

And this version compiled clean and gave the following results when 
executed:

HELLO WORLD
ACCOUNT AT EOF
TRAILER NOT FOUND

So, it appears that these two data items are different storage areas 
even if the 05 levels do not have unique names.  It seems to work as if 
both 05 levels were named FILLER.

Thanks very much!
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-10-03T12:15:33+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gpsomFhbmU1@mid.individual.net>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <i87eo3$9ij$1@news.eternal-september.org> <GYedndEQr8juDjrRnZ2dnUVZ5vSdnZ2d@giganews.com>`

```
Arnold Trembley wrote:
> On 10/2/2010 9:14 AM, Doug Miller wrote:
>> In article<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com>,
…[59 more quoted lines elided]…
> Thanks very much!
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-10-03T13:23:11+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gq0ngF54vU1@mid.individual.net>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <i87eo3$9ij$1@news.eternal-september.org> <GYedndEQr8juDjrRnZ2dnUVZ5vSdnZ2d@giganews.com>`

```

Oops! sorry about previous blank reply.

Comes from having the cursor in the "wrong" place and moving a notebook :-)

More below...

Arnold Trembley wrote:
> On 10/2/2010 9:14 AM, Doug Miller wrote:
>> In article<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com>,
…[57 more quoted lines elided]…
> if both 05 levels were named FILLER.

You mentioned earlier that the project leader had decided the flag fields 
should be fillers. I reckon this is the right solution.

I think the "conundrum" in all of this is not the behaviour of the COBOL 
compiler (which is exactly what I would have expected) but what to do about 
it.

About 35 years ago I encountered a similar situation and (as was usually my 
wont) decided to think about it and decide a course of action for my own 
personal code, for the future. As a contractor, one is bound by the 
installation standards but things can be learned and applied to one's own 
code.  And some sites welcome suggested improvements to standards (I have 
had to produce COBOL coding standards on several occasions during my career 
and was very pleased to note your attitude to same ("I don't want to tell 
any programmer they can't use a legal COBOL verb."). I have mentioned 
previously my attitude to sites that restrict the use of the language so as 
to implement the "lowest common denominator", instead of showing people how 
to use complex cnstructs without confusion. COBOL is simple enough; banning 
things like PERFORM...VARYING or insisting that negated conditions not be 
used, or rigidly applying ANY particular rule so that the programmer has no 
discretion, are all anathema to me and I would avoid working on sites with 
such a culture.

Anyway, coming back to the case in point, it seemed to me that 88 levels 
were a very good way to document certain states (there are equivalent 
constructs in most languages - the Boolean type in C# and other languages 
has the advantage that it can be set "true" or "false"; I believe Micro 
Focus allow this in COBOL as an extension, but it is not part of the COBOL 
'85 standard to set <condition-name> false), and yet, the use of 88 levels 
on some sites caused no end of problems.

It is very arguable whether they should be used at all and some people don't 
use them (for quite sound reasons). For myself, I decided they are useful 
but there needs to be a pattern that won't cause trouble.

I was working in different countries using different national languages 
(Spanish, German, and French) and occasionally, in a single country where 
code was going to be maintained at branches in other countries, where 
English was not the national language.

So, immediately, the question of "Y" or "YES" and "N" or "NO" presents 
itself. A COBOL programmer in Spain who is used to seeing "S" or "N", or a 
programmer in Germany who is used to seeing "J" or "N", will not be confused 
by "Y" or "N", but there is a kind of arrogance in insisting on the English 
form as a standard. What we are really seeking is "true" or "false".  In the 
interests of international respect and co-operation, because the language of 
mathematics knows no borders, and as a mark of respect to George Boole (one 
of my heroes), I opted to always use his representation of true or false 
from the 2 valued Algebra he postulated over a hundred years before 
computers were invented:  "1" = true; "0" false.

So the first change I would personally make would be:

        01  100-PROGRAM-FLAGS.
            05  100-CUST-ACCT-EOF-SW        PIC X(01)   VALUE '1'.
                88  88-100-CUST-ACCT-NOT-EOF            VALUE '0'.
                88  88-100-CUST-ACCT-EOF                VALUE '1'.
            05  100-CUST-ACCT-EOF-SW        PIC X(01)   VALUE '0'.
                88  88-100-TRAILER-FOUND                VALUE '1'.
                88  88-100-TRAILER-NOT-FOUND            VALUE '0'.

Of course, in reality it doesn't matter what these values are because we are 
never going to reference or use them. In the old days (before SET was added 
to the language), we HAD to specifically set a flag by moving a value to it.

MOVE '1' TO 100-CUST-ACCT-EOF-SW

... and immediately we have a problem, because 100-CUST-ACCT-EOF-SW  isn't 
(and , in this case, cannot be) qualified.

But nowadays we have no such constraint:

SET  88-100-TRAILER-NOT-FOUND TO TRUE

The problem is now for the compiler because it still can't qualify which 
instance of the flag we are trying to reference.

But hang on a minute... If we ONLY use SET, we NEVER need to reference the 
flag itself, so why give a name to it at all? Because we want to know what 
the condition or state we are checking for is? The 88 level tells us that. 
So there is no reason to name the flag itself at all. For 35 years now, in 
writing COBOL, I have always defined flags like this:

        01  100-PROGRAM-FLAGS.
            05  FILLER        PIC X   VALUE '1'.
                88  88-100-CUST-ACCT-NOT-EOF            VALUE '0'.
                88  88-100-CUST-ACCT-EOF                VALUE '1'.
            05  FILLER        PIC X   VALUE '0'.
                88  88-100-TRAILER-FOUND                VALUE '1'.
                88  88-100-TRAILER-NOT-FOUND            VALUE '0'.

Now, what about the initial value of the flag?

COBOL allows fillers to have a value so it isn't problematic, however, in 
the extended concept of a flag, as representing a state or condition, when 
the program starts, this condition is indeterminate. Someimes it is useful 
to know whether a flag was ever set (when debugging from a dump - less 
important with modern tools, but still a matter of principle...) so why not 
ALWAYS set the initial value to be "Don't know"?

        01  100-PROGRAM-FLAGS.
            05  FILLER        PIC X   VALUE SPACE.
                88  88-100-CUST-ACCT-NOT-EOF            VALUE '0'.
                88  88-100-CUST-ACCT-EOF                VALUE '1'.
            05  FILLER        PIC X   VALUE SPACE.
                88  88-100-TRAILER-FOUND                VALUE '1'.
                88  88-100-TRAILER-NOT-FOUND            VALUE '0'.

Use your INITIALIZATION code to explicitly set the desired initial 
conditions. If there is any kind of problem during initialization the 
program cannot progress as if a valid value was set in the flags. (This is 
particularly important in online processing where code may be reused...it 
makes sure programmers specifically and explicitly initialize each 
instance.)

SUMMARISING: (One man's opinion...):

1. Use FILLER to define flags and set their initial value to 
"indeterminate". This ensures that only EXPLICIT settings made in code can 
be valid.
2. ONLY use SET to set the flags. (If they are defined as fillers, that is 
almost the only way you CAN reference them - but there is still refmodding 
on the group level or an inadvertent group move.)
3. Use Boolean values to signify TRUE and FALSE. ( It cannot be confused, 
but mainly, it is just respect... to other cultures and to good old George 
Boole without whom, probably, none of us would be enjoying the careers we 
have. :-)

In other words, I completely endorse your lead's solution and your own 
attitude towards programming standards. :-)

Pete.
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

_(reply depth: 4)_

- **From:** Arnold Trembley <arnold.trembley@att.net>
- **Date:** 2010-10-03T03:11:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IIadnRZrH-o0pzXRnZ2dnUVZ5s-dnZ2d@giganews.com>`
- **In-Reply-To:** `<8gq0ngF54vU1@mid.individual.net>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <i87eo3$9ij$1@news.eternal-september.org> <GYedndEQr8juDjrRnZ2dnUVZ5vSdnZ2d@giganews.com> <8gq0ngF54vU1@mid.individual.net>`

```
On 10/2/2010 7:23 PM, Pete Dashwood wrote:
> (snip)
>
…[16 more quoted lines elided]…
> Pete.

That's certainly a well-reasoned approach.  The only thing I might add 
is that putting all flags at the 05 level in a single 01 record would 
make it very easy to check for refmodding the group level or an 
inadvertent group move.  IBM Enterprise COBOL allows FILLER as the 01 
record name, but I'm not sure if that's an IBM extension to the standard.

The hope is that coding style standards will encourage best practices, 
or at least encourage consistent practices that work reliably.

Kind regards,
```

#### ↳ Re: A COBOL conundrum

- **From:** Richard Luketich <rluketich@rlyxx.com>
- **Date:** 2010-10-02T23:58:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v03ga6l3i8h14nq33vm10ths36beo8447t@4ax.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com>`

```
Just a comment on adding the duplicate name warnin to your source code
checker. If you have two 01-levels with subordinate names that are the
same, the subordinate names are not truly duplicates. COBOL allows for
qualification that makes them unique using OF or IN. For example:

        01  100-PROGRAM-FLAGS-A.
            05  100-CUST-ACCT-EOF-SW        PIC X(01)   VALUE 'N'.
                88  88-100-CUST-ACCT-NOT-EOF            VALUE 'N'.
                88  88-100-CUST-ACCT-EOF                VALUE 'Y'.
        01  100-PROGRAM-FLAGS-B
            05  100-CUST-ACCT-EOF-SW        PIC X(01)   VALUE 'N'.
                88  88-100-TRAILER-FOUND                VALUE 'Y'.
                88  88-100-TRAILER-NOT-FOUND            VALUE 'N'.

The names 100-CUST-ACCT-EOF-SW OF 100-PROGRAM-FLAGS-A and
100-CUST-ACCT-EOF-SW OF 100-PROGRAM-FLAGS-B are unique names. If you
were to reference 100-CUST-ACCT-EOF-SW without the OF clause, you'll
get a qualification error, not a duplicate names error.

RL


On Sat, 02 Oct 2010 03:29:17 -0500, Arnold Trembley
<arnold.trembley@att.net> wrote:

>I support a COBOL program that is used to read a COBOL source code file 
>and analyze it for compliance with company coding standards.  Last 
…[48 more quoted lines elided]…
>execute in other COBOL compilers.
```

##### ↳ ↳ Re: A COBOL conundrum

- **From:** Arnold Trembley <arnold.trembley@att.net>
- **Date:** 2010-10-03T02:50:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3uGdneyaPZNHqDXRnZ2dnUVZ5oOdnZ2d@giganews.com>`
- **In-Reply-To:** `<v03ga6l3i8h14nq33vm10ths36beo8447t@4ax.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <v03ga6l3i8h14nq33vm10ths36beo8447t@4ax.com>`

```
On 10/2/2010 11:58 PM, Richard Luketich wrote:
> Just a comment on adding the duplicate name warnin to your source code
> checker. If you have two 01-levels with subordinate names that are the
…[17 more quoted lines elided]…
> RL

That's another very good reason to be careful about warning for 
duplicate data names.  In order to distinguish between the original 
example and your example above the style-checker program needs to know 
if the duplicate names are in the same group item or different group 
items.  That's a much more complex edit to determine if a duplicate data 
name can or cannot be qualified.

Kind regards,
```

###### ↳ ↳ ↳ Re: A COBOL conundrum

- **From:** Richard Luketich <rluketich@rlyxx.com>
- **Date:** 2010-10-12T06:06:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t3g8b6p233rvpib5s35mg554qkgmla0eal@4ax.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <v03ga6l3i8h14nq33vm10ths36beo8447t@4ax.com> <3uGdneyaPZNHqDXRnZ2dnUVZ5oOdnZ2d@giganews.com>`

```
Well, the check is much simpler if the site standard is that all names
must be unique without qualification. If qualification is allowed,
then the checker needs to use complete tree structures to qualify each
name. For that matter, the compiler will reject any true duplicates.

RL

On Sun, 03 Oct 2010 02:50:48 -0500, Arnold Trembley
<arnold.trembley@att.net> wrote:

>On 10/2/2010 11:58 PM, Richard Luketich wrote:
>> Just a comment on adding the duplicate name warnin to your source code
…[27 more quoted lines elided]…
>Kind regards,
```

#### ↳ Re: A COBOL conundrum

- **From:** "Bruce M. Axtens" <bruce.axtens@gmail.com>
- **Date:** 2010-10-03T20:59:46+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a7%po.921$hz6.843@viwinnwfe02.internal.bigpond.com>`
- **In-Reply-To:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com>`

```
Just to let you know that OpenCOBOL 1.1 is working in the canonical way.

First using your version, saved as hello6.cob
bruce@bruce-laptop:~/Desktop/Projects$ cobc -x hello6.cob
bruce@bruce-laptop:~/Desktop/Projects$ ./hello6
HELLO WORLD
TRAILER NOT FOUND

Then your second version, following Doug Miller's suggestion
bruce@bruce-laptop:~/Desktop/Projects$ cobc -x hello6b.cob
bruce@bruce-laptop:~/Desktop/Projects$ ./hello6b
HELLO WORLD
ACCOUNT AT EOF
TRAILER NOT FOUND

For completeness, I edited the original hello6 to see how OC handles the 
ambiguity issue
bruce@bruce-laptop:~/Desktop/Projects$ cobc -x hello6.cob
hello6.cob: In paragraph '0000-MAINLINE':
hello6.cob:17: Error: '100-CUST-ACCT-EOF-SW' ambiguous; need qualification
hello6.cob:8: Error: '100-CUST-ACCT-EOF-SW' in '100-PROGRAM-FLAGS' 
defined here
hello6.cob:11: Error: '100-CUST-ACCT-EOF-SW' in '100-PROGRAM-FLAGS' 
defined here

Kind regards,
Bruce.
```

##### ↳ ↳ Re: A COBOL conundrum

- **From:** Arnold Trembley <arnold.trembley@att.net>
- **Date:** 2010-10-03T12:13:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FYWdnS0FJ8UwJDXRnZ2dnUVZ5vOdnZ2d@giganews.com>`
- **In-Reply-To:** `<a7%po.921$hz6.843@viwinnwfe02.internal.bigpond.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <a7%po.921$hz6.843@viwinnwfe02.internal.bigpond.com>`

```
On 10/3/2010 7:59 AM, Bruce M. Axtens wrote:
> Just to let you know that OpenCOBOL 1.1 is working in the canonical way.
>
…[24 more quoted lines elided]…
> Bruce.

Thanks very much!

I have looked at the website:
http://www.opencobol.org/

There's lots of good information there, including Bill Klein's notes on 
installing OpenCOBOL in Windows.
```

#### ↳ Re: A COBOL conundrum

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-10-04T12:48:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i98ka6dqh3jrfluof9eurtm21erb9aj1d4@4ax.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com>`

```
On Sat, 02 Oct 2010 03:29:17 -0500, Arnold Trembley
<arnold.trembley@att.net> wrote:

>I am very curious to know if this sample program will compile and 
>execute in other COBOL compilers.

Move Corresponding depends upon this behavior.   I can't imagine that
there are compilers which would not accept that code.
```

##### ↳ ↳ Re: A COBOL conundrum

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-10-04T13:53:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Wopqo.259762$Yn5.204024@en-nntp-14.dc1.easynews.com>`
- **References:** `<rMGdnWBe6MzAcDvRnZ2dnUVZ5oydnZ2d@giganews.com> <i98ka6dqh3jrfluof9eurtm21erb9aj1d4@4ax.com>`

```
Howard,
   Unless the version that you checked was different from what I originally 
saw, "MOVE CORR" would fail miserably with the code provided.

It had identically named 01-levels.

MOVE CORR only works with code where two group items (doesn't have to be 
01-level) have DIFFERENT names, but the subordinate names are identical.

The original code in this thread had identically named  items that could NOT 
be qualified to be made unique.

As I indicated, ever since '85, this has been valid (standard conforming) 
code as long as you do NOT reference the items anywhere else in the code.

"Howard Brazee" <howard@brazee.net> wrote in message 
news:i98ka6dqh3jrfluof9eurtm21erb9aj1d4@4ax.com...
> On Sat, 02 Oct 2010 03:29:17 -0500, Arnold Trembley
> <arnold.trembley@att.net> wrote:
…[12 more quoted lines elided]…
> - James Madison
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
