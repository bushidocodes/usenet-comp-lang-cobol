[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Binary Dates

_7 messages · 6 participants · 1998-09_

---

### Binary Dates

- **From:** Manzari <pmanzari@arrow.com>
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35F94195.4644@arrow.com>`

```
It's amazing how many people will try so hard to prove themselves rude,
inconsiderate morons.  If anyone who worked for me responded in such a
manner to a polite question from a colleague, they would be out the door
so fast their head would spin.

Anyway, in answer to your question...

An S9(4) COMP field is a 2 byte binary, or halfword field.  To determine
if a CCCCMMDD date field will fit, you need to know the largest value
that will fit into a halfword field.  The largest value is x'FFFF' or
65,535.  Therefore, a date in the format you describe will not fit.
```

#### ↳ Re: Binary Dates

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35F9B69C.F3880B2A@att.net>`
- **References:** `<35F94195.4644@arrow.com>`

```
Manzari wrote:
> 
> It's amazing how many people will try so hard to prove themselves rude,
…[9 more quoted lines elided]…
> 65,535.  Therefore, a date in the format you describe will not fit.

Bloody Hell! This guy again, same answer as before. BYAM, it's not worth
a double posting.

Bill Lynch
```

#### ↳ Re: Binary Dates

- **From:** docdwarf@clark.net ()
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tbhct$1ve$1@callisto.clark.net>`
- **References:** `<35F94195.4644@arrow.com>`

```
In article <35F94195.4644@arrow.com>, Manzari  <pmanzari@arrow.com> wrote:
>It's amazing how many people will try so hard to prove themselves rude,
>inconsiderate morons.  If anyone who worked for me responded in such a
>manner to a polite question from a colleague, they would be out the door
>so fast their head would spin.

Mr Manzari, I am a consultant... I do not work *for* people, I work *with*
people... but, be that as it may...

... what would be your response if 'any of the people who worked for me'
continued to ask questions which demonstrated a lack of fundamental
knowledge and a total unwillingness to perform even the most basic
research on their own?  How long would they be allowed to remain 'in the
door'?

DD
```

##### ↳ ↳ Re: Binary Dates

- **From:** Jeff Farkas <Jeffrey.Farkas@gte.net>
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tbk4b$545$1@news-1.news.gte.net>`
- **References:** `<35F94195.4644@arrow.com> <6tbhct$1ve$1@callisto.clark.net>`

```
docdwarf@clark.net wrote:
> 
> In article <35F94195.4644@arrow.com>, Manzari  <pmanzari@arrow.com> wrote:
…[14 more quoted lines elided]…
> DD
===================================================================================
    Well Mr. Manzari, I find it difficult to work with ï¿½Colleaguesï¿½ who
can not
perform rudimentary research before asking questions such as the one
posted 
by Wei Lu. Before posting a question to this group I would hope that the
person
would have a least attempted to resolve the problem themselves.  If  the
person
 in question does not care enough to put some effort into their own
problem/question why should anybody else?   

Oh and by the way Mr. Manzari, I do answer all of the questions that my 
ï¿½colleaguesï¿½ ask me.  From time to time I may poke fun at them and they
do the same to me. But it is all in good fun and done with the knowledge 
that we all ask some really dumb questions every now and then and 
it does not hurt to be reminded of that.
```

###### ↳ ↳ ↳ Re: Binary Dates -

- **From:** Jeff Farkas <Jeffrey.Farkas@gte.net>
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tbl57$545$2@news-1.news.gte.net>`
- **References:** `<35F94195.4644@arrow.com> <6tbhct$1ve$1@callisto.clark.net> <6tbk4b$545$1@news-1.news.gte.net>`

```
Jeff Farkas wrote:
> 
> docdwarf@clark.net wrote:
…[17 more quoted lines elided]…
> ===================================================================================
Well Mr. Manzari, I find it difficult to work with ï¿½Colleaguesï¿½ 
who can not perform rudimentary research before asking questions
such as the one posted  by Wei Lu. Before posting a question
to this group I would hope that the person would have a least
attempted to resolve the problem themselves.  If  the person
 in question does not care enough to put some effort into
their own problem/question why should anybody else?   

Oh and by the way Mr. Manzari, I do answer all of the questions
that my ï¿½colleaguesï¿½ ask me.  From time to time I may poke fun
at them and they do the same to me. But it is all in good
fun and done with the knowledge that we all ask some really
dumb questions every now and then and it does not hurt
to be reminded of that from time to time.
```

#### ↳ Re: Binary Dates

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aJeK1.152$pB3.577230@news1.atlantic.net>`
- **References:** `<35F94195.4644@arrow.com>`

```

Manzari wrote in message <35F94195.4644@arrow.com>...
>It's amazing how many people will try so hard to prove themselves rude,
>inconsiderate morons.  If anyone who worked for me responded in such a
…[8 more quoted lines elided]…
>65,535.  Therefore, a date in the format you describe will not fit.

COMP does not, necessarily, mean binary. The method for storing
COMP data items is implementor defined.

There are no halfwords in COBOL.

The maximum value that will fit into a data item that is defined as
S9(4), is +/- 9999. Storage of any value outside that range is
implementor defined.

A more appropriate answer would be "No, you can't put an 8 digit
number in a 4 digit field!" Of course, that answer would have been
obvious to anyone who had done their homework.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

#### ↳ Re: Binary Dates

- **From:** WOB@my-dejanews.com
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tc0ag$k76$1@nnrp1.dejanews.com>`
- **References:** `<35F94195.4644@arrow.com>`

```
In article <35F94195.4644@arrow.com>,
  Manzari <pmanzari@arrow.com> wrote:
> It's amazing how many people will try so hard to prove themselves rude,
> inconsiderate morons.  If anyone who worked for me responded in such a
…[9 more quoted lines elided]…
>

X'FFFF' in an aligned or unaligned signed-halfword is -1. The largest positive
value would be H'32767' or X'7FFF'. Keeping this in mind, beware of TRUNC(OPT)
in your compiler options. This will get you every time. Only TRUNC(BIN) will
ensure that the maximum value can be attained. TRUNC(OPT) will truncate the
number of digits, based upon the PICTURE.

God helps those who help themselves. In this case, there seemed to be ZERO
effort on the part of the original poster in this regard to solve the problem
himself. Therefore, scathing replies were warranted and necessary. I sure hope
the people that work for you understand binary a little bit better.

WOB

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
