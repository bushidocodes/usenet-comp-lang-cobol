[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Numbered prefixes

_124 messages · 18 participants · 2003-07 → 2003-08_

---

### Numbered prefixes

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-07-30T22:18:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net>`

```
Over the last year (or more), I have seen a number of people talking for and
against "numbered prefixes" (particularly the

   0100-Para

type paragraph/section names).

I understand the history of these (READY TRACE debugging, punched
card-decks, line-by-line editors, etc) but IN GENERAL, I have viewed this as
"yet another" style-only issue, i.e. YMMV.

HOWEVER, while working on a totally unrelated "problem", I did discover ONE
"good" (not overwhelming - but still good) reason to use numeric prefixes
for user-defined words.

The following text is from the 2002 ISO Standard - but the wording in the
'85 Standard is SIMILAR,

"In order to reduce conflict between reserved words and user-defined words,
the following rules apply to the formation of reserved words in this
International Standard.

    NOTE It is intended to apply these rules in future editions. It is
recommended that implementors follow these rules in defining extensions.

1) Reserved words shall not begin with the digits 0 through 9 or the letters
'X', 'Y', or 'Z', except for the words ZERO, ZEROES, and ZEROS. ."

In other words, if you have a procedure-name of  "0123-Para" you are (more
or less) guaranteed that there will never be a conflict with any "Standard"
(and possibly vendor-specific) reserved word IN THE FUTURE.  On the other
hand, if you call you procedure "Something-Procedure" it *might* end up
causing you maintenance issues in with a future (or other vendor) compiler.

Some of the "words" that I think *HAVE* been used in historical COBOL source
code as user-defined names, but are now RESERVED words in the 2002 Standard
are:

ADDRESS
ALIGNED
ALLOCATE
AS
BASED
BIT
BOOLEAN
COLUMNS
CONDITION
CONSTANT
CURSOR
DEFAULT
FACTORY
FORMAT
FREE
GET
INHERITS
INTERFACE
INVOKE
LOCALE
METHOD
MINUS
NATIONAL
NESTED
NULL
OBJECT
OPTIONS
OVERRIDE
PRESENT
PROPERTY
RAISE
RAISING
REPOSITORY
RESUME
RETRY
RETURNING
SCREEN
SELF
SHARING
SOURCES
SUPER
UNIVERSAL
UNLOCK
VALID
VALIDATE

    ***

How many programmers are certain that they have NEVER used any of these as
procedure or data names?

P.S. It is a "medium-easy" task to "change" such names in existing
programs - and the enhanced REPLACE statement can also solve this problem,
but it wouldn't BE a problem for sites/programmers who use numeric prefixes.
```

#### ↳ Re: Numbered prefixes

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-07-30T23:20:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net>`

```

William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net...
> Over the last year (or more), I have seen a number of people talking for
and
> against "numbered prefixes" (particularly the
>
…[5 more quoted lines elided]…
> card-decks, line-by-line editors, etc)

You missed the most important one.  Prevention of looping.
Do not ever call a lower-numbered paragraph.  It is that simple.

Another bonus is that the paragraph number confers uniqueness,
so that you can use the same block(s) of code multiple times
in the same program if the solution calls for it and there is no better
way,
by simply incrementing the numbers to a new range.

Another benefit is that the paragraph number gives you an idea
of where physically in the program the code is located.
That can help while jumping around in the editor.

Another is that the paragraph number ranges themselves
can be allocated to indicate similarity of function.

There are probably more benefits, but the basic idea is that
I wouldn't write a program any other way, given my choice.

> but IN GENERAL, I have viewed this as
> "yet another" style-only issue, i.e. YMMV.

It is definitely not.  It is excellent coding practice.
>
> In other words, if you have a procedure-name of  "0123-Para" you are
(more
> or less) guaranteed that there will never be a conflict with any
"Standard"
> (and possibly vendor-specific) reserved word IN THE FUTURE.  On the other
> hand, if you call you procedure "Something-Procedure" it *might* end up
> causing you maintenance issues in with a future (or other vendor)
compiler.
>
> ADDRESS
…[16 more quoted lines elided]…
> How many programmers are certain that they have NEVER used any of these
as
> procedure or data names?

I have never and would never use a single word as a paragraph or data name.
I learned that Day One.

> P.S. It is a "medium-easy" task to "change" such names in existing
> programs - and the enhanced REPLACE statement can also solve this
problem,
> but it wouldn't BE a problem for sites/programmers who use numeric
prefixes.

As far as I am concerned, you have a solution looking for a non-existent
problem.
```

##### ↳ ↳ Re: Numbered prefixes

- **From:** docdwarf@panix.com
- **Date:** 2003-07-30T20:20:27-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bg9ncb$8oi$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net>`

```
In article <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net>,
Hugh Candlin <no@spam.com> wrote:
>
>William M. Klein <wmklein@nospam.netcom.com> wrote in message
…[12 more quoted lines elided]…
>Do not ever call a lower-numbered paragraph.  It is that simple.

Hmmmmm... this brings me back to those Oldene Dayse when I recall being
taught about using SECTIONs to avoid paging.

(Note the wording, please; in order to avoid a repetition of the 
paging/segmentation/other stuff discussion I did *not* state what SECTIONs 
did nor what I was taught SECTIONs did... I stated what 'I recall being 
taught'.  My memory is, admittedly, porous.)

Anyhow... back in those Anciente Tymes - when a coder could code code such 
as *ten* coders codent... errrr, couldn't code today! - I was taught that 
Thou Shalt Not Write a Backwards-Referring PERFORM.  The reason given for 
such is hazy - I remember being told something about a compiler which was 
popular during the last few years of the Protestant Reformation which 
would compile a backwards-referring PERFORM with nary a belch but the 
execution would be unpredictable - but in practise I have found it helpful 
if only to keep the flow of flipping through a stack o' greenbar listing 
in more-or-less the same direction.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-31T16:39:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f289e2f_8@news.athenanews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <bg9ncb$8oi$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:bg9ncb$8oi$1@panix1.panix.com...
> In article <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net>,
> Hugh Candlin <no@spam.com> wrote:
…[3 more quoted lines elided]…
> >> Over the last year (or more), I have seen a number of people talking
for and
> >> against "numbered prefixes" (particularly the
> >>
…[27 more quoted lines elided]…
>

I remember (porously <G>) being told the same thing, Doc.

Backward references were considered a "violation" of the "Top Down" nature
of Structured Programming. Because Evangelists need something more than just
dogma to persuade thinking individuals like Programmers, they then put a
smokescreen round it saying "Well, you can't guarantee paging efficiency if
you use backward references..."

(This is actually true, but it was so piddling even then, that it makes me
smile to think I was taken in by it for a few months.)

Nowadays, it is totally irrelevant.

Pete.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-31T04:20:28-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgajgc$4lj$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <bg9ncb$8oi$1@panix1.panix.com> <3f289e2f_8@news.athenanews.com>`

```
In article <3f289e2f_8@news.athenanews.com>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:bg9ncb$8oi$1@panix1.panix.com...
…[17 more quoted lines elided]…
>>

[snip]

>> Anyhow... back in those Anciente Tymes - when a coder could code code such
>> as *ten* coders codent... errrr, couldn't code today! - I was taught that
…[20 more quoted lines elided]…
>Nowadays, it is totally irrelevant.

And that might be the reason that it is still recalled... because 
irrelevant never forgets!

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-31T13:52:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgb6v3$3uq$1@peabody.colorado.edu>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <bg9ncb$8oi$1@panix1.panix.com>`

```

On 30-Jul-2003, docdwarf@panix.com wrote:

> Anyhow... back in those Anciente Tymes - when a coder could code code such
> as *ten* coders codent... errrr, couldn't code today! - I was taught that
…[6 more quoted lines elided]…
> in more-or-less the same direction.

Some people who moved from interpreted languages such as Basic learned "put the
most commonly performed paragraphs at the top".   I had a language called
ACTION! that had a design where the very last command in the program was the
start.   Forth was kind of like that.

I know we're talking CoBOL, but I don't want to be stuck using a practice that
was set up because of a compiler limitation from Anciente Tymes (I suspect I do
have some such practices).    I want to have better reasons for my styles.
```

##### ↳ ↳ Re: Numbered prefixes

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-31T02:32:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jc%Va.81309$0v4.5405133@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net>`

```

"Hugh Candlin" <no@spam.com> wrote in message
news:apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net...
|
| William M. Klein <wmklein@nospam.netcom.com> wrote in message
…[13 more quoted lines elided]…
| Do not ever call a lower-numbered paragraph.  It is that simple.

How does that prevent looping?
Are you talking about GO TO, or PERFORM?

| Another bonus is that the paragraph number confers uniqueness,
| so that you can use the same block(s) of code multiple times
| in the same program if the solution calls for it and there is no better
| way,
| by simply incrementing the numbers to a new range.

Why not just give it a higher number?
You don't have to move it.
Nobody said they have to be in ascending sequence.

Why would you want to make changes to the same routine in several places?
Doesn't that complicate maintenance, and enhancement?

| Another benefit is that the paragraph number gives you an idea
| of where physically in the program the code is located.
| That can help while jumping around in the editor.

Only if they are in sequence.

| Another is that the paragraph number ranges themselves
| can be allocated to indicate similarity of function.
…[7 more quoted lines elided]…
| It is definitely not.  It is excellent coding practice.

Why don't you discuss this with Mr. Wagner.

<<snip>>
```

###### ↳ ↳ ↳ Re: Numbered prefixes

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-31T16:40:32+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f289e79_6@news.athenanews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <Jc%Va.81309$0v4.5405133@bgtnsc04-news.ops.worldnet.att.net>`

```
LOL!

Dennis I really enjoyed this response and endorse it 100%.

Great stuff!

Pete.

"Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
news:Jc%Va.81309$0v4.5405133@bgtnsc04-news.ops.worldnet.att.net...
>
> "Hugh Candlin" <no@spam.com> wrote in message
…[4 more quoted lines elided]…
> | > Over the last year (or more), I have seen a number of people talking
for
> | and
> | > against "numbered prefixes" (particularly the
…[48 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Numbered prefixes

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-07-31T05:24:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iK1Wa.3966$K4.184208@twister.tampabay.rr.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <Jc%Va.81309$0v4.5405133@bgtnsc04-news.ops.worldnet.att.net>`

```

"Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
news:Jc%Va.81309$0v4.5405133@bgtnsc04-news.ops.worldnet.att.net...
> | You missed the most important one.  Prevention of looping.
> | Do not ever call a lower-numbered paragraph.  It is that simple.
> How does that prevent looping?
> Are you talking about GO TO, or PERFORM?
P2000-INIT.
         PERFORM P3000-DO-STUFF.

P3000-DO-STUFF.
         PERFORM P2000-INIT.

If you only go up it don't happen unless you use GO TO blah dee blah

> | Another bonus is that the paragraph number confers uniqueness,
> | so that you can use the same block(s) of code multiple times
…[4 more quoted lines elided]…
> Nobody said they have to be in ascending sequence.
Obviously you would change it like this to make it highly maintainable.

2000-DO-STUFF.
               some block of code.

2000-D0-STUFF.
                same block of code.

200O-D0-STUFF.
                same block of code.

> Why would you want to make changes to the same routine in several places?
Read the guide to writing unmaintainable code...<G>

> | Another benefit is that the paragraph number gives you an idea
> | of where physically in the program the code is located.
> | That can help while jumping around in the editor.
> Only if they are in sequence.
This isn't as stupid as it sounds.  I actually had a discussion with someone
because we both used numbers but interpreted them differently.  In the end
the issue for me ended up less what the names were and more the logical
position in the module....
I don't like having performs that jump over 10 paragraphs and then back and
then the next perform jumps over 11 paragraphs because reading the code is
like watching tennis....I prefer the pee on the tree view where it trickles
from top down.

JCE
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 4)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-31T12:53:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_i8Wa.81695$0v4.5447548@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <Jc%Va.81309$0v4.5405133@bgtnsc04-news.ops.worldnet.att.net> <iK1Wa.3966$K4.184208@twister.tampabay.rr.com>`

```

"jce" <defaultuser@hotmail.com> wrote in message
news:iK1Wa.3966$K4.184208@twister.tampabay.rr.com...
|
| "Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
…[11 more quoted lines elided]…
| If you only go up it don't happen unless you use GO TO blah dee blah

I understand that this prevents ONE type of looping, but not all.

000-PARA-A.
              VARYING I-TBL  FROM 1  BY 1
                    UNTIL  I-TBL  >  T-TBL-OCCURS
                   PERFORM 900-PARA-B
                 etc.
900-PARA-B.
                 SET I-TBL TO 1
                etc.

Will go into a loop also, and it adheres to the number greater than edict.

The bottom line is you have to check your code.
There is no magic bullet.


|
| > | Another bonus is that the paragraph number confers uniqueness,
| > | so that you can use the same block(s) of code multiple times
| > | in the same program if the solution calls for it and there is no
better
| > | way, by simply incrementing the numbers to a new range.
| > Why not just give it a higher number?
| > You don't have to move it.
| > Nobody said they have to be in ascending sequence.

| Obviously you would change it like this to make it highly maintainable.

SOMETIMES I run into programmers who religiously number their paragraphs.
But, they have trouble with the concept that they should be in ascending
sequence.

| 2000-DO-STUFF.
|                some block of code.
…[7 more quoted lines elided]…
| > Why would you want to make changes to the same routine in several
places?

| Read the guide to writing unmaintainable code...<G>
|
…[4 more quoted lines elided]…
| This isn't as stupid as it sounds.  I actually had a discussion with
someone
| because we both used numbers but interpreted them differently.  In the end
| the issue for me ended up less what the names were and more the logical
| position in the module....
| I don't like having performs that jump over 10 paragraphs and then back
and
| then the next perform jumps over 11 paragraphs because reading the code is
| like watching tennis....I prefer the pee on the tree view where it
trickles
| from top down.
|
What the law, "Do not ever call a lower-numbered paragraph", does is make
the placement of paragraphs dependent on the highest number that performs
them, not on their relationship to the main program functions.

If you put you program initialization near the end of the program (a common
practice), every paragraph that it performs must be a higher number, so you
have to move them based on a single invocation. It doesn't make sense.
Making a copy doesn't make sense either.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 4)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-31T14:00:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgb7ds$44n$1@peabody.colorado.edu>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <Jc%Va.81309$0v4.5405133@bgtnsc04-news.ops.worldnet.att.net> <iK1Wa.3966$K4.184208@twister.tampabay.rr.com>`

```

On 30-Jul-2003, "jce" <defaultuser@hotmail.com> wrote:

> P2000-INIT.
>          PERFORM P3000-DO-STUFF.
…[4 more quoted lines elided]…
> If you only go up it don't happen unless you use GO TO blah dee blah

I never thought of that.  With all of the bad code I have seen over the decades,
I suppose there's always the possibility of seeing something new.


> This isn't as stupid as it sounds.

Entirely possible - but only because it sounds absolutely stupid.   So why isn't
it as stupid as it sounds?

> I actually had a discussion with someone
> because we both used numbers but interpreted them differently.  In the end
…[5 more quoted lines elided]…
> from top down.

That doesn't work when you have many places where you want to PERFORM
9000-STATUS-CHECK
or
WHEN CHOICE1 PERFORM 120-CHOICE1
WHEN CHOICE2 PERFORM 120-CHOICE2
WHEN CHOICE3 PERFORM 120-CHOICE3
WHEN CHOICE4 PERFORM 120-CHOICE4
WHEN CHOICE5 PERFORM 120-CHOICE5
...
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-07-31T12:23:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0307311123.599f78da@posting.google.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <Jc%Va.81309$0v4.5405133@bgtnsc04-news.ops.worldnet.att.net> <iK1Wa.3966$K4.184208@twister.tampabay.rr.com>`

```
"jce" <defaultuser@hotmail.com> wrote

> P2000-INIT.
>          PERFORM P3000-DO-STUFF.
…[4 more quoted lines elided]…
> If you only go up it don't happen unless you use GO TO blah dee blah

That is just putting in a rule as a poor substitute for having a
design for the program.

It would seem that 'P2000-Init' is initialising something, so why is
it _also_ doing stuff ? The P3000-Do-Stuff also requires something to
be initialised, which may be reasonable.

It seems to me that the program is not being broken down into small
enough modules.  This may be the result of requiring too much
'overhead' in creating a new procedure: it needs to be numbered in the
hierarchy of the code, it needs to be positioned in the source code,
any procedure it performs needs to be ensured of being a higher number
(by copying!).  It just becomes too much effort.  This leads to
procedures doing too much so reuse becomes too difficult and too error
prone.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-31T19:41:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgbrdg$dhh$1@peabody.colorado.edu>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <Jc%Va.81309$0v4.5405133@bgtnsc04-news.ops.worldnet.att.net> <iK1Wa.3966$K4.184208@twister.tampabay.rr.com> <217e491a.0307311123.599f78da@posting.google.com>`

```
I did see an interesting loop one time when there was an error in the automatic
error routine.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2003-07-31T16:09:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F298597.2D4FC34D@mb.sympatico.ca>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <Jc%Va.81309$0v4.5405133@bgtnsc04-news.ops.worldnet.att.net>`

```
Harley wrote:

> "Hugh Candlin" <no@spam.com> wrote in message
> news:apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net...
…[20 more quoted lines elided]…
> <snip>

> Only if they are in sequence.
>
…[13 more quoted lines elided]…
> <<snip>>

Judging by the sharpness of your comments, I'd guess that you don't use this
style.  Fair enough.  But all the points made in its favour are very good and
work exactly as stated.  Just the fact that it's easier to navigate the listing
based on the paragraph prefixes makes it worthwhile.   Your note "only if they
are in sequence" is kind of mind-boggling: can you seriously imagine using
numeric prefixes that are out of sequence????

PL
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 4)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-07-31T21:38:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<E%fWa.78960$3o3.5413038@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <Jc%Va.81309$0v4.5405133@bgtnsc04-news.ops.worldnet.att.net> <3F298597.2D4FC34D@mb.sympatico.ca>`

```

Peter Lacey <lacey@mb.sympatico.ca> wrote in message
news:3F298597.2D4FC34D@mb.sympatico.ca...
>
> Judging by the sharpness of your comments, I'd guess that you don't use
this
> style.  Fair enough.  But all the points made in its favour are very good
and
> work exactly as stated.  Just the fact that it's easier to navigate the
listing
> based on the paragraph prefixes makes it worthwhile.   Your note "only if
they
> are in sequence" is kind of mind-boggling: can you seriously imagine
using
> numeric prefixes that are out of sequence????


While I could perhaps be faulted for the brevity of the post,
I took the tack that I was addressing experienced professionals
who would be open-minded and receptive to the expression
of a viewpoint, and capable of seeing the big picture.

Until your post, I was becoming seriously depressed at the antagonistic
and cliquish attitude of most of the respondents, who seem to have
allowed themselves to be brainwashed by the common NG misconception
that having posted frequently somehow confers superior powers and insight,
and sanctions the browbeating of others with their own point of view
and misinterpretations.

This attitude renders the NG worthless as a forum for civil discourse.
One is forced to shake one's head in dismay and ignore the more
blatant displays of uncalled for antagonism.

You made my day.  Thank you, sir.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 5)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-08-01T11:35:51+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f29a8c9_3@news.athenanews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <Jc%Va.81309$0v4.5405133@bgtnsc04-news.ops.worldnet.att.net> <3F298597.2D4FC34D@mb.sympatico.ca> <E%fWa.78960$3o3.5413038@bgtnsc05-news.ops.worldnet.att.net>`

```

"Hugh Candlin" <no@spam.com> wrote in message
news:E%fWa.78960$3o3.5413038@bgtnsc05-news.ops.worldnet.att.net...
>
> Peter Lacey <lacey@mb.sympatico.ca> wrote in message
…[4 more quoted lines elided]…
> > style.  Fair enough.  But all the points made in its favour are very
good
> and
> > work exactly as stated.  Just the fact that it's easier to navigate the
> listing
> > based on the paragraph prefixes makes it worthwhile.   Your note "only
if
> they
> > are in sequence" is kind of mind-boggling: can you seriously imagine
…[8 more quoted lines elided]…
>

But if they disagree with you...?

> Until your post, I was becoming seriously depressed at the antagonistic
> and cliquish attitude of most of the respondents, who seem to have
…[3 more quoted lines elided]…
> and misinterpretations.

As a frequent poster here, I guess I'm included in that.

Hugh, nobody is brow-beating anybody.

If any of  us post here we have to expect there will be disagreement. If you
feel SO strongly about your post that you get depressed when it is attacked
or disagreed with, then there is a statement about kitchens and heat that
comes to mind.

I enjoy seeing your posts (whether I agree with them or not) and it would be
a pity if you become so discouraged that you stop making them.

>
> This attitude renders the NG worthless as a forum for civil discourse.
> One is forced to shake one's head in dismay and ignore the more
> blatant displays of uncalled for antagonism.
>

I honestly believe you are being over sensitive.

I strongly disagree with your expressed views on this, but you are saying
that if I express my disagreement I am being antagonistic or overbearing or
brow-beating you.

It was never my intent to wound.

Don't take it to heart.

It is only "computer programming"....

Pete.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 6)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-08-01T04:34:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95mWa.6609$K4.290412@twister.tampabay.rr.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <Jc%Va.81309$0v4.5405133@bgtnsc04-news.ops.worldnet.att.net> <3F298597.2D4FC34D@mb.sympatico.ca> <E%fWa.78960$3o3.5413038@bgtnsc05-news.ops.worldnet.att.net> <3f29a8c9_3@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3f29a8c9_3@news.athenanews.com...
> But if they disagree with you...?

Or if they are DD?
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-01T08:16:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgdlmn$hov$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <E%fWa.78960$3o3.5413038@bgtnsc05-news.ops.worldnet.att.net> <3f29a8c9_3@news.athenanews.com> <95mWa.6609$K4.290412@twister.tampabay.rr.com>`

```
In article <95mWa.6609$K4.290412@twister.tampabay.rr.com>,
jce <defaultuser@REMOVETHISBIThotmail.com> wrote:
>"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
>news:3f29a8c9_3@news.athenanews.com...
>> But if they disagree with you...?
>
>Or if they are DD?

Answering a question with a question is no answer at all.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-08-01T14:12:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgdsgh$h0e$1@peabody.colorado.edu>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <E%fWa.78960$3o3.5413038@bgtnsc05-news.ops.worldnet.att.net> <3f29a8c9_3@news.athenanews.com> <95mWa.6609$K4.290412@twister.tampabay.rr.com> <bgdlmn$hov$1@panix1.panix.com>`

```

On  1-Aug-2003, docdwarf@panix.com wrote:

> Answering a question with a question is no answer at all.

You keep saying that.   It is an ancient technique that often works.

And certainly lots of the "answers" in this forum do not work.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-01T13:31:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bge854$6cq$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <95mWa.6609$K4.290412@twister.tampabay.rr.com> <bgdlmn$hov$1@panix1.panix.com> <bgdsgh$h0e$1@peabody.colorado.edu>`

```
In article <bgdsgh$h0e$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  1-Aug-2003, docdwarf@panix.com wrote:
…[3 more quoted lines elided]…
>You keep saying that.   It is an ancient technique that often works.

Just like trephanning, I am sure.

>
>And certainly lots of the "answers" in this forum do not work.

The fact that something does or does not do yet another thing does not 
change that answering a question with a question is no answer at all.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-08-01T18:06:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgea7c$mhn$1@peabody.colorado.edu>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <95mWa.6609$K4.290412@twister.tampabay.rr.com> <bgdlmn$hov$1@panix1.panix.com> <bgdsgh$h0e$1@peabody.colorado.edu> <bge854$6cq$1@panix1.panix.com>`

```

On  1-Aug-2003, docdwarf@panix.com wrote:

> >And certainly lots of the "answers" in this forum do not work.
>
> The fact that something does or does not do yet another thing does not
> change that answering a question with a question is no answer at all.

It doesn't change that.   But answering a question with a question is often an
answer nevertheless.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-01T14:16:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgeaqe$lsu$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgdsgh$h0e$1@peabody.colorado.edu> <bge854$6cq$1@panix1.panix.com> <bgea7c$mhn$1@peabody.colorado.edu>`

```
In article <bgea7c$mhn$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  1-Aug-2003, docdwarf@panix.com wrote:
…[7 more quoted lines elided]…
>answer nevertheless. 

This would be rather curious, then, since answering a question with a 
question is no answer at all.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-08-01T18:36:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgebuq$n8o$1@peabody.colorado.edu>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgdsgh$h0e$1@peabody.colorado.edu> <bge854$6cq$1@panix1.panix.com> <bgea7c$mhn$1@peabody.colorado.edu> <bgeaqe$lsu$1@panix1.panix.com>`

```

On  1-Aug-2003, docdwarf@panix.com wrote:

> >It doesn't change that.   But answering a question with a question is often
> >an
…[3 more quoted lines elided]…
> question is no answer at all.

I guess we agree to disagree here.  I kind of like Socrates' method.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-01T19:54:02-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgeuiq$hn1$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgea7c$mhn$1@peabody.colorado.edu> <bgeaqe$lsu$1@panix1.panix.com> <bgebuq$n8o$1@peabody.colorado.edu>`

```
In article <bgebuq$n8o$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  1-Aug-2003, docdwarf@panix.com wrote:
…[8 more quoted lines elided]…
>I guess we agree to disagree here.  I kind of like Socrates' method. 

Mr Brazee, I have studied Socrates, Socrates was an academic subject of 
mine, I have read Platonic Dialogues in Ancient Greek.

Mr Brazee, to you and all others to whom I might have responded with 
'answering a question is no question at all': you are *not* Socrates.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 14)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-08-01T22:07:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ttWdnWShoOFvt7aiXTWJkQ@giganews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgea7c$mhn$1@peabody.colorado.edu> <bgeaqe$lsu$1@panix1.panix.com> <bgebuq$n8o$1@peabody.colorado.edu> <bgeuiq$hn1$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <bgebuq$n8o$1@peabody.colorado.edu>,
> Howard Brazee <howard@brazee.net> wrote:
…[8 more quoted lines elided]…
> 'answering a question is no question at all': you are *not* Socrates.

Wonder what you call an answer for which there was no question? Much like:

"Some say 'use the soap.' "
But soap leaves a dirty ring.
I say: "Hold the soap, hold the soap."
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-02T07:14:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgg6fd$kon$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgebuq$n8o$1@peabody.colorado.edu> <bgeuiq$hn1$1@panix1.panix.com> <ttWdnWShoOFvt7aiXTWJkQ@giganews.com>`

```
In article <ttWdnWShoOFvt7aiXTWJkQ@giganews.com>,
JerryMouse <nospam@bisusa.com> wrote:
>docdwarf@panix.com wrote:
>> In article <bgebuq$n8o$1@peabody.colorado.edu>,
…[15 more quoted lines elided]…
>I say: "Hold the soap, hold the soap."

In the context of Socrates I would call this 'something about which 
certain youths might best be wary'.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 13)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-08-02T13:23:23+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f2b1346_3@news.athenanews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgdsgh$h0e$1@peabody.colorado.edu> <bge854$6cq$1@panix1.panix.com> <bgea7c$mhn$1@peabody.colorado.edu> <bgeaqe$lsu$1@panix1.panix.com> <bgebuq$n8o$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:bgebuq$n8o$1@peabody.colorado.edu...
>
> On  1-Aug-2003, docdwarf@panix.com wrote:
>
> > >It doesn't change that.   But answering a question with a question is
often
> > >an
> > >answer nevertheless.
…[4 more quoted lines elided]…
> I guess we agree to disagree here.  I kind of like Socrates' method.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 13)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-08-02T13:26:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f2b13ff_5@news.athenanews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgdsgh$h0e$1@peabody.colorado.edu> <bge854$6cq$1@panix1.panix.com> <bgea7c$mhn$1@peabody.colorado.edu> <bgeaqe$lsu$1@panix1.panix.com> <bgebuq$n8o$1@peabody.colorado.edu>`

```
Oops! Sorry about the double post..ignore the "other one".

Come to think of it, you could probably ignore this one too without it
making much difference to your day <G>...

"Howard Brazee" <howard@brazee.net> wrote in message
news:bgebuq$n8o$1@peabody.colorado.edu...
>
> On  1-Aug-2003, docdwarf@panix.com wrote:
>
> > >It doesn't change that.   But answering a question with a question is
often
> > >an
> > >answer nevertheless.
…[4 more quoted lines elided]…
> I guess we agree to disagree here.  I kind of like Socrates' method.

I hope you're not referring to his penchant for little boys, Howard. And,
from the smell of it, I shouldn't think hemlock tastes very good...

Pete.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 14)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-01T21:36:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgf4i0$lo1$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgeaqe$lsu$1@panix1.panix.com> <bgebuq$n8o$1@peabody.colorado.edu> <3f2b13ff_5@news.athenanews.com>`

```
In article <3f2b13ff_5@news.athenanews.com>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>Oops! Sorry about the double post..ignore the "other one".
>
…[17 more quoted lines elided]…
>I hope you're not referring to his penchant for little boys, Howard.

Oh, I *cannot* resist... and the habit of answering a question with a 
question might also be seen as likewise...

... buggered-up.

>And,
>from the smell of it, I shouldn't think hemlock tastes very good...

Idealist: One who, on noticing a rose smells better than a cabbage, 
concludes that it will make a better soup. - HL Mencken.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 12)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-08-01T18:40:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JuyWa.5321$On2.366355@twister.tampabay.rr.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgdsgh$h0e$1@peabody.colorado.edu> <bge854$6cq$1@panix1.panix.com> <bgea7c$mhn$1@peabody.colorado.edu> <bgeaqe$lsu$1@panix1.panix.com>`

```
> >It doesn't change that.   But answering a question with a question is
often an
> >answer nevertheless.
>
> This would be rather curious, then, since answering a question with a
> question is no answer at all.

is answering a statement with an answer an answer ?

JCE
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-01T19:56:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgeun0$ir0$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgea7c$mhn$1@peabody.colorado.edu> <bgeaqe$lsu$1@panix1.panix.com> <JuyWa.5321$On2.366355@twister.tampabay.rr.com>`

```
In article <JuyWa.5321$On2.366355@twister.tampabay.rr.com>,
jce <defaultuser@REMOVETHISBIThotmail.com> wrote:
>> >It doesn't change that.   But answering a question with a question is often an
>> >answer nevertheless.
…[4 more quoted lines elided]…
>is answering a statement with an answer an answer ?

It can be... if the answerer's answering answer answers, of course.

(Would responding to a question in that manner while riding in a World War 
II vintage German tank be a case of answers in the Panzers?)

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-02T09:06:19+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgeko1$g3a$3@aklobs.kc.net.nz>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3f29a8c9_3@news.athenanews.com> <95mWa.6609$K4.290412@twister.tampabay.rr.com> <bgdlmn$hov$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>>Or if they are DD?
> 
> Answering a question with a question is no answer at all.

Shouldn't that be:

 Is answering a question with a question any sort of answer at all ?
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-01T19:57:54-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgeuq2$j3p$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <95mWa.6609$K4.290412@twister.tampabay.rr.com> <bgdlmn$hov$1@panix1.panix.com> <bgeko1$g3a$3@aklobs.kc.net.nz>`

```
In article <bgeko1$g3a$3@aklobs.kc.net.nz>,
Richard Plinston  <riplin@Azonic.co.nz> wrote:
>docdwarf@panix.com wrote:
>
…[6 more quoted lines elided]…
> Is answering a question with a question any sort of answer at all ?

Were one to wish a less-subtle demonstration, perhaps.

(Phrased as an interoggative: Whadday want, a less-subtle demonstration?)

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-08-02T13:48:59+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f2b1947_4@news.athenanews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <95mWa.6609$K4.290412@twister.tampabay.rr.com> <bgdlmn$hov$1@panix1.panix.com> <bgeko1$g3a$3@aklobs.kc.net.nz> <bgeuq2$j3p$1@panix1.panix.com>`

```
"Why do you always answer a question with a question?"
"Do I?"
"Don't you think so? Haven't you noticed this behaviour on your part?
"Should I pay attention to it?"
"Has it not occurred to you how irritating this can be for the
interrogator?"
"But how can I point out other pertinances not addressed by the original
question, unless I raise further questions?"
"Couldn't you just address the direct issue, then go on to the other
pertinances?"
"Wouldn't  that be kind of stilted and boring?"
"Did you know that Doc thinks answering a question with a question is no
answer at all?"
"Is the Doc ALWAYS right?"
"Can you show any occasions when he wasn't?"
"Wouldn't you say the above dialogue shows cases where an answer can be
obtained by a legitimate question?"
"Why not ask the Doc?"
"Won't he just reiterate his mantra that answering a question with a
question is no answer at all?"
"How could he say that, without thinking about it?"
"How do you know he hasn't thought about it?"
"If he'd thought about it, wouldn't he have realised that there are
occasions when another question can be a perfectly legitimate answer?"
"Does it really matter?"
"Does anything really matter"?
Hmmmm.... good answer. I guess there is a place for rhetorical questions,
and sometimes that place can be in answer to a  previous question.

Pete.

(TOP POST - no more - once I've signed it there are no further comments.)

<docdwarf@panix.com> wrote in message news:bgeuq2$j3p$1@panix1.panix.com...
> In article <bgeko1$g3a$3@aklobs.kc.net.nz>,
> Richard Plinston  <riplin@Azonic.co.nz> wrote:
…[15 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-02T07:35:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgg7mn$qkb$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgeko1$g3a$3@aklobs.kc.net.nz> <bgeuq2$j3p$1@panix1.panix.com> <3f2b1947_4@news.athenanews.com>`

```
In article <3f2b1947_4@news.athenanews.com>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:

[snip]

>"Did you know that Doc thinks answering a question with a question is no
>answer at all?"
…[10 more quoted lines elided]…
>occasions when another question can be a perfectly legitimate answer?"

I thought I'd addressed this here but perhaps not, it might have been in 
another venue.

Quite openly and honestly: I find that for the overwhelming majority of 
cases answering a question with a question is a stall, a dodge or some way 
to avoid/evade the original query; the 'air' that it carries is 'I cannot 
answer your question so... I'll ask one of you and if you cannot answer it 
then in some way we'll both be even and our arguments will cancel each 
other out, maybe I can even assume a bit of smug superiority by having 
posed the last, unanswerable question.'

Note that I said 'overwhelming majority of cases', not 'all'... but I have 
*never* found a case where the answering question could not be phrased in 
a manner that would turn the dialogue away from the seriocomic interchange 
you posted into something a bit closer to what I would call 'rational 
discourse'.  Consider the differences between:

'Yeah?  Well, what about (condition)?'
'Whaddaya mean, (condition)?'

... and ...

'Yeah?  Well, what about (condition)?'
'I cannot address that until you make it clear what criteria you are using 
to establish the existence of (condition)?'

Now turning the discord of Duelling Interrogatories into the harmony of 
Rational Discourse might require something called 'honesty' and 
'integrity' as the tactics involve using such phrases as 'I don't know' or 
'I cannot address that' or 'I cannot see the relationship'... but if such 
things are uncomfortable they can, with a bit of practise, be hidden 
without forcing folks to fall back into mutual queries.

This having been said - that in the overwhelming majority of cases it is 
used as an evasion instead of an answer and that there are, as noted 
above, structures readily available to render its use unnecessary - then 
the conclusion is that the technique of answering a question with a 
question is treated as an ALTER and should be structured out of 
existence.

('Yeah?  What about replacing it with a called Assembley module?' 'I don't
know what I would say about that without reading the code; if you have it
available I would be most interested in reading it *first* and *then* 
rendering an opinion... but I *do* know that replacing things in such 
manner usually does not eliminate the structural flaws, it merely shifts 
them.')

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 12)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-08-03T06:01:48+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f2bfd48_7@news.athenanews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgeko1$g3a$3@aklobs.kc.net.nz> <bgeuq2$j3p$1@panix1.panix.com> <3f2b1947_4@news.athenanews.com> <bgg7mn$qkb$1@panix1.panix.com>`

```
Good response Doc, I enjoyed it. Thanks.

Pete.

<docdwarf@panix.com> wrote in message news:bgg7mn$qkb$1@panix1.panix.com...
> In article <3f2b1947_4@news.athenanews.com>,
> Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
…[65 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-02T21:00:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bghmri$ckl$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3f2b1947_4@news.athenanews.com> <bgg7mn$qkb$1@panix1.panix.com> <3f2bfd48_7@news.athenanews.com>`

```
In article <3f2bfd48_7@news.athenanews.com>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>Good response Doc, I enjoyed it. Thanks.

Pfoo, you'se jes' easily amused... glad you enjoyed, old boy.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 12)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-08-02T17:24:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kDWdnXSkCbO-p7GiXTWJjQ@giganews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgeko1$g3a$3@aklobs.kc.net.nz> <bgeuq2$j3p$1@panix1.panix.com> <3f2b1947_4@news.athenanews.com> <bgg7mn$qkb$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
>
> I thought I'd addressed this here but perhaps not, it might have been
…[8 more quoted lines elided]…
> of smug superiority by having posed the last, unanswerable question.'

When asked: "What is your ZIP code?" "What is your birthday?" "What is your
email address?" "Do you want to have sex?" and literally hundreds of other
questions, often the best response is another question.

"Why do you ask?"

This is usually followed by: "I'm sorry, that's not a good enough reason for
me to provide an answer. Put me down as 'decline'."

Which almost fits with your "stall, dodge, or evade" theory.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-02T21:14:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bghnmi$hpa$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3f2b1947_4@news.athenanews.com> <bgg7mn$qkb$1@panix1.panix.com> <kDWdnXSkCbO-p7GiXTWJjQ@giganews.com>`

```
In article <kDWdnXSkCbO-p7GiXTWJjQ@giganews.com>,
JerryMouse <nospam@bisusa.com> wrote:
>docdwarf@panix.com wrote:
>>
…[20 more quoted lines elided]…
>Which almost fits with your "stall, dodge, or evade" theory.

I would say your use of 'response' instead of 'answer' comes close to 
assuming this a priori... but in situations like the one you mention 
instead of asking 'Why do you ask me for my telephone number before one of 
your barbers gives me a haircut?' I will say 'I don't understand the 
reason for your needing it.'

If the response is 'The computer won't let us schedule you without one' I
will then, with a smile, say 'Then let me give you *this* one...' and give
the number for mid-state New York Directory Assistance (914-555-1212).

If the response to this is 'the computer won't accept 555 (note to those 
outside the USA: telephone numbers here are of the 999-999-9999 format, 
the first three digits being the 'area code', the next three the 
'exchange' and the final four the 'extension'; the 555 exchange is 
reserved for telephone-company use so an individual would never have an 
extension in this exchange for personal use) numbers' then I smile broadly 
and say 'Of course... let's make that 914-55*4*-1212.'

(Notice the difference between saying 'My number is' and 'Let me give you 
this number'... no misrepresentation there.)

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 14)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-08-03T04:27:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ka0Xa.7446$On2.550487@twister.tampabay.rr.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3f2b1947_4@news.athenanews.com> <bgg7mn$qkb$1@panix1.panix.com> <kDWdnXSkCbO-p7GiXTWJjQ@giganews.com> <bghnmi$hpa$1@panix1.panix.com>`

```
<docdwarf@panix.com> wrote in message news:bghnmi$hpa$1@panix1.panix.com...
> In article <kDWdnXSkCbO-p7GiXTWJjQ@giganews.com>,
> JerryMouse <nospam@bisusa.com> wrote:
…[12 more quoted lines elided]…
> DD

I thought you were King of England...turns out that you might only be a
Knight...


`You are sad,' the Knight said in an anxious tone: `let me sing you a song
to comfort you.'
'Is it very long?' Alice asked, for she had heard a good deal of poetry that
day.
`It's long,' said the Knight, `but very, VERY beautiful. Everybody that
hears me sing it--either it brings the TEARS into their eyes, or else--'
`Or else what?' said Alice, for the Knight had made a sudden pause.
`Or else it doesn't, you know. The name of the song is called "HADDOCKS'
EYES."'
`Oh, that's the name of the song, is it?' Alice said, trying to feel
interested.
`No, you don't understand,' the Knight said, looking a little vexed. `That's
what the name is CALLED. The name really IS "THE AGED AGED MAN."'
`Then I ought to have said "That's what the SONG is called"?' Alice
corrected herself.
`No, you oughtn't: that's quite another thing! The SONG is called "WAYS AND
MEANS": but that's only what it's CALLED, you know!'
`Well, what IS the song, then?' said Alice, who was by this time completely
bewildered.
`I was coming to that,' the Knight said. `The song really IS "A-SITTING ON A
GATE": and the tune's my own invention.'

JCE
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 15)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-08-03T06:52:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CR5Xa.60$pq5.10689@news20.bellglobal.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3f2b1947_4@news.athenanews.com> <bgg7mn$qkb$1@panix1.panix.com> <kDWdnXSkCbO-p7GiXTWJjQ@giganews.com> <bghnmi$hpa$1@panix1.panix.com> <Ka0Xa.7446$On2.550487@twister.tampabay.rr.com>`

```
"jce" <defaultuser@hotmail.com> wrote in message
news:Ka0Xa.7446$On2.550487@twister.tampabay.rr.com...
> <docdwarf@panix.com> wrote in message
news:bghnmi$hpa$1@panix1.panix.com...
> > In article <kDWdnXSkCbO-p7GiXTWJjQ@giganews.com>,
> > JerryMouse <nospam@bisusa.com> wrote:
…[6 more quoted lines elided]…
> > extension in this exchange for personal use) numbers' then I smile
broadly
> > and say 'Of course... let's make that 914-55*4*-1212.'
> >
> > (Notice the difference between saying 'My number is' and 'Let me give
you
> > this number'... no misrepresentation there.)
> >
…[4 more quoted lines elided]…
>

Once  king, always a king, but once a knight is enough.

Donald
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-03T08:47:57-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgj09t$il3$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <kDWdnXSkCbO-p7GiXTWJjQ@giganews.com> <bghnmi$hpa$1@panix1.panix.com> <Ka0Xa.7446$On2.550487@twister.tampabay.rr.com>`

```
In article <Ka0Xa.7446$On2.550487@twister.tampabay.rr.com>,
jce <defaultuser@REMOVETHISBIThotmail.com> wrote:
><docdwarf@panix.com> wrote in message news:bghnmi$hpa$1@panix1.panix.com...

[snip]

>> (Notice the difference between saying 'My number is' and 'Let me give you
>> this number'... no misrepresentation there.)
…[3 more quoted lines elided]…
>Knight...

It might be wise to recall the habit Nobility has of imitating Royalty.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 13)_

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-08-03T20:33:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<virdvuln3iv66c@corp.supernews.com>`
- **In-Reply-To:** `<kDWdnXSkCbO-p7GiXTWJjQ@giganews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgeko1$g3a$3@aklobs.kc.net.nz> <bgeuq2$j3p$1@panix1.panix.com> <3f2b1947_4@news.athenanews.com> <bgg7mn$qkb$1@panix1.panix.com> <kDWdnXSkCbO-p7GiXTWJjQ@giganews.com>`

```
JerryMouse wrote:

> When asked: "What is your ZIP code?" "What is your birthday?" "What is your
> email address?" "Do you want to have sex?" and literally hundreds of other
> questions, often the best response is another question.

Do they really even have to ask us guys that 4th one?
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 12)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-08-03T05:15:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rT0Xa.7541$On2.553731@twister.tampabay.rr.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgeko1$g3a$3@aklobs.kc.net.nz> <bgeuq2$j3p$1@panix1.panix.com> <3f2b1947_4@news.athenanews.com> <bgg7mn$qkb$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:bgg7mn$qkb$1@panix1.panix.com...
> In article <3f2b1947_4@news.athenanews.com>,
>snip snip
…[3 more quoted lines elided]…
>snip snip

The Invading forces of France have the King of England and his 7 subjects on
trial.

Roi : "To save your heads,  could each of you answer my question with an
answer that's a question?"

DD   : Answering a question with a question is no answer at all.

Roi :off with his head

Subject 1: Is the answer to you question a yes or no answer?

Roi : off with his head - that's not an answer

Subject 2: Yes ?

Roi :off with his head  - that's not a really a question

Subject 3: No  ?

Roi :off with his head  - that's not a really a question

Subject 4: I believe you incorrectly beheaded Subject 1 because the subject
did answer - that is, by definition, said or did something to deal with a
question - and it was it in the form of a question.

Roi :that wasn't - off with his head

Subject 5:  Will I live if I answer the question correctly?

Roi : good job Subject 4 was before you

Ghost of DD: ---humph -- that was no answer at all........

Subject 6:  Yeah, whatever 5 said.

Roi : off with his head  - he's a dumbass

Subject 7:  I forgot the question can you repeat it?

Roi :good job Subject 4 was before you

Ghost of DD: ---humph -- that was just evasive...he should have said made it
non iterrogative.."If the question were repeated, I could answer the
question".

......

JCE
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 9)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-08-01T22:11:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zX6dnTkDWfRMtraiXTWJkA@giganews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3f29a8c9_3@news.athenanews.com> <95mWa.6609$K4.290412@twister.tampabay.rr.com> <bgdlmn$hov$1@panix1.panix.com> <bgeko1$g3a$3@aklobs.kc.net.nz>`

```
Richard Plinston wrote:
> docdwarf@panix.com wrote:
>
…[6 more quoted lines elided]…
>  Is answering a question with a question any sort of answer at all ?

To the degree it give the questioner insight sufficient to solve the initial
and subsequent problems, it is the best possible answer.

Light some kindling, and you warm someone for an hour;
Set him afire, and you warm him for the rest of his life.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-02T07:38:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgg7r6$r0i$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgdlmn$hov$1@panix1.panix.com> <bgeko1$g3a$3@aklobs.kc.net.nz> <zX6dnTkDWfRMtraiXTWJkA@giganews.com>`

```
In article <zX6dnTkDWfRMtraiXTWJkA@giganews.com>,
JerryMouse <nospam@bisusa.com> wrote:
>Richard Plinston wrote:
>> docdwarf@panix.com wrote:
…[10 more quoted lines elided]…
>and subsequent problems, it is the best possible answer.

As stated in a previous posting:  to the degree that it is used as a dodge 
and that it can be stated in a manner other than interrogatory it is 
always equally bad.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 11)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-08-02T13:12:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0308021212.30f0a9f6@posting.google.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgdlmn$hov$1@panix1.panix.com> <bgeko1$g3a$3@aklobs.kc.net.nz> <zX6dnTkDWfRMtraiXTWJkA@giganews.com> <bgg7r6$r0i$1@panix1.panix.com>`

```
docdwarf@panix.com wrote 

> >To the degree it give the questioner insight sufficient to solve the initial
> >and subsequent problems, it is the best possible answer.
…[3 more quoted lines elided]…
> always equally bad.

Do you think that Kings should always have their questions answered ?

What about mere mortals, should they be given the same results for their demands ?
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-02T21:18:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bghnsl$iml$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <zX6dnTkDWfRMtraiXTWJkA@giganews.com> <bgg7r6$r0i$1@panix1.panix.com> <217e491a.0308021212.30f0a9f6@posting.google.com>`

```
In article <217e491a.0308021212.30f0a9f6@posting.google.com>,
Richard <riplin@Azonic.co.nz> wrote:
>docdwarf@panix.com wrote 
>
…[7 more quoted lines elided]…
>Do you think that Kings should always have their questions answered ?

I have not spent enough time thinking about Kings and their questions to 
have arrived to a conclusion about this.

>
>What about mere mortals, should they be given the same results for their 
>demands ?

If the King is a man and all men are mortal, then... just as it was 
before, answering a question with a question is no answer at all.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 11)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-08-02T17:27:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qimdnailruYjp7GiXTWJiw@giganews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgdlmn$hov$1@panix1.panix.com> <bgeko1$g3a$3@aklobs.kc.net.nz> <zX6dnTkDWfRMtraiXTWJkA@giganews.com> <bgg7r6$r0i$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <zX6dnTkDWfRMtraiXTWJkA@giganews.com>,
> JerryMouse <nospam@bisusa.com> wrote:
…[17 more quoted lines elided]…
> always equally bad.

Nope. What if whether you answer the question is predicated on the
motivation behind the asking?
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-02T21:22:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgho51$k40$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <zX6dnTkDWfRMtraiXTWJkA@giganews.com> <bgg7r6$r0i$1@panix1.panix.com> <qimdnailruYjp7GiXTWJiw@giganews.com>`

```
In article <qimdnailruYjp7GiXTWJiw@giganews.com>,
JerryMouse <nospam@bisusa.com> wrote:
>docdwarf@panix.com wrote:
>> In article <zX6dnTkDWfRMtraiXTWJkA@giganews.com>,
…[21 more quoted lines elided]…
>motivation behind the asking?

Yep.  If your answer depends on data you do not possess then obtaining
those data without using a question might be done in a manner similar to
saying 'I don't believe I can answer that without knowing (data)'... as
though people are capable of knowing their own motives (La Rochefoucauld,
anyone?) or would respond with them honestly if asked.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 5)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-31T23:59:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<14iWa.82458$0v4.5493566@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <Jc%Va.81309$0v4.5405133@bgtnsc04-news.ops.worldnet.att.net> <3F298597.2D4FC34D@mb.sympatico.ca> <E%fWa.78960$3o3.5413038@bgtnsc05-news.ops.worldnet.att.net>`

```

"Hugh Candlin" <no@spam.com> wrote in message
news:E%fWa.78960$3o3.5413038@bgtnsc05-news.ops.worldnet.att.net...
|
| Peter Lacey <lacey@mb.sympatico.ca> wrote in message
…[4 more quoted lines elided]…
| > style.  Fair enough.  But all the points made in its favour are very
good
| and
| > work exactly as stated.  Just the fact that it's easier to navigate the
| listing
| > based on the paragraph prefixes makes it worthwhile.   Your note "only
if
| they
| > are in sequence" is kind of mind-boggling: can you seriously imagine
…[7 more quoted lines elided]…
| of a viewpoint, and capable of seeing the big picture.

Hugh,

Did you read your post?

Here are some snips:

|> but IN GENERAL, I have viewed this as
|> "yet another" style-only issue, i.e. YMMV.

|It is definitely not.  It is excellent coding practice.

Maybe you could have phrased it better.

|You missed the most important one.  Prevention of looping.
|Do not ever call a lower-numbered paragraph.  It is that simple.

Why is this the MOST important one?
It might be another reason, but the most important one, I don't think so.

| Until your post, I was becoming seriously depressed at the antagonistic
| and cliquish attitude of most of the respondents, who seem to have
…[3 more quoted lines elided]…
| and misinterpretations.

"browbeating of others with their own point of view"
could be associate with your post.

We all learn from each other, sometimes we're right, other times not.
You didn't express a point of view, you came on like a Nazi implying your
way is the best darned thing since sliced bread, and everyone should follow
suit.

| This attitude renders the NG worthless as a forum for civil discourse.
| One is forced to shake one's head in dismay and ignore the more
…[3 more quoted lines elided]…
|
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 6)_

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-08-02T01:15:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NBycna_Kbq961baiXTWJkA@comcast.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <Jc%Va.81309$0v4.5405133@bgtnsc04-news.ops.worldnet.att.net> <3F298597.2D4FC34D@mb.sympatico.ca> <E%fWa.78960$3o3.5413038@bgtnsc05-news.ops.worldnet.att.net> <14iWa.82458$0v4.5493566@bgtnsc04-news.ops.worldnet.att.net>`

```

"Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
news:14iWa.82458$0v4.5493566@bgtnsc04-news.ops.worldnet.att.net...
>
> "Hugh Candlin" <no@spam.com> wrote in message
…[5 more quoted lines elided]…
> | > Judging by the sharpness of your comments, I'd guess that you don't
use
> | this
> | > style.  Fair enough.  But all the points made in its favour are very
> good
> | and
> | > work exactly as stated.  Just the fact that it's easier to navigate
the
> | listing
> | > based on the paragraph prefixes makes it worthwhile.   Your note "only
…[34 more quoted lines elided]…
> | that having posted frequently somehow confers superior powers and
insight,
> | and sanctions the browbeating of others with their own point of view
> | and misinterpretations.
…[6 more quoted lines elided]…
> way is the best darned thing since sliced bread, and everyone should
follow
> suit.


    NOTE - This thread is now officially closed, due to use of the word
"Nazi".




>
> | This attitude renders the NG worthless as a forum for civil discourse.
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 4)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-31T23:44:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MRhWa.82432$0v4.5492499@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <Jc%Va.81309$0v4.5405133@bgtnsc04-news.ops.worldnet.att.net> <3F298597.2D4FC34D@mb.sympatico.ca>`

```

"Peter Lacey" <lacey@mb.sympatico.ca> wrote in message
news:3F298597.2D4FC34D@mb.sympatico.ca...
| Harley wrote:
|
…[5 more quoted lines elided]…
| > | > Over the last year (or more), I have seen a number of people talking
for
| > | and
| > | > against "numbered prefixes" (particularly the
…[33 more quoted lines elided]…
| Judging by the sharpness of your comments, I'd guess that you don't use
this
| style.  Fair enough.  But all the points made in its favour are very good
and
| work exactly as stated.

Except the part about copying code into a paragraph that is identical to the
source paragraph, which increases the maintenance effort needlessly.
The idea of the Paragraph (or section) is that you don't need more than one
copy in a program. You can perform it from multiple locations.

| Just the fact that it's easier to navigate the listing
| based on the paragraph prefixes makes it worthwhile.

I don't use listings, I use the text editor.
It's faster, and I can find thinks in a second or 2.
On my old PC, I would double click the PERFORM, and it located the paragraph
for me. (I have to rewrite the macro, forgot to copy it from my old PC.)

|Your note "only if they
| are in sequence" is kind of mind-boggling: can you seriously imagine using
| numeric prefixes that are out of sequence????

I've seen the numbers out of sequence scenario more than once.
It is rare, but it happens.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 4)_

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-07-31T20:58:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vijib39r8idl04@corp.supernews.com>`
- **In-Reply-To:** `<3F298597.2D4FC34D@mb.sympatico.ca>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <Jc%Va.81309$0v4.5405133@bgtnsc04-news.ops.worldnet.att.net> <3F298597.2D4FC34D@mb.sympatico.ca>`

```
Peter Lacey wrote:

> Judging by the sharpness of your comments, I'd guess that you don't use this
> style.  Fair enough.  But all the points made in its favour are very good and
…[3 more quoted lines elided]…
> numeric prefixes that are out of sequence????

As a matter of fact, I can.

<war_story>
There was a program that had an open deficiency report for over 6 
months.  We were coming up to a maintenance release, but this guy 
couldn't figure out what was wrong.  My supervisor spoke up, "He can do 
it in 2 weeks..."  When I opened the code, I was astounded.  There was a 
24 x 7 x 14 table, some sort files, and some other really strange stuff. 
  I had no clue what it was supposed to do, so I thought I would just 
run it with a "monitor" (a debugging option where every data item is 
displayed before and after it's changed, and all paragraphs are printed 
as they are executed).

I took it home over a weekend and began to pore over it - and I noticed 
that the paragraph numbers were -not- in numerical order.  I was 
starting to understand why this other guy had worked it for 6 months and 
gotten nowhere.  (In his defence, it wasn't the -only- thing he was 
working...)  Anyway, after about a week of looking over things, I found 
in this monitor where the bad data showed up.  I looked at the code, and 
everything looked exactly right.

Another lead programmer suggested that I look at the working-storage 
variables that the code was manipulating.  The field was a 5-position 
ordinal date (YYDDD).  When I looked, I found that in the sending field 
it was a Pic 9(05) Comp, and in the receiving field it was a Pic X(05). 
  Changing the receiving field to a Pic 9(05) was all that was required 
to correct the deficiency.

I don't begrudge the experience - I always enjoy a good challenge, and 
it taught me to include a look or 2 at working-storage when apparently 
good code appears to be doing bad things.  However, the non-sequential 
paragraph numbers really sucked.
</war_story>
```

##### ↳ ↳ Re: Numbered prefixes

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-31T16:33:43+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f289ce2_8@news.athenanews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net>`

```

"Hugh Candlin" <no@spam.com> wrote in message
news:apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net...
>
> William M. Klein <wmklein@nospam.netcom.com> wrote in message
…[14 more quoted lines elided]…
>

So, what if I want to get another input record (having flushed the one I
just read) but I DON'T want to exit my "Get some Input" function until I
have something worth processing? (The rest of my code expects this function
to return "filtered" record.)

Anyone who relies on a numbering system, rather than using logic, to prevent
looping, deserves whatever they get....

> Another bonus is that the paragraph number confers uniqueness,
> so that you can use the same block(s) of code multiple times
…[3 more quoted lines elided]…
>

Oh yeah...!!! Duplicate code with different labels in it. (There is ALWAYS a
better way than this <G>).


> Another benefit is that the paragraph number gives you an idea
> of where physically in the program the code is located.
> That can help while jumping around in the editor.
>

Or not...

> Another is that the paragraph number ranges themselves
> can be allocated to indicate similarity of function.
>

That's why I put them in a SECTION.

> There are probably more benefits, but the basic idea is that
> I wouldn't write a program any other way, given my choice.
>

Good. And I respect your right to do it whatever way you want. You're a
"Programmer", right?

Well, so am I. So how about granting me the same latitude?

> > but IN GENERAL, I have viewed this as
> > "yet another" style-only issue, i.e. YMMV.
>
> It is definitely not.  It is excellent coding practice.

At least in ONE person's view...

Bill is right. This is a matter of style. Just because some people agree
with this style does not change the fact that it is a matter of style.

> >
> > In other words, if you have a procedure-name of  "0123-Para" you are
…[3 more quoted lines elided]…
> > (and possibly vendor-specific) reserved word IN THE FUTURE.  On the
other
> > hand, if you call you procedure "Something-Procedure" it *might* end up
> > causing you maintenance issues in with a future (or other vendor)
…[23 more quoted lines elided]…
> I have never and would never use a single word as a paragraph or data
name.
> I learned that Day One.
>

That would be at the school of "needlessly-verbose-COBOL"?

My point is that if a single word does the job, why use more?


> > P.S. It is a "medium-easy" task to "change" such names in existing
> > programs - and the enhanced REPLACE statement can also solve this
…[6 more quoted lines elided]…
>

It isn't a problem until certain people try and enforce their own opinion as
a standard. If what you have  works for you, then great.

Don't try and make me do it...

Pete.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

- **From:** docdwarf@panix.com
- **Date:** 2003-07-31T04:39:57-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgakkt$9u5$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <3f289ce2_8@news.athenanews.com>`

```
In article <3f289ce2_8@news.athenanews.com>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>
>"Hugh Candlin" <no@spam.com> wrote in message
…[22 more quoted lines elided]…
>to return "filtered" record.)

Oh, I *cannot* resist... this is what you get, then, when you violate the 
Traditions of Yore.  Consider:

 0000-THE-TOP.

     PERFORM 1000-HOUSEKEEPING THRU 1000-EX.

     PERFORM 5000-MAIN-LINE THRU 5000-EX 
      UNTIL NO-MORE-INPUT.

     PERFORM 9000-EOJ THRU 9000-EX.

     GOBACK.

 5000-MAIN-LINE.

     PERFORM 5050-READ-MASTFIL THRU 5050-EX.
     IF NO-MORE-INPUT
         PERFORM 8500-FINAL-TOTALS THRU 8000-EX
         GO TO 5000-EX.
     PERFORM 6000-MATCH-N-EDIT THRU 6000-EX.
     IF NOT ALL-DATA-GOOD
         PERFORM 8300-ERROR-TOTALS THRU 8300-EX
         GO TO 5000-EX.

*** PROCEED PAST HERE ONLY IF ALL MATCHES & EDITS PASSED

     IF CUSTOMER-FROM-HOBOKEN AND ORDERING-SALAMI
         PERFORM 7000-CUSTHOB-ORDSALM THRU 7000-EX.
     IF TODAY-IS-TUESDAY AND NUCLEAR-PHYSICIST-SINGING
        PERFORM 7010-TODTUES THRU 7010-EX.
     IF IN-SHOWER AND I-AM-ENGLANDSKING
        PERFORM 7020-YODEL-GODSAVETHEME THRU 7020-EX.

(please pardon the typos, I didn't try to compile this posting.)

Yes, I know this is Blocky Ugly Old Code... but I also believe that the
classic two-year programmer would have little difficulty following this
for the classic 3:am prod blowup.

Are there any two-year programmers out there who find it difficult to 
determine what this code is doing, where it is doing it and where they 
would put modifications to the code?

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 4)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-07-31T09:32:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-4E9BF6.09324831072003@corp.supernews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <3f289ce2_8@news.athenanews.com> <bgakkt$9u5$1@panix1.panix.com>`

```
Ahhhh -- but you could feed this to a two month Cobol programmer, or 
even a non-Cobol programmer and have no problems:


  X-THE-TOP.  
     Perform INITIAL-HOUSEKEEPING

     Perform READ-MASTFIL
     Perform until NO-MORE-INPUT
        Perform MATCH-N-EDIT
        If ALL-DATA-GOOD
           Perform SKI-SALAMI-AND-SING
        Else
           Perform ERROR-TOTALS
        End-If
        Perform READ-MASTFIL
     End-Perform

     Perform FINAL-TOTALS
     Perform EOJ-CLEANUP
     Goback.

The construction of the loop, complete with exit condition and final 
code is located within a few lines.  No knowledge of that Block Old Ugly 
Style is necessary.

I would wager that you could give this to a Java or Pascal or C 
programmer or even a non-programmer and they would be able to tell you 
what it is doing.  Not the case with the BOUS.



In article <bgakkt$9u5$1@panix1.panix.com>, docdwarf@panix.com wrote:
> 
> Oh, I *cannot* resist... this is what you get, then, when you violate the 
…[43 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 5)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-08-01T04:38:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<S8mWa.6628$K4.290844@twister.tampabay.rr.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <3f289ce2_8@news.athenanews.com> <bgakkt$9u5$1@panix1.panix.com> <joe_zitzelberger-4E9BF6.09324831072003@corp.supernews.com>`

```
"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote in message
news:joe_zitzelberger-4E9BF6.09324831072003@corp.supernews.com...
> Ahhhh -- but you could feed this to a two month Cobol programmer, or
> even a non-Cobol programmer and have no problems:
…[21 more quoted lines elided]…
> what it is doing.  Not the case with the BOUS.

Actually I believe the usual reaction is...what it this crap....this is
COBOL? Jeez...it's so wordy...leave me alone I'm X'ing with my bud on the
latest Web widget service...

JCE
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 4)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-07-31T15:36:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f2928bf.86667557@news.optonline.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <3f289ce2_8@news.athenanews.com> <bgakkt$9u5$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>Yes, I know this is Blocky Ugly Old Code... but I also believe that the
>classic two-year programmer would have little difficulty following this
>for the classic 3:am prod blowup.

This argument is called Dragging Out The Kids. 'Sure, I could write structured
code, but kids wouldn't be able to understand it.' I submit kids would rather
learn to program well than be patronized. I further submit you do it for your
own limitations; kids are just rationalization.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-31T23:55:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgcob3$c5s$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3f289ce2_8@news.athenanews.com> <bgakkt$9u5$1@panix1.panix.com> <3f2928bf.86667557@news.optonline.com>`

```
In article <3f2928bf.86667557@news.optonline.com>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[4 more quoted lines elided]…
>This argument is called Dragging Out The Kids.

No, Mr Wagner, this argument is called the classic 'two-year programmer 
standard'.

>'Sure, I could write structured
>code, but kids wouldn't be able to understand it.'

The code above is quite well structured, Mr Wagner, according to the 
modified Yourdon rules which allow a GO TO directing execution to the 
preceding label, the following EXIT or the ABEND routine.

>I submit kids would rather
>learn to program well than be patronized. I further submit you do it for your
>own limitations; kids are just rationalization.

Your submissions have been noted, Mr Wagner, and found wanting, as they 
seem to have as much or as little basis as any others.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 6)_

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2003-08-01T16:53:34+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5Q9R0vC+zoK$EwzH@ld50macca.demon.co.uk>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3f289ce2_8@news.athenanews.com> <bgakkt$9u5$1@panix1.panix.com> <3f2928bf.86667557@news.optonline.com> <bgcob3$c5s$1@panix1.panix.com>`

```
In message <bgcob3$c5s$1@panix1.panix.com>, docdwarf@panix.com writes
>
>The code above is quite well structured, Mr Wagner, according to the
…[5 more quoted lines elided]…
>
Yourdon allows a goto to a previous label? Tsk. Why would you want to do 
that Doc?
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-08-01T16:53:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bge5ts$ks6$1@peabody.colorado.edu>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <5Q9R0vC+zoK$EwzH@ld50macca.demon.co.uk>`

```

On  1-Aug-2003, Alistair Maclean <alistair@ld50macca.demon.co.uk> wrote:

> >The code above is quite well structured, Mr Wagner, according to the
> >modified Yourdon rules which allow a GO TO directing execution to the
…[6 more quoted lines elided]…
> that Doc?

My guess is because many "structured" languages have commands which do this.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-01T13:36:43-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bge8fb$83t$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3f2928bf.86667557@news.optonline.com> <bgcob3$c5s$1@panix1.panix.com> <5Q9R0vC+zoK$EwzH@ld50macca.demon.co.uk>`

```
In article <5Q9R0vC+zoK$EwzH@ld50macca.demon.co.uk>,
Alistair Maclean  <alistair@ld50macca.demon.co.uk> wrote:
>In message <bgcob3$c5s$1@panix1.panix.com>, docdwarf@panix.com writes
>>
…[8 more quoted lines elided]…
>that Doc?

I don't want to do that, so I don't do it... but perhaps one might have 
seen something like:

    PERFORM 2000-READ-N-PROCESS THRU 2000-EX
     UNTIL NO-MORE-INPUT.

2000-READ-N-PROCESS.

    READ INFILE INTO WS-REC
     AT END MOVE 'Y' TO WS-INFILE-IND
            GO TO 2000-EX.

    IF WS-REC-DEPTNO NOT = LK-PROCESS-DEPTNO
        GO TO 2000-READ-N-PROCESS.

It ain't *my* style (said Casey) but it is not one which I find surprising 
or unintelligible.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 8)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-08-01T21:37:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<E4BWa.80388$3o3.5521939@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3f2928bf.86667557@news.optonline.com> <bgcob3$c5s$1@panix1.panix.com> <5Q9R0vC+zoK$EwzH@ld50macca.demon.co.uk> <bge8fb$83t$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:bge8fb$83t$1@panix1.panix.com...
>
> I don't want to do that, so I don't do it... but perhaps one might have
…[14 more quoted lines elided]…
> It ain't *my* style (said Casey) but it is not one which I find
surprising
> or unintelligible.

If the GO TOs bother you,
or the lack of specific ELSE statements bothers you
(no indication that the programmer considered that logic path)
you could always use this construction style.........

1000-MAINLINE-PROC                                        SECTION.

        PERFORM 9000-DEPTFILE-READ  THRU  9000-EXIT.

        IF                DEPTFILE-AT-EOF
                            PERFORM
                            9100-DEPTFILE-VOID  THRU  9100-EXIT
        ELSE
                            PERFORM
                            2000-DEPTFILE-LOOP  THRU  2000-EXIT
                                   UNTIL NO-MORE-INPUT.
1000-EXIT.
        EXIT.

2000-DEPTFILE-LOOP                                          SECTION.

        IF               WS-REC-DEPTNO                  =
LK-PROCESS-DEPTNO
                           PERFORM
                           3000-DEPTFILE-SAME  THRU  3000-EXIT
        ELSE
                           PERFORM
                           4000-DEPTFILE-CHNG  THRU  4000-EXIT.

        PERFORM 9000-DEPTFILE-READ  THRU  9000-EXIT.

2000-EXIT.
        EXIT.

3000-DEPTFILE-SAME                                          SECTION.

         (Some "SAME" logic omitted)

3000-EXIT.
        EXIT.

4000-DEPTFILE-CHNG                                          SECTION.

         (Some "DIFF" logic omitted)

4000-EXIT.
        EXIT.

9000-DEPTFILE-READ                                           SECTION.

        READ     INFILE                             INTO  WS-REC
                       AT  END
                       MOVE     'Y'                         TO
WS-INFILE-IND.
9000-EXIT.
        EXIT.

9100-DEPTFILE-VOID                                           SECTION.

        (Some "Empty File" processing omitted)

9100-EXIT.
        EXIT.

*=== END OF PROGRAM [PROGNAME]
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-01T20:01:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgev0q$kmk$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <5Q9R0vC+zoK$EwzH@ld50macca.demon.co.uk> <bge8fb$83t$1@panix1.panix.com> <E4BWa.80388$3o3.5521939@bgtnsc05-news.ops.worldnet.att.net>`

```
In article <E4BWa.80388$3o3.5521939@bgtnsc05-news.ops.worldnet.att.net>,
Hugh Candlin <no@spam.com> wrote:
>
><docdwarf@panix.com> wrote in message news:bge8fb$83t$1@panix1.panix.com...
…[24 more quoted lines elided]…
>1000-MAINLINE-PROC                                        SECTION.

I am made of stuff sufficiently stern that the GO TO does not bother me, 
no... but the code-snippet above was in response to a question, not a 
suggestion of how one should do anything.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 7)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-08-02T00:33:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c3588d$997f5dc0$f58bf243@chottel>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3f289ce2_8@news.athenanews.com> <bgakkt$9u5$1@panix1.panix.com> <3f2928bf.86667557@news.optonline.com> <bgcob3$c5s$1@panix1.panix.com> <5Q9R0vC+zoK$EwzH@ld50macca.demon.co.uk>`

```
Ah Yourdon. I remember receiving his newsletter back when it was free. I
bought a tape containing structured programming macros by Gary Neumeth of
Cleveland Trust for $5.

They were so high on "their way" of structured programming. I remember they
were developing a C compiler using "their way" to demonstrate "their
superiority". I don't remember ever hearing about it being completed.

<end of top post>

Alistair Maclean <alistair@ld50macca.demon.co.uk> wrote in article
<5Q9R0vC+zoK$EwzH@ld50macca.demon.co.uk>...
> In message <bgcob3$c5s$1@panix1.panix.com>, docdwarf@panix.com writes
> >
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-07-31T13:08:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0307311208.55e7a904@posting.google.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <3f289ce2_8@news.athenanews.com> <bgakkt$9u5$1@panix1.panix.com>`

```
docdwarf@panix.com wrote

> Yes, I know this is Blocky Ugly Old Code... but I also believe that the
> classic two-year programmer would have little difficulty following this
…[4 more quoted lines elided]…
> would put modifications to the code?

There is probably no problem at all in following what the code is
_supposed_ to do, the problem is finding out what the code is not
doing right.

When there are PERFORM .. THRUs, with potential for GO TO xxx-exit,
then _any_ of them may have had an additional paragraph inserted in
the wrong place, or had its exit paragraph misplaced or the code is
using the wrong one.  When a non-obvious problem occurs the only
solution is to manually check every single perform scope to ensure it
is coded correctly.

Judson (not seen him here for a while) used a checking program that
ensured that labels were correctly formed and used.  Without this the
problem may be anywhere.  A wrong GO TO xxx-exit _may_ be used without
causing any noticable problem until a particular set of conditions
exist, or it may be that path was never followed until now.

If you don't have any GO TO xxx-exit then why is THRU being used at
all?
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 5)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-01T00:05:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<z9iWa.82479$0v4.5494696@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <3f289ce2_8@news.athenanews.com> <bgakkt$9u5$1@panix1.panix.com> <217e491a.0307311208.55e7a904@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0307311208.55e7a904@posting.google.com...
| docdwarf@panix.com wrote
|
…[26 more quoted lines elided]…
| all?

Maybe they get paid by the word.

Sometimes I find PERFORM  .. THRU several paragraphs.
It saved coding 2 or 3 PERFORMS.
I usually change this when I find it.

I agree with your position.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-01T13:55:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgchai$iuf$1@aklobs.kc.net.nz>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgakkt$9u5$1@panix1.panix.com> <217e491a.0307311208.55e7a904@posting.google.com> <z9iWa.82479$0v4.5494696@bgtnsc04-news.ops.worldnet.att.net>`

```
Harley wrote:

> Sometimes I find PERFORM  .. THRU several paragraphs.
> It saved coding 2 or 3 PERFORMS.

<shudder>.  There is just so much wrong with that, I don't know where to 
start.

Consider if exit paragraphs were used too.  There may be:

   3120-Validate-HDiv.
   3120-exit.
   3130-Validate-PDiv.
   3130-exit.
   3140-Validate-TDiv.
   3140-exit.

and a line above those does:

   PERFORM 3120-Validate-HDiv THRU 3140-exit

It _might_ be a keying error and was supposed to be 3120-exit.

If we wanted to find every place that performed 3130-Validate-PDiv this 
would not show as one of them.

If we were to add a new 3135-Validate-RDiv then this would be done without 
being able to find out where except by a complete detailed search of the 
whole program.

However, if a grep of the code shows no occurances of the words THRU or 
SECTION in PD, then one can be sure that such abuses do not arise.

(actually it is somewhat more complicated because THRU may be on a WHEN).

> I usually change this when I find it.

I would suggest _always_.
 
> I agree with your position.

Geez, how can one start a decent argu^H^H^H^Hdiscussion, if people agree.  
I'll have to change my stance now    ;-)
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 7)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-01T12:03:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hGsWa.83071$0v4.5548563@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgakkt$9u5$1@panix1.panix.com> <217e491a.0307311208.55e7a904@posting.google.com> <z9iWa.82479$0v4.5494696@bgtnsc04-news.ops.worldnet.att.net> <bgchai$iuf$1@aklobs.kc.net.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:bgchai$iuf$1@aklobs.kc.net.nz...
| Harley wrote:
|
…[4 more quoted lines elided]…
| start.

You have to be kind when the person who wrote is the manager you report to.

|
| Consider if exit paragraphs were used too.  There may be:
…[10 more quoted lines elided]…
|    PERFORM 3120-Validate-HDiv THRU 3140-exit

What I normally do is change the PERFORM THRU coding, to a format that makes
visual scanning easier when I first enter uncharted waters (maintain a
program).

i.e.
PERFORM 3120-Validate-HDiv THRU 3140-exit
becomes
PERFORM 3120-Validate-HDiv
        THRU 3140-exit

That's how I spot most of these gems.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-31T23:58:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgcogp$d5d$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3f289ce2_8@news.athenanews.com> <bgakkt$9u5$1@panix1.panix.com> <217e491a.0307311208.55e7a904@posting.google.com>`

```
In article <217e491a.0307311208.55e7a904@posting.google.com>,
Richard <riplin@Azonic.co.nz> wrote:
>docdwarf@panix.com wrote
>
…[10 more quoted lines elided]…
>doing right.

That is a problem with most code I have seen, Mr Plinston... the subtle 
error tends to be... subtle.

>
>When there are PERFORM .. THRUs, with potential for GO TO xxx-exit,
…[4 more quoted lines elided]…
>is coded correctly.

I seem to recall such a function being part of a Production Review... have 
such practises been ruled out in the interest of efficiency?

[snip]

>If you don't have any GO TO xxx-exit then why is THRU being used at
>all?

To allow for flexibility in future modifications, of course.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-01T19:41:52+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgd5jh$rn5$1@aklobs.kc.net.nz>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgakkt$9u5$1@panix1.panix.com> <217e491a.0307311208.55e7a904@posting.google.com> <bgcogp$d5d$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>>> Yes, I know this is Blocky Ugly Old Code... but I also believe that the
>>> classic two-year programmer would have little difficulty following this
…[4 more quoted lines elided]…
>>> would put modifications to the code?

> That is a problem with most code I have seen, Mr Plinston... the subtle
> error tends to be... subtle.

Which may, of course, thusly provide the answer of 'yes' to your question.

> I seem to recall such a function being part of a Production Review... have
> such practises been ruled out in the interest of efficiency?

You may find it difficult to assemble a quorum at 3am.

>>If you don't have any GO TO xxx-exit then why is THRU being used at
>>all?
> 
> To allow for flexibility in future modifications, of course.

What foresight - to write all your code to allow for the possibility of 
some future programmer wanting to stick in a GO TO.  I, on the other hand, 
save much effort by ensuring that no such thing can be done to mine.

It is just a different approach.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-01T08:24:28-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgdm5s$jog$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <217e491a.0307311208.55e7a904@posting.google.com> <bgcogp$d5d$1@panix1.panix.com> <bgd5jh$rn5$1@aklobs.kc.net.nz>`

```
In article <bgd5jh$rn5$1@aklobs.kc.net.nz>,
Richard Plinston  <riplin@Azonic.co.nz> wrote:
>docdwarf@panix.com wrote:
>
…[11 more quoted lines elided]…
>Which may, of course, thusly provide the answer of 'yes' to your question.

Mr Plinston, many things 'may' do other things... but you seem to have 
removed the statements to which I was responding (it is difficult to 
determine without the presence of indicators of editing); I'm not sure 
what it is you said to which I was replying here.

>
>> I seem to recall such a function being part of a Production Review... have
>> such practises been ruled out in the interest of efficiency?
>
>You may find it difficult to assemble a quorum at 3am.

Mr Plinston, the context of these statements might indicate the validity 
of your observation.

>
>>>If you don't have any GO TO xxx-exit then why is THRU being used at
…[6 more quoted lines elided]…
>save much effort by ensuring that no such thing can be done to mine.

Mr Plinston, I do not believe that I am capable of interpreting all 
possible future contingencies at all times and that it is better to allow 
for more contingencies than fewer, aye.

>
>It is just a different approach.

Allowing for more on heaven and earth than is dreamt of in my philosophies 
is certainly different than 'Everything from here on out must comply with 
my views of what code is to be', definitely... have you been speaking with 
Mr Dilworth recently?

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-08-02T01:36:47+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f2a6da7_9@news.athenanews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <217e491a.0307311208.55e7a904@posting.google.com> <bgcogp$d5d$1@panix1.panix.com> <bgd5jh$rn5$1@aklobs.kc.net.nz> <bgdm5s$jog$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:bgdm5s$jog$1@panix1.panix.com...
> In article <bgd5jh$rn5$1@aklobs.kc.net.nz>,
>
…[4 more quoted lines elided]…
>

LOL!

O Yeah, Doc, Rich and Tone are real big buddies...<G>

BTW, The role of Horatio does not become you... You're definitely more a
Cassius.... <G>.

Pete.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-01T13:39:27-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bge8kf$8h2$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgd5jh$rn5$1@aklobs.kc.net.nz> <bgdm5s$jog$1@panix1.panix.com> <3f2a6da7_9@news.athenanews.com>`

```
In article <3f2a6da7_9@news.athenanews.com>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:bgdm5s$jog$1@panix1.panix.com...
…[10 more quoted lines elided]…
>O Yeah, Doc, Rich and Tone are real big buddies...<G>

From what's been posted here it seems they both have rather high ideas of 
their own styles, no?

>
>BTW, The role of Horatio does not become you... You're definitely more a
>Cassius.... <G>.

I'm a bad man, Mr Dashwood... veeeeerrrrryyyyy baaaaaddd maaaaaan, I'm 
pretty, I'm smart, I float like a butterfly, sting like a bee...

... whoops, different Cassius.  I get confused so easily.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-08-02T13:56:11+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f2b1af6_2@news.athenanews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgd5jh$rn5$1@aklobs.kc.net.nz> <bgdm5s$jog$1@panix1.panix.com> <3f2a6da7_9@news.athenanews.com> <bge8kf$8h2$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:bge8kf$8h2$1@panix1.panix.com...
> In article <3f2a6da7_9@news.athenanews.com>,
> Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:bgdm5s$jog$1@panix1.panix.com...
> >> In article <bgd5jh$rn5$1@aklobs.kc.net.nz>,
> >>
> >> Allowing for more on heaven and earth than is dreamt of in my
philosophies
> >> is certainly different than 'Everything from here on out must comply
with
> >> my views of what code is to be', definitely... have you been speaking
with
> >> Mr Dilworth recently?
> >>
…[7 more quoted lines elided]…
>

That may be true or false, but Richard makes worthwhile contributions here,
and has done for a considerable period of time.

I'll say no more.


> >
> >BTW, The role of Horatio does not become you... You're definitely more a
…[6 more quoted lines elided]…
>
Ah, now you're talking about one of my all time heroes <G>... We'll never
see his like again.

Pete.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-02T07:40:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgg7vf$rqc$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3f2a6da7_9@news.athenanews.com> <bge8kf$8h2$1@panix1.panix.com> <3f2b1af6_2@news.athenanews.com>`

```
In article <3f2b1af6_2@news.athenanews.com>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:bge8kf$8h2$1@panix1.panix.com...
…[23 more quoted lines elided]…
>I'll say no more.

Then you'll not be asked to, for now.

>
>
…[10 more quoted lines elided]…
>see his like again.

A combination of person, time and place that seems more archetype than 
stereotype, aye.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 7)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-01T12:30:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<U3tWa.83089$0v4.5551945@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgakkt$9u5$1@panix1.panix.com> <217e491a.0307311208.55e7a904@posting.google.com> <bgcogp$d5d$1@panix1.panix.com> <bgd5jh$rn5$1@aklobs.kc.net.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:bgd5jh$rn5$1@aklobs.kc.net.nz...
| docdwarf@panix.com wrote:
|
| What foresight - to write all your code to allow for the possibility of
| some future programmer wanting to stick in a GO TO.  I, on the other hand,
| save much effort by ensuring that no such thing can be done to mine.

Richard,
From some of your other posts, I find that our styles are very similar.
I can tell you from experience, somebody will put THRUs, EXITs, and GO TOs
in the code.
Sometimes you don't know if you should laugh or cry.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-02T09:22:29+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgelmb$gsg$2@aklobs.kc.net.nz>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgcogp$d5d$1@panix1.panix.com> <bgd5jh$rn5$1@aklobs.kc.net.nz> <U3tWa.83089$0v4.5551945@bgtnsc04-news.ops.worldnet.att.net>`

```
Harley wrote:

> From some of your other posts, I find that our styles are very similar.
> I can tell you from experience, somebody will put THRUs, EXITs, and GO TOs
> in the code.

> Sometimes you don't know if you should laugh or cry.

I would yell.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 9)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-01T23:56:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O6DWa.83949$0v4.5598800@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgcogp$d5d$1@panix1.panix.com> <bgd5jh$rn5$1@aklobs.kc.net.nz> <U3tWa.83089$0v4.5551945@bgtnsc04-news.ops.worldnet.att.net> <bgelmb$gsg$2@aklobs.kc.net.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:bgelmb$gsg$2@aklobs.kc.net.nz...
| Harley wrote:
|
| > From some of your other posts, I find that our styles are very similar.
| > I can tell you from experience, somebody will put THRUs, EXITs, and GO
TOs
| > in the code.
|
| > Sometimes you don't know if you should laugh or cry.
|
| I would yell.

I usually shake my head, and chuckle a bit.
Yelling doesn't do any good.
The "damage" is usually minor, so I fix it.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 7)_

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2003-08-01T16:55:41+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<igNX4bD91oK$EwyV@ld50macca.demon.co.uk>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgakkt$9u5$1@panix1.panix.com> <217e491a.0307311208.55e7a904@posting.google.com> <bgcogp$d5d$1@panix1.panix.com> <bgd5jh$rn5$1@aklobs.kc.net.nz>`

```
In message <bgd5jh$rn5$1@aklobs.kc.net.nz>, Richard Plinston 
<riplin@Azonic.co.nz> writes
>docdwarf@panix.com wrote:
>
…[8 more quoted lines elided]…
>
Me too. We don't have GOTO in Assembler        ;-)
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 8)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-01T19:13:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dZyWa.80159$3o3.5511818@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgakkt$9u5$1@panix1.panix.com> <217e491a.0307311208.55e7a904@posting.google.com> <bgcogp$d5d$1@panix1.panix.com> <bgd5jh$rn5$1@aklobs.kc.net.nz> <igNX4bD91oK$EwyV@ld50macca.demon.co.uk>`

```

"Alistair Maclean" <alistair@ld50macca.demon.co.uk> wrote in message
news:igNX4bD91oK$EwyV@ld50macca.demon.co.uk...
| In message <bgd5jh$rn5$1@aklobs.kc.net.nz>, Richard Plinston
| <riplin@Azonic.co.nz> writes
…[8 more quoted lines elided]…
| >some future programmer wanting to stick in a GO TO.  I, on the other
hand,
| >save much effort by ensuring that no such thing can be done to mine.
| >
| Me too. We don't have GOTO in Assembler        ;-)

I could write you a Macro, if you like.
Then you could say you didn't use it by choice.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 9)_

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2003-08-01T22:15:15+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RF6LBGBjhtK$EwnY@ld50macca.demon.co.uk>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgakkt$9u5$1@panix1.panix.com> <217e491a.0307311208.55e7a904@posting.google.com> <bgcogp$d5d$1@panix1.panix.com> <bgd5jh$rn5$1@aklobs.kc.net.nz> <igNX4bD91oK$EwyV@ld50macca.demon.co.uk> <dZyWa.80159$3o3.5511818@bgtnsc05-news.ops.worldnet.att.net>`

```
In message <dZyWa.80159$3o3.5511818@bgtnsc05-news.ops.worldnet.att.net>, 
Harley <dennis.harleyNoSpam@worldnet.att.net> writes
>
>"Alistair Maclean" <alistair@ld50macca.demon.co.uk> wrote in message
…[20 more quoted lines elided]…
>

Nice one.

I'm perfectly capable of writing a macro myself, but thanks for the 
offer. I'll stick to BNZ and the others.
```

##### ↳ ↳ Re: Numbered prefixes

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-01T00:37:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bg9og2$ber$1@aklobs.kc.net.nz>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net>`

```
Hugh Candlin wrote:

> You missed the most important one.  Prevention of looping.
> Do not ever call a lower-numbered paragraph.  It is that simple.

While I can see how this would eliminate recursion, it would seem to be 
that a decent design approach eliminates recursion anyway.
 
> Another bonus is that the paragraph number confers uniqueness,
> so that you can use the same block(s) of code multiple times
> in the same program if the solution calls for it and there is no better
> way,
> by simply incrementing the numbers to a new range.

It seems to me that the only reason you would duplicate a block of code is 
to conserve the rule above.  If one is not allowed to just perform a block 
of existing code 'because it has the wrong number' then copy it and give it 
a new number.  Are you paid by the line of code of what ?

> Another benefit is that the paragraph number gives you an idea
> of where physically in the program the code is located.
> That can help while jumping around in the editor.

Get better tools.

I group paragraphs by functional use.  Layering using paragraph prefixes 
tends to create a resistence to breaking code down into simpler structures, 
especially when it involves moving blocks of code around to satifying some 
placement rules.
 
> Another is that the paragraph number ranges themselves
> can be allocated to indicate similarity of function.

What's wrong with using names to do that ?
 
> There are probably more benefits, but the basic idea is that
> I wouldn't write a program any other way, given my choice.

It's what you are used to.  You _know_ that xx24x-paragarphs are located 
precisely .here. and do exactly .this., probably the same in every program 
you have written in the last couple of decades.

If you look at my programs you would probably be completely lost.  You 
would be checking for things that don't exist, you wouldn't know where to 
look for anything. You would think of them as un-ordered, almost random. 
But then my tools allow this because they find things for me.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2003-07-31T16:20:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F298813.A304C12D@mb.sympatico.ca>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <bg9og2$ber$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote:

> I group paragraphs by functional use.  Layering using paragraph prefixes
> tends to create a resistence to breaking code down into simpler structures,
> especially when it involves moving blocks of code around to satifying some
> placement rules.

Aren't generalizations fun?  If the design is done well, the style doesn't
matter.  Simple structures can be done using any method of expression.


<snip> <ooops>
If you look at my programs you would probably be completely lost.  You

> would be checking for things that don't exist, you wouldn't know where to
> look for anything. You would think of them as un-ordered, almost random.
> But then my tools allow this because they find things for me.

And this is supposed to be an advantage to your style?  How about TPB who has
to try to fix your code when you aren't available?  Is opacity a virtue?

(TPB is The Poor Bastard who has to do maintenance or emergency fixes.  ALL
coding should be done with TPB in mind.  S/He hasn't got time to figure out
your style & tools).

PL
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-01T10:24:32+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgc4ud$dic$1@aklobs.kc.net.nz>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <bg9og2$ber$1@aklobs.kc.net.nz> <3F298813.A304C12D@mb.sympatico.ca>`

```
Peter Lacey wrote:


> Aren't generalizations fun?  If the design is done well, the style doesn't
> matter.  Simple structures can be done using any method of expression.

If the design is well done it doesn't need crutches, such as keeping 
numbered paragraphs in sequence.   ;-)

> <snip> <ooops>
> If you look at my programs you would probably be completely lost.  You
…[3 more quoted lines elided]…
>> But then my tools allow this because they find things for me.
 
> And this is supposed to be an advantage to your style?  

Yes it is.  It allows me to freely break down paragraphs into smaller units 
without any reluctance to do so because of 'red tape' overhead of having to 
add a new layer of numbering and/or shifting code around. And, because I 
only ever perform paragraphs, I have no need to check (in my programs) 
whether a new paragraph is in the scope of something else.

Because I can break down paragraphs so readily I don't wind up with deeply 
nested IFs, or overly complex conditions designed to catch everything at 
once, or 'exit's.

Now it may not be an advantage to you, you may even think of it as a 
disadvantage.  As I said _you_ would probably think of it as un-ordered.

That is the nature of styles.  One migrates to a style (or is forced into 
one) and deals with its advantages and disadvantages until they become 
automatic.  At this point the style is 'natural' and others become clumsy 
and unworkable.

One problem with styles is that they are a complete seies of related 
mechanisms.  There is a tendancy for particualr style features to group 
themselves into idioms.  

On the one hand there are what I call 'heavyweight' idioms: perform section 
or perform thru allowing for goto-exit. Deep nesting is avoided by testing 
for unwanted conditions and gotro exit. Often associated with numering 
systems.  Because of the overhead required for a new layer, and the ease of 
skipping over code and thus lack of deep nesting, there is a tendancy 
towards larger procedures.

On the other hand there are 'lightweight' idioms, such as I desribed.

And there are idioms which fit inbetween.

The essential issue is that for one system only one idiom should be used.

Mixing idioms and trying to pick single style elements and put them in an 
inappropriate idiom tends to not be successful.

> How about TPB who has
> to try to fix your code when you aren't available?  Is opacity a virtue?
 
It isn't 'opacity', it is just 'different'.  Finding the code that is being 
performed isn't done by hitting 'PgDn' 37 times, or flipping forwards on 
lineflo, it is done using widely available tools that I have used for 25 
years, such as 'search' in an editor.  In my case I put the cursor on the 
word required and hit a key. If your editor can't do this then get better 
tools.

The essential thing that TPB should know is that the program (and system 
where possible) is _consistent_.  If TPB looks at a paragraph of code in my 
programs they are guaranteed that it is only ever performed. The label is 
not dropped into from above, it will not drop out to the next paragraph.  
It can be taken and put anywhere else between paragraphs, it can be broken 
in two in situ and have the first part perform the second.

Your style I would assume is also entirely consistent, certain things can 
be guaranteed, certain things may be done, other things may be prohibited.

It happens that in the two styles the permissions and prohibitions are 
different, the things that need to be checked are different.

As long as these rules are understood and followed then there is no problem 
to TPB.

However, if he wants to put a GOTO in my program then he is SOOL.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 5)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-08-01T05:07:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AAmWa.6733$K4.291857@twister.tampabay.rr.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <bg9og2$ber$1@aklobs.kc.net.nz> <3F298813.A304C12D@mb.sympatico.ca> <bgc4ud$dic$1@aklobs.kc.net.nz>`

```
"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:bgc4ud$dic$1@aklobs.kc.net.nz...
> Peter Lacey wrote:
>
> If the design is well done it doesn't need crutches, such as keeping
> numbered paragraphs in sequence.   ;-)
A good design it the most underrated style.

> > <snip> <ooops>
> > If you look at my programs you would probably be completely lost.  You
> >> would be checking for things that don't exist, you wouldn't know where
to
> >> look for anything. You would think of them as un-ordered, almost
random.
> >> But then my tools allow this because they find things for me.
Perhaps you would sell your theories better if you didn't use words such as
"unordered" and "almost random" as this instills the idea that there is no
good design.  Most designs are ordered and far from random.  Usually there
should be some pattern to the code you write...  I have minor issues with
people that have an OPEN-FILES or CONNECT paragraphs but then don't have a
CLOSE-FILES DISCONNECT paragraph...maybe because I started learning to code
in C++...there's a lot to be said for symmetry.

If you can go to a paragraph and KNOW that you can identify where it was
called from and work backwards and forwards and KNOW that there isn't a jump
in the middle and doesn't fall through then TPB won't have any problems at
all and that to me is good enough.

> > And this is supposed to be an advantage to your style?
> Yes it is.  It allows me to freely break down paragraphs into smaller
units
> without any reluctance to do so because of 'red tape' overhead of having
to
> add a new layer of numbering and/or shifting code around. And, because I
> only ever perform paragraphs, I have no need to check (in my programs)
> whether a new paragraph is in the scope of something else.
Have you ever used a formatted print that has lines for paragraph
calls...probably looks like spaghetti junction in your code.  Whilst I don't
disagree with you I think that a case can be made for the occasional move
around.  If the code is as modular and clean and neat as you say this should
be absolutely no risk at all as you can guarantee that you won't lose
anything or interfere with anything else as long as you stay out of the
middle of another paragraph.  There is nothing wrong with printed
readability.

> Because I can break down paragraphs so readily I don't wind up with deeply
> nested IFs, or overly complex conditions designed to catch everything at
> once, or 'exit's.
So instead you have deeply nested paragraphs? ;-)

> The essential thing that TPB should know is that the program (and system
> where possible) is _consistent_.  If TPB looks at a paragraph of code in
my
> programs they are guaranteed that it is only ever performed. The label is
> not dropped into from above, it will not drop out to the next paragraph.
> It can be taken and put anywhere else between paragraphs, it can be broken
> in two in situ and have the first part perform the second.
This is so much better an argument than anything else you have
written....why not say this leave it at that? Why tell people their tools
suck (any tool can handle the above - and I'm talking at about the person
pronoun :-) )  Why use words like looks unorganized and random....

JCE
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-01T20:47:40+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgd9eu$tb7$1@aklobs.kc.net.nz>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3F298813.A304C12D@mb.sympatico.ca> <bgc4ud$dic$1@aklobs.kc.net.nz> <AAmWa.6733$K4.291857@twister.tampabay.rr.com>`

```
jce wrote:

> Perhaps you would sell your theories better if you didn't use words such
> as "unordered" and "almost random" as this instills the idea that there is
> no good design.  

Maybe that is what you thought about the words that I used, but to someone 
that is used to seeing code ordered in a specific way, they may find that 
it is not as they might like.  It is the way that I like.

This is not saying that there is no good design, but saying that there is 
no _best_ design.  Just because it is different doesn't make it better or 
worse, it just has different characteristics, different advantages and 
different disadvantages.  

> Most designs are ordered and far from random.  

Design of the logic (ie program design) is unrelated to physical placemnt 
which is a trivial implementation detail (IMHO).  I place code where it 
convenient for me to work on it, usually adjacent to where it is being used 
from one point or another.  If there is no good reason to move it then it 
stays where it is.  Given that placement makes no difference at all to the 
action of the program (not since I last overlayed programs that is), and 
makes no difference to being able to find it, then there is often no good 
reason.

Now I do understand why some do prefer to keep the physical ordering in 
some particular way, and how they feel this is part of the design.

> Usually there
> should be some pattern to the code you write...  I have minor issues with
> people that have an OPEN-FILES or CONNECT paragraphs but then don't have a
> CLOSE-FILES DISCONNECT paragraph...maybe because I started learning to
> code in C++...there's a lot to be said for symmetry.

Yeah, I have Open-Files and Connect-DB and Close-Files and Disconnect-DB, 
but they may all be down the bottom of the code somewhere.  Some may expect 
the Open-Files to be at the top of the code and the Close-files at the 
bottom.  I don't care where they are much, but the ordering of the PERFORMs 
of these is much more important.

> If you can go to a paragraph and KNOW that you can identify where it was
> called from and work backwards and forwards and KNOW that there isn't a
> jump in the middle and doesn't fall through then TPB won't have any
> problems at all and that to me is good enough.

Exactly.
 
> Have you ever used a formatted print that has lines for paragraph
> calls...probably looks like spaghetti junction in your code.  

I may have done so in the early 70s.  I may have used numbered paragraphs 
then and started by keeping them in order.  I do, however, recall shuffling 
code around to make it fit into overlays.  Some compilers had to have all 
the code for each overlay to be contiguous in the source.  This meant that 
anything performed from more than one overlay had to be in permanent and 
thus at the front of the source code.  A lot of stuff that was done just 
once (such as open-files and close-files) was dumped into another overlay 
and thus was together at the end.

The logical flow was one design for the program, the overlay structure was 
a completely different design that controlled the source code layout.

Perhaps that is when I realised that logic flow doesn't have to be 'down 
the pages'.  It was when I got PC (actually micro-computer) tools in the 
late 70s that I didn't even need 'pages'.

Printed listings ?  Not in the last quarter century, no.

>> Because I can break down paragraphs so readily I don't wind up with
>> deeply nested IFs, or overly complex conditions designed to catch
>> everything at once, or 'exit's.

> So instead you have deeply nested paragraphs? ;-)

There is no free lunch.

> Why use words like looks unorganized and random....

Because I recognise that to someone who likes and expects a strict and 
rigourous hierarchy reflected in the layout that is how they may criticise 
my code (or may say that is has no design).
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 6)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-01T12:42:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZetWa.83099$0v4.5551246@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <bg9og2$ber$1@aklobs.kc.net.nz> <3F298813.A304C12D@mb.sympatico.ca> <bgc4ud$dic$1@aklobs.kc.net.nz> <AAmWa.6733$K4.291857@twister.tampabay.rr.com>`

```

"jce" <defaultuser@hotmail.com> wrote in message
news:AAmWa.6733$K4.291857@twister.tampabay.rr.com...
| "Richard Plinston" <riplin@Azonic.co.nz> wrote in message
| news:bgc4ud$dic$1@aklobs.kc.net.nz...
|
| > Because I can break down paragraphs so readily I don't wind up with
deeply
| > nested IFs, or overly complex conditions designed to catch everything at
| > once, or 'exit's.

| So instead you have deeply nested paragraphs? ;-)

When you break things down, you usually wind up with simple constructions
that can be easily validated by visual review.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-31T23:59:54-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgcojq$duv$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <bg9og2$ber$1@aklobs.kc.net.nz> <3F298813.A304C12D@mb.sympatico.ca>`

```
In article <3F298813.A304C12D@mb.sympatico.ca>,
Peter Lacey  <lacey@mb.sympatico.ca> wrote:

[snip]

>(TPB is The Poor Bastard who has to do maintenance or emergency fixes.  ALL
>coding should be done with TPB in mind.  S/He hasn't got time to figure out
>your style & tools).

Mr Lacey, this seems a variant of my 'two-year programmer standard'... 
don't you know that has been discarded?

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-01T20:52:16+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgd9nh$tb7$2@aklobs.kc.net.nz>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bg9og2$ber$1@aklobs.kc.net.nz> <3F298813.A304C12D@mb.sympatico.ca> <bgcojq$duv$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

> Mr Lacey, this seems a variant of my 'two-year programmer standard'...
> don't you know that has been discarded?

By whom ?  on whose aithority ?
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-01T08:29:57-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgdmg5$lap$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3F298813.A304C12D@mb.sympatico.ca> <bgcojq$duv$1@panix1.panix.com> <bgd9nh$tb7$2@aklobs.kc.net.nz>`

```
In article <bgd9nh$tb7$2@aklobs.kc.net.nz>,
Richard Plinston  <riplin@Azonic.co.nz> wrote:
>docdwarf@panix.com wrote:
>
…[3 more quoted lines elided]…
>By whom ?  on whose aithority ?

Why, by Mr Wagner, of course... he recently referred to is as a 'for the 
kids' argument which his experience seems to prove invalid.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 5)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-01T12:50:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<omtWa.83105$0v4.5553284@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <bg9og2$ber$1@aklobs.kc.net.nz> <3F298813.A304C12D@mb.sympatico.ca> <bgcojq$duv$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:bgcojq$duv$1@panix1.panix.com...
| In article <3F298813.A304C12D@mb.sympatico.ca>,
| Peter Lacey  <lacey@mb.sympatico.ca> wrote:
…[3 more quoted lines elided]…
| >(TPB is The Poor Bastard who has to do maintenance or emergency fixes.
ALL
| >coding should be done with TPB in mind.  S/He hasn't got time to figure
out
| >your style & tools).
|
| Mr Lacey, this seems a variant of my 'two-year programmer standard'...
| don't you know that has been discarded?

Doc,
If you write FOR the "'two-year programmer", you become the "'two-year
programmer".

Don't underestimate the "'two-year programmer".
On one project I was on, I would have taken the one "'two-year programmer"
over the "five-year, and 25 year programmers" on the project.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-01T10:17:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgdspr$s1c$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3F298813.A304C12D@mb.sympatico.ca> <bgcojq$duv$1@panix1.panix.com> <omtWa.83105$0v4.5553284@bgtnsc04-news.ops.worldnet.att.net>`

```
In article <omtWa.83105$0v4.5553284@bgtnsc04-news.ops.worldnet.att.net>,
Harley <dennis.harleyNoSpam@worldnet.att.net> wrote:
>
><docdwarf@panix.com> wrote in message news:bgcojq$duv$1@panix1.panix.com...
…[14 more quoted lines elided]…
>programmer".

And if one deals with mosters long enough one can become one... and if one 
stares long enough into The Abyss The Abyss stares back.

>
>Don't underestimate the "'two-year programmer".
>On one project I was on, I would have taken the one "'two-year programmer"
>over the "five-year, and 25 year programmers" on the project.

One programmer doth not a summer make, last I looked... to write code for 
this one coder you met on one project might have results less than 
desireable.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-02T09:33:40+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgemba$h49$1@aklobs.kc.net.nz>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3F298813.A304C12D@mb.sympatico.ca> <bgcojq$duv$1@panix1.panix.com> <omtWa.83105$0v4.5553284@bgtnsc04-news.ops.worldnet.att.net>`

```
Harley wrote:

> If you write FOR the "'two-year programmer", you become the "'two-year
> programmer".

Put another way: If you make something that even a fool can use then only a 
fool will want to.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-01T20:03:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgev50$l1k$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgcojq$duv$1@panix1.panix.com> <omtWa.83105$0v4.5553284@bgtnsc04-news.ops.worldnet.att.net> <bgemba$h49$1@aklobs.kc.net.nz>`

```
In article <bgemba$h49$1@aklobs.kc.net.nz>,
Richard Plinston  <riplin@Azonic.co.nz> wrote:
>Harley wrote:
>
…[4 more quoted lines elided]…
>fool will want to.

Well... so much for lace-up shoes, bicycles and toothbrushes, I guess.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-08-04T16:28:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgm1ji$p91$1@peabody.colorado.edu>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3F298813.A304C12D@mb.sympatico.ca> <bgcojq$duv$1@panix1.panix.com> <omtWa.83105$0v4.5553284@bgtnsc04-news.ops.worldnet.att.net> <bgemba$h49$1@aklobs.kc.net.nz>`

```

On  1-Aug-2003, Richard Plinston <riplin@Azonic.co.nz> wrote:

> > If you write FOR the "'two-year programmer", you become the "'two-year
> > programmer".
>
> Put another way: If you make something that even a fool can use then only a
> fool will want to.

Counter examples: Shoes, bicycle, pancake, ATM machine.

Examples:   ????
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 8)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-04T16:38:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h_vXa.84267$3o3.5827505@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3F298813.A304C12D@mb.sympatico.ca> <bgcojq$duv$1@panix1.panix.com> <omtWa.83105$0v4.5553284@bgtnsc04-news.ops.worldnet.att.net> <bgemba$h49$1@aklobs.kc.net.nz> <bgm1ji$p91$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:bgm1ji$p91$1@peabody.colorado.edu...
|
| On  1-Aug-2003, Richard Plinston <riplin@Azonic.co.nz> wrote:
…[4 more quoted lines elided]…
| > Put another way: If you make something that even a fool can use then
only a
| > fool will want to.
|
| Counter examples: Shoes,

With or without laces?

|bicycle, pancake, ATM machine.

Pancake?

| Examples:   ????
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 8)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-08-04T16:41:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41wXa.13190$qg3.791916@twister.tampabay.rr.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <3F298813.A304C12D@mb.sympatico.ca> <bgcojq$duv$1@panix1.panix.com> <omtWa.83105$0v4.5553284@bgtnsc04-news.ops.worldnet.att.net> <bgemba$h49$1@aklobs.kc.net.nz> <bgm1ji$p91$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:bgm1ji$p91$1@peabody.colorado.edu...
>
> On  1-Aug-2003, Richard Plinston <riplin@Azonic.co.nz> wrote:
…[4 more quoted lines elided]…
> > Put another way: If you make something that even a fool can use then
only a
> > fool will want to.
>
> Counter examples: Shoes, bicycle, pancake, ATM machine.
>
> Examples:   ????

Ab-rocker, Thigh Master, the Internet Treasure Chest.......The Spirooli

Late night tv exists solely to sell these things to fools.....

JCE
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-05T07:40:39+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgmcs9$29l$1@aklobs.kc.net.nz>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <omtWa.83105$0v4.5553284@bgtnsc04-news.ops.worldnet.att.net> <bgemba$h49$1@aklobs.kc.net.nz> <bgm1ji$p91$1@peabody.colorado.edu>`

```
Howard Brazee wrote:

>> Put another way: If you make something that even a fool can use then only
>> a fool will want to.
> 
> Counter examples: Shoes, bicycle, pancake, ATM machine.

What makes you think that a fool can use those things effectively.

Or, indeed, that it isn't only fools that are using them ?

(Note, that the latter is not denied by your, or my, usage).

Take for example the ATM machines.  Prior to ATMs it was required (by law 
in this country) that funds only be released by the signature of the 
account holder.  Funds released by the bank to someone else on a false 
signature had to be reimbursed by the bank.  For ATMs the money could be 
taken from the account merely by use of a simple keyed number (and the 
card) no matter who used it, and the bank didn't have to make good such 
monies as were stolen.

Only a fool would agree to that.

As for bicycles, I rest my case.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

- **From:** docdwarf@panix.com
- **Date:** 2003-08-01T08:27:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgdmb0$kq2$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <bg9og2$ber$1@aklobs.kc.net.nz>`

```
In article <bg9og2$ber$1@aklobs.kc.net.nz>,
Richard Plinston  <riplin@Azonic.co.nz> wrote:

[snip]

>If you look at my programs you would probably be completely lost.  You 
>would be checking for things that don't exist, you wouldn't know where to 
>look for anything. You would think of them as un-ordered, almost random. 
>But then my tools allow this because they find things for me.

Mr Plinston, this sounds remarkably close to writing code so that you need 
your own special pair of '3D Spectacles' to understand it... but it 
couldn't be *that* simple, right?

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-02T09:39:05+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgemlf$h49$2@aklobs.kc.net.nz>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <bg9og2$ber$1@aklobs.kc.net.nz> <bgdmb0$kq2$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

> Richard Plinston  <riplin@Azonic.co.nz> wrote:
> 
…[8 more quoted lines elided]…
> your own special pair of '3D Spectacles' to understand it... 

I don't think there is anything in my paragraph that refers to 
'understanding', but it does refer to navigation.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-01T20:10:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgevhb$nei$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bg9og2$ber$1@aklobs.kc.net.nz> <bgdmb0$kq2$1@panix1.panix.com> <bgemlf$h49$2@aklobs.kc.net.nz>`

```
In article <bgemlf$h49$2@aklobs.kc.net.nz>,
Richard Plinston  <riplin@Azonic.co.nz> wrote:
>docdwarf@panix.com wrote:
>
…[13 more quoted lines elided]…
>'understanding', but it does refer to navigation.

Mr Plinston, you say 'if you look at my programs you would probably be 
completely lost... You would think of them as un-ordered, almost random.'  
Since a definition of 'understand' is 'to grasp the nature, significance 
or explanation of something' then unless the nature, significance or 
explanation of your code is 'un-ordered, almost random' then, at least by 
the definition cited, understanding is not done.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-02T12:53:13+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgf21i$m9a$1@aklobs.kc.net.nz>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bg9og2$ber$1@aklobs.kc.net.nz> <bgdmb0$kq2$1@panix1.panix.com> <bgemlf$h49$2@aklobs.kc.net.nz> <bgevhb$nei$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:


> Mr Plinston, you say 'if you look at my programs you would probably be
> completely lost... You would think of them as un-ordered, almost random.'
> Since a definition of 'understand' is 'to grasp the nature, significance
> or explanation of something' 

I don't see any reference to placement, sequencing, wereabouts or finding 
ones way in that.

> then unless the nature, significance or
> explanation of your code is 'un-ordered, almost random' then, at least by
> the definition cited, understanding is not done.

Indeed, if that is what your understanding of the definition and of my 
comments is, then your understanding my comments may leave you lost and 
bewildered.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-01T21:33:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgf4cr$kir$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bgemlf$h49$2@aklobs.kc.net.nz> <bgevhb$nei$1@panix1.panix.com> <bgf21i$m9a$1@aklobs.kc.net.nz>`

```
In article <bgf21i$m9a$1@aklobs.kc.net.nz>,
Richard Plinston  <riplin@Azonic.co.nz> wrote:
>docdwarf@panix.com wrote:
>
…[7 more quoted lines elided]…
>ones way in that.

Quite right, Mr Plinston... your statement that 'you would probably be
lost' is not a reference to 'placement, sequencing, wereabouts (sic) or
finding ones (sic) way'

... and I am the King of England.  Likewise, references to 'un-ordered, 
random' is not a reference to 'sequencing' in similar wise.

>
>> then unless the nature, significance or
…[5 more quoted lines elided]…
>bewildered.

... but not in terms of placement, sequencing, whereabouts or finding 
one's way, of course.

DD
```

##### ↳ ↳ Re: Numbered prefixes

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-31T13:48:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgb6nn$3o2$1@peabody.colorado.edu>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net>`

```

On 30-Jul-2003, "Hugh Candlin" <no@spam.com> wrote:

> You missed the most important one.  Prevention of looping.
> Do not ever call a lower-numbered paragraph.  It is that simple.

If you don't have PERFORM THRU nor procedure division sections, nor GO TO, then
you don't have such looping.

I do have copy members with paragraph names.  Those paragraphs don't know where
they will be copied in my program.
```

##### ↳ ↳ Re: Numbered prefixes

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-07-31T22:45:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B_gWa.938$kP6.582@newsread2.news.atl.earthlink.net>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net>`

```
"Hugh Candlin" <no@spam.com> wrote in message
news:apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net...
<snip>
>
> Another bonus is that the paragraph number confers uniqueness,
…[4 more quoted lines elided]…
>

Hugh,
  Unless I misunderstanding what you are suggesting (or unless you use a LOT
of "COPY" - and nested COPY - statements), this REALLY bothers me.

If I perform the same "logic" in multiple places in the "flow" of my
program, I (personally) really, REALLY, want the code to be coded JUST ONCE
in my program - and performed from each of the places where the logic
requires it.  Otherwise, I see too much likelihood of maintenance occurring
to one place - but not all places where this logic is required.  If, during
maintenance, it turns out that I really WANT there to be different code
sequences in the two places, THEN I "split" it into similar - but not
identical - paragraphs.

IMHO, if you have the exact same code sequences in multiple places in your
source code (and the sequence performs a "logical" action), then IN GENERAL,
I think this belongs a "single paragraph".
```

###### ↳ ↳ ↳ Re: Numbered prefixes

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-07-31T23:01:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PchWa.79032$3o3.5421508@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <B_gWa.938$kP6.582@newsread2.news.atl.earthlink.net>`

```

William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:B_gWa.938$kP6.582@newsread2.news.atl.earthlink.net...
> "Hugh Candlin" <no@spam.com> wrote in message
> news:apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net...
…[9 more quoted lines elided]…
>   Unless I misunderstanding what you are suggesting (or unless you use a
LOT
> of "COPY" - and nested COPY - statements), this REALLY bothers me.
>
> If I perform the same "logic" in multiple places in the "flow" of my
> program, I (personally) really, REALLY, want the code to be coded JUST
ONCE
> in my program - and performed from each of the places where the logic
> requires it.

Agreed.

> Otherwise, I see too much likelihood of maintenance occurring
> to one place - but not all places where this logic is required.

Agreed.

> If, during
> maintenance, it turns out that I really WANT there to be different code
> sequences in the two places, THEN I "split" it into similar - but not
> identical - paragraphs.

Agreed, which was my contention right from the start.

But you would have to come up with a different paragraph name,
while I would simply have to increment the paragraph number of the new
paragraph, easily done as my numbering technique anticipates this
possibility.
The numbered prefix differentiates, while the identical alpha remainder
of the paragraph name indicates a logistical relationship.  For instance

3120-VALIDATE-HDIV
3320-VALIDATE-KDIV
3520-VALIDATE-PDIV
3720-VALIDATE-TDIV

....with each paragraph having slightly different business rules encoded.

> IMHO, if you have the exact same code sequences in multiple places in
your
> source code (and the sequence performs a "logical" action), then IN
GENERAL,
> I think this belongs a "single paragraph".
>
Agreed, right down to the necessary "IN GENERAL" qualifier.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-01T11:49:13+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgc9t8$fmh$1@aklobs.kc.net.nz>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <B_gWa.938$kP6.582@newsread2.news.atl.earthlink.net> <PchWa.79032$3o3.5421508@bgtnsc05-news.ops.worldnet.att.net>`

```
Hugh Candlin wrote:

> But you would have to come up with a different paragraph name,
> while I would simply have to increment the paragraph number of the new
…[8 more quoted lines elided]…
> 3720-VALIDATE-TDIV

What part of:

  Validate-HDiv.
  Validate-KDiv.
  Validate-PDiv.
  Validate-TDiv.

are not 'different paragraph names' already ?

Which of these are _not_ 'differentiated' without a numbered prefix ?

Or is it just that the differentiation is required for the 3120-Exit, 
3320-Exit, etc ?  which would never exist in my programs.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-08-01T14:24:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgdt6j$h7k$1@peabody.colorado.edu>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <B_gWa.938$kP6.582@newsread2.news.atl.earthlink.net>`

```
One trouble I have found that exists in an environment with numbered paragraphs
is the following ugly code.


1000-initialize
...
     if done
     go to 1000-exit
...
1000-exit.

2000-read.
...
    if done
    go to 1000-exit
...
2000-exit.

This problem occurred with a cut and paste.
First, I hate PERFORM THRU and will be glad when there is no longer an excuse
for using it.
Second, 1000-exit is a poor paragraph name.
Third - this program was worse than you think.   There were GO TO 2000-READ
commands in that paragraph.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2003-08-01T13:29:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bge820$5hl$1@panix1.panix.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <B_gWa.938$kP6.582@newsread2.news.atl.earthlink.net> <bgdt6j$h7k$1@peabody.colorado.edu>`

```
In article <bgdt6j$h7k$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>One trouble I have found that exists in an environment with numbered paragraphs
>is the following ugly code.
…[16 more quoted lines elided]…
>This problem occurred with a cut and paste.

... and with the walk-through... and with the production review before it 
was implemented.

DD
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-08-01T18:08:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgeaaq$mhr$1@peabody.colorado.edu>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <B_gWa.938$kP6.582@newsread2.news.atl.earthlink.net> <bgdt6j$h7k$1@peabody.colorado.edu> <bge820$5hl$1@panix1.panix.com>`

```

On  1-Aug-2003, docdwarf@panix.com wrote:

> >This problem occurred with a cut and paste.
>
> ... and with the walk-through... and with the production review before it
> was implemented.

And with the IMHO, standards.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-02T09:16:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgelct$gsg$1@aklobs.kc.net.nz>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <apYVa.81111$0v4.5386402@bgtnsc04-news.ops.worldnet.att.net> <B_gWa.938$kP6.582@newsread2.news.atl.earthlink.net> <bgdt6j$h7k$1@peabody.colorado.edu>`

```
Howard Brazee wrote:


> 1000-exit.
> 
…[3 more quoted lines elided]…
>     go to 1000-exit

> This problem occurred with a cut and paste.

It could be worse.  Usually this becomes obvious during testing. In some 
cases, however, it may not be detected for years, either because it is an 
obscure error and is never activated (until 3am), or because it does occur 
but most often it just drops down and finds its way past because some 
change in the data takes it via a different route.  This leads to counts 
being out by one or a record or two being skipped.

An automatic code checker is the only way to go - the compiler can't find 
it for you.
```

#### ↳ Re: Numbered prefixes

- **From:** "Jim Morcombe" <jim@byronics.com.au>
- **Date:** 2003-07-31T13:12:13+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bga80m$i5f$1@yeppa.connect.com.au>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net>`

```
Bill,

You really must be bored and looking for a good debate...

Cobol is based upon the idea of readability.  It is an English-like
language.

Putting "0100-" in front of a Procedure reduces its readability, adds
"noise" and takes it further away from English.

There are zillions of other ways to find where you wrote your procedure in
the code, most supported by the most primative editor.

Jim



William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net...
> Over the last year (or more), I have seen a number of people talking for
and
> against "numbered prefixes" (particularly the
>
…[5 more quoted lines elided]…
> card-decks, line-by-line editors, etc) but IN GENERAL, I have viewed this
as
> "yet another" style-only issue, i.e. YMMV.
>
> HOWEVER, while working on a totally unrelated "problem", I did discover
ONE
> "good" (not overwhelming - but still good) reason to use numeric prefixes
> for user-defined words.
…[4 more quoted lines elided]…
> "In order to reduce conflict between reserved words and user-defined
words,
> the following rules apply to the formation of reserved words in this
> International Standard.
…[4 more quoted lines elided]…
> 1) Reserved words shall not begin with the digits 0 through 9 or the
letters
> 'X', 'Y', or 'Z', except for the words ZERO, ZEROES, and ZEROS. ."
>
> In other words, if you have a procedure-name of  "0123-Para" you are (more
> or less) guaranteed that there will never be a conflict with any
"Standard"
> (and possibly vendor-specific) reserved word IN THE FUTURE.  On the other
> hand, if you call you procedure "Something-Procedure" it *might* end up
> causing you maintenance issues in with a future (or other vendor)
compiler.
>
> Some of the "words" that I think *HAVE* been used in historical COBOL
source
> code as user-defined names, but are now RESERVED words in the 2002
Standard
> are:
>
…[53 more quoted lines elided]…
> but it wouldn't BE a problem for sites/programmers who use numeric
prefixes.
>
> --
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Numbered prefixes

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-08-01T00:34:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c357c4$afdfeb80$9c93f243@chottel>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bga80m$i5f$1@yeppa.connect.com.au>`

```
OK here is the "secret". If you think numbering paragraphes sucks, then you
are right. If you think numbering paragraphs is great, then you are right.
It is that simple.

Jim Morcombe <jim@byronics.com.au> wrote in article
<bga80m$i5f$1@yeppa.connect.com.au>...
> Bill,
> 
…[8 more quoted lines elided]…
> There are zillions of other ways to find where you wrote your procedure
in
> the code, most supported by the most primative editor.
> 
…[6 more quoted lines elided]…
> > Over the last year (or more), I have seen a number of people talking
for
> and
> > against "numbered prefixes" (particularly the
…[6 more quoted lines elided]…
> > card-decks, line-by-line editors, etc) but IN GENERAL, I have viewed
this
> as
> > "yet another" style-only issue, i.e. YMMV.
…[3 more quoted lines elided]…
> > "good" (not overwhelming - but still good) reason to use numeric
prefixes
> > for user-defined words.
> >
> > The following text is from the 2002 ISO Standard - but the wording in
the
> > '85 Standard is SIMILAR,
> >
…[6 more quoted lines elided]…
> > recommended that implementors follow these rules in defining
extensions.
> >
> > 1) Reserved words shall not begin with the digits 0 through 9 or the
…[3 more quoted lines elided]…
> > In other words, if you have a procedure-name of  "0123-Para" you are
(more
> > or less) guaranteed that there will never be a conflict with any
> "Standard"
> > (and possibly vendor-specific) reserved word IN THE FUTURE.  On the
other
> > hand, if you call you procedure "Something-Procedure" it *might* end up
> > causing you maintenance issues in with a future (or other vendor)
…[56 more quoted lines elided]…
> > How many programmers are certain that they have NEVER used any of these
as
> > procedure or data names?
> >
> > P.S. It is a "medium-easy" task to "change" such names in existing
> > programs - and the enhanced REPLACE statement can also solve this
problem,
> > but it wouldn't BE a problem for sites/programmers who use numeric
> prefixes.
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Numbered prefixes

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-01T12:53:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CptWa.83107$0v4.5553256@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bga80m$i5f$1@yeppa.connect.com.au> <01c357c4$afdfeb80$9c93f243@chottel>`

```

"Charles Hottel" <chottel@cpcug.org> wrote in message
news:01c357c4$afdfeb80$9c93f243@chottel...
| OK here is the "secret". If you think numbering paragraphes sucks, then
you
| are right. If you think numbering paragraphs is great, then you are right.
| It is that simple.

Shhhhhhhhhh.
It's supposed to be a secret.

What are you trying to do, end a pointless war?
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 4)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-08-02T01:41:19+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f2a6eb7_6@news.athenanews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bga80m$i5f$1@yeppa.connect.com.au> <01c357c4$afdfeb80$9c93f243@chottel> <CptWa.83107$0v4.5553256@bgtnsc04-news.ops.worldnet.att.net>`

```

"Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
news:CptWa.83107$0v4.5553256@bgtnsc04-news.ops.worldnet.att.net...
>
> "Charles Hottel" <chottel@cpcug.org> wrote in message
…[3 more quoted lines elided]…
> | are right. If you think numbering paragraphs is great, then you are
right.
> | It is that simple.
>
…[4 more quoted lines elided]…
>
What goes..."Arrrrghhhh! Meow!"?

(Schroedinger's cat....)

Pete.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 5)_

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2003-08-01T16:59:30+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JR6NEGFi5oK$Ew1U@ld50macca.demon.co.uk>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bga80m$i5f$1@yeppa.connect.com.au> <01c357c4$afdfeb80$9c93f243@chottel> <CptWa.83107$0v4.5553256@bgtnsc04-news.ops.worldnet.att.net> <3f2a6eb7_6@news.athenanews.com>`

```
In message <3f2a6eb7_6@news.athenanews.com>, Peter E.C. Dashwood 
<dashwood@enternet.co.nz> writes
>
>What goes..."Arrrrghhhh! Meow!"?
…[3 more quoted lines elided]…
>Pete.

But can you be sure of that?
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-08-02T04:31:36+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f2a96a0_7@news.athenanews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bga80m$i5f$1@yeppa.connect.com.au> <01c357c4$afdfeb80$9c93f243@chottel> <CptWa.83107$0v4.5553256@bgtnsc04-news.ops.worldnet.att.net> <3f2a6eb7_6@news.athenanews.com> <JR6NEGFi5oK$Ew1U@ld50macca.demon.co.uk>`

```

"Alistair Maclean" <alistair@ld50macca.demon.co.uk> wrote in message
news:JR6NEGFi5oK$Ew1U@ld50macca.demon.co.uk...
> In message <3f2a6eb7_6@news.athenanews.com>, Peter E.C. Dashwood
> <dashwood@enternet.co.nz> writes
…[7 more quoted lines elided]…
> But can you be sure of that?

Only because Heisenberg told me. But you know how unreliable he is... He was
probably lying.

Pete.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 7)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-08-02T00:27:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c3588c$df1ea8a0$f58bf243@chottel>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bga80m$i5f$1@yeppa.connect.com.au> <01c357c4$afdfeb80$9c93f243@chottel> <CptWa.83107$0v4.5553256@bgtnsc04-news.ops.worldnet.att.net> <3f2a6eb7_6@news.athenanews.com> <JR6NEGFi5oK$Ew1U@ld50macca.demon.co.uk> <3f2a96a0_7@news.athenanews.com>`

```
He was not unreliable, just uncertain.

Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote in article
<3f2a96a0_7@news.athenanews.com>...
> 
> "Alistair Maclean" <alistair@ld50macca.demon.co.uk> wrote in message
…[12 more quoted lines elided]…
> Only because Heisenberg told me. But you know how unreliable he is... He
was
> probably lying.
> 
…[3 more quoted lines elided]…
>
```

#### ↳ Re: Numbered prefixes

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-01T00:17:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bg9na7$ava$1@aklobs.kc.net.nz>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net>`

```
William M. Klein wrote:

> I understand the history of these (READY TRACE debugging, punched
> card-decks, line-by-line editors, etc) but IN GENERAL, I have viewed this
> as "yet another" style-only issue, i.e. YMMV.

Agreed, it is a style issue.
 
> How many programmers are certain that they have NEVER used any of these as
> procedure or data names?

I recall getting caught when going from '74 to '85 with some new-fangled 
reserved word. It wasn't a big deal. 
 
> P.S. It is a "medium-easy" task to "change" such names in existing
> programs - and the enhanced REPLACE statement can also solve this problem,
> but it wouldn't BE a problem for sites/programmers who use numeric
> prefixes.

I can understand why prefixes are used to order and structure the code and 
enforce a hierarchy.  However, this implies a nazi approach to hierarchical 
structuring which is (IMHO) the antithesis of, say, OO, which is a 
bottom-up approach.

I can also be derisive in noting that structured prefixes tend to indicate 
(to me) that a rather fixed and inflexible approach has been made to 
program design - this is another rewrite of the same program design that 
has around in a site for a few decades.

I may have biefly made an offhand reference to only performing paragraphs. 
One of the advantages of that style is the dumping of all the overheads 
associated with 'heavy-weight' perform thru or perform section where 
checking is required whenever a new procedure is created.  The prefixing is 
another overhead associated with that.  It implies that a perform must be 
of a lower level, that level must be positioned in the source file 
correctly and, in turn, any performs must be similarly increasing in level 
and position.

This gives recursive resistence to simplifying structures.  The work 
involved in taking a procedure that is 01234-xyz and breaking it down into 
smaller components becomes too onerus because these have to be distributed 
in the source and structured in a different way.

It becomes so much easier to just stick in a couple of GO TOs.
```

##### ↳ ↳ Re: Numbered prefixes

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-31T16:45:55+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f289fbc_1@news.athenanews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bg9na7$ava$1@aklobs.kc.net.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:bg9na7$ava$1@aklobs.kc.net.nz...
> William M. Klein wrote:
>
> > I understand the history of these (READY TRACE debugging, punched
> > card-decks, line-by-line editors, etc) but IN GENERAL, I have viewed
this
> > as "yet another" style-only issue, i.e. YMMV.
>
> Agreed, it is a style issue.
>
> > How many programmers are certain that they have NEVER used any of these
as
> > procedure or data names?
>
…[4 more quoted lines elided]…
> > programs - and the enhanced REPLACE statement can also solve this
problem,
> > but it wouldn't BE a problem for sites/programmers who use numeric
> > prefixes.
>
> I can understand why prefixes are used to order and structure the code and
> enforce a hierarchy.  However, this implies a nazi approach to
hierarchical
> structuring which is (IMHO) the antithesis of, say, OO, which is a
> bottom-up approach.
…[9 more quoted lines elided]…
> checking is required whenever a new procedure is created.  The prefixing
is
> another overhead associated with that.  It implies that a perform must be
> of a lower level, that level must be positioned in the source file
…[9 more quoted lines elided]…
>

Yeah, that works for me every time I have to maintain such rubbish...<G>
(Fortunately for all concerned, I don't get to maintain COBOL any
more...apart from my own, which so artistically elegant that maintaining it
is just a joy <G>)

You  (and Bill) put your finger on it when you said it is a matter of style.
Hugh took his finger off it when he said it isn't...

Pete.
```

###### ↳ ↳ ↳ Re: Numbered prefixes

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-08-01T00:31:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c357c4$43511660$9c93f243@chottel>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bg9na7$ava$1@aklobs.kc.net.nz> <3f289fbc_1@news.athenanews.com>`

```
Gee Pete I remember you disagreed with me when I said you only worked with
great people, now you admit I was right. Working with only yourself, it
doesn't get any better than that! :-) 

Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote in article
<3f289fbc_1@news.athenanews.com>...
> 
> "Richard Plinston" <riplin@Azonic.co.nz> wrote in message
…[10 more quoted lines elided]…
> > > How many programmers are certain that they have NEVER used any of
these
> as
> > > procedure or data names?
> >
> > I recall getting caught when going from '74 to '85 with some
new-fangled
> > reserved word. It wasn't a big deal.
> >
…[6 more quoted lines elided]…
> > I can understand why prefixes are used to order and structure the code
and
> > enforce a hierarchy.  However, this implies a nazi approach to
> hierarchical
…[3 more quoted lines elided]…
> > I can also be derisive in noting that structured prefixes tend to
indicate
> > (to me) that a rather fixed and inflexible approach has been made to
> > program design - this is another rewrite of the same program design
that
> > has around in a site for a few decades.
> >
> > I may have biefly made an offhand reference to only performing
paragraphs.
> > One of the advantages of that style is the dumping of all the overheads
> > associated with 'heavy-weight' perform thru or perform section where
> > checking is required whenever a new procedure is created.  The
prefixing
> is
> > another overhead associated with that.  It implies that a perform must
be
> > of a lower level, that level must be positioned in the source file
> > correctly and, in turn, any performs must be similarly increasing in
level
> > and position.
> >
> > This gives recursive resistence to simplifying structures.  The work
> > involved in taking a procedure that is 01234-xyz and breaking it down
into
> > smaller components becomes too onerus because these have to be
distributed
> > in the source and structured in a different way.
> >
…[5 more quoted lines elided]…
> more...apart from my own, which so artistically elegant that maintaining
it
> is just a joy <G>)
> 
> You  (and Bill) put your finger on it when you said it is a matter of
style.
> Hugh took his finger off it when he said it isn't...
> 
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Numbered prefixes

_(reply depth: 4)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-08-01T13:24:40+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f29c212_8@news.athenanews.com>`
- **References:** `<6vXVa.2709$lq.216@newsread2.news.atl.earthlink.net> <bg9na7$ava$1@aklobs.kc.net.nz> <3f289fbc_1@news.athenanews.com> <01c357c4$43511660$9c93f243@chottel>`

```

"Charles Hottel" <chottel@cpcug.org> wrote in message
news:01c357c4$43511660$9c93f243@chottel...
> Gee Pete I remember you disagreed with me when I said you only worked with
> great people, now you admit I was right. Working with only yourself, it
> doesn't get any better than that! :-)

Unfortunately, I can't afford to do it indefinitely...<G>

But I do enjoy the times when I can.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
