[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# stacked IF terminology?

_43 messages · 15 participants · 2002-10 → 2002-11_

---

### stacked IF terminology?

- **From:** Edward Reid <edwardreid@spamcop.net>
- **Date:** 2002-10-30T14:59:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com>`

```
What (if anything) do you call the following sort of structure?

IF COND-1
  PERFORM PERF-1
ELSE
IF COND-2
  PERFORM PERF-2
ELSE
IF COND-3
  PERFORM PERF-3

etc. Doesnt matter whether it's C74 or C85, though in the latter you'd 
probably use EVALUATE instead, nor whether the scope terminator is 
used. 

The point is that the logical program structure is sequential 
selection, and so it's formatted as such rather than as nested. 
Technically it's characterized (approximately) by the lack of 
conditional statements between IF and the matching ELSE. The formatting 
also reflects the fact that sequential selection constructs sometimes 
become very long (without much loss of readability), and treating the 
ELSE IF as nested would be difficult to read.

I've been calling this a "stacked IF", but a search of the web and 
Usenet shows that no one else is using this terminology, at least not 
in public.  I contrast it with "nested IF", which is IF with nesting 
used for purposes other than sequential selection -- one alternation 
within another.

For those who say "it's all nested", my point is that whatever the 
compiler thinks, the *programmer* is using the language construct for 
different purposes, and that this is supported by the fact that in a 
C74->C85 conversion we would usually change a "stacked IF" to EVALUATE. 
Also, many programming languages support a true "IF ELSEIF ELSE" flow; 
the syntactic nesting of a "stacked IF" would disappear with such a 
construct.

Thanks,

Edward Reid
```

#### ↳ Re: stacked IF terminology?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-10-30T14:07:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<appeds$hu9$1@slb5.atl.mindspring.net>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com>`

```
I am afraid that (IMHO) this is a "nested IF" statement - no matter what you
think it might be.  Furthermore, in "maintenance" someone can add code after
one of the PERFORMs and that would hide what you think you are doing.

The EVALUATE statement is (traditionally) called a CASE structure.  What you
are doing here is trying to "simulate" a CASE structure using the
*RESTRICTED* syntax of pre'85 Standard COBOL where no native support was
provided.

It might help me to understand your question better if you showed us what
you think is a "nested IF statement" without being a "stacked IF" statement.

It seems to me that ANY time you have an IF statement "embedded" in either
the IF branch or the ELSE branch, you have a "nested IF" and there is really
no way to distinguish between them.
```

##### ↳ ↳ Re: stacked IF terminology?

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-10-30T21:34:54
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dc04f92_3@Usenet.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net>`

```
Comments below, Bill.

William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
news:appeds$hu9$1@slb5.atl.mindspring.net...
> I am afraid that (IMHO) this is a "nested IF" statement - no matter what
you
> think it might be.  Furthermore, in "maintenance" someone can add code
after
> one of the PERFORMs and that would hide what you think you are doing.
>
> The EVALUATE statement is (traditionally) called a CASE structure.  What
you
> are doing here is trying to "simulate" a CASE structure using the
> *RESTRICTED* syntax of pre'85 Standard COBOL where no native support was
…[3 more quoted lines elided]…
> you think is a "nested IF statement" without being a "stacked IF"
statement.
>
> It seems to me that ANY time you have an IF statement "embedded" in either
> the IF branch or the ELSE branch, you have a "nested IF" and there is
really
> no way to distinguish between them.
>
Well, that is certainly ONE definition of a Nested IF...

I have a different one.

For me an IF is "nested"  CORRECTLY when nesting occurs in the TRUE Branch
only.

My reasoning here is that it represents a decision tree.

IF  NOT red light
      IF NOT amber light
           IF NOT green light
                Perform Lights-not-operating
           ELSE
                  Perform GO-for-it
           END-IF
      ELSE
              Perform Prepare-to-stop
      END-IF
ELSE
       Perform STOP-right-now
END-IF

If cond-1 and cond-2 and cond-3 are ALL true  do action 1
If cond-1 and cond-2 are true, but cond-3 is NOT true, do action 2
If cond-1 is true and cond-2 is NOT true, do action 3
If cond-1 is not true do action-4

This method of nesting IFs is the way I learned from Fritz D. MacCameron
PhD., sometime COBOL lecturer at Louisiana State University, in 1969, as
described in his book: "COBOL Logic and Programming" Now, sadly, long out of
print.
(I believe this is the best book on COBOL Language that was ever written and
I have read and reviewed dozens of them...)

This is such a simple and elegant use of nested IF that I have taught it to
numerous students.

In the old days (before standards evolved) we used to suffer from people
nesting IFs every which way in true and false branches and it was a
nightmare. I saw a program once with PAGES (green lineflo) of a single IF
statement.

Imposing the above discipline did us no harm at all.

So, for my money...

A CORRECTLY (or "desirably" if you like...<G>) Nested IF would be as above.

(This is the ONLY usage that I would refer to as a "Nested IF"; reason
being, I would NEVER write the alternative "ugly" form...<G>)

An INCORRECTLY (or "ugly" if you like <G>) Nested IF would use both the true
and false branches and would probably have statements after the IF  like...

IF NOT red-light
     perform no-need-to-stop
     IF NOT amber-light
         perform step-on-it
         perform oops-lights-not-working-maybe
     else
         IF lights-not-working
              ....
and so on ...

Although this may technically qualify as a "Nested IF", to me it is ugly and
I wouldn't use it.

Having disposed of what is and is not a "properly" Nested IF, I believe
Edward's nomenclature of a "Stacked IF" is appropriate and apposite. <G>

Pete.





 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

- **From:** Edward Reid <edwardreid@spamcop.net>
- **Date:** 2002-10-31T00:06:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01HW.B9E62471001A347516E86E00@news-east.usenetserver.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com>`

```
On Wed, 30 Oct 2002 16:34:54 -0500, Peter E. C. Dashwood wrote
> Having disposed of what is and is not a "properly" Nested IF, I believe
> Edward's nomenclature of a "Stacked IF" is appropriate and apposite. <G>

Thanks, Pete. Since you said what I wanted to hear, I'll take your 
advice and retain this nomenclature ;-).

> EVALUATE is obviously preferable

Yes, I should have clarified the context. I'm primarily concerned with 
explaining COBOL85 constructs and good COBOL85 style to experienced 
COBOL74 programmers.

> An INCORRECTLY (or "ugly" if you like <G>) Nested IF would use both the true
> and false branches and would probably have statements after the IF  like...

So you're saying *never* nest the ELSE part? I very much see the point 
about the additional statements. I often preach about flattening, about 
deciding on the situation and then doing all the actions, rather then 
putting some actions in common logic, as in a decision table (and I'm 
often surprised at which COBOL programmers are familiar with decision 
tables). I like the simplicity of the resulting logic. But I don't 
immediately see how I can eliminate the ELSE nesting in something like

  IF CALIFORNIA
    IF VEGETARIAN
      PERFORM SERVE-RADICCHIO
    ELSE
      PERFORM SERVE-SALMON
    END-IF
  ELSE
    IF VEGETARIAN
      PERFORM SERVE-ICEBERG-LETTUCE
    ELSE
      PERFORM SERVE-MEAT-AND-POTATOES
    END-IF
  END-IF

Now it's true that in this case I would prefer to use an EVALUTE with 
two subjects, or to use both conditions in each IF as a sequential 
selection (stacked IF):

  IF CALIFORNIA AND VEGETARIAN
    PERFORM SERVE-RADICCHIO
  ELSE
  IF CALIFORNIA AND NOT VEGETARIAN
    PERFORM SERVE-SALMON

etc. If you're saying always avoid nesting in the ELSE, how does it 
work in general? Of course it's convenient that you already said the 
book is out of print, so naturally I have to ask you instead of looking 
it up.

On Wed, 30 Oct 2002 15:07:02 -0500, William M. Klein wrote
> It might help me to understand your question better if you showed us what
> you think is a "nested IF statement" without being a "stacked IF" statement.

Yes, I should do that. The full example above is nested. There is 
definitely some overlap; consider

  IF CALIFORNICATE
    IF VEGETARIAN
      PERFORM SERVE-RADICCHIO
    ELSE
      PERFORM SERVE-SALMON
    END-IF
  ELSE
  IF FLORIDA
    PERFORM SERVE-COLLARDS-IN-BACON
  ELSE
  IF MINNESOTA
    PERFORM SERVE-VENISON
  ELSE
    IF VEGETARIAN
      PERFORM SERVE-ICEBERG-LETTUCE
    ELSE
      PERFORM SERVE-MEAT-AND-POTATOES
    END-IF
  END-IF

I would call this a stacked IF (the tests on CALIFORNICATE/ FLORIDA/  
MINNESOTA/ other) with two other IFs nested. But it could very easily 
be converted to purely stacked form. Furthermore, though I can see it, 
identifying it automatically is difficult.

My experience is that a "continued IF" (analogous to a continued 
fraction), of the form IF ELSE IF ELSE IF etc, with never an IF IF, is 
virtually always a sequential selection (stacked IF). In fact, in a 
conversion and renovation project we identfied stacked IFs with this 
simple algorithm and formatted them as such, with excellent results. 
(And converted many of them to EVALUATE, which was easier because they 
had already been formatted in stacked style.)

However, this simple algorithm does not completely handle cases such as 
the above. I'm not concerned about the lack of a totally unambiguous 
definition. What's important here is what the programmer writing or 
reading the code is thinking, and it's possible to come out with the 
same code (sequence of COBOL words) from either a sequential or a 
nested mental model.

Again: the issue of stacked vs nested is a question of how the 
programmer is using the language, not of language syntax itself.

> I am afraid that (IMHO) this is a "nested IF" statement - no matter what you
> think it might be. 

Syntactically, yes, of course. And that's because COBOL74 didn't have a 
construct for sequential selection. I would expect a programmer writing 
COBOL85 to use EVALUATE for sequential selection. As mentioned, I'm 
concerned with programmers moving from C74 to C85; I want to clarify 
for them the ways they use C74, so that they can map their experience 
into C85.

> Furthermore, in "maintenance" someone can add code after
> one of the PERFORMs and that would hide what you think you are doing.

True. That's a good reason to format the C74 code appropriately, or to 
use EVALUATE instead in C85.

> The EVALUATE statement is (traditionally) called a CASE structure.

Partly. Well, "case" has been used to mean various things. Sometimes it 
is strict alternation (exclusive selection) based on an integer. Other 
times, as with EVALUATE, it's sequential selection (non-exclusive 
conditions). And everything in between.

That's one reason I want to map EVALUATE to what programmers have done 
in C74. I want them to use the power of EVALUATE, not just use WHEN 1, 
WHEN 2, WHEN 3 etc.

> What you
> are doing here is trying to "simulate" a CASE structure using the
> *RESTRICTED* syntax of pre'85 Standard COBOL where no native support was
> provided.

Right. As mentioned above, I initially failed to point out my context. 
I don't want C85 programmers to use this style; I want to train them to 
recognize it so they know when to use EVALUATE instead.

> It seems to me that ANY time you have an IF statement "embedded" in either
> the IF branch or the ELSE branch, you have a "nested IF" and there is really
> no way to distinguish between them.

Again, this is the difference between the syntax of the language and 
the psychology of the programmer writing or reading the program (and 
primarily the latter given what we know about the ratio of times read 
to times written). Because of what COBOL (especially pre-85) lacks, 
these diverge more than in some other programming languages, but 
hopefully we can train programmers so that the divergence is less in 
C85 than in C74. Of course, matching the mental and syntax models 
exactly is a holy grail which language designers have long sought in 
vain.

I'm trying to clarify programmers' thoughts so that I can better train 
them to make those thoughts clear in written COBOL.

Thanks for the thoughts.

Edward
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-11-01T00:48:08
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dc1ccdb_6@Usenet.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <01HW.B9E62471001A347516E86E00@news-east.usenetserver.com>`

```
Comments interspersed below, Edward...

Pete.

Edward Reid <edwardreid@spamcop.net> wrote in message
news:01HW.B9E62471001A347516E86E00@news-east.usenetserver.com...
>
<snip>
> > An INCORRECTLY (or "ugly" if you like <G>) Nested IF would use both the
true
> > and false branches and would probably have statements after the IF
like...
>
> So you're saying *never* nest the ELSE part?

No, I'm saying it is ugly to do so, and I'm saying I wouldn't do it from
preference.(Actually, I feel strongly enough about it that I would never do
it, but I have no problem with what other people do, and it would be against
my own principle of encouraging freedom of choice for me to say that no-one
else should do it...<G>)

> I very much see the point
> about the additional statements. I often preach about flattening, about
…[19 more quoted lines elided]…
>
While the above is OK, it suffers from testing the same thing twice, and if
you need to add more conditions it becomes messy...

Given that EVALUATE is not an option, why not:

move zero to truth-value
if CALIFORNIAN
   add 1 to truth-value
end-if
if VEGETARIAN
    add 2 to truth-value
end-if
*> if you don't mind using GO TO, you could now add 1 to truth-value and
*> code a GO TO...DEPENDING ON truth-value here...
*> (Each branch could be to a PERFORM statement if you need to maintain
control flow.)
*> if you prefer not to use GO TO, then the following will do the job...
if NOT truth-value = zero
   if NOT truth-value = 1
      if NOT truth-value = 2
         if NOT truth-value = 3
            perform internal-logic-error
         else
             *> CALIFORNIAN AND VEGETARIAN
             perform serve-raddichio
         end-if
      else
          *>  NOT CALIFORNIAN AND VEGETARIAN
          peform serve-iceberg-lettuce
      end-if
   else
       *> CALIFORNIAN AND NOT VEGETARIAN
       perform serve-salmon
   end-if
else
    *>  NOT (CALIFORNIAN OR VEGETARIAN)
    perform serve-meat-and-potatoes
end-if

This is a typical case of converting a redundant Boolean expression into a
truth value and using the value to decide what is happening. It is a simple
matter to extend the truth table by adding another condition which would
cause 4 to be added to the truth value, another condition again would add 8
to the truth value, and so on.... in this way every possible combination of
the  (in this example, 4...) conditions is covered, and yet each condition
is tested only once.

Storing compound conditions as a truth value is useful because the truth
value can be checked at various places in the program even if the actual
conditions are no longer obtainable ("remembered" conditions). However, it
is important to document them as shown above...

Obviously, EVALUATE is more elegant.

> Now it's true that in this case I would prefer to use an EVALUTE with
> two subjects, or to use both conditions in each IF as a sequential
…[7 more quoted lines elided]…
>

This is fine for two conditions. I agree that this is technically a nested
IF but, for myself I don't consider it as such. I prefer your label of
"stacked IF".

I still don't like the redundant test on CALIFORNIA and would be unlikely to
code it myself, for this reason.

> etc. If you're saying always avoid nesting in the ELSE, how does it
> work in general? Of course it's convenient that you already said the
> book is out of print, so naturally I have to ask you instead of looking
> it up.
>
On the contrary, it is extremely inconvenient that the book is out of print
<G> I would LOVE to get my hands on a copy of it...

To answer your question, it works that you only nest IFs in the true branch
so that a nested IF is only required to implement a decision tree. I showed
it in the last post. (I learned the technique from the good Doctor McCracken
and it has served me long and well. I have passed it on to at least 50 other
COBOL programmers and God knows how many people reading this will decide it
is not a bad way to deal with nested IFs...but I really don't mind whether
they adopt it or not.)

Please be aware Edward that I am NOT saying "always avoid nesting in the
ELSE". What I am saying is that I personally always avoid nesting in the
ELSE. I really don't mind what other people do. I have maintained COBOL code
all my life; some of it was easy, some of it was difficult, some of it was
what I considered good style and some of it wasn't, but, in the final
analysis, if you call yourself a programmer, you should be able to program
in the language, and have enough understanding of it to deal with how others
use it.

There is no universal COBOL programming standard. There cannot be and
shouldn't be. Implementing local standards for a given shop is one thing,
doing it for the World is quite another...

In forums like this we can discuss alternative styles but it amuses me to
see how evangelical these discussions quickly become. (Like it really
MATTERS, or the fate of the World depends on it...said it before; I say it
again: "It is only computer programming, not life and death...")



> On Wed, 30 Oct 2002 15:07:02 -0500, William M. Klein wrote
> > It might help me to understand your question better if you showed us
what
> > you think is a "nested IF statement" without being a "stacked IF"
statement.
>
> Yes, I should do that. The full example above is nested. There is
…[45 more quoted lines elided]…
> > I am afraid that (IMHO) this is a "nested IF" statement - no matter what
you
> > think it might be.
>
…[33 more quoted lines elided]…
> > It seems to me that ANY time you have an IF statement "embedded" in
either
> > the IF branch or the ELSE branch, you have a "nested IF" and there is
really
> > no way to distinguish between them.
>
…[12 more quoted lines elided]…
>

That is a very worthwhile objective and I endorse it. The danger is that
style can stifle as well as stimulate...

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 5)_

- **From:** Edward Reid <edwardreid@spamcop.net>
- **Date:** 2002-10-31T22:00:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01HW.B9E75881001063051710ECE0@news-east.usenetserver.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <01HW.B9E62471001A347516E86E00@news-east.usenetserver.com> <3dc1ccdb_6@Usenet.com>`

```
On Thu, 31 Oct 2002 19:48:08 -0500, Peter E. C. Dashwood wrote
> On the contrary, it is extremely inconvenient that the book is out of print
> <G> I would LOVE to get my hands on a copy of it...

Well, the web seems to think that Fritz MacCameron is not around ...

> To answer your question, it works that you only nest IFs in the true branch
> so that a nested IF is only required to implement a decision tree. 

OK, I see. Seems like a rather formal technique. But I won't disagree 
much, since you like my terminology ;-). Anyway, we seem to agree that 
there are better ways to do this. If I need more than a couple of 
conditions, and I really cannot co-opt the situation by slicing off 
obvious cases to reduce it to simpler terms, then I'll make the 
decision table explicit -- code the rules in WS, compute the truth 
values as fields in a record, and search the rules for a match on the 
truth value. It's an indication of how rarely this much complexity 
occurs in practice that I've actually done this only about two or three 
times in 30 years. (I've far more often used a decision table to 
clarify a situation, and realized in the process that I could find a 
short cut.)

> (I learned the technique from the good Doctor McCracken

Ah, Dan'l. He's still around. His Fortran book was my introduction to 
computing in the summer of 1966. Interesting man. Hiker. (Aside: so was 
Nobel physicist Glenn Seaborg, who died recently. Seaborg's son Eric 
was one of those responsible for developing the American Discovery 
Trail.) His brother, who died only a few weeks ago, was a top expert on 
solar energy.

> in the final
> analysis, if you call yourself a programmer, you should be able to program
> in the language, and have enough understanding of it to deal with how others
> use it.

Absolutely. And retain the style (if it's perceptible and consistent) 
while modifying the program.

> "It is only computer programming, not life and death..."

Huh?

Edward
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 6)_

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2002-11-01T08:53:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0211010853.3c00841@posting.google.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <01HW.B9E62471001A347516E86E00@news-east.usenetserver.com> <3dc1ccdb_6@Usenet.com> <01HW.B9E75881001063051710ECE0@news-east.usenetserver.com>`

```
Oh Dear!

Only when I read your response did I realise my mistake...

It was Dr. MacCAMERON NOT Dr. McCRACKEN... (I wasn't impressed with
McCracken's COBOL text... although adequate, it was dry and
dispassionate. MacCameron's text is vital and energised.)

Sorry, I slipped up there...

Pete.


Edward Reid <edwardreid@spamcop.net> wrote in message news:<01HW.B9E75881001063051710ECE0@news-east.usenetserver.com>...
> On Thu, 31 Oct 2002 19:48:08 -0500, Peter E. C. Dashwood wrote
> > On the contrary, it is extremely inconvenient that the book is out of print
…[41 more quoted lines elided]…
> Edward
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-10-31T12:12:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0210311212.3dd7a44e@posting.google.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com>`

```
"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote

> For me an IF is "nested"  CORRECTLY when nesting occurs in the TRUE Branch
> only.
…[15 more quoted lines elided]…
> END-IF

In this particular case [!] it would be better, in terms of actual
decision making to have:

   IF ( Red-Light = "ON" )
       PERFORM STOP-right-now
   ELSE
   IF ( Amber-Light = "ON" )
       PERFORM Prepare-to-Stop
   ELSE
   IF ( Green-Light = "ON" )
        ...
   ELSE

simply on the basis that the most important decision is made earliest.
 
> If cond-1 and cond-2 and cond-3 are ALL true  do action 1
> If cond-1 and cond-2 are true, but cond-3 is NOT true, do action 2
> If cond-1 is true and cond-2 is NOT true, do action 3
> If cond-1 is not true do action-4

I suspect that this is more complex than what is actually required. 
However neither your or my code copes correctly with british traffic
lights where it goes from red to red+amber before green.

In my case it can be prepended as:

   IF ( Red-Light = "ON" AND Amber-Light = "ON" )
       PERFORM Stop-Prepare-to-go
   ELSE
   .... 

Some failure conditions are also catered for differently.  If all
lights are on, or red+green, then yours would GO and mine would STOP
(or prepare to go).
For New Zealand, of course, it should be amended to:

   IF ( Amber-Light = "ON" )
       PERFORM Accelerate-hard
   ELSE

and possibly:

    IF ( Red-Light = "ON" )
        IF ( Time-since-change < 3 )
            PERFORM Full-Acceleration
        ELSE
            PERFORM Stop-and-curse
        END-IF
    END-IF
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-11-01T00:22:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ePjw9.3577$mN6.986628@newssrv26.news.prodigy.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0210311212.3dd7a44e@posting.google.com...
> However neither your or my code copes correctly with british traffic
> lights where it goes from red to red+amber before green.

We have the same thing - "green light coming soon"  - here in the States.

Except we only have it at the dragstrip.

MCM
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 5)_

- **From:** "Russell Styles" <RWSTYLES@worldnet.att.net>
- **Date:** 2002-11-01T07:46:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1jqw9.19338$VJ5.1075204@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <ePjw9.3577$mN6.986628@newssrv26.news.prodigy.com>`

```

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:ePjw9.3577$mN6.986628@newssrv26.news.prodigy.com...
> "Richard" <riplin@Azonic.co.nz> wrote in message
> news:217e491a.0210311212.3dd7a44e@posting.google.com...
…[9 more quoted lines elided]…
>

    That sounds suicidal.   Around here (Atlanta), anyone that
dares cross an intersection in the first 3 or 4 seconds of green
isn't likely to live long.  The red + amber would seem to encourage
people to be quick off the line when it turns green.
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 6)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-11-01T14:00:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pOvw9.3676$mN6.1056355@newssrv26.news.prodigy.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <ePjw9.3577$mN6.986628@newssrv26.news.prodigy.com> <1jqw9.19338$VJ5.1075204@bgtnsc05-news.ops.worldnet.att.net>`

```
"Russell Styles" <RWSTYLES@worldnet.att.net> wrote in message
news:1jqw9.19338$VJ5.1075204@bgtnsc05-news.ops.worldnet.att.net...
>
> > > However neither your or my code copes correctly with british traffic
> > > lights where it goes from red to red+amber before green.
> >
> > We have the same thing - "green light coming soon"  - here in the
States.
> >
> > Except we only have it at the dragstrip.
…[3 more quoted lines elided]…
> isn't likely to live long.

That's why we only have it the dragstrip.

But that does remind me of when I moved back to Wisconsin from Illinois a
few years ago.  The behavior of drivers when the light is yellow is subtly
different on the two sides of the Cheddar Curtain... in Illinois, drivers
don't "jackrabbit" off the line because people seem to interpret a yellow
light as a "step on it" instruction... in Wisconsin, drivers *do*
"jackrabbit" because the yellow is more often interpreted as "stop now."

Took a little getting used to...

MCM
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 4)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2002-11-01T00:22:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xPjw9.38878$Mb3.1736975@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com>`

```

Richard <riplin@Azonic.co.nz> wrote in message news:217e491a.0210311212.3dd7a44e@posting.google.com...

> However neither your or my code copes correctly with british traffic
> lights where it goes from red to red+amber before green.

I vaguely remember that a fairly extensive British survey concluded
that the majority of Britons, or perhaps just a very large segment of the populace,
could not recite the correct display sequence from memory.

IIRC, Red - Amber - Green - Amber - Red was the most popular choice.

I wouldn't be surprised if that conclusion turned out to be still true today.
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 4)_

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2002-11-01T08:41:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0211010841.4abbe41d@posting.google.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com>`

```
Hahaha!

Thanks Richard. I had a ï¿½5 bet with a colleague (I am currently in the
U.K.) that SOMEONE would respond to my post with the fact that it
didn't cover British traffic light sequences...<G>

I'll drink a Jack Daniels to you with the proceeds.

Pete


riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0210311212.3dd7a44e@posting.google.com>...
> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote
> 
…[67 more quoted lines elided]…
>     END-IF
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 5)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2002-11-03T06:31:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021103013108.24388.00002717@mb-mw.aol.com>`
- **References:** `<b3638c46.0211010841.4abbe41d@posting.google.com>`

```
>From: dashwood@enternet.co.nz  (Peter E. C. Dashwood)
>Date: 11/1/02 11:41 AM Eastern Standard Time

>Hahaha!
>
…[6 more quoted lines elided]…
>Pete

Doesn't cover the blinking red before green we have in some areas either :)

Not to be confused with the blinking red of a traffic light either 'off' for
the evening or at an intersection where there is no full traffic light.  These
are found usually on left turn lights meaning - ok to turn if you have
clearence before you get the full right of way of a green light.
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-11-03T12:17:18-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0211031217.616bcd93@posting.google.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <b3638c46.0211010841.4abbe41d@posting.google.com>`

```
dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote

> Thanks Richard. I had a #5 bet with a colleague (I am currently in
> the U.K.) that SOMEONE would respond to my post with the fact that
> it didn't cover British traffic light sequences...<G>

I had hoped that you would respond with an explanation about how
your mechanism would have usefully dealt with the situations not
covered.

> > If cond-1 and cond-2 and cond-3 are ALL true  do action 1
> > If cond-1 and cond-2 are true, but cond-3 is NOT true, do action 2
> > If cond-1 is true and cond-2 is NOT true, do action 3
> > If cond-1 is not true do action-4

While this is 'exhaustive' for 4 states, there are in fact 8
possible (some less probable) states (plus some flashing and
alternating).

> > For me an IF is "nested"  CORRECTLY when nesting occurs in
> > the TRUE Branch only.
> > My reasoning here is that it represents a decision tree.

Trees have branches on both sides. You have artificially cut off
one side.

The 'obvious' place to put the red+amber test would be after
the ELSE before Prepare-to-stop.

> > ELSE
        IF amber light
            PERFORM Prepare-to-go
        ELSE
> >         Perform Prepare-to-stop
        END-IF
> > END-IF

This, however, would be contrary to your 'nesting only in the
true branch'.

Alternately a test for red+amber could be prepended to the code
but then the whole of your current code would be in the false
branch of that.

It seems that you would do something like:

       IF NOT red + amber + green light
           IF NOT red + amber light
               IF NOT amber + green light
> >               IF NOT red light
> >                  IF NOT amber light
> >                     IF NOT green light

Which does fullfil your 'nesting in true', but to me has several
'uglinesses':

First is the highly contrived negative testing required to make
it all in the true branch.  Many programmers make mistakes with
negative tests, especially in conjunction with ANDs and ORs,
where they would write perfectly correct positive tests.

In fact there were changes to Cobol made specifically because of
how the use of NOT was confusing to many.  I would expect that
many programmers would be unsure of what all these meant:

      IF NOT Red OR Amber
      IF NOT ( Red OR Amber )
      IF NOT Red AND Amber
      IF NOT Red AND NOT Amber

as a test put these into groups that are equivalent without
looking the rules up the in manual.

Second that it ensures that the actions are as far removed from
the test as it is possible to make them.  Making it difficult to
directly relate condition and action makes for poor understanding
and thus makes changes prone to errors.

In a 'case' statement there is direct relationship:

        condition
             action
        condition
             action
        ...

with little chance of mistaking which action goes with which
condition.

In your code there is

       condition
           condition
               condition
                   condition
                       condition
                           condition
                               condition
                                   action
                               action
                           action
                        action
                    action
                action
            action
            action

Which requires:
      Relying on indentation being perfectly done.
      Picking through each ELSE IF and back.
      Comments, which may or may not be true.

none of which are reliable until _proven_ to be so at great
expense of time.  Of course if you had written this yourself
then you _know_ you can rely on all those without having to
check them, but the 'next programmer' cannot.  He is looking
at the code, perhaps, because it doesn't quite work.

It seems that McCameron invented the anti-EVALUATE.

> > with pages of a single IF statement.

If wouldn't necessarily be the pages per se. that made it a
nightmare, it was probably the large separation between the
condition and the resulting action.

I have worked with a 1500 line EVALUATE statement that was
perfectly clear _beacuse_ the condition-actions were tightly
linked.  This was a Windows program so each WHEN could be
treated as if it were a paragraph with the event as its
name.

> in 1969, as described in his book: "COBOL Logic and Programming"

In 1969 there were no Cobol constructs that later came in with
ANS85.  It may have been quite reasonable when using Cobol'61 or
68 to constrain the way IF ... ELSEs were used in order to avoid
ugly 'ELSE NEXT SENTENCE' or, worse, forgetting the ELSE and
winding up with incorrect code. But move on, we no longer need
these obsolete rules now that we have real solutions to the
problems of the 60s.

> Now, sadly, long out of print.

I suspect that there is a good reason why it is out of print, such
as: it is archaic and obsolete.

> An INCORRECTLY (or "ugly" if you like <G>) Nested IF would use
> both the true and false branches and would probably have
> statements after the IF  like..

What is 'incorrect' or 'ugly' is what you are not used to and
don't immediately recognise.

You see your code as: "simple and elegant", I see it as contrived
and difficult when compared to, say, an EVALUATE, or its
equivalent in IF .. ELSEs.


BTW. In NZ there is also another mode: flashing alternate
red/green which means 'out of service - proceed with caution as
if an uncontrolled intersection'.
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 6)_

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2002-11-04T11:13:32-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0211041113.73591314@posting.google.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <b3638c46.0211010841.4abbe41d@posting.google.com> <217e491a.0211031217.616bcd93@posting.google.com>`

```
Amazed at your response, Richard. It is not like you to NOT read what
you are responding to...

Comments below...


riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0211031217.616bcd93@posting.google.com>...
> dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote
> 
…[7 more quoted lines elided]…
> 

I did. Previously, with the use of truth values. If you REALLY want to
look at every possible combination (apart from flashing) then I would
simply assign a truth value to each colour and use EVALUATE...

However, that would NOT demonstrate the use of the decision tree noted
below, or the use of a Nested IF to implement it.

> > > If cond-1 and cond-2 and cond-3 are ALL true  do action 1
> > > If cond-1 and cond-2 are true, but cond-3 is NOT true, do action 2
…[6 more quoted lines elided]…
> 

The object if the exercise was simply to demonstrate the use of a
Nested IF; not a treatise on the possible sequences of traffic lights
around the World
(which, by the way, I am perfectly familiar with...apart from Eileen's
flashing red. Right turns on a red light are quite legitimate in
California but the light doesn't flash.) I therefore opted for
something with 4 states. It was an EXAMPLE, for Chrissake!


> > > For me an IF is "nested"  CORRECTLY when nesting occurs in
> > > the TRUE Branch only.
…[4 more quoted lines elided]…
>

No I haven't. Both the true and false branches are documented, but the
IF is ONLY nested in the TRUE side.


========================  complete irrelevance 
=======================
> The 'obvious' place to put the red+amber test would be after
> the ELSE before Prepare-to-stop.
>
If I was going to do a RED+AMBER test I would have used a truth value
as discussed in earlier post to this thread. If there were 8 values I
CERTAINLY would not use a Nested IF, especially when EVALUATE is now
available. In the olden days I would have broken the tests down.

Anything on combinations of lights OTHER than the ones I chose to
demonstrate the nested IF is therefore irrelevant...

> > > ELSE
>         IF amber light
…[13 more quoted lines elided]…
> It seems that you would do something like:

Assumption on your part, and incorrect assumption at that...

> 
>        IF NOT red + amber + green light
…[8 more quoted lines elided]…
> 

I agree. I wouldn't do it. If you had read what I wrote you wouldn't
have believed that I would do it.

> First is the highly contrived negative testing required to make
> it all in the true branch.  Many programmers make mistakes with
…[13 more quoted lines elided]…
> looking the rules up the in manual.

No problem at all... I'm perfectly familar with both of De Morgan's
Laws and have run seminars on Boolean Algebra and Propositional
Calculus... (However, I would use parentheses to remove any ambiguity
for the sake of people less logically endowed <G>)


> 
> Second that it ensures that the actions are as far removed from
…[11 more quoted lines elided]…
> 

I can't believe you are arguing this! Of course, an EVALUATE is to be
preferred. I said as much in my post. The discussion was predicated on
the fact that EVALUATE was NOT available!!!




> with little chance of mistaking which action goes with which
> condition.
…[30 more quoted lines elided]…
> It seems that McCameron invented the anti-EVALUATE.

There WAS no EVALUATE when Fritz wrote his book! Cheesh!


> 
> > > with pages of a single IF statement.
…[25 more quoted lines elided]…
> 

Yes, it is certainly archaic. However, it has a style of its own which
makes it a classic. Many COBOL programmers in the Sixties (self
included) struggled with nested IFs; McCameron's book cleared the
topic nicely.

And if you REALLY believe I still code the way I did then and HAVEN'T
moved on then you really haven't got much idea of how I write COBOL.
(But, then I rarely post public samples of code because people seem to
misinterpret why they are posted, and go off on to their own private
tangent...<G>)


> > An INCORRECTLY (or "ugly" if you like <G>) Nested IF would use
> > both the true and false branches and would probably have
…[4 more quoted lines elided]…
>

There is no COBOL that I don't recognise. I'm a COBOL programmer. What
I consider ugly is purely a subjective judgement that has more to do
with aesthetics than failure to understand.

 
> You see your code as: "simple and elegant", I see it as contrived
> and difficult when compared to, say, an EVALUATE, or its
> equivalent in IF .. ELSEs.
> 

Again, you are ascribing a position to me which I never adopted. The
code is predicated on NOT using IF...ELSE...END-IF  (for efficiency)
and not using
EVALUATE (as being not available). If you want to nest an IF, then I
suggest it is simpler and more elegant to nest only in the TRUE
branch. But I really don't care how you do it. If required to, I'll
debug your code no matter how you code it.


> 
> BTW. In NZ there is also another mode: flashing alternate
> red/green which means 'out of service - proceed with caution as
> if an uncontrolled intersection'.

Ah, yes! I remember that now....of course. Wonder why I didn't think
it was relevant to a discussion of nested IFs in COBOL...? It must be,
or you wouldn't have raised it would you <G>?
==========================  end of complete irrelevance
====================

Pete.
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 7)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2002-11-05T03:27:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021104222758.20473.00000054@mb-cl.aol.com>`
- **References:** `<b3638c46.0211041113.73591314@posting.google.com>`

```
>From: dashwood@enternet.co.nz  (Peter E. C. Dashwood)
>Date: 11/4/02 2:13 PM Eastern Standard Time

> It was an EXAMPLE, for Chrissake!
>

Take a deep breath Pete :)  Grab a brew or nice glass of your favorite wine and
kick back.  You know these discussions always deteriorate into a mass of this
and that trivia!
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 8)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-11-06T08:16:11
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dc8ce35_3@Usenet.com>`
- **References:** `<b3638c46.0211041113.73591314@posting.google.com> <20021104222758.20473.00000054@mb-cl.aol.com>`

```
Sound advice, as always, Eileen <G>.

And you're right that I do know better...(I just expect more from
Richard...<G>)

Pete.
YukonMama <yukonmama@aol.com> wrote in message
news:20021104222758.20473.00000054@mb-cl.aol.com...
> >From: dashwood@enternet.co.nz  (Peter E. C. Dashwood)
> >Date: 11/4/02 2:13 PM Eastern Standard Time
…[4 more quoted lines elided]…
> Take a deep breath Pete :)  Grab a brew or nice glass of your favorite
wine and
> kick back.  You know these discussions always deteriorate into a mass of
this
> and that trivia!



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-11-04T21:18:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0211042118.4d4f038@posting.google.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <b3638c46.0211010841.4abbe41d@posting.google.com> <217e491a.0211031217.616bcd93@posting.google.com> <b3638c46.0211041113.73591314@posting.google.com>`

```
dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote

> Amazed at your response, Richard. It is not like you to NOT read what
> you are responding to...

OTOH, it is not like you to think that I am responding to something
completely different.

> I agree. I wouldn't do it. If you had read what I wrote you wouldn't
> have believed that I would do it.

If I had read what you wrote _elsewhere_, then maybe ..

> I can't believe you are arguing this! Of course, an EVALUATE is to be
> preferred. I said as much in my post. 

No. You didn't.  Not in the post that I responded to.  You may have
done so in a completely different, later, post.

> The discussion was predicated on
> the fact that EVALUATE was NOT available!!!

Not in the actual post that I responded to, and _read_.  Perhaps you
were reading something else entirely.

> There WAS no EVALUATE when Fritz wrote his book! Cheesh!

There were, however, equivalent structures in other languages at the
time.

Regardless of whether there was an EVALUATE or not, the 'only true'
nesting is the antithesis of how a case statement makes a clear
relationship between the conditions and the actions.  The 'else only'
nesting (or stacked IF) does emulate an EVALUATE nicely.

The issue was that you posted that the nesting only in the true branch
was the only 'correct' or 'desirable' or 'proper' way, you taught it
and recommended it, and that other structures, such as balanced
IF..ELSE and a nested (or stacked) IF that emulated an EVALUATE was
'ugly', 'incorrect', a 'nightmare' and you wouldn't use it.

I considered that the opinions you expressed in that post that I
responded to was wrong.  While it may have appeared useful 30 years
ago, if you hadn't seen a better way, I think that your continuing
enthusiasm for it was misplaced.

> And if you REALLY believe I still code the way I did then and HAVEN'T
> moved on then you really haven't got much idea of how I write COBOL.

No, I haven't much idea about how you code, I can only base this on
what you call 'proper', 'correct' and 'desirable'.

> Again, you are ascribing a position to me which I never adopted. The
> code is predicated on NOT using IF...ELSE...END-IF  (for efficiency)
> and not using
> EVALUATE (as being not available). 

No it wasn't, but then I only read the post that I was _responding_ to
and not some other collection of posts that you had in mind.

> If you want to nest an IF, then I
> suggest it is simpler and more elegant to nest only in the TRUE
> branch. 

And I suggested that was a very poor way of doing it (for reasons
stated), emulating an EVALUATE is simpler and more elegant.

In fact I often prefer stacked IFs (nested enirely in each ELSE) over
an EVALUATE where there is a variety of conditions necessitating a
rather contrived 'EVALUATE TRUE'.

> > BTW. In NZ ..

> Ah, yes! I remember that now....of course. Wonder why I didn't think
> it was relevant to a discussion of nested IFs in COBOL...? It must be,
> or you wouldn't have raised it would you <G>?

You do understand what 'BTW' means don't you ?
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 8)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2002-11-06T05:42:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DC8ABAC.3080702@optonline.NOSPAM.net>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <b3638c46.0211010841.4abbe41d@posting.google.com> <217e491a.0211031217.616bcd93@posting.google.com> <b3638c46.0211041113.73591314@posting.google.com> <217e491a.0211042118.4d4f038@posting.google.com>`

```
Richard wrote:
> dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote

(snip)
> 
> And I suggested that was a very poor way of doing it (for reasons
…[4 more quoted lines elided]…
> rather contrived 'EVALUATE TRUE'.

What the devil's wrong with "Evaluate True"?
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 9)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-11-06T08:17:24
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dc8ce3c_3@Usenet.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <b3638c46.0211010841.4abbe41d@posting.google.com> <217e491a.0211031217.616bcd93@posting.google.com> <b3638c46.0211041113.73591314@posting.google.com> <217e491a.0211042118.4d4f038@posting.google.com> <3DC8ABAC.3080702@optonline.NOSPAM.net>`

```
Go on Liam! Sic 'im! <G>

Pete.

Liam Devlin <LiamD@optonline.NOSPAM.net> wrote in message
news:3DC8ABAC.3080702@optonline.NOSPAM.net...
> Richard wrote:
> > dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote
…[11 more quoted lines elided]…
>



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-11-06T19:56:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aqbs5e$2ca$1@peabody.colorado.edu>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <b3638c46.0211010841.4abbe41d@posting.google.com> <217e491a.0211031217.616bcd93@posting.google.com> <b3638c46.0211041113.73591314@posting.google.com> <217e491a.0211042118.4d4f038@posting.google.com> <3DC8ABAC.3080702@optonline.NOSPAM.net>`

```

On  5-Nov-2002, Liam Devlin <LiamD@optonline.NOSPAM.net> wrote:

> What the devil's wrong with "Evaluate True"?

It's neither English nor computerese.   Why use big English words if it isn't
obvious to a non-programmer what it means?
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 10)_

- **From:** Liam Devlin <LiamD@optonline.SPAMNOT.net>
- **Date:** 2002-11-09T08:25:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DCCC63A.6050907@optonline.SPAMNOT.net>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <b3638c46.0211010841.4abbe41d@posting.google.com> <217e491a.0211031217.616bcd93@posting.google.com> <b3638c46.0211041113.73591314@posting.google.com> <217e491a.0211042118.4d4f038@posting.google.com> <3DC8ABAC.3080702@optonline.NOSPAM.net> <aqbs5e$2ca$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> On  5-Nov-2002, Liam Devlin <LiamD@optonline.NOSPAM.net> wrote:
> 
…[4 more quoted lines elided]…
> obvious to a non-programmer what it means?

That's where we disagree, "Evaluate True" is required to handle the 
COBOL 88-levels. I went nuts the first time I tried to code COBOL II and 
wanted to set up a case structure, e.g.:

Evaluate	variable
When		88-level ...

End-Evaluate

That's invalid, the "True" form makes it work, as in:

Evaluate	True
When		88-level ...

End-Evaluate

Every IF statement evaluates (small "e") as either True or False. I just 
don't see the issue with:

Evaluate True.

As always, YMMV

:-)
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 11)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-11-10T07:45:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DCE0E9A.27E805D7@Azonic.co.nz>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <b3638c46.0211010841.4abbe41d@posting.google.com> <217e491a.0211031217.616bcd93@posting.google.com> <b3638c46.0211041113.73591314@posting.google.com> <217e491a.0211042118.4d4f038@posting.google.com> <3DC8ABAC.3080702@optonline.NOSPAM.net> <aqbs5e$2ca$1@peabody.colorado.edu> <3DCCC63A.6050907@optonline.SPAMNOT.net>`

```
Liam Devlin wrote:
> 
> That's where we disagree, "Evaluate True" is required to handle the
> COBOL 88-levels.

"EVALUATE TRUE" is not _required_.  It is perfectly correct to handle
88-levels with IF.
 
> Evaluate        variable
> When            88-level ...

Or, putting it another way: using EVALUATE means that you never need
88-levels.

   EVALUATE variable
   WHEN value-1
   WHEN value-2 THRU value-3
         action-1
   WHEN value-4
         action-2

> As always, YMMV

Yes, entirely a matter of prefernece.
```

###### ↳ ↳ ↳ EVALUATE TRUE (was: stacked IF terminology?

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-11-09T13:58:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aqjpe9$8v2$1@slb6.atl.mindspring.net>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <b3638c46.0211010841.4abbe41d@posting.google.com> <217e491a.0211031217.616bcd93@posting.google.com> <b3638c46.0211041113.73591314@posting.google.com> <217e491a.0211042118.4d4f038@posting.google.com> <3DC8ABAC.3080702@optonline.NOSPAM.net> <aqbs5e$2ca$1@peabody.colorado.edu> <3DCCC63A.6050907@optonline.SPAMNOT.net> <3DCE0E9A.27E805D7@Azonic.co.nz>`

```
The disadadvantage of the technique

  Evaluate Data-Name
   When Value-1 ...
    When Value-2 thru Value-3

is the same as all uses of "explicit" value checks versus 88-levels, i.e.
that you must change EVERY occurrence of the test in the procedure division
when do this - instead of a single place when you use 88-levels.  Certainly
it can be done either way, but IMHO, the 88-level method is always BETTER
for a "condition" that is used multiple times in the Procedure Division.
(When it is used a single place in the Procedure Division, I see little
advantage one way or another).  Even for compilers that support "true
constants" (extension in '85 Standard, required in the 2002 Standard), there
is still an advantage in using 88-levels as these allow for ADDING
additional values (not expanding a range) with a single place to do this.

    ****

And back to the original issue of when/if to use "EVALUATE TRUE" - I like to
use it for multi-condition case structures.  Although these MAY be difficult
to "maintain" or understand, the often better (IMHO) reflect some business
cases, e.g.

Evaluate TRUE also TRUE also FALSE    *> and some people may NOT like mixing
trues and falses

  When A > B Also C = D  also A = C
      Perform Case-1
  When A < B Also C > D  Also A > C
   When A < B Also C = D Also A > C
      Perform Case-2
   When ...

In the "abstract" this doesn't look great, but it certainly is typical of
SOME business logic.  Changing this to nested IF's certainly CAN be done,
but does tend to look a little "odd" (using one form of optional punctuation
and indenting)

If (A > B)
  and (C = D)
  and (A not = C)
       Perform Case-1
Else If
 ( (A < B)
  and (C > D)
  and (A not > C))
 or
  (A < B)
  and (C = D)
  and (A not > C))
    Perform Case-2
 Else IF
 ...
```

###### ↳ ↳ ↳ Re: EVALUATE TRUE (was: stacked IF terminology?

_(reply depth: 13)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-11-09T20:28:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0211092028.3e6299e6@posting.google.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <b3638c46.0211010841.4abbe41d@posting.google.com> <217e491a.0211031217.616bcd93@posting.google.com> <b3638c46.0211041113.73591314@posting.google.com> <217e491a.0211042118.4d4f038@posting.google.com> <3DC8ABAC.3080702@optonline.NOSPAM.net> <aqbs5e$2ca$1@peabody.colorado.edu> <3DCCC63A.6050907@optonline.SPAMNOT.net> <3DCE0E9A.27E805D7@Azonic.co.nz> <aqjpe9$8v2$1@slb6.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote

> The disadadvantage of the technique
> 
…[6 more quoted lines elided]…
> when do this - instead of a single place when you use 88-levels.  

OTOH using 88 levels means that text searches or greps for use of the
'data-name' are defeated. Of course one could have all your 88 levels
prepended by the data-name but then it looks quite contrived IMHO.

In general if a value changes or is added then it is not just a matter
of fiddling the 88 levels, all the uses of the 88 levels have to be
checked because usually the new value is a _different_ option than
needs a new condition branch.

So generally I prefer to be able to text search easily for data-name
rather than to search for several 88 levels.

> but IMHO, the 88-level method is always BETTER
> for a "condition" that is used multiple times in the Procedure Division.

Dislike 88s, never use them.  I sometime, however, use symbolic
constants (or variables that emulate this) instead of literals:  Then
I get both advantages (IMHO) with the data name _and_ meaningful
condition names:

      EVALUATE Interface-Function
      WHEN Read-with-Lock
            ...

where, for example these are defined as:

      01  Interface-Function        PIC X.
      01  IF-values.
          03  Read-with-Lock        PIC X VALUE "L".
          03  Read-no-Lock          PIC X VALUE "R".
              etc

> And back to the original issue of when/if to use "EVALUATE TRUE" - I like to
> use it for multi-condition case structures.  Although these MAY be difficult
…[11 more quoted lines elided]…
>    When ...

'Backwards' decision tables.
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 12)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2002-11-10T01:35:55+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qr6rsuggmpsg78c0vl77lb0b5bcpm176pt@4ax.com>`
- **References:** `<appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <b3638c46.0211010841.4abbe41d@posting.google.com> <217e491a.0211031217.616bcd93@posting.google.com> <b3638c46.0211041113.73591314@posting.google.com> <217e491a.0211042118.4d4f038@posting.google.com> <3DC8ABAC.3080702@optonline.NOSPAM.net> <aqbs5e$2ca$1@peabody.colorado.edu> <3DCCC63A.6050907@optonline.SPAMNOT.net> <3DCE0E9A.27E805D7@Azonic.co.nz>`

```
On Sun, 10 Nov 2002 07:45:30 +0000 Richard Plinston <riplin@Azonic.co.nz>
wrote:

:>Liam Devlin wrote:
 
:>> That's where we disagree, "Evaluate True" is required to handle the
:>> COBOL 88-levels.

:>"EVALUATE TRUE" is not _required_.  It is perfectly correct to handle
:>88-levels with IF.


:>> Evaluate        variable
:>> When            88-level ...

That requires tieing the 88 to the name in code - part of what an 88 can
prevent.

:>Or, putting it another way: using EVALUATE means that you never need
:>88-levels.

So you don't like 88's.

:>   EVALUATE variable
:>   WHEN value-1
:>   WHEN value-2 THRU value-3
:>         action-1
:>   WHEN value-4
:>         action-2

:>> As always, YMMV

:>Yes, entirely a matter of prefernece.

Yep.
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 12)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2002-11-10T20:15:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DCEBE20.6070301@optonline.NOSPAM.net>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <b3638c46.0211010841.4abbe41d@posting.google.com> <217e491a.0211031217.616bcd93@posting.google.com> <b3638c46.0211041113.73591314@posting.google.com> <217e491a.0211042118.4d4f038@posting.google.com> <3DC8ABAC.3080702@optonline.NOSPAM.net> <aqbs5e$2ca$1@peabody.colorado.edu> <3DCCC63A.6050907@optonline.SPAMNOT.net> <3DCE0E9A.27E805D7@Azonic.co.nz>`

```
Richard Plinston wrote:
> Liam Devlin wrote:
> 
…[5 more quoted lines elided]…
> 88-levels with IF.

I didn't mean "IF" was no longer valid, but that's how you use 88-levels 
in a case structure.

Evaluating the variable and coding the When's as value-1 value-2, etc., 
defeats the whole purpose of the 88-levels IMHO.
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-11-11T16:22:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aqolg8$sh7$1@peabody.colorado.edu>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <b3638c46.0211010841.4abbe41d@posting.google.com> <217e491a.0211031217.616bcd93@posting.google.com> <b3638c46.0211041113.73591314@posting.google.com> <217e491a.0211042118.4d4f038@posting.google.com> <3DC8ABAC.3080702@optonline.NOSPAM.net> <aqbs5e$2ca$1@peabody.colorado.edu> <3DCCC63A.6050907@optonline.SPAMNOT.net>`

```

On  9-Nov-2002, Liam Devlin <LiamD@optonline.SPAMNOT.net> wrote:

> > It's neither English nor computerese.   Why use big English words if it
> > isn't
…[4 more quoted lines elided]…
> wanted to set up a case structure, e.g.:

I use it for the same reason you do.  It does the job - but it doesn't do it in
what I call the "spirit" of CoBOL.

Do you truly disagree with my criticism of the command?  Do you think it is
either English or computerese?

It would have been more like English simply to leave out the word "true".
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 12)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2002-11-12T19:54:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DD15C5F.6070506@optonline.NOSPAM.net>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <b3638c46.0211010841.4abbe41d@posting.google.com> <217e491a.0211031217.616bcd93@posting.google.com> <b3638c46.0211041113.73591314@posting.google.com> <217e491a.0211042118.4d4f038@posting.google.com> <3DC8ABAC.3080702@optonline.NOSPAM.net> <aqbs5e$2ca$1@peabody.colorado.edu> <3DCCC63A.6050907@optonline.SPAMNOT.net> <aqolg8$sh7$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> On  9-Nov-2002, Liam Devlin <LiamD@optonline.SPAMNOT.net> wrote:
> 
…[14 more quoted lines elided]…
> either English or computerese?

Certainly not English, what is "computerese"?

> It would have been more like English simply to leave out the word "true".

Perhaps, but I've never bought into the COBOL is an "English-like" 
programming language very much. Maybe this is a problem inherent in a 
language designed by a committee? :-)
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-11-07T07:37:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DCA182E.2C85F9BC@Azonic.co.nz>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <b3638c46.0211010841.4abbe41d@posting.google.com> <217e491a.0211031217.616bcd93@posting.google.com> <b3638c46.0211041113.73591314@posting.google.com> <217e491a.0211042118.4d4f038@posting.google.com> <3DC8ABAC.3080702@optonline.NOSPAM.net>`

```
Liam Devlin wrote:
> Richard wrote:
> > In fact I often prefer stacked IFs (nested enirely in each ELSE) over
…[3 more quoted lines elided]…
> What the devil's wrong with "Evaluate True"?

There is nothing "wrong" with EVALUATE TRUE, it is just (as I said) a
personal preference.

'EVALUATE variable WHEN value ...' is a structure found in many
languages as a case statement.

'EVALUATE TRUE WHEN condition ..' is just 'IF condition .. ELSE IF's
with another syntax.

Thus we have available two identical structures with only minor syntax
changes.

    EVALUTE TRUE WHEN ( condition 1 )
        action 1
    WHEN ( condition 2 )
        ...

    IF ( condition 1 )
        action 1
    ELSE IF ( condition 2 )
        ...

I find it clearer to only use EVALUATE when it is specifically a case
statement.  YMMV.

(Or is it just that I am a refugee from the 70s who thinks that all
these new fangled '85 ideas are just a passing fad ?).
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 10)_

- **From:** "David Robinson" <david@nighttime.demon.invalid>
- **Date:** 2002-11-06T21:31:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HSfy9.2301$kj6.21174522@news-text.cableinet.net>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <b3638c46.0211010841.4abbe41d@posting.google.com> <217e491a.0211031217.616bcd93@posting.google.com> <b3638c46.0211041113.73591314@posting.google.com> <217e491a.0211042118.4d4f038@posting.google.com> <3DC8ABAC.3080702@optonline.NOSPAM.net> <3DCA182E.2C85F9BC@Azonic.co.nz>`

```
"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3DCA182E.2C85F9BC@Azonic.co.nz...
> (Or is it just that I am a refugee from the 70s who thinks that all
> these new fangled '85 ideas are just a passing fad ?).

Yes you are :)

Pre-85 COBOL is *EVIL*, I tells ya, *EVIL*!!!
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 8)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-11-06T08:14:05
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dc8ce30_3@Usenet.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <b3638c46.0211010841.4abbe41d@posting.google.com> <217e491a.0211031217.616bcd93@posting.google.com> <b3638c46.0211041113.73591314@posting.google.com> <217e491a.0211042118.4d4f038@posting.google.com>`

```
Richard,

It is pretty obvious that you didn't see the EARLIER (NOT later) post in the
same thread and a misunderstanding ensued.

While I am very happy to spend time defending a position I HAVE adopted, I'm
not prepared to do so on positions which are ascribed to me by assumption
and which I have NOT adopted.

I see no point in going further with this.

Pete.


Richard <riplin@Azonic.co.nz> wrote in message
news:217e491a.0211042118.4d4f038@posting.google.com...
> dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote
>
…[75 more quoted lines elided]…
> You do understand what 'BTW' means don't you ?



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-11-06T10:17:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0211061017.39396165@posting.google.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <b3638c46.0211010841.4abbe41d@posting.google.com> <217e491a.0211031217.616bcd93@posting.google.com> <b3638c46.0211041113.73591314@posting.google.com> <217e491a.0211042118.4d4f038@posting.google.com> <3dc8ce30_3@Usenet.com>`

```
"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote 

> It is pretty obvious that you didn't see the EARLIER (NOT later) post in the
> same thread and a misunderstanding ensued.

The post that I was responding to and quoted was, according to Google,
the 3rd post in the thread and your first:
--------------------------------
>> Date: 2002-10-30 13:43:26 PST
>>
…[5 more quoted lines elided]…
>> TRUE Branch only.


My response was, by the way, dated by Google as
--------------------------------
>> Date: 2002-10-31 12:12:15 PST 


I did find a message in which you mentioned EVALUATE:
---------------------------------
>> Date: 2002-10-31 16:50:11 PST

>>> So you're saying *never* nest the ELSE part?

>> No, I'm saying it is ugly to do so, and I'm saying I wouldn't 
>> do it from preference.(Actually, I feel strongly enough about 
>> it that I would never do it, ...

>> Given that EVALUATE is not an option, why not:

Do you think that Google 'misunderstood' your personal time sequencing
too ?  ;-)

Or perhaps the northern hemisphere has confused you: day is now night,
spring is now fall, the Sun is south not north, calendars run
backwards ?  ;-)

Or is it now being upright after so long of standing upside down 'down
under' ?


> While I am very happy to spend time defending a position I HAVE adopted, I'm
> not prepared to do so on positions which are ascribed to me by assumption
> and which I have NOT adopted.

>> For me an IF is "nested"  CORRECTLY when nesting occurs in the 
>> TRUE Branch only.

So, is it only my assumption that you said this (and reinforced it in
_later_ message)?
 
> I see no point in going further with this.

OK. If you don't _actually_ "feel strongly enough" about discussing
forms of IF statements and prefer to argue procedural issues.
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 10)_

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2002-11-07T09:06:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0211070906.58c69ff7@posting.google.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <217e491a.0210311212.3dd7a44e@posting.google.com> <b3638c46.0211010841.4abbe41d@posting.google.com> <217e491a.0211031217.616bcd93@posting.google.com> <b3638c46.0211041113.73591314@posting.google.com> <217e491a.0211042118.4d4f038@posting.google.com> <3dc8ce30_3@Usenet.com> <217e491a.0211061017.39396165@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0211061017.39396165@posting.google.com>...
> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote 
> 
> > It is pretty obvious that you didn't see the EARLIER (NOT later) post in the
> > same thread and a misunderstanding ensued.
> 

I meant earlier than your response... sorry <G>.

> The post that I was responding to and quoted was, according to Google,
> the 3rd post in the thread and your first:
…[37 more quoted lines elided]…
>
I believe all of the above, combined with advancing senility, may have
affected my sense of time. <G> I stand corrected.
 
> 
> > While I am very happy to spend time defending a position I HAVE adopted, I'm
…[8 more quoted lines elided]…
> 

No, that wasn't what you made the assumptions about... I DID say that,
and I stand by it.

> > I see no point in going further with this.
> 
> OK. If you don't _actually_ "feel strongly enough" about discussing
> forms of IF statements and prefer to argue procedural issues.

I don't actually "prefer" to argue anything. I will happily express an
opinion and defend it by argument, but I have no particular
preference. What I won't do is waste time arguing things that are not
part of the position I have adopted. My posts were intended to
demonstrate one form of Nested IF. (The one I personally prefer and
use.) They were not intended to stimulate a lecture on the traffic
lights of the World or the relative merits of EVALUATE or IF ELSE...
with diversions into what I would PROBABLY code (based on incorrect
assumptions), all for the sake of having a good "argument"...<G>

Maybe, in a year or two, as the brain cells continue to die you will
be able to trap me into such a debate, but that time is not yet...<G>

Pete.
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-11-01T03:25:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c28156$4e5a3360$abc2f943@chottel>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com>`

```
www.amazon.com has used books and based on Pete's recommendation I just
ordered one for $8.44 including shipping!  Search on the book title not on
the author name.

Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote in article
<3dc04f92_3@Usenet.com>...
> Comments below, Bill.
> 
> William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
> news:appeds$hu9$1@slb5.atl.mindspring.net...
> > I am afraid that (IMHO) this is a "nested IF" statement - no matter
what
> you
> > think it might be.  Furthermore, in "maintenance" someone can add code
…[3 more quoted lines elided]…
> > The EVALUATE statement is (traditionally) called a CASE structure. 
What
> you
> > are doing here is trying to "simulate" a CASE structure using the
> > *RESTRICTED* syntax of pre'85 Standard COBOL where no native support
was
> > provided.
> >
> > It might help me to understand your question better if you showed us
what
> > you think is a "nested IF statement" without being a "stacked IF"
> statement.
> >
> > It seems to me that ANY time you have an IF statement "embedded" in
either
> > the IF branch or the ELSE branch, you have a "nested IF" and there is
> really
…[6 more quoted lines elided]…
> For me an IF is "nested"  CORRECTLY when nesting occurs in the TRUE
Branch
> only.
> 
…[23 more quoted lines elided]…
> described in his book: "COBOL Logic and Programming" Now, sadly, long out
of
> print.
> (I believe this is the best book on COBOL Language that was ever written
and
> I have read and reviewed dozens of them...)
> 
> This is such a simple and elegant use of nested IF that I have taught it
to
> numerous students.
> 
…[9 more quoted lines elided]…
> A CORRECTLY (or "desirably" if you like...<G>) Nested IF would be as
above.
> 
> (This is the ONLY usage that I would refer to as a "Nested IF"; reason
> being, I would NEVER write the alternative "ugly" form...<G>)
> 
> An INCORRECTLY (or "ugly" if you like <G>) Nested IF would use both the
true
> and false branches and would probably have statements after the IF 
like...
> 
> IF NOT red-light
…[9 more quoted lines elided]…
> Although this may technically qualify as a "Nested IF", to me it is ugly
and
> I wouldn't use it.
> 
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 4)_

- **From:** Edward Reid <edwardreid@spamcop.net>
- **Date:** 2002-11-01T09:53:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01HW.B9E7FF7C00379CEF1710ECE0@news-east.usenetserver.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <01c28156$4e5a3360$abc2f943@chottel>`

```
On Thu, 31 Oct 2002 22:25:28 -0500, Charles Hottel wrote
> www.amazon.com has used books and based on Pete's recommendation I just
> ordered one for $8.44 including shipping!  Search on the book title not on
> the author name.

Ah-ha. Pete is normally such a stickler that I didn't consider the 
possibility that he'd misspelled the name -- it's McCameron, and now I 
can find it with no trouble. Thanks.

There seem to be later editions into the 1980s, including a hardback in 
1986 which may or may not differ from the softbacks in the early 1980s. 
Looks like the softbacks at least were in a 4th edition.

Edward
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 5)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-11-03T14:02:53
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dc52a92$1_6@Usenet.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <01c28156$4e5a3360$abc2f943@chottel> <01HW.B9E7FF7C00379CEF1710ECE0@news-east.usenetserver.com>`

```
Sorry about that.

I remember this book as having a black soft cover. I read it over 30 years
ago and haven't seen it since, but I should've got the name right.

Pete.

Edward Reid <edwardreid@spamcop.net> wrote in message
news:01HW.B9E7FF7C00379CEF1710ECE0@news-east.usenetserver.com...
> On Thu, 31 Oct 2002 22:25:28 -0500, Charles Hottel wrote
> > www.amazon.com has used books and based on Pete's recommendation I just
> > ordered one for $8.44 including shipping!  Search on the book title not
on
> > the author name.
>
…[10 more quoted lines elided]…
>



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 4)_

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2002-11-01T08:45:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0211010845.3163558@posting.google.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <01c28156$4e5a3360$abc2f943@chottel>`

```
Charles,

are you saying that Amazon have actually come up with a copy of "COBOL
LOGIC AND PROGRAMMING"?

I never thought to try them... thanks, I'll try and get a copy myself.

Pete.


"Charles Hottel" <chottel@cpcug.org> wrote in message news:<01c28156$4e5a3360$abc2f943@chottel>...
> www.amazon.com has used books and based on Pete's recommendation I just
> ordered one for $8.44 including shipping!  Search on the book title not on
…[124 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 5)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-11-02T00:48:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c28209$8ee230a0$3cccf943@chottel>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <01c28156$4e5a3360$abc2f943@chottel> <b3638c46.0211010845.3163558@posting.google.com>`

```
Apparently they have made deals with bookstores and individuals to sell
those peoples used books.  Last time I logged on they displayed how much
money I could make by selling all the books that I previously bought from
them!

Peter E. C. Dashwood <dashwood@enternet.co.nz> wrote in article
<b3638c46.0211010845.3163558@posting.google.com>...
> Charles,
> 
…[8 more quoted lines elided]…
> "Charles Hottel" <chottel@cpcug.org> wrote in message
news:<01c28156$4e5a3360$abc2f943@chottel>...
> > www.amazon.com has used books and based on Pete's recommendation I just
> > ordered one for $8.44 including shipping!  Search on the book title not
on
> > the author name.
> > 
…[9 more quoted lines elided]…
> > > > think it might be.  Furthermore, in "maintenance" someone can add
code
> >  after
> > > > one of the PERFORMs and that would hide what you think you are
doing.
> > > >
> > > > The EVALUATE statement is (traditionally) called a CASE structure. 
…[3 more quoted lines elided]…
> > > > *RESTRICTED* syntax of pre'85 Standard COBOL where no native
support
> >  was
> > > > provided.
> > > >
> > > > It might help me to understand your question better if you showed
us
> >  what
> > > > you think is a "nested IF statement" without being a "stacked IF"
…[4 more quoted lines elided]…
> > > > the IF branch or the ELSE branch, you have a "nested IF" and there
is
> >  really
> > > > no way to distinguish between them.
…[30 more quoted lines elided]…
> > > This method of nesting IFs is the way I learned from Fritz D.
MacCameron
> > > PhD., sometime COBOL lecturer at Louisiana State University, in 1969,
as
> > > described in his book: "COBOL Logic and Programming" Now, sadly, long
out
> >  of
> > > print.
> > > (I believe this is the best book on COBOL Language that was ever
written
> >  and
> > > I have read and reviewed dozens of them...)
> > > 
> > > This is such a simple and elegant use of nested IF that I have taught
it
> >  to
> > > numerous students.
> > > 
> > > In the old days (before standards evolved) we used to suffer from
people
> > > nesting IFs every which way in true and false branches and it was a
> > > nightmare. I saw a program once with PAGES (green lineflo) of a
single IF
> > > statement.
> > > 
…[7 more quoted lines elided]…
> > > (This is the ONLY usage that I would refer to as a "Nested IF";
reason
> > > being, I would NEVER write the alternative "ugly" form...<G>)
> > > 
> > > An INCORRECTLY (or "ugly" if you like <G>) Nested IF would use both
the
> >  true
> > > and false branches and would probably have statements after the IF 
…[12 more quoted lines elided]…
> > > Although this may technically qualify as a "Nested IF", to me it is
ugly
> >  and
> > > I wouldn't use it.
> > > 
> > > Having disposed of what is and is not a "properly" Nested IF, I
believe
> > > Edward's nomenclature of a "Stacked IF" is appropriate and apposite.
<G>
> > > 
> > > Pete.
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: stacked IF terminology?

_(reply depth: 6)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2002-11-02T06:18:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DC36E1B.3040406@optonline.NOSPAM.net>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com> <appeds$hu9$1@slb5.atl.mindspring.net> <3dc04f92_3@Usenet.com> <01c28156$4e5a3360$abc2f943@chottel> <b3638c46.0211010845.3163558@posting.google.com> <01c28209$8ee230a0$3cccf943@chottel>`

```
Charles Hottel wrote:
> Apparently they have made deals with bookstores and individuals to sell
> those peoples used books.  Last time I logged on they displayed how much
> money I could make by selling all the books that I previously bought from
> them!

Seems Amazon usually has prices for used CD's and asks if I have one I 
want to sell when I check their site.
```

#### ↳ Re: stacked IF terminology?

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-10-30T21:00:28
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dc04f8a_3@Usenet.com>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com>`

```

Edward Reid <edwardreid@spamcop.net> wrote in message
news:01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com...
> What (if anything) do you call the following sort of structure?
>
…[8 more quoted lines elided]…
>
"Stacked IF" is a very good name for it.

EVALUATE is obviously preferable, but where it isn't available the above can
offer some efficiency increase over "Test and Branch" and doesn't offend the
sensibilities of the people who don't like GO TO.

Pete.

> etc. Doesnt matter whether it's C74 or C85, though in the latter you'd
> probably use EVALUATE instead, nor whether the scope terminator is
…[28 more quoted lines elided]…
>



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

#### ↳ Re: stacked IF terminology?

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-10-31T00:22:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c28073$a29ba960$9995f243@chottel>`
- **References:** `<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com>`

```
I usually call this "multi-way decision" because in "The C programming
Language" page 57 it says that this sequence "occurs so often it is worth a
brief separate discussion. This sequence of IF statements is  the most
general way of writing a multi-way decision."  However I would not object
to calling it "case" because that is how case was usually implemented
before the arrival of EVALUATE.

Edward Reid <edwardreid@spamcop.net> wrote in article
<01HW.B9E5A46E006639C616D5FAF0@news-east.usenetserver.com>...
> What (if anything) do you call the following sort of structure?
> 
…[40 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
