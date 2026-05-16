[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol Program (URGENT and IMPORTANT)

_31 messages · 13 participants · 2003-02 → 2003-05_

---

### Cobol Program (URGENT and IMPORTANT)

- **From:** yusufjee <member25738@dbforums.com>
- **Date:** 2003-02-28T05:11:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2586396.1046409100@dbforums.com>`

```

Is there someone who can write a program for me in COBOL that will
calculate the area of TRIANGLE, area of RECTANGLE and area of CIRCLE. I
know its too much of asking but i need it, Please help me.
```

#### ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** mfcobol2002 <marcos_as@terra.com.br>
- **Date:** 2003-02-28T10:43:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2587350.1046429029@dbforums.com>`
- **References:** `<2586396.1046409100@dbforums.com>`

```

Microfocus Cobol:Netexpress

ACOS function
ASIN function
ATAN function
COS function
SIN function
TAN function
---------------------------

Sample:

The PI function returns a value that is an approximation of p, the ratio
of the circumference of a circle to its diameter. The type of this
function is numeric.

General Format

FUNCTION PI

Returned Values

1.      The returned value is:

3.141592653589793238

----------------------
The SIN function returns a numeric value that approximates the sine of
an angle or arc, expressed in radians, that is specified by argument-1.
The type of this function is numeric.

General Format

FUNCTION SIN (argument-1)

Arguments

1.      Argument-1 must be class numeric.
        See Trigonometric Functions for conversion factors from degrees
        and Gon (grad) to radians.

Returned Values

1.      The returned value is the approximation of the sine of
        argument-1 and is greater than or equal to �1 and less than or
        equal to +1.
2.      Floating-point format is used for numeric non-integer results.


----------------------------

Trigonometric Functions

Trigonometry deals with the relationships among the sides of a triangle
and its angles. An angle can be measured in degrees, radians or Gon
(grad). Since a computer usually generates trigonometric values by
series approximation, the angle is specified in radians when used as the
argument to the SIN, COS, and TAN functions or as the returned value
from the ASIN,ACOS, and ATAN functions.
A radian is an arc of a circle whose length is equal to the circle's
radius. Since the relationship between a circle's radius and
circumference is

C =2x P x r
and there are 360 degress in a circle, we can derive from
360 = 2 x P x r
that the values for conversion are:
1 radian = 180/ P = 57.295780 degrees
1 degree = P /180 = 0.01745329 radians.
Another scale that is sometimes used to measure angles is Gon, also
known as grad.  The values for conversion are:
1 radian = 200/ P = 63.661977 Gon (grad)
1 Gon (grad) = P /200 = 0.01570796 radians=94

Marcos A.S
Brasil
```

#### ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** docdwarf@panix.com
- **Date:** 2003-02-28T05:45:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3nekm$q77$1@panix1.panix.com>`
- **References:** `<2586396.1046409100@dbforums.com>`

```
In article <2586396.1046409100@dbforums.com>,
yusufjee  <member25738@dbforums.com> wrote:
>
>Is there someone who can write a program for me in COBOL that will
>calculate the area of TRIANGLE, area of RECTANGLE and area of CIRCLE. I
>know its too much of asking but i need it, Please help me.

Please do your own homework.

DD
```

##### ↳ ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2003-02-28T16:16:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E5F8B4C.70707@optonline.NOSPAM.net>`
- **References:** `<2586396.1046409100@dbforums.com> <b3nekm$q77$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <2586396.1046409100@dbforums.com>,
> yusufjee  <member25738@dbforums.com> wrote:
…[5 more quoted lines elided]…
> Please do your own homework.

Really. At least this guy was up front in asking us to do his homework  ;)

OP must have cut all his classes, how hard is it to calc the area of a 
rectangle, anyway?
```

###### ↳ ↳ ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** docdwarf@panix.com
- **Date:** 2003-02-28T11:35:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3o34h$m7u$1@panix1.panix.com>`
- **References:** `<2586396.1046409100@dbforums.com> <b3nekm$q77$1@panix1.panix.com> <3E5F8B4C.70707@optonline.NOSPAM.net>`

```
In article <3E5F8B4C.70707@optonline.NOSPAM.net>,
Liam Devlin  <LiamD@optonline.NOSPAM.net> wrote:
>docdwarf@panix.com wrote:
>> In article <2586396.1046409100@dbforums.com>,
…[11 more quoted lines elided]…
>rectangle, anyway?

Now, now... he may have an old compiler that has difficulties dealing with 
fractional exponents.

DD
```

###### ↳ ↳ ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-02-28T18:41:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c3O7a.31$3g.20936@newssrv26.news.prodigy.com>`
- **References:** `<2586396.1046409100@dbforums.com> <b3nekm$q77$1@panix1.panix.com> <3E5F8B4C.70707@optonline.NOSPAM.net>`

```
"Liam Devlin" <LiamD@optonline.NOSPAM.net> wrote in message
news:3E5F8B4C.70707@optonline.NOSPAM.net...
> OP must have cut all his classes, how hard is it to calc the area of a
> rectangle, anyway?

I always had problems with those five-sided rectangles.

MCM
```

###### ↳ ↳ ↳ Re: Cobol Program (URGENT and IMPORTANT)

_(reply depth: 4)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2003-03-02T17:53:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E624534.60309@optonline.NOSPAM.net>`
- **References:** `<2586396.1046409100@dbforums.com> <b3nekm$q77$1@panix1.panix.com> <3E5F8B4C.70707@optonline.NOSPAM.net> <c3O7a.31$3g.20936@newssrv26.news.prodigy.com>`

```
Michael Mattias wrote:
> "Liam Devlin" <LiamD@optonline.NOSPAM.net> wrote in message
> news:3E5F8B4C.70707@optonline.NOSPAM.net...
…[4 more quoted lines elided]…
> I always had problems with those five-sided rectangles.

Didn't we all.
```

#### ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** yusufjee <member25738@dbforums.com>
- **Date:** 2003-02-28T11:46:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2587435.1046432801@dbforums.com>`
- **References:** `<2586396.1046409100@dbforums.com>`

```

Thanks for reply mfccobol but that wasnt wat i wanted. And for dwarf,
sorry buddy, dont mean to offend anyone but i m just crap to do it.
```

##### ↳ ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** docdwarf@panix.com
- **Date:** 2003-02-28T08:45:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3np5l$svh$1@panix1.panix.com>`
- **References:** `<2586396.1046409100@dbforums.com> <2587435.1046432801@dbforums.com>`

```
In article <2587435.1046432801@dbforums.com>,
yusufjee  <member25738@dbforums.com> wrote:
>
>Thanks for reply mfccobol but that wasnt wat i wanted. And for dwarf,
>sorry buddy, dont mean to offend anyone but i m just crap to do it.

No offense taken... now please do your own homework.

DD
```

##### ↳ ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-28T15:04:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3ntpn$otr$1@peabody.colorado.edu>`
- **References:** `<2586396.1046409100@dbforums.com> <2587435.1046432801@dbforums.com>`

```

On 28-Feb-2003, yusufjee <member25738@dbforums.com> wrote:

> Thanks for reply mfccobol but that wasn't wat i wanted. And for dwarf,
> sorry buddy, dont mean to offend anyone but i m just crap to do it.

You're just crap to do it?

That's an interesting expression - is it common, or is it an expression that
only applies to you?
```

#### ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-02-28T14:12:43+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pgku5v8489lcmujf91tdgkjerirecvtqf7@4ax.com>`
- **References:** `<2586396.1046409100@dbforums.com>`

```
On Fri, 28 Feb 2003 05:11:40 +0000 yusufjee <member25738@dbforums.com> wrote:

:>Is there someone who can write a program for me in COBOL that will
:>calculate the area of TRIANGLE, area of RECTANGLE and area of CIRCLE. I
:>know its too much of asking but i need it, Please help me.

How would you do it in another language?

Why would you choose COBOL for this?
```

#### ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-02-28T12:37:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aKI7a.2152$rM4.438058@newssrv26.news.prodigy.com>`
- **References:** `<2586396.1046409100@dbforums.com>`

```
"yusufjee" <member25738@dbforums.com> wrote in message
news:2586396.1046409100@dbforums.com...
>
> Is there someone who can write a program for me in COBOL that will
> calculate the area of TRIANGLE, area of RECTANGLE and area of CIRCLE. I
> know its too much of asking but i need it, Please help me.

I'll bet you are wishing you had paid better attention in *both* geometry
and programming class, huh?

MCM
```

#### ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-28T15:03:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3ntn6$otk$1@peabody.colorado.edu>`
- **References:** `<2586396.1046409100@dbforums.com>`

```

On 27-Feb-2003, yusufjee <member25738@dbforums.com> wrote:

> Is there someone who can write a program for me in COBOL that will
> calculate the area of TRIANGLE, area of RECTANGLE and area of CIRCLE. I
> know its too much of asking but i need it, Please help me.

Actually, all of us can do this.

Please tell us what your environment is, list the code that you have tried, and
explain what problems you have had, and we will be glad to help you.


The operative request above was "Please help me.".


Of course, if you had said "Please do my homework", our response would be
different.  Obviously we have our profession to protect and don't want people
hired under the pretense that they learned something in school.   But you didn't
ask that, so you wouldn't mind showing us exactly where you are having
difficulty.
```

#### ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** yusufjee <member25738@dbforums.com>
- **Date:** 2003-02-28T16:26:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2588315.1046449599@dbforums.com>`
- **References:** `<2586396.1046409100@dbforums.com>`

```

leave me alone just asking for help
```

##### ↳ ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** docdwarf@panix.com
- **Date:** 2003-02-28T21:19:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3p5b0$2h4$1@panix1.panix.com>`
- **References:** `<2586396.1046409100@dbforums.com> <2588315.1046449599@dbforums.com>`

```
In article <2588315.1046449599@dbforums.com>,
yusufjee  <member25738@dbforums.com> wrote:
>
>leave me alone just asking for help

Now that's just silly... helping someone is, quite often, done by *not* 
leaving them alone.

Oh... and please do your own homework.

DD
```

#### ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-02-28T20:58:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c2df6c$17e152e0$328bf243@chottel>`
- **References:** `<2586396.1046409100@dbforums.com>`

```
Look up the COMPUTE statment.  With the right variables defined you should
be able to do it with three COMPUTEs.

yusufjee <member25738@dbforums.com> wrote in article
<2586396.1046409100@dbforums.com>...
> 
> Is there someone who can write a program for me in COBOL that will
…[5 more quoted lines elided]…
>
```

#### ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** yusufjee <member25738@dbforums.com>
- **Date:** 2003-03-01T06:06:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2591142.1046498777@dbforums.com>`
- **References:** `<2586396.1046409100@dbforums.com>`

```

IDENTIFICATION DIVISION.
PROGRAM-ID. Compute.

*===========================================
* This program computes the area of circle
* area of  rectangle
* and the area of triangle
*===========================================

ENVIRONMENT DIVISION.

DATA DIVISION.

WORKING STORAGE SECTION.

01 T-OR-C-OR-A PIC X.
01 CALCULATE-CIRCLE PIC 9(5)V99.
        03 CIRCLE PIC 9(5)V99.
        03 RADIUS PIC 9(5)V99.

01 CALCULATE-RECTANGLE PIC 9(5)V99.
        03 HEIGHT PIC 9(5)V99.
        03 WIDTH PIC 9(5)V99.

01 CALCULATE-TRIANGLE 9(5)V99.
        03 BASE PIC 9(5)V99.

01 REPEAT-OR-EXIT PIC X.


PROCEDURE DIVISION.

PROGRAM-BEGIN.


    PERFORM DISPLAY-MSG.
    PERFORM T-OR-C-OR-A
    PERFORM CALCULATE-CIRCLE.
    PERFORM CALCULATE-RECTANGLE.
    PERFORM CALCULATE-TRIANGLE.
    PERFORM REPEAT-OR-EXIT.

PROGRAM DONE.

    STOP RUN.

DISPLAY-MSG.
    "THIS PROGRAM COMPUTES THE AREA OF CIRCLE, RECTANGLE AND TRIANGLE.".

T-OR-C-OR-A.

    DISPLAY "TYPE T FOR TRIANGLE OR C FOR CIRCLE OR A FOR RECTANGLE".
    ACCEPT T-OR-C-OR-A.
    IF T-OR-C-OR-A = "T" OR T-OR-C-OR-A = "t"
        PERFORM CALCULATE-TRIANGLE
    ELSE IF T-OR-C-OR-A = "C" OR T-OR-C-OR-A = "c"
        PERFORM CALCULATE-CIRCLE
    ELSE IF T-OR-C-OR-A = "A" OR T-OR-C-OR-A = "a"
        PERFORM CALCULATE-RECTANGLE
    ELSE
        PERFORM PROGRAM-BEGIN.

CALCULATE-CIRCLE.

* PERFORMS CALCULATION OF THE CIRCLE BY GIVEN VALUES

    DISPLAY "ENTER THE RADIUS TO CALCULATE".
    ACCEPT RADIUS.

* THE FORMULA TO COMPUTE CIRCLE
    COMPUTE CIRCLE = pi * RADIUS ** 2.

DISPLAY-CIRCLE.

    DISPLAY "THE AREA OF CIRCLE IS: " CIRCLE.

CALCULATE-RECTANGLE.

* PERFORMS CALCULATION OF THE RECTANGLE BY GIVEN VALUES *

    DISPLAY "ENTER THE WIDTH".
    ACCEPT WIDTH.
    DISPLAY "ENTER THE HEIGHT".
    ACCEPT HEIGHT.

* FORMULA TO COMPUTE RECTANGLE

    COMPUTE RECTANGLE = WIDTH * HEIGHT.

DISPLAY-RECTANGLE.

    DISPLAY "THE AREA OF RECTANGLE IS: " RECTANGLE.

CALCULATE-TRIANGLE.

* PERFORMS CALCULATION OF THE TRIANGLE BY GIVEN VALUES *

    DISPLAY "ENTER THE BASE".
    ACCEPT BASE.
    DISPLAY "ENTER HEIGHT".
    ACCEPT HEIGHT.

* FORMULA TO CALCULATE TRIANGLE

    COMPUTE TRIANGLE = 1/2 * BASE * HEIGHT.

DISPLAY-TRIANGLE.

    DISPLAY "THE AREA OF TRIANGLE: " TRIANGLE.

REPEAT-OR-EXIT.

    DISPLAY "TYPE R TO REPEAT OR E TO EXIT".
    ACCEPT REPEAT-EXIT.
    IF REPEAT-EXIT = "R" OR REPEAT-EXIT = "r"
        PERFORM PROGRAM-BEGIN
    ELSE
        PERFORM PROGRAM-DONE.



so wats wrong.
```

##### ↳ ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** docdwarf@panix.com
- **Date:** 2003-03-01T06:59:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3q7bl$n7n$1@panix1.panix.com>`
- **References:** `<2586396.1046409100@dbforums.com> <2591142.1046498777@dbforums.com>`

```
In article <2591142.1046498777@dbforums.com>,
yusufjee  <member25738@dbforums.com> wrote:
>
>IDENTIFICATION DIVISION.

[snip]

>
>so wats wrong.

What's wrong is that the book gives you only a skeleton and then *you* 
have to code the rest.

Now please do your own homework.

DD
```

##### ↳ ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-03-01T13:36:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A5F05EA6F93A73CE.1146548F2B58B671.ADAC52AAE92A63AB@lp.airnews.net>`
- **References:** `<2586396.1046409100@dbforums.com> <2591142.1046498777@dbforums.com>`

```
On Sat, 01 Mar 2003 06:06:17 +0000, yusufjee
<member25738@dbforums.com> enlightened us:

>
>IDENTIFICATION DIVISION.
…[120 more quoted lines elided]…
>so wats wrong.

You are missing variables that need to be defined in WS.  Maybe if you
compiled this obvious skeleton code you'd have known that.  If you
want help with your homework in this news group, you need to show that
you've put forth more effort than copy and paste.
Regards,

          ////
         (o o)
-oOO--(_)--OOo-

"Going to war without France is like going deer hunting 
without your accordian."  - Donald Rumsfeld / US Secretary of Defense
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

##### ↳ ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-01T23:28:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e614140.5229466@news.optonline.net>`
- **References:** `<2586396.1046409100@dbforums.com> <2591142.1046498777@dbforums.com>`

```
yusufjee <member25738@dbforums.com> wrote:

>so wats wrong

I'll limit these comments to errors which will not be caught by the compiler. 


>    PERFORM CALCULATE-CIRCLE.
>    PERFORM CALCULATE-RECTANGLE.
>    PERFORM CALCULATE-TRIANGLE.

These are performed from T-OR-C-OR-A. They do not belong here.

>T-OR-C-OR-A.
> ...
>    ELSE
>        PERFORM PROGRAM-BEGIN.

This, and the one at the end, are recursive performs. At the top you need
"perform until repeat-exit not equal to 'R'' and 'r' "

>    COMPUTE CIRCLE = pi * RADIUS ** 2.

When doing two different operations, it is best to use parentheses, especially
if you are a beginner: pi * (Radius ** 2). Alternatively: pi * Radius * Radius.
In this case, it will work as expected. Next time you might not be as lucky.

>DISPLAY-CIRCLE.
>
>    DISPLAY "THE AREA OF CIRCLE IS: " CIRCLE.

You did not perform this paragraph. Just remove the paragraph name.

>    COMPUTE TRIANGLE = 1/2 * BASE * HEIGHT.

The more normal form is: (BASE * HEIGHT) / 2. 

>    DISPLAY "TYPE R TO REPEAT OR E TO EXIT".
>    ACCEPT REPEAT-EXIT.
…[3 more quoted lines elided]…
>        PERFORM PROGRAM-DONE.

See above, then delete the IF.

Put decision-making at the top of your structure and mundane tasks at the
bottom. Your structure is inverted (upside-down). 

Robert
```

##### ↳ ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2003-03-03T01:46:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Lty8a.46166$Tz6.2057411@twister.austin.rr.com>`
- **References:** `<2586396.1046409100@dbforums.com> <2591142.1046498777@dbforums.com>`

```
For some reason, I find myself believing that you are just trying to get some help. You do realize, of course, that this is one of
the most common programs assigned in schools/classes that teach COBOL, so most people are going to look at this
and say riiiighhhhttttt.....

I think it is the errors that convince me you probably did do this yourself. So I will offer a little bit of help to see where it
takes you. You should be able to get this to the point where the compiler will tell you what is wrong with it.

"yusufjee" <member25738@dbforums.com> wrote in message news:2591142.1046498777@dbforums.com...
>
> IDENTIFICATION DIVISION.
> PROGRAM-ID. Compute.
                                           ^--- Problem number one. COMPUTE is a reserved word. Pick another name for the
                                                   program. For example, PROG1 or something equally boring.

>
> *===========================================
…[11 more quoted lines elided]…
> 01 T-OR-C-OR-A PIC X.
             ^---- You have this defined as both a data item and a paragraph name.
                       Change one of them to a better name. For example, this one might be better named
                        WS-USER-CHOICE or something like that.

> 01 CALCULATE-CIRCLE PIC 9(5)V99.
>         03 CIRCLE PIC 9(5)V99.
>         03 RADIUS PIC 9(5)V99.
>
            ^--- You missed something here. What you got is not what your indenting says you intended to get.
                    Also, that naming this is going on here again. This is data, not executable code.
                    You might have meant something like this:

                    01 CIRCLE-DATA.
                         01 CIRCLE-RADIUS                      PIC 9(5)V9(2).
                         01 CIRCLE-AREA                          PIC 9(5)V99.

            Do you see the difference? If not, figure out how many bytes of storage you will use in your original,
            and how many I would use in the same above.

> 01 CALCULATE-RECTANGLE PIC 9(5)V99.
>         03 HEIGHT PIC 9(5)V99.
…[102 more quoted lines elided]…
> Posted via http://dbforums.com
```

##### ↳ ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-03T15:14:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3vrgg$15u$1@peabody.colorado.edu>`
- **References:** `<2586396.1046409100@dbforums.com> <2591142.1046498777@dbforums.com>`

```
Is there a compiler that has defined variables such as pi?


What compiler and environment were you using?   What were your errors?  What did
you think the errors meant?

Sometimes compiler listings aren't very clear when they list compiler errors.  
We would be glad to clarify them.

Sometimes run-time listings aren't very clear when they list run-time errors.  
We will be glad to clarify them.

Sometimes, you just get results that don't make sense.  We will help you
determine where your mistakes are - but it doesn't appear that you are near this
far by looking at the code.
```

###### ↳ ↳ ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-03-03T17:52:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hDM8a.3616$3g.530880@newssrv26.news.prodigy.com>`
- **References:** `<2586396.1046409100@dbforums.com> <2591142.1046498777@dbforums.com> <b3vrgg$15u$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message
news:b3vrgg$15u$1@peabody.colorado.edu...
> Is there a compiler that has defined variables such as pi?


05 WS-PI   USAGE COMP-1 VALUE IS    +3 AND SOME CHANGE.

MCM
```

#### ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** yusufjee <member25738@dbforums.com>
- **Date:** 2003-03-02T14:31:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2594191.1046615474@dbforums.com>`
- **References:** `<2586396.1046409100@dbforums.com>`

```

what the hell is wrong with u people. I m not copying and pasting
anything. This is what i have done myself. If u dont want to answer
dont but please dont say i this is not my work cuz it is mine. And by
the way if i had tp copy and paste, i would have never came to the
forum for help :(
```

##### ↳ ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-03T15:22:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3vrv9$1fr$1@peabody.colorado.edu>`
- **References:** `<2586396.1046409100@dbforums.com> <2594191.1046615474@dbforums.com>`

```

On  2-Mar-2003, yusufjee <member25738@dbforums.com> wrote:

> what the hell is wrong with u people. I m not copying and pasting
> anything. This is what i have done myself. If u dont want to answer
> dont but please dont say i this is not my work cuz it is mine. And by
> the way if i had tp copy and paste, i would have never came to the
> forum for help :(

It's probably best to be polite, and also edit your messages when you are asking
for help.   The more it looks as though you are working hard, and appreciate a
bit of help, the more likely it will be for you to get that help.

We are trying to get you to perform the same kind of debugging that we do
ourselves - that is the way to learn.  That's why we have asked for you to tell
us what error messages you have been getting, and what you have tried to do to
resolve them.    We also need to know your compiler and its environment, as they
sometimes change some factors.

BTW, it is obvious that your code wasn't copied from a textbook example.
```

#### ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** yusufjee <member25738@dbforums.com>
- **Date:** 2003-03-02T14:32:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2594192.1046615566@dbforums.com>`
- **References:** `<2586396.1046409100@dbforums.com>`

```

and thanks to rpbert :)
```

#### ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** yusufjee <member25738@dbforums.com>
- **Date:** 2003-03-03T18:15:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2598094.1046715339@dbforums.com>`
- **References:** `<2586396.1046409100@dbforums.com>`

```

Thanks to all of u as the program is solved now. Special thanks to Paul
Raulerson for making me realize my silly mistakes, which i guess all the
beginners do.

Thanks again :)
```

##### ↳ ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2003-03-04T02:19:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C2U8a.63375$O41.2357960@twister.austin.rr.com>`
- **References:** `<2586396.1046409100@dbforums.com> <2598094.1046715339@dbforums.com>`

```
You are welcome from all us, including me, who made a typo in the example I commented for you.
I messed up the levels in the Data Section example.

-Paul

"yusufjee" <member25738@dbforums.com> wrote in message news:2598094.1046715339@dbforums.com...
>
> Thanks to all of u as the program is solved now. Special thanks to Paul
…[6 more quoted lines elided]…
> Posted via http://dbforums.com
```

#### ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** weberm@polaris.net (Ubiquitous)
- **Date:** 2003-05-10T22:03:27-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yLqdnZe4PubiICCjXTWcoQ@comcast.com>`
- **References:** `<2586396.1046409100@dbforums.com>`

```
In article <2586396.1046409100@dbforums.com>, member25738@dbforums.com 
wrote:

>Is there someone who can write a program for me in COBOL that will
>calculate the area of TRIANGLE, area of RECTANGLE and area of CIRCLE. I
>know its too much of asking but i need it, Please help me.

Do your own homework.
```

##### ↳ ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-05-11T10:27:51+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tpurbv05a1545d8d8nd6p2k7d1r6b02dm1@4ax.com>`
- **References:** `<2586396.1046409100@dbforums.com> <yLqdnZe4PubiICCjXTWcoQ@comcast.com>`

```
On Sat, 10 May 2003 22:03:27 -0500 weberm@polaris.net (Ubiquitous) wrote:

:>In article <2586396.1046409100@dbforums.com>, member25738@dbforums.com 
:>wrote:

:>>Is there someone who can write a program for me in COBOL that will
:>>calculate the area of TRIANGLE, area of RECTANGLE and area of CIRCLE. I
:>>know its too much of asking but i need it, Please help me.

:>Do your own homework.

Why didn't you simply answer his question?

"Yes, there are people who can write this program".

How hard was that?
```

##### ↳ ↳ Re: Cobol Program (URGENT and IMPORTANT)

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-11T09:29:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EBE5E4F.4040507@Knology.net>`
- **References:** `<2586396.1046409100@dbforums.com> <yLqdnZe4PubiICCjXTWcoQ@comcast.com>`

```
member425738@dbforums.com wrote:
>Is there someone who can write a program for me in COBOL that will
>calculate the area of TRIANGLE, area of RECTANGLE and area of CIRCLE. I
>know its too much of asking but i need it, Please help me.

Yes, there is.  However, you don't learn if someone here does it.  You 
should be able to find a "shell" of a COBOL program (with the four 
divisions) in a textbook, the language reference manual of the compiler, 
even online.

To do what you need, you'll need to define picture clauses for your 
variables.  You'll also probably want to make them bigger than your 
biggest final expected value, as many of the math verbs calculate 
"intermediate values" that can be larger than the final value.

In the procedure division, check out the ACCEPT verb to ask the user 
whether they want a triangle, rectangle, or circle, and to prompt them 
for the dimensions of what they've selected.  Then, check out the ADD, 
SUBTRACT, MULTIPLY, DIVIDE, and COMPUTE verbs for actually doing the 
calculations.  Again, you should be able to find these in a textbook or 
language reference manual.  If you have neither, here's a link to a 
COBOL language reference manual (it's the one we use at work)...

http://public.support.unisys.com/2200/docs/ix80/PDF/78310448-002.PDF

(You'll have to define PI manually, unless you've got a COBOL 
2002-compliant compiler.  The rules for picture clauses should describe 
how to do decimal numbers.)

Once you get something put together, you'll find folks here more than 
willing to help you learn - but, we like to see that the person asking 
for help has expended a bit of effort on learning it themselves first.

Good luck...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
