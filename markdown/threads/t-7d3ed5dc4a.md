[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF DialogSystem vs. Everyone else

_17 messages · 9 participants · 2000-04_

---

### MF DialogSystem vs. Everyone else

- **From:** "Bill Wood" <nospambeavis27@bigfoot.com>
- **Date:** 2000-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#cw8h1in$GA.232@cpmsnbbsa03>`

```
I recently ran into a problem that I thought was a bug, but MicroFocus tells
me it is expected behavior and I'm curious if everyone agrees that it is
expected behavior.  Here is the scenario:

Put a button with a mnemonic shortcut on a window
Hide the button
Use the mnemonic to fire the button

My question is should a hidden button fire when the mnemonic is used?  I
don't think so, but Dialog and Visual C both do.  I'm curious if other
products do also.  The workaround is simple enough, disable the button when
you hide it and enable it when you show it.  If we had known about this 2
years ago when we started the project that would be no problem, but our
application currently has over 500 screensets and that is a lot of
retro-fitting.  Anyway, I'm just curious how other products work and what
other people think.  Thanks.
```

#### ↳ Re: MF DialogSystem vs. Everyone else

- **From:** "Lucas, Todd" <todd.lucas@ibm.net>
- **Date:** 2000-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38ea03aa_1@news1.prserv.net>`
- **References:** `<#cw8h1in$GA.232@cpmsnbbsa03>`

```
Or totally dump Dialog System altogether and use a Visual Basic
front-end that calls your Cobol business logic contained in a DLL
created by NetExpress.  I used to be a firm supporter of Dialog - the
only reason was that it worked on OS/2 and Windows.  Now that we have
dropped support for OS/2, VB is the front-end GUI of choice.

Just a thought...

TL

Bill Wood <nospambeavis27@bigfoot.com> wrote in message
news:#cw8h1in$GA.232@cpmsnbbsa03...
> I recently ran into a problem that I thought was a bug, but MicroFocus
tells
> me it is expected behavior and I'm curious if everyone agrees that it
is
> expected behavior.  Here is the scenario:
>
…[4 more quoted lines elided]…
> My question is should a hidden button fire when the mnemonic is used?
I
> don't think so, but Dialog and Visual C both do.  I'm curious if other
> products do also.  The workaround is simple enough, disable the button
when
> you hide it and enable it when you show it.  If we had known about
this 2
> years ago when we started the project that would be no problem, but
our
> application currently has over 500 screensets and that is a lot of
> retro-fitting.  Anyway, I'm just curious how other products work and
what
> other people think.  Thanks.
>
…[4 more quoted lines elided]…
>
```

##### ↳ ↳ Re: MF DialogSystem vs. Everyone else

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38EA18A0.BEF0ABF@home.com>`
- **References:** `<#cw8h1in$GA.232@cpmsnbbsa03> <38ea03aa_1@news1.prserv.net>`

```


"Lucas, Todd" wrote:
> 
> Or totally dump Dialog System altogether and use a Visual Basic
…[6 more quoted lines elided]…
> 
Whoa there ! Don't go dumping anything. (BTW I don't use Dialog System).
From correspondence I see so many different options being used :-

- Fujitsu	 - Thane Hubbell	- SP2
- Fujitsu	 - Pete Dashwood	- Activex
- Fujitsu	 - Don Tees 	  	- Screen Section and  SP2 
- NetExpress	 - Ken Mullins 		- Win APIs
- NetExpress	 - Simon Hart 		- OO/GUIs, D/S and Activex
- NetExpress	 - Jim Smith 		- OO/GUIs
- NetExpress	 - Gene Webb		- OO Visual Basic
- NetExpress	 - Yours truly		- OO/GUIs

Each of the above will give you a sound argument for why they took their
particular route. Which one is right - none - they are all different
solutions. There is a time investment in learning a particular tool,
plus all that code you have written using the 'old' tool. It requires
careful thought before you make a switch. Each new tool means a new
learning curve.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: MF DialogSystem vs. Everyone else

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2000-04-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cegfa$8u$1@hermes.enternet.co.nz>`
- **References:** `<#cw8h1in$GA.232@cpmsnbbsa03> <38ea03aa_1@news1.prserv.net> <38EA18A0.BEF0ABF@home.com>`

```

James J. Gavan wrote in message <38EA18A0.BEF0ABF@home.com>...
>

>Whoa there ! Don't go dumping anything. (BTW I don't use Dialog System).
>From correspondence I see so many different options being used :-
>
>- Fujitsu - Thane Hubbell - SP2
>- Fujitsu - Pete Dashwood - Activex

For MS WINDOWS GUI development I use Fujitsu PowerCOBOL with ActiveX
components where possible. For GUI platform independence and Web Enablement
(where required) I am moving to JAVA and CORBA, with Fujitsu OOCOBOL 97
routines in the background for data processing which is not what JAVA does
best. I am still firmly persuaded that component based development is the
way to go, and I believe OOP is the best way to build the components. (That
is NOT a criticism of structured COBOL, which has served us long and well
over many years.)

Horses for courses. No Evangelism, no bigotry, and totally respect everyone
else's right to do it differently. Getting systems developed is hard enough
without vacillating over what tool to use. I use whatever works, with the
shortest learning curve and the quickest return on investment.

>- Fujitsu - Don Tees   - Screen Section and  SP2
>- NetExpress - Ken Mullins - Win APIs
…[10 more quoted lines elided]…
>learning curve.

Yes it does, Jimmy. Fortunately each one you learn makes the next one a bit
easier. Or maybe we just get smarter with age <grin>??

Pete.
```

##### ↳ ↳ Re: MF DialogSystem vs. Everyone else

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#pgEfkln$GA.351@cpmsnbbsa04>`
- **References:** `<#cw8h1in$GA.232@cpmsnbbsa03> <38ea03aa_1@news1.prserv.net>`

```

Lucas, Todd <todd.lucas@ibm.net> wrote in message
news:38ea03aa_1@news1.prserv.net...
> Or totally dump Dialog System altogether and use a Visual Basic
> front-end that calls your Cobol business logic contained in a DLL
> created by NetExpress.  I used to be a firm supporter of Dialog -
the
> only reason was that it worked on OS/2 and Windows.  Now that we
have
> dropped support for OS/2, VB is the front-end GUI of choice.
>
…[3 more quoted lines elided]…
>
I would have agreed with you in the past, but I think that VB may not
be the language of choice in that it ties you to Windows.
The ability to work on a variety of platforms should still be a
concern.
While there is no current alternative contender for the desktop OS of
choice, it may not be that way forever.

Relational Database products have implemented extensions to SQL, which
effectively bound a user to a product. When competing products came
along which offered a price/performance advantage, those who used the
extensions would have to rewrite portions of their systems to migrate
to a better product.

I think we need to develop flexible solutions.
```

###### ↳ ↳ ↳ Re: MF DialogSystem vs. Everyone else

- **From:** "Lucas, Todd" <todd.lucas@ibm.net>
- **Date:** 2000-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38ea494c_2@news1.prserv.net>`
- **References:** `<#cw8h1in$GA.232@cpmsnbbsa03> <38ea03aa_1@news1.prserv.net> <#pgEfkln$GA.351@cpmsnbbsa04>`

```
You can develop flexible solutions, as long as you keep your business
loginc and front-end user-interface separate.  There is no one GUI
development tool (that I know of) that works on all platforms.  My take
is, if you are going to do something then do it right - use the best
products available for the most widely used platform.  Like I said, we
used Dialog system successfully for more than 4 years, but it outlived
its usefulness when we dumped OS/2.  Not saying that this is the right
solution for you, but it was definitely right for us.

Thanks - TL

DennisHarley <LegacyBlue@email.msn.com> wrote in message
news:#pgEfkln$GA.351@cpmsnbbsa04...
>
> Lucas, Todd <todd.lucas@ibm.net> wrote in message
…[28 more quoted lines elided]…
>
```

##### ↳ ↳ Re: MF DialogSystem vs. Everyone else

- **From:** Rich Rohde <richNOriSPAM@richware.net.invalid>
- **Date:** 2000-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<032a5c88.25b720ba@usw-ex0101-005.remarq.com>`
- **References:** `<#cw8h1in$GA.232@cpmsnbbsa03> <38ea03aa_1@news1.prserv.net>`

```
Todd,

I am thinking about doing the same thing you are doing in
regards to GUI. In order to do VB what all did you purchase
(e.g. VB Suite etc)? This may be a 'duh' question.

Rich

* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network *
The fastest and easiest way to search and participate in Usenet - Free!
```

###### ↳ ↳ ↳ Re: MF DialogSystem vs. Everyone else

- **From:** "Lucas, Todd" <todd.lucas@ibm.net>
- **Date:** 2000-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38ea8498_3@news1.prserv.net>`
- **References:** `<#cw8h1in$GA.232@cpmsnbbsa03> <38ea03aa_1@news1.prserv.net> <032a5c88.25b720ba@usw-ex0101-005.remarq.com>`

```
Rich,

We use all three of the 32-bit MF products (Workbench, NetExpress, and
MFE) and Visual Basic 5 (or 6 if you prefer), and that is all as far as
development goes.  We do alot of API programming to interface with
various communications packages as well (IBM Personal Communications,
TCP/IP, APPC, CPI-C, etc.), but these are probably not required for what
you want to do - but then again only you know what you want to do.
<grin>

We simply create all of our business logic in Cobol and create either
.DLL or .EXE files, and then create a Visual Basic .EXE that invokes the
Cobol .DLL's / .Exe's.  It's really easy and simple to do.  It used to
be a big hassle with the 16-bit MF products, but they have made some
great progress here in the last few years to make their stuff "play"
better with the other "kids" on the block - VB, VC, Win32 API,
Powerbuilder, etc...

If you need some examples of VB calling Cobol just let me know and I
will send some to you off-line...

Thanks - TL
```

###### ↳ ↳ ↳ Re: MF DialogSystem vs. Everyone else

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-04-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38EA8300.613E79F5@home.com>`
- **References:** `<#cw8h1in$GA.232@cpmsnbbsa03> <38ea03aa_1@news1.prserv.net> <032a5c88.25b720ba@usw-ex0101-005.remarq.com>`

```


Rich Rohde wrote:
> 
> Todd,
…[4 more quoted lines elided]…
> 
Rich,

If I was switching from GUIs (and I'm assuming you are talking about
GUIs with the Dialog Editor), then I would seriously consider Flexus SP2
or ScreenIO as serious contenders before VB. Use VB, and yet again all
roads point to Microsloth. Maybe you never saw it on Answerlab but
somebody did comment "Much faster than VB...." - and I don't know if
they were talking GUIs, Win APIs or D/S - but it got my attention.

It wont change your mind but I'll send you privately MyDialog.cbl -
gives you a different slant on GUIs.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: MF DialogSystem vs. Everyone else

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2000-04-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ceemu$68$2@hermes.enternet.co.nz>`
- **References:** `<#cw8h1in$GA.232@cpmsnbbsa03> <38ea03aa_1@news1.prserv.net>`

```

Lucas, Todd wrote in message <38ea03aa_1@news1.prserv.net>...
>Or totally dump Dialog System altogether and use a Visual Basic
>front-end that calls your Cobol business logic contained in a DLL
…[6 more quoted lines elided]…
>TL

Hmmm....so why would anybody dump a system because it works the way it is
SUPPOSED to (rather than the way the programmer thought it ought to...)?

This behaviour of MF DIALOG is (forgive the pun...) right on the button.

I was intrigued by your reason for using and dropping DIALOG.

I also used it (found it very good and liked the separation from the
underlying complexity of PANELS). I dropped it because I dropped MF, not
because there was anything wrong with it.

Did you really only use it because of OS/2? If so, why not use Presentation
Manager?

As for using VB as the GUI development tool of choice, yes, many
corporations are doing this and I have managed several projects where we
used VB successfully as a front end to the mainframe backend. But check
again....VB also implements the properties of a push button in exactly the
same way as DIALOG (and, in fact, anything that uses WINDOWS; it is a
WINDOWS standard).

In this instance, the fault was not with the software but with the
programmer.

Pete.
```

###### ↳ ↳ ↳ Re: MF DialogSystem vs. Everyone else

- **From:** "Lucas, Todd" <todd.lucas@ibm.net>
- **Date:** 2000-04-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38eb5e72_3@news1.prserv.net>`
- **References:** `<#cw8h1in$GA.232@cpmsnbbsa03> <38ea03aa_1@news1.prserv.net> <8ceemu$68$2@hermes.enternet.co.nz>`

```
Can you honestly say that creating / maintaining code in Dialog System
is as easy as doing it in VB?  I certainly did not think so, not to
mention that VB has so much more to offer - not only in the base
language itself, but in third-party custom controls, OCX, etc.

Creating a screenset is fairly easy - maintaining one is altogether
different.  The only reason we used it was because the same code worked
for both OS/2 and Windows platforms.  It was hard to add new
functionality, the passing of variables between the Cobol program and
Dialog was cheesy, not to mention the un-professional look of the
application - and no, it was not the programmers fault on how it looked
either.  Throw into account the extra code to support varying screen
resolutions, and you have a mess that is a maintenance nightmare!

And like you, I wasted alot of time developing native panels
applications before "discovering" Dialog.  At that time I thought it was
the best thing since sliced bread.  I saw how much easier it was to code
an application using it vs. Panels2.  About three years and alot of
frustration later, I discovered VB and it was euphoria all over again!
I guess that's the way of nature though - start with something and
always look for a better way.

I'm relieved that we got rid of it.  Just my take...

TL

Peter E. C. Dashwood <dashwood@enternet.co.nz> wrote in message
news:8ceemu$68$2@hermes.enternet.co.nz...
>
> Lucas, Todd wrote in message <38ea03aa_1@news1.prserv.net>...
…[10 more quoted lines elided]…
> Hmmm....so why would anybody dump a system because it works the way it
is
> SUPPOSED to (rather than the way the programmer thought it ought
to...)?
>
> This behaviour of MF DIALOG is (forgive the pun...) right on the
button.
>
> I was intrigued by your reason for using and dropping DIALOG.
>
> I also used it (found it very good and liked the separation from the
> underlying complexity of PANELS). I dropped it because I dropped MF,
not
> because there was anything wrong with it.
>
> Did you really only use it because of OS/2? If so, why not use
Presentation
> Manager?
>
> As for using VB as the GUI development tool of choice, yes, many
> corporations are doing this and I have managed several projects where
we
> used VB successfully as a front end to the mainframe backend. But
check
> again....VB also implements the properties of a push button in exactly
the
> same way as DIALOG (and, in fact, anything that uses WINDOWS; it is a
> WINDOWS standard).
…[5 more quoted lines elided]…
>
```

#### ↳ Re: MF DialogSystem vs. Everyone else

- **From:** khansen@screenio.com (Kevin Hansen)
- **Date:** 2000-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38ea2f31.90704996@wingate>`
- **References:** `<#cw8h1in$GA.232@cpmsnbbsa03>`

```
Just when you think you've got it figured out, someone comes up with a
new wrinkle...

We would do the same thing today in GUI ScreenIO, but you've got a
very valid point.  If an accelerator or mnemonic key is assigned to a
pushbutton or a menu selection, you'd reasonably expect the
accelerator would be disabled if the menu selection or pushbutton was
grayed out (disabled). 

Otherwise, as you discovered, the user can circumvent your disabling
of the menu item.  It strikes me as clumsy to require you to handle
the accelerator key separately in your program.  The screen manager
should take care of it automatically because the items are clearly
related.

I think we'll incorporate this disabling of the accelerator in our
next update...  Appreciate the idea!

Kevin

On Tue, 4 Apr 2000 08:03:42 -0400, "Bill Wood"
<nospambeavis27@bigfoot.com> wrote:

>Put a button with a mnemonic shortcut on a window
>Hide the button
…[9 more quoted lines elided]…
>other people think.  Thanks.

NORCOM COBOL Programming Tools
GUI ScreenIO; a cool COBOL/Windows Screen Manager
http://www.ScreenIO.com
```

##### ↳ ↳ Re: MF DialogSystem vs. Everyone else

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38ea52c7.64909286@news.cox-internet.com>`
- **References:** `<#cw8h1in$GA.232@cpmsnbbsa03> <38ea2f31.90704996@wingate>`

```
On Tue, 04 Apr 2000 18:25:14 GMT, khansen@screenio.com (Kevin Hansen)
wrote:

>Just when you think you've got it figured out, someone comes up with a
>new wrinkle...
…[6 more quoted lines elided]…
>

There is a difference between "Greyed out" and "hidden" yes?  With
Dialog System I am fairly sure that if you grey it out it won't
respond to the accelerator key.  But hidden - I would not expect it to
respond, but I can see others making a case for having it respond --
those who live in the event driven UI world.   Without the button it
may be difficult to detect the key being pressed, so they assign ALT+H
to a hidden (as opposed to greyed out) button.  

My preference - hidden or greyed out should disable the accelerator
key (as it does with sp2).
```

###### ↳ ↳ ↳ Re: MF DialogSystem vs. Everyone else

- **From:** khansen@screenio.com (Kevin Hansen)
- **Date:** 2000-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38ea5697.100790779@wingate>`
- **References:** `<#cw8h1in$GA.232@cpmsnbbsa03> <38ea2f31.90704996@wingate> <38ea52c7.64909286@news.cox-internet.com>`

```
There is indeed a difference between grayed out and hidden.  We call
'em "blind menu items" instead of hidden, but the principle is the
same;  you might not want to show an item on the menu or on a button,
but you still want it to return an event to the application.

Blind menu items can, of course, also be enabled/disabled at runtime
if you choose to do so, just as a visible button or menu selection may
be grayed out at runtime.

Kevin

On Tue, 04 Apr 2000 20:41:51 GMT, thaneH@softwaresimple.com (Thane
Hubbell) wrote:
>
>There is a difference between "Greyed out" and "hidden" yes?  With
…[5 more quoted lines elided]…
>to a hidden (as opposed to greyed out) button.  


NORCOM COBOL Programming Tools
GUI ScreenIO; a cool COBOL/Windows Screen Manager
http://www.ScreenIO.com
```

#### ↳ Re: MF DialogSystem vs. Everyone else

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38ea51e3.64681586@news.cox-internet.com>`
- **References:** `<#cw8h1in$GA.232@cpmsnbbsa03>`

```
On Tue, 4 Apr 2000 08:03:42 -0400, "Bill Wood"
<nospambeavis27@bigfoot.com> wrote:

>I recently ran into a problem that I thought was a bug, but MicroFocus tells
>me it is expected behavior and I'm curious if everyone agrees that it is
…[14 more quoted lines elided]…
>

I would expect it NOT to fire on the shortcut key.

With Flexus COBOL sp2 a hidden button does not respond to the shortcut
key.  I hide them on occasion, although more often I grey them out
(also will not fire).
```

#### ↳ Re: MF DialogSystem vs. Everyone else

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-04-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cdval$d45$1@news.inet.tele.dk>`
- **References:** `<#cw8h1in$GA.232@cpmsnbbsa03>`

```
Hey,
I beleive you started a discussion about methods and tools, but you ask
about shortcut keys in Dialog System.

I would expect all disabled objects to disabled for mouse-clicks and
shortcut keys. If you hide something, it's still there - so, disable and
then hide; that might be the solution.

On the other hand - you could have some global dialog that unconditionally
executes a procedure on an event as F5. I wouldn't expect that dialog to be
stopped, just because you disable an object.

Regards
Ib

Bill Wood skrev i meddelelsen <#cw8h1in$GA.232@cpmsnbbsa03>...
>I recently ran into a problem that I thought was a bug, but MicroFocus
tells
>me it is expected behavior and I'm curious if everyone agrees that it is
>expected behavior.  Here is the scenario:
…[18 more quoted lines elided]…
>
```

#### ↳ Re: MF DialogSystem vs. Everyone else

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2000-04-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ceemt$68$1@hermes.enternet.co.nz>`
- **References:** `<#cw8h1in$GA.232@cpmsnbbsa03>`

```
This is exactly the behaviour I would expect programming in C, VB, JAVA, or
Fujitsu PowerCOBOL.

Just because you HIDE a control does NOT mean it is disabled.

It's no reflection on MF Dialog (other than a good one; they have
implemented it the way Windows intended)

This, to me, is a perfect example of what's going wrong with COBOL.

People don't bother to read how things actually work, implement in the way
in which they think it should work, then jump up and down to get the
Language changed because their way is "better".

Take the COBOL DIVIDE for example. The original language spec. specified:
DIVIDE ....INTO... (This was because BY had already been used for MULTIPLY).
Thousands of programmers wrote DIVIDE... BY (well, COBOL's an "English-like"
language, right?), grizzled because it didn't work and the vendors then
incorporated it into the language. A trivial example, granted, but there are
many more.

So now we see someone who obviously doesn't understand Windows controls,
writing a Windows program and then suggesting that what the Vendor has
provided is wrong. Why? Because it didn't do what one person expected.

How can we ever get a simple, stable, standard in anything if everyone
expects it to behave in a different manner? By the time the language is
extended to include all the "good ideas" we end up with a morass of options
and alternative constructs which suck all the simple elegance which was
there originally, out of it. (Just look at COBOL today...)

Here's my take on it: Use what is provided. If it doesn't work AS SPECIFIED,
then jump up and down at the vendor, or use some other tool. If you REALLY
don't like what is specified, then consider using a different tool.

The over-complication of COBOL (supposedly in response to user demands, but
actually in a frantic game of "catch-up", to enable commercial programmers
to put men in orbit, analyze chaos theory, and re-write the Operating
System) should be a warning to us all. If something is simple, elegant, and
ideally suited to the purpose for which it was intended, DON'T MESS WITH IT!

Fortunately, Bill Gates has too much on his mind at the moment to worry
about changing the behaviour of Windows controls, so get used to the fact
that hidden controls are NOT disabled, write it up to experience, and move
on....

Pete.

Bill Wood wrote in message <#cw8h1in$GA.232@cpmsnbbsa03>...
>I recently ran into a problem that I thought was a bug, but MicroFocus
tells
>me it is expected behavior and I'm curious if everyone agrees that it is
>expected behavior.  Here is the scenario:
…[7 more quoted lines elided]…
>products do also.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
