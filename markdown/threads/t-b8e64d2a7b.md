[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL "non-myth" confirmed - Index and subscripts (MF on Windows)

_8 messages · 4 participants · 2007-09_

---

### Re: COBOL "non-myth" confirmed - Index and subscripts (MF on Windows)

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-09-21T14:23:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g0a8f35vgdji41nvg4v5eu1mghln10e9q6@4ax.com>`
- **References:** `<igvme3had674qhm1imohgi0f7u9oah543h@4ax.com> <pabte318v4n344saoq74ifeh7u3t1f8v9n@4ax.com> <13eu3serlerr449@corp.supernews.com> <8sn0f35tq2j9hsrp75rulk5hsfksakvr8m@4ax.com> <1190233728.916560.306340@k35g2000prh.googlegroups.com> <bhm3f3lhlko53ia8rbjg536gjqc95s344e@4ax.com> <NvidnVqkrOLOZ2_bnZ2dnUVZ_oOnnZ2d@comcast.com> <i656f31589490irb94ts6fc1mcl9ubdi8c@4ax.com> <YaidncS6RurpsG7bnZ2dnUVZ_j6dnZ2d@comcast.com> <5li2ppF8fhaiU1@mid.individual.net>`

```
On Sat, 22 Sep 2007 02:29:21 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I remember coding COBOL before there was a PICTURE clause (It was the COBOL 
>59 compiler). We used SIZE, CLASS, and USAGE to achieve the same result. I 
>also remember being able to write OTHERWISE in an IF statement... happy 
>days...:-)

I used to use OTHERWISE, but my first compiler had the brand new
PICTURE feature.   I don't know of another optional feature that took
over as rapidly as that one.
```

#### ↳ Re: COBOL "non-myth" confirmed - Index and subscripts (MF on Windows)

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-09-21T17:38:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46F4018F.6F0F.0085.0@efirstbank.com>`
- **References:** `<igvme3had674qhm1imohgi0f7u9oah543h@4ax.com> <pabte318v4n344saoq74ifeh7u3t1f8v9n@4ax.com> <13eu3serlerr449@corp.supernews.com> <8sn0f35tq2j9hsrp75rulk5hsfksakvr8m@4ax.com> <1190233728.916560.306340@k35g2000prh.googlegroups.com> <bhm3f3lhlko53ia8rbjg536gjqc95s344e@4ax.com> <NvidnVqkrOLOZ2_bnZ2dnUVZ_oOnnZ2d@comcast.com> <i656f31589490irb94ts6fc1mcl9ubdi8c@4ax.com> <YaidncS6RurpsG7bnZ2dnUVZ_j6dnZ2d@comcast.com> <5li2ppF8fhaiU1@mid.individual.net> <g0a8f35vgdji41nvg4v5eu1mghln10e9q6@4ax.com>`

```
>>> On 9/21/2007 at 2:23 PM, in message
<g0a8f35vgdji41nvg4v5eu1mghln10e9q6@4ax.com>, Howard
Brazee<howard@brazee.net> wrote:
> On Sat, 22 Sep 2007 02:29:21 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[10 more quoted lines elided]…
> over as rapidly as that one.

PICTURE has its usefulness, but even having never worked with it's
predecessors, I don't understand why it seemed to have caused the
obsolescence of it's alternatives (SIZE and CLASS, I guess).  PICTURE is
useful for DISPLAY items.  I dare say that it's not so useful for
COMPUTATIONAL items.  Specifically when interacting with other languages.  I
guess that's why we now have POINTER, BINARY-CHAR, BINARY-SHORT, BINARY-LONG
and the like (no PICTURE allowed!!)...

I guess PICTURE S9(4) COMP does make it easier to know the maximum possible
value of the field.  But it also limits its usefulness.  Not worth it, in my
opinion.

Frank
```

##### ↳ ↳ Re: COBOL "non-myth" confirmed - Index and subscripts (MF onWindows)

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-22T11:56:59+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5lj42cF8f4hiU1@mid.individual.net>`
- **References:** `<igvme3had674qhm1imohgi0f7u9oah543h@4ax.com> <pabte318v4n344saoq74ifeh7u3t1f8v9n@4ax.com> <13eu3serlerr449@corp.supernews.com> <8sn0f35tq2j9hsrp75rulk5hsfksakvr8m@4ax.com> <1190233728.916560.306340@k35g2000prh.googlegroups.com> <bhm3f3lhlko53ia8rbjg536gjqc95s344e@4ax.com> <NvidnVqkrOLOZ2_bnZ2dnUVZ_oOnnZ2d@comcast.com> <i656f31589490irb94ts6fc1mcl9ubdi8c@4ax.com> <YaidncS6RurpsG7bnZ2dnUVZ_j6dnZ2d@comcast.com> <5li2ppF8fhaiU1@mid.individual.net> <g0a8f35vgdji41nvg4v5eu1mghln10e9q6@4ax.com> <46F4018F.6F0F.0085.0@efirstbank.com>`

```


"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
news:46F4018F.6F0F.0085.0@efirstbank.com...
>>>> On 9/21/2007 at 2:23 PM, in message
> <g0a8f35vgdji41nvg4v5eu1mghln10e9q6@4ax.com>, Howard
…[17 more quoted lines elided]…
> obsolescence of it's alternatives (SIZE and CLASS, I guess).

Frank, can you confirm that you can see my post, one above the post from 
Howard you are referring to, and noted in the headers to this post?

I've had trouble in the past with posts not being relayed to North America.

I mention this because I stated specifcally, "SIZE, CLASS, and USAGE"

Cheers,
Pete.
```

###### ↳ ↳ ↳ Re: COBOL "non-myth" confirmed - Index and subscripts (MF onWindows)

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-09-21T18:52:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46F412F5.6F0F.0085.0@efirstbank.com>`
- **References:** `<igvme3had674qhm1imohgi0f7u9oah543h@4ax.com> <pabte318v4n344saoq74ifeh7u3t1f8v9n@4ax.com> <13eu3serlerr449@corp.supernews.com> <8sn0f35tq2j9hsrp75rulk5hsfksakvr8m@4ax.com> <1190233728.916560.306340@k35g2000prh.googlegroups.com> <bhm3f3lhlko53ia8rbjg536gjqc95s344e@4ax.com> <NvidnVqkrOLOZ2_bnZ2dnUVZ_oOnnZ2d@comcast.com> <i656f31589490irb94ts6fc1mcl9ubdi8c@4ax.com> <YaidncS6RurpsG7bnZ2dnUVZ_j6dnZ2d@comcast.com> <5li2ppF8fhaiU1@mid.individual.net> <g0a8f35vgdji41nvg4v5eu1mghln10e9q6@4ax.com> <46F4018F.6F0F.0085.0@efirstbank.com> <5lj42cF8f4hiU1@mid.individual.net>`

```
>>> On 9/21/2007 at 5:56 PM, in message
<5lj42cF8f4hiU1@mid.individual.net>,
Pete Dashwood<dashwood@removethis.enternet.co.nz> wrote:

> 
> "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
…[9 more quoted lines elided]…
>>>>59 compiler). We used SIZE, CLASS, and USAGE to achieve the same
result.
>>> I
>>>>also remember being able to write OTHERWISE in an IF statement... happy
…[17 more quoted lines elided]…
> I mention this because I stated specifcally, "SIZE, CLASS, and USAGE"

Umm, yes I believe I saw all of them.  Certainly I saw your reference to
"SIZE, CLASS, and USAGE" in as much as they are also present in the body of
this post.  I'm not sure what I stated that would make you think I did not
see them.

I was simply wondering why PICTURE became the standard while SIZE and CLASS
seemed to have disappeared from the language altogether.

Frank
```

###### ↳ ↳ ↳ Re: COBOL "non-myth" confirmed - Index and subscripts (MFonWindows)

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-22T23:31:37+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5lkcorF8kqk3U1@mid.individual.net>`
- **References:** `<igvme3had674qhm1imohgi0f7u9oah543h@4ax.com> <pabte318v4n344saoq74ifeh7u3t1f8v9n@4ax.com> <13eu3serlerr449@corp.supernews.com> <8sn0f35tq2j9hsrp75rulk5hsfksakvr8m@4ax.com> <1190233728.916560.306340@k35g2000prh.googlegroups.com> <bhm3f3lhlko53ia8rbjg536gjqc95s344e@4ax.com> <NvidnVqkrOLOZ2_bnZ2dnUVZ_oOnnZ2d@comcast.com> <i656f31589490irb94ts6fc1mcl9ubdi8c@4ax.com> <YaidncS6RurpsG7bnZ2dnUVZ_j6dnZ2d@comcast.com> <5li2ppF8fhaiU1@mid.individual.net> <g0a8f35vgdji41nvg4v5eu1mghln10e9q6@4ax.com> <46F4018F.6F0F.0085.0@efirstbank.com> <5lj42cF8f4hiU1@mid.individual.net> <46F412F5.6F0F.0085.0@efirstbank.com>`

```


"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
news:46F412F5.6F0F.0085.0@efirstbank.com...
>>>> On 9/21/2007 at 5:56 PM, in message
> <5lj42cF8f4hiU1@mid.individual.net>,
…[39 more quoted lines elided]…
> this post.

That's because I quoted it :-)

  I'm not sure what I stated that would make you think I did not
> see them.
(It was the fact that USAGE wasn't included, and the "I guess" which 
indicated uncertainty.)

Thanks for the confirmation. As I mentioned, I've had problems in the past 
with relaying to North America; it's quite spooky... people in Europe can 
see the post and respond to it, I can see the post, but people in the USA 
and Canada couldn't. Anyway, that wasn't the problem on this occasion.
>
> I was simply wondering why PICTURE became the standard while SIZE and 
> CLASS
> seemed to have disappeared from the language altogether.

I believe they were dropped when PICTURE enjoyed the phenomenal success it 
did.

Pete.
```

###### ↳ ↳ ↳ Re: COBOL "non-myth" confirmed - Index and subscripts (MF onWindows)

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-21T19:15:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190427303.965310.119380@50g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<5lj42cF8f4hiU1@mid.individual.net>`
- **References:** `<igvme3had674qhm1imohgi0f7u9oah543h@4ax.com> <46F4018F.6F0F.0085.0@efirstbank.com> <5lj42cF8f4hiU1@mid.individual.net>`

```
On 22 Sep, 00:56, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Frank Swarbrick" <Frank.Swarbr...@efirstbank.com> wrote in message
>
…[31 more quoted lines elided]…
>

Are you posting via Google? I only ask because I have posted and
nothing has turned up on more than one occasion because Google counts
the posts and only allows so many per (arbitrary) unit of time and
when my ire is raised I feel the need to respond  -  witness
Evolution.
```

###### ↳ ↳ ↳ Re: COBOL "non-myth" confirmed - Index and subscripts (MF onWindows)

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-22T23:32:46+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5lkcr0F8n9c5U1@mid.individual.net>`
- **References:** `<igvme3had674qhm1imohgi0f7u9oah543h@4ax.com> <46F4018F.6F0F.0085.0@efirstbank.com> <5lj42cF8f4hiU1@mid.individual.net> <1190427303.965310.119380@50g2000hsm.googlegroups.com>`

```


"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1190427303.965310.119380@50g2000hsm.googlegroups.com...
> On 22 Sep, 00:56, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[42 more quoted lines elided]…
> Evolution.

No, I'm posting via server in Germany.

Pete.
```

##### ↳ ↳ Re: COBOL "non-myth" confirmed - Index and subscripts (MF on Windows)

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-09-24T10:22:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lsoff3l31id5703mrkqmmvnhabc44v0rk1@4ax.com>`
- **References:** `<13eu3serlerr449@corp.supernews.com> <8sn0f35tq2j9hsrp75rulk5hsfksakvr8m@4ax.com> <1190233728.916560.306340@k35g2000prh.googlegroups.com> <bhm3f3lhlko53ia8rbjg536gjqc95s344e@4ax.com> <NvidnVqkrOLOZ2_bnZ2dnUVZ_oOnnZ2d@comcast.com> <i656f31589490irb94ts6fc1mcl9ubdi8c@4ax.com> <YaidncS6RurpsG7bnZ2dnUVZ_j6dnZ2d@comcast.com> <5li2ppF8fhaiU1@mid.individual.net> <g0a8f35vgdji41nvg4v5eu1mghln10e9q6@4ax.com> <46F4018F.6F0F.0085.0@efirstbank.com>`

```
On Fri, 21 Sep 2007 17:38:23 -0600, "Frank Swarbrick"
<Frank.Swarbrick@efirstbank.com> wrote:

>PICTURE has its usefulness, but even having never worked with it's
>predecessors, I don't understand why it seemed to have caused the
…[8 more quoted lines elided]…
>opinion.

I think it makes it easier to remember the decimal nature of CoBOL
numbers.   I expect our overflow rules are less efficient than that of
languages that don't think in decimal - but they are closer to our
business needs.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
