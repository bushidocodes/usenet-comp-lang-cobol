[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Zombie COBOL

_14 messages · 7 participants · 2016-10_

---

### Zombie COBOL

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2016-10-22T20:16:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e72dqkF8p5jU1@mid.individual.net>`

```
About 20 years ago, here in this forum, I predicted that COBOL would be
"dead" by the year 2015.

I have taken a little time from my current very busy (C#... :-)) programming
schedule to check out some of the key indicators that would decide the truth
or falsity of this statement.

My conclusion is that I was not entirely correct in this, but I was not
entirely "wrong" either.

It depends on how you define "dead".

At the time I made the statement, the use of networked computers was
starting to replace the centralized mainframes which had "governed"
commercial computing for decades. There were still many people writing COBOL
who were convinced that they would be "good for life" and there was no need
to expand skill sets because "toy computers"would never replace "real
computers".

We had been in an era where COBOL was the "only game in town" in real terms
for commercial system development so it was hard to imagine anything
replacing it.

A quick search on any of the major job sites revealed thousands of COBOL
jobs. The same searches today reveal a few dozen, so, at least to that
extent, my prediction was true.

Nevertheless, COBOL IS still alive and well on a small (in the scheme of
things) but significant, number of sites.

I could write a great deal about why COBOL refuses to "lie down" but really,
I'm just glad it is still standing, at least in some places.

For the last 10 years I have dedicated my energy to getting legacy COBOL
systems migrated to the new networked model, in a way that doesn't degrade
the network and that provides options for the future. Removing dependency on
indexed files (so the data resource can be shared with software other than
COBOL; opening it up to both legacy and new processes...), generating
separation layers for data manipulation, tapping into facilities not usually
available to COBOL (like LINQ), and, most recently, seeking to provide a
path for people using Fujitsu's PowerCOBOL, to get out from dependency on
it. To automate these processes has been a long hard grind and it has meant
writing generators that generate both COBOL and C#. (PowerCOBOL "sheets"
(GUI windows) get analyzed and converted to Windows Forms which are built
using generated C# for the MS Designer in Visual Studio; the "scrptlets" in
PowerCOBOL which drive these sheets, get transformed into standard OO COBOL
and become "code-behind" components for the new Windows Forms...)). These
tools are dealing with COBOL on a daily basis. If COBOL is "dead" then there
are a lot of zombies walking around... :-)

I have been pretty obsessed by getting this stuff built and tested and a
number of people have been helping by running Proofs of Concept (POCs). We
are now in the home straight for PowerCOBOL and the results are quite
stunning. But there is a still a lot to do (especially with Testing) and we
won't have a commercially releaseable product before December. There is no
point in releasing a new product in the run-up to the holidays, so it will
be announced in January. In the meantime, I will be revising the PRIMA web
site to accommodate the new migration products and I hope to make it an
interesting and comfortable place for COBOL people to go to.

It is interesting to me to see legacy "zombie COBOL"" being reincarnated
into modern COBOL Classes that can lead a full life in the .Net environment.

The emphasis in all our tools is not to force people to replace their COBOL,
but rather to give them options where they CAN replace it (in a phased and
prioritised manner with no risk) or they can continue with COBOL if they
want to.

Pease "keep an eye on us" at http://primacomputing.co.nz

Pete.

"I used to write COBOL...now I can do anything."
```

#### ↳ Re: Zombie COBOL

- **From:** "luuk" <ua-author-557437@usenetarchives.gap>
- **Date:** 2016-10-23T09:11:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac0a83e67c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<e72dqkF8p5jU1@mid.individual.net>`
- **References:** `<e72dqkF8p5jU1@mid.individual.net>`

```
On 23-10-16 02:16, Pete Dashwood wrote:
› Pease "keep an eye on us" at http://primacomputing.co.nz

Piease is written with a 'c' or with an 'l' ....

;)
```

##### ↳ ↳ Re: Zombie COBOL

- **From:** "luuk" <ua-author-557437@usenetarchives.gap>
- **Date:** 2016-10-23T09:13:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac0a83e67c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ac0a83e67c-p2@usenetarchives.gap>`
- **References:** `<e72dqkF8p5jU1@mid.individual.net> <gap-ac0a83e67c-p2@usenetarchives.gap>`

```
On 23-10-16 15:11, Luuk wrote:
› On 23-10-16 02:16, Pete Dashwood wrote:
›› Pease "keep an eye on us" at http://primacomputing.co.nz
…[3 more quoted lines elided]…
› ;)


Ih hate it when i make a type in a message correcting someone else......

;(
```

###### ↳ ↳ ↳ Re: Zombie COBOL

- **From:** "luuk" <ua-author-557437@usenetarchives.gap>
- **Date:** 2016-10-23T09:15:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac0a83e67c-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ac0a83e67c-p3@usenetarchives.gap>`
- **References:** `<e72dqkF8p5jU1@mid.individual.net> <gap-ac0a83e67c-p2@usenetarchives.gap> <gap-ac0a83e67c-p3@usenetarchives.gap>`

```
On 23-10-16 15:13, Luuk wrote:
› On 23-10-16 15:11, Luuk wrote:
›› On 23-10-16 02:16, Pete Dashwood wrote:
…[9 more quoted lines elided]…
› ;(

time for new battery's in my keyboard.... ;)
```

##### ↳ ↳ Re: Zombie COBOL

- **From:** "dashwood" <ua-author-14256666@usenetarchives.gap>
- **Date:** 2016-10-23T19:31:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac0a83e67c-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ac0a83e67c-p2@usenetarchives.gap>`
- **References:** `<e72dqkF8p5jU1@mid.individual.net> <gap-ac0a83e67c-p2@usenetarchives.gap>`

```
On Sun, 23 Oct 2016 15:11:12 +0200, Luuk wrote:

› On 23-10-16 02:16, Pete Dashwood wrote:
›› Pease "keep an eye on us" at http://primacomputing.co.nz
…[3 more quoted lines elided]…
› ;)

I was using a remote keyboard and missed a key.

How would you write "Please" with a "c"?

Maybe I was subconsciously thinking of black-eyed peas; pease keeping
an eye on things... :-)

Pete.
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Zombie COBOL

- **From:** "luuk" <ua-author-557437@usenetarchives.gap>
- **Date:** 2016-10-24T13:13:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac0a83e67c-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ac0a83e67c-p5@usenetarchives.gap>`
- **References:** `<e72dqkF8p5jU1@mid.individual.net> <gap-ac0a83e67c-p2@usenetarchives.gap> <gap-ac0a83e67c-p5@usenetarchives.gap>`

```
On 24-10-16 01:31, Pete Dashwood wrote:
››› Pease "keep an eye on us" at http://primacomputing.co.nz
››› 
…[5 more quoted lines elided]…
› How would you write "Please" with a "c"?

Peace
```

###### ↳ ↳ ↳ Re: Zombie COBOL

_(reply depth: 4)_

- **From:** "bill.woodger" <ua-author-14501802@usenetarchives.gap>
- **Date:** 2016-10-24T14:20:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac0a83e67c-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ac0a83e67c-p6@usenetarchives.gap>`
- **References:** `<e72dqkF8p5jU1@mid.individual.net> <gap-ac0a83e67c-p2@usenetarchives.gap> <gap-ac0a83e67c-p5@usenetarchives.gap> <gap-ac0a83e67c-p6@usenetarchives.gap>`

```
On Monday, October 24, 2016 at 7:13:10 PM UTC+2, Luuk wrote:
› On 24-10-16 01:31, Pete Dashwood wrote:
›››› Pease "keep an eye on us" at http://primacomputing.co.nz
…[8 more quoted lines elided]…
› Peace

Police.

Piece. Pease is of course a word (so no spell-check saviour for the typo). Peas (a more modern word). Pearlies. Probably more typonyms, but I should stop.

Major job sites 20 years ago? You mean the trade press? A "quick rustle through the jobs pages"?

To go from this: "If COBOL is "dead" then there are a lot of zombies walking around... :-)" to "It is interesting to me to see legacy "zombie COBOL"" being reincarnated" within two paragraphs is a nice trick. Now you see 'em, now you don't? Anyway, hasn't a zombie already been reincarnated (although it seems people go for "reanimated" anyway)?

However, for the attempt, if human = COBOL, then zombie (husk of human, reanimated, foul, decaying automaton) = (husk of original COBOL, err... with objects and layers) then the Zombie COBOL is the new stuff, not the old. I'll expect the update to your (now) police-monitored website forthwith :-)

Of course, if you were trying to make some other point by the use of zombie, it was unclear.
```

#### ↳ Re: Zombie COBOL

- **From:** "gregwebace" <ua-author-14501803@usenetarchives.gap>
- **Date:** 2016-10-23T22:08:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac0a83e67c-p8@usenetarchives.gap>`
- **In-Reply-To:** `<e72dqkF8p5jU1@mid.individual.net>`
- **References:** `<e72dqkF8p5jU1@mid.individual.net>`

```
On Sunday, 23 October 2016 10:16:22 UTC+10, Pete Dashwood wrote:
› About 20 years ago, here in this forum, I predicted that COBOL would be 
› "dead" by the year 2015.
…[71 more quoted lines elided]…
› "I used to write COBOL...now I can do anything."

Hi Pete, I am following the threads and appreciate your input. I remain an advocate for COBOL and it is not yet a Zombie language. My action for business change so far is no COBOL change but I continue to follow alternatives. What I am working on currently is improving my website so that it is HTML5, CSS3 and gradually removing tables. The pages will also be compatible and adjust for mobile devices. Behind it is still my COBOL products both on-premise and SaaS for cloud. The initial page is www.aceway.net and the linked pages are still subject to replacement with newer code. You can open this page in a PC browser, squeeze the width or open it on a smartphone to see how it adapts.

Further ideas that go beyond COBOL even tho COBOL is used.

When people choose an APP they are not concerned with the language and methods used. They just want to know about functionality, does it do what I want and is the price acceptable.

I get a bit peeved by COBOL people who want to discuss the use of Compute vs individual Add/Subtract/Multiply/Divide.

Marketing a product is a bigger issue so having clever meta-tags, text, associations with global social pages in Facebook, Linked-In, Twitter, Youtube and more seem to increase Google search criteria to get on the first page of a query.

I am also exploring the use of Explainer Videos on YouTube that cut down the verbosity of text on my web pages.

This is my current challenge.
```

##### ↳ ↳ Re: Zombie COBOL

- **From:** "bill.woodger" <ua-author-14501802@usenetarchives.gap>
- **Date:** 2016-10-24T14:27:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac0a83e67c-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ac0a83e67c-p8@usenetarchives.gap>`
- **References:** `<e72dqkF8p5jU1@mid.individual.net> <gap-ac0a83e67c-p8@usenetarchives.gap>`

```
And your clients may be peeved, if they are coming from, or are in, the Mainframe world.

Does it peeve you that a question is asked, that it is answered, or what? I won't bother with why it peeves. Just askin'.
```

##### ↳ ↳ Re: Zombie COBOL

- **From:** "0robert.jones" <ua-author-14501639@usenetarchives.gap>
- **Date:** 2016-10-25T18:46:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac0a83e67c-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ac0a83e67c-p8@usenetarchives.gap>`
- **References:** `<e72dqkF8p5jU1@mid.individual.net> <gap-ac0a83e67c-p8@usenetarchives.gap>`

```
On Monday, 24 October 2016 03:08:42 UTC+1, Greg Wallace wrote:
› On Sunday, 23 October 2016 10:16:22 UTC+10, Pete Dashwood  wrote:
›› About 20 years ago, here in this forum, I predicted that COBOL would be 
…[86 more quoted lines elided]…
› This is my current challenge.

It used to matter how intermediates were handled in a calculation with respect to available precision and truncations. Though modern compilers are a lot more careful and versatile, there may still be instances where it matters and breaking up a calculation into its components can provide better control.
Robert
```

##### ↳ ↳ Re: Zombie COBOL

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2016-10-27T08:06:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac0a83e67c-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ac0a83e67c-p8@usenetarchives.gap>`
- **References:** `<e72dqkF8p5jU1@mid.individual.net> <gap-ac0a83e67c-p8@usenetarchives.gap>`

```
Greg Wallace wrote:
› On Sunday, 23 October 2016 10:16:22 UTC+10, Pete Dashwood  wrote:
›› About 20 years ago, here in this forum, I predicted that COBOL would
…[79 more quoted lines elided]…
› remain an advocate for COBOL and it is not yet a Zombie language.

Hi Greg

The "zombie" tag was a joke against myself because I said it would be dead
but (at least in some places) it is still walking around...

I do see legacy COBOL as kind of dead (modern OO COBOL is supplanting it on
networked COBOL systems) but there is still a place for even "old" COBOL in
batch processing (for which it has always been ideally suited).

>
› I get a bit peeved by COBOL people who want to discuss the use of
› Compute vs individual Add/Subtract/Multiply/Divide.
›

Why?

We've had far worse discussions than that here over the years...

› Marketing a product is a bigger issue so having clever meta-tags,
› text, associations with global social pages in Facebook, Linked-In,
› Twitter, Youtube and more seem to increase Google search criteria to
› get on the first page of a query.

Maybe. I don't link to social media but I do use meta tags. I'm happy with
the PRIMA rankings...
›
› I am also exploring the use of Explainer Videos on YouTube that cut
› down the verbosity of text on my web pages.

Yes, I like the use of videos but it has to be managed very carefully. They
take a lot of work (read "time" which = money, to produce and, until
everybody has Broadband and decent streaming bandwidth, you can't guarantee
everyone will see what you'd like them to.)

Nevertheless, it is certainly true that a picture can be worth 1000 words,
and a moving picture can be even more valuable.

The main problem with the current PRIMA videos is that they are too long;
I'll be producing a whole new set for the new product.
› This is my current challenge.

Good luck with it!

Pete.

"I used to write COBOL...now I can do anything."
```

#### ↳ Re: Zombie COBOL

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2016-10-24T08:08:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac0a83e67c-p12@usenetarchives.gap>`
- **In-Reply-To:** `<e72dqkF8p5jU1@mid.individual.net>`
- **References:** `<e72dqkF8p5jU1@mid.individual.net>`

```
In article ,
Pete Dashwood wrote:
› About 20 years ago, here in this forum, I predicted that COBOL would be 
› "dead" by the year 2015.
…[8 more quoted lines elided]…
› It depends on how you define "dead".

THis seems to be a very good time to discover Author's Intent. If whoever
posted 'COBOL will be dead by 2015' is reading would you be so kind as to
state the definition of 'dead' you were using?

Thanks!

DD
```

##### ↳ ↳ Re: Zombie COBOL

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2016-10-27T08:31:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac0a83e67c-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ac0a83e67c-p12@usenetarchives.gap>`
- **References:** `<e72dqkF8p5jU1@mid.individual.net> <gap-ac0a83e67c-p12@usenetarchives.gap>`

```
doc··f@pa··x.com wrote:
› In article ,
› Pete Dashwood  wrote:
…[16 more quoted lines elided]…
› Thanks!

I was going to respond to this at length and justify my statement, but I
realized it would not be fair because I could use a definition that would
support my own case, and it doesn't really matter in the scheme of
things...IT today is what it is and a career in COBOL (alone) is no longer
viable, as it once was. To that extent, COBOL is "dead" as a career choice.

The real truth is that I didn't think about exactly what I meant (at the
time I made the statement); it was more of a "feeling" and along the lines
that COBOL would no longer be the primary commercial programming language it
had been from the 1960s through to the 1990s, and that the change would be
so drastic that people would lose their jobs, organizations would replace
COBOL and centralized mainframes with distributed systems on networks, using
objects, so that, from a COBOL perspective the landscape would shrink to the
point where COBOL would be confined to the Fortresses where change was
resisted at all costs, and even these Fortresses would decline in number.

Like I said, I wasn't entirely right, but I wasn't entirely wrong either.

There were many factors that led to the decline of COBOL and some of them
actually had nothing to do with the language.

Pete
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Zombie COBOL

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2016-10-27T10:13:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac0a83e67c-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ac0a83e67c-p13@usenetarchives.gap>`
- **References:** `<e72dqkF8p5jU1@mid.individual.net> <gap-ac0a83e67c-p12@usenetarchives.gap> <gap-ac0a83e67c-p13@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:
› doc··f@pa··x.com wrote:
›› In article ,
…[22 more quoted lines elided]…
› things...

With a small smile... this might read, to an uncharitable eye, as 'Given
an opportunity to stack the deck Mr Dashwood studiously endeavours to deal
himself a losing hand.'

[snip]

› Like I said, I wasn't entirely right, but I wasn't entirely wrong either.

One who is blessed with a porous memory might say 'Oh, did I say that?
Well, now that you mention it maybe I did, maybe I was thinking...
something... or maybe something else... have you noticed how young women
nowadays aren't afraid to show a finely-tuned ankle? By the stars, it is
a glorious time to be alive... zzZZZzzzz....'

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
