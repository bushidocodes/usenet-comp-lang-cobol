[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Check Digit

_12 messages · 10 participants · 1998-11 → 1998-12_

---

### Check Digit

- **From:** suevarma@aol.com (Sue Varma)
- **Date:** 1998-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981121183013.09762.00001484@ng40.aol.com>`

```
CAn anyone out there help me. I am working with check digits at the moment and
need to know how to work out the modulus of a number. What is the modulus? and
how is it calculated. Many thanks in advance to anyone who can help.
```

#### ↳ Re: Check Digit (modulo arithmetic)

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 1998-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3657BE1E.3BA29B4C@worldnet.att.net>`
- **References:** `<19981121183013.09762.00001484@ng40.aol.com>`

```
Sue Varma wrote:
> 
> CAn anyone out there help me. I am working with check digits at the moment and
> need to know how to work out the modulus of a number. What is the modulus? and
> how is it calculated. Many thanks in advance to anyone who can help.

If your compiler has intrinsic functions, there is a FUNCTION MOD, I
believe.  If not, then modulo arithmetic can generally be done using
DIVIDE ... GIVING ... REMAINDER.  It's the remainder that you're
interested in.

For example, if you have a date expressed as the absolute count of days
from a base date, and you know the day of week for the base date, then
divide the day-count by seven and save only the remainder (daycount
modulo 7).  You can easily use that to determine the day of the week.

Another example is Leap Year calculation.  The simplest rule is if YEAR
modulo 4 equals zero, then it's a leap year (ignoring the 100-year and
400-year rules).  
```

##### ↳ ↳ Re: Check Digit (modulo arithmetic)

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-11-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3659700B.1B03DA49@home.com>`
- **References:** `<19981121183013.09762.00001484@ng40.aol.com> <3657BE1E.3BA29B4C@worldnet.att.net>`

```
> Another example is Leap Year calculation.  The simplest rule is if YEAR
> modulo 4 equals zero, then it's a leap year (ignoring the 100-year and
> 400-year rules).

So far, I haven't seen cases where COBOL programmers have ignored the
100 and 400 year rules.  Maybe we're not as dumb as the press indicates.
```

###### ↳ ↳ ↳ Re: Check Digit (modulo arithmetic)

- **From:** "Warren Porter" <warrenp@netdoor.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%OH62.2309$b53.11587@axe.netdoor.com>`
- **References:** `<19981121183013.09762.00001484@ng40.aol.com> <3657BE1E.3BA29B4C@worldnet.att.net> <3659700B.1B03DA49@home.com>`

```

Howard Brazee wrote in message <3659700B.1B03DA49@home.com>...
>> Another example is Leap Year calculation.  The simplest rule is if YEAR
>> modulo 4 equals zero, then it's a leap year (ignoring the 100-year and
…[3 more quoted lines elided]…
>100 and 400 year rules.  Maybe we're not as dumb as the press indicates.

I don't know if ignore is the right word.  No living COBOL programmer will
ever see a century year that won't be a leap year.
```

###### ↳ ↳ ↳ Re: Check Digit (modulo arithmetic)

_(reply depth: 4)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<enU3JbVG#GA.220@upnetnews05>`
- **References:** `<19981121183013.09762.00001484@ng40.aol.com> <3657BE1E.3BA29B4C@worldnet.att.net> <3659700B.1B03DA49@home.com> <%OH62.2309$b53.11587@axe.netdoor.com>`

```

Warren Porter wrote in message
>
>Howard Brazee wrote in message <3659700B.1B03DA49@home.com>...
…[9 more quoted lines elided]…
>


And modesty prohibits the vast majority of COBOL programmers now extant from
daring to dream that any of their code will still be executing in production
in the year MMC (2100, with an 'Italian' accent)?
```

###### ↳ ↳ ↳ Re: Check Digit (modulo arithmetic)

_(reply depth: 5)_

- **From:** Albert Ratzlaff <albert@infonet.com.py>
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365E8B40.28FBAD94@infonet.com.py>`
- **References:** `<19981121183013.09762.00001484@ng40.aol.com> <3657BE1E.3BA29B4C@worldnet.att.net> <3659700B.1B03DA49@home.com> <%OH62.2309$b53.11587@axe.netdoor.com> <enU3JbVG#GA.220@upnetnews05>`

```


"Dennis J. Minette" wrote:

> And modesty prohibits the vast majority of COBOL programmers now extant from
> daring to dream that any of their code will still be executing in production
> in the year MMC (2100, with an 'Italian' accent)?

Just in case, I code all date with ten digits ;-)

Regards
Albert Ratzlaff
```

###### ↳ ↳ ↳ Re: Check Digit (modulo arithmetic)

_(reply depth: 6)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73pvm7$q4u$1@news.igs.net>`
- **References:** `<19981121183013.09762.00001484@ng40.aol.com> <3657BE1E.3BA29B4C@worldnet.att.net> <3659700B.1B03DA49@home.com> <%OH62.2309$b53.11587@axe.netdoor.com> <enU3JbVG#GA.220@upnetnews05> <365E8B40.28FBAD94@infonet.com.py>`

```
Albert Ratzlaff wrote in message <365E8B40.28FBAD94@infonet.com.py>...

>Just in case, I code all date with ten digits ;-)


I hear we have another year two thousand problem on our hands.
It seems that someone at Microsoft has discovered that all their
code stops running correctly at midnight of the day it is installed.

The bug has been in production at a base level now for seven years
and has infected all their product lines and DLLs.  It was only noticed
last week, as this was always considered normal for Microsoft
products; however, now that it has been noticed, MS says it will
be working on it ...
```

###### ↳ ↳ ↳ Re: Check Digit (modulo arithmetic)

_(reply depth: 6)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73pvq6$q74$1@news.igs.net>`
- **References:** `<19981121183013.09762.00001484@ng40.aol.com> <3657BE1E.3BA29B4C@worldnet.att.net> <3659700B.1B03DA49@home.com> <%OH62.2309$b53.11587@axe.netdoor.com> <enU3JbVG#GA.220@upnetnews05> <365E8B40.28FBAD94@infonet.com.py>`

```
I noticed on that last post that MS's own spelling checker
suggested that I change MicroSoft to microfossil.   Perhaps
their software is getting better?
```

###### ↳ ↳ ↳ Re: Check Digit (modulo arithmetic)

_(reply depth: 6)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<udq3mMxG#GA.154@upnetnews03>`
- **References:** `<19981121183013.09762.00001484@ng40.aol.com> <3657BE1E.3BA29B4C@worldnet.att.net> <3659700B.1B03DA49@home.com> <%OH62.2309$b53.11587@axe.netdoor.com> <enU3JbVG#GA.220@upnetnews05> <365E8B40.28FBAD94@infonet.com.py>`

```

Albert Ratzlaff wrote in message <365E8B40.28FBAD94@infonet.com.py>...
>
>
>"Dennis J. Minette" wrote:
>
>> And modesty prohibits the vast majority of COBOL programmers now extant
from
>> daring to dream that any of their code will still be executing in
production
>> in the year MMC (2100, with an 'Italian' accent)?
>
>Just in case, I code all date with ten digits ;-)

Binary, octal, decimal, hexadecimal or Roman?<G>


>Regards
>Albert Ratzlaff
>
>
```

#### ↳ Re: Check Digit

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1998-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EFC4A6F2D059FB23.557850B3553EF866.2BC28761154215A5@library-proxy.airnews.net>`
- **References:** `<19981121183013.09762.00001484@ng40.aol.com>`

```
On 21 Nov 1998 23:30:13 GMT, suevarma@aol.com (Sue Varma) enlightened
us:

>CAn anyone out there help me. I am working with check digits at the moment and
>need to know how to work out the modulus of a number. What is the modulus? and
>how is it calculated. Many thanks in advance to anyone who can help.

A modulus is defined as:  A number by which two given numbers can be
divided and produce the same remainder.  It can also mean:  The
absolute value of a complex number.  When working with check digits,
the modulus or mod, as it is sometimes called, is usually a single
number.  In the banking industry where I've worked the most common
ones I've seen are mod 11 and mod 9.  Each has its own formula for
calculating the check digit.  If you need an example, let me know and
I'll dig up what I have and post it.

HTH

Regards,

          ////
         (o o)
-oOO--(_)--OOo-
I went to a bookstore and asked the saleswoman where the Self Help
section was. She said if she told me it would defeat the purpose.


 Steve
```

#### ↳ Re: Check Digit

- **From:** jraben19@mail.idt.net (Jeff Raben)
- **Date:** 1998-12-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3666b6e8.2520343@news.idt.net>`
- **References:** `<19981121183013.09762.00001484@ng40.aol.com>`

```
suevarma@aol.com (Sue Varma) wrote:

>CAn anyone out there help me. I am working with check digits at the moment and
>need to know how to work out the modulus of a number. What is the modulus? and
>how is it calculated. Many thanks in advance to anyone who can help.

with some minor variations 'mod' is the remainder of an integer
divide.

15 mod 10 = 5,   25 mod 10=5

however checkdigits are often far more complex being weighted by
occurance of digits in different positions of a source number.

say  # 12345   may be  1*ckd1 + 2*chk2 + 3*chk3 + 4*chk4 + 5*chk5=sum
     sum mod 10 = ?    there is the checkdigit for 12345.
where ckd-n  was a weighted occurance. 
in some formulas, if the wieghts were even take the carry and add it
back to the first digit..
7*2=14 don't use the 4 but use 5  (1+4) for summing.....

for a project i was on ckd1=7 ckd2=3 ckd3=1 ... ckd4=7 again etc.....
our checkdigit was a little more complex but....
  simple variations are based on how often the first digit of a (say)
5-digit part number went from 0 to 9.  

the idea is to catch transposition errors during writing/typing.

enough????


jr
and stir with a Runcible spoon...
```

##### ↳ ↳ Re: Check Digit

- **From:** "Martin G. Diehl" <mdiehl@nac.net>
- **Date:** 1998-12-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3672A172.BFBAC9E3@nac.net>`
- **References:** `<19981121183013.09762.00001484@ng40.aol.com> <3666b6e8.2520343@news.idt.net>`

```
Jeff Raben wrote:
> 
> suevarma@aol.com (Sue Varma) wrote:
…[31 more quoted lines elided]…
> and stir with a Runcible spoon...

Another example of Check Digits is the identification number that 
identifies a security (bond, or stock) -- the CUSIP number.  The 
check digit is based on "Modulus 10 Double Add Double" and uses the 
complement of the last digit of the sum as the check digit vlaue.  
See http://www.cusip.com/ for a full explanation with examples.  
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
