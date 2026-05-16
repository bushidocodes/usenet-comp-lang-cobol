[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Basic as a business language

_19 messages · 9 participants · 1998-12 → 1999-01_

---

### Basic as a business language

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76g10o$1e5$1@news.igs.net>`

```
In an attempt to explain to a newbie "why Cobol", I demo'd
the following to him:

10 FOR i = 1 TO 100
20 IF ((1 / i) * (i * i)) <> i THEN PRINT ((1 / i) * (i * i)), i
30 NEXT i

(which fails on 4 values in the 100 under QBASIC)

I was curious how VB fares on the same test, but do not
have a copy.  Anybody willing to run the test, out of curiosity?
```

#### ↳ Re: Basic as a business language

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76g6fr$12o$1@server.cntfl.com>`
- **References:** `<76g10o$1e5$1@news.igs.net>`

```

Donald Tees wrote in message <76g10o$1e5$1@news.igs.net>...
>In an attempt to explain to a newbie "why Cobol", I demo'd
>the following to him:
…[9 more quoted lines elided]…
>
In VB 5.0, it failed 13 times. When I defined i to be either
an integer or long, it did not fail.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

#### ↳ Re: Basic as a business language

- **From:** "Art Perry" <arthur.perry@eds88.com>
- **Date:** 1998-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76g80h$kqe$1@news.ses.cio.eds.com>`
- **References:** `<76g10o$1e5$1@news.igs.net>`

```
Donald Tees wrote in message <76g10o$1e5$1@news.igs.net>...
>10 FOR i = 1 TO 100
>20 IF ((1 / i) * (i * i)) <> i THEN PRINT ((1 / i) * (i * i)), i
>30 NEXT i
>I was curious how VB fares on the same test, but do not
>have a copy.  Anybody willing to run the test, out of curiosity?


I am a relative newbie, and I don't really understand what your test is
trying to show.  I ran it in visual basic and it didn't print anything.  The
results of the calculation (1/i)*(i*i) are the same as i.  Is that the
point?

-Art
```

##### ↳ ↳ Re: Basic as a business language

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76gbuc$7ef$1@news.igs.net>`
- **References:** `<76g10o$1e5$1@news.igs.net> <76g80h$kqe$1@news.ses.cio.eds.com>`

```
In qbasic, they are not.  In fact, that program will
print four values.  Basic switches all to floating point
to do calculations, then changes it back unless you
specifically do string math.  You end up with small
differences that are almost impossible to predict.

If you are trying to balance a set of books, the
result is absolute anarchy.

That VB does not is interesting.  Could you try the same test
up to the value of 10000, instead of 100?

Art Perry wrote in message <76g80h$kqe$1@news.ses.cio.eds.com>...
>Donald Tees wrote in message <76g10o$1e5$1@news.igs.net>...
>>10 FOR i = 1 TO 100
…[7 more quoted lines elided]…
>trying to show.  I ran it in visual basic and it didn't print anything.
The
>results of the calculation (1/i)*(i*i) are the same as i.  Is that the
>point?
>
>-Art
```

###### ↳ ↳ ↳ Re: Basic as a business language

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1999-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3690CFBB.F2C31590@home.com>`
- **References:** `<76g10o$1e5$1@news.igs.net> <76g80h$kqe$1@news.ses.cio.eds.com> <76gbuc$7ef$1@news.igs.net>`

```
I believe REXX can be set up to handle any size integers!!!  If your
integers were larger than the computer would handle natively, it slowed
down considerably.

I suppose a string handling language such as lisp may do the same
thing.  I wonder which languages are effective in calculating pi to
5,000 places.

Who here has had to fudge numbers larger than what their COBOL
implementation can handle natively?  How did you do it?
```

###### ↳ ↳ ↳ Re: Basic as a business language

_(reply depth: 4)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36917c13.100333245@news1.ibm.net>`
- **References:** `<76g10o$1e5$1@news.igs.net> <76g80h$kqe$1@news.ses.cio.eds.com> <76gbuc$7ef$1@news.igs.net> <3690CFBB.F2C31590@home.com>`

```
On Mon, 04 Jan 1999 07:27:07 -0700, Howard Brazee
<NOSPAMbrazee@home.com> wrote:

>I believe REXX can be set up to handle any size integers!!!  If your
>integers were larger than the computer would handle natively, it slowed
…[7 more quoted lines elided]…
>implementation can handle natively?  How did you do it?

Leif's ETK at http://www.etk.com has a neat way to do it.  Pretty
clean.
```

###### ↳ ↳ ↳ Re: Basic as a business language

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1999-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3690CFC0.1900D24@home.com>`
- **References:** `<76g10o$1e5$1@news.igs.net> <76g80h$kqe$1@news.ses.cio.eds.com> <76gbuc$7ef$1@news.igs.net>`

```
I believe REXX can be set up to handle any size integers!!!  If your
integers were larger than the computer would handle natively, it slowed
down considerably.

I suppose a string handling language such as lisp may do the same
thing.  I wonder which languages are effective in calculating pi to
5,000 places.

Who here has had to fudge numbers larger than what their COBOL
implementation can handle natively?  How did you do it?
```

###### ↳ ↳ ↳ Re: Basic as a business language

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yV5k2.2857$0t.1812763@news4.mia>`
- **References:** `<76g10o$1e5$1@news.igs.net> <76g80h$kqe$1@news.ses.cio.eds.com> <76gbuc$7ef$1@news.igs.net> <3690CFC0.1900D24@home.com>`

```
Howard Brazee wrote:
>
>Who here has had to fudge numbers larger than what their COBOL
>implementation can handle natively?  How did you do it?

I have written long precision routines in COBOL, but it has been quite
a while, and I no longer have them.  If you want to see high precision
(up to 1075 digits) handled in C, you can download BIGCALC.ZIP from my
web page below.  BIGCALC is a RPN calculator which can do logs, trig,
powers, etc. as easily as a normal calculator.  Add and subtract are
simple, and multiply is not difficult.  Divide is much more complex,
especially if it is efficient.  Everything else is built on the basic
four functions.

The simplest conceptual way is probably to use a table for each number,
where one element is a digit.  Then write algorithms to handle them as
you learned to do in grammar school.  Keep the signs separate, and deal
with the numbers as if they were positive, then set the signs.  To add
numbers with opposite signs, subtract the smaller absolute value from
the larger absolute value and set the sign of the result to the sign of
the larger absolute value.  For multiply and divide the resultant sign
is positive if the two input signs are the same, negative if they are
different.  To subtract a negative number, reverse the sign of the
subtrahend and add.  And so on.

For example, to multiply you can do just what you do on paper:

       1 2 3 4 -
      x  5 6 7 +  (signs different, result negative)
   -------------
       8 6 3 8
     7 4 0 4
   6 1 7 0
   -------------
   6 9 9 6 7 8 -

However, you don't have to keep the intermediate rows.  Add all results
immediately into the product field.

Divide is usually implemented as a series of subtracts.  Left align the
subtrahend with the minuend, and start subtracting.  Each time you
successfully subtract the subtrahend from the minuend, add 1 to the
quotient, shifted as many digits as you shifted the subtrahend to match
the left of the minuend.  When you get an underflow, then restore the
minuend by adding back any part of the subtrahend which you have already
subtracted from the minuend on that cycle, then shift the subtrahend one
position to the right, as well as the pointer into the product where you
are adding each subtract cycle.  If you structure your number tables so
it is easy to do, you can compare the subtrahend against the part of the
minuend it is shifted to, so you don't have to subtract when the minuend
is smaller.  If the compare is efficient, it is faster than the partial
subtract.  Continue this process until the minuend is zero or until the
desired accuracy is reached.  In BIGCALC I divide the first few digits
of the subtrahend into the first few digits of the subtrahend, and use
that as a multiple to do the subtracts in one cycle.  This is probably
efficient only if you have a large number of digits.

You can speed up the basic processes by keeping more than one digit in
each table entry.  In COBOL you can keep up to 18 digits, but you should
keep only 9 digits to avoid overflow on multiply.
```

###### ↳ ↳ ↳ Re: Basic as a business language

_(reply depth: 5)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76qv30$phv$1@news.igs.net>`
- **References:** `<76g10o$1e5$1@news.igs.net> <76g80h$kqe$1@news.ses.cio.eds.com> <76gbuc$7ef$1@news.igs.net> <3690CFC0.1900D24@home.com> <yV5k2.2857$0t.1812763@news4.mia>`

```
While the digit by digit method works quite well, the way
that I have done it in the past is a small variation.  You take
the large number, and redefine it as an array of large integers
that can be handled.  One then does exactly the same thing
(without the tables) as one would do with single digits,
adding the carry from the low order to the top.  I have no
idea how the two would compare in speed.  The time that I
did it I only had a couple of numbers to deal with, and time
was not critical enough to experiment.

Judson McClendon wrote in message ...
>Howard Brazee wrote:
>>
…[65 more quoted lines elided]…
>
```

#### ↳ Re: Basic as a business language

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<368bddea.46528011@netnews>`
- **References:** `<76g10o$1e5$1@news.igs.net>`

```
'Twas Thu, 31 Dec 1998 09:18:39 -0500, when "Donald Tees"
<donald@willmack.com> illuminated comp.lang.cobol thusly:

>In an attempt to explain to a newbie "why Cobol", I demo'd
>the following to him:
…[3 more quoted lines elided]…
>30 NEXT i

I'm not this familiar with QBasic (though two weeks ago I billed about 40
hours of QBasic work at my A Series Cobol guru rate).  It appears to be
impossible to precisely store an intermediate result.  I tried LONG,
SINGLE and DOUBLE in the DIM statement below, but I still got your four
failures.

  DIM j AS DOUBLE
  FOR i = 1 TO 100
  LET j = ((1 / i) * (i * i))
  IF j <> ((1 / i) * (i * i)) THEN PRINT j; "-"; ((1 / i) * (i * i)); "=";
j - ((1 / i) * (i * i))
  NEXT i
```

##### ↳ ↳ Re: Basic as a business language

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76grrn$j59$1@news.igs.net>`
- **References:** `<76g10o$1e5$1@news.igs.net> <368bddea.46528011@netnews>`

```
The real problem with basic is that it converts to floating
point for all decimals.  As soon as you get away from integers
for dollars and cents, you are in trouble.  Ten cents expressed
as "$0.10" is a repeating decimal, like it or not.

If you have to write financial stuff in basic, the only way it
will ever work reliably is to do all accounting in pennies, and
convert only for output.  As long as you have enough precision
that will work.  Even then, however, when it comes to stuff
like percentage calculations, you had better insure that you
convert back to integer form before you start adding and
subtracting. By the time you are done, the code is about four
times as verbose as Cobol.

This one always astonishes beginners:

10 for i = 1 to 1000000
20 x = x + 0.1
30 next  i
40 print x

Randall Bart wrote in message <368bddea.46528011@netnews>...
>'Twas Thu, 31 Dec 1998 09:18:39 -0500, when "Donald Tees"
><donald@willmack.com> illuminated comp.lang.cobol thusly:
…[28 more quoted lines elided]…
>l    |/ MS^7=6/28/107   http://members.aol.com/PanicYr00/Sequence.html
```

###### ↳ ↳ ↳ Re: Basic as a business language

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76h6g4$ngc$1@server.cntfl.com>`
- **References:** `<76g10o$1e5$1@news.igs.net> <368bddea.46528011@netnews> <76grrn$j59$1@news.igs.net>`

```

Donald Tees wrote in message <76grrn$j59$1@news.igs.net>...
>The real problem with basic is that it converts to floating
>point for all decimals.  As soon as you get away from integers
…[10 more quoted lines elided]…
>times as verbose as Cobol.
[...]

Although your statements are correct, with respect to the older
BASICs, they are not particularly valid with Visual Basic. The
Visual Basic "currency" data type is intended for use with fixed
decimal values. It is equivalent to specifying S9(14)V9(4)
BINARY, in COBOL.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: Basic as a business language

_(reply depth: 4)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76hd5e$sjm$1@news.igs.net>`
- **References:** `<76g10o$1e5$1@news.igs.net> <368bddea.46528011@netnews> <76grrn$j59$1@news.igs.net> <76h6g4$ngc$1@server.cntfl.com>`

```
Thats interesting to know. It would certainly make
life a lot easier.  Is there anyway of declaring any
other "picture" types, or is that the only one?

There were also a bunch of Basics a few years back
that had "character arithmetic".  It was done with ASCII
type strings much like Cobol data but null terminated.

Rick Smith wrote in message <76h6g4$ngc$1@server.cntfl.com>...
>
>Donald Tees wrote in message <76grrn$j59$1@news.igs.net>...
…[24 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Basic as a business language

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76hngb$5oi$1@server.cntfl.com>`
- **References:** `<76g10o$1e5$1@news.igs.net> <368bddea.46528011@netnews> <76grrn$j59$1@news.igs.net> <76h6g4$ngc$1@server.cntfl.com> <76hd5e$sjm$1@news.igs.net>`

```

Donald Tees wrote in message <76hd5e$sjm$1@news.igs.net>...
>Thats interesting to know. It would certainly make
>life a lot easier.  Is there anyway of declaring any
>other "picture" types, or is that the only one?

This is the only one that has decimal positions.


>Rick Smith wrote in message <76h6g4$ngc$1@server.cntfl.com>...
>>
[...]
>>
>>[...] The
>>Visual Basic "currency" data type is intended for use with fixed
>>decimal values. It is equivalent to specifying S9(14)V9(4)
>>BINARY, in COBOL.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: Basic as a business language

_(reply depth: 6)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XB3j2.1546$Zk.562050@news3.mia>`
- **References:** `<76g10o$1e5$1@news.igs.net> <368bddea.46528011@netnews> <76grrn$j59$1@news.igs.net> <76h6g4$ngc$1@server.cntfl.com> <76hd5e$sjm$1@news.igs.net> <76hngb$5oi$1@server.cntfl.com>`

```
Rick Smith wrote:
>
>Donald Tees wrote:
…[5 more quoted lines elided]…
>This is the only one that has decimal positions.


Check out VB type 'Decimal', which is 96 bit decimal floating point.
However, it can only be declared for use in a variant.
```

###### ↳ ↳ ↳ Re: Basic as a business language

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76ivmm$q3m$1@server.cntfl.com>`
- **References:** `<76g10o$1e5$1@news.igs.net> <368bddea.46528011@netnews> <76grrn$j59$1@news.igs.net> <76h6g4$ngc$1@server.cntfl.com> <76hd5e$sjm$1@news.igs.net> <76hngb$5oi$1@server.cntfl.com> <XB3j2.1546$Zk.562050@news3.mia>`

```

Judson McClendon wrote in message ...
>Rick Smith wrote:
>>
…[4 more quoted lines elided]…
>--
I was not aware of its existence!

This allows for any representation in the form:

        PIC S9(m)V9(n) BINARY; where m + n < 29.

It still has all the problems of floating point; since one would
necessarily need to force rounding or truncation to ensure that
values extending past 'n' always contain zeros.

Usable, but still clumsy when compared with COBOL!

I get to learn something new every day.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: Basic as a business language

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Uz3j2.1545$Zk.561532@news3.mia>`
- **References:** `<76g10o$1e5$1@news.igs.net> <368bddea.46528011@netnews> <76grrn$j59$1@news.igs.net>`

```
Donald Tees wrote:
>The real problem with basic is that it converts to floating
>point for all decimals.  As soon as you get away from integers
…[10 more quoted lines elided]…
>times as verbose as Cobol.

The same holds equally true for C and most other languages which
do not support scaled decimal math.  In my opinion, anybody who
chooses to write money handling programs in C/C++, Java, etc.,
in situations when COBOL could be used, has a screw loose.  Yes,
you could write classes in C++ and Java to handle it after a
fashion, but why should you?  Note that VB and PDS 7.1 have a
CURRENCY data type which is equivalent to PIC S9(14)V9(4).  VB
has 'Decimal' a 96 bit decimal floating point variant data type.

>This one always astonishes beginners:
>
…[3 more quoted lines elided]…
>40 print x


Even simpler, try this

10 FOR I=0 TO 1 STEP .1
20   PRINT I,
30 NEXT

It makes one shudder to think that people actually use this stuff
to handle money.  Ugh!
```

###### ↳ ↳ ↳ Re: Basic as a business language

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<368F5B7F.B3F0A19B@zip.com.au>`
- **References:** `<76g10o$1e5$1@news.igs.net> <368bddea.46528011@netnews> <76grrn$j59$1@news.igs.net> <Uz3j2.1545$Zk.561532@news3.mia>`

```
Judson McClendon wrote:
> 
> The same holds equally true for C and most other languages which
…[8 more quoted lines elided]…
> Judson McClendon      judmc123@bellsouth.net  (remove numbers)

The MVS C370 has an extension that allows you to define packed fields in
exactly the same way as Cobol.

Ken
```

#### ↳ Re: Basic as a business language

- **From:** "Kevin G. Rhoads" <T_Rhoads@NoSpam.CLASSIC.MSN.COM>
- **Date:** 1999-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be34f9$d5b89f20$LocalHost@stupidwin95>`
- **References:** `<76g10o$1e5$1@news.igs.net>`

```
Curious, I tried it both as written, and with an auxilliry variable
15 J = (1/I)*(I*I)
with QuickBasic 4.5 -- when compiled to an EXE either
from the IDE or from the command line it runs fine.
(i.e., nothing printed.)  This was true for both 1 .. 100
and 1 .. 10000 ranges.  The (uncompressed) EXE is under
30k if anyone wants it by e-mail.

When executed interactively, it runs fine with the auxilliary
variable (again, nothing printed) .

When executed interactively W/O the auxilliary variable
results varied -- sometimes printing EVERY line with
two identical numbers but more often printing nothing.

But it never printed just four numbers.   

I thought QBasic was just a stripped down version of
QuickBasic, but it looks like the differences may be
more fundamental.  

If I get a chance I'll see if I can translate this into VB4
for windows (16 and 32 bits) and see how it does.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
