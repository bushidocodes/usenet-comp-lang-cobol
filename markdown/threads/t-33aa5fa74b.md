[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# GOTO-less C form rapes COBOL

_23 messages · 17 participants · 1996-11 → 1996-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### GOTO-less C form rapes COBOL

- **From:** "bovine remailer" <ua-author-463748@usenetarchives.gap>
- **Date:** 1996-11-27T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9611281432.AA13249@cow.net>`

```

I was recently tasked to make an enhancement to a
COBOL program. This meant changing one copy file
that is about 250 lines long. But what started
out to be a simple change became a nightmare.

The whole copy file was one IF statement. It had
a total of 25 IF's inside of it, some nested to
the 7th level. Only one sentence (an ADD) was in
the first level, all of the remaining code was a
part of it's ELSE clause.

This is the worst case of spaghetti code I've
seen in many years.

The enhancement I was tasked with entailed adding
2 more IF statements in different places. I
could not tell what level of IF I was in at any
particular place. I could not add my
enhancements until I could understand the level
of all IF's. I risked throwing off the whole
nesting structure of the IF's below them
otherwise.

I wound up re-formatting and re-writing the
entire copy file just so I could read it! After
this was done I could add my enhancements to get
the expected results. This simple task took 8
times (!) longer than expected.

True to C form there were no explicit GO TO's
anywhere in the original code. My re-format and
re-write inserted GO TO's where appropriate to
break the IF's down to a maintainable level and
structure. After this was done, my enhancements
were easy.

I tracked down the author of the original code and
casually asked him if he had ever done C code.
He said he was DEEP (emphasis his) into C code.

I believe in top down structured code more than
anybody I know. But this *IS NOT* accomplished
by abolishing the GO TO statement. What you wind
up with is COBOL code that is just as cryptic as
C. C programmers throw out and re-write routines
that need to be enhanced as a matter of course.
Now I can see why.

You coders that believe that you can "quick fix"
the maintainability of all the programs in the
world by abolishing the GO TO can spindle, fold,
mutilate, and shove it in your (pardon my French
expletive deleted) a: drive.


- Ol' Bud

(opinions expressed, though crankier in my old
age, are not necessarily those of my employer)
```

#### ↳ Re: GOTO-less C form rapes COBOL

- **From:** "geir knaplund" <ua-author-6588924@usenetarchives.gap>
- **Date:** 1996-11-28T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<9611281432.AA13249@cow.net>`
- **References:** `<9611281432.AA13249@cow.net>`

```

Bovine Remailer wrote:
›
---- snip ---
Very good example cut..
--- end snip ---
› 
›  You coders that believe that you can "quick fix"
…[8 more quoted lines elided]…
›    age, are not necessarily those of my employer)


Words of wisdom from a practical person!!!!

I sure do hate ridicilous IF/ELSE-constructs written by so
called programmers to avoid GOTO's..
(The same goes for hopelessly complex EVALAUTE-constructs!!!)

By the way,.. I try to write C just as readable as I write my COBOL! :-)


---------------------
kna··.@s··.no
---------------------
```

##### ↳ ↳ Re: GOTO-less C form rapes COBOL

- **From:** "rune..." <ua-author-15584783@usenetarchives.gap>
- **Date:** 1996-11-28T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-33aa5fa74b-p2@usenetarchives.gap>`
- **References:** `<9611281432.AA13249@cow.net> <gap-33aa5fa74b-p2@usenetarchives.gap>`

```

On Fri, 29 Nov 1996 03:45:17 +0100, Geir Knaplund wrote:

› Bovine Remailer wrote:
››  You coders that believe that you can "quick fix"
…[11 more quoted lines elided]…
› By the way,.. I try to write C just as readable as I write my COBOL! :-)

I have never so far had to use any GO TO, even if I have wanted to use it. This
counts for both C and Cobol. But I have to admit that I've used it in DOS
batch-files :-)
There is always a nicer way around using EVALUATE and switches. I also found
that the way the test is done (I always do positive testing) gives no
limitations on writing nice code.

My point is that lazyness and unwillingness in changing to doing things a new
way is more important here than actually reading/rebuilding the code.
```

###### ↳ ↳ ↳ Re: GOTO-less C form rapes COBOL

- **From:** "joseph lenz" <ua-author-17071704@usenetarchives.gap>
- **Date:** 1996-11-29T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-33aa5fa74b-p3@usenetarchives.gap>`
- **References:** `<9611281432.AA13249@cow.net> <gap-33aa5fa74b-p2@usenetarchives.gap> <gap-33aa5fa74b-p3@usenetarchives.gap>`

```

blah blah blah
```

###### ↳ ↳ ↳ Re: GOTO-less C form rapes COBOL

- **From:** "steve wolfe" <ua-author-733217@usenetarchives.gap>
- **Date:** 1996-11-29T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-33aa5fa74b-p3@usenetarchives.gap>`
- **References:** `<9611281432.AA13249@cow.net> <gap-33aa5fa74b-p2@usenetarchives.gap> <gap-33aa5fa74b-p3@usenetarchives.gap>`

```

Rune Meier wrote:
› 
› On Fri, 29 Nov 1996 03:45:17 +0100, Geir Knaplund  wrote:
…[24 more quoted lines elided]…
› way is more important here than actually reading/rebuilding the code.

Well, I think that readibility comes into play as well. If I code a
perform, I expect the control to return to the next executable
instruction after the perform has completed. That sounds great, but what
if I'm performing an abend routine? The cobol standard doesn't read that
control should return to the next executable instruction following the
perform except in the case that the programmer is using a perform in
place of a goto for personal preference. If you don't expect to come
back to a point of code use a goto to transfer control. It doesn't upset
the gods of structured programming to use a goto judiciously, nor does
it imply a lazyness or unwillingness to change. Hey, I'm all for new
procedures and methods, but maint. is king in this business and reading
code is very important.

just my two cents.

***************************************************************************
          "Thought by many to be endangered, the lesser spotted
                     COBOL programmer makes a comeback". 

email: prg··.@ep··x.net
url  : http://www.epix.net/~prgsdw
***************************************************************************
```

#### ↳ Re: GOTO-less C form rapes COBOL

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1996-11-28T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p6@usenetarchives.gap>`
- **In-Reply-To:** `<9611281432.AA13249@cow.net>`
- **References:** `<9611281432.AA13249@cow.net>`

```



›  I believe in top down structured code more than
›  anybody I know.  But this *IS NOT* accomplished
…[12 more quoted lines elided]…
› 

While I agree that multiple levels of nested If statements can be a
nightmare, I don't agree that inserting the GO TO's is the best solution.
Judicious use of IF and END-IF can make the same code very readable and
easy to modify. It was poorly written to begin with, but could have been
cleaned up with some other method than the insertion of GO TO's. (I assume
you had to add a label to go to also).

One thing you mentioned was the fact that nearly all the code was included
in the ELSE. I assume this was the original author's attempt to avoid a
"NOT". Perhaps reversing the if would have cleaned things up for you.

This code may have been written for a compiler where END-IF and END-PERFORM
were not supported. I have such a program with a 500 line if statment with
a lot of continues. I would have liked to split it up, but the resulting
object code exceeded the code segment. Keeping them all in the one if
statment created smaller code.
```

##### ↳ ↳ Re: GOTO-less C form rapes COBOL

- **From:** "mike childers" <ua-author-6588922@usenetarchives.gap>
- **Date:** 1996-12-08T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-33aa5fa74b-p6@usenetarchives.gap>`
- **References:** `<9611281432.AA13249@cow.net> <gap-33aa5fa74b-p6@usenetarchives.gap>`

```

I am amazed to this cry about goto less programs.
I never meet a goto that I didn't wanted to delete. Yes, it takes a
little more time to create well structured programs. But in the long run
that code is better than the short cuts that you try to create in using
cheap goto statements.
I have been doing this a long time, I have never really seen a well
structured program that contains a GOTO in it.

Hope you change your mind.
by the way Cobol programmers always create better data elements than
'C' programmers. That's because we believe our code will be around for more
that
1 or 2 years.

Mike Childers

Thane Hubbell wrote in article
<01bbde00$cb69dea0$42f548a6@thane-hubbell>...
› 
› 
…[17 more quoted lines elided]…
› nightmare, I don't agree that inserting the GO TO's is the best solution.
 
› Judicious use of IF and END-IF can make the same code very readable and
› easy to modify.  It was poorly written to begin with, but could have been
…[17 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: GOTO-less C form rapes COBOL

- **From:** "bent hoff s��rensen" <ua-author-6585215@usenetarchives.gap>
- **Date:** 1996-12-09T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-33aa5fa74b-p7@usenetarchives.gap>`
- **References:** `<9611281432.AA13249@cow.net> <gap-33aa5fa74b-p6@usenetarchives.gap> <gap-33aa5fa74b-p7@usenetarchives.gap>`

```

Why don't all you people quit discussing religion in a COBOL newsgroup ?

GOTO isn't a 'cheap' statement. It's a normal part of the COBOL language
wether you like it or not. Wether you use it or not.

Let's discuss COBOL. Let's help newcomers and other people with questions
about COBOL. And let's keep religion out of it.

Ben
A COBOL (and lots of other languages) programmer for almost 20 years.

mike childers skrev i artiklen
<01bbe589$f8995820$5919f8cc@mrc>...
› I am amazed to this cry about goto less programs.
› I never meet a goto that  I didn't wanted to delete.  Yes, it takes a
…[5 more quoted lines elided]…
› 
and a lot more
```

###### ↳ ↳ ↳ Re: GOTO-less C form rapes COBOL

- **From:** "soft..." <ua-author-6881452@usenetarchives.gap>
- **Date:** 1996-12-11T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-33aa5fa74b-p7@usenetarchives.gap>`
- **References:** `<9611281432.AA13249@cow.net> <gap-33aa5fa74b-p6@usenetarchives.gap> <gap-33aa5fa74b-p7@usenetarchives.gap>`

```

mike childers (m.··.@no··a.net) wrote:
: by the way Cobol programmers always create better data elements than
: 'C' programmers. That's because we believe our code will be around for more
: that
: 1 or 2 years.

Um.... okay, then why is the year 2000 such a problem for COBOL programs
and a non-issue for C programs which use the C standard library? :^)

Scott
```

###### ↳ ↳ ↳ Re: GOTO-less C form rapes COBOL

_(reply depth: 4)_

- **From:** "joseph lenz" <ua-author-17071704@usenetarchives.gap>
- **Date:** 1996-12-12T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-33aa5fa74b-p9@usenetarchives.gap>`
- **References:** `<9611281432.AA13249@cow.net> <gap-33aa5fa74b-p6@usenetarchives.gap> <gap-33aa5fa74b-p7@usenetarchives.gap> <gap-33aa5fa74b-p9@usenetarchives.gap>`

```

Scott McMahan - Softbase Systems wrote:
› 
› mike childers (m.··.@no··a.net) wrote:
…[8 more quoted lines elided]…
› Scott


The YEAR 2000 issue is not just a problem for COBOL programs. It a problem for any application that manages a
2 byte year instead of a 4 byte year.

Joseph Lenz
```

###### ↳ ↳ ↳ Re: GOTO-less C form rapes COBOL

_(reply depth: 5)_

- **From:** "dle..." <ua-author-1136377@usenetarchives.gap>
- **Date:** 1996-12-16T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-33aa5fa74b-p10@usenetarchives.gap>`
- **References:** `<9611281432.AA13249@cow.net> <gap-33aa5fa74b-p6@usenetarchives.gap> <gap-33aa5fa74b-p7@usenetarchives.gap> <gap-33aa5fa74b-p9@usenetarchives.gap> <gap-33aa5fa74b-p10@usenetarchives.gap>`

```

To borrow a phrase from the aviation arena:

"It ain't the machine, it's the man."

Good systems and programs are the products of good technicians; the
language is simply a vessel. Good technicians like good, quality oats
cost a fair price. Oats that have already been through the horse come
a lot cheaper.

dle··.@onr··p.net
96Б∙╗8'W 34Б∙╗11'N

BABYLON 5: Man's last best hope for QUALITY science fiction.
```

###### ↳ ↳ ↳ Re: GOTO-less C form rapes COBOL

_(reply depth: 4)_

- **From:** "dennis taylor" <ua-author-34211@usenetarchives.gap>
- **Date:** 1996-12-12T19:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-33aa5fa74b-p9@usenetarchives.gap>`
- **References:** `<9611281432.AA13249@cow.net> <gap-33aa5fa74b-p6@usenetarchives.gap> <gap-33aa5fa74b-p7@usenetarchives.gap> <gap-33aa5fa74b-p9@usenetarchives.gap>`

```



Scott McMahan - Softbase Systems wrote in
article <58p9jl$s.··.@red··h.net>...
› mike childers (m.··.@no··a.net) wrote:
› : by the way Cobol programmers always create better data elements than
…[9 more quoted lines elided]…
› 

Most 'newer' programmers have trouble believing that there was a time when
you actually had to take into consideration disk space and memory usage
when designing a program. Back in the bad old days, we would actually have
to juggle decisions about whether we could manage a 4-digit year, or
whether we should use the two digits to expand two numeric fields by one
byte each. Programmers would spend what seems now like ludicrous amounts of
time trying to design encoding schemes to fit dates into three bytes, or
whatever.

The century problem has nothing to do with COBOL. If you programmed in
assembler, or RPG, or even (gasp!) BASIC, you were still working in an
environment where 16K memory and 1 MB disk might seem like incredible
luxuries.
```

###### ↳ ↳ ↳ Re: GOTO-less C form rapes COBOL

_(reply depth: 4)_

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1996-12-12T19:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-33aa5fa74b-p9@usenetarchives.gap>`
- **References:** `<9611281432.AA13249@cow.net> <gap-33aa5fa74b-p6@usenetarchives.gap> <gap-33aa5fa74b-p7@usenetarchives.gap> <gap-33aa5fa74b-p9@usenetarchives.gap>`

```



Scott McMahan - Softbase Systems wrote in
article <58p9jl$s.··.@red··h.net>...
› mike childers (m.··.@no··a.net) wrote:
› : by the way Cobol programmers always create better data elements than
…[7 more quoted lines elided]…
› 

It may or may not be a non issue. It is still mostly an Application
program problem (Wow been a while since I heard that term ).

This is however, better discussed on comp.software.year-2000.
```

##### ↳ ↳ Re: GOTO-less C form rapes COBOL

- **From:** "steven g. townsend" <ua-author-6589043@usenetarchives.gap>
- **Date:** 1996-12-21T19:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-33aa5fa74b-p6@usenetarchives.gap>`
- **References:** `<9611281432.AA13249@cow.net> <gap-33aa5fa74b-p6@usenetarchives.gap>`

```

Thane Hubbell wrote:
› 
› [ comments deleted]
 
››  You coders that believe that you can "quick fix"
››  the maintainability of all the programs in the
…[16 more quoted lines elided]…
› were not supported.

I agree. The original IF statement sounds like a nightmare. I myself have had
to re-write code just to see what it was doing. It is unfortunate that after
all that work you choose to use GOTOs. Judicious use of IF NOT, PERFORMs (inline
or standard), EVALUATE, IF END-IF probably would have yielded the same clarity.

Someone down the line will probably feel compelled to "clean-up" your GOTOs.

I could tell you stories about how bugs could "pop-up" in very strange and
difficult to track down ways because of GOTOs.



BTW... Not all 'C' programmers write deeply nested ifs or other confusing
constructs. My rule is whatever language I am using is keep it simple.
Assume someone with less experience than you have,
who comes to the company after you have left,
and who doesn't know anybody on the "original development team"
will have to maintain the code... Even if it is for a future
enhancement that was unthought of during the original development
effort.
```

#### ↳ Re: GOTO-less C form rapes COBOL

- **From:** "sel..." <ua-author-17086096@usenetarchives.gap>
- **Date:** 1996-12-15T19:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p15@usenetarchives.gap>`
- **In-Reply-To:** `<9611281432.AA13249@cow.net>`
- **References:** `<9611281432.AA13249@cow.net>`

```


In a previous article, bhs··.@eur··t.dk ("Bent Hoff Sï¿½rensen") says:

› From: "Bent Hoff Sï¿½rensen" 
› (snip)
…[10 more quoted lines elided]…
› A COBOL (and lots of other languages) programmer for almost 20 years.

Hear, hear.

Practical implementation issues are welcome. But most sermons here
have been reruns anyway.

Steven


› mike childers  skrev i artiklen
› <01bbe589$f8995820$5919f8cc@mrc>...
…[11 more quoted lines elided]…
› 
- Steven
  sel··.@pra··t.org
```

##### ↳ ↳ Re: GOTO-less C form rapes COBOL

- **From:** "steven g. townsend" <ua-author-6589043@usenetarchives.gap>
- **Date:** 1996-12-20T19:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-33aa5fa74b-p15@usenetarchives.gap>`
- **References:** `<9611281432.AA13249@cow.net> <gap-33aa5fa74b-p15@usenetarchives.gap>`

```

Steven O. Ellis wrote:
››
›› GOTO isn't a 'cheap' statement. It's a normal part of the COBOL language
›› wether you like it or not. Wether you use it or not.

So is ALTER... But I know of no employer who will sanction its use.
I have found no situation in COBOL (or any other langauge other than
assembly) in which a GOTO could not be avoided.
The GOTO-less code is much more maintainable and less error-prone.
The GOTO problem is particularly bad because there is no symantic
difference between
used as a function name
used as a label
used to designate one or more functions (SECTION)

This last item (i.e. execute and range of functions) is not a part of
most language constructs.

I can't think of another language that allows a GOTO function.
››
›› Let's discuss COBOL.
› Let's help newcomers and other people with questions
›› about COBOL.

I agree... I happen to think that encouraging the non-use of GOTOs
DOES help newcomers and those with questions.

› And let's keep religion out of it.

Agreed. Let us keep the discussion "on the merits" and not cast
those opposed to GOTOs as "religious fanatics".

›› 
›› Ben
›› A COBOL (and lots of other languages) programmer for almost 20 years.
 
› Me too.
› 
…[23 more quoted lines elided]…
›   sel··.@pra··t.org
```

###### ↳ ↳ ↳ Re: GOTO-less C form rapes COBOL

- **From:** "remo.w..." <ua-author-17086660@usenetarchives.gap>
- **Date:** 1996-12-20T19:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-33aa5fa74b-p16@usenetarchives.gap>`
- **References:** `<9611281432.AA13249@cow.net> <gap-33aa5fa74b-p15@usenetarchives.gap> <gap-33aa5fa74b-p16@usenetarchives.gap>`

```

› So is ALTER... But I know of no employer who will sanction its use.
› I have found no situation in COBOL (or any other langauge other than
› assembly) in which a GOTO could not be avoided.

Then you don't code error handling. I can't discuss the merits of GOTO-usage
with someone who hasn't done systems programming. Tell me I'm wrong. Tell me
you're a systems programmer.

So I can laugh at you.

*Try* to avoid the use of GOTO. Code around it, rewrite algorithms, do a
better job of design. By all means, keep as many GOTOs out of the code.
HOWEVER, when I get a critical error and it makes no more sense to keep
processing, I'm gonna PERFORM ERROR-HANDLING and if I've reached max errors,
we're done, folks. Clean up the system and bomb.

-Remo
```

###### ↳ ↳ ↳ Re: GOTO-less C form rapes COBOL

_(reply depth: 4)_

- **From:** "steven g. townsend" <ua-author-6589043@usenetarchives.gap>
- **Date:** 1996-12-21T19:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-33aa5fa74b-p17@usenetarchives.gap>`
- **References:** `<9611281432.AA13249@cow.net> <gap-33aa5fa74b-p15@usenetarchives.gap> <gap-33aa5fa74b-p16@usenetarchives.gap> <gap-33aa5fa74b-p17@usenetarchives.gap>`

```

Remo Williams wrote:
› 
›› So is ALTER... But I know of no employer who will sanction its use.
…[5 more quoted lines elided]…
› you're a systems programmer.

Yes I do code error handling. I HAVE done systems programming. I have also
work on OS kernal code. So PLEASE no more condesending crap.
COBOL (this newsgroup) stands for COmmon Business Oriented Language...
I don't know about you, but I don't usually do systems programming in
COBOL.

There are some conditions in systems programming where performance
(execution time) is critical that a goto might be used.
However, ususally these (and possible alternatives) are considered
at design reviews. Remember, somebody will have to support this code
for the remaining life of the product. GOTOs make code considerably
more difficult to maintain.


› 
› So I can laugh at you.
…[7 more quoted lines elided]…
› -Remo
```

###### ↳ ↳ ↳ Re: GOTO-less C form rapes COBOL

_(reply depth: 5)_

- **From:** "bent hoff s��rensen" <ua-author-6585215@usenetarchives.gap>
- **Date:** 1996-12-23T19:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-33aa5fa74b-p18@usenetarchives.gap>`
- **References:** `<9611281432.AA13249@cow.net> <gap-33aa5fa74b-p15@usenetarchives.gap> <gap-33aa5fa74b-p16@usenetarchives.gap> <gap-33aa5fa74b-p17@usenetarchives.gap> <gap-33aa5fa74b-p18@usenetarchives.gap>`

```



Steven G. Townsend skrev i artiklen
<32B··.@pac··l.net>...
› Remo Williams wrote:
›› 
…[13 more quoted lines elided]…
› 

Oh, I don't know. I remember working on a Wang MVP2200 mini computer back
in
the eighties. The operating system, file access etc. was all written in
BASIC !!


› There are some conditions in systems programming where performance
› (execution time) is critical that a goto might be used.
…[3 more quoted lines elided]…
› more difficult to maintain.

I simply don't agree with you on that one. A GOTO can indeed make the code
considerably easier to maintain. I think that a few other people have
posted
stuff in this NG about re-writing code because there were no GOTOs. So have
I.
A long nested IF can be made a whole lot easier to read using a few GOTOs
here
and there. And I don't talk about 3 or 4 nested IFs but IFs taking up
several pages
and nesting 9 or 10 levels (or more). Yes I've seen them. I've rewritten
them. But
I've never written such a thing myself ;-)

Ben
```

###### ↳ ↳ ↳ Re: GOTO-less C form rapes COBOL

_(reply depth: 6)_

- **From:** "seekermike" <ua-author-3832286@usenetarchives.gap>
- **Date:** 1996-12-22T19:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-33aa5fa74b-p19@usenetarchives.gap>`
- **References:** `<9611281432.AA13249@cow.net> <gap-33aa5fa74b-p15@usenetarchives.gap> <gap-33aa5fa74b-p16@usenetarchives.gap> <gap-33aa5fa74b-p17@usenetarchives.gap> <gap-33aa5fa74b-p18@usenetarchives.gap> <gap-33aa5fa74b-p19@usenetarchives.gap>`

```

Bent Hoff S=F8rensen wrote:
› =
 
› Steven G. Townsend  skrev i artiklen
› <32B··.@pac··l.net>...
…[16 more quoted lines elided]…
›› I don't know about you, but I don't usually do systems programming in=
 
›› COBOL.
›› 
› =
 
› Oh, I don't know. I remember working on a Wang MVP2200 mini computer ba=
› ck
› in
› the eighties. The operating system, file access etc. was all written in=
 
› BASIC !!
› =
 
›› There are some conditions in systems programming where performance
›› (execution time) is critical that a goto might be used.
›› However, ususally these (and possible alternatives) are considered
›› at design reviews.  Remember, somebody will have to support this code=
 
›› for the remaining life of the product.  GOTOs make code considerably
›› more difficult to maintain.
› =
 
› I simply don't agree with you on that one. A GOTO can indeed make the c=
› ode
…[14 more quoted lines elided]…
› =
 
› Ben



Well, Ben, try the EVALUATE statement! It is easier than 10-level IF
statements and GOTOs. =


EVALUTE TRUE

WHEN A
do x

WHEN B
do y

WHEN C
do z

END-EVALUATE.

It's great! Try it.


-- =

Michael Shank
sek··.@ix.··m.com
http://serve.com/seeker/
```

###### ↳ ↳ ↳ Re: GOTO-less C form rapes COBOL

_(reply depth: 7)_

- **From:** "bent hoff s���rensen" <ua-author-6589046@usenetarchives.gap>
- **Date:** 1996-12-25T19:00:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-33aa5fa74b-p20@usenetarchives.gap>`
- **References:** `<9611281432.AA13249@cow.net> <gap-33aa5fa74b-p15@usenetarchives.gap> <gap-33aa5fa74b-p16@usenetarchives.gap> <gap-33aa5fa74b-p17@usenetarchives.gap> <gap-33aa5fa74b-p18@usenetarchives.gap> <gap-33aa5fa74b-p19@usenetarchives.gap> <gap-33aa5fa74b-p20@usenetarchives.gap>`

```



Seekermike skrev i artiklen
<32B··.@ix.··m.com>...
Bent Hoff S嚙緝ensen wrote:
› 
› Steven G. Townsend  skrev i artiklen
…[20 more quoted lines elided]…
› Ben



Well, Ben, try the EVALUATE statement! It is easier than 10-level IF
statements and GOTOs.

EVALUTE TRUE

WHEN A
do x

WHEN B
do y

WHEN C
do z

END-EVALUATE.

It's great! Try it.


Michael Shank
sek··.@ix.··m.com
http://serve.com/seeker/

----------

Oh, but I do. If I have a COBOL-85 / COBOL II / COBOL 370 compiler
available ;-)
Ben
```

###### ↳ ↳ ↳ Re: GOTO-less C form rapes COBOL

- **From:** "the image trader" <ua-author-3881168@usenetarchives.gap>
- **Date:** 1996-12-20T19:00:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-33aa5fa74b-p16@usenetarchives.gap>`
- **References:** `<9611281432.AA13249@cow.net> <gap-33aa5fa74b-p15@usenetarchives.gap> <gap-33aa5fa74b-p16@usenetarchives.gap>`

```

Huh???????

What a tempest in a teapot... sheesh

I use GO TO routinely to branch directly to the exit point of a performed routine in
COBOL, the same way that I use GoTo in Visual BASIC to branch to the bottom of a Do
While loop. It's an easy and effective way of getting out of a loop structure.

What's the problem????



Steven G. Townsend wrote:
› 
› Steven O. Ellis wrote:
…[60 more quoted lines elided]…
››   sel··.@pra··t.org
```

###### ↳ ↳ ↳ Re: GOTO-less C form rapes COBOL

- **From:** "bent hoff s���rensen" <ua-author-6589046@usenetarchives.gap>
- **Date:** 1996-12-23T19:00:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-33aa5fa74b-p23@usenetarchives.gap>`
- **In-Reply-To:** `<gap-33aa5fa74b-p16@usenetarchives.gap>`
- **References:** `<9611281432.AA13249@cow.net> <gap-33aa5fa74b-p15@usenetarchives.gap> <gap-33aa5fa74b-p16@usenetarchives.gap>`

```


Steven G. Townsend skrev i artiklen
<32B··.@pac··l.net>...
› So is ALTER... But I know of no employer who will sanction its use.
› I have found no situation in COBOL (or any other langauge other than
…[25 more quoted lines elided]…
›› 
Whew. What have I stepped in here ?

ALTER is not used because it 'alter's the code/behaviour.
I've worked on quite a few self-modifying assembler language
programs. Not easy but great fun !! We want none of that.

GOTO doesn't alter the code/behaviour of the program. It makes
clear to the reader what happens next e.g. in a nested if.
See example below.
if .....
if.....
if.....
end-if
go to xxxx-exit
end-if
end-if.
Other languages also allow a goto. They just call it something else.
'RETURN'
'EXIT'
'STOP'
'EZERTN'
etc. etc.

When it comes to my remarks about religion they don't refer
to the people that don't like GOTO. They refer to the whole
discussion about goto/no-goto.

I couldn't care less whether you code goto statements or not.
That's your business - not mine. Live and let live.

Ben
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
