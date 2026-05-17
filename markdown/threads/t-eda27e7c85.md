[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Inaccurate math results in Micro Focus Unix

_46 messages · 14 participants · 2013-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Inaccurate math results in Micro Focus Unix

- **From:** eselick <eselick@gmail.com>
- **Date:** 2013-05-11T03:54:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com>`

```
Hi

The following formula gives $5.88/hr in MF cobol V3.2 on Unix which is incorrect.

COMPUTE WS-DOL-HR ROUNDED = WS-DOL-ERN / WS-HRS-WRK

Initial values:

WS-HRS-WRK = .0833333
WS-DOL-ERN = .49

Working storage:

       77  WS-HRS-WRK                  PIC 9(2)V9(6) COMP.
       77  WS-DOL-HR                   PIC 9(2)V9(2) COMP.
       77  WS-DOL-ERN                  PIC 9V9(2)    COMP.


The same formula in Excel gives $5.93/hr which is the correct answer.

This is only happening when dol-ern is very small.

Thanks for any ideas.

E.
```

#### ↳ Re: Inaccurate math results in Micro Focus Unix

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2013-05-11T04:27:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b54ad80-826a-4884-b01b-45736ca5e68e@googlegroups.com>`
- **In-Reply-To:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com>`

```
On Saturday, May 11, 2013 6:54:01 AM UTC-4, eselick wrote:
> Hi
> 
…[20 more quoted lines elided]…
> Thanks for any ideas.

.0833333 requires a PIC of 9(2)V9(7).

Both Windows Calculator and Excel 2010 give 5.88, on my system.

That suggests either there is a problem with the Excel being
used or the formula as used in Excel.
```

##### ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

- **From:** elliotg8@gmail.com
- **Date:** 2013-05-11T05:19:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1b24d0da-0373-4ad8-99bc-4ebea3a95a47@googlegroups.com>`
- **In-Reply-To:** `<3b54ad80-826a-4884-b01b-45736ca5e68e@googlegroups.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <3b54ad80-826a-4884-b01b-45736ca5e68e@googlegroups.com>`

```
Hi Rick
I've figured out what's happening. In fact, the real dollars earned is .49425. 

This is calculated by multiplying 5.93 by 5 minutes worked or .083333 in decimal hours but the precision was lost by the time I did my formula.

I was misled in Excel even when I redid it the calculation because I had the output formatted as $, so it displayed as $.49, however internally is was using the extra decimals and got 5.93

When I just keyed in .49 it did get 5.88 as you said. The formatting got me!!

Duh !!.

It's a business problem since people are not paid in dollars to 4 decimal places, so the accuracy is lost.

Thanks for engaging in the dialog

Elliot
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2013-05-11T06:16:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eaf66d7e-fb4a-4430-9332-a9bbc4858d8e@googlegroups.com>`
- **In-Reply-To:** `<1b24d0da-0373-4ad8-99bc-4ebea3a95a47@googlegroups.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <3b54ad80-826a-4884-b01b-45736ca5e68e@googlegroups.com> <1b24d0da-0373-4ad8-99bc-4ebea3a95a47@googlegroups.com>`

```
On Saturday, May 11, 2013 8:19:42 AM UTC-4, elli...@gmail.com wrote:
[snip]

> Thanks for engaging in the dialog

And thank you for providing the resolution to the problem.
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-05-12T12:06:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<av84orFakjaU1@mid.individual.net>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <3b54ad80-826a-4884-b01b-45736ca5e68e@googlegroups.com> <1b24d0da-0373-4ad8-99bc-4ebea3a95a47@googlegroups.com>`

```
elliotg8@gmail.com wrote:
> Hi Rick
> I've figured out what's happening. In fact, the real dollars earned
…[20 more quoted lines elided]…
> Elliot

I learned a long time ago that for dealing with currency in COBOL a picture 
with 4 decimal places avoids rounding problems.

When obtaining currency data from other systems  like Excel or Access store 
it into COBOL as PIC S9(14)v9(4).

Obviously when it is formatted for output only 2 places are shown.

Saves a lot of head scratching...

Pete.


-- 
"I used to write COBOL...now I can do anything."
```

#### ↳ Re: Inaccurate math results in Micro Focus Unix

- **From:** Doug Miller <doug_at_milmac_dot_com@example.com>
- **Date:** 2013-05-12T16:12:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com>`

```
eselick <eselick@gmail.com> wrote in news:599b5508-65a7-43df-bc9f-0b92c1e511d9
@googlegroups.com:

> Hi
> 
…[16 more quoted lines elided]…
> The same formula in Excel gives $5.93/hr which is the correct answer.

No, it is not. Do it with pencil and paper, or pick up a calculator, and you will see that the 
correct answer is indeed 5.88, not 5.93.
```

##### ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

- **From:** Pete Trashwood <peteisinthood@trashwood.com>
- **Date:** 2013-05-12T16:28:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kmofv5$3a6$4@solani.org>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116>`

```
On 2013-05-12, Doug Miller <doug_at_milmac_dot_com@example.com> wrote:
> eselick <eselick@gmail.com> wrote in news:599b5508-65a7-43df-bc9f-0b92c1e511d9
> @googlegroups.com:
…[3 more quoted lines elided]…
>> The following formula gives $5.88/hr in MF cobol V3.2 on Unix which is incorrect.

I'm going with Doug on this one. It sure looks correct to me.

>> Working storage:
>> 
>>        77  WS-HRS-WRK                  PIC 9(2)V9(6) COMP.
>>        77  WS-DOL-HR                   PIC 9(2)V9(2) COMP.
>>        77  WS-DOL-ERN                  PIC 9V9(2)    COMP.

Does your compiler not have packed decimal support? Doing money calcs in
binary is a sure way to get your incompetent ass fired. I wouldn't want to
be you.

>> The same formula in Excel gives $5.93/hr which is the correct answer.
>
> No, it is not. Do it with pencil and paper, or pick up a calculator, and you will see that the 
> correct answer is indeed 5.88, not 5.93.

Yep it sure is and I have some serious questions about this guy and how he
got this job.
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-05-13T12:42:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avar7bFslqoU1@mid.individual.net>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org>`

```
Pete Trashwood wrote:
> On 2013-05-12, Doug Miller <doug_at_milmac_dot_com@example.com> wrote:
>> eselick <eselick@gmail.com> wrote in
…[26 more quoted lines elided]…
> how he got this job.

You are obviously no relation to me.

I post under my own name because I have the courage of my convictions, and I 
don't need to hide behind an alias.

I also accept that some people will be pissed off with my posts but most of 
them also have the balls to say so to my face.

Pete.

-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 4)_

- **From:** Doug Miller <doug_at_milmac_dot_com@example.com>
- **Date:** 2013-05-13T00:57:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XnsA1BED5AFDCCA0dougmilmaccom@78.46.70.116>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <avar7bFslqoU1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in news:avar7bFslqoU1
@mid.individual.net:

> Pete Trashwood wrote:
>> On 2013-05-12, Doug Miller <doug_at_milmac_dot_com@example.com> wrote:
…[38 more quoted lines elided]…
> 
Nevertheless, his point is valid: doing money calculations in binary *is* a very bad idea.
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2013-05-12T18:27:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bbe2dd75-6864-4056-a179-be1e32be3984@wb17g2000pbc.googlegroups.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <avar7bFslqoU1@mid.individual.net> <XnsA1BED5AFDCCA0dougmilmaccom@78.46.70.116>`

```
On May 13, 12:57 pm, Doug Miller <doug_at_milmac_dot_...@example.com>
wrote:
> "Pete Dashwood" <dashw...@removethis.enternet.co.nz> wrote in news:avar7bFslqoU1
> @mid.individual.net:
…[50 more quoted lines elided]…
> Nevertheless, his point is valid: doing money calculations in binary *is* a very bad idea.

Complete nonsense.
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 5)_

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2013-05-12T22:13:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<61m0p819ce73nr0huiuo055egg5466jfst@4ax.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <avar7bFslqoU1@mid.individual.net> <XnsA1BED5AFDCCA0dougmilmaccom@78.46.70.116>`

```
On Mon, 13 May 2013 00:57:11 +0000 (UTC), Doug Miller
<doug_at_milmac_dot_com@example.com> wrote:

>"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in news:avar7bFslqoU1
>@mid.individual.net:
…[42 more quoted lines elided]…
>Nevertheless, his point is valid: doing money calculations in binary *is* a very bad idea.


To agree with Richard: completely wrong.

Currency calculations need to be done in properly scaled (almost
always decimal scaled) fixed point arithmetic.  *FP* is certainly a
bad idea most of the time.

Decimal scaling is somewhat more convenient if you have decimal
arithmetic facilities, but that's, and the greater similarity to some
I/O formats are only advantages.

In fact the Cobol spec doesn't specify the internal representation*,
but it does specify the results of arithmetic operations.  Any
fiddling needed to accomplish that is the job of the compiler, and the
result of:

   01 A PIC 9(9)v9(3) USAGE x.
   01 B PIC 9(5)v9(6) USAGE x.
   01 C PIC 9(10)v9(4) USAGE x.

   COMPUTE C = A * B.

is the same if USAGE specifies a display binary or decimal format.

Again, doing currency in floating point is bad idea.


*OK, these days it does get into that a bit, but it didn't used to,
and what COMP-x actually meant was quite undefined.
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-05-13T19:07:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avbhp4F2f2eU1@mid.individual.net>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <avar7bFslqoU1@mid.individual.net> <XnsA1BED5AFDCCA0dougmilmaccom@78.46.70.116> <61m0p819ce73nr0huiuo055egg5466jfst@4ax.com>`

```
Robert Wessel wrote:
> On Mon, 13 May 2013 00:57:11 +0000 (UTC), Doug Miller
> <doug_at_milmac_dot_com@example.com> wrote:
…[72 more quoted lines elided]…
> is the same if USAGE specifies a display binary or decimal format.

A very good point.

As stated previously, I use PIC s9(14)v9(4)  for currency and have never had 
a problem.

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 7)_

- **From:** bill@server1.cs.uofs.edu (Bill Gunshannon)
- **Date:** 2013-05-13T11:57:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avc2pcF62qbU1@mid.individual.net>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <avar7bFslqoU1@mid.individual.net> <XnsA1BED5AFDCCA0dougmilmaccom@78.46.70.116> <61m0p819ce73nr0huiuo055egg5466jfst@4ax.com> <avbhp4F2f2eU1@mid.individual.net>`

```
In article <avbhp4F2f2eU1@mid.individual.net>,
	"Pete Dashwood" <dashwood@removethis.enternet.co.nz> writes:
> Robert Wessel wrote:
>> On Mon, 13 May 2013 00:57:11 +0000 (UTC), Doug Miller
…[79 more quoted lines elided]…
> 

Glad to see the "s".  :-)  My last gig involved a bunch of programs
that computed parts and labor costs and everyone was so proud of the
fact that according to their reports estimating was so good they
never went over the amounts they estimated.

That is they never did until I got there and found none of the
intermediate results had signs so as soon as the budget went
negative, presto, it was positive again!!  :-)  Oh yeah, these
programs had been running for nigh on to 30 years like that.  Sigh....

bill

-- 
Bill Gunshannon          |  de-moc-ra-cy (di mok' ra see) n.  Three wolves
billg999@cs.scranton.edu |  and a sheep voting on what's for dinner.
University of Scranton   |
Scranton, Pennsylvania   |         #include <std.disclaimer.h>
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-05-14T11:10:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avda6mFf5u7U1@mid.individual.net>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <avar7bFslqoU1@mid.individual.net> <XnsA1BED5AFDCCA0dougmilmaccom@78.46.70.116> <61m0p819ce73nr0huiuo055egg5466jfst@4ax.com> <avbhp4F2f2eU1@mid.individual.net> <avc2pcF62qbU1@mid.individual.net>`

```
Bill Gunshannon wrote:
> In article <avbhp4F2f2eU1@mid.individual.net>,
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> writes:
…[83 more quoted lines elided]…
> Glad to see the "s".  :-)

It's olde tyme mainframe programming, as I'm sure you know, Bill.

If you don't put a sign on it, extra logical OR instructions are generated 
to force a positive sign. There was a time, back in the mists of antiquity, 
when EVERY extra instruction generated had to be considered... Thankfully, 
those days are gone. Nowadays we use a sign because of functionality and not 
especially for efficiency.



> My last gig involved a bunch of programs
> that computed parts and labor costs and everyone was so proud of the
…[6 more quoted lines elided]…
> programs had been running for nigh on to 30 years like that.  Sigh....

It's amazing, isn't it?  Passed all the test plans, went live and everybody 
"believes" in it...

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 6)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2013-05-17T20:35:51-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o9fdp894bfkute1ls9jattehcap30tsc6k@4ax.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <avar7bFslqoU1@mid.individual.net> <XnsA1BED5AFDCCA0dougmilmaccom@78.46.70.116> <61m0p819ce73nr0huiuo055egg5466jfst@4ax.com>`

```
On Sun, 12 May 2013 22:13:58 -0500, Robert Wessel
<robertwessel2@yahoo.com> wrote:

>On Mon, 13 May 2013 00:57:11 +0000 (UTC), Doug Miller
><doug_at_milmac_dot_com@example.com> wrote:
…[72 more quoted lines elided]…
>
That depends.  If your COBOL has the new IEEE decimal floating point
(which the IBM z series COBOL doesn't despite Mike Cowlishaw having
played a major role in developing it while he was still at IBM and
working as an IBM fellow), it is designed for financial transactions
and supports multiple forms of rounding including rounding half to the
nearest even - 6.5 and 5.5 both round to 6.  The failure by IBM COBOL
to support the IEEE floating point and the decimal floating point
despite the fact that Java supports them and IBM COBOL OO is to
support interface with Java is something that baffles and angers me.

Clark Morris 
>
>*OK, these days it does get into that a bit, but it didn't used to,
>and what COMP-x actually meant was quite undefined.
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 7)_

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2013-05-18T04:10:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ligep8doct3e2738vfnsgpj7n8jo6ae2ed@4ax.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <avar7bFslqoU1@mid.individual.net> <XnsA1BED5AFDCCA0dougmilmaccom@78.46.70.116> <61m0p819ce73nr0huiuo055egg5466jfst@4ax.com> <o9fdp894bfkute1ls9jattehcap30tsc6k@4ax.com>`

```
On Fri, 17 May 2013 20:35:51 -0300, Clark F Morris
<cfmpublic@ns.sympatico.ca> wrote:

>On Sun, 12 May 2013 22:13:58 -0500, Robert Wessel
><robertwessel2@yahoo.com> wrote:
…[31 more quoted lines elided]…
>support interface with Java is something that baffles and angers me.


Sort-of.  IEEE decimal math is defined in such a way so that results
largely avoid the "floating" aspect of FP numbers so long as you keep
the results in range.

So IEEE decimal float is OK for currency calculations so long as you
don't actually let the numbers float...  But the 128-bit format is big
enough that you can use it that way much of the time.

Still, I'm of the opinion that decimal hardware of any sort is mostly
a waste (some decimal to/from binary conversion support would probably
be worthwhile)), and just converting to fixed point binary and doing
the decimal scaling there is fast enough.  (Old) packed decimal
arithmetic on Z is slow enough that it's likely to be faster to go the
binary route for all but the most trivial calculations.  The decimal
FP looks to be pretty fast, though.  But the actual amount of decimal
math that's done is now such a small fraction of CPUs spend time on, I
just don't see the value of a bunch of dedicated hardware.

And I acknowledge that some people disagree with me on that, but the
general computing community does not.  The only meaningful decimal
support is packed on Z, and decimal FP on POWER and Z.  Literally
nobody else has much worth noting.

BTW, IEEE binary FP has supported round to even (as the default) since
day one, so that's not exactly new with decimal FP, although the
implications of rounding a binary fraction are obviously different
than rounding a decimal fraction.
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-05-13T19:04:10+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avbhj8F2dpgU1@mid.individual.net>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <avar7bFslqoU1@mid.individual.net> <XnsA1BED5AFDCCA0dougmilmaccom@78.46.70.116>`

```
Doug Miller wrote:
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in
> news:avar7bFslqoU1 @mid.individual.net:
…[45 more quoted lines elided]…
> *is* a very bad idea.

Yes it is, but why didn't you say that under your own name? Do you seriously 
think I don't have the capability to trace your mail?

Doug, we have had differences in the past but I never expected you to resort 
to trashing the family name. If you have an issue with me, have it with me, 
not my family.

I bear you no malice despite the disrespect you have shown, but that says 
more about you than it does about me.

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2013-05-12T18:23:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org>`

```
On May 13, 4:28 am, Pete Trashwood <peteisinth...@trashwood.com>
wrote:
> On 2013-05-12, Doug Miller <doug_at_milmac_dot_...@example.com> wrote:
>
…[8 more quoted lines elided]…
> be you.

For COBOL there is no difference at all in the results of calculations
when the fields are COMP, BINARY, COMP-5, PACKED, or DISPLAY NUMERIC,
or any combination. There may be tiny differences in the speed.

The only significant difference is the storage format and size.

It is not like floating point real was specified.

The incompetence in COBOL is yours.


> >> The same formula in Excel gives $5.93/hr which is the correct answer.
>
…[4 more quoted lines elided]…
> got this job.

The serious question is why anyone would use Excel.
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-05-13T19:10:58+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avbi01F2gk9U1@mid.individual.net>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com>`

```
Richard wrote:
> On May 13, 4:28 am, Pete Trashwood <peteisinth...@trashwood.com>
> wrote:
…[17 more quoted lines elided]…
> The only significant difference is the storage format and size.

Exactly. COBOL does a great job of converting and scaling.

>
> It is not like floating point real was specified.
…[14 more quoted lines elided]…
> The serious question is why anyone would use Excel.

Millions of people use Excel every day and not only find it useful, but also 
get it right. I think the OP was fair and open about his mistake and 
explained how he got it wrong. It wasn't Excel that was wrong here.

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 5)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2013-05-13T08:01:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com>`
- **In-Reply-To:** `<avbi01F2gk9U1@mid.individual.net>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net>`

```
> > The serious question is why anyone would use Excel. 

> Millions of people use Excel every day and not only find it useful, but also get it right. I think the OP was fair and open about his mistake and explained how he got it wrong. It wasn't Excel that was wrong here. 

I use Excel extensively but if you look up Louise Pryor's Excel Archives you will find enough reasons to mistrust peoples' use of Excel:

http://www.louisepryor.com/tag/spreadsheet-errors/
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 6)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2013-05-13T13:21:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<05adnYp6rp2bvAzMnZ2dnUVZ_qednZ2d@earthlink.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com>`

```

"Alistair Maclean" <alistair.j.l.maclean@gmail.com> wrote in message 
news:a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com...
>> > The serious question is why anyone would use Excel.
>
…[7 more quoted lines elided]…
> http://www.louisepryor.com/tag/spreadsheet-errors/

Just about any tool can be misused.  That is not necessarily the tool's 
fault.  People need to learn to use their tools properly and with in their 
applicable limits.
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-05-14T11:12:30+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avdaauFf6ofU1@mid.individual.net>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <05adnYp6rp2bvAzMnZ2dnUVZ_qednZ2d@earthlink.com>`

```
Charles Hottel wrote:
> "Alistair Maclean" <alistair.j.l.maclean@gmail.com> wrote in message
> news:a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com...
…[13 more quoted lines elided]…
> with in their applicable limits.

As someone who produces tools, all I can say is: "Amen to that!"

Pete.

-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 7)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2013-05-14T14:21:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373f103c-ffb9-4939-85ee-7db0d7d146cb@googlegroups.com>`
- **In-Reply-To:** `<05adnYp6rp2bvAzMnZ2dnUVZ_qednZ2d@earthlink.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <05adnYp6rp2bvAzMnZ2dnUVZ_qednZ2d@earthlink.com>`

```
On Monday, 13 May 2013 18:21:13 UTC+1, Charles Hottel wrote:
>> Millions of people use Excel every day and not only find it useful, but 
>> also get it right. I think the OP was fair and open about his mistake and >> explained how he got it wrong. It wasn't Excel that was wrong here. 

Alistair Maclean wrote:
> I use Excel extensively but if you look up Louise Pryor's Excel Archives > 
> you will find enough reasons to mistrust peoples' use of Excel: 
> http://www.louisepryor.com/tag/spreadsheet-errors/

CH wrote: 
> Just about any tool can be misused. That is not necessarily the tool's 
> fault. People need to learn to use their tools properly and with in 
> their applicable limits.

And in reply:
I was not criticising the tool but the lack of skill and rigour in the application and verification of the results of using that tool by those who use the tool naively believing that they are capable programmers.
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2013-05-15T13:12:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kn01ko$5rt$1@reader1.panix.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <05adnYp6rp2bvAzMnZ2dnUVZ_qednZ2d@earthlink.com> <373f103c-ffb9-4939-85ee-7db0d7d146cb@googlegroups.com>`

```
In article <373f103c-ffb9-4939-85ee-7db0d7d146cb@googlegroups.com>,
Alistair Maclean  <alistair.j.l.maclean@gmail.com> wrote:
>On Monday, 13 May 2013 18:21:13 UTC+1, Charles Hottel wrote:

[snip]

>Alistair Maclean wrote:

[snip]

>CH wrote: 

[snip]

>And in reply:

[snip]

Your diligent work is noticed and appreciated, Mr Maclean.

DD
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 9)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2013-05-16T11:58:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e0a01f9c-f534-42fd-9d2d-b3a355a75b1b@googlegroups.com>`
- **In-Reply-To:** `<kn01ko$5rt$1@reader1.panix.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <05adnYp6rp2bvAzMnZ2dnUVZ_qednZ2d@earthlink.com> <373f103c-ffb9-4939-85ee-7db0d7d146cb@googlegroups.com> <kn01ko$5rt$1@reader1.panix.com>`

```
On Wednesday, 15 May 2013 14:12:56 UTC+1, docd...@panix.com wrote:
> Your diligent work is noticed and appreciated, Mr Maclean. DD

Thanks. I am trying (very) so please forgive any recidivism.
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-05-14T11:11:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avda9eFf6ceU1@mid.individual.net>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com>`

```
Alistair Maclean wrote:
>>> The serious question is why anyone would use Excel.
>
…[9 more quoted lines elided]…
> http://www.louisepryor.com/tag/spreadsheet-errors/

OR, if you spend time working with computers, you will find many reasons to 
mistrust people's use of them, too :-)

Pete.

-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 7)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2013-05-14T14:23:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com>`
- **In-Reply-To:** `<avda9eFf6ceU1@mid.individual.net>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net>`

```
On Tuesday, 14 May 2013 00:11:42 UTC+1, Pete Dashwood wrote:
> OR, if you spend time working with computers, you will find many reasons to 
> mistrust people's use of them, too :-) 

I have encountered the phrase "it's been produced by a computer so it must be true".
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-05-15T11:41:22+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avg0d5F303gU1@mid.individual.net>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net> <8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com>`

```
Alistair Maclean wrote:
> On Tuesday, 14 May 2013 00:11:42 UTC+1, Pete Dashwood wrote:
>> OR, if you spend time working with computers, you will find many
…[3 more quoted lines elided]…
> must be true".

Marshall MacLuhan famously said (back in the 1960s): "The media is the 
message."

I once did an experiement (and nearly got fired for it) where I  caused the 
figures in an account summary program to be ridiculously wrong. The green 
lineflo was subsequently presented to Directors and there was much wailing 
and gnashing of teeth...

ONLY ONE guy actually said:"This is insane, the computer must be wrong." The 
rest of them figured that if it was on green lineflo, it must be true.

I retained my job by the skin of my teeth because I was in my early 20s and 
my Boss wrote it off as a prank (which in a way it was), but it was made 
clear to me that such behaviour in the future would not be tolerated. (so 
much for my plans to produce the next lot of summaries in Roman numerals...)

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 9)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2013-05-15T03:10:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com>`
- **In-Reply-To:** `<avg0d5F303gU1@mid.individual.net>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net> <8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com> <avg0d5F303gU1@mid.individual.net>`

```
On Wednesday, 15 May 2013 00:41:22 UTC+1, Pete Dashwood wrote:
> so much for my plans to produce the next lot of summaries in Roman 
> numerals...) 

Yeah, like that. :-)

Did you ever write the (Cobol) code to do it? Roman numerals have been blamed for the demise of their empire. Does anyone know if the Romans ever had any great mathematicians?
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-05-15T23:39:16+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avhaf4FbiqoU1@mid.individual.net>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net> <8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com> <avg0d5F303gU1@mid.individual.net> <9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com>`

```
Alistair Maclean wrote:
> On Wednesday, 15 May 2013 00:41:22 UTC+1, Pete Dashwood wrote:
>> so much for my plans to produce the next lot of summaries in Roman
…[4 more quoted lines elided]…
> Did you ever write the (Cobol) code to do it?

No, but it really wouldn't be hard.

> Roman numerals have
> been blamed for the demise of their empire. Does anyone know if the
> Romans ever had any great mathematicians?

They had no zero.

I've often wondered about that. Not sure if it was a conceptual flaw or they 
just figured if you had nothing you didn't need to represent it.

Maybe some math historian can elucidate?

Pete.

-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 11)_

- **From:** Fred Mobach <fred@mobach.nl>
- **Date:** 2013-05-15T18:44:59+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5193bb8b$0$32107$14726298@news.sunsite.dk>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net> <8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com> <avg0d5F303gU1@mid.individual.net> <9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com> <avhaf4FbiqoU1@mid.individual.net>`

```
Pete Dashwood wrote:

> Alistair Maclean wrote:
>> On Wednesday, 15 May 2013 00:41:22 UTC+1, Pete Dashwood wrote:
…[17 more quoted lines elided]…
> it.

Romans were famous for engineering but not for mathematics as they
seemed to prefer practice instead of theory (which they left for the
Greeks).
-- 
Fred Mobach
website : https://fred.mobach.nl
 .... In God we trust ....
 .. The rest we monitor ..
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 11)_

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2013-05-15T13:03:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rej7p89h8cbbtbmaucjvmj7a9onsh20laq@4ax.com>`
- **References:** `<XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net> <8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com> <avg0d5F303gU1@mid.individual.net> <9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com> <avhaf4FbiqoU1@mid.individual.net>`

```
On Wed, 15 May 2013 23:39:16 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Alistair Maclean wrote:
>> On Wednesday, 15 May 2013 00:41:22 UTC+1, Pete Dashwood wrote:
…[18 more quoted lines elided]…
>Maybe some math historian can elucidate?


A decent overview of the history is at:

http://en.wikipedia.org/wiki/0_(number)
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-05-16T13:50:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avisc0FmcsqU1@mid.individual.net>`
- **References:** `<XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net> <8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com> <avg0d5F303gU1@mid.individual.net> <9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com> <avhaf4FbiqoU1@mid.individual.net> <rej7p89h8cbbtbmaucjvmj7a9onsh20laq@4ax.com>`

```
Robert Wessel wrote:
> On Wed, 15 May 2013 23:39:16 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[27 more quoted lines elided]…
> http://en.wikipedia.org/wiki/0_(number)

Thanks Robert.

The link as posted didn't work because the closing parenthesis was not 
included in the link.

However, it was pretty easy to redirect to the correct page and I found it 
interetsing.

Cheers,

Pete.

-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 10)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2013-05-15T18:38:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7o-dnSIeQaHxkwnMnZ2dnUVZ_radnZ2d@earthlink.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net> <8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com> <avg0d5F303gU1@mid.individual.net> <9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com>`

```

"Alistair Maclean" <alistair.j.l.maclean@gmail.com> wrote in message 
news:9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com...
> On Wednesday, 15 May 2013 00:41:22 UTC+1, Pete Dashwood wrote:
>> so much for my plans to produce the next lot of summaries in Roman
…[6 more quoted lines elided]…
> had any great mathematicians?

In college I  wrote a program that manipulated (I don't remember the details 
but I think I still have the listing) Roman numerials.  It was written in 
SNOBOL IV.
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-05-16T13:53:28+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avisgqFmds9U1@mid.individual.net>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net> <8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com> <avg0d5F303gU1@mid.individual.net> <9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com> <7o-dnSIeQaHxkwnMnZ2dnUVZ_radnZ2d@earthlink.com>`

```
Charles Hottel wrote:
> "Alistair Maclean" <alistair.j.l.maclean@gmail.com> wrote in message
> news:9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com...
…[12 more quoted lines elided]…
> was written in SNOBOL IV.

Whenever I see a reference to SNOBOL I get an image of a computer programmer 
with his nose in the air (snob) :-)

I know in the US they pronounce it like "snowball" but that isn't apparent 
from seeing it written down...

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 11)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2013-05-16T12:01:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37ce1c8c-7c33-4ead-80ab-1d41ec0e796a@googlegroups.com>`
- **In-Reply-To:** `<7o-dnSIeQaHxkwnMnZ2dnUVZ_radnZ2d@earthlink.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net> <8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com> <avg0d5F303gU1@mid.individual.net> <9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com> <7o-dnSIeQaHxkwnMnZ2dnUVZ_radnZ2d@earthlink.com>`

```
On Wednesday, 15 May 2013 23:38:56 UTC+1, Charles Hottel wrote:
> In college I wrote a program that manipulated (I don't remember the details 
> but I think I still have the listing) Roman numerials. It was written in 
> SNOBOL IV.

Ah, a language named after Lisa Simpson's cat.

Does SNOBOL bear any relation to COBOL?
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 12)_

- **From:** bill@server1.cs.uofs.edu (Bill Gunshannon)
- **Date:** 2013-05-16T19:20:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avkprhF4b4hU7@mid.individual.net>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net> <8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com> <avg0d5F303gU1@mid.individual.net> <9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com> <7o-dnSIeQaHxkwnMnZ2dnUVZ_radnZ2d@earthlink.com> <37ce1c8c-7c33-4ead-80ab-1d41ec0e796a@googlegroups.com>`

```
In article <37ce1c8c-7c33-4ead-80ab-1d41ec0e796a@googlegroups.com>,
	Alistair Maclean <alistair.j.l.maclean@gmail.com> writes:
> On Wednesday, 15 May 2013 23:38:56 UTC+1, Charles Hottel wrote:
>> In college I wrote a program that manipulated (I don't remember the details 
…[5 more quoted lines elided]…
> Does SNOBOL bear any relation to COBOL?

None whatsoever.

bill

-- 
Bill Gunshannon          |  de-moc-ra-cy (di mok' ra see) n.  Three wolves
billg999@cs.scranton.edu |  and a sheep voting on what's for dinner.
University of Scranton   |
Scranton, Pennsylvania   |         #include <std.disclaimer.h>
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 13)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2013-05-17T03:09:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<51d65c36-d453-4e51-91e3-3f2f1ba49056@googlegroups.com>`
- **In-Reply-To:** `<avkprhF4b4hU7@mid.individual.net>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net> <8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com> <avg0d5F303gU1@mid.individual.net> <9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com> <7o-dnSIeQaHxkwnMnZ2dnUVZ_radnZ2d@earthlink.com> <37ce1c8c-7c33-4ead-80ab-1d41ec0e796a@googlegroups.com> <avkprhF4b4hU7@mid.individual.net>`

```
Thanks Bill. Curiousity killed the cat but satisfaction....

Bill Gunshannon wrote:
> > AJM wrote: Does SNOBOL bear any relation to COBOL? 
> None whatsoever. bill
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 12)_

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2013-05-16T12:27:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fb115811-db74-4ad8-91ad-260ccb0f5ba6@googlegroups.com>`
- **In-Reply-To:** `<37ce1c8c-7c33-4ead-80ab-1d41ec0e796a@googlegroups.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net> <8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com> <avg0d5F303gU1@mid.individual.net> <9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com> <7o-dnSIeQaHxkwnMnZ2dnUVZ_radnZ2d@earthlink.com> <37ce1c8c-7c33-4ead-80ab-1d41ec0e796a@googlegroups.com>`

```
On Thursday, May 16, 2013 3:01:35 PM UTC-4, Alistair Maclean wrote:
[snip]
> Does SNOBOL bear any relation to COBOL?

Not as a language, however Micro Focus used SNOBOL in 1976
to produce a working COBOL compiler.

"The development of the COBOL compilers began with an extremely
simple COBOL compiler, for internal use, written in the Snobol
language. This compiler accepted only a small sub-set of COBOL,
but this was sufficient to compile a more advanced version of
COBOL. By repeatedly using the current COBOL compiler to compile
a more advanced version, a compiler suitable for marketing was
produced. ..."
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 13)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2013-05-16T18:56:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e26a7d43-097b-420c-892c-f2c167fa84f9@pd6g2000pbc.googlegroups.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net> <8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com> <avg0d5F303gU1@mid.individual.net> <9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com> <7o-dnSIeQaHxkwnMnZ2dnUVZ_radnZ2d@earthlink.com> <37ce1c8c-7c33-4ead-80ab-1d41ec0e796a@googlegroups.com> <fb115811-db74-4ad8-91ad-260ccb0f5ba6@googlegroups.com>`

```
On May 17, 7:27 am, Rick Smith <rs847...@gmail.com> wrote:
> On Thursday, May 16, 2013 3:01:35 PM UTC-4, Alistair Maclean wrote:
>
…[13 more quoted lines elided]…
> produced. ..."

My understanding is that in 1976 the founders of Microfocus were
working for ICL DataSkill in Bridge House, Reading writing a subset
COBOL compiler and runtime system for the ICL 1500 (ex Cogar/Singer)
desktop networked computers.

Later they formed MF and released a much upgraded system as CIS COBOL.

I still have some 1500s here somewhere and a manual for the COBOL
subset. There are probably some mini-tapes with this software here,
but condition completely unknown. CIS COBOL was later implemented for
ICL on the DRS20 system which replaced the 1500 series. I still have
some DRS20s here too, Models 10, 20, 40, 50. I used CIS COBOL
extensively on DRS20, CP/M and Concrrent-CP/M-86 (and later).
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 14)_

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2013-05-16T23:47:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46565f08-5d8e-47c1-b88b-5a56b6255dab@googlegroups.com>`
- **In-Reply-To:** `<e26a7d43-097b-420c-892c-f2c167fa84f9@pd6g2000pbc.googlegroups.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net> <8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com> <avg0d5F303gU1@mid.individual.net> <9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com> <7o-dnSIeQaHxkwnMnZ2dnUVZ_radnZ2d@earthlink.com> <37ce1c8c-7c33-4ead-80ab-1d41ec0e796a@googlegroups.com> <fb115811-db74-4ad8-91ad-260ccb0f5ba6@googlegroups.com> <e26a7d43-097b-420c-892c-f2c167fa84f9@pd6g2000pbc.googlegroups.com>`

```
On Thursday, May 16, 2013 9:56:58 PM UTC-4, Richard wrote:
> On May 17, 7:27 am, Rick Smith <rs847...@gmail.com> wrote:
> > On Thursday, May 16, 2013 3:01:35 PM UTC-4, Alistair Maclean wrote:
…[28 more quoted lines elided]…
> extensively on DRS20, CP/M and Concrrent-CP/M-86 (and later).

My source is: Alan D. T. Fryer, "COBOL on Microcomputers", 1984.
Fryer was a member of, and represented Micro Focus on, the CODASYL
COBOL Committee. I got the book when I purchased Personal COBOL 1.0.
In Appendix G, "History of Micro Focus", he writes, "Micro Focus was
founded in 1976 in England by Brian Reynolds and Paul O'Grady."

What it does not say is where the SNOBOL interpreter was located.
It may have been on an ICL machine or C/PM or some other. I did
make the modest assumption that, having founded Micro Focus in 1976,
they began developing with SNOBOL the same year.
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 13)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2013-05-17T03:13:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9d3a9ef0-2d08-4f7c-9149-ff01779a5472@googlegroups.com>`
- **In-Reply-To:** `<fb115811-db74-4ad8-91ad-260ccb0f5ba6@googlegroups.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net> <8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com> <avg0d5F303gU1@mid.individual.net> <9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com> <7o-dnSIeQaHxkwnMnZ2dnUVZ_radnZ2d@earthlink.com> <37ce1c8c-7c33-4ead-80ab-1d41ec0e796a@googlegroups.com> <fb115811-db74-4ad8-91ad-260ccb0f5ba6@googlegroups.com>`

```
On Thursday, 16 May 2013 20:27:33 UTC+1, Rick Smith wrote:
>> Alistair Maclean wrote: [snip] 
>> Does SNOBOL bear any relation to COBOL? 


> Not as a language, however Micro Focus used SNOBOL in 1976 
> to produce a working COBOL compiler. 
…[6 more quoted lines elided]…
> produced. ..."

Reminds me of some of the blurb for UFO (a 4GL called User Files Online) which said that it had been written by using UFO (a previous version).
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-05-17T11:41:08+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avl94lF85a0U1@mid.individual.net>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net> <8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com> <avg0d5F303gU1@mid.individual.net> <9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com> <7o-dnSIeQaHxkwnMnZ2dnUVZ_radnZ2d@earthlink.com> <37ce1c8c-7c33-4ead-80ab-1d41ec0e796a@googlegroups.com>`

```
Alistair Maclean wrote:
> On Wednesday, 15 May 2013 23:38:56 UTC+1, Charles Hottel wrote:
>> In college I wrote a program that manipulated (I don't remember the
…[5 more quoted lines elided]…
> Does SNOBOL bear any relation to COBOL?

I note in passing (as one of the little coincidences that the Universe never 
ceases to amaze me with) that Yeardley Smith (the French born American 
actress who is the voice of Lisa Simpson) will be attending the Armageddon 
Expo in Hamilton, NZ (a little over an hour's drive from where I am writing 
this) tomorrow, Saturday.  I almost went but I have some other things to do 
this weekend. A good friend of mine is going to both the Hamilton and 
Wellington conventions and she tells me they are always worth a visit. (She 
writes Fantasy stories for kids so it is a chance to promote her work).

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 13)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2013-05-17T03:18:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c17f44fa-2fcc-48a0-a77e-99ad4f066791@googlegroups.com>`
- **In-Reply-To:** `<avl94lF85a0U1@mid.individual.net>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net> <8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com> <avg0d5F303gU1@mid.individual.net> <9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com> <7o-dnSIeQaHxkwnMnZ2dnUVZ_radnZ2d@earthlink.com> <37ce1c8c-7c33-4ead-80ab-1d41ec0e796a@googlegroups.com> <avl94lF85a0U1@mid.individual.net>`

```
On Friday, 17 May 2013 00:41:08 UTC+1, Pete Dashwood wrote:
> I note in passing (as one of the little coincidences that the Universe 
> never ceases to amaze me with) that Yeardley Smith (the French born 
> American actress who is the voice of Lisa Simpson) will be attending 
> the Armageddon Expo in Hamilton, NZ. 

I've never dragged my self to any fan fest but was amused to see the news item about Star Wars fans fighting with Dr Who Fans:

http://www.bbc.co.uk/news/uk-england-norfolk-22542222
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 12)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2013-05-16T23:53:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BbmdnZwRgsQoNAjMnZ2dnUVZ_h6dnZ2d@earthlink.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net> <8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com> <avg0d5F303gU1@mid.individual.net> <9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com> <7o-dnSIeQaHxkwnMnZ2dnUVZ_radnZ2d@earthlink.com> <37ce1c8c-7c33-4ead-80ab-1d41ec0e796a@googlegroups.com>`

```

"Alistair Maclean" <alistair.j.l.maclean@gmail.com> wrote in message 
news:37ce1c8c-7c33-4ead-80ab-1d41ec0e796a@googlegroups.com...
> On Wednesday, 15 May 2013 23:38:56 UTC+1, Charles Hottel wrote:
>> In college I wrote a program that manipulated (I don't remember the 
…[6 more quoted lines elided]…
> Does SNOBOL bear any relation to COBOL?

Not really, it is/was primarily a string manipulation language.
```

###### ↳ ↳ ↳ Re: Inaccurate math results in Micro Focus Unix

_(reply depth: 13)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2013-05-17T03:19:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ae385945-9bb2-4ff7-8ec0-63f0a5b39976@googlegroups.com>`
- **In-Reply-To:** `<BbmdnZwRgsQoNAjMnZ2dnUVZ_h6dnZ2d@earthlink.com>`
- **References:** `<599b5508-65a7-43df-bc9f-0b92c1e511d9@googlegroups.com> <XnsA1BE7CD2C7A2Fdougmilmaccom@78.46.70.116> <kmofv5$3a6$4@solani.org> <f24e37db-bfeb-43fe-91cb-c9718f1fafa4@a10g2000pbr.googlegroups.com> <avbi01F2gk9U1@mid.individual.net> <a6b4e50e-5607-4582-91b2-71ebfb70f750@googlegroups.com> <avda9eFf6ceU1@mid.individual.net> <8fa4a60d-0ce8-4ff4-9506-4f9638f46559@googlegroups.com> <avg0d5F303gU1@mid.individual.net> <9f8cb2bb-959a-44ed-a8c2-6fcfed4e32cb@googlegroups.com> <7o-dnSIeQaHxkwnMnZ2dnUVZ_radnZ2d@earthlink.com> <37ce1c8c-7c33-4ead-80ab-1d41ec0e796a@googlegroups.com> <BbmdnZwRgsQoNAjMnZ2dnUVZ_h6dnZ2d@earthlink.com>`

```
On Friday, 17 May 2013 04:53:48 UTC+1, Charles Hottel wrote:
> > Does SNOBOL bear any relation to COBOL? 
> Not really, it is/was primarily a string manipulation language.

Thanks to all who responded to my query.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
