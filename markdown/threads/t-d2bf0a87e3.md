[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IF

_6 messages · 5 participants · 1998-10_

---

### IF

- **From:** "Ben Maler" <benmaler@netvision.net.il>
- **Date:** 1998-10-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6v952n$go9$1@news.netvision.net.il>`

```
HOW IS THE "IF" STATEMENT GOES ??????
```

#### ↳ Re: IF

- **From:** The Goobers <docdwarf@erols.com>
- **Date:** 1998-10-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3618216B.B70@erols.com>`
- **References:** `<6v952n$go9$1@news.netvision.net.il>`

```
Ben Maler wrote:
> 
> HOW IS THE "IF" STATEMENT GOES ??????

Please do your own homework.

DD
```

#### ↳ Re: IF

- **From:** SkidMike <skidmike@~NOSPAM~mindspring.com>
- **Date:** 1998-10-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6v99cv$k2h$1@camel19.mindspring.com>`
- **References:** `<6v952n$go9$1@news.netvision.net.il>`

```
if <condition> then
    <do something>
end-if

or, if i understand the sample code sent to me to help me out you can
skip "if" and use "evaluate....when <something> <do something>,
end-evaluate.  is evaluate preferred over if?
```

##### ↳ ↳ Re: IF

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-10-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-D5O03Y4PZYvM@Dwight_Miller.iix.com>`
- **References:** `<6v952n$go9$1@news.netvision.net.il> <6v99cv$k2h$1@camel19.mindspring.com>`

```
On Mon, 5 Oct 1998 02:02:47, SkidMike 
<skidmike@~NOSPAM~mindspring.com> wrote:

> if <condition> then
>     <do something>
…[4 more quoted lines elided]…
> end-evaluate.  is evaluate preferred over if?

Different purposes with some overlap.

As a GENERAL rule, if you have an IF IMMEDIATELY after an ELSE with no
other intervening code - consider using Evaluate instead.
```

##### ↳ ↳ Re: IF

- **From:** "kennet" <kennet@post11.tele.dk>
- **Date:** 1998-10-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vaunj$5juq$1@news-inn.inet.tele.dk>`
- **References:** `<6v952n$go9$1@news.netvision.net.il> <6v99cv$k2h$1@camel19.mindspring.com>`

```
I prefer EVALUATE if I would otherwise need nested IF's.

Kennet

SkidMike skrev i meddelelsen <6v99cv$k2h$1@camel19.mindspring.com>...
>if <condition> then
>    <do something>
…[4 more quoted lines elided]…
>end-evaluate.  is evaluate preferred over if?
```

#### ↳ Re: IF

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1998-10-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3618a075.5472198@news2.ibm.net>`
- **References:** `<6v952n$go9$1@news.netvision.net.il>`

```
On Mon, 5 Oct 1998 01:05:20 +0200, "Ben Maler" <benmaler@netvision.net.il> wrote:

>HOW IS THE "IF" STATEMENT GOES ??????
>

oh, simple, one step at a time


with kind regards

Volker Bandke
(BSP GmbH)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
