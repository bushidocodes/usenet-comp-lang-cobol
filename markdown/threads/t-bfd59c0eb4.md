[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VS COBOL Problem

_5 messages · 4 participants · 1997-07 → 1997-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### VS COBOL Problem

- **From:** "bo.sc..." <ua-author-3577038@usenetarchives.gap>
- **Date:** 1997-07-31T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<870474198@stackbbs.xs4all.nl>`

```

-=> Quoting A.··.@it.··u.au to All <=-

At> !!!! HELP !!!!

At> I am using VS COBOL in compiling my program and it doesn't recognise
At> the following.
At> 05 Totals occurs 14 times.
At> 10 Amount pic s9(13)v99 comp-3 value +0.


At> I am tring to initialise every cell in the table to be zero value. It
At> compiles ok without the "VALUE +0". My appreciate if you can help me.

At> Please email me at alv··.@tre··v.au.

Sorry, can't email from this QWK mailer ;)
I think we need to see more of your data division.
You start at level 05, and then up.
How do we know if it isn't a redefine of something?
Please show your code from level 01.

Bo.

ps, with VS COBOL, you probably don't mean Wang VS Cobol right?
```

#### ↳ Re: VS COBOL Problem

- **From:** "luiz defreitas" <ua-author-17071420@usenetarchives.gap>
- **Date:** 1997-08-02T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfd59c0eb4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<870474198@stackbbs.xs4all.nl>`
- **References:** `<870474198@stackbbs.xs4all.nl>`

```

OK,

First rule with a table. DO NOT USE A VALUE STATEMENT!!!!!!!

I say this from expirenece and

Second rule, DO NOT and I MEAN, DO NOT MOVE SPACES TO THE GROUP LEVEL OF
THE TABLE

because.....The code generated for the move will cause a program to run
long AND I MEAN VERY LONG!

What I suggest is two techniques: (You choose!)

#1 - HIGHLY EFFICIENT!

Do not clear the entire table at all unless you have too.
Instead keep a counter of the occurances that you need to use. This
will not be an option is you know that the program will use the
all occurances all the time. But if the number of occurnaces vary,
then you may want to consider this option.

#2 - PERFORM VARYING

Use a perform varying to clear the table, occurance by occurance.


#3 - Create a 'CLEAR AREA' that is defined exactly as one of the
occurances.

In your example you could code:

01 CLEAR-AMT PIC s9(13)v99 comp-3 value +0.

Then move CLEAR-AMT TO TOTALS

Because CLEAR-AMT is only 8 bytes the move statement will propigate

X'000000000000000C' in position 1-8, then 9-16 etc.

Good luck!
```

##### ↳ ↳ Re: VS COBOL Problem

- **From:** "luiz defreitas" <ua-author-17071420@usenetarchives.gap>
- **Date:** 1997-08-02T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfd59c0eb4-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfd59c0eb4-p2@usenetarchives.gap>`
- **References:** `<870474198@stackbbs.xs4all.nl> <gap-bfd59c0eb4-p2@usenetarchives.gap>`

```

Regarding #3 in my org response,

A better example provided by Jim is as follows:

01 TABLE-1-INIT.
05 FILLER PIC 9(05) VALUE 12345.
05 FILLER PIC X(05) VALUE 'ABCDE'.
05 TABLE-1.
10 TABLE-1-ENTRY OCCURS 5 TIMES.
15 TABLE-1-ITEM-1 PIC 9(05).
15 TABLE-1-ITEM-2 PIC X(05).

then...

MOVE TABLE-1-INIT TO TABLE-1.
```

#### ↳ Re: VS COBOL Problem

- **From:** "john hofstad-parkhill" <ua-author-6589075@usenetarchives.gap>
- **Date:** 1997-08-09T23:47:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfd59c0eb4-p4@usenetarchives.gap>`
- **In-Reply-To:** `<870474198@stackbbs.xs4all.nl>`
- **References:** `<870474198@stackbbs.xs4all.nl>`

```

As Luiz points out, you can't use the VALUE clause as coded in the example,
never have been able to.

Also, not noted by you but as a reminder, group data items are
alphanumeric, thus move zero(s) to group above TOTALS would fill it with
display decimal zeros, not the same as packed (COMP-3), and would not work.

He is not correct in his assertion that moving spaces introduces
unnecessary run times, the time involved is trivial compared to any indexed
or subscripted loop you can generate.

Depending on the compiler and options and the size of the group item a move
figurative-constant can be very efficient.

Some compilers, VS COBOL in particular, complain about overlapping moves.
Exact reasons must be referred to the compiler manual. However, his example
of a overlapping move is still a viable and valuable hint.

Traditional methods remain the tiresome.

05 TABLE-DATA.
10 FILLER PIC S9(13)V99 COMP-3 VALUE ZERO.
10 FILLER PIC S9(13)V99 COMP-3 VALUE ZERO.
...

05 TOTALS REDEFINES TABLE-DATA.
10 AMOUNT OCCURS .. TIMES PIC S9(13)V99 COMP-3.

And finally, subscript -vs- index name (INDEXED BY).

Most compilers maintain the index name in two values, the relative-to-one
value referenced in the code, and the computed, last known, offset value of
the index name. Thus procedure references using the index name can use the
already-stored offset value. Few compilers can generate the same efficiency
with subscripts. To my knowledge there is not a volitale storage class in
COBOL, thus the compiler must re-calculate the offset into the array
(table) for each subscript reference.

This is not "hard and fast", like many things in programming it's rather a
rule of thumb.

There are times where trade-off's dictate the use of a subscript. Again, if
you can use an index name you should.
```

##### ↳ ↳ Re: VS COBOL Problem

- **From:** "arn b" <ua-author-2587922@usenetarchives.gap>
- **Date:** 1997-08-13T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfd59c0eb4-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfd59c0eb4-p4@usenetarchives.gap>`
- **References:** `<870474198@stackbbs.xs4all.nl> <gap-bfd59c0eb4-p4@usenetarchives.gap>`

```

When faced with a performance situation I always turn on the assembler
list and look at the generated code. One rule of thumb is when you see a
COBOL subroutine being called you got some slow code. Minor picture
adjustments {s9(9) comp vs s9(8) comp}, varying compiler options {TRUNC
in particular} or keeping all your arithmetic fields in COMP-3 or COMP
format can have amazing results in the object code.

My favorite example was

03 wk01-counter pic s9(9) comp.

Add 1 to wk01-counter.

I expected a load; add and store. The compiler generated about 30
instructions to accomplish the task including multiplies, divides and
shifts. Changing the picture to S9(8) comp and adjusting the Trunc
option eventually corrected the problem.

One other point I want to make; when moving space to a large array or
data area COBOL II usually generates a MVCL (MOVE Character Long) which
is very efficient. Just be sure it is not using one of those slow
subroutines.

**********************************************************
Please remove NOJUNK. from return address or click
here to mailto:AR··.@mys··f.com
***********************************************************
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
