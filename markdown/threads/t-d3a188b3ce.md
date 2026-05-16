[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# i need help to write a cobol program as soon as possible

_7 messages · 6 participants · 2000-10_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### i need help to write a cobol program as soon as possible

- **From:** gz11375@my-deja.com
- **Date:** 2000-10-09T02:01:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8rr8u9$43$1@nnrp1.deja.com>`

```
I need help!!!  To write a cobol program by this thursday or so.  Can
someone please help me???
Here is the question
Given two related dates,(eg: start and end of the World War !!) find
the number od days, the number of months and the number of
years/months/days between the two dates.

If it is interactive, submit your disk with the correct .int file on it.
If you are using files, include a copy of both the input and output
files...
If there is someone who can help me please email me .. gz11375@aol.com


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: i need help to write a cobol program as soon as possible

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8rsffq$rr7$1@news.igs.net>`
- **References:** `<8rr8u9$43$1@nnrp1.deja.com>`

```
Nobody will do your homework for you.

gz11375@my-deja.com wrote in message <8rr8u9$43$1@nnrp1.deja.com>...
>I need help!!!  To write a cobol program by this thursday or so.  Can
>someone please help me???
…[12 more quoted lines elided]…
>Before you buy.
```

#### ↳ Re: i need help to write a cobol program as soon as possible

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E1C4EB.8827247@brazee.net>`
- **References:** `<8rr8u9$43$1@nnrp1.deja.com>`

```


gz11375@my-deja.com wrote:
> 
> I need help!!!  To write a cobol program by this thursday or so.  Can
> someone please help me???

Please tell us your compiler and operating system, as well as what you
have tried so far, along with the results you have found.

And in this case, what further limits you have on your work.  (With
modern date functions, the problem is too trivial to be used in
homework, so I imagine you were told to figure it out some other way). 
I suspect you are very early in your course, so it may be that you
haven't yet started using tables, and I know you haven't read this
newsgroup's FAQ.
```

#### ↳ Re: i need help to write a cobol program as soon as possible

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fpvE5.319$8F.125775@nnrp1.sbc.net>`
- **References:** `<8rr8u9$43$1@nnrp1.deja.com>`

```
ACCEPT START-DATE.
ACCEPT END-DATE
COMPUTE NUM-DAYS = some code
COMPUTE NUM-MONTHS = some other code
COMPUTE NUM-YEARS = some different code
DISPLAY NUM-DAYS NUM-MONTHS NUM-YEARS.
STOP RUN.

Glad to be of help.


<gz11375@my-deja.com> wrote in message
news:8rr8u9$43$1@nnrp1.deja.com...
> I need help!!!  To write a cobol program by this thursday or so.
Can
> someone please help me???
> Here is the question
…[4 more quoted lines elided]…
> If it is interactive, submit your disk with the correct .int file on
it.
> If you are using files, include a copy of both the input and output
> files...
> If there is someone who can help me please email me ..
gz11375@aol.com
>
>
> Sent via Deja.com http://www.deja.com/
> Before you buy.
>
```

##### ↳ ↳ Re: i need help to write a cobol program as soon as possible

- **From:** J@nowhere.moc (J)
- **Date:** 2000-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PhHE5.2961$Df7.282344@cletus.bright.net>`
- **References:** `<8rr8u9$43$1@nnrp1.deja.com> <fpvE5.319$8F.125775@nnrp1.sbc.net>`

```
You really should put some spaces in the display or all the numbers will run 
together

DISPLAY NUM-DAYS "  " NUM-MONTHS "  " NUM-YEARS.

Other than that this will work...



In article <fpvE5.319$8F.125775@nnrp1.sbc.net>, "Jerry P" <jerryp@bisusa.com> 
wrote:
>ACCEPT START-DATE.
>ACCEPT END-DATE
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: i need help to write a cobol program as soon as possible

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qlNE5.73$wV1.71869@nnrp2.sbc.net>`
- **References:** `<8rr8u9$43$1@nnrp1.deja.com> <fpvE5.319$8F.125775@nnrp1.sbc.net> <PhHE5.2961$Df7.282344@cletus.bright.net>`

```
I wanted to keep it simple.


"J" <J@nowhere.moc> wrote in message
news:PhHE5.2961$Df7.282344@cletus.bright.net...
> You really should put some spaces in the display or all the numbers
will run
> together
>
…[6 more quoted lines elided]…
> In article <fpvE5.319$8F.125775@nnrp1.sbc.net>, "Jerry P"
<jerryp@bisusa.com>
> wrote:
> >ACCEPT START-DATE.
…[9 more quoted lines elided]…
>
```

#### ↳ Re: i need help to write a cobol program as soon as possible

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-10-09T02:13:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6R9E5.13706$l35.226357@iad-read.news.verio.net>`
- **References:** `<8rr8u9$43$1@nnrp1.deja.com>`

```
In article <8rr8u9$43$1@nnrp1.deja.com>,  <gz11375@my-deja.com> wrote:
>I need help!!!

You need to do your own homework.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
