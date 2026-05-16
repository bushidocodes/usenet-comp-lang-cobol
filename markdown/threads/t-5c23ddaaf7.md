[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Rounding timings

_6 messages · 3 participants · 2007-09_

---

### Rounding timings

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-20T22:31:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4e6f3p01lij7o99aq1fsr0kgg07s88qgt@4ax.com>`

```
01  A binary pic s9(09)v9(04) value 1.005.
01  B pic s9(09)v9(02).
01  E pic z(09).9(02)-.

Move A to B                     790
Compute B = A                830
Compute B rounded = A  860
Compute B = A + .005    980
Compute B = A + (function sign(A) * .005)  9,580
If A is negative               1320
compute E rounded = A 1410

Excemptng function sign, which is a disaster, there isn't a huge difference between the
forms. They all reflect the slowness of display numbers.
```

#### ↳ Re: Rounding timings

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-21T04:40:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DWHIi.503953$Bo7.404419@fe07.news.easynews.com>`
- **References:** `<b4e6f3p01lij7o99aq1fsr0kgg07s88qgt@4ax.com>`

```
and in all cases confirm that using the ROUNDED phrase is faster (no matter how 
much) than doing the arithmetic yourself.

Now, can you admit it, that was what the original recommendation said?

How much impact this could have on an application would depend upon how much 
rounding (and in what constructs) there  were, but the original recommendation 
("myth") certainly seems confirmed.
```

##### ↳ ↳ Re: Rounding timings

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-21T19:45:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j3p8f3d4g88pdf4ld48bhuc722bbkd2es3@4ax.com>`
- **References:** `<b4e6f3p01lij7o99aq1fsr0kgg07s88qgt@4ax.com> <DWHIi.503953$Bo7.404419@fe07.news.easynews.com>`

```
On Fri, 21 Sep 2007 04:40:03 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>and in all cases confirm that using the ROUNDED phrase is faster (no matter how 
>much) than doing the arithmetic yourself.
…[5 more quoted lines elided]…
>("myth") certainly seems confirmed.

Correct. I didn't say the test results busted a myth. I don't recall the conversation that
prompted my running this test. People keep starting new threads for no good reason,
thereby making it difficult to trace a thread backward.
```

###### ↳ ↳ ↳ Re: Rounding timings

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-22T02:23:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<W0%Ii.519352$Bo7.310763@fe07.news.easynews.com>`
- **References:** `<b4e6f3p01lij7o99aq1fsr0kgg07s88qgt@4ax.com> <DWHIi.503953$Bo7.404419@fe07.news.easynews.com> <j3p8f3d4g88pdf4ld48bhuc722bbkd2es3@4ax.com>`

```
Robert,
  It seems pretty easy for me to find what you originally said - and contrary to 
what you say below, you DID claim to "but the myth" for ROUNDED.  Here are your 
original words,

"Proposition: "Do not use the REMAINDER, ROUNDED, ON SIZE ERROR or CORRESPONDING 
phrases if
you want the fastest performance. No optimization is done on arithmetic 
statements if the
ON SIZE ERROR phrase is used. For this reason, we recommend you do not use this 
phrase if
high performance is required. The ROUNDED  phrase impacts performance, but it is 
generally
faster to use ROUNDED than try to round the result using your own routine. "

Test:
compute binary-number rounded = binary-number + 1       *> 1 us (no penalty)
add 1 to binary-number                                                        *> 
15 us
       on size error display 'overflow'
end-add

Finding: busted for rounded, confirmed for size error."

   ***

Obviously, the test itself has changed, but you have never retracted your 
original claim to have "busted" the myth for ROUNDED>
```

###### ↳ ↳ ↳ Re: Rounding timings

_(reply depth: 4)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-22T00:36:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tr99f3d1m4ttoaqh1465coso39i2uprjl0@4ax.com>`
- **References:** `<b4e6f3p01lij7o99aq1fsr0kgg07s88qgt@4ax.com> <DWHIi.503953$Bo7.404419@fe07.news.easynews.com> <j3p8f3d4g88pdf4ld48bhuc722bbkd2es3@4ax.com> <W0%Ii.519352$Bo7.310763@fe07.news.easynews.com>`

```
On Sat, 22 Sep 2007 02:23:51 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>Robert,
>  It seems pretty easy for me to find what you originally said - and contrary to 
…[25 more quoted lines elided]…
>original claim to have "busted" the myth for ROUNDED>

After several people pointed out there's no rounding in the integer arithmetic of number +
1, I changed it to number + .5. Results were much slower. That confirmed "ROUNDED impacts
performance". I hadn't tested ROUNDED versus "your own routine" until the test I posted
this week, which does confirm the advice. 

I select tests based on scepticism, but post results no matter WHICH way they go.
```

###### ↳ ↳ ↳ Re: Rounding timings

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-09-21T22:47:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190440026.011733.271640@y42g2000hsy.googlegroups.com>`
- **In-Reply-To:** `<tr99f3d1m4ttoaqh1465coso39i2uprjl0@4ax.com>`
- **References:** `<b4e6f3p01lij7o99aq1fsr0kgg07s88qgt@4ax.com> <DWHIi.503953$Bo7.404419@fe07.news.easynews.com> <j3p8f3d4g88pdf4ld48bhuc722bbkd2es3@4ax.com> <W0%Ii.519352$Bo7.310763@fe07.news.easynews.com> <tr99f3d1m4ttoaqh1465coso39i2uprjl0@4ax.com>`

```
On Sep 22, 5:36 pm, Robert <n...@e.mail> wrote:
> On Sat, 22 Sep 2007 02:23:51 GMT, "William M. Klein" <wmkl...@nospam.netcom.com> wrote:
>
…[36 more quoted lines elided]…
> I select tests based on scepticism, but post results no matter WHICH way they go.

Maybe, but the claims you made for 'busted' were failures on your part
to actually find a test that showed the proposition.  In fact I can't
think of _one_ item where your 'busted' claim stands up.

You claimed "they were wasting our time" when actually it was _you_
that was wasting everyone's time.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
