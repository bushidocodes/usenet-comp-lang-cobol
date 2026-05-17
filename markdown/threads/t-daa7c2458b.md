[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# General Info

_19 messages · 12 participants · 1998-03_

---

### General Info

- **From:** "lok..." <ua-author-1038600@usenetarchives.gap>
- **Date:** 1998-03-11T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980312030600.WAA06952@ladder02.news.aol.com>`

```

I have a couple of questions that hopefull someone can answer. First of all,
what is the difference between Cobol and C? Also, is Cobol a broad based
language (in the sense that it is used for many types of applications) or is it
used generally in a business or other environment. No, I'm not a student
trying to do some homework. Thanks for any responses in advance.
```

#### ↳ Re: General Info

- **From:** "jim rivera" <ua-author-902354@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daa7c2458b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19980312030600.WAA06952@ladder02.news.aol.com>`
- **References:** `<19980312030600.WAA06952@ladder02.news.aol.com>`

```

Lok1220 wrote:
› 
› I have a couple of questions that hopefull someone can answer.  First of all,
…[3 more quoted lines elided]…
› trying to do some homework.  Thanks for any responses in advance.


Here goes.
COBOL = good for business, is much concerned with input & output & file
handling.

C = for systems work, very efficient but not as good as assembler.

These are two very different languages, from opposite ends of the
software spectrum and ideology. C. especially Windows, is harder (let
the flames come, I know both & stand by my statement, there's nothing
like Intel segments in COBOL), and closer to a "pure" language. COBOL
is sometimes used for things it shouldn't do. So is C. There are some
business systems in C but it's not the best use of the language -
something like putting a race horse in fromt of a plow.

JR


JR
```

##### ↳ ↳ Re: General Info

- **From:** "jerry peacock" <ua-author-36061@usenetarchives.gap>
- **Date:** 1998-03-11T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daa7c2458b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daa7c2458b-p2@usenetarchives.gap>`
- **References:** `<19980312030600.WAA06952@ladder02.news.aol.com> <gap-daa7c2458b-p2@usenetarchives.gap>`

```


Jim Rivera wrote in message <6e80pj$g.··.@bgt··t.net>...
› Lok1220 wrote:
›› 
…[8 more quoted lines elided]…
› 
Another take:
COBOL (Common Business Oriented Language) was the first of the
so-called "High-Level" languages, was designed by a committee under
the direction of the Department of Defense.

There exists a spectrum of programming languages that range from the
specific machine languate ('1' & '0') to the abstract. One rendition might
be:
machine language
assembly language (1 source statement = 1 machine instruction)
C (1 source statement = very few machine instructions)
FORTRAN (1 source statement = a few machine instrucions)
BASIC
(others)
COBOL (1 source statement = many machine instructions)
LISP (1 source statement = very many machine instrucions)
Get-Mull-Put

The last one is a joke, but you get the idea.

Each language has its strenghts (and weaknesses). For example:
Floating a dollar sign to the immediate left of a number
COBOL=trivial, FORTRAN=very hard, C=damned near impossible
Computing the hyperbolic arc tangent of an angle
FORTRAN=trivial, COBOL=leads to heroin addiction
Computing the inverse of a 50x50 matrix
C=takes years, COBOL=causes rash, LISP=one statement

>From a management perspective, however, COBOL is far, far
superior to almost any other language for almost any task. First,
with minimal policy guidelines, it is difficult to write really bad code.
Second, COBOL is easier to maintain and revise than its
contemporaries. Both of these conditions result in cheaper
development and maintenance.

Just my experience and observations.

Good Luck
```

###### ↳ ↳ ↳ Re: General Info

- **From:** "gvwm..." <ua-author-47960@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daa7c2458b-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daa7c2458b-p3@usenetarchives.gap>`
- **References:** `<19980312030600.WAA06952@ladder02.news.aol.com> <gap-daa7c2458b-p2@usenetarchives.gap> <gap-daa7c2458b-p3@usenetarchives.gap>`

```

On Thu, 12 Mar 1998 21:41:22 -0600, "Jerry Peacock"
wrote:

› Floating a dollar sign to the immediate left of a number
› COBOL=trivial, FORTRAN=very hard, C=damned near impossible


oh thats easy.

long number;
int temp;
temp=strlen(_ltoa(number));
printf("$");
for(int lp=0;lp<(num_float_points-temp);++lp)
printf(" ");
printf("%l",number);

if you can read that, you are a real programmer.


gvw··.@ix.··m.com remove the spam
```

###### ↳ ↳ ↳ Re: General Info

_(reply depth: 4)_

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1998-03-13T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daa7c2458b-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daa7c2458b-p4@usenetarchives.gap>`
- **References:** `<19980312030600.WAA06952@ladder02.news.aol.com> <gap-daa7c2458b-p2@usenetarchives.gap> <gap-daa7c2458b-p3@usenetarchives.gap> <gap-daa7c2458b-p4@usenetarchives.gap>`

```

G Moore wrote:
›  wrote:
› 
…[13 more quoted lines elided]…
› if you can read that, you are a real programmer.

Your version will print something like "$ 123". For " $123"
instead, try this change:

for(int lp=0;lp<(num_float_points-temp);++lp)
printf(" ");
printf("$");
printf("%l",number);

Where's the decimal point? Money amounts are almost always printed
with decimal points. Using float types will give you binary rounding
problems with pennies. Just one of the many things which make C a
very poor choice for business programming. Anyway, PIC $$$,$$$.99
is MUCH easier. :-)
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: General Info

_(reply depth: 5)_

- **From:** "gvwm..." <ua-author-47960@usenetarchives.gap>
- **Date:** 1998-03-13T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daa7c2458b-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daa7c2458b-p5@usenetarchives.gap>`
- **References:** `<19980312030600.WAA06952@ladder02.news.aol.com> <gap-daa7c2458b-p2@usenetarchives.gap> <gap-daa7c2458b-p3@usenetarchives.gap> <gap-daa7c2458b-p4@usenetarchives.gap> <gap-daa7c2458b-p5@usenetarchives.gap>`

```

On 14 Mar 1998 23:48:37 GMT, "Judson McClendon"
wrote:

› G Moore  wrote:
››  wrote:
…[17 more quoted lines elided]…
› instead, try this change:
 
›  for(int lp=0;lp<(num_float_points-temp);++lp)
› printf(" ");
›  printf("$");
›  printf("%l",number);
 
› Where's the decimal point?  Money amounts are almost always printed
› with decimal points.  Using float types will give you binary rounding
› problems with pennies.  Just one of the many things which make C a
› very poor choice for business programming.  Anyway, PIC $$$,$$$.99
› is MUCH easier.  :-)

ho hum. guess i mixed up fixed with floating dollars.
in any case, to do the float thingy...
(now maintaining C code ...)

float number;
number=(long) (number * 100);
number/=100;
/*that should get rid of the extra decimal*/

/* use _ftoa instead of _itoa*/



gvw··.@ix.··m.com remove the spam
```

###### ↳ ↳ ↳ Re: General Info

_(reply depth: 6)_

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1998-03-14T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daa7c2458b-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daa7c2458b-p6@usenetarchives.gap>`
- **References:** `<19980312030600.WAA06952@ladder02.news.aol.com> <gap-daa7c2458b-p2@usenetarchives.gap> <gap-daa7c2458b-p3@usenetarchives.gap> <gap-daa7c2458b-p4@usenetarchives.gap> <gap-daa7c2458b-p5@usenetarchives.gap> <gap-daa7c2458b-p6@usenetarchives.gap>`

```

G Moore wrote:
› Judson McClendon  wrote:
›› G Moore  wrote:
…[38 more quoted lines elided]…
› /*that should get rid of the extra decimal*/

Not really. The binary rounding problem can't be solved that easily.

#include "stdio.h"
void main(void)
{
float number, value;
for (value = 0; value <= 1; value += .01) {
number = (long) (value * 100);
number /= 100;
printf("%10.8f\n", number);
}
}

0.00000000 0.00000000 0.01000000 0.02000000 0.03000000 0.05000000 0.06000000
0.07000000 0.07000000 0.08000000 0.09000000 0.10000000 0.11000000 0.12000000
0.14000000 0.15000000 0.16000000 0.17000000 0.18000000 0.19000000 0.20000000
0.21000000 0.22000000 0.22999999 0.23999999 0.24999999 0.25999999 0.26999999
0.27999999 0.28999999 0.29999999 0.30999999 0.30999999 0.31999999 0.32999999
0.33999999 0.34999999 0.35999999 0.36999999 0.37999999 0.38999999 0.39999999
0.40999999 0.41999999 0.42999999 0.43999999 0.44999999 0.45999999 0.46999999
0.47999999 0.48999999 0.49999999 0.50999999 0.51999999 0.52999999 0.53999999
0.54999999 0.55999999 0.56999999 0.57999999 0.58999999 0.59999999 0.60999999
0.61999999 0.62999999 0.63999999 0.64999999 0.65999999 0.66999999 0.67999998
0.68999998 0.69999998 0.70999998 0.71999998 0.72999998 0.73999998 0.74999998
0.75999998 0.76999998 0.77999998 0.78999998 0.79999998 0.80999998 0.81999998
0.82999998 0.83999998 0.84999998 0.85999998 0.86999998 0.87999998 0.88999998
0.89999998 0.90999998 0.91999998 0.92999998 0.93999998 0.94999998 0.95999998
0.96999998 0.97999998 0.98999998

Notice that the first TWO amounts are zero. This is because the binary
representation of .01 is actually LESS than .01, and gets truncated.
Now, wouldn't you really love for your bank to calculate your account
balance like that? :-) Using C to write programs to handle money makes
as much sense as writing an operating system in COBOL.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: General Info

_(reply depth: 7)_

- **From:** "gvwm..." <ua-author-47960@usenetarchives.gap>
- **Date:** 1998-03-18T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daa7c2458b-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daa7c2458b-p7@usenetarchives.gap>`
- **References:** `<19980312030600.WAA06952@ladder02.news.aol.com> <gap-daa7c2458b-p2@usenetarchives.gap> <gap-daa7c2458b-p3@usenetarchives.gap> <gap-daa7c2458b-p4@usenetarchives.gap> <gap-daa7c2458b-p5@usenetarchives.gap> <gap-daa7c2458b-p6@usenetarchives.gap> <gap-daa7c2458b-p7@usenetarchives.gap>`

```

On 15 Mar 1998 11:17:45 GMT, "Judson McClendon"
wrote:

› G Moore  wrote:
›› Judson McClendon  wrote:
 
››››› Floating a dollar sign to the immediate left of a number
›››››    COBOL=trivial, FORTRAN=very hard, C=damned near impossible
…[36 more quoted lines elided]…
› Not really.  The binary rounding problem can't be solved that easily.

kill one bug and another shows up.

how about:

char *temp= _ltoa(number);
char *temp2=strchr (temp, '.');

/* if period is found, truncate it*/
if(temp2)
temp2 [0]=0;



/*insert previous code here for floating dollar*/

printf("%s",temp);



gvw··.@ix.··m.com remove the spam
```

###### ↳ ↳ ↳ Re: General Info

_(reply depth: 8)_

- **From:** "rene..." <ua-author-6375353@usenetarchives.gap>
- **Date:** 1998-03-19T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daa7c2458b-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daa7c2458b-p8@usenetarchives.gap>`
- **References:** `<19980312030600.WAA06952@ladder02.news.aol.com> <gap-daa7c2458b-p2@usenetarchives.gap> <gap-daa7c2458b-p3@usenetarchives.gap> <gap-daa7c2458b-p4@usenetarchives.gap> <gap-daa7c2458b-p5@usenetarchives.gap> <gap-daa7c2458b-p6@usenetarchives.gap> <gap-daa7c2458b-p7@usenetarchives.gap> <gap-daa7c2458b-p8@usenetarchives.gap>`

```

All of a sudden, gvw··.@ix.··m.com (G Moore) wrote:

› On 15 Mar 1998 11:17:45 GMT, "Judson McClendon"
› wrote:
…[63 more quoted lines elided]…
› gvw··.@ix.··m.com remove the spam

That'll teach you to start talking that "C" crap in a COBOL
newsgroup... :)


Dave


You may e-mail replies to: renegade at (@) dwx dot (.) com
```

###### ↳ ↳ ↳ Re: General Info

_(reply depth: 4)_

- **From:** "rene..." <ua-author-6375353@usenetarchives.gap>
- **Date:** 1998-03-14T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daa7c2458b-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daa7c2458b-p4@usenetarchives.gap>`
- **References:** `<19980312030600.WAA06952@ladder02.news.aol.com> <gap-daa7c2458b-p2@usenetarchives.gap> <gap-daa7c2458b-p3@usenetarchives.gap> <gap-daa7c2458b-p4@usenetarchives.gap>`

```

All of a sudden, gvw··.@ix.··m.com (G Moore) wrote:

› On Thu, 12 Mar 1998 21:41:22 -0600, "Jerry Peacock"
› wrote:
…[18 more quoted lines elided]…
› gvw··.@ix.··m.com remove the spam
I may be wrong (my C is a little weak), but your example will not
float the dollar sign just to the left of the number. Instead it will
print it, then several spaces (zero suppress), then print the number.
Something like this:

$ 999 instead of $999. If you run through your "for" loop first,
then print the $ and your number, it should work (I think). I'm not
familiar with the _ltoa function, but I'm assuming that it is
returning the significant digits only (so that temp is set to that
length).


Dave


You may e-mail replies to: renegade at (@) dwx dot (.) com
```

###### ↳ ↳ ↳ Re: General Info

_(reply depth: 5)_

- **From:** "jerry peacock" <ua-author-36061@usenetarchives.gap>
- **Date:** 1998-03-14T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daa7c2458b-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daa7c2458b-p10@usenetarchives.gap>`
- **References:** `<19980312030600.WAA06952@ladder02.news.aol.com> <gap-daa7c2458b-p2@usenetarchives.gap> <gap-daa7c2458b-p3@usenetarchives.gap> <gap-daa7c2458b-p4@usenetarchives.gap> <gap-daa7c2458b-p10@usenetarchives.gap>`

```


Renegade wrote in message <350··.@new··x.com>...
› All of a sudden, gvw··.@ix.··m.com (G Moore) wrote:
› 
…[37 more quoted lines elided]…
› 

See what I mean about floating a dollar sign in C?
```

###### ↳ ↳ ↳ Re: General Info

_(reply depth: 6)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-03-14T19:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daa7c2458b-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daa7c2458b-p11@usenetarchives.gap>`
- **References:** `<19980312030600.WAA06952@ladder02.news.aol.com> <gap-daa7c2458b-p2@usenetarchives.gap> <gap-daa7c2458b-p3@usenetarchives.gap> <gap-daa7c2458b-p4@usenetarchives.gap> <gap-daa7c2458b-p10@usenetarchives.gap> <gap-daa7c2458b-p11@usenetarchives.gap>`

```

Jerry Peacock wrote:

› Renegade wrote in message <350··.@new··x.com>...
›› All of a sudden, gvw··.@ix.··m.com (G Moore) wrote:
…[40 more quoted lines elided]…
› See what I mean about floating a dollar sign in C?

QED, man, QED.

Bill Lynch :-)
```

###### ↳ ↳ ↳ Re: General Info

_(reply depth: 6)_

- **From:** "joe zitzelberger" <ua-author-8235501@usenetarchives.gap>
- **Date:** 1998-03-15T19:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daa7c2458b-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daa7c2458b-p11@usenetarchives.gap>`
- **References:** `<19980312030600.WAA06952@ladder02.news.aol.com> <gap-daa7c2458b-p2@usenetarchives.gap> <gap-daa7c2458b-p3@usenetarchives.gap> <gap-daa7c2458b-p4@usenetarchives.gap> <gap-daa7c2458b-p10@usenetarchives.gap> <gap-daa7c2458b-p11@usenetarchives.gap>`

```

Jerry Peacock wrote:
› 
› Renegade wrote in message <350··.@new··x.com>...
…[19 more quoted lines elided]…
››› if you can read that, you are a real programmer.


Would ya'll get into the 80's.....cout is cool, and available on every
compiler I've ever seen:

#include
#include

float dlrVal = whatever;

int dgtMax = 10^'whatever max col width you desire' - 3; // e.g. num
dgts left + a decimal + 2 cent dgts
for ( int dgtCnt = 0;
(int)dlrVal / dgtMax--; // true when the number will fit
dgtCnt++ );

cout << ios::fixed
<< ios::setWidth( dlrCnt )
<< ios::setFill( '$')
<< dlrVal;

Actually, there is an easier way to do the digit count, as standard lib
function I think, but, being in a COBOL shop, all my C references are at
home....but it could be:

#include
#include

float dlrVal = whatever;
cout << ios::fixed
<< ios::setWidth( someStdLibDgtCntFunc(dlrCnt) )
<< ios::setFill( '$')
<< dlrVal;

that looks quite easy to understand to me.....further, many (but I'm not
sure if it is part of the standard) support an io manipulator of

ios::currancy or ios::setBase( ios::currancy ) makeing life even
easier.....
```

###### ↳ ↳ ↳ Re: General Info

_(reply depth: 4)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-03-14T19:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daa7c2458b-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daa7c2458b-p4@usenetarchives.gap>`
- **References:** `<19980312030600.WAA06952@ladder02.news.aol.com> <gap-daa7c2458b-p2@usenetarchives.gap> <gap-daa7c2458b-p3@usenetarchives.gap> <gap-daa7c2458b-p4@usenetarchives.gap>`

```



G Moore wrote:

› On Thu, 12 Mar 1998 21:41:22 -0600, "Jerry Peacock"
›  wrote:
…[14 more quoted lines elided]…
› if you can read that, you are a real programmer.

Well, as long as we're on the topic, how's about:

Loc Object Code Addr1 Addr2 Stmt Source Statement
000084 D209 3176 316C 00176 0016C 46 MVC F1,PAT
00008A 4110 317D 0017D 47 LA R1,F1+7
00008E DF09 3176 3158 00176 00158 48 EDMK F1,P1
000094 0610 49 BCTR R1,0

000096 925B 1000 00000 50 MVI
0(R1),C'$'
00009A D209 3196 316C 00196 0016C 52 MVC F2,PAT
0000A0 4110 319D 0019D 53 LA R1,F2+7
0000A4 DF09 3196 315C 00196 0015C 54 EDMK F2,P2
0000AA 0610 55 BCTR R1,0
0000AC 925B 1000 00000 56 MVI 0(R1),C'$'
0000B0 D209 31B6 316C 001B6 0016C 58 MVC F3,PAT
0000B6 4110 31BD 001BD 59 LA R1,F3+7
0000BA DF09 31B6 3160 001B6 00160 60 EDMK F3,P3
0000C0 0610 61 BCTR
R1,0
0000C2 925B 1000 00000 62 MVI
0(R1),C'$'
0000C6 D209 31D6 316C 001D6 0016C 64 MVC F4,PAT
0000CC 4110 31DD 001DD 65 LA R1,F4+7
0000D0 DF09 31D6 3164 001D6 00164 66 EDMK F4,P4
0000D6 0610 67 BCTR R1,0

0000D8 925B 1000 00000 68 MVI 0(R1),C'$'

0000DC D209 31F6 316C 001F6 0016C 70 MVC F5,PAT
0000E2 4110 31FD 001FD 71 LA R1,F5+7
0000E6 DF09 31F6 3168 001F6 00168 72 EDMK F5,P5
0000EC 0610 73 BCTR R1,0

0000EE 925B 1000 00000 74 MVI 0(R1),C'$'

which produces (in hex dump format):

15080000 19980315 00000000 0000010C 0000210C
...........h.....q..............
4020206B 2020214B 20204040 40404040 5B4BF1F0 ............
..,...... $.10
40404040 40404040 40404040 4040405B F24BF1F0
$2.10
40404040 40404040 40404040 40405BF1 F24BF1F0
$12.10
40404040 40404040 40404040 405BF3F2 F14BF1F0
$321.10
40404040 40404040 4040405B F46BF3F2 F14BF1F0
$4,321.10

Each "LA R1,..." thru the "MVI 0(R1),C'$'" processes one field. Some
(many?) of us have seen similar stuff in dumps past & present.

Bill Lynch
:-)

›
›
› gvw··.@ix.··m.com remove the spam
```

###### ↳ ↳ ↳ Re: General Info

- **From:** "warren g. simmons" <ua-author-6589103@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daa7c2458b-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daa7c2458b-p3@usenetarchives.gap>`
- **References:** `<19980312030600.WAA06952@ladder02.news.aol.com> <gap-daa7c2458b-p2@usenetarchives.gap> <gap-daa7c2458b-p3@usenetarchives.gap>`

```

Jerry Peacock wrote:
› 
› Jim Rivera wrote in 
…[3 more quoted lines elided]…
› the direction of the Department of Defense.

History takes many forms. The above statement is almost correct.

My version:

Several interested parties (mostly users of all varieties) formed the
Conference on Data System Languages. Committees were not popular at the
time. I can name most of the people who made up the Executive Committee
of the Conference. They reasoned that to succeed in their effort to
create a higher level and standard programming language for the user's
applications, they would need some big guns. Already on their side were
parts of the Navy and Airforce, and Army, several large manufactures,
insurance companies, oil companies, and the Dept. of Commerce. They
approached The Comptroller of the Department of Defense with their idea,
and recruited him to be their chairman. It was his ability to add a
sentence to the yearly contract that the government required that
eventually read something like this: "Will ..........(the vendor's name)
provide a COBOL Compiler?"
Following that question, all renewals were deferred until that question
was answered. Meanwhile, the DOD asked the DOJ to review the rules for
vendors meeting together to accomplish something. In the USA standards
had to be made and submitted, not dictated as in some other countries.
With the clarification of that, it was agreed that if vendors and users
cooperated in a committee to develop a standard, and submitted the
result to ANS, it would be legal. So DOD had a very large role in the
success of the project, but it was the drive of the USERS who brought
this about.

While not as short and sweet as the original answer, more clearly
reveals the nature and difficulty of the effort from my view. It was
more than a year later before the COBOL Committee of CODASYL delived
their first spec.

Warren Simmons
›
› There exists a spectr
```

##### ↳ ↳ Re: General Info

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daa7c2458b-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daa7c2458b-p2@usenetarchives.gap>`
- **References:** `<19980312030600.WAA06952@ladder02.news.aol.com> <gap-daa7c2458b-p2@usenetarchives.gap>`

```

Jim Rivera wrote:

› COBOL is sometimes used for things it shouldn't do. So is C. There are some
› business systems in C but it's not the best use of the language -
› something like putting a race horse in fromt of a plow.

Or putting a plow horse in front of a raceing car?

Cobol is the Frog
```

#### ↳ Re: General Info

- **From:** "gvwm..." <ua-author-47960@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daa7c2458b-p17@usenetarchives.gap>`
- **In-Reply-To:** `<19980312030600.WAA06952@ladder02.news.aol.com>`
- **References:** `<19980312030600.WAA06952@ladder02.news.aol.com>`

```

On 12 Mar 1998 03:06:35 GMT, lok··.@a··.com (Lok1220) wrote:

› I have a couple of questions that hopefull someone can answer.  First of all,
› what is the difference between Cobol and C?  Also, is Cobol a broad based
› language (in the sense that it is used for many types of applications) or is it
› used generally in a business or other environment.  No, I'm not a student
› trying to do some homework.  Thanks for any responses in advance.

apples and oranges. cobol is mainly a business language, yes,
but it connects to other systems machines.



gvw··.@ix.··m.com remove the spam
```

#### ↳ Re: General Info

- **From:** "scott mckellar" <ua-author-13531501@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daa7c2458b-p18@usenetarchives.gap>`
- **In-Reply-To:** `<19980312030600.WAA06952@ladder02.news.aol.com>`
- **References:** `<19980312030600.WAA06952@ladder02.news.aol.com>`

```

Lok1220 wrote:
›
› I have a couple of questions that hopefull someone can answer. First of all,
› what is the difference between Cobol and C?

COBOL and C are about as different as two procedural languages can
be. You might as well ask about the differences between MVS and
UNIX, or English and Japanese.

› Also, is Cobol a broad based
› language (in the sense that it is used for many types of applications) or is it
› used generally in a business or other environment.

Yes and yes, in that order.

COBOL is most typically used for business applications because of its
readable, English-like syntax (so that the accountants can look over
your shoulder), its support for scaled decimal arithmetic, its
built-in support for sorts and indexed files, and the ease with
which it processes fixed-field file formats.

Most COBOL applications are custom-built for particular enterprises.
You won't see many shrink-wrapped packages written in COBOL, apart
from accounting, payroll, banking, or similar applications for
mainframes and minis.

On the other hand, there is very little that you can do in C that
you can't do in COBOL (depending somewhat on the dialect), and vice
versa. You may have to exercise some ingenuity. Some tasks are a
better fit for one language and others for the other. C can be
somewhat clumsy for business applications, but it is well suited for
systems programming, text parsing, and the implementation of complex
algorithms and data structures.

Michael C. Kasten mc··.@swb··l.net
http://home.swbell.net/mck9/cobol/cobol.html
```

#### ↳ Re: General Info

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-03-11T19:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daa7c2458b-p19@usenetarchives.gap>`
- **In-Reply-To:** `<19980312030600.WAA06952@ladder02.news.aol.com>`
- **References:** `<19980312030600.WAA06952@ladder02.news.aol.com>`

```

In article <199··.@lad··l.com>,
Lok1220 wrote:
› I have a couple of questions that hopefull someone can answer.  First of all,
› what is the difference between Cobol and C?
 
› About four letters.
 
› Also, is Cobol a broad based
› language (in the sense that it is used for many types of applications) or is it
› used generally in a business or other environment.

Well it *used* to be broad-based... but then it followed the advice of
Tommy LaSorda and went on the Slim-Fast Diet (tm)... and now it is
pleasingly svelte.

› No, I'm not a student
› trying to do some homework. Thanks for any responses in advance.


My pleasure.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
