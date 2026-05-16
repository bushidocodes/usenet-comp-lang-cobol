[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# mod equivalent in cobol

_40 messages · 19 participants · 1999-01 → 1999-02_

---

### mod equivalent in cobol

- **From:** "���" <no@spam.com>
- **Date:** 1999-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j4Tp2.1911$PD.11130759@news.magma.ca>`

```
Hi, i'm trying to calculate leap years and need to know the " mod "
equivalent in COBOL for the remainder.  Any help would be greatly
appreciated ;)

Steve
```

#### ↳ Re: mod equivalent in cobol

- **From:** pduboisREMOVETHIS@enteract.com (PAL3000)
- **Date:** 1999-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36a833c7.10004769@news.enteract.com>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca>`

```
I use a redefines.  SOmething like.

01 DIV-RESULT          PIC 9(9)V9999.
01 DIV-RED REDEFINES DEV-RESULT.
      03 DIV-WHOLE      PIC 9(9).
      03 DIV-DEV             PIC V9999.


Then in your code:

    COMPUTE DIV-RESULT = SOME-YR / 4.
    IF DIV-DEC NOT = ZERO
   etx
etc

On Fri, 22 Jan 1999 04:24:47 GMT, "ï¿½" <no@spam.com> wrote:

>Hi, i'm trying to calculate leap years and need to know the " mod "
>equivalent in COBOL for the remainder.  Any help would be greatly
…[3 more quoted lines elided]…
>

--------------------------------------
To reply by email, please take out the
words REMOVETHIS from my email address
```

#### ↳ Re: mod equivalent in cobol

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36a82258.544306@netnews>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca>`

```
'Twas Fri, 22 Jan 1999 04:24:47 GMT, when "�" <no@spam.com> illuminated
comp.lang.cobol thusly:

>Hi, i'm trying to calculate leap years and need to know the " mod "
>equivalent in COBOL for the remainder.  Any help would be greatly
>appreciated ;)

COMPUTE REMAINDER = FUNCTION MOD (YYYY, 4)
```

##### ↳ ↳ Re: mod equivalent in cobol

- **From:** dxmixxer@netdirect.net (Doug Miller)
- **Date:** 1999-01-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78fi8d$178_003@news.netdirect.net>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <36a82258.544306@netnews>`

```
In article <36a82258.544306@netnews>,
   Barticus@att.spam.net (Randall Bart) wrote:
+'Twas Fri, 22 Jan 1999 04:24:47 GMT, when "�" <no@spam.com> illuminated
+comp.lang.cobol thusly:
+
+>Hi, i'm trying to calculate leap years and need to know the " mod "
+>equivalent in COBOL for the remainder.  Any help would be greatly
+>appreciated ;)
+
+COMPUTE REMAINDER = FUNCTION MOD (YYYY, 4)
+
Close, but no cigar. "REMAINDER" is a reserved word, and this won't
compile. Besides, older compilers don't support intrinsic functions. 
This should work on any compiler:

DIVIDE 4 INTO yyyy GIVING xyz REMAINDER re-mainder.
```

#### ↳ Re: mod equivalent in cobol

- **From:** "Mark Undrill" <marku@affirm.co.uk>
- **Date:** 1999-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<917006250.10420.0.nnrp-11.9e987e6e@news.demon.co.uk>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca>`

```

� <no@spam.com> wrote in message
news:j4Tp2.1911$PD.11130759@news.magma.ca...
>Hi, i'm trying to calculate leap years and need to know the " mod "
>equivalent in COBOL for the remainder.  Any help would be greatly
…[3 more quoted lines elided]…
>
Something like FUNCTION MOD(FIELDA, FIELDB) if you have an up to date
compiler.
```

#### ↳ Re: mod equivalent in cobol

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78a0rm$cro$1@news.igs.net>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca>`

```
DIVIDE a [BY/INTO] b GIVING c [ROUNDED] REMAINDER d.

� wrote in message ...
>Hi, i'm trying to calculate leap years and need to know the " mod "
>equivalent in COBOL for the remainder.  Any help would be greatly
…[4 more quoted lines elided]…
>
```

#### ↳ Re: mod equivalent in cobol

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36a9dbaf.381814714@news1.ibm.net>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca>`

```
On Fri, 22 Jan 1999 04:24:47 GMT, "�" <no@spam.com> wrote:

>Hi, i'm trying to calculate leap years and need to know the " mod "
>equivalent in COBOL for the remainder.  Any help would be greatly
…[4 more quoted lines elided]…
>

You probably really want the remaider and not the MOD.  Try

COMPUTE The-Remainder = Function Rem (Full-Year 4)
```

##### ↳ ↳ Re: mod equivalent in cobol

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 1999-01-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78d79a$ra8$1@juliana.sprynet.com>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <36a9dbaf.381814714@news1.ibm.net>`

```
Steve,

    Try this:

    03    WS-HALFWORD    PIC S9(04)     BINARY.
    03    WS-REMAINDER   PIC S9(04)     BINARY.
    03    WS-RESULT           PIC S9(04)     BINARY.
    03    WS-LEAP-IND        PIC    X(01).
            88    WS-LEAP-YR                          VALUE 'Y'.
    03    WS-DATE                PIC    9(07).
    03    WS-DATE-X            REDEFINES WS-DATE.
            05    WS-DATE-CCYY
                                                PIC   9(04).
            05    FILLER              REDEFINES WS-DATE-CCYY.
                    07      FILLER    PIC    9(02).
                    07      WS-DATE-YY
                                                PIC    9(02).
            05    FILLER              PIC    9(03).

    MOVE 1999023                       TO   WS-DATE.
    MOVE WS-DATE-CCYY        TO    WS-HALFWORD.
    MOVE SPACE                        TO    WS-LEAP-IND.
    DIVIDE    WS-HALFWORD    BY    +400
                                                        GIVING    WS-RESULT
                                                        REMAINDER
WS-REMAINDER.

    IF    WS-REMAINDER IS NOT EQUAL TO ZERO
            MOVE    WS-DATE-YY    TO    WS-HALFWORD
            DIVIDE    WS-HALFWORD    BY +4
                                                        GIVING    WS-RESULT
                                                        REMAINDER
WS-REMAINDER
            END-IF.

    IF    WS-REMAINDER IS EQUAL TO ZERO
            SET    WS-LEAP-YR       TO TRUE
            END-IF.

===============================================================

The first DIVIDE determines CCYY as a leap-year (like 2000). Note that CCYY
leap-year compliance occurs only every 400 years. If the remainder is not
zero, then issue the DIVIDE again, using only the YY as the divisor. YY
compliant leap-years for the 21st century begins with 2000 and progress
forward every 4 years, Hence, the need for the two DIVIDES.

BTW, I prefer using BINARY when performing this type of calculation. You
could substitute PACKED-DECIMAL or DISPLAY. It's your call.

HTH....

WOB,
Atlanta

>>Hi, i'm trying to calculate leap years and need to know the " mod "
>>equivalent in COBOL for the remainder.  Any help would be greatly
…[4 more quoted lines elided]…
>>
```

##### ↳ ↳ Re: mod equivalent in cobol

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 1999-01-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be47d6$765aace0$0100007f@vaagshaugen>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <36a9dbaf.381814714@news1.ibm.net>`

```
Thane Hubbell <redsky@ibm.net> wrote in article
<36a9dbaf.381814714@news1.ibm.net>...
> >Hi, i'm trying to calculate leap years and need to know the " mod "
> You probably really want the remaider and not the MOD.

And what is the difference in this context?
For positive years - none.
For negative years (BC), try -5 as an example:
FUNCTION REM: -1, i.e. "one year before leap year"
FUNCTION MOD: +3, i.e. "three years after leap year"
which is effectively the same.

Gunnar.
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36aba85e.499767707@news1.ibm.net>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <36a9dbaf.381814714@news1.ibm.net> <01be47d6$765aace0$0100007f@vaagshaugen>`

```
On 24 Jan 1999 22:59:47 GMT, "Gunnar Opheim" <gunnar.opheim@eunet.no>
wrote:

>Thane Hubbell <redsky@ibm.net> wrote in article
><36a9dbaf.381814714@news1.ibm.net>...
…[8 more quoted lines elided]…
>which is effectively the same.

Yes, of course - but the test really calls for remainder and not mod,
and they are different.  If one starts using them interchangably, the
proper meaning may become lost.
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 4)_

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 1999-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be4887$46fdb710$0100007f@vaagshaugen>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <36a9dbaf.381814714@news1.ibm.net> <01be47d6$765aace0$0100007f@vaagshaugen> <36aba85e.499767707@news1.ibm.net>`

```
Thane Hubbell <redsky@ibm.net> wrote in article
<36aba85e.499767707@news1.ibm.net>...
> On 24 Jan 1999 22:59:47 GMT, "Gunnar Opheim" <gunnar.opheim@eunet.no>
> wrote:
…[16 more quoted lines elided]…
> 

Just out of curiosity: what is your argument for "the test calls for
remainder and not mod"?

Gunnar.
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 5)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36ad291e.598279063@news1.ibm.net>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <36a9dbaf.381814714@news1.ibm.net> <01be47d6$765aace0$0100007f@vaagshaugen> <36aba85e.499767707@news1.ibm.net> <01be4887$46fdb710$0100007f@vaagshaugen>`

```
On 25 Jan 1999 18:25:07 GMT, "Gunnar Opheim" <gunnar.opheim@eunet.no>
wrote:


>Just out of curiosity: what is your argument for "the test calls for
>remainder and not mod"?

I'm on relatively weak ground -- However, 

Leap years are those whos numbers are evenly divisible by 4 and NOT
evenly divisible by 100 except when they are evenly divisible by 400.
By divisible we mean the division leaves no REMainder.  That's the
basic reason.  The second is the general misunderstanding that is
propogated by use of MOD instead of remainder.  Yes MOD and REM give
the same result most of the time, but the MOD (Modulus) of two numbers
is entirely different than the REM of the specified division.

Modulus:  Same as Absolute Value: for a complex number, computed by
adding the squares of each part and taking the positive square root of
each sum.  (Ex The Modulus of a + bi = The Square root of (a squared +
b squared).  Second meaning:  a given quantity wich gives the same
remainder when it is the divisor of two quantities (How it is used in
Function MOD).
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 6)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36ad9756.102986297@netnews>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <36a9dbaf.381814714@news1.ibm.net> <01be47d6$765aace0$0100007f@vaagshaugen> <36aba85e.499767707@news1.ibm.net> <01be4887$46fdb710$0100007f@vaagshaugen> <36ad291e.598279063@news1.ibm.net>`

```
'Twas Tue, 26 Jan 1999 04:44:51 GMT, when redsky@ibm.net (Thane Hubbell)
illuminated comp.lang.cobol thusly:

>Yes MOD and REM give
>the same result most of the time, but the MOD (Modulus) of two numbers
>is entirely different than the REM of the specified division.

Someone please correct me if I'm wrong, but I think they're only the same
when the numerator is positive, because it depends on the signs.  If both
numbers are positive, MOD and REM are the same.  The sign of MOD is always
the sign of the divisor.  The sign of REM is the product of the two signs.
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 6)_

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-01-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b75b5b.87170454@news3.ibm.net>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <36a9dbaf.381814714@news1.ibm.net> <01be47d6$765aace0$0100007f@vaagshaugen> <36aba85e.499767707@news1.ibm.net> <01be4887$46fdb710$0100007f@vaagshaugen> <36ad291e.598279063@news1.ibm.net>`

```
On Tue, 26 Jan 1999 04:44:51 GMT, redsky@ibm.net (Thane Hubbell) wrote:


>
>Modulus:  Same as Absolute Value: for a complex number, computed by
…[4 more quoted lines elided]…
>Function MOD).


????? Could you say that again ??????

According to my sources (whixh is me, but I have to admit that it is about 20 years ago
since I studied mathematics) the MODULUS m of a number N to the reference k is the
equivalence set of all numbers m where N = k*x + m for some integer x.  Usually, all the
elements in this equivalence set are "equated" to the smallest, nonnegative number.

Example:  The modulus of 12 to the reference number 5 is the following set: 
{...,-12,-8,-3,2,7,12,17,....}, or

2 = MOD(12,5)
-3 = MOD(12,5) as well

The ABSOLUTE VALUE of a COMPLEX (or REAL) number has nothing to do with the MODulus

(at least I firmly believe in what I said above, but haven't really taken any effort to
dig out my old math books to verify <s>)


with kind regards

Volker Bandke
(BSP GmbH)
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 7)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b3a563.1023371559@news1.ibm.net>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <36a9dbaf.381814714@news1.ibm.net> <01be47d6$765aace0$0100007f@vaagshaugen> <36aba85e.499767707@news1.ibm.net> <01be4887$46fdb710$0100007f@vaagshaugen> <36ad291e.598279063@news1.ibm.net> <36b75b5b.87170454@news3.ibm.net>`

```
On Sat, 30 Jan 1999 20:37:25 GMT, vbandke@ibm.net (Volker Bandke)
wrote:

>On Tue, 26 Jan 1999 04:44:51 GMT, redsky@ibm.net (Thane Hubbell) wrote:
>
…[10 more quoted lines elided]…
>????? Could you say that again ??????

I got it from Websters! <G>
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 8)_

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-01-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b4428b.2788239@news3.ibm.net>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <36a9dbaf.381814714@news1.ibm.net> <01be47d6$765aace0$0100007f@vaagshaugen> <36aba85e.499767707@news1.ibm.net> <01be4887$46fdb710$0100007f@vaagshaugen> <36ad291e.598279063@news1.ibm.net> <36b75b5b.87170454@news3.ibm.net> <36b3a563.1023371559@news1.ibm.net>`

```
On Sun, 31 Jan 1999 00:36:08 GMT, redsky@ibm.net (Thane Hubbell) wrote:

>On Sat, 30 Jan 1999 20:37:25 GMT, vbandke@ibm.net (Volker Bandke)
>wrote:
…[15 more quoted lines elided]…
>I got it from Websters! <G>  


Which, of course, is quite an authority on mathematics.   I guess, I will have to consult
my linear algebra textbooks for spell checking <g>

BTW, when it comes to leap year checking then MOD and REM are interchangeable, as a number
N is divisible by K if and only if MOD(N,k) = 0


with kind regards

Volker Bandke
(BSP GmbH)
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 8)_

- **From:** "kennet" <kennet@post11.tele.dk>
- **Date:** 1999-01-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<790soe$4cf8$1@news-inn.inet.tele.dk>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <36a9dbaf.381814714@news1.ibm.net> <01be47d6$765aace0$0100007f@vaagshaugen> <36aba85e.499767707@news1.ibm.net> <01be4887$46fdb710$0100007f@vaagshaugen> <36ad291e.598279063@news1.ibm.net> <36b75b5b.87170454@news3.ibm.net> <36b3a563.1023371559@news1.ibm.net>`

```

Thane Hubbell skrev i meddelelsen <36b3a563.1023371559@news1.ibm.net>...
>On Sat, 30 Jan 1999 20:37:25 GMT, vbandke@ibm.net (Volker Bandke)
>wrote:
…[15 more quoted lines elided]…
>I got it from Websters! <G>

As with many words "modulus" has many meanings in mathematics. For a complex
number z=a+ib it is true that mod(z) = squareroot(a*a + b*b). So for a real
number a we have mod(a)=squareroot(a*a) which is equal to the absolute value
of a.

However, modulus also has a different meaning for integers, and this is the
following: for integers a and b,

a mod b

(also written "mod(a b)") is the integer c in the interval 0,1,2,...,b-1
such that there exists another integer d, so that a = d *b + c. So it is a
bit like remainder. For positve numbers, it is precisely the same as
remainder.
This is the usual meaning when you use the function mod in any computer
language (that I know).

This is probably not very clear, but the point is this:
Websters is correct, it's just reffering to another meaning of the word
"modulus".

Regards,
Kennet
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 6)_

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 1999-01-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be4d54$3a874dd0$0100007f@vaagshaugen>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <36a9dbaf.381814714@news1.ibm.net> <01be47d6$765aace0$0100007f@vaagshaugen> <36aba85e.499767707@news1.ibm.net> <01be4887$46fdb710$0100007f@vaagshaugen> <36ad291e.598279063@news1.ibm.net>`

```
Thane Hubbell <redsky@ibm.net> wrote in article
<36ad291e.598279063@news1.ibm.net>...
> On 25 Jan 1999 18:25:07 GMT, "Gunnar Opheim" <gunnar.opheim@eunet.no>
> wrote:
…[6 more quoted lines elided]…
> Function MOD).

I am aware of those two definitions, and even a third one concerning math:
the number by which a logarithm to one base is multiplied to give the
corresponding logarithm to another base.

However the MOD function as defined in COBOL bears a strong resemblance to
REM as far as positive numbers are involved.  And that was the original
theme of this thread.
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 7)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-STvdgGJeUjoE@Dwight_Miller.iix.com>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <36a9dbaf.381814714@news1.ibm.net> <01be47d6$765aace0$0100007f@vaagshaugen> <36aba85e.499767707@news1.ibm.net> <01be4887$46fdb710$0100007f@vaagshaugen> <36ad291e.598279063@news1.ibm.net> <01be4d54$3a874dd0$0100007f@vaagshaugen>`

```
On Sun, 31 Jan 1999 23:32:25, "Gunnar Opheim" <gunnar.opheim@eunet.no>
wrote:
> I am aware of those two definitions, and even a third one concerning math:
> the number by which a logarithm to one base is multiplied to give the
…[4 more quoted lines elided]…
> theme of this thread.

I hate to belabor the point but... I'm not arguing that the results 
for positive numbers are different.  What I am saying is that MOD and 
REM "ARE" different and that one should not use MOD and REM 
interchangably - else MOD (as it has in other languages -- apparantly)
will lose it's proper meaning.
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 8)_

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be4e5e$3fcaf2f0$0100007f@vaagshaugen>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <36a9dbaf.381814714@news1.ibm.net> <01be47d6$765aace0$0100007f@vaagshaugen> <36aba85e.499767707@news1.ibm.net> <01be4887$46fdb710$0100007f@vaagshaugen> <36ad291e.598279063@news1.ibm.net> <01be4d54$3a874dd0$0100007f@vaagshaugen> <Jl0PnHJ5PvPd-pn2-STvdgGJeUjoE@Dwight_Miller.iix.com>`

```
Thane Hubbell <redsky@ibm.net> wrote in article
<Jl0PnHJ5PvPd-pn2-STvdgGJeUjoE@Dwight_Miller.iix.com>...
> I hate to belabor the point but... I'm not arguing that the results 
> for positive numbers are different.  What I am saying is that MOD and 
> REM "ARE" different and that one should not use MOD and REM 
> interchangably - else MOD (as it has in other languages -- apparantly)
> will lose it's proper meaning.

I finally have consulted a book on number theory, and I rush to admit that
you are quite right.

Gauss (1777-1855) introduced the idea of congruence, and he defined that A
is congruent to B for the modulus M if both yields the same non-negative
remainder R when divided by the modulus.

So, in the Cobol sentence
   COMPUTE R = MOD(A,M)
M is the modulus and R is the remainder when A is divided by M.  But note
that R is defined to be non-negative, while in
   COMPUTE R = REM(A,D)
R may be negative (if A or D, but not both, are negative).

So R for both functions is a remainder.  In the MOD function the second
argument is called modulus, while in the REM function the second argument
is called divisor.

When applied to determination of leap years, both functions will work.  If
we do it for negative years AD (God forbid) they yield different results
for non-leap years.  Which of them is correct is a matter of taste.

The bottom line: The function name MOD must not be confused with the
modulus argument.

Now, if that doesn't solve it, I give up.
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 9)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b69737.45480316@netnews>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <36a9dbaf.381814714@news1.ibm.net> <01be47d6$765aace0$0100007f@vaagshaugen> <36aba85e.499767707@news1.ibm.net> <01be4887$46fdb710$0100007f@vaagshaugen> <36ad291e.598279063@news1.ibm.net> <01be4d54$3a874dd0$0100007f@vaagshaugen> <Jl0PnHJ5PvPd-pn2-STvdgGJeUjoE@Dwight_Miller.iix.com> <01be4e5e$3fcaf2f0$0100007f@vaagshaugen>`

```
'Twas 2 Feb 1999 03:44:12 GMT, when "Gunnar Opheim"
<gunnar.opheim@eunet.no> illuminated comp.lang.cobol thusly:

>When applied to determination of leap years, both functions will work.  If
>we do it for negative years AD (God forbid) they yield different results
>for non-leap years.  Which of them is correct is a matter of taste.

Furthermore, to determine leap years for negative years the modulus is 3.
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 9)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-eoU9yxSzzREQ@Dwight_Miller.iix.com>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <36a9dbaf.381814714@news1.ibm.net> <01be47d6$765aace0$0100007f@vaagshaugen> <36aba85e.499767707@news1.ibm.net> <01be4887$46fdb710$0100007f@vaagshaugen> <36ad291e.598279063@news1.ibm.net> <01be4d54$3a874dd0$0100007f@vaagshaugen> <Jl0PnHJ5PvPd-pn2-STvdgGJeUjoE@Dwight_Miller.iix.com> <01be4e5e$3fcaf2f0$0100007f@vaagshaugen>`

```
On Tue, 2 Feb 1999 03:44:12, "Gunnar Opheim" <gunnar.opheim@eunet.no> 
wrote:

> Now, if that doesn't solve it, I give up.

I agree completely.   Case closed <G>.


-------------------------
Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

- **From:** cwestbury@giant.intranet.com (Chris Westbury)
- **Date:** 1999-01-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1999Jan24.214510.19488@giant>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <01be47d6$765aace0$0100007f@vaagshaugen>`

```
In article <01be47d6$765aace0$0100007f@vaagshaugen>,
"Gunnar Opheim" <gunnar.opheim@eunet.no> wrote:
>
> In article <36a9dbaf.381814714@news1.ibm.net>,
…[6 more quoted lines elided]…
> For negative years (BC), try -5 as an example:

Please note that positive years BC and negative years AD are *NOT* the
same thing because of the discontinuity caused by the fact that there is
no year zero.  The year I BC is immediately followed by the year AD I. 
The leap year V BC is AD -IV, and conversely the leap year AD IV is -V
BC.
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 4)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78h38o$ne5$1@news.igs.net>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <01be47d6$765aace0$0100007f@vaagshaugen> <1999Jan24.214510.19488@giant>`

```
I was always under the impression that there were no
leap years 2000 years ago.
;<)

Chris Westbury wrote in message <1999Jan24.214510.19488@giant>...
>In article <01be47d6$765aace0$0100007f@vaagshaugen>,
>"Gunnar Opheim" <gunnar.opheim@eunet.no> wrote:
…[18 more quoted lines elided]…
>"My wife and I bought a remote mountain hideaway and equipped it with
enough
>food, fuel, and water to last a dozen years."  "You think Y2k is going to
be
>that serious?"  "No, but we hope to sell the place to the highest panicked
>bidder at the last possible moment."  --Brian Bassett
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 5)_

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 1999-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be488c$9348b6b0$0100007f@vaagshaugen>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <01be47d6$765aace0$0100007f@vaagshaugen> <1999Jan24.214510.19488@giant> <78h38o$ne5$1@news.igs.net>`

```
Donald Tees <donald@willmack.com> wrote in article
<78h38o$ne5$1@news.igs.net>...
> I was always under the impression that there were no
> leap years 2000 years ago.

Sorry that I have to disappoint you.  The Julian calendar was introduced in
the year 46 BC in the Roman Empire and included the use of leap years.  The
year 46 BC was called the 'annus confusionis' since it lasted 445 days to
make up for errors made since year 153 BC when Jan 1. was introduced as the
start of the year.  The first year after this, 45 BC, was a leap year, and
every 4th year after that is a leap year.  Until the Gregorian calendar
revised the Julian in 1582 and introduced the additional rule that even
hundred years should be divisable by 400 to be a leap year.  To account for
the errors so far, Oct 5. to 10. was skipped that year.  This goes for the
Roman Empire, other countries switched to the Gregorian calendar much
later: in my country, Norway, 1700, in England 1752, Sweden 1753, Russia
after the revolution 1917, to mention a few.  Some countries still use the
Julian calendar, and others use quite different calendars.

OB.Cobol: If you are confident that your programs won't ever have to
support the year 2100 (or 1900), you can safely forget Gregorius' rule and
program leap year as the years divisable by four.

Gunnar Opheim.
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 6)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1999-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36ACCC41.54C5EA39@home.com>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <01be47d6$765aace0$0100007f@vaagshaugen> <1999Jan24.214510.19488@giant> <78h38o$ne5$1@news.igs.net> <01be488c$9348b6b0$0100007f@vaagshaugen>`

```
> Sorry that I have to disappoint you.  The Julian calendar was introduced in
> the year 46 BC in the Roman Empire and included the use of leap years.  

I wonder what people do who need to reference dates from before our
modern calendar.  Besides making assumptions, there would be a fair
amount of table use.  I could see a scholar having a screen which
accepts dates in a dozen different formats, including the 4th year of
the reign of Old King Cole!   It would be nice to be able to enter
Jewish and Islamic dates as well right now.  I suppose they would likely
be translated into a day based standard (modern (not IBM) Julian or
something).  Sort of like European money all converts to the Euro...
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nFmr2.2067$VB.2861690@news4.mia>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <01be47d6$765aace0$0100007f@vaagshaugen> <1999Jan24.214510.19488@giant> <78h38o$ne5$1@news.igs.net> <01be488c$9348b6b0$0100007f@vaagshaugen> <36ACCC41.54C5EA39@home.com>`

```
Howard Brazee wrote:
>
>I wonder what people do who need to reference dates from before our
…[6 more quoted lines elided]…
>something).  Sort of like European money all converts to the Euro...

There are masochists :) who have written programs to print ranges of
dates in any of a number of calendars and formats.
```

###### ↳ ↳ ↳ Calendrical Calculations .. was Re: mod equivalent in cobol

_(reply depth: 7)_

- **From:** ah739@cleveland.Freenet.Edu (Leslie J. Somos)
- **Date:** 1999-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7934cn$pms$1@pale-rider.INS.CWRU.Edu>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <01be47d6$765aace0$0100007f@vaagshaugen> <1999Jan24.214510.19488@giant> <78h38o$ne5$1@news.igs.net> <01be488c$9348b6b0$0100007f@vaagshaugen> <36ACCC41.54C5EA39@home.com>`

```

In a previous article, NOSPAMbrazee@home.com (Howard Brazee) says:

>> Sorry that I have to disappoint you.  The Julian calendar was introduced in
>> the year 46 BC in the Roman Empire and included the use of leap years.  
…[9 more quoted lines elided]…
>

Calendrical Calculations
Nachum Dershowitz and Edward M. Reingold
ISBN 0-521-56413-1 hardback
ISBN 0-521-56474-3 paperback
"The purpose of this book is to present, in a unified,
completely algorithmic form, a description of fourteen
calendars and how they relate to one another: the
present civil calendar (Gregorian), the recent ISO
commercial calendar, the old civil calendar (Julian),
the Coptic and Ethiopic calendars, the Islamic (Moslem)
calendar, the modern Persian (solar) calendar, the
Baha'i calendar, the Hebrew (Jewish) calendar, the
Mayan calendars, the French Revolutionary calendar,
the Chinese calendar, and both the old (mean) and new
(true) Hindu (Indian) calendars. Easy conversion among
these calendars is a by-product of the approach, as is
the determination of secular and religious holidays.
Calendrical Calculations makes accurate calendrical
algorithms readily available for computer use.
This volume will be a valuable resource for working
programmers, as well as a source of useful algorithmic
tools for computer scientists. It also includes a
wealth of historical material of value to anyone
interested in chronology."
```

###### ↳ ↳ ↳ Re: Calendrical Calculations .. was Re: mod equivalent in cobol

_(reply depth: 8)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36B5BF67.792541D1@NOSPAMhome.com>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <01be47d6$765aace0$0100007f@vaagshaugen> <1999Jan24.214510.19488@giant> <78h38o$ne5$1@news.igs.net> <01be488c$9348b6b0$0100007f@vaagshaugen> <36ACCC41.54C5EA39@home.com> <7934cn$pms$1@pale-rider.INS.CWRU.Edu>`

```
Thanks, I saved this message.

Leslie J. Somos wrote:

> Calendrical Calculations
> Nachum Dershowitz and Edward M. Reingold
…[22 more quoted lines elided]…
> --
```

###### ↳ ↳ ↳ Re: Calendrical Calculations .. was Re: mod equivalent in cobol

_(reply depth: 8)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yBFt2.2560$Xl5.3010173@news1.mia>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <01be47d6$765aace0$0100007f@vaagshaugen> <1999Jan24.214510.19488@giant> <78h38o$ne5$1@news.igs.net> <01be488c$9348b6b0$0100007f@vaagshaugen> <36ACCC41.54C5EA39@home.com> <7934cn$pms$1@pale-rider.INS.CWRU.Edu>`

```
Thank you Leslie, for that info!  I have been looking for a book like
that for a long time, and immediately ordered a copy!  You can find
the paperback edition at www.borders.com for $18.36 U.S.
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 6)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78kgmr$mfs$1@news.igs.net>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <01be47d6$765aace0$0100007f@vaagshaugen> <1999Jan24.214510.19488@giant> <78h38o$ne5$1@news.igs.net> <01be488c$9348b6b0$0100007f@vaagshaugen>`

```

Gunnar Opheim wrote in message <01be488c$9348b6b0$0100007f@vaagshaugen>...

>Sorry that I have to disappoint you.  The Julian calendar was introduced in
>the year 46 BC in the Roman Empire and included the use of leap years.  The
>year 46 BC was called the 'annus confusionis' since it lasted 445 days to
>make up for errors made since year 153 BC when Jan 1. was introduced as the
>start of the year.  The first year after this, 45 BC, was a leap year, and


I can absolutely assure you, that he did *not* declare the year
to be 45 BC.
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 7)_

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 1999-01-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be4d5d$3bc1da90$0100007f@vaagshaugen>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <01be47d6$765aace0$0100007f@vaagshaugen> <1999Jan24.214510.19488@giant> <78h38o$ne5$1@news.igs.net> <01be488c$9348b6b0$0100007f@vaagshaugen> <78kgmr$mfs$1@news.igs.net>`

```
Donald Tees <donald@willmack.com> wrote in article
<78kgmr$mfs$1@news.igs.net>...
> I can absolutely assure you, that he did *not* declare the year
> to be 45 BC.

Certainly not, even if prophets existed then :-) 
But that is how we refer to it now.  So the concept of leap years is more
than 2000 years old.
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 8)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1999-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<329931.66911.16449@kcbbs.gen.nz>`
- **References:** `<01be4d5d$3bc1da90$0100007f@vaagshaugen>`

```
In message <<01be4d5d$3bc1da90$0100007f@vaagshaugen>> "Gunnar Opheim" <gunnar.opheim@eunet.no> writes:
> <78kgmr$mfs$1@news.igs.net>...
> > I can absolutely assure you, that he did *not* declare the year
…[5 more quoted lines elided]…
> 

Quite, but leap years in the past are a matter of historical
record rather than of calculation.  I understand that in Rome
the years 45BC, 42BC and 39BC were leap years.

Calculations are fine for the last couple of centuries and
for the next few.  For example whether 1600 was a leap year
or not depends on the country.

When did the October 1917 revotion occur ?  The answer is
November (if you lived in Europe).
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 8)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7954ps$o86$1@news.igs.net>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <01be47d6$765aace0$0100007f@vaagshaugen> <1999Jan24.214510.19488@giant> <78h38o$ne5$1@news.igs.net> <01be488c$9348b6b0$0100007f@vaagshaugen> <78kgmr$mfs$1@news.igs.net> <01be4d5d$3bc1da90$0100007f@vaagshaugen>`

```
Depends on what you mean as a "concept".  Certainly
there were years, and they had a number of days in them,
and the number may have been 365 or 366.  However,
the concept of a leap year is that a normal year has
365 days, while a leap year has 366, and is added at
specific intervals.  That took another 16 centuries to
evolve.

Gunnar Opheim wrote in message <01be4d5d$3bc1da90$0100007f@vaagshaugen>...
>Donald Tees <donald@willmack.com> wrote in article
><78kgmr$mfs$1@news.igs.net>...
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 9)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<329932.69132.17560@kcbbs.gen.nz>`
- **References:** `<7954ps$o86$1@news.igs.net>`

```
In message <<7954ps$o86$1@news.igs.net>> "Donald Tees" <donald@willmack.com> writes:
> there were years, and they had a number of days in them,
> and the number may have been 365 or 366.  However,
…[3 more quoted lines elided]…
> evolve.

Simply not true.  What took until 1584 was establishing the
rules that we now use that keeps the years in sync with
the earth's orbit to an adequate accuracy.

A leap year every 4 years was well established by the Julian
calendar.
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 9)_

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be4e40$93c928e0$0100007f@vaagshaugen>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <01be47d6$765aace0$0100007f@vaagshaugen> <1999Jan24.214510.19488@giant> <78h38o$ne5$1@news.igs.net> <01be488c$9348b6b0$0100007f@vaagshaugen> <78kgmr$mfs$1@news.igs.net> <01be4d5d$3bc1da90$0100007f@vaagshaugen> <7954ps$o86$1@news.igs.net>`

```
Donald Tees <donald@willmack.com> wrote in article
<7954ps$o86$1@news.igs.net>...
> Depends on what you mean as a "concept".  Certainly
> there were years, and they had a number of days in them,
…[4 more quoted lines elided]…
> evolve.

I detailed this in an earlier posting (which you probably will have to go
to Dejanews to find now).  If my sources are not completely wrong, the
Julian calendar was decided in 46 BC (which they then called year 708 after
the foundation of Rome).  The first year of that calendar, 45 BC in our
terms, was to have 366 days (leap year), as well as every 4. year
thereafter.  The other years were 365 days.  So it has been since, and
still is, except that the adjustment of leaving out the century years not
divisible by 400 was declared by Pope Gregory XIII in 1582 (introduced
later in non-Roman-Catholic western countries).  So leap years have existed
(in the Julian/Gregorian calendar) since 45 BC.

Since this thread long since diverted from the original Cobol question,
this is my last posting on the theme.
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 5)_

- **From:** cwestbury@giant.intranet.com (Chris Westbury)
- **Date:** 1999-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1999Jan25.194710.19491@giant>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <78h38o$ne5$1@news.igs.net>`

```
In article <78h38o$ne5$1@news.igs.net>,
"Donald Tees" <donald@willmack.com> wrote:
>
> In article <1999Jan24.214510.19488@giant>,
…[5 more quoted lines elided]…
> ;<)

Heh!  In this newsgroup, not even a smiley will keep your joke from being
taken seriously!
```

###### ↳ ↳ ↳ Re: mod equivalent in cobol

_(reply depth: 6)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78kb0i$j8h$1@news.igs.net>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca> <78h38o$ne5$1@news.igs.net> <1999Jan25.194710.19491@giant>`

```
Yes.  I am sure that a few of them even write their
code so that it handles negative dates.  Just in case
a *really* old receivable comes up.

" I hereby declare the year to be 46 BC".  "There will be
no year zero, of course, so next year (45 BC) will be
the first leap year".  "years divisible by the root of
minus one will only happen in the past".


Chris Westbury wrote in message <1999Jan25.194710.19491@giant>...
>In article <78h38o$ne5$1@news.igs.net>,
>"Donald Tees" <donald@willmack.com> wrote:
…[14 more quoted lines elided]…
>Christopher Westbury   Y2K CAN PUT YOU ON E-Z STREET!  "I'm personally
going
>Midtown Associates     with simple stickers and fridge magnets saying 'Turn
>15 Fallon Place        Off Computer Before Midnight, 1999' reports
freelancer
>Cambridge, MA 02138    Yram Senoj (not her real name)."  --Bruce McCall
```

#### ↳ Re: mod equivalent in cobol

- **From:** "Jerry Peacock" <bismail@bisusa.com>
- **Date:** 1999-01-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78gs9m$5di$1@birch.prod.itd.earthlink.net>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca>`

```

� wrote in message ...
>Hi, i'm trying to calculate leap years and need to know the " mod "
>equivalent in COBOL for the remainder.  Any help would be greatly
>appreciated ;)
>
>Steve


Careful! Not all mod-4 years are leap years (2000 is, but 1900 was not).
```

#### ↳ Re: mod equivalent in cobol

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YwTq2.926$fz.1793467@storm.twcol.com>`
- **References:** `<j4Tp2.1911$PD.11130759@news.magma.ca>`

```
>Hi, i'm trying to calculate leap years and need to know the " mod "
>equivalent in COBOL for the remainder.  Any help would be greatly
>appreciated ;)


First to calculate a leap year lets explain a little. A leap year is any
year divisible by 4 and not divisible by 100. if divisible by 100, must be
divisible by 400. Thus:

       01  LEAP-YEAR-VARS.
           05 LY-YEAR PIC 9(04).
           05 FILLER REDEFINES LY-YEAR.
              10 LY-CC PIC 9(02).
              10 LY-YY PIC 9(02).
           05 CC-MOD-4 PIC 9(02).
           05 YY-MOD-4 PIC 9(02).
           05 TEMP-Q   PIC 9(02).
           05 LEAP-YEAR-STATUS PIC X(01) VALUE 'N'.
              88 NOT-LEAP-YEAR VALUE 'N'.
              88 IS-LEAP-YEAR  VALUE 'Y'.

       PROCEDURE DIVISION.
       .......
           MOVE GIVEN-YEAR TO LY-YEAR
           DIVIDE LY-CC BY 4 GIVING TEMP-Q REMAINDER CC-MOD4
           DIVIDE LY-YY BY 4 GIVING TEMP-Q REMAINDER YY-MOD4
           IF LY-YY = 00 THEN
              IF CC-MOD-4 = 00 THEN
                 SET IS-LEAP-YEAR TO TRUE
              ELSE
                 SET NOT-LEAP-YEAR TO TRUE
              END-IF
            ELSE
              IF YY-MOD-4 = 00 THEN
                 SET IS-LEAP-YEAR TO TRUE
              ELSE
                 SET NOT-LEAP-YEAR TO TRUE
              END-IF
            END-IF
            .

Now if you want to do something like making an array from 1 to 100 and have
the values in the array determine if it is a leap year you could eliminate
the computation and if logic:

       01  LEAP-YEAR-DATA.
      *                               00000000001111111111
      *                               01234567890123456789
           05 FILLER PIC X(00) VALUE '10001000100010001000'.
           05 FILLER PIC X(00) VALUE '10001000100010001000'.
           05 FILLER PIC X(00) VALUE '10001000100010001000'.
           05 FILLER PIC X(00) VALUE '10001000100010001000'.
           05 FILLER PIC X(00) VALUE '10001000100010001000'.
       01  FILLER REDEFINES LEAP-YEAR-DATA.
           05 FILLER OCCURS 100 TIMES.
              10 FILLER PIC X(01).
                 88 IS-IDX-LEAP-YEAR VALUE '1'.

Then using the previous example:
           MOVE GIVEN-YEAR TO LY-YEAR
           SET NOT-LEAP-YEAR TO TRUE
           IF IS-IDX-LEAP-YEAR (LY-CC + 1) THEN
              SET IS-LEAP-YEAR TO TRUE
           ELSE
              IF IS-IDX-LEAP-YEAR (LY-YY + 1) THEN
                 SET IS-LEAP-YEAR TO TRUE
              END-IF
           END-IF
           .

There may even be a simpler way to do this, but I can't think f it at the
time.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
