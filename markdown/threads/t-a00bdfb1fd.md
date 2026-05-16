[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Making a conditional, multiple random number generator

_4 messages · 2 participants · 2001-03_

---

### Making a conditional, multiple random number generator

- **From:** "J. Reis" <jreis26@hotmail.com>
- **Date:** 2001-03-06T08:59:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iZ6p6.2325$dV3.114811@news.uswest.net>`

```
Greetings all.

For part of a class that I am taking, I am developing a random number
generator.  I want this number generator to display eight unique,
non-repeating numbers at random in a range of 1 - 99 and a nineth number to
be drawn from 1-99 that could duplicate one of the first eight.  Basically I
am making a bigger lottery Powerball game.  This supposed to work on the
fujitsu compiler on a PC.  I have figured out how to use the random number
feature but I cant seem to get the right commands to make it funtion
multiple times in the manner described above.  If anyone can give a little
help or some advice, it would be greatly appreciated.  Thanks.

J.  Reis
```

#### ↳ Re: Making a conditional, multiple random number generator

- **From:** floydj@netins.net (Floyd Johnson)
- **Date:** 2001-03-06T15:05:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<982uci$vvs$1@ins21.netins.net>`
- **References:** `<iZ6p6.2325$dV3.114811@news.uswest.net>`

```
If you could give us some idea of what you have tried, we might be better
able to be of help.  This is sort of a policy when working with homework -
I expect it would be true even if this is not homework.

Floyd Johnson

J. Reis (jreis26@hotmail.com) wrote:
: Greetings all.

: For part of a class that I am taking, I am developing a random number
: generator.  I want this number generator to display eight unique,
: non-repeating numbers at random in a range of 1 - 99 and a nineth number to
: be drawn from 1-99 that could duplicate one of the first eight.  Basically I
: am making a bigger lottery Powerball game.  This supposed to work on the
: fujitsu compiler on a PC.  I have figured out how to use the random number
: feature but I cant seem to get the right commands to make it funtion
: multiple times in the manner described above.  If anyone can give a little
: help or some advice, it would be greatly appreciated.  Thanks.

: J.  Reis
```

##### ↳ ↳ Re: Making a conditional, multiple random number generator

- **From:** "J. Reis" <jreis26@hotmail.com>
- **Date:** 2001-03-06T09:53:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fK7p6.2788$dV3.145307@news.uswest.net>`
- **References:** `<iZ6p6.2325$dV3.114811@news.uswest.net> <982uci$vvs$1@ins21.netins.net>`

```
Not a problem.  Btw - its for a GrandView class.

Ok, I have the single random number code worked out.
Looks like this:
100 WORKING-STORAGE SECTION.
110 01  RANDOM-SEED      PIC 9(8)     VALUE ZEROS.
120 01  RANDOM-NUMBER    PIC 99       VALUE ZEROS.
130 01  RANDOM-GENERATE  PIC V9(18)   VALUE ZEROS.

160     MOVE FUNCTION CURRENT-DATE (9:8) TO RANDOM-SEED
170     COMPUTE RANDOM-GENERATE = FUNCTION RANDOM (RANDOM-SEED)
180     COMPUTE RANDOM-NUMBER = (RANDOM-GENERATE * 99) + 1
190     DISPLAY RANDOM-NUMBER

Where I run into difficulty is making it do multiple numbers.  Can you add
the same statement multiple times to complete the same function and then add
a statement to compare the numbers and make it recalculate and of the
duplicate numbers?  That would seem a bit clunky for coding.  It would seem
to me that maybe there is a line command to produce multiple numbers at
once.

J.  Reis
"Floyd Johnson" <floydj@netins.net> wrote in message
news:982uci$vvs$1@ins21.netins.net...
> If you could give us some idea of what you have tried, we might be better
> able to be of help.  This is sort of a policy when working with homework -
…[9 more quoted lines elided]…
> : non-repeating numbers at random in a range of 1 - 99 and a nineth number
to
> : be drawn from 1-99 that could duplicate one of the first eight.
Basically I
> : am making a bigger lottery Powerball game.  This supposed to work on the
> : fujitsu compiler on a PC.  I have figured out how to use the random
number
> : feature but I cant seem to get the right commands to make it funtion
> : multiple times in the manner described above.  If anyone can give a
little
> : help or some advice, it would be greatly appreciated.  Thanks.
>
…[16 more quoted lines elided]…
> +-----------------------------------------------------------+
```

###### ↳ ↳ ↳ Re: Making a conditional, multiple random number generator

- **From:** Floyd Johnson <floydj@netins.net>
- **Date:** 2001-03-06T11:46:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AA51483.E1F67415@netins.net>`
- **References:** `<iZ6p6.2325$dV3.114811@news.uswest.net> <982uci$vvs$1@ins21.netins.net> <fK7p6.2788$dV3.145307@news.uswest.net>`

```
Some hints that might help - 

It looks like you have the code right for a single value.  

How you handle the other three would depend on what features of COBOL
you have previously seen.  For example the four random values could be
stored in a table or as four separate variables.  Either technique would
be valid.

You will need to use a looping structure (i.e. IF-THEN-ELSE) to
determine whether you are repeating any values.  it might reduce the
complexity if you could initialize the random variables to illogical
values (e.g. negative numbers).  Finally, complexity could be reduced by
using a separate paragraph or subprogram (if you have seen these in your
COBOL course) to handle the duplication problem.  If a number is
duplicated, it will need to be re-COMPUTEed.  

Let us know if this helps or if more information is needed.

Floyd Johnson

"J. Reis" wrote:
> 
> Not a problem.  Btw - its for a GrandView class.
…[62 more quoted lines elided]…
> > +-----------------------------------------------------------+
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
