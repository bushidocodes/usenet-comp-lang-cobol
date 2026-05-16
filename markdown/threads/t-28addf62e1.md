[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Generating Random Numbers

_7 messages · 4 participants · 2002-02 → 2002-03_

---

### Generating Random Numbers

- **From:** "Dan" <dan@weekender.fsnet.co.uk>
- **Date:** 2002-03-01T02:39:23
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a5mpjn$jrf$1@news7.svr.pol.co.uk>`

```
Hi, its been a while since I programmed in cobol and I need to find a way of
generating random numbers in Micro Focus Personnal Cobol V2.0.02.  I know
that I can just use a combination of date and time but I'd prefer a proper
random number.

Cheers for any help.
Dan.
```

#### ↳ Re: Generating Random Numbers

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-02-28T22:42:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a5n0rf$gec$1@slb1.atl.mindspring.net>`
- **References:** `<a5mpjn$jrf$1@news7.svr.pol.co.uk>`

```
Check out the intrinsic function RANDOM - it is probably best if you use the
date/time as a "seed value" -as the ANSI/ISO definition of FUNCTION RANDOM
is "pseudo-random" which means that given the SAME seed value, you get the
same series of returned values.
```

#### ↳ Re: Generating Random Numbers

- **From:** "Fim W���stberg" <fim.wastberg@fimator.se>
- **Date:** 2002-03-01T11:09:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7kJf8.22279$n4.4158024@newsc.telia.net>`
- **References:** `<a5mpjn$jrf$1@news7.svr.pol.co.uk>`

```

"Dan" <dan@weekender.fsnet.co.uk> skrev i meddelandet
news:a5mpjn$jrf$1@news7.svr.pol.co.uk...
> Hi, its been a while since I programmed in cobol and I need to find a way
of
> generating random numbers in Micro Focus Personnal Cobol V2.0.02.  I know
> that I can just use a combination of date and time but I'd prefer a proper
…[4 more quoted lines elided]…
>
If you do not have the intrinsic function RANDOM, you can use
the code in this program:

IDENTIFICATION DIVISION.
PROGRAM-ID.    RNDGEN.
AUTHOR.        FIMATOR AB  FIM W�STBERG.
DATE-WRITTEN.  2002-03-01 12:05 IN J�RF�LLA.

* THIS PROGRAM GENERATES RANDOM NUMBERS > ZERO AND < 1


ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
*=====================

SPECIAL-NAMES. DECIMAL-POINT IS COMMA.



DATA DIVISION.
WORKING-STORAGE SECTION.
*=======================
*
01  DIVERSE.
    10  SVAR                    PIC X(1).

01  SLUMPTALSVARIABLER.
    10  SLUMPTAL-DISPLAY        PIC 9,999999999999.
    10  SLUMPTAL                PIC 9(3)V9(12).
    10  FILLER REDEFINES SLUMPTAL.
        20  SLUMP-HELTALSDEL    PIC 999.
        20  SLUMP-DECIMALDEL-1  PIC X(6).
        20  SLUMP-DECIMALDEL-2  PIC X(6).



PROCEDURE DIVISION.
STARTING SECTION.
*===============
*
    MOVE ZERO TO SLUMPTAL.
    ACCEPT SLUMP-DECIMALDEL-1 FROM TIME.
    ACCEPT SLUMP-DECIMALDEL-2 FROM TIME.


NEXT-RANDOM-NUMBER SECTION.
*==========================
*
GENERATE.
    COMPUTE SLUMPTAL = SLUMPTAL * 137.
    MOVE ZERO TO SLUMP-HELTALSDEL.

DISPLAY-IT.
    MOVE SLUMPTAL TO SLUMPTAL-DISPLAY
    DISPLAY SLUMPTAL-DISPLAY.

ASK-FOR-MORE.
    DISPLAY "MORE? Y/N"
    ACCEPT SVAR
    IF SVAR = "Y"
        GO TO NEXT-RANDOM-NUMBER.

SLUT.
    STOP RUN.


Regards
Fim.Wastberg@fimator.se
```

##### ↳ ↳ Re: Generating Random Numbers

- **From:** epc8@juno.com (E P Chandler)
- **Date:** 2002-03-03T11:44:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f64e2ff.0203031144.4698f07e@posting.google.com>`
- **References:** `<a5mpjn$jrf$1@news7.svr.pol.co.uk> <7kJf8.22279$n4.4158024@newsc.telia.net>`

```
"Fim W?tberg" <fim.wastberg@fimator.se> wrote in message news:<7kJf8.22279$n4.4158024@newsc.telia.net>...
> "Dan" <dan@weekender.fsnet.co.uk> skrev i meddelandet
> news:a5mpjn$jrf$1@news7.svr.pol.co.uk...
…[76 more quoted lines elided]…
> Fim.Wastberg@fimator.se

This works, except for two things.

First, the multiplier 137 is too small to have good statistical
properties. Tack on a few more decimal digits before the 137 in your
multiplier. Second, since you are not adding a constant after the
multiply, your seed value must not be zero, or a multiple of 2 or a
multiple of 5, lest the sequence degenerate. Just check the last
decimal digit of SLUMP-DECIMALDEL-2 and
adjust if need be. [My old compiler also wants a paragraph name in the
STARTING SECTION.]
```

###### ↳ ↳ ↳ Re: Generating Random Numbers

- **From:** "Fim W���stberg" <fim.wastberg@fimator.se>
- **Date:** 2002-03-05T08:35:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zr%g8.23079$n4.4390067@newsc.telia.net>`
- **References:** `<a5mpjn$jrf$1@news7.svr.pol.co.uk> <7kJf8.22279$n4.4158024@newsc.telia.net> <7f64e2ff.0203031144.4698f07e@posting.google.com>`

```

"E P Chandler" <epc8@juno.com> skrev i meddelandet
news:7f64e2ff.0203031144.4698f07e@posting.google.com...
> "Fim W?tberg" <fim.wastberg@fimator.se> wrote in message
news:<7kJf8.22279$n4.4158024@newsc.telia.net>...
> > "Dan" <dan@weekender.fsnet.co.uk> skrev i meddelandet
> > news:a5mpjn$jrf$1@news7.svr.pol.co.uk...
> > > Hi, its been a while since I programmed in cobol and I need to find a
way
> >  of
> > > generating random numbers in Micro Focus Personnal Cobol V2.0.02.  I
know
> > > that I can just use a combination of date and time but I'd prefer a
proper
> > > random number.
> > >
…[81 more quoted lines elided]…
> STARTING SECTION.]

You are right about the seed. Bettter to use date + time.

But you are saying "the multiplier 137 is too small to have good statistical
properties". Prove it !!

Regards
Fim.Wastberg@fimator.se
```

###### ↳ ↳ ↳ Re: Generating Random Numbers

_(reply depth: 4)_

- **From:** epc8@juno.com (E P Chandler)
- **Date:** 2002-03-05T10:44:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f64e2ff.0203051044.320cc9e@posting.google.com>`
- **References:** `<a5mpjn$jrf$1@news7.svr.pol.co.uk> <7kJf8.22279$n4.4158024@newsc.telia.net> <7f64e2ff.0203031144.4698f07e@posting.google.com> <zr%g8.23079$n4.4390067@newsc.telia.net>`

```
> > > AUTHOR.        FIMATOR AB  FIM Wï¿½STBERG.
> > > DATE-WRITTEN.  2002-03-01 12:05 IN Jï¿½RFï¿½LLA.

> > > GENERATE.
> > >     COMPUTE SLUMPTAL = SLUMPTAL * 137.
…[17 more quoted lines elided]…
> Fim.Wastberg@fimator.se

First, I was partially mistaken about the multiplier 137, it turns out
that it would be better to be 139. 137 is fine if the seed has only 4
decimal digits or less, but 139 doubles the period for seeds of 5 or
more decimal digits. See Donald Knuth's "The Art of Computer
Programming", 2nd ed. volume 2, page 20. [I investigated seeds with
1-4 decimal digits myself this past weekend. Knuth only talks about 5
or more decimal digits.]

The problem with 137 is that it is too small with respect to the
modulus. Let me refer you to an old article that discusses using pairs
of randon numbers to generate random values conforming to a normal
(gaussian) distribution. Although the authors conclude that the method
for generating normal values (the Box-Muller Transform) is at fault,
it turns out that the wild results they obtain arise because their
multiplier is too small.

Ref: Neave, H.R. On using the Box-Muller transformation with
multiplicative congruential pseudorandom number generators, Applied
Statistics, 22 (1973), 92-97.

Correlation between successive values is the problem. You might say
that it is easy to "cook" up a statistical or graphical test that
"flunks" a particular generator. This is true. All psuedo random
number generators that use the linear congruential method suffer from
some degree of "granularity".

For a discussion of the underlying theoretical problem, see

Marsaglia, George. Random Numbers fall mainly in the planes,
Proceedings of the National Academy of Sciences, 61 (1968), 25-28.

For a more recent article , see the next citation and the discussion
that follows.

Park, Stephen K and Miller, Keith W, Random number generators: good
ones are hard to find, Communications of the ACM (Association for
Computing Machinery), 31(10), 1192-1201, 1998.

Meanwhile, I'll try to cook up a nice example and post it as a follow
up.
```

###### ↳ ↳ ↳ Re: Generating Random Numbers

_(reply depth: 5)_

- **From:** epc8@juno.com (E P Chandler)
- **Date:** 2002-03-05T20:05:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f64e2ff.0203052005.5cbf9c35@posting.google.com>`
- **References:** `<a5mpjn$jrf$1@news7.svr.pol.co.uk> <7kJf8.22279$n4.4158024@newsc.telia.net> <7f64e2ff.0203031144.4698f07e@posting.google.com> <zr%g8.23079$n4.4390067@newsc.telia.net> <7f64e2ff.0203051044.320cc9e@posting.google.com>`

```
> You are right about the seed. Bettter to use date + time.
> 
> But you are saying "the multiplier 137 is too small to have good statistical
> properties". Prove it !!
 
I wrote fixed point decimal fractions to a file, then used two draws
to create 2 letter sequences of letters A to Z. I tabulated their
frequencies and computed chi-square, expecting 20 counts per cell.

10 runs with a multiplier of 137 gave these chi-square values with 675
degrees of freedom:

690.3 777.6 787.7 839.6 743.1
777.1 797.7 776.7 754.7 718.2

Since the critical value, at the 5% level of significance, of
chi-square for 675 degrees of freedom is approximately 736.4, having 8
out of 10 runs with extreme values of the statistic is good evidence
that the numbers are not in fact uniformly distributed.

Using a slightly larger multiplier of 1137 I obtained:

647.9 648.8 566.6 690.6 641.8
610.4 585.3 700.6 704.7 711.8

None of these values are extreme.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
