[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Test for numeric value

_14 messages · 8 participants · 1998-08_

**Topics:** [`Meta: FAQs, group policy, charter`](../topics.md#meta)

---

### Test for numeric value

- **From:** "vern_b..." <ua-author-13503960@usenetarchives.gap>
- **Date:** 1998-08-20T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35ddf1bf.10139904@netnews.worldnet.att.net>`

```
Hi,

I would like to test a data item to determine if it has a valid
numeric value. I am reading data in from an external source and can't
be sure they will not have non-numeric characters in there.

A friend suggested I REDEFINE the numericitem as an alphanumeric item
and use NUMERIC class test. I have been unable to get that to work
because my data can contain decimal points and negative values.

I also tried defining my own class in the SPECIAL-NAMES paragraph with
no luck (my code is listed below).

Any ideas?

Thanks!

Vern
```

#### ↳ Re: Test for numeric value

- **From:** "leif svalgaard" <ua-author-6445756@usenetarchives.gap>
- **Date:** 1998-08-20T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db12bc072a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<35ddf1bf.10139904@netnews.worldnet.att.net>`
- **References:** `<35ddf1bf.10139904@netnews.worldnet.att.net>`

```

Vern Bradner wrote in message
<35d··.@net··t.net>...
› I would like to test a data item to determine if it has a valid
› numeric value. I am reading data in from an external source and can't
…[34 more quoted lines elided]…
› 01 ALPHA-VALUE REDEFINES NUM-VALUE PIC X(12).



=====> the NYM-VALUE is 9 bytes, but ALPHA-VALUE is 12.
=====> this alone is giving you trouble



› 
› PROCEDURE DIVISION.
…[15 more quoted lines elided]…
› My opinions are not necessarily those of Newcourt.
```

##### ↳ ↳ Re: Test for numeric value

- **From:** "vern_b..." <ua-author-13503960@usenetarchives.gap>
- **Date:** 1998-08-20T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db12bc072a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-db12bc072a-p2@usenetarchives.gap>`
- **References:** `<35ddf1bf.10139904@netnews.worldnet.att.net> <gap-db12bc072a-p2@usenetarchives.gap>`

```
Hi Leif,

Seems I am having trouble counting :-). Thanks, I will go try the
correct count!

Vern

On Fri, 21 Aug 1998 17:46:14 -0500, "Leif Svalgaard"
wrote:

› 
› Vern Bradner wrote in message
…[64 more quoted lines elided]…
› 

Vern Bradner ver··.@new··t.com

My opinions are not necessarily those of Newcourt.
```

##### ↳ ↳ Re: Test for numeric value

- **From:** "vern_b..." <ua-author-13503960@usenetarchives.gap>
- **Date:** 1998-08-20T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db12bc072a-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-db12bc072a-p2@usenetarchives.gap>`
- **References:** `<35ddf1bf.10139904@netnews.worldnet.att.net> <gap-db12bc072a-p2@usenetarchives.gap>`

```
That solved my problem. Thanks Leif!

Vern



On Fri, 21 Aug 1998 17:46:14 -0500, "Leif Svalgaard"
wrote:

› 
› Vern Bradner wrote in message
…[64 more quoted lines elided]…
› 

Vern Bradner ver··.@new··t.com

My opinions are not necessarily those of Newcourt.
```

#### ↳ Re: Test for numeric value

- **From:** "kitty carr" <ua-author-4641293@usenetarchives.gap>
- **Date:** 1998-08-21T19:59:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db12bc072a-p5@usenetarchives.gap>`
- **In-Reply-To:** `<35ddf1bf.10139904@netnews.worldnet.att.net>`
- **References:** `<35ddf1bf.10139904@netnews.worldnet.att.net>`

```
Vern Bradner wrote:
› 
› Hi,
…[56 more quoted lines elided]…
› My opinions are not necessarily those of Newcourt.

You cannot move special characters to a numeric field. Your NUM-VALUE
should be PIC 9(6)V99. The ALPHA-VALUE redefines contains too many
characters. It should be PIC X(8). If you're moving money amounts to
NUM-VALUE, they should not contain decimal points, but implied decimal
points.

If I understand correctly what you're doing, a class test to determine
if a field is numeric, this should work:

01 NUM-VALUE PIC 9(6)V99 VALUE ZEROS.

**IF STATEMENT

IF NUM-VALUE NUMERIC
DISPLAY 'VALUE IS NUMERIC'
ELSE
DISPLAY 'VALUE IS ALPHANUMERIC'.

Kitty
```

##### ↳ ↳ Re: Test for numeric value

- **From:** "vern_b..." <ua-author-13503960@usenetarchives.gap>
- **Date:** 1998-08-20T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db12bc072a-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-db12bc072a-p5@usenetarchives.gap>`
- **References:** `<35ddf1bf.10139904@netnews.worldnet.att.net> <gap-db12bc072a-p5@usenetarchives.gap>`

```
Thanks Kitty!

Vern



On Fri, 21 Aug 1998 22:59:52 GMT, Kitty Carr
wrote:

› Vern Bradner wrote:
›› 
…[77 more quoted lines elided]…
› Kitty

Vern Bradner ver··.@new··t.com

My opinions are not necessarily those of Newcourt.
```

#### ↳ Re: Test for numeric value

- **From:** "dave_sl..." <ua-author-16041449@usenetarchives.gap>
- **Date:** 1998-08-22T01:15:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db12bc072a-p7@usenetarchives.gap>`
- **In-Reply-To:** `<35ddf1bf.10139904@netnews.worldnet.att.net>`
- **References:** `<35ddf1bf.10139904@netnews.worldnet.att.net>`

```
If your data is coming from an external source which cannot be trusted, even
if you fix the initial problem in your code you will still need a more
complex validation routine. I am assuming you are getting a text string for
the number, so what about "--123-" which will pass your test, or "12-345"?

If you are allowing free format data in the field ie " -123.45" or
"-123456.7" or " 123" then you will need to do quite a bit of validation
- allow leading spaces until '-', '.' or 0-9, then 0-9 until '.' or end, then
0-9 until end - and you will have to extract the result to a numeric field as
you are going and cater for the sign. It's even worse if you allow trailing
spaces eg " 123 ". If the format is set then it should be quite
straightforward - check for decimal/sign in the correct place and check the
other parts of the string are numeric, then extract the validated value to a
numeric field.

Ver··.@new··t.com (Vern Bradner) wrote:
› Hi,
› 
…[52 more quoted lines elided]…
› 	STOP RUN.

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

##### ↳ ↳ Re: Test for numeric value

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-08-22T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db12bc072a-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-db12bc072a-p7@usenetarchives.gap>`
- **References:** `<35ddf1bf.10139904@netnews.worldnet.att.net> <gap-db12bc072a-p7@usenetarchives.gap>`

```
dav··.@ya··o.com wrote:
› 
› (snip)
 
› If your data is coming from an external source which cannot be trusted, even
› if you fix the initial problem in your code you will still need a more
…[11 more quoted lines elided]…
› numeric field.

Sounds like multiple passes of the INSPECT verb to: replace leading
spaces with zeros, determine the last numeric position and location of
the decimal point (if present) so you can move the actual numeric part
to an aligned field...?

Bill Lynch
```

###### ↳ ↳ ↳ Re: Test for numeric value

- **From:** "vern_b..." <ua-author-13503960@usenetarchives.gap>
- **Date:** 1998-08-22T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db12bc072a-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-db12bc072a-p8@usenetarchives.gap>`
- **References:** `<35ddf1bf.10139904@netnews.worldnet.att.net> <gap-db12bc072a-p7@usenetarchives.gap> <gap-db12bc072a-p8@usenetarchives.gap>`

```
On 23 Aug 1998 05:00:44 GMT, Bill Lynch wrote:

› dav··.@ya··o.com wrote:
›› 
…[22 more quoted lines elided]…
› Bill Lynch

I will try that.

Thanks Bill!

Vern

Vern Bradner ver··.@new··t.com

My opinions are not necessarily those of Newcourt.
```

###### ↳ ↳ ↳ Re: Test for numeric value

_(reply depth: 4)_

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-08-22T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db12bc072a-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-db12bc072a-p9@usenetarchives.gap>`
- **References:** `<35ddf1bf.10139904@netnews.worldnet.att.net> <gap-db12bc072a-p7@usenetarchives.gap> <gap-db12bc072a-p8@usenetarchives.gap> <gap-db12bc072a-p9@usenetarchives.gap>`

```
I just thought that I should add to this thread some additional information
(and my usual plug for the next COBOL Standard). In the next Standard,
there will be new intrinsic functions to test of a field meets the
definition of either the NumVal or NumVal-C functions. I think that this
will solve *many* validation problems like that posed at the beginning of
this thread.

Given the uncertain date for the next Standard being approved and
implemented, I would suggest that any reader of this newsgroup who has
regular contact with their COBOL compiler vendor, contact them NOW about
creating an early implementation (as an extension) of the new TEST-
intrinsic functions.
```

###### ↳ ↳ ↳ Re: Test for numeric value

_(reply depth: 5)_

- **From:** "rick smith" <ua-author-44949@usenetarchives.gap>
- **Date:** 1998-08-25T17:57:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db12bc072a-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-db12bc072a-p10@usenetarchives.gap>`
- **References:** `<35ddf1bf.10139904@netnews.worldnet.att.net> <gap-db12bc072a-p7@usenetarchives.gap> <gap-db12bc072a-p8@usenetarchives.gap> <gap-db12bc072a-p9@usenetarchives.gap> <gap-db12bc072a-p10@usenetarchives.gap>`

```

William M. Klein wrote in message <6rpt1c$9.··.@dfw··m.com>...
› I just thought that I should add to this thread some additional information
› (and my usual plug for the next COBOL Standard).  In the next Standard,
…[10 more quoted lines elided]…
› 
For those who want it. I have written a TEST-NUMVAL subprogram.
Although I performed several test cases, I cannot be assured
that I have covered every possible misuse of the program.
The program is written as a state machine.

After calling the program, examine the value of the error
return parameter. If the value is zero, no errors were detected
and it should be safe to use FUNCTION NUMVAL with the same string.
If the value is not zero, the value is the position of the error.

Since the program was intended to be used with the intrinsic
function NUMVAL, intrinsic functions were used in the program
and are required.

WARNINGS:
I used some go tos to exit the loop early. The alternative
was to introduce another state which would simply read
the remaining characters. Think of it as "optimization."
I alter the value of the loop variable during
the loop. This was to prevent adding additional states
when processing trailing signs.

The subprogram for testing numeric values.
-------------
program-id. test-num is initial.
*> test for valid numeric value
*> when used prior to function numval
*> will return 0 if no errors
*> greater than 0 is position of error
data division.
working-storage section.
01 currentState pic s9(4) comp-5 value 1.
01 digitCount pic s9(4) comp-5 value 0.
01 signFound-Flag pic s9(4) comp-5 value 0.
88 signFound value 1.
01 s pic s9(4) comp-5. *> source character
linkage section.
01 theString pic x(36).
01 itsLength pic s9(4) comp-5.
01 errorPosition pic s9(4) comp-5.
procedure division using
by reference theString
by value itsLength
by reference errorPosition.
move 0 to errorPosition.
move 1 to currentState
if itsLength > function length (theString)
move function length (theString) to errorPosition
go to error-exit
end-if
perform varying s from 1 by 1
until s > itsLength
evaluate currentState
when 1 *> scan to leading start of number
evaluate theString (s:1)
when ' '
continue
when '+'
when '-'
set signFound to true
when '0' thru '9'
add 1 to digitCount
move 2 to currentState
when '.'
move 3 to currentState
when other
move s to errorPosition
go to error-exit
end-evaluate

when 2 *> scan number to decimal point
evaluate function upper-case (theString (s:1))
when '0' thru '9'
add 1 to digitCount
if digitCount > 18
move s to errorPosition
go to error-exit
end-if
when '.'
move 3 to currentState
when ' '
move 4 to currentState
when 'C'
when 'D'
when '+'
when '-'
if signFound
move s to errorPosition
go to error-exit
end-if
subtract 1 from s
move 4 to currentState
when other
move s to errorPosition
go to error-exit
end-evaluate

when 3 *> scan trailing digits
evaluate function upper-case (theString (s:1))
when '0' thru '9'
add 1 to digitCount
if digitCount > 18
move s to errorPosition
go to error-exit
end-if
when ' '
move 4 to currentState
when 'C'
when 'D'
when '+'
when '-'
if signFound
move s to errorPosition
go to error-exit
end-if
subtract 1 from s *> push back
move 4 to currentState
when other
move s to errorPosition
go to error-exit
end-evaluate

when 4 *> scan to end of string
evaluate function upper-case (theString (s:1))
when ' '
continue
when 'C'
if signFound
move s to errorPosition
go to error-exit
end-if
if s < itsLength
add 1 to s *> get next
if function upper-case (theString (s:1))
not = 'R'
move s to errorPosition
go to error-exit
end-if
end-if
set signFound to true
when 'D'
if signFound
move s to errorPosition
go to error-exit
end-if
if s < itsLength
add 1 to s *> get next
if function upper-case (theString (s:1))
not = 'B'
move s to errorPosition
go to error-exit
end-if
end-if
set signFound to true
when '+'
when '-'
if signFound
move s to errorPosition
go to error-exit
end-if
set signFound to true
when other
move s to errorPosition
go to error-exit
end-evaluate
end-evaluate
end-perform
if digitCount = 0
move itsLength to errorPosition
end-if
.
error-exit.
exit program
.
-------------
The test program.
-------------
program-id. n-test.
data division.
working-storage section.
01 aString pic x(25).
01 theError pic s9(4) comp-5.
procedure division.
display space
move "0" to aString
perform test-num-call
display aString space theError
move " 88 " to aString
perform test-num-call
display aString space theError
move " 88. " to aString
perform test-num-call
display aString space theError
move " .88 " to aString
perform test-num-call
display aString space theError
move "+88.44" to aString
perform test-num-call
display aString space theError
move "88.44-" to aString
perform test-num-call
display aString space theError
move "88.44cr" to aString
perform test-num-call
display aString space theError
move "88 .44+" to aString
perform test-num-call
display aString space theError
move "88. 44+" to aString
perform test-num-call
display aString space theError
move "88.4 4+" to aString
perform test-num-call
display aString space theError
move "+99.99.99" to aString
perform test-num-call
display aString space theError
move "+123456789.9876543210" to aString
perform test-num-call
display aString space theError
move spaces to aString
perform test-num-call
display aString space theError
move "one" to aString
perform test-num-call
display aString space theError
move "8.00+ cr" to aString
perform test-num-call
display aString space theError
move "8.00db -" to aString
perform test-num-call
display aString space theError
move "don't care" to aString
call "test-num" using *> to test string length > 36
characters
by reference aString
by value 50 size 2
by reference theError
display aString space theError
stop run
.

test-num-call.
call "test-num" using
by reference aString
by value function length (aString) size 2
by reference theError.
-------------
Have fun!
-------------------------------
Rick Smith
e-mail: < ric··.@ais··s.com >
```

##### ↳ ↳ Re: Test for numeric value

- **From:** "vern_b..." <ua-author-13503960@usenetarchives.gap>
- **Date:** 1998-08-22T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db12bc072a-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-db12bc072a-p7@usenetarchives.gap>`
- **References:** `<35ddf1bf.10139904@netnews.worldnet.att.net> <gap-db12bc072a-p7@usenetarchives.gap>`

```
On Sat, 22 Aug 1998 05:15:12 GMT, dav··.@ya··o.com wrote:

› If your data is coming from an external source which cannot be trusted, even
› if you fix the initial problem in your code you will still need a more
…[12 more quoted lines elided]…
› 

Hi Dave,

I had not thought of that possibility. But now I will :-).

Thanks!

Vern

›  Ver··.@new··t.com (Vern Bradner) wrote:
›› Hi,
…[56 more quoted lines elided]…
› http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum

Vern Bradner ver··.@new··t.com

My opinions are not necessarily those of Newcourt.
```

#### ↳ Re: Test for numeric value

- **From:** "gordon...." <ua-author-10958913@usenetarchives.gap>
- **Date:** 1998-08-22T20:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db12bc072a-p13@usenetarchives.gap>`
- **In-Reply-To:** `<35ddf1bf.10139904@netnews.worldnet.att.net>`
- **References:** `<35ddf1bf.10139904@netnews.worldnet.att.net>`

```
Ver··.@new··t.com (Vern Bradner) wrote:

› Hi,
› 
…[55 more quoted lines elided]…
› My opinions are not necessarily those of Newcourt.

Once you validate that the field contains a correctly formated number you can
use the function NUMVAL or NUMVAL-C to convert the number (what ever the form)
to numeric data. The function does a pretty good job of converting any format
number to a numeric value. Try it out!
------------------------------------------------
Gordon DeGrandis _____ GDe··.@Con··e.be
Contraste Europe S.A.
These are my opinions
```

##### ↳ ↳ Re: Test for numeric value

- **From:** "vern_b..." <ua-author-13503960@usenetarchives.gap>
- **Date:** 1998-08-26T20:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db12bc072a-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-db12bc072a-p13@usenetarchives.gap>`
- **References:** `<35ddf1bf.10139904@netnews.worldnet.att.net> <gap-db12bc072a-p13@usenetarchives.gap>`

```
On Sun, 23 Aug 1998 21:09:08 GMT, Gor··.@pi··g.be (Gordon
DeGrandis) wrote:

› Ver··.@new··t.com (Vern Bradner) wrote:
› 
…[66 more quoted lines elided]…
› These are my opinions

Hi Gordon,

I will check it out.

Thanks!

Vern
Vern Bradner ver··.@new··t.com

My opinions are not necessarily those of Newcourt.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
