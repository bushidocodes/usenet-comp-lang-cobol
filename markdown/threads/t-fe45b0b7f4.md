[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How is unit testing performed at your location?

_7 messages · 5 participants · 2008-10_

---

### How is unit testing performed at your location?

- **From:** "Methods & Tools" <editor@methodsandtools.com>
- **Date:** 2008-10-09T08:29:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a68e19b9-cd5b-4acc-ac57-d85a85ddc62b@l42g2000hsc.googlegroups.com>`

```
Methods & Toosl is currently conducting a one-question poll to know
how is unit testing performed at your location? Go to
http://www.methodsandtools.com/dynpoll/vote.php to participate and to
see intermediate results.
```

#### ↳ Re: How is unit testing performed at your location?

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-10-10T11:03:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1OWdnYSsf45O4XLVnZ2dnUVZ_ovinZ2d@earthlink.com>`
- **References:** `<a68e19b9-cd5b-4acc-ac57-d85a85ddc62b@l42g2000hsc.googlegroups.com>`

```
Methods & Tools wrote:
> Methods & Toosl is currently conducting a one-question poll to know
> how is unit testing performed at your location? Go to
> http://www.methodsandtools.com/dynpoll/vote.php to participate and to
> see intermediate results.

First is the "Smoke Test."
    Turn it on. Does smoke pour out?
Second is the "Shame Test."
   Does the component immediately die of shame.

If the component passes these tests, ship it and book the revenue.
```

##### ↳ ↳ Re: How is unit testing performed at your location?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-10-11T11:23:50+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6la2voFbf7ncU1@mid.individual.net>`
- **References:** `<a68e19b9-cd5b-4acc-ac57-d85a85ddc62b@l42g2000hsc.googlegroups.com> <1OWdnYSsf45O4XLVnZ2dnUVZ_ovinZ2d@earthlink.com>`

```


"HeyBub" <heybub@NOSPAMgmail.com> wrote in message 
news:1OWdnYSsf45O4XLVnZ2dnUVZ_ovinZ2d@earthlink.com...
> Methods & Tools wrote:
>> Methods & Toosl is currently conducting a one-question poll to know
…[10 more quoted lines elided]…
>

I like that approach... must try it. :-)

Pete.
```

#### ↳ Re: How is unit testing performed at your location?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-10-11T11:22:58+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6la2u5Fbho2gU1@mid.individual.net>`
- **References:** `<a68e19b9-cd5b-4acc-ac57-d85a85ddc62b@l42g2000hsc.googlegroups.com>`

```


"Methods & Tools" <editor@methodsandtools.com> wrote in message 
news:a68e19b9-cd5b-4acc-ac57-d85a85ddc62b@l42g2000hsc.googlegroups.com...
> Methods & Toosl is currently conducting a one-question poll to know
> how is unit testing performed at your location? Go to
> http://www.methodsandtools.com/dynpoll/vote.php to participate and to
> see intermediate results.

Testing? Seems to ring a bell...

I think that's when you try to fix programs before they go live.

Doesn't matter how many bugs you fix the users will simply find more, so why 
bother?

Write it, run it, put it in production.

Testing is a waste of time... (besides, it's boring...)

Pete.
```

#### ↳ Re: How is unit testing performed at your location?

- **From:** Robert <no@e.mail>
- **Date:** 2008-10-10T20:16:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fquve4p1gdvjnoks494d4cumkdsbal3cq4@4ax.com>`
- **References:** `<a68e19b9-cd5b-4acc-ac57-d85a85ddc62b@l42g2000hsc.googlegroups.com>`

```
On Thu, 9 Oct 2008 08:29:43 -0700 (PDT), "Methods & Tools" <editor@methodsandtools.com>
wrote:

>Methods & Toosl is currently conducting a one-question poll to know
>how is unit testing performed at your location? Go to
>http://www.methodsandtools.com/dynpoll/vote.php to participate and to
>see intermediate results.

The major US telephone company just rolled out a new methodology called Unified Process.
It has templates for most everything except, can you believe, it doesn't have one for Unit
Testing. It has Integration, System and Regression testing, but no Unit. Why do you
suppose they omitted Unit? Answer: they don't trust programmers to test their own code.
```

##### ↳ ↳ Re: How is unit testing performed at your location?

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-10-14T08:08:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cr99f4l650r4jkeftfvcvk4f7m95pj8q1b@4ax.com>`
- **References:** `<a68e19b9-cd5b-4acc-ac57-d85a85ddc62b@l42g2000hsc.googlegroups.com> <fquve4p1gdvjnoks494d4cumkdsbal3cq4@4ax.com>`

```
On Fri, 10 Oct 2008 20:16:25 -0500, Robert <no@e.mail> wrote:

>The major US telephone company just rolled out a new methodology called Unified Process.
>It has templates for most everything except, can you believe, it doesn't have one for Unit
>Testing. It has Integration, System and Regression testing, but no Unit. Why do you
>suppose they omitted Unit? Answer: they don't trust programmers to test their own code.

I don't know what "Unified Process" entails.   But I do wonder if it's
possible to have a template that covers all unit testing adequately. 
Maybe they do trust programmers to do better unit testing than
trusting a template methodology to be complete.
```

###### ↳ ↳ ↳ Re: How is unit testing performed at your location?

- **From:** Robert <no@e.mail>
- **Date:** 2008-10-14T12:30:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<thl9f41fue1qnm93shtceqfdmue9sba3jc@4ax.com>`
- **References:** `<a68e19b9-cd5b-4acc-ac57-d85a85ddc62b@l42g2000hsc.googlegroups.com> <fquve4p1gdvjnoks494d4cumkdsbal3cq4@4ax.com> <cr99f4l650r4jkeftfvcvk4f7m95pj8q1b@4ax.com>`

```
On Tue, 14 Oct 2008 08:08:04 -0600, Howard Brazee <howard@brazee.net> wrote:

>On Fri, 10 Oct 2008 20:16:25 -0500, Robert <no@e.mail> wrote:
>
…[3 more quoted lines elided]…
>>suppose they omitted Unit? Answer: they don't trust programmers to test their own code.

The FORMAT of a Unit Test document is similar to Integration and System Test: test cases,
expected and actual results. The difference in which planning document it links back to. A
Unit Test follows the Detailed Design; Integration is linked to high level design; System
is linked to Business Requirments.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
