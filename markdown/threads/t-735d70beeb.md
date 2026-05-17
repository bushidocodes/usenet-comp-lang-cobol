[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Scope Terminators

_17 messages · 10 participants · 1995-03_

---

### Scope Terminators

- **From:** "sdr..." <ua-author-17087487@usenetarchives.gap>
- **Date:** 1995-03-05T11:09:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3jcnn3$kl6@news1.delphi.com>`

```
I followed, with great interest, the recent discussion on the relative
merits of scope-terminators in COBOL-85. I had been sold on them until
I ran into a problem posed by the following code fragment:


200-PROCESS-INPUT-RECORD.
IF ADDITION MOVE TRANSACTION-RECORD TO ADD-MASTER-RECORD
ELSE IF PAYMENT OR CHARGE MOVE TRANSACTION-RECORD
TO CHANGE-MASTER-RECORD
ELSE MOVE TRANSACTION-RECORD
TO DELETE-MASTER-RECORD
END-IF

The first record is a payment and this code sends the program into a
continuous loop. I solved the problem by deleting the scope-terminator
and using a period:

200-PROCESS-INPUT-RECORD.
IF ADDITION MOVE TRANSACTION-RECORD TO ADD-MASTER-RECORD
ELSE IF PAYMENT OR CHARGE MOVE TRANSACTION-RECORD
TO CHANGE-MASTER-RECORD
ELSE MOVE TRANSACTION-RECORD
TO DELETE-MASTER-RECORD.

The program runs fine like this. Any ideas on what I'm doing wrong.

Thanks in advance.

Steven Drake, TSUD, Dothan, Alabama
Internet: sdr··.@del··i.com or ste··.@a··.com
Entered: 03/05/95 at 09:37 CST
```

#### ↳ Re: Scope Terminators

- **From:** "t..." <ua-author-15731627@usenetarchives.gap>
- **Date:** 1995-03-05T13:31:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-735d70beeb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3jcnn3$kl6@news1.delphi.com>`
- **References:** `<3jcnn3$kl6@news1.delphi.com>`

```
In article <3jcnn3$k.··.@new··i.com>, SDR··.@Del··i.com (Steven R. Drake) says:
› 
› I followed, with great interest, the recent discussion on the relative
…[30 more quoted lines elided]…
›                                                                         

I would start with better indentation then it would be easy to see that an end-if is missing.

200-PROCESS-INPUT-RECORD.
IF ADDITION
MOVE TRANSACTION-RECORD TO ADD-MASTER-RECORD
ELSE
IF PAYMENT OR CHARGE
MOVE TRANSACTION-RECORD TO CHANGE-MASTER-RECORD
ELSE
MOVE TRANSACTION-RECORD TO DELETE-MASTER-RECORD
END-IF *>missing end-if
END-IF

Here it is easy to see that there is an end-if missing. I don't see why your statement would
cause a loop, but then again I haven't seen the perform statement or what code follows.

Tim Mitchell
```

#### ↳ Re: Scope Terminators

- **From:** "richard_..." <ua-author-17073823@usenetarchives.gap>
- **Date:** 1995-03-06T00:40:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-735d70beeb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3jcnn3$kl6@news1.delphi.com>`
- **References:** `<3jcnn3$kl6@news1.delphi.com>`

```
› 
› 200-PROCESS-INPUT-RECORD.
…[7 more quoted lines elided]…
› [alternate deleted]
 
› The program runs fine like this.  Any ideas on what I'm doing wrong.

You need two END-IFs, one for each IF.
```

#### ↳ Re: Scope Terminators

- **From:** "martyn woerner" <ua-author-15047705@usenetarchives.gap>
- **Date:** 1995-03-06T04:52:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-735d70beeb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3jcnn3$kl6@news1.delphi.com>`
- **References:** `<3jcnn3$kl6@news1.delphi.com>`

```
SDR··.@Del··i.com (Steven R. Drake) wrote:
› 
› I followed, with great interest, the recent discussion on the relative
…[10 more quoted lines elided]…
›      END-IF

If you have two IFs then you need two END-IFs, but why not consider
evaluate?

200-PROCESS-INPUT-RECORD.
EVALUATE TRUE
WHEN ADDITION MOVE TRANSACTION-RECORD TO ADD-MASTER-RECORD
WHEN PAYMENT
WHEN CHARGE MOVE TRANSACTION-RECORD TO CHANGE-MASTER-RECORD
WHEN OTHER MOVE TRANSACTION-RECORD TO DELETE-MASTER-RECORD
END-EVALUATE
```

##### ↳ ↳ Re: Scope Terminators

- **From:** "sdr..." <ua-author-17087487@usenetarchives.gap>
- **Date:** 1995-03-08T00:12:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-735d70beeb-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-735d70beeb-p4@usenetarchives.gap>`
- **References:** `<3jcnn3$kl6@news1.delphi.com> <gap-735d70beeb-p4@usenetarchives.gap>`

```

m>If you have two IFs then you need two END-IFs, but why not consider
m>evaluate?

m> 200-PROCESS-INPUT-RECORD.
m> EVALUATE TRUE
m> WHEN ADDITION MOVE TRANSACTION-RECORD TO ADD-MASTER-RECORD
m> WHEN PAYMENT
m> WHEN CHARGE MOVE TRANSACTION-RECORD TO CHANGE-MASTER-RECORD
m> WHEN OTHER MOVE TRANSACTION-RECORD TO DELETE-MASTER-RECORD
m> END-EVALUATE

Believe it or not, in my intro course I was advised to avoid using the
evaluate because it might "give me problems". This was a comment
directed at the class as a whole, and I think the intent was to simplify
things for some of the folks who were floundering (several didn't make
it). Someone else advised this path to me through email so I dusted off
the intro book and was impressed in the options this offers. As I said
in another post, all the comments and direction have helped me to learn
a great deal in the last 24 hours. An understanding of the EVALUATE
statement was probably my biggest gain.

Welburn's text does not even explain linear nested conditionals with
scope terminators...he just recommends the use of EVALUATE.

Steven Drake, TSUD, Dothan, Alabama
Internet: sdr··.@del··i.com or ste··.@a··.com
Entered: 03/07/95 at 22:33 CST
```

#### ↳ Re: Scope Terminators

- **From:** "bwil..." <ua-author-12789603@usenetarchives.gap>
- **Date:** 1995-03-06T13:19:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-735d70beeb-p6@usenetarchives.gap>`
- **In-Reply-To:** `<3jcnn3$kl6@news1.delphi.com>`
- **References:** `<3jcnn3$kl6@news1.delphi.com>`

```
SDR··.@Del··i.com (Steven R. Drake) writes:

› I followed, with great interest, the recent discussion on the relative
› merits of scope-terminators in COBOL-85.  I had been sold on them until
› I ran into a problem posed by the following code fragment:
 
 
› 200-PROCESS-INPUT-RECORD.
›     IF ADDITION MOVE TRANSACTION-RECORD TO ADD-MASTER-RECORD
…[4 more quoted lines elided]…
›     END-IF
 
› The first record is a payment and this code sends the program into a
› continuous loop.  I solved the problem by deleting the scope-terminator
› and using a period:
 
› 200-PROCESS-INPUT-RECORD.
›     IF ADDITION MOVE TRANSACTION-RECORD TO ADD-MASTER-RECORD
…[3 more quoted lines elided]…
›         TO DELETE-MASTER-RECORD.
 
› The program runs fine like this.  Any ideas on what I'm doing wrong.
 
› Thanks in advance.
 
› Steven Drake, TSUD, Dothan, Alabama
› Internet: sdr··.@del··i.com or ste··.@a··.com
› Entered: 03/05/95 at 09:37 CST
›                                                                         
Try:

200-PROCESS-INPUT-RECORD.
IF ADDITION
MOVE TRANSACTION-RECORD TO ADD-MASTER-RECORD
ELSE
IF PAYMENT OR CHARGE
MOVE TRANSACTION-RECORD TO CHANGE-MASTER-RECORD
ELSE
MOVE TRANSACTION-RECORD TO DELETE-MASTER-RECORD
END-IF
END-IF.

One must pair each scope-delimiter with its corresponding
verb. You might get away with a period on the first "END-IF"
delimiter if the entire conditional is not embedded in a
instream loop and/or conditional statement. I perfer avoiding
possible maintenance confusion by strict pairing and indenting
the "ELSE IF" conditionals to clearly show the structure.

Hope this helps,
Boyce Williams
```

##### ↳ ↳ Re: Scope Terminators

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-03-07T20:12:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-735d70beeb-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-735d70beeb-p6@usenetarchives.gap>`
- **References:** `<3jcnn3$kl6@news1.delphi.com> <gap-735d70beeb-p6@usenetarchives.gap>`

```
The style I use for ELSE IF in COBOL, given the peculiarity of the syntax
is

PERFORM
IF ...
...
ELSE IF ...
...
ELSE IF ...
...
...
ELSE
...
END-PERFORM

It is really unfortunate to indent each ELSE IF, since there can be a whole
sequence of them, and logically they are at the same level in the structure.
```

##### ↳ ↳ Re: Scope Terminators

- **From:** "sdr..." <ua-author-17087487@usenetarchives.gap>
- **Date:** 1995-03-08T00:10:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-735d70beeb-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-735d70beeb-p6@usenetarchives.gap>`
- **References:** `<3jcnn3$kl6@news1.delphi.com> <gap-735d70beeb-p6@usenetarchives.gap>`

```

Many thanks to all who offered advice, both by email and in the
newsgroup...many have offered up the following:

200-PROCESS-INPUT-RECORD.
IF ADDITION
MOVE TRANSACTION-RECORD TO ADD-MASTER-RECORD
ELSE
IF PAYMENT OR CHARGE
MOVE TRANSACTION-RECORD TO CHANGE-MASTER-RECORD
ELSE
MOVE TRANSACTION-RECORD TO DELETE-MASTER-RECORD
END-IF
END-IF

I have learned a great deal from all of you...two things have been
hammered home the hardest:

1. Ensure that each IF is paired with a scope-terminator and
2. Use indentation to ease readability.

I tried something akin to the code above with IBM VS COBOL:

200-PROCESS-INPUT-RECORD.
IF ADDITION
MOVE TRANSACTION-RECORD TO ADD-MASTER-RECORD
ELSE
IF PAYMENT OR CHARGE
MOVE TRANSACTION-RECORD TO CHANGE-MASTER-RECORD
END-IF
ELSE
MOVE TRANSACTION-RECORD TO DELETE-MASTER-RECORD
END-IF

yet this generates a compile error: Trailing END-IF is not paired with
an IF. I hate to be obtuse, but I don't see the difference.

Steven Drake, TSUD, Dothan, Alabama
Internet: sdr··.@del··i.com or ste··.@a··.com
Entered: 03/07/95 at 22:23 CST
```

###### ↳ ↳ ↳ Re: Scope Terminators

- **From:** "s..." <ua-author-599642@usenetarchives.gap>
- **Date:** 1995-03-08T08:52:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-735d70beeb-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-735d70beeb-p8@usenetarchives.gap>`
- **References:** `<3jcnn3$kl6@news1.delphi.com> <gap-735d70beeb-p6@usenetarchives.gap> <gap-735d70beeb-p8@usenetarchives.gap>`

```
In article <3jje8m$p.··.@new··i.com>, SDR··.@Del··i.com says...

›    200-PROCESS-INPUT-RECORD.
›        IF ADDITION
…[10 more quoted lines elided]…
› an IF.  I hate to be obtuse, but I don't see the difference.

and so it should. ADDITION is condition with only two states, true or
false.

"IF ADDITION" covers the TRUE state whereas the first ELSE covers FALSE.
So what does the second ELSE cover?

Your original code of...

›    200-PROCESS-INPUT-RECORD.
›        IF ADDITION
…[7 more quoted lines elided]…
›        END-IF

... had the second else as part of the "IF PAYMENT OR CHARGE" condition
meaning that the statement "MOVE TRANSACTION-RECORD TO
DELETE-MASTER-RECORD" was only executed if ADDITION was FALSE and
"PAYMENT OR CHARGE" was FALSE. This code is syntacically correct but
maybe not the logic you were after.

I'm assuming that ADDITION, PAYMENT and CHARGE are Level 88 items and
that you have these set up ok. If they aren't, you need to relook up
level 88 in your manual to see how it works or change your statements to
IF ADDITION = "Y" or whatever you are using to indicate ADDITION is TRUE.

Indenting and not using periods unless you have to is a step in the right
direction though.

Shaun.
```

###### ↳ ↳ ↳ Re: Scope Terminators

- **From:** "ggra..." <ua-author-17087605@usenetarchives.gap>
- **Date:** 1995-03-08T12:53:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-735d70beeb-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-735d70beeb-p8@usenetarchives.gap>`
- **References:** `<3jcnn3$kl6@news1.delphi.com> <gap-735d70beeb-p6@usenetarchives.gap> <gap-735d70beeb-p8@usenetarchives.gap>`

```
Steven R. Drake (SDR··.@Del··i.com) wrote:

: ...

: I tried something akin to the code above with IBM VS COBOL:

: 200-PROCESS-INPUT-RECORD.
: IF ADDITION
: MOVE TRANSACTION-RECORD TO ADD-MASTER-RECORD
: ELSE
: IF PAYMENT OR CHARGE
: MOVE TRANSACTION-RECORD TO CHANGE-MASTER-RECORD
: END-IF
: ELSE
: MOVE TRANSACTION-RECORD TO DELETE-MASTER-RECORD
: END-IF

: yet this generates a compile error: Trailing END-IF is not paired with
: an IF. I hate to be obtuse, but I don't see the difference.

That's true. Use indention to indicate pairing ;-)

200-PROCESS-INPUT-RECORD.
IF ADDITION
MOVE TRANSACTION-RECORD TO ADD-MASTER-RECORD
ELSE
IF PAYMENT OR CHARGE
MOVE TRANSACTION-RECORD TO CHANGE-MASTER-RECORD
ELSE
MOVE TRANSACTION-RECORD TO DELETE-MASTER-RECORD
END-IF
END-IF

I'm assuming the above is what you intented, the problem was the second
ELSE statement which didn't 'belong' to any IF.

You'll also note that I line my END-IF's up with the last line of the
inner block, this isn't generally how you see it (usually folks line it
up with the last line of the outer block), but I think it reads better.

The most important thing is that you follow the same indention rules
all the time (be consistent) ... of course sometimes company policy
gets in the way.

As has been pointed out an EVALUATE might work better, but either is
fine for a few items.
```

###### ↳ ↳ ↳ Re: Scope Terminators

_(reply depth: 4)_

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-03-09T19:11:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-735d70beeb-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-735d70beeb-p10@usenetarchives.gap>`
- **References:** `<3jcnn3$kl6@news1.delphi.com> <gap-735d70beeb-p6@usenetarchives.gap> <gap-735d70beeb-p8@usenetarchives.gap> <gap-735d70beeb-p10@usenetarchives.gap>`

```
Greg Granger's idiosyncratic positioning of END-IF lines is a pretty good
example of how important it is not to let individual programmers decide
what they think looks better when it comes to coding style. I have no doubt
that Greg finds it pleasanter, you can get used to anything, and once you
are used to it, it seems right.

But to anyone used to the more standard style (END-IF lined up under IF),
it is very strange looking and quite confusing (quite likely Greg finds
the "standard" style confusing to him).

Furthermore, when people adopt different styles like this in a project,
you get a code "ownership" phenomenon where people don't like to work on
any code but their own.

So, a good object lesson here, standardize coding style!

One of the nice things in Ada 95 (true of Ada 83 too) is that the reference
manual stongly suggested a layout style, and for many basic things like
indentation, nearly *all* Ada programmers follow this style, avoiding this'
kind of variation.
```

###### ↳ ↳ ↳ Re: Scope Terminators

_(reply depth: 5)_

- **From:** "ggra..." <ua-author-17087605@usenetarchives.gap>
- **Date:** 1995-03-13T12:21:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-735d70beeb-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-735d70beeb-p11@usenetarchives.gap>`
- **References:** `<3jcnn3$kl6@news1.delphi.com> <gap-735d70beeb-p6@usenetarchives.gap> <gap-735d70beeb-p8@usenetarchives.gap> <gap-735d70beeb-p10@usenetarchives.gap> <gap-735d70beeb-p11@usenetarchives.gap>`

```
Robert Dewar (de··.@cs.··u.edu) wrote:
: Greg Granger's idiosyncratic positioning of END-IF lines is a pretty good
: example of how important it is not to let individual programmers decide
: what they think looks better when it comes to coding style. I have no doubt
: that Greg finds it pleasanter, you can get used to anything, and once you
: are used to it, it seems right.

: But to anyone used to the more standard style (END-IF lined up under IF),
: it is very strange looking and quite confusing (quite likely Greg finds
: the "standard" style confusing to him).


Nope, I grok "standard style" just fine too.
Just because the first guy did it wrong doesn't mean I have to ;-)
```

###### ↳ ↳ ↳ Re: Scope Terminators

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-03-09T07:26:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-735d70beeb-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-735d70beeb-p8@usenetarchives.gap>`
- **References:** `<3jcnn3$kl6@news1.delphi.com> <gap-735d70beeb-p6@usenetarchives.gap> <gap-735d70beeb-p8@usenetarchives.gap>`

```
Steve wonders why:

200-PROCESS-INPUT-RECORD.
IF ADDITION
MOVE TRANSACTION-RECORD TO ADD-MASTER-RECORD
ELSE
IF PAYMENT OR CHARGE
MOVE TRANSACTION-RECORD TO CHANGE-MASTER-RECORD
END-IF
ELSE
MOVE TRANSACTION-RECORD TO DELETE-MASTER-RECORD
END-IF

does not work. The trouble here is that the second ELSE does not go with
any IF. Each ELSE must go with one IF. I assume the reason that you tried
this, as opposed to

IF ADDITION
MOVE TRANSACTION-RECORD TO ADD-MASTER-RECORD
ELSE
IF PAYMENT OR CHARGE
MOVE TRANSACTION-RECORD TO CHANGE-MASTER-RECORD
ELSE
MOVE TRANSACTION-RECORD TO DELETE-MASTER-RECORD
END-IF
END-IF

is that you don't like the indentation. Indeed if you had ten ELSE-IF
sequences, you would like the indentation even less! Here again is how
I would write the above:

PERFORM
IF ADDITION
MOVE TRANSACTION-RECORD TO ADD-MASTER-RECORD
ELSE IF PAYMENT OR CHARGE
MOVE TRANSACTION-RECORD TO CHANGE-MASTER-RECORD
ELSE
MOVE TRANSACTION-RECORD TO DELETE-MASTER-RECORD
END-PERFORM

any number of ELSE IF sequences can be added to this without indenting.
This corresponds to the normal use of the else if in a language that has
a proper else if construct, For instance, in Ada-95 the above would be
written

if Addition then
Move (Transaction_Record, Add_Master_Record);
elsif Payment or Change then
Move (Transaction_Record, Change_Master_Record);
else
Move (Transaction_Record, Delete_Master_Record);
end if;

Notice that we use elsif in the Ada 95, not else if. But unfortunately
COBOL has no equivalent to the elsif. The PERFORM however closes off
all open IF's so that's how to get the same effect in COBOL. You can
also consider using Evaluate.
```

###### ↳ ↳ ↳ Re: Scope Terminators

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-03-09T15:03:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-735d70beeb-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-735d70beeb-p8@usenetarchives.gap>`
- **References:** `<3jcnn3$kl6@news1.delphi.com> <gap-735d70beeb-p6@usenetarchives.gap> <gap-735d70beeb-p8@usenetarchives.gap>`

```
"END-IF is illegal before an ELSE"

where did this rule come from???
```

#### ↳ Re: Scope Terminators

- **From:** "charles godwin" <ua-author-2829225@usenetarchives.gap>
- **Date:** 1995-03-06T20:33:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-735d70beeb-p15@usenetarchives.gap>`
- **In-Reply-To:** `<3jcnn3$kl6@news1.delphi.com>`
- **References:** `<3jcnn3$kl6@news1.delphi.com>`

```
SDR··.@Del··i.com (Steven R. Drake) wrote:
› 
› I followed, with great interest, the recent discussion on the relative
…[24 more quoted lines elided]…
› 

The problem is you have two ifs and only one end-if add a second end-if.

The period acts as a definitive scope delimiter.

› Thanks in advance.
› 
…[3 more quoted lines elided]…
›
```

#### ↳ Re: Scope Terminators

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-03-06T21:10:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-735d70beeb-p16@usenetarchives.gap>`
- **In-Reply-To:** `<3jcnn3$kl6@news1.delphi.com>`
- **References:** `<3jcnn3$kl6@news1.delphi.com>`

```
Regarding the problem with ELSE IF, COBOL syntax has a serious mistake
here. Generally languages are designed with either a single statement
after compound statements like IF, using BEGIN/EMD or somesuch for
grouping (C, Pascal, Algol-60 are examples) of this approach, or they
use scope terminators (Algol-68, Ada, and COBOL are examples of this
second approach).

However, if you use scope terminators, then you definitely need a composite
else if operation (In Ada it is ELSIF, in Algol-68 it is ELIF). COBOL needs
such a composite, otherwise you get a pile of END-IF's waiting. The obvious
syntax would be ELSE-IF.

I can't understand how this mistake was made, it seems such an obvious
oversight.
```

#### ↳ Re: Scope Terminators

- **From:** "t..." <ua-author-7864391@usenetarchives.gap>
- **Date:** 1995-03-06T23:57:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-735d70beeb-p17@usenetarchives.gap>`
- **In-Reply-To:** `<3jcnn3$kl6@news1.delphi.com>`
- **References:** `<3jcnn3$kl6@news1.delphi.com>`

```
Steven R. Drake (SDR··.@Del··i.com) wrote:
: I followed, with great interest, the recent discussion on the relative
: merits of scope-terminators in COBOL-85. I had been sold on them until
: I ran into a problem posed by the following code fragment:


: 200-PROCESS-INPUT-RECORD.
: IF ADDITION MOVE TRANSACTION-RECORD TO ADD-MASTER-RECORD
: ELSE IF PAYMENT OR CHARGE MOVE TRANSACTION-RECORD
: TO CHANGE-MASTER-RECORD
: ELSE MOVE TRANSACTION-RECORD
: TO DELETE-MASTER-RECORD
: END-IF

: The first record is a payment and this code sends the program into a
: continuous loop. I solved the problem by deleting the scope-terminator
: and using a period:

: 200-PROCESS-INPUT-RECORD.
: IF ADDITION MOVE TRANSACTION-RECORD TO ADD-MASTER-RECORD
: ELSE IF PAYMENT OR CHARGE MOVE TRANSACTION-RECORD
: TO CHANGE-MASTER-RECORD
: ELSE MOVE TRANSACTION-RECORD
: TO DELETE-MASTER-RECORD.

: The program runs fine like this. Any ideas on what I'm doing wrong.

Yes - Try reading your code like:

200-PROCESS-INPUT-RECORD.
IF ADDITION
MOVE TRANSACTION-RECORD TO ADD-MASTER-RECORD
ELSE
IF PAYMENT OR CHARGE
MOVE TRANSACTION-RECORD TO CHANGE-MASTER-RECORD
ELSE
MOVE TRANSACTION-RECORD TO DELETE-MASTER-RECORD
END-IF
END-IF

Hence you were missing an End-if. Have FUN!!


/------------------------------------------------------------------------¥
| Tim Dawson t.··.@wer··t.au |
¥------------------------------------------------------------------------/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
