[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# New to Cobol

_18 messages · 12 participants · 2000-03 → 2000-04_

---

### New to Cobol

- **From:** "John Wolanski" <brgr88@REMOVETHISyahoo.com>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_gyE4.9678$_c3.65791@typhoon.columbus.rr.com>`

```
Hello, Group!

I was recently looking through the bargain books section of a local computer
store when I found a "Teach Yourself Cobol in 21 Days, by Mo Budlong" for
really cheap.

Being that I am a mainframe operator in my job, and that there are scant few
books, training materials, etc. readily available on the open market for an
affordable price (at least I can't find any), I thought that learning Cobol
might come in handy when looking for promotions, etc. in my job, so I
grabbed a copy.

The book says that I'm going to need a compiler to do any of the work in it,
and that's where I need help (and I highly doubt that my company will let me
"mess around" with their utilities).

The author recommended the Micro Focus Personal compiler, but also made
mention of compilers made by other companies.

I went to the MF website and their DOS version is about $50, but it also
mentioned that it doesn't make .exe files, and all programs must be run
through some other software feature.  Is there a compiler that makes
plain-old .exe files to run?  Or is this not the best way to go about it?
Is there one available that isn't too expensive?

I hunted down and found Cobol650, but I don't seem to be doing it right,
since every time I try to compile a source code file, I just get a "Please
donate to..." message and it quits.  And from what I can gather from the
instructions, it seems to be lacking a linking utility anyway.  Is there
some sort of voodoo that needs worked to get this program to run?

What about those Cobol books that come with (I believe) a compiler?  Are
those any good to work with?  I'm not looking for anything GUI or fancy or
anything.  I noticed a few books like this; is there any one in particular
that has a good software package (preferably one that isn't a demo version)?

Thanks for any help, and I hope I wasn't too annoying with all my questions.
```

#### ↳ Re: New to Cobol

- **From:** Charles Hammond <ceh1@ritz.cec.wustl.edu>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.SOL.3.96.1000330104950.3875A-100000@ritz.cec.wustl.edu>`
- **References:** `<_gyE4.9678$_c3.65791@typhoon.columbus.rr.com>`

```
Compilers for different languages often say they can not make an exe file,
this means that you can write a program in source program and you can
execute it from within the compiler. However you can run the program.
You can learn how the logic of a program works in this method.  Try
looking at Amazon.com for books on COBOL I bought one a while back written
for the AS400 COBOL.  

Mainframe COBOL is a lot different in how the programs are stored linked
and run.  You have to run programs with job control language (JCL) which
is specific to the actual mainframe environment.  Whether it be
Honneywell, Mitsubishi, IBM or others.

There is also a difference between the Batch programs you will find in
most programming books and CICS which is an on-line interactive kind of
programming.  When you get into larger organizations, you will also
see DBMS database and possible use of COBOL to maintain it.  Then you have
the object oriented crowd and the GUI interfaces.  At the present there is
a big demand for possible applications that can be run accross platforms
like the internet that interact with data live on the mainframe.

Microfocus also makes a compiler they call Workbench which I have seen
used.  I've used both versions.  The Workbench has it's benefits but the
version I saw didn't have any extra object oriented stuff in it.  The
Windows versions can help you learn quite a bit.  It is possible to run
a program and watch it step through all the steps to spot possible
problems.  The other day I was doing something with it and set it up so I
could watch the output and the program running through it's steps at the
same time in different windows.  But you need more advanced training.  Of
course you have to start somewhere.

Would be nice if they had a version that used a PC and simulated a
mainframe environment.

Charles Hammond, BSIM Undergraduate Program

On Thu, 30 Mar 2000, John Wolanski wrote:

> Hello, Group!
> 
…[38 more quoted lines elided]…
>
```

##### ↳ ↳ Re: New to Cobol

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Vt9F4.805$lT3.38499@news.swbell.net>`
- **References:** `<_gyE4.9678$_c3.65791@typhoon.columbus.rr.com> <Pine.SOL.3.96.1000330104950.3875A-100000@ritz.cec.wustl.edu>`

```

Charles Hammond <ceh1@ritz.cec.wustl.edu

> Would be nice if they had a version that used a PC and simulated a
> mainframe environment.
>

This is Realia's niche. Download from mainframe, develop, test, upload
to mainframe.

We used to use Realia. Don't anymore.
```

#### ↳ Re: New to Cobol

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E2D5E8.3B092AA7@home.com>`
- **References:** `<_gyE4.9678$_c3.65791@typhoon.columbus.rr.com>`

```


John Wolanski wrote:
> 
> Hello, Group!
…[3 more quoted lines elided]…
> really cheap.

Don't know "TYC in 21 Days" - but one academic jumped in here a couple
of months back and gave it a big RASPBERRY - can't comment other than
that.

Better bet, get Thane Hubbell's "TYC COBOL in 24 Hours" comes with 
Fujitsu compiler - so we're talking a desktop to play with. Any decent 
bookshop will have it or Amazon.com/Barnes & Nobel.

Jimmy


> 
> Being that I am a mainframe operator in my job, and that there are scant few
…[29 more quoted lines elided]…
> Thanks for any help, and I hope I wasn't too annoying with all my questions.
```

##### ↳ ↳ Re: New to Cobol

- **From:** "John Wolanski" <brgr88@REMOVETHISyahoo.com>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WrBE4.9729$_c3.68222@typhoon.columbus.rr.com>`
- **References:** `<_gyE4.9678$_c3.65791@typhoon.columbus.rr.com> <38E2D5E8.3B092AA7@home.com>`

```
What's a "RASPBERRY"?  Is that bad or good?

At any rate, thanks to you & Mr. Hubbel for the "24 Hours" suggestion!  I've
had success with other 24 Hours books and they're usually priced right.

James J. Gavan <jjgavan@home.com> wrote in message
news:38E2D5E8.3B092AA7@home.com...
> Don't know "TYC in 21 Days" - but one academic jumped in here a couple
> of months back and gave it a big RASPBERRY - can't comment other than
…[4 more quoted lines elided]…
> bookshop will have it or Amazon.com/Barnes & Nobel.
```

###### ↳ ↳ ↳ Re: New to Cobol

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E38CE2.45960DE0@home.com>`
- **References:** `<_gyE4.9678$_c3.65791@typhoon.columbus.rr.com> <38E2D5E8.3B092AA7@home.com> <WrBE4.9729$_c3.68222@typhoon.columbus.rr.com>`

```


John Wolanski wrote:
> 
> What's a "RASPBERRY"?  Is that bad or good?
> 
OK. Bill Klein speaks both 'American' and 'English'  - i.e.
vacation/holiday - so please translate Bill :-)

Jimmy
```

###### ↳ ↳ ↳ Re: New to Cobol

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c2mp3$ks6$1@slb3.atl.mindspring.net>`
- **References:** `<_gyE4.9678$_c3.65791@typhoon.columbus.rr.com> <38E2D5E8.3B092AA7@home.com> <WrBE4.9729$_c3.68222@typhoon.columbus.rr.com> <38E38CE2.45960DE0@home.com>`

```
My "usually reliable source" (and boy did I need to think who to contact on
this one) says,

"To 'give someone the raspberry' or 'blow a raspberry' are both in use in UK
English.  The meaning is exactly as you describe and it is a show of
disrespect or dismissal, often considered immature or vulgar.  The practice
plays a part in slapstick humo(u)r and is highly amusing to children.  I
believe there are also some spoof awards known as the Golden Raspberries..."
```

###### ↳ ↳ ↳ Re: New to Cobol

_(reply depth: 5)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cr5F4.15865$0o4.94449@iad-read.news.verio.net>`
- **References:** `<_gyE4.9678$_c3.65791@typhoon.columbus.rr.com> <WrBE4.9729$_c3.68222@typhoon.columbus.rr.com> <38E38CE2.45960DE0@home.com> <8c2mp3$ks6$1@slb3.atl.mindspring.net>`

```
In article <8c2mp3$ks6$1@slb3.atl.mindspring.net>,
William M. Klein <wmklein@nospam.ix.netcom.com> wrote:
>My "usually reliable source" (and boy did I need to think who to contact on
>this one) says,
…[5 more quoted lines elided]…
>believe there are also some spoof awards known as the Golden Raspberries..."

Perhaps, Mr Klein, you might wish to try the obvious before wracking your
brain.  From http://www.m-w.com:

--begin quoted text:

2 [short for raspberry tart, rhyming slang for fart] : a sound of contempt
made by protruding the tongue between the lips and expelling air forcibly
to produce a vibration; broadly : an expression of disapproval or contempt 

--end quoted text

(rhyming slang of this nature is common amongst the 'Cockneys', or those
lower socioeconomic stature born in London within earshot of Bow's Bells)

DD

>"James J. Gavan" <jjgavan@home.com> wrote in message
>news:38E38CE2.45960DE0@home.com...
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: New to Cobol

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E4ECE2.827520F0@home.com>`
- **References:** `<_gyE4.9678$_c3.65791@typhoon.columbus.rr.com> <WrBE4.9729$_c3.68222@typhoon.columbus.rr.com> <38E38CE2.45960DE0@home.com> <8c2mp3$ks6$1@slb3.atl.mindspring.net> <cr5F4.15865$0o4.94449@iad-read.news.verio.net>`

```
I swear ! I swear ! I didn't know its Cockney derivation - and had no
intention of turning this back to the topic of FLATULENCE - yet once
again :-)

Jimmy

docdwarf@clark.net wrote:
> 
> In article <8c2mp3$ks6$1@slb3.atl.mindspring.net>,
…[39 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: New to Cobol

_(reply depth: 7)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xs6F4.15875$0o4.94825@iad-read.news.verio.net>`
- **References:** `<_gyE4.9678$_c3.65791@typhoon.columbus.rr.com> <8c2mp3$ks6$1@slb3.atl.mindspring.net> <cr5F4.15865$0o4.94449@iad-read.news.verio.net> <38E4ECE2.827520F0@home.com>`

```
In article <38E4ECE2.827520F0@home.com>,
James J. Gavan <jjgavan@home.com> wrote:
>I swear ! I swear ! I didn't know its Cockney derivation - and had no
>intention of turning this back to the topic of FLATULENCE - yet once
>again :-)

Then flee, man... run!  Run like the winds!

DD

>
>docdwarf@clark.net wrote:
…[41 more quoted lines elided]…
>> >
```

###### ↳ ↳ ↳ Re: New to Cobol

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FpME4.95036$Hq3.2468785@news2.rdc1.on.home.com>`
- **References:** `<_gyE4.9678$_c3.65791@typhoon.columbus.rr.com> <38E2D5E8.3B092AA7@home.com> <WrBE4.9729$_c3.68222@typhoon.columbus.rr.com>`

```
George Carlin refers to it as a 'bilabial fricative'. It is also known as a
'Bronx cheer'.

Karl

"John Wolanski" <brgr88@REMOVETHISyahoo.com> wrote in message
news:WrBE4.9729$_c3.68222@typhoon.columbus.rr.com...
> What's a "RASPBERRY"?  Is that bad or good?
>
> At any rate, thanks to you & Mr. Hubbel for the "24 Hours" suggestion!
I've
> had success with other 24 Hours books and they're usually priced right.
>
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: New to Cobol

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eTGEqOim$GA.257@cpmsnbbsa05>`
- **References:** `<_gyE4.9678$_c3.65791@typhoon.columbus.rr.com> <38E2D5E8.3B092AA7@home.com> <WrBE4.9729$_c3.68222@typhoon.columbus.rr.com>`

```

"John Wolanski" <brgr88@REMOVETHISyahoo.com> wrote in message
news:WrBE4.9729$_c3.68222@typhoon.columbus.rr.com...
> What's a "RASPBERRY"?  Is that bad or good?

You really don't know?
```

###### ↳ ↳ ↳ Re: New to Cobol

- **From:** pknudsen@gw.total-web.net (Paul Knudsen)
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38f95dc7.5259753@news.gw.total-web.net>`
- **References:** `<_gyE4.9678$_c3.65791@typhoon.columbus.rr.com> <38E2D5E8.3B092AA7@home.com> <WrBE4.9729$_c3.68222@typhoon.columbus.rr.com>`

```
On Thu, 30 Mar 2000 05:17:42 GMT, "John Wolanski"
<brgr88@REMOVETHISyahoo.com> wrote:

>What's a "RASPBERRY"?  Is that bad or good?
>
It's also known (perhaps better known) as a "Bronx Cheer".  To
explain, The Bronx is a very tough working-class section of New York
City where Yankee Stadium is situated.

---------------------------------------------------------------
SuSE Linux Users meet at: http://clubs.yahoo.com/clubs/suselinuxusers
```

#### ↳ Re: New to Cobol

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38e2d936.6264047@news.cox-internet.com>`
- **References:** `<_gyE4.9678$_c3.65791@typhoon.columbus.rr.com>`

```
On Thu, 30 Mar 2000 01:41:14 GMT, "John Wolanski"
<brgr88@REMOVETHISyahoo.com> wrote:

>What about those Cobol books that come with (I believe) a compiler?  Are
>those any good to work with?  I'm not looking for anything GUI or fancy or
…[3 more quoted lines elided]…
>Thanks for any help, and I hope I wasn't too annoying with all my questions.

Try Sams Teach Yourself COBOL in 24 Hours (by me) - it has the Fujitsu
3.0 compiler.  It's unrestricted except in a few areas - ODBC and
Native code optimization is disabled.  But it's great to learn with
and will make executables.  The book isn't half bad either.
```

##### ↳ ↳ Re: New to Cobol

- **From:** "John Wolanski" <brgr88@REMOVETHISyahoo.com>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WvBE4.9731$_c3.68352@typhoon.columbus.rr.com>`
- **References:** `<_gyE4.9678$_c3.65791@typhoon.columbus.rr.com> <38e2d936.6264047@news.cox-internet.com>`

```
Thanks for the suggestion.  I'm still at the "Hello, World" phase so not
only do I not know about those things you said it restricted, but probably
won't need them for awhile.

Since you wrote the book, your suggestion counts for two points!  :-)

Thane Hubbell <thaneH@softwaresimple.com> wrote in message
news:38e2d936.6264047@news.cox-internet.com...
> Try Sams Teach Yourself COBOL in 24 Hours (by me) - it has the Fujitsu
> 3.0 compiler.  It's unrestricted except in a few areas - ODBC and
> Native code optimization is disabled.  But it's great to learn with
> and will make executables.  The book isn't half bad either.
```

###### ↳ ↳ ↳ Re: New to Cobol

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4qLE4.5735$Fk.83309@news2.mia>`
- **References:** `<_gyE4.9678$_c3.65791@typhoon.columbus.rr.com> <38e2d936.6264047@news.cox-internet.com> <WvBE4.9731$_c3.68352@typhoon.columbus.rr.com>`

```
The problem with "TYC in 21 days" (not Thane's book) is that it asks
the student to repeatedly key in example programs.  You can go through
a tutorial like that and still not be able to write any code yourself.
Though some people like the method, because it is easy (not much
thinking), but in my experience it is a very poor teaching technique.
Examples are important, but unless you begin thinking through the
process yourself, you are not learning how to program.  It works for
playing a musical instrument, for example, because that is basically a
see-do activity.  But programming is a highly creative mental activity,
and you can only learn to do that by thinking it through yourself, not
by blindly keying in sample code written by someone else.  That only
improves your typing skills, not your thinking skills. :-)
```

###### ↳ ↳ ↳ Re: New to Cobol

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EZIE4.13389$0o4.86510@iad-read.news.verio.net>`
- **References:** `<_gyE4.9678$_c3.65791@typhoon.columbus.rr.com> <38e2d936.6264047@news.cox-internet.com> <WvBE4.9731$_c3.68352@typhoon.columbus.rr.com>`

```
In article <WvBE4.9731$_c3.68352@typhoon.columbus.rr.com>,
John Wolanski <brgr88@REMOVETHISyahoo.com> wrote:

[snippage]

>Since you wrote the book, your suggestion counts for two points!  :-)

In which direction?

DD
```

#### ↳ Re: New to Cobol

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OYMr2Njm$GA.306@cpmsnbbsa04>`
- **References:** `<_gyE4.9678$_c3.65791@typhoon.columbus.rr.com>`

```
I just bought Mastering Cobol by Carol Baroudi, published by  SYBEX .
It came with Fujitsu COBOL V 4.
Don't know about the book, haven't read it. Just bought it for the
compiler.

There are additional tools.
Casegen COBOL for Windows is one.
Crystal Reports is another.

John Wolanski <brgr88@REMOVETHISyahoo.com> wrote in message
news:_gyE4.9678$_c3.65791@typhoon.columbus.rr.com...
> Hello, Group!
>
> I was recently looking through the bargain books section of a local
computer
> store when I found a "Teach Yourself Cobol in 21 Days, by Mo
Budlong" for
> really cheap.
>
> Being that I am a mainframe operator in my job, and that there are
scant few
> books, training materials, etc. readily available on the open market
for an
> affordable price (at least I can't find any), I thought that
learning Cobol
> might come in handy when looking for promotions, etc. in my job, so
I
> grabbed a copy.
>
> The book says that I'm going to need a compiler to do any of the
work in it,
> and that's where I need help (and I highly doubt that my company
will let me
> "mess around" with their utilities).
>
> The author recommended the Micro Focus Personal compiler, but also
made
> mention of compilers made by other companies.
>
> I went to the MF website and their DOS version is about $50, but it
also
> mentioned that it doesn't make .exe files, and all programs must be
run
> through some other software feature.  Is there a compiler that makes
> plain-old .exe files to run?  Or is this not the best way to go
about it?
> Is there one available that isn't too expensive?
>
> I hunted down and found Cobol650, but I don't seem to be doing it
right,
> since every time I try to compile a source code file, I just get a
"Please
> donate to..." message and it quits.  And from what I can gather from
the
> instructions, it seems to be lacking a linking utility anyway.  Is
there
> some sort of voodoo that needs worked to get this program to run?
>
> What about those Cobol books that come with (I believe) a compiler?
Are
> those any good to work with?  I'm not looking for anything GUI or
fancy or
> anything.  I noticed a few books like this; is there any one in
particular
> that has a good software package (preferably one that isn't a demo
version)?
>
> Thanks for any help, and I hope I wasn't too annoying with all my
questions.
>
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
