[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# function random

_3 messages · 3 participants · 1999-07_

---

### function random

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<378E9DF3.83378E33@zip.com.au>`

```
The function random is defined as having a value between 0 and
less than 1.

What format is the value returned in?

This is important so that I can understand the rounding issues. 
Yes I am basically MVS, but I am interested in other responses
especially standards oriented.  I beleive that if the format is
implementor defined the implementor MUST be required to define the
format they use.

Ken
```

#### ↳ Re: function random

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7mm8e4$2b7@dfw-ixnews7.ix.netcom.com>`
- **References:** `<378E9DF3.83378E33@zip.com.au>`

```
Ken Foskey <waratah@zip.com.au> wrote in message
news:378E9DF3.83378E33@zip.com.au...
> The function random is defined as having a value between 0 and
> less than 1.
…[9 more quoted lines elided]…
> Ken

The good news is that you are correct that the "format" is implementor
defined.

The BAD news is that the "current" Standard ('85 plus '89 plus '91) does
*not* require the implementor to tell you a THING about their "implementor
defined" items.  There is a change in the draft for the next Standard - but
I don't think that will help you much.

FYI - I know of several implementations that return many (not ALL) values
from numeric intrinsic functions as "floating-point" which leads to OBVIOUS
non-Standard and "rounding" and assorted other issues.
```

#### ↳ Re: function random

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<378EA8BC.C4EF4EA8@home.com>`
- **References:** `<378E9DF3.83378E33@zip.com.au>`

```
Ken Foskey wrote:
> 
> The function random is defined as having a value between 0 and
…[10 more quoted lines elided]…
> Ken

Can see this one generating a lot of debate. But for what it is worth
this is the on-line help for NetExpress :-

Quote :-
....................
The RANDOM function returns a numeric value that is a pseudo-random
number from a rectangular distribution. The type of this function is
numeric.

General Format

FUNCTION RANDOM [(argument-1)]

Arguments

1.	If argument-1 is specified, it must be zero or a positive integer. It
is used as the seed value to generate a sequence of pseudo-random
numbers.
2.	If a subsequent reference specifies argument-1, a new sequence of
pseudo-random numbers is started.
3.	If the first reference to this function in the run unit does not
specify argument-1, the seed value of zero is used. 
4.	In each case, subsequent references without specifying argument-1
return the next number in the current sequence.

Returned Values

1.	The returned value is greater than or equal to zero and less than
one.
2.	For a given seed value on a given implementation, the sequence of
pseudo-random numbers will always be the same.
3.	The domain of argument-1 values will yield distinct sequences of
pseudo-random numbers. This subset includes the values from 0 through at
least 32767.
4.	Floating-point format is used for numeric non-integer results.
...................
Unquote :-

Jimmy Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
