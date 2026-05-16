[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# L S 6 W K M C Re: Short-circuiting

_1 message · 1 participant · 1998-10_

---

### L S 6 W K M C Re: Short-circuiting

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298273.5884.10226@kcbbs.gen.nz>`

```

 
>> In each language it is necessary to understand its particular
>> evaluation order, there is _no_ substitute.  In C, for example,
>> there are 15 levels precedence, each specifying the grouping,
>> and 15 levels of associativity.
 
> It has escaped your notice (why am I not surprised?), but it is
> not computer languages which establish evaluation order in
> mathematical expressions, but universally recognized
> mathematical practice.
 
In mathematical expressions it is exactly the 'mathematical
language' that establishes evaluation order.  Different
mathematical languages (and there are several) may establish
their own order. Polish Notation and RPN, for example, have
different orders of evaluation than infix notation.  Your idea
that there is a 'universally recognised practice' is flawed by
your apparent belief that there is only _one_ system.
 
Computer languages do, in fact, establish the evaluation order
that _they_ require.  Some languages do strict left-to-right
evaluation regardless of any priorities.  Other languages use
one or other of the mathematical notations, or some other
ordering that is appropriate.
 
> This has absolutely nothing to do with what I was talking about.
 
'Mathematical Practice' has nothing to do with what anyone was
talking about, so why did you introduce it ? (except as a
misunderstanding about the points raised with C).
 
The fact that you misunderstood the issue with C language
evaluation does tend to show that you don't even understand the
terminology of C, let alone the issues involved.
 
Now looking at the core part of your arguments:
 
>> There isn't a programmer alive who has written a lot of code
>> in several languages who hasn't at one time or another
>> written a statement using the syntax of a wrong language.
 
and:
 
>> A practice such as you suggest is absolutely guaranteed to
>> increase the probability of writing broken code, and there is
>> nothing in this world you can do to eliminate that, except
>> avoid the practice altogether.
 
Just to summarise, the 'practice' that I suggested was:
       1) testing indecies before use
       2) using short-circuit evaluation in Cobol 85
 
In Cobol the short-circuiting of evaluations is a non-issue.
If you code correctly and do not know of short-circuiting
then whether evaluations are actually done or not is irrelevant
 
However, you brought in "several languages".  In other langauages
(notably C, but others as well) the issue of short-circuited
evaluations is _vital_ to the correct coding of the program.
You need to know that they occur and when they occur, you need
to know the standard for each language.
 
You cannot "avoid the issue" if you "code in several languages".
 
> No, I work hard at developing habits which will serve me, not
> trick me.  This is because I am smart enough to know that I am
> not perfect. Apparently you aren't that smart, because it is a
> sure bet you aren't perfect.  Not that you would agree on that,
> of course.
 
>> This is a fact, not an opinion.
 
You seem to work hard at 'abuse', 'intellectual bullying',
'pomposity', perhaps these do generally serve you well.
 
 
> Only seemingly obsolete to someone who hasn't a clue about the
> real issue here.  You are apparently unaware (as you are of so
> many other things) that many, many MIS shops do *not* use the
> latest compiler?
 
Fully aware, and that is _exactly_ why I qualified all my
comments about Cobol to ensure that it was recognised as applying
to Cobol-85.  However, just because some MIS shops still use
older standards does not mean that everyone should continue to
write Cobol that is a quarter of a century old.
 
If they use Cobol-85 then they should use END-~ and EVALUATE
and Functions (if they have the 89 addendum) and also short-
circuit evaluations.  Or they should at least be able to
recognise these because they will come across them.
 
Your idea that they should be avoided, and that knowledge of
them should be avoided is flawed.
 
 
> Richard, I have been examining code from compilers for a long
> time. I have been studying and programming in COBOL, and many
…[4 more quoted lines elided]…
> the beginning, ...
 
You really do come across as a ludite here.  The order of
evaluation of logical expression _is_ embodied in the Cobol
Standards and is thus guaranteed in any conforming compiler.
It is in the Cobol-85 standard, and in the 74 standard.  It
was also in the -68 standard but some changes were made in
respect of the order of evaluating NOT when going to -74.
 
If you had taken a few minutes looking at the specification of
Cobol instead of burying yourself in the machine code output from
some specific implementations you may have a better idea of
what constitutes standard Cobol.
 
> ... I would agree that you could test limits and end
> conditions in the same statement.
 
This is actually a somewhat different issue to that of 'order of
evaluation', but you seem to have them somewhat confused.
 
All compilers _are_ required (in order to be standard) to
follow the appropriate order of evaluation rules which you think
are missing.
 
The issue of whether bound checking can be used in the same
conditional as the use of the index is subject to
'short-circuiting' the evaluation, the correct ordering, while
important, is not enough.  This _is_ guaranteed in Cobol-85.
 
> But the fact is that there are still a lot of compilers out
> there which do not guarantee that.
 
You are referring to ANSI-74 and -68 compilers ?  These compilers
also do not have END-~, EVALUATE, reference notation, in-line
performs, and many other features.  Do you avoid all these too ?
 
In fact, if you had looked closely, the example was an in-line
perform.  This was obviously Cobol-85, it couldn't have been an
earlier standard, and so testing the bounds in the same condition
is entirely appropriate.
 
> And once code is written, who knows where it might end up?
> You assume that I avoid certain practices because I don't
> understand them.  The fact is that I avoid them because I
> do understand them, and I understand the ramifications of
> using them.
 
Well clearly not in this case.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
