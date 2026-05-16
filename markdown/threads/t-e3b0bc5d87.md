[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help with logic?

_13 messages · 7 participants · 2001-04_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help with logic?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-04-13T18:12:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<okHB6.1200$Yi2.275360@paloalto-snr1.gtei.net>`

```
I am trying to put together a generic logic tester. I am asking here
because, well, here is where the best logic guys are.

Given:
Three true/false conditions
Conditions may appear in any order
There is no "NOT" condition

Are the only possiblilities for compound conditions...

1 and 2  and 3      (all conditions true)
1  or  2   or   3      (any condition true)
(1 and 2) or  3       (either one condition true or both other conditions
true)

I think all other possible variations can be handled by rearranging which
conditions are number 1, number 2 and number 3.

But I could EASILY be wrong; this is not my strong suit.

Comments?
```

#### ↳ Re: Help with logic?

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-04-13T18:43:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ONHB6.570830$Pm2.9226499@news20.bellglobal.com>`
- **References:** `<okHB6.1200$Yi2.275360@paloalto-snr1.gtei.net>`

```
Three true/false is 000H thru 007H, eight conditions in all, is it not?
Anything generic is going to have to cover all eight, however you express
it.
01 variableA            PICTURE X VALUE "Y".
    88 FALSEA        VALUE "N".
    88 TRUEA        VALUE "Y".
etc.

If
    falsea and falseb and falsec
    perform do hex0-routine
else
if
    falsea and falseb and truec
    perform hex1-routine
else
*** etc.
else
if  truea and trueb and truec
    perform hex7-routine.

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:okHB6.1200$Yi2.275360@paloalto-snr1.gtei.net...
> I am trying to put together a generic logic tester. I am asking here
> because, well, here is where the best logic guys are.
…[36 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Help with logic?

- **From:** Jeff Baynard <jeffbaynard@home.com>
- **Date:** 2001-04-14T00:12:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B6FD0E2D.8E7%jeffbaynard@home.com>`
- **References:** `<okHB6.1200$Yi2.275360@paloalto-snr1.gtei.net> <ONHB6.570830$Pm2.9226499@news20.bellglobal.com>`

```
I recently used code just like this.  It works good for 8 combinations but
it's fairly unusable for much anything bigger.

Is it possible to do this better with an EVALUATE or some other construct?

Jeff


> 01 variableA            PICTURE X VALUE "Y".
> 88 FALSEA        VALUE "N".
…[14 more quoted lines elided]…
> perform hex.....
```

###### ↳ ↳ ↳ Re: Help with logic?

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-04-14T00:22:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lLMB6.573223$Pm2.9261366@news20.bellglobal.com>`
- **References:** `<okHB6.1200$Yi2.275360@paloalto-snr1.gtei.net> <ONHB6.570830$Pm2.9226499@news20.bellglobal.com> <B6FD0E2D.8E7%jeffbaynard@home.com>`

```
sure. see below
<G>

"Jeff Baynard" <jeffbaynard@home.com> wrote in message
news:B6FD0E2D.8E7%jeffbaynard@home.com...
> I recently used code just like this.  It works good for 8 combinations but
> it's fairly unusable for much anything bigger.
…[8 more quoted lines elided]…
> > 88 TRUEA        VALUE "Y".
    01 THE-NUMBER        PICTURE 9.
> > etc.
> >
> > If
> > falsea and falseb and falsec
>>perform do hex0-routine
    MOVE ZERO TO MY-NUMBER
> > else
> > if
> > falsea and falseb and truec
> > perform hex1-routine
    MOVE 1 TO MY-NUMBER
> > else
> > *** etc.
> > else
> > if  truea and trueb and truec
> > perform hex.....
    MOVE 7 TO MY-NUMBER.
>

    EVALUATE MY-NUMBER
    etc.]

In all seriousness, you can treat each condition as a digit, but the worse
case is always going to be 2**x where x is the number of true/false
conditions.  In other words, you are simply replacing eight if statements
with eight elvaluations. The only way to shorten that is if a subset of the
conditions have a common routine.
```

#### ↳ Re: Help with logic?

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-04-13T19:01:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<22IB6.569517$f36.16955872@news20.bellglobal.com>`
- **References:** `<okHB6.1200$Yi2.275360@paloalto-snr1.gtei.net>`

```
ps to that last.

Maybe the way to do the job Pete was talking about (parse old code and
produce new better code) could be handled by writing out 88 level
definitions of conditions, then spewing out variations of that code.

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:okHB6.1200$Yi2.275360@paloalto-snr1.gtei.net...
> I am trying to put together a generic logic tester. I am asking here
> because, well, here is where the best logic guys are.
…[36 more quoted lines elided]…
>
```

#### ↳ Re: Help with logic?

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-04-13T19:41:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AD75630.3BE012F8@home.com>`
- **References:** `<okHB6.1200$Yi2.275360@paloalto-snr1.gtei.net>`

```


Michael Mattias wrote:

> I am trying to put together a generic logic tester. I am asking here
> because, well, here is where the best logic guys are.
…[18 more quoted lines elided]…
> Comments?

OK Michael - Decision Tables :

---------------------------------------------
Conditions        Rules 1 through 8
----------------------------------------------
Red           Y    Y    Y    Y    N    N    N    N
White        Y    Y    N    N    Y    Y    N    N
Blue          Y    N    Y    N    Y     N   Y    N
---------------------------------------------
Actions (i.e. Perform Para 'x')
----------------------------------------------
Para A        x    -    -    -    -    -    -    -    -
Para B        -    x    -    -    -    -    -    -    -
Para C etc   -    -    x    -    -    -    -    -    -

-----------------------------------------------------

Conditions or Rules :

Start the bottom line with alternate Yes and No, double up on the next and so
on.
As you can see, too many Conditions and you'll go off the edge of the paper.
So when it gets this complex your actions are 'Go to Table xxx', i.e.
sub-divide the problem..

Actions : You determine those which are relevant and act accordingly. If it's
not Red, White, Blue either an error or ignore. Similarly some of the others
with a 'No' condition you may choose to ignore.

Jimmy
```

##### ↳ ↳ Re: Help with logic?

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-04-13T21:39:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XlKB6.572393$Pm2.9246484@news20.bellglobal.com>`
- **References:** `<okHB6.1200$Yi2.275360@paloalto-snr1.gtei.net> <3AD75630.3BE012F8@home.com>`

```

"James J. Gavan" <jjgavan@home.com> wrote in message
news:3AD75630.3BE012F8@home.com...
>
>
…[14 more quoted lines elided]…
> > (1 and 2) or  3       (either one condition true or both other
conditions
> > true)
> >
> > I think all other possible variations can be handled by rearranging
which
> > conditions are number 1, number 2 and number 3.
> >
…[12 more quoted lines elided]…
> ---------------------------------------------

If you look at this table edge on, you have a binary number that can be
handled by a case statement.  If you look at it vertically, and group
certain combinations with lower level logic, you have a generic if/then/else
chain. The choice of efficiency has to be made on the level of lower level
logic.  For example, can case x through y binary be assigned a single case
(all the instances of red or white). If it can, then you do not need an
exhuastive case statement, and can reduce the logic to an if/then sequence.




> Actions (i.e. Perform Para 'x')
> ----------------------------------------------
…[8 more quoted lines elided]…
> Start the bottom line with alternate Yes and No, double up on the next and
so
> on.
> As you can see, too many Conditions and you'll go off the edge of the
paper.
> So when it gets this complex your actions are 'Go to Table xxx', i.e.
> sub-divide the problem..
>
> Actions : You determine those which are relevant and act accordingly. If
it's
> not Red, White, Blue either an error or ignore. Similarly some of the
others
> with a 'No' condition you may choose to ignore.
>
> Jimmy
>
```

###### ↳ ↳ ↳ Re: Help with logic?

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-04-13T22:50:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AD782A2.8A71EAA@home.com>`
- **References:** `<okHB6.1200$Yi2.275360@paloalto-snr1.gtei.net> <3AD75630.3BE012F8@home.com> <XlKB6.572393$Pm2.9246484@news20.bellglobal.com>`

```


Donald Tees wrote:

>
> > ---------------------------------------------
…[13 more quoted lines elided]…
> exhuastive case statement, and can reduce the logic to an if/then sequence.

Agreed Don. But I was viewing it as an initial VISUAL design tool. For example,
I had to do some specs years ago for stock transfers - it was a set of such
tables. But in designing the above table you might want to throw in two more
conditions, and having 'seen' the whole picture, (if your paper is wide enough
<G>) and worked out your logic, you could well dismiss more than two thirds of
the conditions as being irrelevant.

A snippet of code perhaps - because as I see it, to get to your 'binary' you've
got to translate from file flags perhaps ?

Re  "(all the instances of red or white). If it can, then you do not need an
exhaustive case statement, and can reduce the logic to an if/then sequence...."

Depends doesn't it - if you know it to be a MUST that you ALWAYS have Red, it
simplifies case statements.
:
Another issue - a while back Richard said use a preprocessor on a Decision
Table. Richard care to show how you might preprocess this Red, White and Blue ?
(Yours truly has done absolutely zilch with preprocessors).

Jimmy
```

#### ↳ Re: Help with logic?

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz.nospam>
- **Date:** 2001-04-14T15:37:45+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ad7cc43_4@my.newsfeeds.com>`
- **References:** `<okHB6.1200$Yi2.275360@paloalto-snr1.gtei.net>`

```

Michael Mattias wrote in message ...
>I am trying to put together a generic logic tester. I am asking here
>because, well, here is where the best logic guys are.
…[19 more quoted lines elided]…
>
Michael,

>>>
Are the only possibilities for compound conditions...
<<<
Given that you are excluding NOT as an operator and only considering AND and
OR,  there are 4 ways in which you can combine 3 variables with 2 operators:
(& means "AND"; + means "OR")

A&B+C
A&B&C
A+B+C
A+B&C

You covered them, so the answer to your question is "YES".

The little universe described above has the properties which make it an
Algebra, (Association, Commutation, and Multiplicative and Additive
Identities (the Truth Values 1 and 0), even though we have not admitted
NEGATION to the Set.  If NEGATION was admitted, we could derive some further
Laws (named after a Frenchman, De Morgan) and it would then qualify as a
Boolean Algebra and we could do some useful work with it...<G>

There have been some very good posts regarding Decision Tables etc. but they
all deal with specific conditions. As has been pointed out, for three
specific variables (I think Jimmy used Red, Blue, and Green) there are 8
possible combinations. Don noted that you can view them in two different
ways and obtain "truth values". All excellent stuff. All easily
implementable in COBOL (Hey Guys! we're actually on topic for once...!)

There is another point you should consider...nested IFs.

<Begin Style War>

We have all seen horrendous examples of Nested IFs which make COBOL programs
almost unmaintainable.

Since the introduction of scope delimiters it has been ameliorated, but not
relieved entirely. Some installations ban them (like they ban anything you
might cut yourself with...ALTER, PERFORM...VARYING, INSPECT, SEARCH..
GO...TO,<G> (OK, I'm not entirely serious...but I have worked on
installations where PERFORM VARYING and SEARCH were banned; most people who
call themselves "Programmer" would find these pretty innocuous...).

Nested IFs are a useful and valid weapon in COBOL's armoury, especially when
used "properly"  I'm not going to get into a big discussion about Nested
IFs, but they are pertinent to Michael's enquiry for reasons I shall
describe.

I use Nested IFs ONLY to describe a decision TREE. I only "nest" in the TRUE
branches. Used in this way, Nested IFs cover a specific set of cases which
COULD be covered by a series of compound conditions, but it is arguably more
elegant to use a single construct.

The truth value for MY nested IFs can be described as:
(where ' represents Negation. read C' as NOT C, and => as 'implies')


A&B&C => Action1
A&B&C'=> Action2
A&B'      => Action3
A'           => Action4

In "English"...(Conditions represented by c1 c2 etc.)

if c1
    if c2
        if c3
             *> (A&B&C)
              Do Action 1
        else
             *> (A&B&C')
              Do Action 2
         end-if
     else
          *> (A&B')
           DoAction 3
     end-if
else
     *> A'
     Do Action 4
end-if

Your Logic evaluator needs to be aware of the equivalence between Nested IFs
and compound conditions, Michael. Remember that some of the above conditions
may well be compound ones including negation...

</end Style War>

Finally, the other excellent posts regarding Decision Tables may have left
some of the newcomers wondering HOW they might actually implement this in
code.

Apart from doing it by table lookup, here is a simple way for tables with
only a few conditions...
(Using the notation defined above...)

move zero to logic-value
if c1
   add 1 to logic-value
end-if
if c2
   add 2 to logic-value
end-if
if c3
   add 4 to logic-value
end-if
if c4
   add 8 to logic-value
end-if
evaluate logic-value
     when zero
              (c1+c2+c3+c4)'
     when 1
              c1&(c2+c3+c4)'
     when 2
               c2&(c1+c3+c4)'
     when 3
              c1&c2&(c3+c4)'
     when 4
              c3&(c1+c2+c4)'
     when 5
              c3&c1&(c2+c3)'
     when 6
              c3&c2&(c1+c4)'
     when 7
               c1&c2&c3&c4'
     when 8
               c4&(c1+c2+c3)'
     when 9
               c4&c1&(c2+c3)'
     when 10
               c4&c2&(c1+c3)'
     when 11
               c4&c2&c1&c3'
     when 12
               c4&c3&(c1+c2)'
     when 13
               c4&c3&c1&c2'
     when 14
               c4&c3&c2&c1'
     when 15
               C4&c3&c2&c1
end-evaluate

Newbie question: Why do you suppose there is NO "when...other" in this
evaluate? What does that mean? What would happen if one of the Actions taken
under a WHEN actually changed the value of the logic-value field?

Hope this helps (somebody...) <G>

Pete.






-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

##### ↳ ↳ Re: Help with logic?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-04-14T14:13:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iWYB6.1065$dW5.124417@paloalto-snr1.gtei.net>`
- **References:** `<okHB6.1200$Yi2.275360@paloalto-snr1.gtei.net> <3ad7cc43_4@my.newsfeeds.com>`

```
Peter E. C. Dashwood <dashwood@enternet.co.nz.nospam> wrote in message
news:3ad7cc43_4@my.newsfeeds.com...
>
> Michael Mattias wrote in message ...
…[5 more quoted lines elided]…
>

A direct answer. Thank you.

My goodness, what have I spawned? A huge style war?

All I was trying to do in my system is this:

You, Ms. User, may set from zero to three true/false conditions for an
action to occur.

When there are no conditions, I don't do nothing.
When there is one condition, I will test for true or false
When there are two conditions, I will test for both true, one true or none
true.
When there are three conditions, I will test for:
   1 and 2  and 3      (all conditions true)
   1  or  2   or   3      (any condition true)
   (1 and 2) or  3       (either one condition true or both other conditions
true)

You, Ms. User, can do any combination of truths within this definition,
although you may need to rearrange the order of your conditions to insure
the condition you want is tested.

Boolean Logic is not my strong suit, so I thought I'd just ask here. Sheesh,
I guess I should have listened to my mother when she told me to be careful
what I asked for.....

MCM
PS: But I kind of like that 8-way-box thing. Maybe I'll put in a user
maintainable truth table.. that would certainly let me add more
conditions...?????
```

###### ↳ ↳ ↳ Re: Help with logic?

- **From:** Calvin Crumrine <Calvin_Crumrine@dced.state.ak.us>
- **Date:** 2001-04-16T13:56:57-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ADB6AA9.B7B05CC8@dced.state.ak.us>`
- **References:** `<okHB6.1200$Yi2.275360@paloalto-snr1.gtei.net> <3ad7cc43_4@my.newsfeeds.com> <iWYB6.1065$dW5.124417@paloalto-snr1.gtei.net>`

```
Michael Mattias wrote:

> Peter E. C. Dashwood <dashwood@enternet.co.nz.nospam> wrote in message
> news:3ad7cc43_4@my.newsfeeds.com...
…[39 more quoted lines elided]…
> conditions...?????

As noted earlier, the 8-way box becomes unwieldy if you go much beyond 3
conditions. A different way combines the 2 approaches. You'd need to spend more
time analyzing it than I have to determine how efficient it is. This is just
real quick, off the top of my head, now.

Take 4 conditions, A, B, C, and D. You also have 4 tests.
1) a and b and c and d
2) a or b or c or d
Run these tests once with:
a=A, b=B, c=C, d=D

3) (a and b) or c or d
Run this test 7 times with:
a=A, b=B, c=C, d=D
a=A, b=C, c=B, d=D
a=A, b=D, c=B, d=C
a=B, b=C, c=A, d=D
a=B, b=D, c=A, d=C
a=C, b=D, c=A, d=B
(Note that the order of a and b don't matter, nor does the order of c and d.
That's what keeps this test to 7 iterations.)

4) (a and b and c) or d
Run this test 4 times with:
a=A, b=B, c=C, d=D
a=A, b=B, c=D, d=C
a=A, b=C, c=D, d=B
a=B, b=C, c=D, d=A

Now I believe that this conducts as many tests as the n-way box, but it might be
easier to manage, particularly for larger values of n. Plus, maybe you could
find an even easier way. For example, test the conditions 2 at a time. Test 4
then becomes ((a and b) and c) or d. You can use the 2-variable switching logic
from test 3 to cycle thru the first part. Or maybe this becomes so inefficient
code-wise that it overshadows the efficiency maintenance-wise. Like I said, I
haven't exactly analyzed this yet.
```

###### ↳ ↳ ↳ Re: Help with logic?

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-04-16T21:57:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ADB6ABB.668AE5D5@home.com>`
- **References:** `<okHB6.1200$Yi2.275360@paloalto-snr1.gtei.net> <3ad7cc43_4@my.newsfeeds.com> <iWYB6.1065$dW5.124417@paloalto-snr1.gtei.net> <3ADB6AA9.B7B05CC8@dced.state.ak.us>`

```


Calvin Crumrine wrote:

> Michael Mattias wrote:
>
…[7 more quoted lines elided]…
> real quick, off the top of my head, now. <snip>

For those interested in following up on Decision Tables, there's a fair bit on the
Net if you go into google.com, tutorial stuff and software.
```

#### ↳ Re: Help with logic?

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-04-14T17:40:21+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AD87D75.2D4A73D1@Azonic.co.nz>`
- **References:** `<okHB6.1200$Yi2.275360@paloalto-snr1.gtei.net>`

```
Michael Mattias wrote:
> 
> I am trying to put together a generic logic tester. I am asking here
…[5 more quoted lines elided]…
> There is no "NOT" condition

This is what Decision Tables were for.  

                        1 2 3 4 5 6 7 8 E
     Condition 1        Y Y Y Y N N N N
     Condition 2        Y Y N N Y Y N N
     Condition 3        Y N Y N Y N Y N

8 possible, 2^3. With decision table processors the actions would then
be listed below this with an indicator as to which should be performed.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
