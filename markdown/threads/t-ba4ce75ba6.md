[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Top 10 Language Constructs (Cobol)

_24 messages · 16 participants · 2000-07_

---

### Top 10 Language Constructs (Cobol)

- **From:** "Bruno Gustavs" <GustavsB@ch.sibt.com>
- **Date:** 2000-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kmjmf$l7h$1@pollux.ip-plus.net>`

```
What do you think are the top ten language constructs in Cobol?
Please don't answer in terms of concepts, but try to restrict
yourself to those statements you really use to cope with your
daily work.

Curious why I'm asking this question? In spite of all requirements
engineering effort we know exactly *how* to solve problems
with computer languages but know fairly, *what* we're doing
during this process.

Regards
Bruno Gustavs
```

#### ↳ Re: Top 10 Language Constructs (Cobol)

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2000-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LUEb5.37273$T%3.358702@typhoon.austin.rr.com>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net>`

```

Bruno Gustavs <GustavsB@ch.sibt.com>

> What do you think are the top ten language constructs in Cobol?
> Please don't answer in terms of concepts, but try to restrict
…[6 more quoted lines elided]…
> during this process.

MOVE
IF
PERFORM
COMPUTE
CALL

is all I use
```

#### ↳ Re: Top 10 Language Constructs (Cobol)

- **From:** tscoffey@my-deja.com
- **Date:** 2000-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8knhbf$lc3$1@nnrp1.deja.com>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net>`

```
In article <8kmjmf$l7h$1@pollux.ip-plus.net>,
  "Bruno Gustavs" <GustavsB@ch.sibt.com> wrote:
> What do you think are the top ten language constructs in Cobol?
> Please don't answer in terms of concepts, but try to restrict
> yourself to those statements you really use to cope with your
> daily work.
>

I like the ones that don't cause S0C7's, S0C4's, or S0C1's.

The rest I ignore.



Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Top 10 Language Constructs (Cobol)

- **From:** Susan Allen <susan.a.allen@boeing.com>
- **Date:** 2000-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396F8822.B7170BC6@boeing.com>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net>`

```
Bruno Gustavs wrote:
> 
> What do you think are the top ten language constructs in Cobol?
…[3 more quoted lines elided]…
> 
evaluate
perform
if
else
move
compute
when
read
open close
call

	Susan (I probably forgot something I would fail without)
```

#### ↳ Re: Top 10 Language Constructs (Cobol)

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ko6gg$am2$1@news.igs.net>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net>`

```

Bruno Gustavs wrote in message <8kmjmf$l7h$1@pollux.ip-plus.net>...
>What do you think are the top ten language constructs in Cobol?
>Please don't answer in terms of concepts, but try to restrict
…[7 more quoted lines elided]…
>

I must be stupid, but I have no idea whatsoever what that paragraph
means, or is suppose to mean.

In fact, the entire question seems rather silly.  If you want to know the
most common words, then run a few million lines of code through
a counting program.  MOVE will prove to be the most common verb,
but then we have all known that since the 60's.
```

##### ↳ ↳ Re: Top 10 Language Constructs (Cobol)

- **From:** "Bruno Gustavs" <GustavsB@ch.sibt.com>
- **Date:** 2000-07-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kuqfl$ok4$1@pollux.ip-plus.net>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net> <8ko6gg$am2$1@news.igs.net>`

```
"donald tees" <donald@willmack.com> wrote in message
news:8ko6gg$am2$1@news.igs.net...
> I must be stupid, but I have no idea whatsoever what that paragraph
> means, or is suppose to mean.
…[4 more quoted lines elided]…
> but then we have all known that since the 60's.

You are not stupid. It's just my fault, if I can't explain things right!

The aim of this question is just to understand what we are doing
in the software engineering process. Asking you what language constructs
your working with makes it possible to deduce what your are doing.
If I asked for concepts, you probably answered with some generic stuff,
which would reflect the discussions in the journals.

To be more concrete, let's assume you're going to design Cobol2.
What would this language contain? What should Cobol2 support?
What would you like to solve with Cobol2?
```

###### ↳ ↳ ↳ Re: Top 10 Language Constructs (Cobol)

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-07-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kuuba$ckh$1@news.igs.net>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net> <8ko6gg$am2$1@news.igs.net> <8kuqfl$ok4$1@pollux.ip-plus.net>`

```

Bruno Gustavs wrote in message <8kuqfl$ok4$1@pollux.ip-plus.net>...
>"donald tees" <donald@willmack.com> wrote in message
>news:8ko6gg$am2$1@news.igs.net...
…[20 more quoted lines elided]…
>
I don't think it works that way.  A language evolves/is invented as
a set ... there is a minimum set that allows you to start and go. If the
language is rich enough, then construct frequency is a stylistic phenomena
rather than a necessity.

The key to language is simple agreement ... we both agree that "X" will
mean the same thing and then start communicating in X's.    What
those X's mean is irrelevant, as long as I understand them
the way you meant them, then we can communicate.
```

###### ↳ ↳ ↳ Re: Top 10 Language Constructs (Cobol)

- **From:** "Warren Simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2000-07-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2zQc5.3839$o71.227118@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net> <8ko6gg$am2$1@news.igs.net> <8kuqfl$ok4$1@pollux.ip-plus.net>`

```
This was an interesting exchange but got off topic fast.  I liked one
answer. Who cares? It was Bruno's defense of his question.

Warren Simmons
"Bruno Gustavs" <GustavsB@ch.sibt.com> wrote in message
news:8kuqfl$ok4$1@pollux.ip-plus.net...
> "donald tees" <donald@willmack.com> wrote in message
> news:8ko6gg$am2$1@news.igs.net...
…[3 more quoted lines elided]…
> > In fact, the entire question seems rather silly.  If you want to know
the
> > most common words, then run a few million lines of code through
> > a counting program.  MOVE will prove to be the most common verb,
…[16 more quoted lines elided]…
>
```

#### ↳ Re: Top 10 Language Constructs (Cobol)

- **From:** theodp@aol.com (Theo DP)
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000714220920.16958.00000671@ng-cu1.aol.com>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net>`

```
>Subject: Top 10 Language Constructs (Cobol)
>From: "Bruno Gustavs" GustavsB@ch.sibt.com 
…[15 more quoted lines elided]…
>

I actually much prefer some other languages, most notably SAS (PC, UNIX, MF)
and PL/I (MF), but I have to admit that I miss some useful COBOL language
constructs that are typically absent from or clunkier in other major PC and
mainframe languages.

In no particular order of importance, here are ten of them:

1. Complex record structures with nested occurs.
2. A real SORT verb.
3. Real SEARCH verbs (linear and binary).
4. Built-in support for keyed files.
5. Unparalleled compiler optimization and corresponding execution -->SPEED!
6. Recent substring notation enhancements - FIELD-NAME (start:length)
7. Packed decimal precision.
8. (Easy) dynamic subroutines and parameter linkage.
9. MOVE/ADD CORRESPONDING VERBS (Sorry, I but DO like these!)
10. Group level MOVEs and compares.

And a few bonuses to bring it to a baker's dozen:

11. Flexible redefines.
12. Variable length record support.
13. Report writer (RIP).
```

##### ↳ ↳ Re: Top 10 Language Constructs (Cobol)

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8koifk$sf2$1@nntp9.atl.mindspring.net>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net> <20000714220920.16958.00000671@ng-cu1.aol.com>`

```
"Theo DP" <theodp@aol.com> wrote in message
news:20000714220920.16958.00000671@ng-cu1.aol.com...
  <snippage>
> 13. Report writer (RIP).

Just in case you have missed it:

A) Report Writer is still available on IBM mainframes (and PCs) via an add-on
product

B) Report Writer is being enhanced in the draft of the next COBOL Standard

C) Report Writer will move from "optional" to "required" in the next COBOL
Standard.
```

###### ↳ ↳ ↳ Re: Top 10 Language Constructs (Cobol)

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396FE634.1034D8B4@home.com>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net> <20000714220920.16958.00000671@ng-cu1.aol.com> <8koifk$sf2$1@nntp9.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> "Theo DP" <theodp@aol.com> wrote in message
…[13 more quoted lines elided]…
> 
Oooooh ! You do love your R/W don't you. Back in ye olden-dayse when you
had a fixed print barrel - great. OK so you can write a program to
include a particular printer's control characters - but what a pain.
I only use one printer, but what about the guys with two or more
different printers in a network. Sorry, it just doesn't cut it in
PC-land. 

And besides, most bills I get (utilities, retail, plastic money etc.)
have a proliferation of fonts, styles etc. I have a suspicion that if
they are using COBOL the majority aren't using R/W.

"Klein style" - Having said that, I DO AGREE R/W is a great module.

Still WMK - keep plugging away <G>

Jimmy
```

###### ↳ ↳ ↳ Re: Top 10 Language Constructs (Cobol)

_(reply depth: 4)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t9svmsk3e8lo4vnpc3i5bt2bv6buoio7k1@4ax.com>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net> <20000714220920.16958.00000671@ng-cu1.aol.com> <8koifk$sf2$1@nntp9.atl.mindspring.net> <396FE634.1034D8B4@home.com>`

```
On Sat, 15 Jul 2000 04:19:53 GMT, "James J. Gavan" <jjgavan@home.com> wrote:


>Oooooh ! You do love your R/W don't you. Back in ye olden-dayse when you
>had a fixed print barrel - great. OK so you can write a program to
…[3 more quoted lines elided]…
>PC-land. 
Jimmy,

not quite true.  I have report writer for the PC (an add on for Visual  Age Cobol 2.2,
included in Visual Age COBOL 3.0), and it does support
	different printer (even LASER type <g>)
	different fonts at different places
	etc etc



     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)



      Bolub's Fourth Law of Computerdom: Project teams detest weekly progress reporting because it so vividly manifests their lack of progress.
```

###### ↳ ↳ ↳ Re: Top 10 Language Constructs (Cobol)

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kpsuo$qdu$1@nntp9.atl.mindspring.net>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net> <20000714220920.16958.00000671@ng-cu1.aol.com> <8koifk$sf2$1@nntp9.atl.mindspring.net> <396FE634.1034D8B4@home.com> <t9svmsk3e8lo4vnpc3i5bt2bv6buoio7k1@4ax.com>`

```
Just to "clarify" - the required/enhanced Report Writer in the draft Standard
does *not* (easily) handle proportional/mixed fonts.

The SPC product (available on the PC for a VARIETY of compilers and on
various other IBM platforms) *does* already support these (and I assume will
continue to - after/when/if the new Standard is approved).
```

###### ↳ ↳ ↳ Re: Top 10 Language Constructs (Cobol)

_(reply depth: 5)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kq3ha$6uj$1@news.cerf.net>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net> <20000714220920.16958.00000671@ng-cu1.aol.com> <8koifk$sf2$1@nntp9.atl.mindspring.net> <396FE634.1034D8B4@home.com> <t9svmsk3e8lo4vnpc3i5bt2bv6buoio7k1@4ax.com>`

```
"Volker Bandke" <vbandke@bsp-gmbh.com> wrote in message
news:t9svmsk3e8lo4vnpc3i5bt2bv6buoio7k1@4ax.com...
> not quite true.  I have report writer for the PC (an add on for Visual
Age Cobol 2.2,
> included in Visual Age COBOL 3.0), and it does support
> different printer (even LASER type <g>)
> different fonts at different places

May I ask for a code example showing how they have accomplished this?

Cheesle
```

###### ↳ ↳ ↳ Re: Top 10 Language Constructs (Cobol)

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39705cd3.119185477@207.126.101.100>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net> <20000714220920.16958.00000671@ng-cu1.aol.com> <8koifk$sf2$1@nntp9.atl.mindspring.net> <396FE634.1034D8B4@home.com>`

```
On Sat, 15 Jul 2000 04:19:53 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>Oooooh ! You do love your R/W don't you. Back in ye olden-dayse when you
>had a fixed print barrel - great. OK so you can write a program to
…[4 more quoted lines elided]…
>

I've been studying it a bit off and on, because frankly I never have
had a chance to make real use of it.  HOWEVER, I think that if I can
redirect it's output to a file and put "control" footers and such on
the report I could make it work for a graphical print style.  There
would be a post process after report creation, but it could be
standardized.
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Top 10 OT

_(reply depth: 5)_

- **From:** Dwight Scott Miller <Merlin43PhD@netscape.net>
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3970AA8C.D66751FD@netscape.net>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net> <20000714220920.16958.00000671@ng-cu1.aol.com> <8koifk$sf2$1@nntp9.atl.mindspring.net> <396FE634.1034D8B4@home.com> <39705cd3.119185477@207.126.101.100>`

```


Thane Hubbell wrote:
> 
> I've been studying a bit off and on,
Greetings, Guru, pls pardon OT - just letting you know that I can, once
again, contact my news server in Deutschland.

I guess I have to find something to call you besides "slave" now, huh?
Best of fortune to you - - -  and dinner is still on, whatever day we
pick.
```

###### ↳ ↳ ↳ Re: Top 10 OT

_(reply depth: 6)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3970d18f.24175570@207.126.101.100>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net> <20000714220920.16958.00000671@ng-cu1.aol.com> <8koifk$sf2$1@nntp9.atl.mindspring.net> <396FE634.1034D8B4@home.com> <39705cd3.119185477@207.126.101.100> <3970AA8C.D66751FD@netscape.net>`

```
On Sat, 15 Jul 2000 13:16:44 -0500, Dwight Scott Miller
<Merlin43PhD@netscape.net> wrote:

>
>
…[8 more quoted lines elided]…
>pick.

I've put out some feelers for you.  I'll let you know what comes of it
if anything.  I'm not at all sure, even though assurances have been
given, that I am long for the world there either....  Pressure is on
to move anything and everything off the MF and they already tossed the
manuals except for what I screamed and hollered needed to be saved to
support the box at present.  I've a feeling that once that job is done
and all is on VMS (where I was told to port everything) my time will
be through.  I'm not the least bit concerned, however.... It's just
sad sad sad......  We plan to stay in the area, we like it a lot.
I'll just be working for a harder boss after they lay me off too...
ME.
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Top 10 OT

_(reply depth: 7)_

- **From:** Dwight Scott Miller <Merlin43PhD@netscape.net>
- **Date:** 2000-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39726D1E.1376D898@netscape.net>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net> <20000714220920.16958.00000671@ng-cu1.aol.com> <8koifk$sf2$1@nntp9.atl.mindspring.net> <396FE634.1034D8B4@home.com> <39705cd3.119185477@207.126.101.100> <3970AA8C.D66751FD@netscape.net> <3970d18f.24175570@207.126.101.100>`

```


Thane Hubbell wrote:
> I'll just be working for a harder boss 
Speaking thereof, where did you wind up?  (or should we take this to
email?)
```

###### ↳ ↳ ↳ Re: Top 10 Language Constructs (Cobol)

- **From:** Ron <NoSoy@swbell.net>
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396FEFD3.D71173FD@swbell.net>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net> <20000714220920.16958.00000671@ng-cu1.aol.com> <8koifk$sf2$1@nntp9.atl.mindspring.net>`

```
>> A) Report Writer is still available on IBM mainframes (and PCs) via 
an add-on product

I always did like Report Writer and will be glad to see it return 
as a "required" component since my company has chosen not to get
the optional module.

If I could put a plug in for something,
it would really be nice if the SOURCE statement allowed a 
calculation or even a conditional. Such as for example: 

05 column 20 pic z,zz9.99 source (compute tot-amount * tot-hours). 
   or 
05 column 20 pic z,zz9.99 source (if overtime = 'y' 
                                   compute tot-amount * tot-over-hours
                                  else
                                   compute tot-amount * tot-hours).
```

###### ↳ ↳ ↳ Re: Top 10 Language Constructs (Cobol)

_(reply depth: 4)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uj91nsg9423hmtrlfbtjqn0db9n0tur21f@4ax.com>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net> <20000714220920.16958.00000671@ng-cu1.aol.com> <8koifk$sf2$1@nntp9.atl.mindspring.net> <396FEFD3.D71173FD@swbell.net>`

```
On Sat, 15 Jul 2000 00:00:03 -0500, Ron <NoSoy@swbell.net> wrote:

>>> A) Report Writer is still available on IBM mainframes (and PCs) via 
>an add-on product
…[9 more quoted lines elided]…
>05 column 20 pic z,zz9.99 source (compute tot-amount * tot-hours). 
From the Language reference


This clause specifies the source field (or expression) that provides the contents of a
field in your report. The source field is usually outside the REPORT SECTION, but 
may also be implicitly defined within it. 

+-- Format -----------------------------------------------+
|                   +-------------+                       |
|                   v             |                       |
…[4 more quoted lines elided]…
|             +ARE+                                       |
+---------------------------------------------------------+




>   or 
>05 column 20 pic z,zz9.99 source (if overtime = 'y' 
>                                   compute tot-amount * tot-over-hours
>                                  else
>                                   compute tot-amount * tot-hours).
Could possibly done using PRESENT WHEN combined with ABSENT WHEN


     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)



      "Imitation is the sincerest form of television."  - The New Mighty Mouse
```

###### ↳ ↳ ↳ Re: Top 10 Language Constructs (Cobol)

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3970B07A.CDC436F2@home.com>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net> <20000714220920.16958.00000671@ng-cu1.aol.com> <8koifk$sf2$1@nntp9.atl.mindspring.net> <396FEFD3.D71173FD@swbell.net>`

```


Ron wrote:
> 
> >> A) Report Writer is still available on IBM mainframes (and PCs) via
…[15 more quoted lines elided]…
>                                    compute tot-amount * tot-hours).

This is not the place to do it, other than feedback on your idea. If you
feel this is a "real need" then your should address your proposal to Don
Schricker, J4 chairman.

Jimmy
```

###### ↳ ↳ ↳ Re: Top 10 Language Constructs (Cobol)

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kpsod$v2t$1@nntp9.atl.mindspring.net>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net> <20000714220920.16958.00000671@ng-cu1.aol.com> <8koifk$sf2$1@nntp9.atl.mindspring.net> <396FEFD3.D71173FD@swbell.net>`

```
The report writer "enhancements" include both of the items that you mention:

1) Source can use an arithmetic expression

2) "WHEN" phrase for conditional inclusions
```

#### ↳ Re: Top 10 Language Constructs (Cobol)

- **From:** WDS@WDS.WDS.5 (WDS)
- **Date:** 2000-07-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39735283.3522697@news1.frb.gov>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net>`

```
On Fri, 14 Jul 2000 10:42:26 +0200, Bruno Gustavs wrote:

>What do you think are the top ten language constructs in Cobol?
[...]

MOVE
IF
PERFORM
ADD
READ
WRITE
SUBTRACT
CALL
```

#### ↳ Re: Top 10 Language Constructs (Cobol)

- **From:** lsunley@mb.sympatico.ca (Lorne Sunley)
- **Date:** 2000-07-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hqdYs1NR7tmZ-pn2-ShYOGvhqQ1RZ@tcpserver>`
- **References:** `<8kmjmf$l7h$1@pollux.ip-plus.net>`

```
On Fri, 14 Jul 2000 08:42:26, "Bruno Gustavs" <GustavsB@ch.sibt.com> 
wrote:

> What do you think are the top ten language constructs in Cobol?

  IF something
      MOVE x to y.
     PERFORM VARYING d from y by 1 until d > 200
            IF something
                 COMPUTE
            ELSE
                  EVALUATE d
                     WHEN
                         COMPUTE
                     WHEN
                         MOVE
                  END-EVALUATE
            END-IF
       END-PERFORM.

Now why does it always keep doing that loop ???
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
