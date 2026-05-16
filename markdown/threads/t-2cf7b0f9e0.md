[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help with compute

_11 messages · 9 participants · 1998-08 → 1998-09_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help with compute

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35e9a5b4.0@news1.ibm.net>`

```
The following Cobol program gives different results on different compilers.
What should it give?
On Realia and MicroFocus the two displays are the same.
On Fujitsu, the second on shows zeroes.
What does the standard say here?
Or are intermediate results 'implementor defined'?

000100 IDENTIFICATION DIVISION.
000200 PROGRAM-ID.    TT.
000300
000400 AUTHOR.        LEIF SVALGAARD.
000500
000600 DATE-WRITTEN.  98/08/30
000700     -REVISED:  98/08/30.
000800
000900 ENVIRONMENT DIVISION.
001000
001100 CONFIGURATION SECTION.
001200 SOURCE-COMPUTER. ALMOST-PORTABLE.
001300 OBJECT-COMPUTER. ALMOST-PORTABLE.
001400
001500 DATA DIVISION.
001600
001700 WORKING-STORAGE SECTION.
001800
001900 01  SOME-VARIABLES.
002000     02  THE-SIZE                PIC S9(7)  COMP  VALUE +5000000.
002100     02  THE-RESULT              PIC S9(7)  COMP.
002300     02  RANDOM-INTEGER          PIC S9(7)  COMP  VALUE +1234567.
002400     02  RANDOM-MODULUS          PIC S9(7)  COMP  VALUE +2099863.
002900     02  JUNK                    PIC X.
003000
003100 PROCEDURE DIVISION.
003200 BEGIN-PROGRAM.
003300     COMPUTE THE-RESULT = RANDOM-INTEGER * THE-SIZE
003400                        / RANDOM-MODULUS
003500     DISPLAY THE-RESULT
003600     COMPUTE THE-RESULT = RANDOM-INTEGER / RANDOM-MODULUS
003700                        * THE-SIZE
003800     DISPLAY THE-RESULT
003900     ACCEPT JUNK
004000     .
004100
004200 EXIT-PROGRAM.
004300     EXIT PROGRAM
004400     .
004500 STOP-PROGRAM.
004600     STOP RUN
004700     .
```

#### ↳ Re: Help with compute

- **From:** AS-DATA@t-online.de (Andreas Strzoda)
- **Date:** 1998-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6scbp4$3cn$1@news01.btx.dtag.de>`
- **References:** `<35e9a5b4.0@news1.ibm.net>`

```
Andreas Strzoda schrieb:

> Does someone out ther has experience with
> FC 4.0 (standard, not PowerCobol) and
…[8 more quoted lines elided]…
>
```

#### ↳ Re: Help with compute

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JFiG1.3809$_B3.4376878@news2.mia.bellsouth.net>`
- **References:** `<35e9a5b4.0@news1.ibm.net>`

```
Welcome to the wonderful world of expression evaluation! ;-)

What is likely happening is that, because all arguments are integers,
Fujitsu COBOL is storing the intermediate results in an integer.
Since RANDOM-INTEGER < RANDOM-MODULUS, the intermediate result of the
divide is zero which, when multiplied by THE-SIZE returns zero.

Because of this, it is usually advisable to place your multiplies
before your divides (or nest them in parenthesis to force earlier
evaluation), so long as you do not generate an intermediate result
which is *too* large and is truncated.  I don't have Fujitsu COBOL
to check, but there is a good chance that if you define one of the
data names (e.g. RANDOM-INTEGER) with a V9 on the end, it will work
correctly.  This alerts the compiler to provide for non integer
intermediate results.  Believe it or not, figuring out just how to
evaluate a particular expression without truncation or overflow is
not a trivial problem for the compiler to solve.  It's much easier
with real variables, of course.
```

##### ↳ ↳ Re: Help with compute

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35e9bd28.0@news1.ibm.net>`
- **References:** `<35e9a5b4.0@news1.ibm.net> <JFiG1.3809$_B3.4376878@news2.mia.bellsouth.net>`

```
Judson McClendon wrote in message ...
>Welcome to the wonderful world of expression evaluation! ;-)
>
…[8 more quoted lines elided]…
>which is *too* large and is truncated.

(snippage)

All that is perfectly clear. My question has to do with (input to?)
what the (coming)standard has to say about this. Is this even
considered?
>Leif Svalgaard wrote:
>>
>>The following Cobol program gives different results on different
compilers.
>>What should it give?
>>On Realia and MicroFocus the two displays are the same.
…[52 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Help with compute

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<U6kG1.1132$Kt4.5466240@news1.atlantic.net>`
- **References:** `<35e9a5b4.0@news1.ibm.net> <JFiG1.3809$_B3.4376878@news2.mia.bellsouth.net> <35e9bd28.0@news1.ibm.net>`

```

Leif Svalgaard wrote in message <35e9bd28.0@news1.ibm.net>...
>Judson McClendon wrote in message ...
>>Welcome to the wonderful world of expression evaluation! ;-)
…[15 more quoted lines elided]…
>considered?

Committee Draft 1.2 provides for "native" arithmetic and "standard"
arithmetic. Native is defined by the implementor. Standard specifies
that intermediate results shall have at least 32 significant digits and
an exponent with a range of plus or minus 100.

If you want to get a better idea how each of your current compilers
processes intermediate results, look for the section on "arithmetic
expressions." I find it interesting that MicroFocus uses two methods;
one of which is selected based upon compatibilty with other systems.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: Help with compute

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6scnkq$l9a@dfw-ixnews9.ix.netcom.com>`
- **References:** `<35e9a5b4.0@news1.ibm.net> <JFiG1.3809$_B3.4376878@news2.mia.bellsouth.net> <35e9bd28.0@news1.ibm.net>`

```

Leif Svalgaard wrote in message <35e9bd28.0@news1.ibm.net>...
>Judson McClendon wrote in message ...
>>Welcome to the wonderful world of expression evaluation! ;-)
…[17 more quoted lines elided]…
>>>


   and the good news is that the draft Standard has a new option called
"Arithmetic is Standard" which (I think) will impact or at least give a
portable result for this statement.  A few things to note:

  1) There are a LOT of rules for Standard Arithmetic - so I am not positive
that it applies in this sample.  (You can look at the draft if you want to
figure it out for yourself)

   2)  There is some concern that the overhead for Standard Arithmetic will
be so great that in the "real world" no one will ever use it.  (It requires
that most arithmetic be done in a floating point format with 32 digits of
precision.  This is a very imprecise description of it, so please don't get
excited from this wording.)

 3) For programs coded today, the default will remain "ARITHMETIC IS NATIVE"
which means you will get the same un-portable results as today.

P.S.  If you want me to forward your original sample to the person who
understands Standard Arithmetic the best - and ask him what the results will
be, I will try and do so.
```

###### ↳ ↳ ↳ Re: Help with compute

_(reply depth: 4)_

- **From:** scm@enterprise.net (Shaun C. Murray)
- **Date:** 1998-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sgtb5$g4j$5@news.enterprise.net>`
- **References:** `<35e9a5b4.0@news1.ibm.net> <JFiG1.3809$_B3.4376878@news2.mia.bellsouth.net> <35e9bd28.0@news1.ibm.net> <6scnkq$l9a@dfw-ixnews9.ix.netcom.com>`

```
In article <6scnkq$l9a@dfw-ixnews9.ix.netcom.com>, wmklein@ix.netcom.com 
says...

>
>   and the good news is that the draft Standard has a new option called
>"Arithmetic is Standard" which (I think) will impact or at least give a
>portable result for this statement.  A few things to note:

Of course there already is a portable solution. Don't use COMPUTE.
```

#### ↳ Re: Help with compute

- **From:** nop06685@mail.telepac.pt (Frederico Fonseca)
- **Date:** 1998-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35eb529e.1257132@news.telepac.pt>`
- **References:** `<35e9a5b4.0@news1.ibm.net>`

```
On Sun, 30 Aug 1998 14:19:16 -0500, "Leif Svalgaard" <leif@ibm.net>
wrote:

>The following Cobol program gives different results on different compilers.
>What should it give?
…[3 more quoted lines elided]…
>Or are intermediate results 'implementor defined'?
With RM/COBOL and ACUCOBOL the result is

 2939637
 2939637

With Fujitsu v4 the output is

 2939637
 0000000

Maybe this is some "bug" of Fujitus (They have others)


FF
```

#### ↳ Re: Help with compute

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298242.29578.8079@kcbbs.gen.nz>`
- **References:** `<35e9a5b4.0@news1.ibm.net>`

```
In message <<35e9a5b4.0@news1.ibm.net>> "Leif Svalgaard" <leif@ibm.net> writes:
> What should it give?
> On Realia and MicroFocus the two displays are the same.
…[9 more quoted lines elided]…
> 003800     DISPLAY THE-RESULT

In the Fujitsu 'Migration Guide' for version 3 (is this 3 or 4
you are using) it states:

"In MF Cobol the accuracy of intermediate results is assured
for 18 digits in the integer part and 18 digits in the 
fractional part.

"In Cobol-85 the accuracy of intermediate results is assured
for 30 gigits for the integer and fractional parts combined."

Given this is true I can't see why it would give zero.
```

##### ↳ ↳ Re: Help with compute

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35eab136.0@news1.ibm.net>`
- **References:** `<35e9a5b4.0@news1.ibm.net> <3298242.29578.8079@kcbbs.gen.nz>`

```
see below

Richard Plinston wrote in message <3298242.29578.8079@kcbbs.gen.nz>...
>In message <<35e9a5b4.0@news1.ibm.net>> "Leif Svalgaard" <leif@ibm.net>
writes:
>> What should it give?
>> On Realia and MicroFocus the two displays are the same.
…[21 more quoted lines elided]…
>Given this is true I can't see why it would give zero.



===> neither can I, but it does.
probably because the result of the divide is zero (as an integer).

>
```

##### ↳ ↳ Re: Help with compute

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35EB6F26.F58BA5D9@att.net>`
- **References:** `<35e9a5b4.0@news1.ibm.net> <3298242.29578.8079@kcbbs.gen.nz>`

```
Richard Plinston wrote:
> 
(snip)
> 
> In the Fujitsu 'Migration Guide' for version 3 (is this 3 or 4
…[7 more quoted lines elided]…
> for 30 gigits for the integer and fractional parts combined."

Wow! 30 gigits (sic) = 30 (1000 x 1000) digits? That's some precision.

Bill Lynch :-)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
