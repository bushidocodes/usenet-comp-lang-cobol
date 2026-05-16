[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Rounding

_83 messages · 15 participants · 2011-01 → 2011-02_

---

### Rounding

- **From:** jmoore <jmoore207@gmail.com>
- **Date:** 2011-01-18T04:15:51-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com>`

```
What is the best way to round up 4.88 to 4.9 and not 5. The input
comes in as 2 decimals but is being moved to a 9(7)v9 field.
```

#### ↳ Re: Rounding

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2011-01-18T12:49:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ih429k$reg$1@news.eternal-september.org>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com>`

```
In article <c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com>, jmoore <jmoore207@gmail.com> wrote:
>What is the best way to round up 4.88 to 4.9 and not 5. The input
>comes in as 2 decimals but is being moved to a 9(7)v9 field.

COMPUTE nine-seven-vee-nine = nine-seven-vee-nine-nine ROUNDED.
```

##### ↳ ↳ Re: Rounding

- **From:** jmoore <jmoore207@gmail.com>
- **Date:** 2011-01-18T05:26:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<655c78d6-d2b0-4500-a152-caf0bbedaa97@o14g2000yqe.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <ih429k$reg$1@news.eternal-september.org>`

```
On Jan 18, 7:49 am, spamb...@milmac.com (Doug Miller) wrote:
> In article <c0d054fb-8b4e-4a97-b299-ef153d4fc...@32g2000yqz.googlegroups.com>, jmoore <jmoore...@gmail.com> wrote:
>
…[3 more quoted lines elided]…
> COMPUTE nine-seven-vee-nine = nine-seven-vee-nine-nine ROUNDED.

Thanks, I will try that!
```

##### ↳ ↳ Re: Rounding

- **From:** jmoore <jmoore207@gmail.com>
- **Date:** 2011-01-18T05:26:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d80f247c-39f8-4f26-ad25-e90e44b0e4c5@n11g2000yqh.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <ih429k$reg$1@news.eternal-september.org>`

```
On Jan 18, 7:49 am, spamb...@milmac.com (Doug Miller) wrote:
> In article <c0d054fb-8b4e-4a97-b299-ef153d4fc...@32g2000yqz.googlegroups.com>, jmoore <jmoore...@gmail.com> wrote:
>
…[3 more quoted lines elided]…
> COMPUTE nine-seven-vee-nine = nine-seven-vee-nine-nine ROUNDED.

Thanks! I will try it!
```

###### ↳ ↳ ↳ Re: Rounding

- **From:** jmoore <jmoore207@gmail.com>
- **Date:** 2011-01-18T06:03:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<864c9911-0dfd-4283-ad63-342df2b41102@f2g2000vby.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <ih429k$reg$1@news.eternal-september.org> <d80f247c-39f8-4f26-ad25-e90e44b0e4c5@n11g2000yqh.googlegroups.com>`

```
On Jan 18, 8:26 am, jmoore <jmoore...@gmail.com> wrote:
> On Jan 18, 7:49 am, spamb...@milmac.com (Doug Miller) wrote:
>
…[7 more quoted lines elided]…
> Thanks! I will try it!

Thanks. The syntax was wrong.

COMPUTE nine-seven-vee-nine ROUNDED = nine-seven-vee-nine-nine.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 4)_

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2011-01-18T19:39:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ih4q9n$nrr$1@news.eternal-september.org>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <ih429k$reg$1@news.eternal-september.org> <d80f247c-39f8-4f26-ad25-e90e44b0e4c5@n11g2000yqh.googlegroups.com> <864c9911-0dfd-4283-ad63-342df2b41102@f2g2000vby.googlegroups.com>`

```
In article <864c9911-0dfd-4283-ad63-342df2b41102@f2g2000vby.googlegroups.com>, jmoore <jmoore207@gmail.com> wrote:
>On Jan 18, 8:26=A0am, jmoore <jmoore...@gmail.com> wrote:
>> On Jan 18, 7:49=A0am, spamb...@milmac.com (Doug Miller) wrote:
…[13 more quoted lines elided]…
>COMPUTE nine-seven-vee-nine ROUNDED = nine-seven-vee-nine-nine.

Sorry, my fault -- you're right.
```

##### ↳ ↳ Re: Rounding

- **From:** "robin" <robin51@dodo.mapson.com.au>
- **Date:** 2011-01-24T22:13:12+11:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<4d3d6919$0$88227$c30e37c6@exi-reader.telstra.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <ih429k$reg$1@news.eternal-september.org>`

```

"Doug Miller" <spambait@milmac.com> wrote in message news:ih429k$reg$1@news.eternal-september.org...
| In article <c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com>, jmoore <jmoore207@gmail.com> wrote:
| >What is the best way to round up 4.88 to 4.9 and not 5. The input
| >comes in as 2 decimals but is being moved to a 9(7)v9 field.
|
| COMPUTE nine-seven-vee-nine = nine-seven-vee-nine-nine ROUNDED.

In PL/I, it's Y = ROUND(X, 1);
```

#### ↳ Re: Rounding

- **From:** docdwarf@panix.com ()
- **Date:** 2011-01-18T14:34:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ih48di$qtu$1@reader1.panix.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com>`

```
In article <c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com>,
jmoore  <jmoore207@gmail.com> wrote:
>What is the best way to round up 4.88 to 4.9 and not 5. The input
>comes in as 2 decimals but is being moved to a 9(7)v9 field.

It might be interesting to see what you have tried already and learn the 
reasons you've concluded that your method is not 'the best way'.

DD
```

#### ↳ Re: Rounding

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2011-01-18T08:20:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pmbbj6d7dbnkjcu8pkt575t5fgkaqskitm@4ax.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com>`

```
On Tue, 18 Jan 2011 04:15:51 -0800 (PST), jmoore <jmoore207@gmail.com>
wrote:

>What is the best way to round up 4.88 to 4.9 and not 5. The input
>comes in as 2 decimals but is being moved to a 9(7)v9 field.

The first thing you need to establish is what your users want.   While
there are accounting standards, they may or may not apply to your
needs.     

Hopefully COMPUTE ROUNDED will give you what you want.   But you've
got to understand your data.   

What do you want 4.85 to round to?
What do you want 4.75 to round to?
```

##### ↳ ↳ Re: Rounding

- **From:** Kerry Liles <"kerry.liles[minus_the_spam]"@gmail.com>
- **Date:** 2011-01-18T10:40:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ih4c7h$aph$1@news.eternal-september.org>`
- **In-Reply-To:** `<pmbbj6d7dbnkjcu8pkt575t5fgkaqskitm@4ax.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <pmbbj6d7dbnkjcu8pkt575t5fgkaqskitm@4ax.com>`

```
On 1/18/2011 10:20 AM, Howard Brazee wrote:
> On Tue, 18 Jan 2011 04:15:51 -0800 (PST), jmoore<jmoore207@gmail.com>
> wrote:
…[13 more quoted lines elided]…
>

And don't forget rounding negative numbers...

What do you want -4.85 and -4.75 to round to?!

I would love to find a reference to a clear statement of how 'rounding' 
*ought to work*
  - for positive and negative values;
  - for discarded digits of all sorts - especially "5",
    (some people argue 4.451 should be rounded to 4.5
     "because" the .051 is greater than .050)
  - for individual values to be rounded
  - for a set of numbers to be rounded yet still total to (say) 100
(I believe the last case is sometimes referred to as "distributed 
rounding" according to some sources eg: rounding a set of percentages 
that must total 100)
```

###### ↳ ↳ ↳ Re: Rounding

- **From:** Kerry Liles <"kerry.liles[minus_the_spam]"@gmail.com>
- **Date:** 2011-01-18T11:08:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ih4dt2$6sk$1@news.eternal-september.org>`
- **In-Reply-To:** `<ih4c7h$aph$1@news.eternal-september.org>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <pmbbj6d7dbnkjcu8pkt575t5fgkaqskitm@4ax.com> <ih4c7h$aph$1@news.eternal-september.org>`

```
On 1/18/2011 10:40 AM, Kerry Liles wrote:
> On 1/18/2011 10:20 AM, Howard Brazee wrote:
>> On Tue, 18 Jan 2011 04:15:51 -0800 (PST), jmoore<jmoore207@gmail.com>
…[32 more quoted lines elided]…
>

Sad to be answering my own question, but I did find some interesting 
info here: http://en.wikipedia.org/wiki/Rounding   (Duh)

and here: http://www.diycalculator.com/popup-m-round.shtml

... currently chasing links from those places too.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 4)_

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2011-01-18T09:07:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d41498b8-efb2-4196-b3c7-aa7136284a9f@y31g2000vbt.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <pmbbj6d7dbnkjcu8pkt575t5fgkaqskitm@4ax.com> <ih4c7h$aph$1@news.eternal-september.org> <ih4dt2$6sk$1@news.eternal-september.org>`

```
On Jan 18, 4:08 pm, Kerry Liles
<"kerry.liles[minus_the_spam]"@gmail.com> wrote:
> On 1/18/2011 10:40 AM, Kerry Liles wrote:
>
…[39 more quoted lines elided]…
>

Saves Doc Dwarf from having to regale you with his usual missive (used
elsewhere in this thread).
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 5)_

- **From:** Kerry Liles <"kerry.liles[minus_the_spam]"@gmail.com>
- **Date:** 2011-01-18T13:01:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ih4kgh$tv$1@news.eternal-september.org>`
- **In-Reply-To:** `<d41498b8-efb2-4196-b3c7-aa7136284a9f@y31g2000vbt.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <pmbbj6d7dbnkjcu8pkt575t5fgkaqskitm@4ax.com> <ih4c7h$aph$1@news.eternal-september.org> <ih4dt2$6sk$1@news.eternal-september.org> <d41498b8-efb2-4196-b3c7-aa7136284a9f@y31g2000vbt.googlegroups.com>`

```
On 1/18/2011 12:07 PM, Alistair Maclean wrote:
> On Jan 18, 4:08 pm, Kerry Liles
> <"kerry.liles[minus_the_spam]"@gmail.com>  wrote:
…[44 more quoted lines elided]…
> elsewhere in this thread).

I'm always pleased to NOT provoke Doc et al.    :)
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 6)_

- **From:** Anonymous <nobody@remailer.paranoici.org>
- **Date:** 2011-01-18T21:27:54+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f84fd103cbdef9c9a99ac251ff9eab7e@remailer.paranoici.org>`
- **References:** `<ih4kgh$tv$1@news.eternal-september.org>`

```
> I'm always pleased to NOT provoke Doc et al.    :)

Or just do what I do, killfile the arrogant bastard! Problem solved :-)
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 6)_

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2011-01-18T14:29:20-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6286c328-6b5a-4596-b6b3-cbf25b57a0f5@m35g2000vbn.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <pmbbj6d7dbnkjcu8pkt575t5fgkaqskitm@4ax.com> <ih4c7h$aph$1@news.eternal-september.org> <ih4dt2$6sk$1@news.eternal-september.org> <d41498b8-efb2-4196-b3c7-aa7136284a9f@y31g2000vbt.googlegroups.com> <ih4kgh$tv$1@news.eternal-september.org>`

```
On Jan 18, 6:01 pm, Kerry Liles
<"kerry.liles[minus_the_spam]"@gmail.com> wrote:
> On 1/18/2011 12:07 PM, Alistair Maclean wrote:
>
…[48 more quoted lines elided]…
>

Best to let sleeping Docs lie.
```

#### ↳ Re: Rounding

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-19T17:21:54+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pn774FcdhU1@mid.individual.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com>`

```
jmoore wrote:
> What is the best way to round up 4.88 to 4.9 and not 5. The input
> comes in as 2 decimals but is being moved to a 9(7)v9 field.

I don't know the BEST way (but I try to avoid using ROUNDED in COBOL because 
it behaves differently on different platforms and depending on what compiler 
options are in effect), but I would do it as follows:

01 in-field  pic s9(7)v99.

01 rounded-field  pic s9(7)v9.

     compute rounded-field = in-field + .05

That'll work on any platform...

Pete.
```

##### ↳ ↳ Re: Rounding

- **From:** jmoore <jmoore207@gmail.com>
- **Date:** 2011-01-19T04:01:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f7ccaf00-29e6-41cc-b78f-346cb414a1dc@k30g2000vbn.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net>`

```
On Jan 18, 11:21 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> jmoore wrote:
> > What is the best way to round up 4.88 to 4.9 and not 5. The input
…[16 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."

Thanks Pete! I tried that as well, but I am getting some strange
results. In my displays the incoming field (in-field) is 004.88. when
I compute rounded-field the display is 00006088. Very odd. Thanks for
responding.
```

###### ↳ ↳ ↳ Re: Rounding

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2011-01-19T07:29:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c33c074c-d7f7-4d2a-ba79-1ea181c4dfa4@q18g2000vbk.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <f7ccaf00-29e6-41cc-b78f-346cb414a1dc@k30g2000vbn.googlegroups.com>`

```
On Jan 19, 12:01 pm, jmoore <jmoore...@gmail.com> wrote:
> On Jan 18, 11:21 pm, "Pete Dashwood"
> Thanks Pete! I tried that as well, but I am getting some strange
…[3 more quoted lines elided]…
>
That shouldn't be happening. Please post the field definitions and the
code you use with the result that you get. Also-----what compiler are
you using to get these results?
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 4)_

- **From:** jmoore <jmoore207@gmail.com>
- **Date:** 2011-01-19T09:38:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<24819f45-d095-470f-97b8-6ca62110dba0@fm22g2000vbb.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <f7ccaf00-29e6-41cc-b78f-346cb414a1dc@k30g2000vbn.googlegroups.com> <c33c074c-d7f7-4d2a-ba79-1ea181c4dfa4@q18g2000vbk.googlegroups.com>`

```
On Jan 19, 10:29 am, Alistair Maclean
<alistair.j.l.macl...@googlemail.com> wrote:
> On Jan 19, 12:01 pm, jmoore <jmoore...@gmail.com> wrote:> On Jan 18, 11:21 pm, "Pete Dashwood"
> > Thanks Pete! I tried that as well, but I am getting some strange
…[6 more quoted lines elided]…
> you using to get these results?

I fixed this part with a simple select round statement. I still have a
weird issue on compute tho. Thanks for everyone's input. I have new
issue now where I may have to divide the field by 2 or 3 depending a
switch and I am not getting what I would expect. I am not sure what
the compiler is. We use Micro-Focus Cobol in a unix environment with
Oracle Database. The compiler uses pro*Cobol. All of our programs have
embedded sql. Here is how the incoming field is defined and all of the
variables.

(lmkvas-d is the variable fetched into from oracle)
01 lmkvas-d    pic x(05).
01 lmkvas     redefines
   lmkvas-d    pic 9(03)v99.

01 ws-kvas-d    pic x(05).
01 ws-kvas     redefines
   ws-kvas-d    pic 9(03)v99.

         compute ws-kvas = lmkvas / 2.
display "ws-kvas " ws-kvas     07045      I was expecting this to be
6.45
display "lmkvas " lmkvas       12.90
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 5)_

- **From:** jmoore <jmoore207@gmail.com>
- **Date:** 2011-01-19T09:45:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<458428a3-7319-4fda-ad7b-66d4d79fd599@u3g2000vbj.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <f7ccaf00-29e6-41cc-b78f-346cb414a1dc@k30g2000vbn.googlegroups.com> <c33c074c-d7f7-4d2a-ba79-1ea181c4dfa4@q18g2000vbk.googlegroups.com> <24819f45-d095-470f-97b8-6ca62110dba0@fm22g2000vbb.googlegroups.com>`

```
On Jan 19, 12:38 pm, jmoore <jmoore...@gmail.com> wrote:
> On Jan 19, 10:29 am, Alistair Maclean
>
…[32 more quoted lines elided]…
> display "lmkvas " lmkvas       12.90




Sorry I think I am on the right track now. I ran it through function
numval. Thanks everyone!
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 6)_

- **From:** Kerry Liles <"kerry.liles[minus_the_spam]"@gmail.com>
- **Date:** 2011-01-19T13:39:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ih7b3q$a61$1@news.eternal-september.org>`
- **In-Reply-To:** `<458428a3-7319-4fda-ad7b-66d4d79fd599@u3g2000vbj.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <f7ccaf00-29e6-41cc-b78f-346cb414a1dc@k30g2000vbn.googlegroups.com> <c33c074c-d7f7-4d2a-ba79-1ea181c4dfa4@q18g2000vbk.googlegroups.com> <24819f45-d095-470f-97b8-6ca62110dba0@fm22g2000vbb.googlegroups.com> <458428a3-7319-4fda-ad7b-66d4d79fd599@u3g2000vbj.googlegroups.com>`

```
On 1/19/2011 12:45 PM, jmoore wrote:
> On Jan 19, 12:38 pm, jmoore<jmoore...@gmail.com>  wrote:
>> On Jan 19, 10:29 am, Alistair Maclean
…[39 more quoted lines elided]…
> numval. Thanks everyone!

Never mind what the pic x variable says, why dont you just display the 
pic 9 variable? By the way, you can avoid the ugly redefines:

05 ws-kvas-x.
    10 ws-kvas-d  pic 9(3)v99.

(Group items are always treated as pic x)

good luck.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 7)_

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2011-01-19T12:13:35-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f13939c-cf4a-4cbe-a4c7-ddd88a6d3c72@q35g2000vbb.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <f7ccaf00-29e6-41cc-b78f-346cb414a1dc@k30g2000vbn.googlegroups.com> <c33c074c-d7f7-4d2a-ba79-1ea181c4dfa4@q18g2000vbk.googlegroups.com> <24819f45-d095-470f-97b8-6ca62110dba0@fm22g2000vbb.googlegroups.com> <458428a3-7319-4fda-ad7b-66d4d79fd599@u3g2000vbj.googlegroups.com> <ih7b3q$a61$1@news.eternal-september.org>`

```
On Jan 19, 6:39 pm, Kerry Liles
<"kerry.liles[minus_the_spam]"@gmail.com> wrote:
> On 1/19/2011 12:45 PM, jmoore wrote:
>
…[54 more quoted lines elided]…
> - Show quoted text -

Except where:

 05 ws-kvas-x  pic 9(3)v99.
     10 ws-kvas-d.

Or am  I going potty?
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 8)_

- **From:** Kerry Liles <"kerry.liles[minus_the_spam]"@gmail.com>
- **Date:** 2011-01-19T15:48:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ih7ikv$4b4$1@news.eternal-september.org>`
- **In-Reply-To:** `<3f13939c-cf4a-4cbe-a4c7-ddd88a6d3c72@q35g2000vbb.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <f7ccaf00-29e6-41cc-b78f-346cb414a1dc@k30g2000vbn.googlegroups.com> <c33c074c-d7f7-4d2a-ba79-1ea181c4dfa4@q18g2000vbk.googlegroups.com> <24819f45-d095-470f-97b8-6ca62110dba0@fm22g2000vbb.googlegroups.com> <458428a3-7319-4fda-ad7b-66d4d79fd599@u3g2000vbj.googlegroups.com> <ih7b3q$a61$1@news.eternal-september.org> <3f13939c-cf4a-4cbe-a4c7-ddd88a6d3c72@q35g2000vbb.googlegroups.com>`

```
On 1/19/2011 3:13 PM, Alistair Maclean wrote:
> On Jan 19, 6:39 pm, Kerry Liles
> <"kerry.liles[minus_the_spam]"@gmail.com>  wrote:
…[63 more quoted lines elided]…
> Or am  I going potty?

potty it is. Your example is not legal syntax afaik.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 9)_

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2011-01-19T13:02:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1bd19093-e730-4f21-a3b8-9015cef5c203@g26g2000vbi.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <f7ccaf00-29e6-41cc-b78f-346cb414a1dc@k30g2000vbn.googlegroups.com> <c33c074c-d7f7-4d2a-ba79-1ea181c4dfa4@q18g2000vbk.googlegroups.com> <24819f45-d095-470f-97b8-6ca62110dba0@fm22g2000vbb.googlegroups.com> <458428a3-7319-4fda-ad7b-66d4d79fd599@u3g2000vbj.googlegroups.com> <ih7b3q$a61$1@news.eternal-september.org> <3f13939c-cf4a-4cbe-a4c7-ddd88a6d3c72@q35g2000vbb.googlegroups.com> <ih7ikv$4b4$1@news.eternal-september.org>`

```
On Jan 19, 8:48 pm, Kerry Liles
<"kerry.liles[minus_the_spam]"@gmail.com> wrote:
> On 1/19/2011 3:13 PM, Alistair Maclean wrote:
>
…[69 more quoted lines elided]…
> - Show quoted text -

When I last checked, any clause applicable at the data-item level
could be placed on a group-item.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 10)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2011-01-19T16:29:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4D371183.6F0F.0085.0@efirstbank.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <f7ccaf00-29e6-41cc-b78f-346cb414a1dc@k30g2000vbn.googlegroups.com> <c33c074c-d7f7-4d2a-ba79-1ea181c4dfa4@q18g2000vbk.googlegroups.com> <24819f45-d095-470f-97b8-6ca62110dba0@fm22g2000vbb.googlegroups.com> <458428a3-7319-4fda-ad7b-66d4d79fd599@u3g2000vbj.googlegroups.com> <ih7b3q$a61$1@news.eternal-september.org> <3f13939c-cf4a-4cbe-a4c7-ddd88a6d3c72@q35g2000vbb.googlegroups.com> <ih7ikv$4b4$1@news.eternal-september.org> <1bd19093-e730-4f21-a3b8-9015cef5c203@g26g2000vbi.googlegroups.com>`

```
>>> On 1/19/2011 at 2:02 PM, in message
<1bd19093-e730-4f21-a3b8-9015cef5c203@g26g2000vbi.googlegroups.com>,
Alistair Maclean<alistair.j.l.maclean@googlemail.com> wrote:
> 
> When I last checked, any clause applicable at the data-item level
> could be placed on a group-item.

From ISO/IEC 1989:2002(E): "The PICTURE clause may be specified only at the
elementary level."
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 11)_

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2011-01-20T03:30:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<780d0841-ad8e-43f4-8cd1-10421fd0e365@fu15g2000vbb.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <f7ccaf00-29e6-41cc-b78f-346cb414a1dc@k30g2000vbn.googlegroups.com> <c33c074c-d7f7-4d2a-ba79-1ea181c4dfa4@q18g2000vbk.googlegroups.com> <24819f45-d095-470f-97b8-6ca62110dba0@fm22g2000vbb.googlegroups.com> <458428a3-7319-4fda-ad7b-66d4d79fd599@u3g2000vbj.googlegroups.com> <ih7b3q$a61$1@news.eternal-september.org> <3f13939c-cf4a-4cbe-a4c7-ddd88a6d3c72@q35g2000vbb.googlegroups.com> <ih7ikv$4b4$1@news.eternal-september.org> <1bd19093-e730-4f21-a3b8-9015cef5c203@g26g2000vbi.googlegroups.com> <4D371183.6F0F.0085.0@efirstbank.com>`

```
On Jan 19, 11:29 pm, "Frank Swarbrick"
<Frank.Swarbr...@efirstbank.com> wrote:
> >>> On 1/19/2011 at 2:02 PM, in message
>
…[8 more quoted lines elided]…
> elementary level."

Thanks. So I was going potty.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 10)_

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2011-01-20T00:25:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FzQZo.548881$Qg.458218@en-nntp-04.dc1.easynews.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <f7ccaf00-29e6-41cc-b78f-346cb414a1dc@k30g2000vbn.googlegroups.com> <c33c074c-d7f7-4d2a-ba79-1ea181c4dfa4@q18g2000vbk.googlegroups.com> <24819f45-d095-470f-97b8-6ca62110dba0@fm22g2000vbb.googlegroups.com> <458428a3-7319-4fda-ad7b-66d4d79fd599@u3g2000vbj.googlegroups.com> <ih7b3q$a61$1@news.eternal-september.org> <3f13939c-cf4a-4cbe-a4c7-ddd88a6d3c72@q35g2000vbb.googlegroups.com> <ih7ikv$4b4$1@news.eternal-september.org> <1bd19093-e730-4f21-a3b8-9015cef5c203@g26g2000vbi.googlegroups.com>`

```

"Alistair Maclean" <alistair.j.l.maclean@googlemail.com> wrote in message 
news:1bd19093-e730-4f21-a3b8-
<snip>
> When I last checked, any clause applicable at the data-item level
> could be placed on a group-item.

NOPE,
  Lots of clauses are only valid at the elementary level.  (Some compilers 
allow SOME at group levels as extensions and some may be used at either 
level in the Standard)
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 8)_

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2011-01-20T15:29:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ih9kcp$h1d$1@news.eternal-september.org>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <f7ccaf00-29e6-41cc-b78f-346cb414a1dc@k30g2000vbn.googlegroups.com> <c33c074c-d7f7-4d2a-ba79-1ea181c4dfa4@q18g2000vbk.googlegroups.com> <24819f45-d095-470f-97b8-6ca62110dba0@fm22g2000vbb.googlegroups.com> <458428a3-7319-4fda-ad7b-66d4d79fd599@u3g2000vbj.googlegroups.com> <ih7b3q$a61$1@news.eternal-september.org> <3f13939c-cf4a-4cbe-a4c7-ddd88a6d3c72@q35g2000vbb.googlegroups.com>`

```
In article <3f13939c-cf4a-4cbe-a4c7-ddd88a6d3c72@q35g2000vbb.googlegroups.com>, Alistair Maclean <alistair.j.l.maclean@googlemail.com> wrote:

> 05 ws-kvas-x  pic 9(3)v99.
>     10 ws-kvas-d.
>
>Or am  I going potty?

Yes, you are. PICture clauses are not permitted on group items.
```

##### ↳ ↳ Re: Rounding

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2011-01-20T00:21:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net>`

```
Pete,
   Can you give me some examples of where ROUNDED works differently on 
different platforms?  You could mean that COMPUTE (with or without ROUNDED 
works differently on different platforms - and that is correct).  However, 
I don't think there any cases that I know of where COMPUTE withOUT rounded 
would give the same answer with two different compilers or two different 
platforms, but that adding ROUNDED would give different answers.

The rules for "determining" the result of a COMPUTE are implementor defined; 
the rules for what happens AFTER you get the result of the COMPUTE when you 
add ROUNDED is "well defined" (and portable - as far as I know).

The only POSSIBLE exception that I know of is for "implementor defined 
USAGEs".  I think that if you ROUND with floating-point data types you may 
get different results with different compilers.

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:8pn774FcdhU1@mid.individual.net...
> jmoore wrote:
>> What is the best way to round up 4.88 to 4.9 and not 5. The input
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Rounding

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-21T16:26:51+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pscnuF93uU1@mid.individual.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com>`

```
Bill Klein wrote:
> Pete,
>   Can you give me some examples of where ROUNDED works differently on
> different platforms?  You could mean that COMPUTE (with or without
> ROUNDED works differently on different platforms - and that is
> correct).

Yes, that is what I actually meant. I learned a long time ago, in different 
environments that rounded results were not always what I expected. I 
remember an NCR 315 running the same COBOL as an ICL 1900 and getting 
different ROUNDED results. I don't have the listings to hand (it was in the 
1960s) but I do remember making mental note to self: "If you want something 
rounded, do it yourself. There is no ambiguity about adding .5 and 
truncating."


However, I don't think there any cases that I know of
> where COMPUTE withOUT rounded would give the same answer with two
> different compilers or two different platforms, but that adding
> ROUNDED would give different answers.

How about 2 computes (on different machines) where one is subject to TRUNC 
and one is NOT? If you ROUND them you may get different answers...

How about a short floating point and a long floating point being ROUNDED? 
OK, sorry, I just noticed you exclued that below.

But I don't want exclusions and exceptions. I want ONE processs that a 
simple brain like mine can cope with. If I don't use ROUNDED (and I haven't 
for over 40 years) I don't have to worry about it. It is similar to the 
arguments about ODO. It is another pointless waste of time.


> The rules for "determining" the result of a COMPUTE are implementor
> defined; the rules for what happens AFTER you get the result of the
…[4 more quoted lines elided]…
> you may get different results with different compilers.

I'm sure you're right, Bill, but I like the simple life. I don't want to 
know all the nuances of the implications of all the legalese in every 
successive COBOL standard; I want something clear, simple, and easily 
remembered, that works. I'm afraid my approach has always been empirical 
rather than theoretical.

(No disrespect to people like yourself who don't necessarily work that 
way...)

Pete.
<unreferenced previous snipped>
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2011-01-20T20:57:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tv0ij6tl1tkjp371a1ajp3u0u5vn336u1m@4ax.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net>`

```
On Fri, 21 Jan 2011 16:26:51 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Yes, that is what I actually meant. I learned a long time ago, in different 
>environments that rounded results were not always what I expected. I 
…[4 more quoted lines elided]…
>truncating."

I couldn't agree more.   And if the accountants want a different
definition (I'd better check), then I can do it, make comments about
how and why I did it that way, and leave it for prosperity.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-01-21T13:50:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ihc2ul$u$1@reader1.panix.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net>`

```
In article <8pscnuF93uU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>Bill Klein wrote:
>> Pete,
…[11 more quoted lines elided]…
>truncating."

Leaving aside the dreaded Source of Idiosyncratic Standards reference here 
('well, about 40 - 50 years ago someone saw some kind of behavior they 
didn't like... nobody's kept any documentation on it but when that guy 
made it to a Corner Office it became part of our Site Standard') there 
might be a difficulty here with 'If you want something rounded...'

Just as different departments have had longstanding arguments about 
certain basic business concepts - ever been in the middle of 'Accounting 
says this report's wrong... now Inventory Management says the report's 
wrong'? - so might different folks have different understanding as to what 
constitutes 'rounding'.

There is no ambiguity about 'adding .5 and truncating' (assuming the same 
numeric base on all sides) but there are most definitely questions as to 
whether this approach constitutes what someone who signs my timesheets 
calls 'rounding'.

[snip]

>How about 2 computes (on different machines) where one is subject to TRUNC 
>and one is NOT? If you ROUND them you may get different answers...

One may not get different results, as well.  There are a few folks using 
this newsgroup who might have access to various computers on different 
machines; a request for assistance in gathering data might be in order.

[snip]

>But I don't want exclusions and exceptions. I want ONE processs that a 
>simple brain like mine can cope with.

If one gathers a bit of data, Mr Dashwood, one might learn that what one 
wants is an inaccurate representation of the possible set of results 
available.

DD
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-22T13:47:06+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8punodFd6kU1@mid.individual.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net> <ihc2ul$u$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <8pscnuF93uU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[20 more quoted lines elided]…
> something rounded...'

I have NEVER insisted that my personal coding preferences be ensconced as 
site standards ANYWHERE I have worked, even when I had the power to do so.

There have been several occasions in my life where I was tasked with 
formulating site standards and it was ALWAYS done by discussion and debate 
with the programming staff, NEVER arbitrarily "because I say so".

As for "If you want something rounded" the context was clear. We are talking 
about adding 2 real numbers together. Nothing more, nothing less.

ALL other meanings and definitions of "rounding" (and I agree there are many 
in a large and diverse organisation) have to be identified by discussion 
with the people concerned and appropriate program code developed to fit 
their requirements. Pretty basic stuff really, and I'm surprised you made an 
issue of it.



>
>> How about 2 computes (on different machines) where one is subject to
…[3 more quoted lines elided]…
> One may not get different results, as well.

Sure. The question was rhetorical. I don't care because I don't use ROUNDED 
in COBOL. (Ah, the freedom...)


>There are a few folks
> using this newsgroup who might have access to various computers on
> different machines; a request for assistance in gathering data might
> be in order.

Sure, let's waste more people's time (not to mention their company's 
computer time) in proving something that is completely irrelevant to 
anything.

I would (and have) ask for assistance from this group for things I actually 
care about.

Just being right for the sake of argument is not one of those things.

>
> [snip]
…[6 more quoted lines elided]…
> results available.

To a pessimist, certainly.

On the other hand, I find that I usually get what I want.

(The secret is in not having unrealistic expectations...)  I HAVE  a single 
simple process that solves the problem of rounding 2 real numbers for me.

And that was all I wanted.

Pete.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-01-22T02:11:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ihded2$shk$1@reader1.panix.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pscnuF93uU1@mid.individual.net> <ihc2ul$u$1@reader1.panix.com> <8punodFd6kU1@mid.individual.net>`

```
In article <8punodFd6kU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <8pscnuF93uU1@mid.individual.net>,
…[24 more quoted lines elided]…
>site standards ANYWHERE I have worked, even when I had the power to do so.

I don't believe that anything I wrote in the paragraph above was intended 
to convey that you did, Mr Dashwood... but it might never be that the 
laddie doth protest too much.


>As for "If you want something rounded" the context was clear. We are talking 
>about adding 2 real numbers together. Nothing more, nothing less.

In what's quoted above, Mr Dashwood, neither Mr Klein, you nor I sought to 
limit the number of things added to two real numbers until you mentioned 
it in the paragraph above.  If there's something I missed perhaps that 
might pointed out.

>ALL other meanings and definitions of "rounding" (and I agree there are many 
>in a large and diverse organisation) have to be identified by discussion 
>with the people concerned and appropriate program code developed to fit 
>their requirements. Pretty basic stuff really, and I'm surprised you made an 
>issue of it.

A moment of surprise might be a moment to learn, Mr Dashwood... try not to 
let one pass.

>>
>>> How about 2 computes (on different machines) where one is subject to
…[6 more quoted lines elided]…
>in COBOL. (Ah, the freedom...)

Restricting the amount of reserved words one chooses to use is freedom?  
Perhaps in the sense that maximum security is a prison.

>
>
…[7 more quoted lines elided]…
>anything.

Who needs facts when the mind is already made up?

>>> But I don't want exclusions and exceptions. I want ONE processs that
>>> a simple brain like mine can cope with.
…[5 more quoted lines elided]…
>To a pessimist, certainly.

To anyone who has learned something new after gathering a bit of data 
'pessimism' might be another thing, entire.

DD
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 6)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2011-01-24T09:46:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c73f222c-29a0-486d-8e65-7dcec89dd29b@e9g2000prn.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net> <ihc2ul$u$1@reader1.panix.com> <8punodFd6kU1@mid.individual.net>`

```
On Jan 22, 1:47 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> docdw...@panix.com wrote:
> > In article <8pscnuF93...@mid.individual.net>,
…[80 more quoted lines elided]…
> simple process that solves the problem of rounding 2 real numbers for me.

A simple process it may be but one problem with reals is that many
numbers are not represented exactly. If 0.5 in your code is
represented in one machine as 0.49999999 and another as 0.5000001 and
these are applied to a number that is actually xxx.50 but is
represented as xxx.499999999 then you will get different results.





> And that was all I wanted.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 7)_

- **From:** "robertwessel2@yahoo.com" <robertwessel2@yahoo.com>
- **Date:** 2011-01-24T12:01:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9afc8557-01fc-4649-a6ac-ce51479c15c5@i22g2000prd.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net> <ihc2ul$u$1@reader1.panix.com> <8punodFd6kU1@mid.individual.net> <c73f222c-29a0-486d-8e65-7dcec89dd29b@e9g2000prn.googlegroups.com>`

```
On Jan 24, 11:46 am, Richard <rip...@Azonic.co.nz> wrote:
> A simple process it may be but one problem with reals is that many
> numbers are not represented exactly. If 0.5 in your code is
> represented in one machine as 0.49999999 and another as 0.5000001 and
> these are applied to a number that is actually xxx.50 but is
> represented as xxx.499999999 then you will get different results.


Of course that raises the question of whether there are any machines
with such an issue storing the value one-half.  Almost all* "real"
implementations that can store fractional results, either floating or
scaled integer, can exactly store one-half.  Even on floating formats
where the number becomes large enough that you lose the .5 due to
limited precision, the result is typically the next higher or lower
integer value (before degrading further).

Had you picked one-tenth, or even better, one-sixth, and then
questioned the rounding of x*5 or x*3, they're be no issue.


*I'm sure someone out there is running a trinary (or other unusual
base) implementation where that's not true, but it's not a
consideration for most of us.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 8)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2011-01-24T13:09:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4904cc53-d68b-4586-953e-eb2c2934aa72@29g2000prb.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net> <ihc2ul$u$1@reader1.panix.com> <8punodFd6kU1@mid.individual.net> <c73f222c-29a0-486d-8e65-7dcec89dd29b@e9g2000prn.googlegroups.com> <9afc8557-01fc-4649-a6ac-ce51479c15c5@i22g2000prd.googlegroups.com>`

```
On Jan 25, 9:01 am, "robertwess...@yahoo.com"
<robertwess...@yahoo.com> wrote:
> On Jan 24, 11:46 am, Richard <rip...@Azonic.co.nz> wrote:
>
…[15 more quoted lines elided]…
> questioned the rounding of x*5 or x*3, they're be no issue.

One-sixth cannot be represented in floating denary. One-tenth cannot
be represented in floating binary.

However, the same issue would be true if 0.5 was represented exactly
but 12345.50 was represented on one machine as 12345.49999999 and on
another as 12345.500000..

Or even, on one machine, if 12345.50 was represented as
12345.4999999.. and 12346.50 was represented as 12346.500000000..

While PD claimed it was NEVER a problem, it is likely that, if he
_actually_ did use reals*, he never _noticed_ a problem.

> *I'm sure someone out there is running a trinary (or other unusual
> base) implementation where that's not true, but it's not a
> consideration for most of us.

Many decades ago I did program on a machine that used Excess-3**, and
it even had a (very limited) COBOL compiler***. In fact I still have
some in my old computer stack, though I doubt that they work.



* It is more likely that PD used fixed decimal or BCD. It is unusual
to find reals (floating point binary) in COBOL, and if they are used
then the problems soon become apparent.

** The Cogar/Singer networked desktop machine from the early 70s that
later became the ICL 1500. Its replacement machine, the ICL DRS20
multi-processor micro based system included a 'reatined mode'
processor that emulated the 1500 (I have some of those as well).

*** The ICL 1500 COBOL compiler was written by the people who later
left ICL and formed MicroFocus.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-25T12:02:47+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q6eopF59tU1@mid.individual.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net> <ihc2ul$u$1@reader1.panix.com> <8punodFd6kU1@mid.individual.net> <c73f222c-29a0-486d-8e65-7dcec89dd29b@e9g2000prn.googlegroups.com> <9afc8557-01fc-4649-a6ac-ce51479c15c5@i22g2000prd.googlegroups.com> <4904cc53-d68b-4586-953e-eb2c2934aa72@29g2000prb.googlegroups.com>`

```
Richard wrote:
> On Jan 25, 9:01 am, "robertwess...@yahoo.com"
> <robertwess...@yahoo.com> wrote:
…[30 more quoted lines elided]…
> _actually_ did use reals*, he never _noticed_ a problem.

I DID use "real"s but that is outside the scope of this discussion. Had 
results been incorrect, SOMEBODY would have noticed, whether I did or not...
>
>> *I'm sure someone out there is running a trinary (or other unusual
…[11 more quoted lines elided]…
> then the problems soon become apparent.

As I was writing COBOL mostly, yes, fixed point decimal is what I was 
talking about., and this was reflected in the example pictures I posted. I 
used "real" loosely in the mathematical sense of a non-integer, but this is 
a whole 'nother can of worms as the mathematical definition of "real" is 
still being argued about. It IS unusual to find floating point binary in 
COBOL, nevertheless one installation in Auckland where I worked during the 
late 60s DID use them in COBOL. I honestly can't remember whether I had 
occasion to use my rounding technique or not.
>
> ** The Cogar/Singer networked desktop machine from the early 70s that
…[5 more quoted lines elided]…
> left ICL and formed MicroFocus.

Based on work I'm doing at the moment, they have a lot to answer for... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-25T11:49:57+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q6e0nFvbkU1@mid.individual.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net> <ihc2ul$u$1@reader1.panix.com> <8punodFd6kU1@mid.individual.net> <c73f222c-29a0-486d-8e65-7dcec89dd29b@e9g2000prn.googlegroups.com> <9afc8557-01fc-4649-a6ac-ce51479c15c5@i22g2000prd.googlegroups.com>`

```
robertwessel2@yahoo.com wrote:
> On Jan 24, 11:46 am, Richard <rip...@Azonic.co.nz> wrote:
>> A simple process it may be but one problem with reals is that many
…[20 more quoted lines elided]…
> consideration for most of us.

Thank you Robert.

You have confirmed what 46 years of programming experience has also 
indicated.

Like I said elsewhere, my approach is based on experience and I have NEVER 
found .5 to be anything OTHER Than .5 on any platform, on any continent, in 
any decade.

I do take your point about values other than .5 though. I have never 
considered that.

Pete.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-25T11:45:57+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q6dp7FtokU1@mid.individual.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net> <ihc2ul$u$1@reader1.panix.com> <8punodFd6kU1@mid.individual.net> <c73f222c-29a0-486d-8e65-7dcec89dd29b@e9g2000prn.googlegroups.com>`

```
Richard wrote:
> On Jan 22, 1:47 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[93 more quoted lines elided]…
>
 Yes, that's true.

But it is only theoretically true, inasmuch as it has never happened to me. 
(probably because the .5 is a literal, it is always held as .5. We did 
exclude floating point from the discussion as "everybody knows" this may 
give different results.

Pete.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 4)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2011-01-21T19:03:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9p3kj618bb4udkmg6i83i0b2cehbnhgqbg@4ax.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net>`

```
On Fri, 21 Jan 2011 16:26:51 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Bill Klein wrote:
>> Pete,
…[12 more quoted lines elided]…
>
I hope you actually tested and added -.5 (or the appropriate value in
case you were rounding to other than an integer) when the value of the
item being rounded was negative.  Actually if there were no
intermediate results involved (i.e. only a two operand computation)
one of the compilers had a bug because the rounding process is well
specified if you were just doing the standard COBOL rounding and not
something like ROUND to the nearest even where you would have to code
it.  

Clark Morris
>
>However, I don't think there any cases that I know of
…[34 more quoted lines elided]…
><unreferenced previous snipped>
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-22T13:58:31+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8puodqFhcfU1@mid.individual.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net> <9p3kj618bb4udkmg6i83i0b2cehbnhgqbg@4ax.com>`

```
Clark F Morris wrote:
> On Fri, 21 Jan 2011 16:26:51 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[18 more quoted lines elided]…
> item being rounded was negative.

It's a very good point, Clark. (I'm pretty sure I didn't... In my own 
defence, I was a junior programmer in my early 20s. There were not the "best 
practices" and "standard procedures" in place that there are now and 
programming was very much a "seat of the pants" experience. But mostly, I 
knew that the numbers I was applying this to could not be negative. I'd like 
to think that if I had been confronted with a case where it COULD be 
negative, I would have considered that, but who knows...? It was a career 
lifetime ago.)

Pete.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 6)_

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2011-01-22T13:14:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s0G_o.627562$iV7.84005@en-nntp-15.dc1.easynews.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net> <9p3kj618bb4udkmg6i83i0b2cehbnhgqbg@4ax.com> <8puodqFhcfU1@mid.individual.net>`

```
Should anyone care, the draft of the next COBOL Standard allows for a 
variety of rounding options to be specified on either a "global" (per 
program) or a per statement.  The supported rounding techniques are called 
(and I think there names match "industry standards")

 - AWAY-FROM-ZERO
 - NEAREST-AWAY-FROM-ZERO
 - NEAREST-EVEN
 - NEAREST-TOWARD-ZERO
  PROHIBITED
 - TOWARD-GREATER
 - TOWARD-LESSER
 - TRUNCATION

The default is compatible with previous Standards - as the note says,
  "NEAREST-AWAY-FROM-ZERO is the rounding mode provided by the ROUNDED 
phrase in previous COBOL standards."

These new rounding options allow for portable rounding results that meet 
different business needs.

P.S.  As stated in a previous note, ROUNDING is (and as far as I know has 
always been) PORTABLE.  It is COMPUTE that is not.

If you use COMPTUE to add ".5" (or whatever) then you won't get portability 
(guaranteed).  If you get portable results explicitly adding ".5" (or 
whatever) with COMPUTE, you will also get portable results using ROUNDED 
(with the old options - or the new ones)
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-23T16:21:42+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q1l68FqmmU1@mid.individual.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net> <9p3kj618bb4udkmg6i83i0b2cehbnhgqbg@4ax.com> <8puodqFhcfU1@mid.individual.net> <s0G_o.627562$iV7.84005@en-nntp-15.dc1.easynews.com>`

```
Bill Klein wrote:
> Should anyone care, the draft of the next COBOL Standard allows for a
> variety of rounding options to be specified on either a "global" (per
> program) or a per statement.

While I don't actually "care", I am certainly "interested" :-)



>The supported rounding techniques are
> called (and I think there names match "industry standards")
…[9 more quoted lines elided]…
>

Man!  I look at this and all I feel is "So glad I don't have to deal with 
this."

And that's a pity.

Because someone has put considerable thought into the possibilities and 
dealing with them. It is good work and they deserve credit for it.

But increasing the verbosity of COBOL simply increases the complexity of it. 
(More things to learn and remember...) And for what?

So I can keep using COBOL?

But it ISN'T the COBOL I knew and loved. THAT COBOL died when the Network 
arrived and devices started talking to each other in ways that COBOL could 
never even imagine. A whole new paradigm that made software a service driven 
from hardware, instead of the other way round. Interrupt driven processes 
that required immediate attention, not "I'll read you when I'm ready to...", 
or, "My program controls when things happen...".

The fundamental paradigm is flawed for this day and age. It is a 
centralised, monolithic, procedural, Von Neumann processing language. Until 
THAT is addressed it has no future. (And I am now persuaded it cannot be 
fixed...so, I see no future for it.)

Some people (VERY smart people who never received accolades and awards or 
attended dinners in their honour...), quite some time ago, realised this and 
added Object Orientation to it.

Once you got the hang of it, it was pretty good. I used OO COBOL to write 
components and run them on desktops and web pages without problem  for 
around 10 years and it was fun as well. (Fujitsu (in particular) bent over 
backwards to give COBOL special classes that simplified interfacing to COM 
components and let COBOL code play nicely with components written in other 
languages.)

However, the really sad thing is that OO COBOL is just unwieldy compared to 
langages like Java and C#. Scripting languages like PHP (which is very like 
C#), Python, and even Perl (although Perl has it's own complexity problems), 
just wipe the floor with it.

Why is COBOL (even OO COBOL) more unwieldy than other modern languages? 
Because of things like the above. It just gets more and more verbose with 
every new standard (and I won't go there...) to the point where vendors 
won't implement it and users won't use it.

Do you seriously believe any commercial COBOL vendor will implement this, 
Bill? (Those fanatical hobbyists at OpenCOBOL might have a go... I honestly 
wish them well. :-))

If so, when? (Please don't say:"In 17 years time...")

I will be pleased to stand corrected if they do, but I won't be taking bets.



> The default is compatible with previous Standards - as the note says,
>  "NEAREST-AWAY-FROM-ZERO is the rounding mode provided by the ROUNDED
…[9 more quoted lines elided]…
> portability (guaranteed).

I challenge that, given the data structure in my example, which was the 
structure the OP gave us.

> If you get portable results explicitly
> adding ".5" (or whatever) with COMPUTE, you will also get portable
> results using ROUNDED (with the old options - or the new ones)

In my experience, it doesn't matter whether you use COMPUTE or ADD/MOVE, the 
code I posted using .5 is portable. (As long as the pictures I also posted 
are used.)

I think these discussions get way out of control sometimes.

A person posted asking for ways to do rounding. I replied (in good faith) 
with a way which has worked across numerous platforms and NEVER failed. I 
stated a personal preference as to not using ROUNDED and why I came to that 
conclusion.

That seems fair enough for free advice, to me.

If you can show an example, using the pictures I posted, where it ISN'T 
portable ("guaranteed") then please do so.

I don't think you can, and your argument is based on theory, where mine is 
based on experience.

Pete.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-01-23T14:51:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ihhfa6$515$1@reader1.panix.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8puodqFhcfU1@mid.individual.net> <s0G_o.627562$iV7.84005@en-nntp-15.dc1.easynews.com> <8q1l68FqmmU1@mid.individual.net>`

```
In article <8q1l68FqmmU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>Bill Klein wrote:
>> Should anyone care, the draft of the next COBOL Standard allows for a
…[3 more quoted lines elided]…
>While I don't actually "care", I am certainly "interested" :-)

From http://www.learnersdictionary.com/search/care%5B2%5D :

--begin quoted text:

1 : to feel interest in something : to be interested in or concerned about 
something

--end quoted text

It kind of reminds me of actions I've seen performed by members of the 
constabulary as depicted on 'Real Life' television shows.  According to 
the Supreme Court of the United States of America - what do *they* know 
about laws, anyhow? - a person is considered detained when circumstances 
are such that a reasonable person would believe he is not free to leave.  

Officers of the law are routinely shown handcuffing a person and saying 'I 
am restraining your motion out of concerns for my safety but I am not 
detaining you.'  Now... it is obvious that these badge-toting, 
gun-carrying, Taser-wielding civil servants have learned, somewhere, that 
having a set of handcuffs on your wrists in no wise would cause a 
reasonable person to believe he is not free to leave.

Likewise, 'I do not care (defined, as shown above, as 'to be interested') 
but I am interested' seems to be of a similar case.

DD
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-24T14:12:29+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q41vuFc2kU1@mid.individual.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8puodqFhcfU1@mid.individual.net> <s0G_o.627562$iV7.84005@en-nntp-15.dc1.easynews.com> <8q1l68FqmmU1@mid.individual.net> <ihhfa6$515$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <8q1l68FqmmU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[14 more quoted lines elided]…
> --end quoted text

That's ONE definition. "care" also has other meanings...

care (k�r)
n.
1. A burdened state of mind, as that arising from heavy responsibilities; 
worry.
2. Mental suffering; grief.
3. An object or source of worry, attention, or solicitude.

So, I can be "not burdened or worried" by Bill's post or the implications in 
it, but still be interested.

But then, if you took it in the context it was stated, you wouldn't have a 
chance to entertain us with your opinion on the "constabulary", and where's 
the fun in that?

>
> It kind of reminds me of actions I've seen performed by members of the
…[12 more quoted lines elided]…
> leave.

It seems sad to me that they even need to state such a disclaimer. (They 
don't here...)

If a cop puts handcuffs on you it is fair to suppose he has a good reason. 
(On the rare occasions when he doesn't, there are Civil Processes that can 
be pursued to obtain compensation, or, if you live in Texas, you can give 
someone a crate of beer to beat him up.

Don't like being detained? Avoid conflict with the "badge-toting, 
gun-carrying, Taser-wielding civil servants" who protect and serve you. They 
have a much bigger gang than you've got and there is no possible way you 
will win an argument with them. (Unless you manage to get it to Court, and 
even then it is exremely difficult because the cop has credibility and you 
don't.) Stay calm, stay polite, show you are no kind of threat, but you know 
your rights.

I have had numerous cases where it has been necessary to engage in discourse 
with Officers of the Law (and in the USA I found cops to be invariably 
courteous and not looking for trouble), usually because I had infracted it. 
Never been handcuffed in my life (not even in Mexico... :-)) . Came close in 
Australia once, but everybody calmed down before any real damage was done.
>
> Likewise, 'I do not care (defined, as shown above, as 'to be
> interested') but I am interested' seems to be of a similar case.

As that particular definition is contrived by you to fit the statement, it 
is completely irrelevant and has no bearing on anything.

BTW, the only reason I bothered to reply to this nonsense is because I am 
sick at home with time on my hands... :-)

What's your excuse, Doc?

Pete.




 to my statement
>
> DD
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-01-24T13:23:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ihjugk$52k$1@reader1.panix.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8q1l68FqmmU1@mid.individual.net> <ihhfa6$515$1@reader1.panix.com> <8q41vuFc2kU1@mid.individual.net>`

```
In article <8q41vuFc2kU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <8q1l68FqmmU1@mid.individual.net>,
…[27 more quoted lines elided]…
>it, but still be interested.

There's the rub, Mr Dashwood.  English, last I looked, she is a funny 
language; one word can have a variety of definitions.  Perhaps it is a 
good idea to consider those definitions when trying to communicate 
something instead of assuming 'oh, Everyone Knows that I'm using M-W 2 and 
not AHD 7... it's Just Obvious'.

>
>But then, if you took it in the context it was stated, you wouldn't have a 
>chance to entertain us with your opinion on the "constabulary", and where's 
>the fun in that?

Likewise, Mr Dashwood, you might not have had a chance to see how 
precision is applied to language in order to make communication less 
ambiguous... and you've demonstrated, frequently, that you find absolutely 
no fun in that repeatedly.

(aye, that was nasty... but every so often I show how weak I can be, I 
guess)

>> Officers of the law are routinely shown handcuffing a person and
>> saying 'I am restraining your motion out of concerns for my safety
…[12 more quoted lines elided]…
>someone a crate of beer to beat him up.

It seems that in this part of the world there's been a sufficient number 
of instances where 'a good reason' has been shown to have no legal 
basis... then again, the police in the United States are a strongly 
unionised force and, as such, may readily be seen to be showing behavior 
of such.

>
>Don't like being detained? Avoid conflict with the "badge-toting, 
>gun-carrying, Taser-wielding civil servants" who protect and serve you.

The problem with that, Mr Dashwood, is how such servants havve, in the 
past, interpreted avoiding contact with them to be grounds for detention.

[snip]

>> Likewise, 'I do not care (defined, as shown above, as 'to be
>> interested') but I am interested' seems to be of a similar case.
>
>As that particular definition is contrived by you to fit the statement, it 
>is completely irrelevant and has no bearing on anything.

If one sees taking a definition from a commonly-accepted source as 
'contrivance', Mr Dashwood, then Humpty-Dumptyisms appear to be reasonably 
close.  In future one might see a person of integrity responding with 
'Given that definition the conclusion is plausible; my use, however, was 
based on (source) and that might throw things into an entirely different 
light.  Wonderful language, this English.'

>
>BTW, the only reason I bothered to reply to this nonsense is because I am 
>sick at home with time on my hands... :-)
>
>What's your excuse, Doc?

I am an American, born of two Americans, Mr Dashwood, and I act within the 
law based on free will.

DD
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-25T12:19:35+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q6fo9FbrbU1@mid.individual.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8q1l68FqmmU1@mid.individual.net> <ihhfa6$515$1@reader1.panix.com> <8q41vuFc2kU1@mid.individual.net> <ihjugk$52k$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <8q41vuFc2kU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[48 more quoted lines elided]…
> guess)

:-) It's really OK... I've lived a full life, and been insulted by experts 
:-)

There might even be some truth in the allegation. I am not always 
meticulously precise when writing English it really depends on how important 
it is, and on other factors. For example, I would not take the same care 
when writing a magazine article that I would when drafting a contract. If I 
did, no-one would buy the articles I write. What is invariably true is that 
I do say what I mean. However the derivation of meaning is something perhaps 
better left to another thread....

>
>>> Officers of the law are routinely shown handcuffing a person and
…[44 more quoted lines elided]…
> into an entirely different light.  Wonderful language, this English.'

Doc, you don't seriously want me to become you? I yam what I yam.

>
>>
…[6 more quoted lines elided]…
> within the law based on free will.

Isn't it because of free will that laws had to be invented? :-)

Pete.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-01-25T02:11:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ihlbh4$eqd$1@reader1.panix.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8q41vuFc2kU1@mid.individual.net> <ihjugk$52k$1@reader1.panix.com> <8q6fo9FbrbU1@mid.individual.net>`

```
In article <8q6fo9FbrbU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:

[snip]

>> Likewise, Mr Dashwood, you might not have had a chance to see how
>> precision is applied to language in order to make communication less
…[9 more quoted lines elided]…
>There might even be some truth in the allegation.

My apologies for making it in public, then, and you may consider it 
withdrawn.  Lovely weather, isn't it?

DD
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 11)_

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2011-01-26T03:01:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<af0d1ec4-ee80-485d-8261-59bd246b979f@w17g2000vbl.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8q1l68FqmmU1@mid.individual.net> <ihhfa6$515$1@reader1.panix.com> <8q41vuFc2kU1@mid.individual.net> <ihjugk$52k$1@reader1.panix.com>`

```
On Jan 24, 1:23 pm, docdw...@panix.com () wrote:
> Likewise, Mr Dashwood, you might not have had a chance to see how
> precision is applied to language in order to make communication less
> ambiguous...

Language and precision is an oxymoron.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-01-26T12:22:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ihp3ms$e1j$1@reader1.panix.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8q41vuFc2kU1@mid.individual.net> <ihjugk$52k$1@reader1.panix.com> <af0d1ec4-ee80-485d-8261-59bd246b979f@w17g2000vbl.googlegroups.com>`

```
In article <af0d1ec4-ee80-485d-8261-59bd246b979f@w17g2000vbl.googlegroups.com>,
Alistair Maclean  <alistair.j.l.maclean@googlemail.com> wrote:
>On Jan 24, 1:23?pm, docdw...@panix.com () wrote:
>> Likewise, Mr Dashwood, you might not have had a chance to see how
…[3 more quoted lines elided]…
>Language and precision is an oxymoron.

That might be, Mr Maclean, a reason for my having constructed my statement 
as I did.

(is the opposite of an oxymoron an anaerobegenius?)

DD
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 13)_

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2011-01-26T11:14:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a837937f-d0b1-44c6-9511-f948fafa08f1@s9g2000vby.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8q41vuFc2kU1@mid.individual.net> <ihjugk$52k$1@reader1.panix.com> <af0d1ec4-ee80-485d-8261-59bd246b979f@w17g2000vbl.googlegroups.com> <ihp3ms$e1j$1@reader1.panix.com>`

```
On Jan 26, 12:22 pm, docdw...@panix.com () wrote:
> In article <af0d1ec4-ee80-485d-8261-59bd246b9...@w17g2000vbl.googlegroups.com>,
> Alistair Maclean  <alistair.j.l.macl...@googlemail.com> wrote:
…[13 more quoted lines elided]…
> DD

Smart, I like the second half of the response.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 14)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-01-26T19:40:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ihptbj$g86$1@reader1.panix.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <af0d1ec4-ee80-485d-8261-59bd246b979f@w17g2000vbl.googlegroups.com> <ihp3ms$e1j$1@reader1.panix.com> <a837937f-d0b1-44c6-9511-f948fafa08f1@s9g2000vby.googlegroups.com>`

```
In article <a837937f-d0b1-44c6-9511-f948fafa08f1@s9g2000vby.googlegroups.com>,
Alistair Maclean  <alistair.j.l.maclean@googlemail.com> wrote:
>On Jan 26, 12:22?pm, docdw...@panix.com () wrote:
>> In article
><af0d1ec4-ee80-485d-8261-59bd246b9...@w17g2000vbl.googlegroups.com>,
>> Alistair Maclean ?<alistair.j.l.macl...@googlemail.com> wrote:

[snip]

>> >Language and precision is an oxymoron.
>>
…[5 more quoted lines elided]…
>Smart, I like the second half of the response.

One takes enjoyment where one can find it, I guess... it is like that 8-oz 
cup that contains 4oz of kerosene; the pessimist sees it as half-empty but 
the optimist sees it as half-fuel.

DD
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 15)_

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2011-01-27T09:21:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d7b84b3-3872-462f-9b65-c2fa82a7938c@a5g2000vbs.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <af0d1ec4-ee80-485d-8261-59bd246b979f@w17g2000vbl.googlegroups.com> <ihp3ms$e1j$1@reader1.panix.com> <a837937f-d0b1-44c6-9511-f948fafa08f1@s9g2000vby.googlegroups.com> <ihptbj$g86$1@reader1.panix.com>`

```
On Jan 26, 7:40 pm, docdw...@panix.com () wrote:
> In article <a837937f-d0b1-44c6-9511-f948fafa0...@s9g2000vby.googlegroups.com>,
> Alistair Maclean  <alistair.j.l.macl...@googlemail.com> wrote:
…[21 more quoted lines elided]…
> DD

And the engineer sees the cup as being twice the size that it needs to
be.

Sorry missed the pun. Another goody.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 8)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2011-01-25T18:40:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<66trj65ttftnjpo6olgtcb5267a10lfjc6@4ax.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net> <9p3kj618bb4udkmg6i83i0b2cehbnhgqbg@4ax.com> <8puodqFhcfU1@mid.individual.net> <s0G_o.627562$iV7.84005@en-nntp-15.dc1.easynews.com> <8q1l68FqmmU1@mid.individual.net>`

```
On Sun, 23 Jan 2011 16:21:42 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Bill Klein wrote:
>> Should anyone care, the draft of the next COBOL Standard allows for a
…[21 more quoted lines elided]…
>this."

In many if not most shops, you would not have to deal with this.  In
shops that really should be using banker's rounding (NEAREST-EVEN)
this should have been available 40 - 50 years ago since writing the
routine in COBOL would be difficult and cute even in a called
assembler routine.  There is hardware support on computers that
implemented IEEE decimal floating point (system z has done so as of
the z9 with full hardware implementation in the z10 and z196 while
power6 and power7 architectures also have hardware implementation).
IBM's C/C++ has language implementation on at least some of the
platforms.  DB2 has support.  SAP ABAP also has support.  Now that
COBOL has defined decimal floating point for the next standard, I
would hope the platform that is most COBOL oriented will implemented
ALL of the IEEE754-2008 floating point types so that COBOL can play
nicely and natively with the other languages on the platform.  I also
hope they implement it in COBOL on the i and p processors (AS400
follow-on and the AIX box). 

In short, if your application needs rounding other than the standard
COBOL rounding (DEFAULT in the new standard), you will need to deal
with this and wish you had language support.  Otherwise you can ignore
the rounding modes that will be available and which have been
implemented by shops that have needed them just as I implemented the
special rounding to the nearest half cent for pay rates that was in
one payroll system (thank heaven the pay rates were always positive).

Clark Morris
> 
>And that's a pity.
…[91 more quoted lines elided]…
>Pete.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 8)_

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2011-01-26T04:12:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HsS%o.572738$Qg.342907@en-nntp-04.dc1.easynews.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net> <9p3kj618bb4udkmg6i83i0b2cehbnhgqbg@4ax.com> <8puodqFhcfU1@mid.individual.net> <s0G_o.627562$iV7.84005@en-nntp-15.dc1.easynews.com> <8q1l68FqmmU1@mid.individual.net>`

```
Pete,

I have been waiting a little bit to think about how to respond to your note. 
There are a couple of "general" things that I though you (and others) might 
be interested in (that relate to your general issues):


1) The new syntax adds no REQUIRED verbosity to COBOL programming. The 
default (if you code only "as you used to") is to work exactly as it always 
has, i.e. ROUNDED = "round to nearest"


2) Yes, I think there will be some (many?) implementations of this feature.


The reason has to do with how this enhancement was "developed" (for the next 
COBOL Standard). The feature is actually derived from the (relatively) 
recent enhancement to the IEEE Floating Point specification (IEEE 754). It 
was this new standard that introduced "standard defined DECIMAL floating 
point" data types and arithmetic. Although traditional (IEEE, not IBM) 
"binary floating point" data items and arithmetic is "maintained" in the new 
Standard, it also provide "better" arithmetic (and portable data types) for 
those who want to use floating point - but expect it to work "correctly" 
with DECIMAL arithmetic.


There are already C "libraries" for the new data types and arithmetic 
operations, but more importantly, IBM already provides hardware support for 
it. I can't remember whether INTEL has the hardware support for it yet, but 
they were involved in the development of the Standard and (I think) have 
indicated that they will have hardware support for it.


IBM (on its z/OS) mainframes already provides language support for it in 
Assembler, C/C++, and PL/I. They have accepted the requirement o add it to 
COBOL (which is USUALLY a sign that it will be available within a 
RELATIVELY? short period of time).


Now, to be clear supporting Decimal Floating Point data types and "basic" 
arithmetic does NOT mean that language implementations MUST provide support 
for ALL the Standardized rounding options. However, as most of the existing 
C libraries for DFP support them, I think it is HIGHLY likely that IBM (and 
probably others) will support the ROUNDING options. After all, they are all 
used in various "normal" business and scientific applications. (The old 
"TELCO" cross-language test required "bankers rounding". See: 
http://en.wikipedia.org/wiki/Rounding and look for "[edit] Round half to 
even").


3) Therefore, for COBOL, I expect that IBM mainframe COBOL will support all 
(or most) of these rounding options within the next few years (possibly 
before the end of this year). I expect that Micro Focus and all the 
"Mainframe Compatible" COBOL compilers will then implement them within a 
year or two.


* * * * * * *


Could my "crystal ball" be wrong? Absolutely! but I don't think so.


As partial confirmation of my expectation, see the EXISTING IBM reference 
manual for their mainline C/C++ product at:

http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/edclb1b0/3.258



"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:8q1l68FqmmU1@mid.individual.net...
> Bill Klein wrote:
>> Should anyone care, the draft of the next COBOL Standard allows for a
…[119 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-27T01:34:45+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qain8FnpeU1@mid.individual.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net> <9p3kj618bb4udkmg6i83i0b2cehbnhgqbg@4ax.com> <8puodqFhcfU1@mid.individual.net> <s0G_o.627562$iV7.84005@en-nntp-15.dc1.easynews.com> <8q1l68FqmmU1@mid.individual.net> <HsS%o.572738$Qg.342907@en-nntp-04.dc1.easynews.com>`

```
Bill Klein wrote:
> Pete,
>
…[58 more quoted lines elided]…
> Could my "crystal ball" be wrong? Absolutely! but I don't think so.

Thanks Bill, it is a very good response.

After reading what Clark said about Banking needing some of these features, 
you might be right.

I'm still glad I'm not affected by it. :-)

Crystal Balls are always dodgy and mine is no exception; I was wrong about 
voice input being the next "Big Thing"; it is surfaces...and I think we're 
going to hear a lot more about parallell processing and specific program 
constructs to accommodate it (based on what's happening with C#). But, I do 
get it right, too: ["Learn Java", "move to RDB", "pick up OO", all long 
before the world was the way it has become...]

I do take your point (1) above. But I'm still not convinced that vendors 
will continue pouring money into COBOL, knowing that they are on a hiding to 
nothing long term.

Time will tell.

Pete


>
>
…[127 more quoted lines elided]…
>> "I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 4)_

- **From:** "robin" <robin51@dodo.mapson.com.au>
- **Date:** 2011-01-26T00:49:22+11:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4d3ee001$0$88217$c30e37c6@exi-reader.telstra.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message news:8pscnuF93uU1@mid.individual.net...

| Yes, that is what I actually meant. I learned a long time ago, in different
| environments that rounded results were not always what I expected. I
…[4 more quoted lines elided]…
| truncating."

That was >50 years ago.

How is that relevent now?
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2011-01-25T09:34:05-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e2824f81-55c4-4914-80ac-8547957e12d8@i32g2000pri.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net> <4d3ee001$0$88217$c30e37c6@exi-reader.telstra.net>`

```
On Jan 26, 2:49 am, "robin" <robi...@dodo.mapson.com.au> wrote:
> "Pete Dashwood" <dashw...@removethis.enternet.co.nz> wrote in messagenews:8pscnuF93uU1@mid.individual.net...
>
…[8 more quoted lines elided]…
> That was >50 years ago.

1960 itself may be >50 years ago but "the 1960s" can only be said to
be >40 years ago. I think that you have a rounding error.


> How is that relevent now?
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-26T17:57:28+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q9ntqF5k3U1@mid.individual.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net> <4d3ee001$0$88217$c30e37c6@exi-reader.telstra.net> <e2824f81-55c4-4914-80ac-8547957e12d8@i32g2000pri.googlegroups.com>`

```
Richard wrote:
> On Jan 26, 2:49 am, "robin" <robi...@dodo.mapson.com.au> wrote:
>> "Pete Dashwood" <dashw...@removethis.enternet.co.nz> wrote in
…[13 more quoted lines elided]…
> be >40 years ago. I think that you have a rounding error.

:-)

Pete.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-26T18:11:56+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q9oouFadoU1@mid.individual.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <wvQZo.322013$Ph5.58275@en-nntp-07.dc1.easynews.com> <8pscnuF93uU1@mid.individual.net> <4d3ee001$0$88217$c30e37c6@exi-reader.telstra.net>`

```
robin wrote:
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
> news:8pscnuF93uU1@mid.individual.net...
…[9 more quoted lines elided]…
> That was >50 years ago.

No, it isn't. Think again. It would have been around 1968...
>
> How is that relevent now?

It probably isn't... to you. (It certainly is, to me... funny thing that 
Life Experience...)

The point I was trying to make was WHY I arrived at my current practise, 
which is to avoid using ROUNDED and add .5 instead.

Robin, sometimes things which happened a long time ago are definitely no 
longer relevant:

Bustle skirts, little boys sweeping chimneys, pit ponies, chinese foot 
binding, quill pens, even steam engines and hansom cabs... the list goes on.

But other things that happened long ago can be a beacon to the future and 
light the way for new innovation and improvement.

Writing COBOL today, is really not much different (for most people) to 
writing COBOL 40 years ago. For that reason, lessons learned writing COBOL 
THEN can still be relevant NOW.

(And I'm NOT suggesting that my personal experience and the conclusions I 
drew from it are valid or relevant for everyone, only that they led to my 
current practise, in this particular case.)

Pete.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-01-26T12:28:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ihp429$e1j$2@reader1.panix.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pscnuF93uU1@mid.individual.net> <4d3ee001$0$88217$c30e37c6@exi-reader.telstra.net> <8q9oouFadoU1@mid.individual.net>`

```
In article <8q9oouFadoU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>Robin, sometimes things which happened a long time ago are definitely no 
>longer relevant:
>
>Bustle skirts, little boys sweeping chimneys, pit ponies, chinese foot 
>binding, quill pens, even steam engines and hansom cabs... the list goes on.

Hmmmmm... bustle skirts, little boys sweeping chimmneys, pit ponies and 
hansom cabs no longer relevant?  Tell *that* to the purveyors of certain 
kinds of literature!

DD
```

##### ↳ ↳ Re: Rounding

- **From:** "robin" <robin51@dodo.mapson.com.au>
- **Date:** 2011-01-24T22:16:56+11:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<4d3d691a$0$88227$c30e37c6@exi-reader.telstra.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message news:8pn774FcdhU1@mid.individual.net...
| jmoore wrote:
| > What is the best way to round up 4.88 to 4.9 and not 5. The input
…[12 more quoted lines elided]…
| That'll work on any platform...

It will, provided that the value is positive.
However, when the value is negative, it will round down.

The ROUND function in PL/I will correctly round up regardless of sign.
```

###### ↳ ↳ ↳ Re: Rounding

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2011-01-24T08:47:00-07:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<4l7rj6tqvf5vj1t367fembll2fon5uqsnu@4ax.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <4d3d691a$0$88227$c30e37c6@exi-reader.telstra.net>`

```
On Mon, 24 Jan 2011 22:16:56 +1100, "robin"
<robin51@dodo.mapson.com.au> wrote:

>The ROUND function in PL/I will correctly round up regardless of sign. 

Provided that those who are paying for my application want this
"correct" interpretation for this need.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 4)_

- **From:** "robin" <robin51@dodo.mapson.com.au>
- **Date:** 2011-01-26T00:50:27+11:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<4d3ee002$0$88217$c30e37c6@exi-reader.telstra.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <4d3d691a$0$88227$c30e37c6@exi-reader.telstra.net> <4l7rj6tqvf5vj1t367fembll2fon5uqsnu@4ax.com>`

```
"Howard Brazee" <howard@brazee.net> wrote in message news:4l7rj6tqvf5vj1t367fembll2fon5uqsnu@4ax.com...
|| jmoore wrote:
||| > What is the best way to round up 4.88 to 4.9 and not 5. The input
…[20 more quoted lines elided]…
| "correct" interpretation for this need.

You started out by saying that you avoid ROUNDED in COBOL
because its effect is different on different platforms.

On the other hand, ROUND in PL/I is consistent.
What's more, it does it correctly.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 5)_

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2011-01-26T03:11:49-06:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<nzR%o.340760$Ph5.198741@en-nntp-07.dc1.easynews.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <4d3d691a$0$88227$c30e37c6@exi-reader.telstra.net> <4l7rj6tqvf5vj1t367fembll2fon5uqsnu@4ax.com> <4d3ee002$0$88217$c30e37c6@exi-reader.telstra.net>`

```
"robin" <robin51@dodo.mapson.com.au> wrote in message 
news:4d3ee002$0$88217$c30e37c6@exi-reader.telstra.net...
> "Howard Brazee" <howard@brazee.net> wrote in message 
> news:4l7rj6tqvf5vj1t367fembll2fon5uqsnu@4ax.com...
> || jmoore wrote:
<snip>
> You started out by saying that you avoid ROUNDED in COBOL
> because its effect is different on different platforms.
…[3 more quoted lines elided]…
>
Actually, if you try it with existing COBOL's, check any manual or check the 
current or PAST COBOL Standards (or simply read all the notes in this 
thread), you will find that COBOL
 - does it correctly (if you are concerned about "rounding to nearest - for 
negative numbers)
 - does it consistantly (across platforms and vendors)

Of course, COBOL does have the advantage over PL/I that it has an actively 
maintained and enhanced ANSI *and* ISO Standard.

This (for conforming compilers) provide "supported" (by a recognized 
Standard) portability across platforms, releases, and vendors.

As far as I know, PL/I is also consistant for portability across platforms 
and vendors; it just doesn't have a currently maintained and enhanced 
Standard against which vendors and implementors can compare it.

I might be interested in how many participants in ths group actually work in 
an environment where PL/I is a supported (by those who pay for their work) 
option.  Certainly, MOST of the participants from IBM mainframes have such 
an option (although their management may or may not accept PL/I as an 
option - just as some IBM PL/I shops do not accept COBOL as an option).  On 
the other hand, for those participants who work for or in Winjdows or 
Unix/Linux environments, often if they support COBOL development, they do 
NOT support PL/I development.  This doesn't mean that such compilers don't 
exist, only that those shops do not have the compilers or allow them to be 
used for development.

All of this is in addition to the number of participants in this group who 
don't even have or do COBOL development any more.  The one thing that I 
think is fairly certain is that there are few (if any other than Robin) 
participants in this forum that do NOT currently do COBOL devlopment but do 
do PL/I development.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 6)_

- **From:** "robin" <robin51@dodo.mapson.com.au>
- **Date:** 2011-01-26T22:24:20+11:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<4d400471$0$88214$c30e37c6@exi-reader.telstra.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <4d3d691a$0$88227$c30e37c6@exi-reader.telstra.net> <4l7rj6tqvf5vj1t367fembll2fon5uqsnu@4ax.com> <4d3ee002$0$88217$c30e37c6@exi-reader.telstra.net> <nzR%o.340760$Ph5.198741@en-nntp-07.dc1.easynews.com>`

```
"Bill Klein" <wmklein@noreply.ix.netcom.com> wrote in message 
news:nzR%o.340760$Ph5.198741@en-nntp-07.dc1.easynews.com...
| "robin" <robin51@dodo.mapson.com.au> wrote in message
| news:4d3ee002$0$88217$c30e37c6@exi-reader.telstra.net...
…[14 more quoted lines elided]…
| negative numbers)

According to Howard, it doesn't.

| - does it consistantly (across platforms and vendors)

Accordinmg to Howard, it doesn't.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2011-01-26T09:00:17-07:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<68h0k6p4ae8vqvhgr6s587mlj10qpprvj5@4ax.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <4d3d691a$0$88227$c30e37c6@exi-reader.telstra.net> <4l7rj6tqvf5vj1t367fembll2fon5uqsnu@4ax.com> <4d3ee002$0$88217$c30e37c6@exi-reader.telstra.net> <nzR%o.340760$Ph5.198741@en-nntp-07.dc1.easynews.com> <4d400471$0$88214$c30e37c6@exi-reader.telstra.net>`

```
On Wed, 26 Jan 2011 22:24:20 +1100, "robin"
<robin51@dodo.mapson.com.au> wrote:

>| Actually, if you try it with existing COBOL's, check any manual or check the
>| current or PAST COBOL Standards (or simply read all the notes in this
…[8 more quoted lines elided]…
>Accordinmg to Howard, it doesn't. 

Not according to me.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 8)_

- **From:** "robin" <robin51@dodo.mapson.com.au>
- **Date:** 2011-01-27T11:32:12+11:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<4d40bd1b$0$88227$c30e37c6@exi-reader.telstra.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <4d3d691a$0$88227$c30e37c6@exi-reader.telstra.net> <4l7rj6tqvf5vj1t367fembll2fon5uqsnu@4ax.com> <4d3ee002$0$88217$c30e37c6@exi-reader.telstra.net> <nzR%o.340760$Ph5.198741@en-nntp-07.dc1.easynews.com> <4d400471$0$88214$c30e37c6@exi-reader.telstra.net> <68h0k6p4ae8vqvhgr6s587mlj10qpprvj5@4ax.com>`

```
"Howard Brazee" <howard@brazee.net> wrote in message news:68h0k6p4ae8vqvhgr6s587mlj10qpprvj5@4ax.com...
| On Wed, 26 Jan 2011 22:24:20 +1100, "robin"
| <robin51@dodo.mapson.com.au> wrote:
…[13 more quoted lines elided]…
| Not according to me.

Sorry, that was Pete.
I looked thru the chain of posters and your name came up.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 6)_

- **From:** Peter Flass <Peter_Flass@Yahoo.com>
- **Date:** 2011-01-26T09:23:21-05:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<ihpap1$pu0$1@news.eternal-september.org>`
- **In-Reply-To:** `<nzR%o.340760$Ph5.198741@en-nntp-07.dc1.easynews.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <4d3d691a$0$88227$c30e37c6@exi-reader.telstra.net> <4l7rj6tqvf5vj1t367fembll2fon5uqsnu@4ax.com> <4d3ee002$0$88217$c30e37c6@exi-reader.telstra.net> <nzR%o.340760$Ph5.198741@en-nntp-07.dc1.easynews.com>`

```
On 1/26/2011 4:11 AM, Bill Klein wrote:
>
> As far as I know, PL/I is also consistant for portability across platforms
> and vendors; it just doesn't have a currently maintained and enhanced
> Standard against which vendors and implementors can compare it.

Unfortunately somewhat true.  Most compilers support at least Subset G, 
but the real standard seems to be "whatever IBM implements."

>
> I might be interested in how many participants in ths group actually work in
…[15 more quoted lines elided]…
>

I don't really count here, but I'll chip in anyway.  PPOE is a mainframe 
shop supporting both COBOL and PL/I, though mostly COBOL.  I personally 
haven't written any COBOL since the 1970's, but did a lot of PL/I up 
until I left.

Obviously with Iron Spring I do a lot of PL/I on Linux ;-)  I'm hoping 
that the availability of a reasonably priced and easily available 
compiler - none of this "request a quote" stuff - will increase PL/I 
usage on Linux.

The compiler still isn't quite ready for prime time.  I'm keeping it a 
beta, and current users are finding lots of odd bits of the language, or 
odd coding errors, that still cause problems, but it's still quite 
usable.  Next release: multi-tasking.

http://www.iron-spring.com
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-27T11:18:57+13:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<8qbkujFm45U1@mid.individual.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <4d3d691a$0$88227$c30e37c6@exi-reader.telstra.net> <4l7rj6tqvf5vj1t367fembll2fon5uqsnu@4ax.com> <4d3ee002$0$88217$c30e37c6@exi-reader.telstra.net> <nzR%o.340760$Ph5.198741@en-nntp-07.dc1.easynews.com> <ihpap1$pu0$1@news.eternal-september.org>`

```
Peter Flass wrote:
> On 1/26/2011 4:11 AM, Bill Klein wrote:
>>
…[42 more quoted lines elided]…
> http://www.iron-spring.com

Good luck with it, Peter.

I always liked PL/I as a language.

Pete.
```

###### ↳ ↳ ↳ Re: Rounding

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-25T12:24:23+13:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<8q6g18FdktU1@mid.individual.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <4d3d691a$0$88227$c30e37c6@exi-reader.telstra.net>`

```
robin wrote:
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
> news:8pn774FcdhU1@mid.individual.net...
…[20 more quoted lines elided]…
> The ROUND function in PL/I will correctly round up regardless of sign.

Thanks for your observation, Robin. (It is immensely amusing to me to have 
someone logged in as "robin" talking about "rounding", but it doesn't make 
your observation any less valid. :-))

This was already noted and I agreed that I had only ever used it in cases 
where I knew the value was positive. Perhaps reading the whole thread might 
save superfluous posts in future?

Pete.
```

###### ↳ ↳ ↳ Re: Rounding

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2011-01-24T18:26:03-06:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<CMo%o.596669$pX3.297011@en-nntp-11.dc1.easynews.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <4d3d691a$0$88227$c30e37c6@exi-reader.telstra.net>`

```
For Robin or anyone else who hadn't checked the actual COBOL rules, the 
following is what the next of the current COBOL Standard says (inpart),

"When rounding is requested, the absolute value of the resultant identifier 
is increased by one in the low-order position whenever the most significant 
digit of the excess is greater than or equal to five."

This is BEFORE all the new variations introduced in the current draft of the 
next ANSI/ISO COBOL Standard. (See separate post in this thread)

"robin" <robin51@dodo.mapson.com.au> wrote in message 
news:4d3d691a$0$88227$c30e37c6@exi-reader.telstra.net...
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
> news:8pn774FcdhU1@mid.individual.net...
…[23 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 4)_

- **From:** "robin" <robin51@dodo.mapson.com.au>
- **Date:** 2011-01-26T10:36:06+11:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<4d3f5e72$0$88217$c30e37c6@exi-reader.telstra.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <4d3d691a$0$88227$c30e37c6@exi-reader.telstra.net> <CMo%o.596669$pX3.297011@en-nntp-11.dc1.easynews.com>`

```
"Bill Klein" <wmklein@noreply.ix.netcom.com> wrote in message 
news:CMo%o.596669$pX3.297011@en-nntp-11.dc1.easynews.com...
| For Robin or anyone else who hadn't checked the actual COBOL rules, the
| following is what the next of the current COBOL Standard says (inpart),

That's entireley irrelevant.  Pete specified adding 0.05 in his code.
I pointed out that that won't correctly round when the value is negative.

| "When rounding is requested, the absolute value of the resultant identifier
| is increased by one in the low-order position whenever the most significant
| digit of the excess is greater than or equal to five."

In any case, the above specification is inadequate because
it states that the absolute value of the identifier it taken.
In other words, a negative value loses its negative sign!

| This is BEFORE all the new variations introduced in the current draft of the
| next ANSI/ISO COBOL Standard. (See separate post in this thread)
…[26 more quoted lines elided]…
| > The ROUND function in PL/I will correctly round up regardless of sign.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 5)_

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2011-01-26T03:21:25-06:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<xIR%o.154064$Mg5.99808@en-nntp-06.dc1.easynews.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <4d3d691a$0$88227$c30e37c6@exi-reader.telstra.net> <CMo%o.596669$pX3.297011@en-nntp-11.dc1.easynews.com> <4d3f5e72$0$88217$c30e37c6@exi-reader.telstra.net>`

```
"robin" <robin51@dodo.mapson.com.au> wrote in message 
news:4d3f5e72$0$88217$c30e37c6@exi-reader.telstra.net...
> "Bill Klein" <wmklein@noreply.ix.netcom.com> wrote in message
> news:CMo%o.596669$pX3.297011@en-nntp-11.dc1.easynews.com...
…[15 more quoted lines elided]…
>
Simply WRONG.

It says that the absolute value of the RESTING identifier is increased.  It 
doesn't say anything about changing the sign of the resulting identifier.

The rule is, of course correct, and is how all COBOL implementations do it.
  Correct, portable, and consistant with the current (and post) ANSI and ISO 
Standards.

Robin,
  If you would like access to the current Standard (or the draft of the next 
one), I would be happy to provide you the links.  Similarly, the links to a 
number of vendors' COBOL language references are easily available online. 
Should you have COBOL source code that you would like anyone to test for you 
(if you don't have access to a compiler yourself), I am certain that I or 
many others in this group would be willing to run a test for you.

Any ongoing statement that COBOL doesn't do rounded "correctly" (if what you 
want is "round to nearest") for negative numbers is simply wrong.

As far as Pete's technique goes, it was (is?) one that he used - but said in 
other posts that he eithere didn't test with negative numbers or didn't need 
to handle negative numbers.  I am certain were he to code a COBOL program 
today that needed to round negative (and positive) numbes hew ould use a 
technique that would work correclty.  Whether he would use the COBOL 
"ROUNDED" syntax or an explicit arithmetic statement is something that he 
would consider when the time came.  Given his current work (known to many 
frequent participantes in this group), I find it unlikely that he will need 
to make such a choice, but one never knows.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 6)_

- **From:** "robin" <robin51@dodo.mapson.com.au>
- **Date:** 2011-01-26T22:50:34+11:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<4d400a97$0$88227$c30e37c6@exi-reader.telstra.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <4d3d691a$0$88227$c30e37c6@exi-reader.telstra.net> <CMo%o.596669$pX3.297011@en-nntp-11.dc1.easynews.com> <4d3f5e72$0$88217$c30e37c6@exi-reader.telstra.net> <xIR%o.154064$Mg5.99808@en-nntp-06.dc1.easynews.com>`

```
"Bill Klein" <wmklein@noreply.ix.netcom.com> wrote in message news:xIR%o.154064$Mg5.99808@en-nntp-06.dc1.easynews.com...
| "robin" <robin51@dodo.mapson.com.au> wrote in message
| news:4d3f5e72$0$88217$c30e37c6@exi-reader.telstra.net...
…[14 more quoted lines elided]…
| > In other words, a negative value loses its negative sign!

| Simply WRONG.

Of course it [the specification] is wrong.
Yet, that's what it means.

| It says that the absolute value of the RESTING identifier is increased.

What's a resting identifier?

|  It doesn't say anything about changing the sign of the resulting identifier.

You need to read what is says, not what you think that it means.

| The rule is, of course correct,

The rule is incorrect as the standard now stands.

| and is how all COBOL implementations do it.
|  Correct, portable, and consistant with the current (and post) ANSI and ISO
| Standards.

Not according to Pete.  You should take it up with him.

|  If you would like access to the current Standard [nonsense deleted].

| Any ongoing statement that COBOL doesn't do rounded "correctly" (if what you
| want is "round to nearest") for negative numbers is simply wrong.
…[3 more quoted lines elided]…
| to handle negative numbers.

The example he gave was for signed values, where he added 0.05.
I merely pointed out that this would give wrong results for negative values.

You should take up that issue with him.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-27T02:39:13+13:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<8qamg3FjlmU1@mid.individual.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <4d3d691a$0$88227$c30e37c6@exi-reader.telstra.net> <CMo%o.596669$pX3.297011@en-nntp-11.dc1.easynews.com> <4d3f5e72$0$88217$c30e37c6@exi-reader.telstra.net> <xIR%o.154064$Mg5.99808@en-nntp-06.dc1.easynews.com> <4d400a97$0$88227$c30e37c6@exi-reader.telstra.net>`

```
robin wrote:
> "Bill Klein" <wmklein@noreply.ix.netcom.com> wrote in message
> news:xIR%o.154064$Mg5.99808@en-nntp-06.dc1.easynews.com...
…[30 more quoted lines elided]…
> What's a resting identifier?

A little caution here. The man you are arguing with is quite severely 
visually impaired. He sometimes makes errors like this. Try substituting 
"RESULTING" for "RESTING" back in the original context and you can see that 
he is taking issue with your contention that a negative value loses its 
sign. Here's the whole exchange, in context with spelling errors by both 
parties corrected:
==================================================
>
> In any case, the above specification is inadequate because
> it states that the absolute value of the identifier is taken.
> In other words, a negative value loses its negative sign!
>
Simply WRONG.

It says that the absolute value of the RESULTING identifier is increased. 
It
doesn't say anything about changing the sign of the resulting identifier.
==================================================

>
>>  It doesn't say anything about changing the sign of the resulting
>> identifier.
>
> You need to read what is says, not what you think that it means.

One of you certainly does... :-)

>
>> The rule is, of course correct,
…[7 more quoted lines elided]…
> Not according to Pete.  You should take it up with him.

No, YOU should take it up with me. If you were to do so I could correct your 
misunderstanding of what I said. I never mentioned anything about standards. 
I related an incident that occurred which shook my faith in ROUNDED as a 
COBOL construct. Bill says the standard is clear and I believe him. 
(Experience over many years here has shown that he is usually right in these 
matters.)
>
>>  If you would like access to the current Standard [nonsense deleted].

If you are arguing based on a standard and someone offers to help, when does 
that become "nonsense"?

>
>> Any ongoing statement that COBOL doesn't do rounded "correctly" (if
…[11 more quoted lines elided]…
> You should take up that issue with him.

Robin, a number of points here.

1. You haven't read the whole thread, or if you have, you are conveniently 
ignoring parts of it. I already responded to you, specifically saying that 
the technique I posted was not intended for cases where the numbers could be 
negative. Before that, I had posted the same qualifier, to the thread 
generally, when Clark raised the point about negative numbers (before you 
did). It is standard practice in COBOL for pictures to have signs even when 
the fields they represent cannot be negative. This may have caused some 
confusion. No-one, not even me :-), is disputing that you were correct about 
negative numbers. We had already noted it before you posted.

2. You have attributed comments to Howard which he never made. (They are 
actually misquotes of what you think I said.)

3. Bill Klein is one of the top people in the world on the COBOL standard 
and has spent many years of his life working for the betterment of COBOL. If 
he says your interpretation of the standard is wrong, you better believe 
it.(Or have a very clear copy of the text, in crayon with non-joined-up 
writing to hand :-)) In terms of the COBOL standard, if Bill Klein said the 
sun wasn't going to rise tomorrow, I would buy a candle. Show a little more 
respect and listen to what he's saying.

You DID misunderstand the standard (just as you have misquoted what I said). 
Read the posts.

I've been trying to understand how this happened (I don't believe there was 
any malice by any party involved). I think it is because things which a 
COBOL programmer takes as a matter of course (like signs on numeric pictures 
irrespective of the value domain) and words with loaded meanings like 
"absolute value", may have different shades of meaning in terms of a 
different language like PL/1. This means that someone with that background 
perceives them differently. It may be only a very slight shade of difference 
but it is enough to cause an argument... :-)

I did make a statement that I believed (under some very strange and unusual 
circumstances) the ROUNDED feature in COBOL may give inconsistent results. I 
may be right, I may be wrong, it doesn't matter. If I don't use it (and I 
don't) I don't encounter problems. Bill says he believes it is consistent, 
and he is usually right on things pertaining to Standard COBOL. (However, 
not every implementation of Standard COBOL is flawless...).

I am staggered at the results of posting what I thought was a simple 
succinct solution, but I have learned much so I guess it isn't all a waste 
:-)

I don't think I have much more to say on this, so please feel free to have 
the last word (at least as far as I'm concerned... :-))

Pete.
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-27T01:39:49+13:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<8qaj0oFqclU1@mid.individual.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <8pn774FcdhU1@mid.individual.net> <4d3d691a$0$88227$c30e37c6@exi-reader.telstra.net> <CMo%o.596669$pX3.297011@en-nntp-11.dc1.easynews.com> <4d3f5e72$0$88217$c30e37c6@exi-reader.telstra.net> <xIR%o.154064$Mg5.99808@en-nntp-06.dc1.easynews.com>`

```
Bill Klein wrote:
> "robin" <robin51@dodo.mapson.com.au> wrote in message
> news:4d3f5e72$0$88217$c30e37c6@exi-reader.telstra.net...
…[47 more quoted lines elided]…
> make such a choice, but one never knows.

Thank you, Bill. Right on the nail and I couldn't have said it better.

Pete.
```

#### ↳ Re: Rounding

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-01-26T15:31:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CdednXLuTY03D93QnZ2dnUVZ_uadnZ2d@earthlink.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com>`

```
jmoore wrote:
> What is the best way to round up 4.88 to 4.9 and not 5. The input
> comes in as 2 decimals but is being moved to a 9(7)v9 field.

The classic way of rounding is to add one-half of the lowest level of 
precision.

If you want rounding to 1 decimal place, you add 0.05 to the number. If you 
want two decimal places of precision, you add 0.005 to the number.
```

##### ↳ ↳ Re: Rounding

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-27T11:24:09+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qbl8bFofmU1@mid.individual.net>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <CdednXLuTY03D93QnZ2dnUVZ_uadnZ2d@earthlink.com>`

```
HeyBub wrote:
> jmoore wrote:
>> What is the best way to round up 4.88 to 4.9 and not 5. The input
…[7 more quoted lines elided]…
> number.

Yes Jerry,

that was (pretty much) what I said....

Then all Hell broke loose... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Rounding

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-02-06T06:58:50-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<-66dnbm6zPKWBtPQnZ2dnUVZ_qCdnZ2d@earthlink.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <CdednXLuTY03D93QnZ2dnUVZ_uadnZ2d@earthlink.com> <8qbl8bFofmU1@mid.individual.net>`

```
Pete Dashwood wrote:
> HeyBub wrote:
>> jmoore wrote:
…[15 more quoted lines elided]…
>

I guess it's all in the way you say it:

Elderly gentleman slowly regains consciousness in the recovery room. He sees 
a woman in the room.

"Nurse! Are my testicles black?"

"I'm sorry sir, I'm just an aide. Let me get you a nurse..."

"No, no! I've got to know! I can't wait! Please! ARE MY TESTICLES BLACK? !!"

The aide, feeling compassion, walks over to the bed, slowly lifts the sheets 
and examines the poor man's testicles - up, down, left, right. She turns 
them over, raises them gently to peer underneath. Finally she gently lowers 
them and replaces the sheets.

"Sir, your testicles seem just fine."

"I really appreciate your gentle massage, miss. It was very nice.  But, 
please, I still need to know: are my test results back?"
```

###### ↳ ↳ ↳ Re: Rounding

_(reply depth: 4)_

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2011-02-07T03:15:20-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33ffeefc-0970-414e-a47b-3858e63cd449@w6g2000vbo.googlegroups.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <CdednXLuTY03D93QnZ2dnUVZ_uadnZ2d@earthlink.com> <8qbl8bFofmU1@mid.individual.net> <-66dnbm6zPKWBtPQnZ2dnUVZ_qCdnZ2d@earthlink.com>`

```
On Feb 6, 12:58 pm, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> Pete Dashwood wrote:
> > HeyBub wrote:
…[38 more quoted lines elided]…
> - Show quoted text -

GROAN!
```

##### ↳ ↳ Re: Rounding

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2011-01-26T15:51:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a991k6lcd95bcuf6v429mrka5h81nno11b@4ax.com>`
- **References:** `<c0d054fb-8b4e-4a97-b299-ef153d4fc7be@32g2000yqz.googlegroups.com> <CdednXLuTY03D93QnZ2dnUVZ_uadnZ2d@earthlink.com>`

```
On Wed, 26 Jan 2011 15:31:21 -0600, "HeyBub" <heybub@NOSPAMgmail.com>
wrote:

>> What is the best way to round up 4.88 to 4.9 and not 5. The input
>> comes in as 2 decimals but is being moved to a 9(7)v9 field.
…[5 more quoted lines elided]…
>want two decimal places of precision, you add 0.005 to the number. 

Then the way that rounds either up or down from .5 to create an even
number is - what?   neo-classic?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
