[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Graphical User Interface

_143 messages · 30 participants · 2000-06 → 2000-07_

---

### Graphical User Interface

- **From:** "Steven Helsen" <s.helsen@planetinternet.be>
- **Date:** 2000-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8j156q$m7c$1@news.planetinternet.be>`

```
Hi,

I'm planning on making a program (a quiz) in Cobol.
To make it more attractive, I would like to make use of a GUI (I'm kinda fed
up with typing 100s of lines in the screen section just to obtain some lousy
dos-screebs). I also want to work with *.gif or *.jpg pictures (i.e.
displaying them on the screen during the program). I'm using CA-Realia 3.0
on a Win-platform.
My questions:
```

#### ↳ Re: Graphical User Interface

- **From:** jets@nbnet.nb.ca (Tony M. Mina)
- **Date:** 2000-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3954e87b.7733996@allnews.nbnet.nb.ca>`
- **References:** `<8j156q$m7c$1@news.planetinternet.be>`

```
We are using Cobol Sp2 and FormPrint from Flexus International. You
don't need screen section in your cobol program.  Visit their site at
www.flexus.com.  I believe you can download an evaluation copy.

Tony M. Mina



On Sat, 24 Jun 2000 04:07:58 +0200, "Steven Helsen"
<s.helsen@planetinternet.be> wrote:

>Hi,
>
…[8 more quoted lines elided]…
>

Tony M. Mina
Email: jets@nbnet.nb.ca  info@mc-sys.com
Web:   www.mc-sys.com
```

##### ↳ ↳ Re: Graphical User Interface

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 2000-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000624140646.03037.00000326@ng-fd1.aol.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca>`

```
Good Morning,

Flexus Sp2 is a great product and easy to use.

Bob Hennessey
```

###### ↳ ↳ ↳ Re: Graphical User Interface

- **From:** "JSA" <jsa@kona.penguinpowered.com>
- **Date:** 2000-07-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sltgf29dop3112@corp.supernews.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com>`

```
In article <20000624140646.03037.00000326@ng-fd1.aol.com>, bob7536@aol.com
(Bob7536) wrote:
> Good Morning,
> 
…[3 more quoted lines elided]…
> 

You are free to believe it is a great product, but it is anything
but easy to use.  Your code becomes so entangled with the
windows interface that you might as well write in C++.

A good screen interface would handle all of that for you.

Try GUI Screenio at http://www.screenio.com/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<395f33b5.210878021@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com>`

```
Uh, let's not be so general and try to be a bit more fair shall we.

I have been a Screenio AND an sp2 user.

I'm not going to say that one is better than the other, but your
comments lead one to believe that there is a distinct difference in
architecture that makes one more convoluted than the other.

In fact, the two products take very similar approaches.  Each paints a
screen in a separate panel (Although Sp2 allows dynamic creation as
well), and each processes this panel by making a call to a custom
runtime.  This runtime then returns the reason for the return from the
call and the data values associated with the panel in working storage.
This is not dissimilar from the screen section or from BMS Macros.

As I said I have used both products.  In fact, the premise behind both
is excellent - separate your business logic from your user interface.
Given that, how can you say that Sp2 makes the code more "entangled
with the Windows user interface" than Screenio does.  It's just not
true.

To quote somone else who frequents this group:

"It's the artist, not the paintbrush."

On Sat, 01 Jul 2000 20:15:33 -0900, "JSA"
<jsa@kona.penguinpowered.com> wrote:

>In article <20000624140646.03037.00000326@ng-fd1.aol.com>, bob7536@aol.com
>(Bob7536) wrote:
…[16 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 5)_

- **From:** "brucepbarrett" <brucepbarrett@email.msn.com>
- **Date:** 2000-07-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#yJBo1C5$GA.293@cpmsnbbsa09>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100>`

```
How do these compare to DIALOG?

"Thane Hubbell" <thaneH@softwaresimple.com> wrote in message
news:395f33b5.210878021@207.126.101.100...
> Uh, let's not be so general and try to be a bit more fair shall we.
>
…[26 more quoted lines elided]…
> >In article <20000624140646.03037.00000326@ng-fd1.aol.com>,
bob7536@aol.com
> >(Bob7536) wrote:
> >> Good Morning,
…[19 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 6)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<395f4b08.216849388@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09>`

```
Good Question.  I have also used Dialog System.  I'll lump Dialog
System and PowerCOBOL together for this post if you don't mind - each
takes a similar approach.

Sp2 and Screenio present and process a whole "window" for you.
Control returns to your program when a specific "action" occurs.  This
could be a push button, a menu selection or even a change in value in
a field - if you so define your "panel".  There's no "CODE" in your
panel definitions -- you simply specify certain field attributes and
this controls how the fields are formatted and when control is
returned to your program.

Calls to the runtime are standard COBOL code.

Dialog System and Fujitsu POWER COBOL are "event driven" tools.  There
is a certain level of tedium when creating the (Dialog = Screensets,
PowerCOBOL = Forms).  You must put "CODE" behind EACH object on the
screen.  With PowerCOBOL this code is COBOL.  With Dialog System, this
code is a proprietary language called Dialog System.  One big
difference between Dialog System and PowerCOBOL is that the POWERCOBOL
COBOL code behind the objects is compiled into your program.  Dialog
System is not, and thus it is interpreted at runtime by the Dialog
System runtime.

Dialog System only now:

As I said, one must put the keys one wishes to detect, and the events
one wishes to respond to in the "dialog" behind each object.  The
dialog is evaluated at several levels.  When an "event" occurs - be
that a key press, a mouse over, a gain or loss of focus, or whatever,
the runtime first checks the objects dialog to see if any action is
coded for.  If not, it then checks the Windows dialog to see if any
action is coded.  If not, it then checks the "Global" dialog to see if
any action is coded.  This is done for each and every event that
occurs.  It can be quite time consuming to code for because you can
have "accidental" effects quite easily.  For example.  Let's say that
you want a specific action to happen on "lost focus" so you code a
loss focus event in your window dialog.  The code behind this event
you want only to execute when the WINDOW loses focus and not any of
the objects in the window.  In this case, you have to code dummy noop
lost focus events on each and every control in the window -- or else
your "window" lost focus event will trigger when any object loses
focus.  (We battled side effects like this for quite some time until
we came up with some very strict standards for how things were to be
done).

The bottom line is that the root difference is that Dialog System and
PowerCOBOL are event driven tools, where Sp2 and Screenio handle the
event driven tedium for you and return "screens" of data, not unlike a
Screen Section or BMS defined Map with CICS.  

Because of this is it MUCH easier to separate the interface from the
application using Sp2 or Screenio.

An additional note - there's more than screen handling that can happen
in "Dialog" - you can move data around, call programs, etc within the
Proprietary dialog language.  This makes maintenance harder, as it's
difficult to find out where something is really happening.


On Sun, 2 Jul 2000 09:59:01 -0400, "brucepbarrett"
<brucepbarrett@email.msn.com> wrote:

>How do these compare to DIALOG?
>
…[55 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-07-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<395FB812.8BECDFEC@home.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100>`

```


Thane Hubbell wrote:
> 
> Good Question.  I have also used Dialog System.  I'll lump Dialog
…[3 more quoted lines elided]…
> Sp2 and Screenio present and process a whole "window" for you.
<snip>...

I thought ouch ! when I saw the first query on this topic, but in both
your posts you have been fair - I was a little curious when you
emphasised the separate 'dialog' routines triggered events, but then you
confirmed later that SP2/Scrennio in fact do this for you.

For the other person who commented, note that Bob Hennessey attended a
NetExpress Dialog System course and then finished up using SP2 - what
does that tell you.

Thane your quote "It's the artist not the paintbrush". MCM will be ever
so pleased - you got it right this time <G>

Jimmy
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 8)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-07-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zv985.1028$q94.260788@paloalto-snr1.gtei.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FB812.8BECDFEC@home.com>`

```
James J. Gavan <jjgavan@home.com> wrote in message
news:395FB812.8BECDFEC@home.com...
>
> Thane your quote "It's the artist not the paintbrush". MCM will be ever
> so pleased - you got it right this time <G>
>

Thane obviously be good people.

MCM
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 7)_

- **From:** nowitt@freedsl.com
- **Date:** 2000-07-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<395FD244.C6A64190@freedsl.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100>`

```
I challenge Dialog, SpII and ScreenIO to even come close to doing this
(http://www.ils-international.com/goldmine/newcobol.htm) as elegantly and as
efficiently as it has been beautifully done using PowerCOBOL from Fujitsu.

If some of you cannot grasp the finesse behind this work, let me just ask one
question: can any of the 3 mess ketir* cited above do what is shown in
picture 1 through 13 in 3 second flat on a 200mhz machine?.

*-One of my middle Eastern friend told me that ketir means "a lot".  Got it??

By the way all products have been evaluated, and we are top experts in Dialog
(now try changing fonts in a screenset already loaded, flipping controls or
even moving a control 1 single pixel from is location)

If you can't do it 100% in COBOL then may be you should consider changing
career!

COBOL is dead, Long live COBOL
Nowitt Oal


Thane Hubbell wrote:

> Good Question.  I have also used Dialog System.  I'll lump Dialog
> System and PowerCOBOL together for this post if you don't mind - each
…[121 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 8)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-07-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39608D03.698ECA6E@zip.com.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com>`

```
nowitt@freedsl.com wrote:
> 
> I challenge Dialog, SpII and ScreenIO to even come close to doing this
> (http://www.ils-international.com/goldmine/newcobol.htm) as elegantly and as
> efficiently as it has been beautifully done using PowerCOBOL from Fujitsu.

I am note a power cobol expert but the little I have seen indicates
that it is a fundamentally bad design of code wizards.  A little
explanation is needed.

If you design an application in power cobol version xx and upgrade to
version xx+2 does your application magically take on the benefits of
the new release.  The answer is no because the code is generated
directly into the application.  This also means that bugs in version
xx will not automatically be corrected when you upgrade.

Windows needs to be hidden more behind called modules (or OO methods)
this means that the upgrades will automatically work.

Also putting so much code into the business space leads to a tight
interconnection between the screen and the business.  This is bad
design as we move from windows to Unix to other platforms much faster
now days.

The isolation of screenio and SPII gives it some benefits in this
regard.  A simple relink is the most that would be needed to correct
some flaw in the screen generation code.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 9)_

- **From:** nowitt@freedsl.com
- **Date:** 2000-07-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3960DE42.A8712695@freedsl.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au>`

```
Ken Foskey wrote:
nowitt@freedsl.com wrote:
>
> I challenge Dialog, SpII and ScreenIO to even come close to doing this
> (http://www.ils-international.com/goldmine/newcobol.htm) as elegantly and as
> efficiently as it has been beautifully done using PowerCOBOL from Fujitsu.

I am note a power cobol expert but the little I have seen indicates
that it is a fundamentally bad design of code wizards.  A little
explanation is needed.
        Yes you are right:  You are not an expert.  Therefore your opinion has no
        significance if no value at all.  How can you pretend to speak of
        "fundamental bad design" when you know so little about what you can do
        with this master tool or even how it is structured.

If you design an application in power cobol version xx and upgrade to
version xx+2 does your application magically take on the benefits of
the new release.  The answer is no because the code is generated
directly into the application.  This also means that bugs in version
xx will not automatically be corrected when you upgrade.

        It is obvious that you have no clue about how PowerCOBOL works.
        For your information the system components described in
        http://www.ils-international.com/goldmine/newcobol.htm were developed
        in Feb. 1999 using version 4.2.  In May 2000 they have been rebuild at
        a click of button (Project Rebuild Menu option) a few minutes later all
        DLL and main EXE run with no glitches under version 5.0b and with
        NO user programs modifications.

        Your theory is quite false actually.  Because the code is indeed generated

        directly into the application,  we can be sure that any bad code generated
in
        the previous version (and we have encountered none) would be generated
        correctly, provided that indeed there was some buggy code generated in
        the previous version and that Fujitsu has rewrote it.

Windows needs to be hidden more behind called modules (or OO methods)
this means that the upgrades will automatically work.

        It is again obvious that you have not understood how PowerCOBOL works.
        ALL controls activation-deactivation, manipulation and properties are
        performed via the INVOKE "methods" USING "properties".
        it is unmistakably Object Orientation.  It is OO COBOL.  This DOES mean
        that upgrades will automatically work.  Converting from v. 4.2 to 5.0 DID
        prove that your theory is false.

        In addition Windows and its cryptic WinAPI ARE hidden totally behind
        INVOKE "methods" (CALLed modules using your language).

Also putting so much code into the business space leads to a tight
interconnection between the screen and the business.  This is bad
design as we move from windows to Unix to other platforms much faster
now days.

        WRONG!!   As a wise person did put it earlier, "it's not the brush, it's
the artist"
        the system described in
http://www.ils-international.com/goldmine/newcobol.htm was
        designed is such a way that COBOL programs are used 100% for the business
        logic and the User Interface  parameters storage and validation (user
logon,
        user taste [colors, fonts, graphics, native tongue, writing direction,
etc., etc. etc.]
        are all retrieved, validated, updated and saved using COBOL programs.

        The GUI part simply gets what is passed to it by the appropriate COBOL
program
        and respond accordingly.  In fact one could use Windows handlers such as
SPII
        or GUI ScreenIO and connect to the COBOL programs described above and it
        would run OK.  In fact with some graphic limitations one could use a
character
        screen handler such as  and use the business and user interface
        COBOL programs.   In both instances (SPII / GUI ScreenIO and CHAR ScreenIO

        one would loose all the other functionality that ONLY PowerCOBOL offers is
the
        100% control that the properly trained developer would have over the
COMPLETE
        Windows development such as real-time change of ALL controls properties
and
        other things such as control flipping, native tongue switching, etc.)

The isolation of screenio and SPII gives it some benefits in this
regard.  A simple relink is the most that would be needed to correct
some flaw in the screen generation code.

        The isolation of screenio and SPII [and DIALOG SYSTEM] give the
sophisticated
        programmer only one thing: Limitations.

        Unlike PowerCOBOL which gives you Full power and control over the real
Windows
        Environment GUI development like C++, products such as SPII, GUI ScreenIO
        and the famous DIALOG SYSTEM still use the old fashion mentality of
        DISPLAY/ACCEPT character Screen or the CICS SEND/RECEIVE way of working
        with the GUI Windows Environment.

        As to "a simple relink is the most that would be needed to correct some
flaw in the screen
        generation code", so does PowerCOBOL.  A simple click on the "Rebuild
project" Menu
        option give you a freshly compiled and relinked application, and thanks to
the generated
        code being being part of the application, PowerCOBOL give you something
that now
        other Screen Handler can: High speed execution.  and lightening speed
window displays.

My regards to the people of the land down under
Nowitt Oal

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 10)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3960e0d0.81248845@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com>`

```
On Mon, 03 Jul 2000 18:39:02 GMT, nowitt@freedsl.com wrote:


>        It is again obvious that you have not understood how PowerCOBOL works.
>        ALL controls activation-deactivation, manipulation and properties are
…[3 more quoted lines elided]…
>        prove that your theory is false.


>        The isolation of screenio and SPII [and DIALOG SYSTEM] give the
>sophisticated
>        programmer only one thing: Limitations.
>


What is obvious is that you don't understand Sp2, Screenio or Dialog
System.  Dialog System and PowerCOBOL have the same "problem". That is
each utilizes an event driven programming model that requires the
programmer to write code for each object on the screen.  Sp2 and
Screenio do not.  Which is better?  I have my opinion, others have
theirs. 

I have a suggestion for you.  Please, if you are going to compare and
contrast, give specific examples not just generalities.  If you are
going to make statements like  the above, try not to be so insulting
to your desired audience.  Read that again -- it says that if you are
a "Sophisticated" programmer than the other tools give you
limitations.  This infers several things:  Being a "Sophisticat" is
good.  If you are not such a programmer, you are not good.  PowerCOBOL
is unlimited.  (Really?).

I'm asking you also to please tone this down a bit.  I don't think you
realize it but you are coming off as a bit of a snakeoil salesman.  

If this is Roger (and I don't think it is, but I could be wrong) or
someone who works for Roger, please give me a call -- you have my
number and we need to talk.



>        Unlike PowerCOBOL which gives you Full power and control over the real
>Windows
…[26 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 11)_

- **From:** nowitt@freedsl.com
- **Date:** 2000-07-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3960FEC0.7864B87D@freedsl.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com> <3960e0d0.81248845@207.126.101.100>`

```

Thane Hubbell wrote:
On Mon, 03 Jul 2000 18:39:02 GMT, nowitt@freedsl.com wrote:

What is obvious is that you don't understand Sp2, Screenio or Dialog
System.  Dialog System and PowerCOBOL have the same "problem". That is
each utilizes an event driven programming model that requires the
programmer to write code for each object on the screen.  Sp2 and
Screenio do not.  Which is better?  I have my opinion, others have
theirs.

        Perhaps it is you who really did not understand my lines:

        I have described SPII and GUI ScreenIO as Screen handler similar to CICS
        and the old character ScreenIO based on the ACCEPT/DISPLAY technology.

        DIALOG although is somewhat Event Driven - I grant you that - behave still as
        if one is working with the character screen ACCEPT/DISPLAY.  The proof?
        There is noway in DIALOG to return to the COBOL program that has
        loaded the screenset until you do a RETC - which technically is a SEND screen.
        Once you return to the COBOL program and AS LONG AS the program
        is processing - let say a large database search - your active window in the
screenset
        is ""dead".  You can do nothing with it: enrty fields are locked, radio/check
buttons
        are inoperable, etc.. they do not come back "alive" until the COBOL program
        performs a CALL DIALOG-SYSTEM USING DATABLOCK....It is technically
        a RECEIVE screen.
        If the user desides that it was enough waiting for the data to show on the
screen and clicks on
        -let say an "Exit" button the "Event"  will not be processed until the COBOL
program has
         completed the CALL DIALOG-SYSTEM....

        This what I would call "faked"  Event Driven support.

I have a suggestion for you.  Please, if you are going to compare and
contrast, give specific examples not just generalities.  If you are
going to make statements like  the above, try not to be so insulting
to your desired audience.  Read that again -- it says that if you are
a "Sophisticated" programmer than the other tools give you
limitations.  This infers several things:  Being a "Sophisticat" is
good.  If you are not such a programmer, you are not good.  PowerCOBOL
is unlimited.  (Really?).

            Specific example?  Hum...
            1- DIALOG, SPII, GUI ScreenIO.  Try moving a control, any control
            from one place to another on a window at runtime.

            2-DIALOG, SPII, GUI ScreenIO.  Try flipping controls as if you were
            looking at them in a mirror at runtime.

            3-DIALOG try changing fonts in a screenset already loaded in memory.
            Datablock - Why one has to carry all that fat unused space in the screenset

            just because i.e. the fourth program down the line is using a table or 20
rows
            of 250 bytes?

             4-DIALOG why to you have to build multiple screensets and "push 'n pop"
            screenset clugging memory with bulky screensets megabytes sized?  Not to
            mention the record breaking craches for corrupted memory

            I could go on for a long time...

            Good or bad has nothing to do with being "Sophisticated".
            By "Sophisticated programmer" I mean someone who is looking
            into accomplishing much more that the average programmer
            who is given a tool, GUI or otherwise, happy to accept just
            what the tool is allowing him/her to accomplish.

            With GUI tools mentioned in this topic, the programmer's
            imagination and creativity are limited by those tools.
            With PowerCOBOL the capabilities of the tool are limited only by
            the probrammer's imagination and creativity which makes the tool unlimited.

I'm asking you also to please tone this down a bit.  I don't think you
realize it but you are coming off as a bit of a snakeoil salesman.

            It seems that you asking to too many people to "tone down a bit" today...
            What are you? Somekind of user group classroom teacher??
            Anyhow, why is it that when highlighing defects and qualities of various
            product is someone accused of being snakeoil salesman?

If this is Roger (and I don't think it is, but I could be wrong) or
someone who works for Roger, please give me a call -- you have my
number and we need to talk.

            Yes. You are 100% wrong I am no Roger, and I do not have your number.
            I will be happy to call you if provide me with it.  My direct email is
nowitt@freedsl.com.

            Regards
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 12)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396108e4.91510122@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com> <3960e0d0.81248845@207.126.101.100> <3960FEC0.7864B87D@freedsl.com>`

```
On Mon, 03 Jul 2000 20:57:40 GMT, nowitt@freedsl.com wrote:


>        Perhaps it is you who really did not understand my lines:
>
>        I have described SPII and GUI ScreenIO as Screen handler similar to CICS
>        and the old character ScreenIO based on the ACCEPT/DISPLAY technology.
>

Such Features make these two ideal for legacy code conversion.

>        DIALOG although is somewhat Event Driven - I grant you that - behave still as
>        if one is working with the character screen ACCEPT/DISPLAY.  The proof?
…[9 more quoted lines elided]…
>        a RECEIVE screen.

When multi-threading is NOT used with PowerCOBOL the same is true of
it, is it not?


>            Specific example?  Hum...
>            1- DIALOG, SPII, GUI ScreenIO.  Try moving a control, any control
>            from one place to another on a window at runtime.
>

              This is possible with Sp2, but I don't really want my
users manipulating the user interface.
  
>            2-DIALOG, SPII, GUI ScreenIO.  Try flipping controls as if you were
>            looking at them in a mirror at runtime.
>

What is the real world advantage of this?  Serious question.  

>
>            With GUI tools mentioned in this topic, the programmer's
>            imagination and creativity are limited by those tools.
>            With PowerCOBOL the capabilities of the tool are limited only by
>            the probrammer's imagination and creativity which makes the tool unlimited.

Check past news group postings for PowerCOBOL limitations - especially
in the area of a high number of items in a list box.  Even PowerCOBOL
has it's limitations.


>
>I'm asking you also to please tone this down a bit.  I don't think you
…[5 more quoted lines elided]…
>            product is someone accused of being snakeoil salesman?

I'm actually trying to help you.  I'm nobody.  I'm just a user of
these products and a programmer.  However, I have also been involved
in marketing myself and my products.  You may not realize it, and this
is where I am trying to help you -- and Paul from Merant:  You begin
to sound insulting and franky, Rabid after a time.  Additionaly you
are posting frequently and repetatively.  This is known as news group
Spam.  I'm gratified to see that you are reading the responses to your
messages -- this alone separates your messages from spam.  From the
other replies I am sure you can see that I am not the only reader that
has a negative attitude after reading one of your messages.  

What I'm trying to say is -- You'll attract more flies with honey.

Try posting messages touting the advantages and features of your
product WITHOUT even mentioning the "Competition".  If your tool is
indeed that superior there will be no need to slam the competition --
the tool will speak for itself.

>
>If this is Roger (and I don't think it is, but I could be wrong) or
…[5 more quoted lines elided]…
>nowitt@freedsl.com.

I don't use the phone much.  You have my email address if you wish to
dicuss any of this privately.
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 13)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-07-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6Rc85.124$Vp5.108061@nnrp1.sbc.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com> <3960e0d0.81248845@207.126.101.100> <3960FEC0.7864B87D@freedsl.com> <396108e4.91510122@207.126.101.100>`

```

Thane Hubbell <thaneH@softwaresimple.com>
>
> >        DIALOG although is somewhat Event Driven - I grant you
that - behave still as
> >        if one is working with the character screen ACCEPT/DISPLAY.
The proof?
> >        There is noway in DIALOG to return to the COBOL program
that has
> >        loaded the screenset until you do a RETC - which
technically is a SEND screen.
> >        Once you return to the COBOL program and AS LONG AS the
program
> >        is processing - let say a large database search - your
active window in the
> >screenset
> >        is ""dead".  You can do nothing with it: enrty fields are
locked, radio/check
> >buttons
> >        are inoperable, etc.. they do not come back "alive" until
the COBOL program
> >        performs a CALL DIALOG-SYSTEM USING DATABLOCK....It is
technically
> >        a RECEIVE screen.
>
> When multi-threading is NOT used with PowerCOBOL the same is true of
> it, is it not?

Don't think so, if I understand what you're saying. Assume a program
is processing a large database. On the screen is a button labeled
"Stop." The program has an event procedure to set the variable
STOP-BUTTON-PRESSED to "Y" when the user clicks the button. The
program can test STOP-BUTTON-PRESSED for "Y" anytime.

> Check past news group postings for PowerCOBOL limitations -
especially
> in the area of a high number of items in a list box.  Even
PowerCOBOL
> has it's limitations.

I dunno. I put 65,000 100-character lines in a listbox and PowerCOBOL
didn't croak (it slowed significantly as Windows paged stuff
in-and-out, though).
>
>
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 14)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3961ddb2.145996625@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com> <3960e0d0.81248845@207.126.101.100> <3960FEC0.7864B87D@freedsl.com> <396108e4.91510122@207.126.101.100> <6Rc85.124$Vp5.108061@nnrp1.sbc.net>`

```
On Mon, 3 Jul 2000 22:27:25 -0500, "Jerry P" <jerryp@bisusa.com>
wrote:

>> When multi-threading is NOT used with PowerCOBOL the same is true of
>> it, is it not?
…[6 more quoted lines elided]…
>

Try this when deployed using the single threaded runtime.  I think you
will see that the same thing happens as happens with dialog.  Only one
thing can happen at a time.  The Window may accept the push of the
button, but control will not return to process the message and set the
flag until your database access finishes.  That is UNLESS there is
another thread processing the window and updating the flag in memory.
This multi-treading is a powerful part of PowerCOBOL and is included
in the development version by default, but not in the runtime
distribution unless you specifically install and request it.    

>> Check past news group postings for PowerCOBOL limitations -
>especially
…[6 more quoted lines elided]…
>in-and-out, though).

That's a limitation.  I'm not saying PowerCOBOL is bad.  Far from it.
It's just that the original poster is, shall we say, a little over
enthusiastic.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 15)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-07-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2CI85.6$B5.2476@nnrp3.sbc.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com> <3960e0d0.81248845@207.126.101.100> <3960FEC0.7864B87D@freedsl.com> <396108e4.91510122@207.126.101.100> <6Rc85.124$Vp5.108061@nnrp1.sbc.net> <3961ddb2.145996625@207.126.101.100>`

```

Thane Hubbell <thaneH@softwaresimple.com

>
> Try this when deployed using the single threaded runtime.  I think
you
> will see that the same thing happens as happens with dialog.  Only
one
> thing can happen at a time.  The Window may accept the push of the
> button, but control will not return to process the message and set
the
> flag until your database access finishes.  That is UNLESS there is
> another thread processing the window and updating the flag in
memory.
> This multi-treading is a powerful part of PowerCOBOL and is included
> in the development version by default, but not in the runtime
> distribution unless you specifically install and request it.

Hmmm.

FJ added a method called 'ThruEvents' in Version 5. According to a
sample program (below) you can poke a button on the screen and have an
executing event pause and catch up with the Windows message queue
(which, presumably, has taken note of your button click).

Of course, if, as you say, "ThruEvents" is really part of the
multi-thread runtime, there's a distribution/royalty issue, but the
concept is a good one.



ENVIRONMENT DIVISION.
DATA DIVISION.
WORKING-STORAGE SECTION.
01  RUNNING-FLAG GLOBAL PIC S9(4).               *>In WS of form.
Included here for clarity
   88 IS-RUNNING VALUE 1.
01 I PIC S9(9) COMP-5.
PROCEDURE DIVISION.
    IF IS-RUNNING THEN
      EXIT PROGRAM                        *> Exit to prevent nesting
of the event
    END-IF
    MOVE 1 TO RUNNING-FLAG.               *> Sets the executing flag
    PERFORM VARYING I FROM 1 BY 1 UNTIL I > 1000000
      MOVE I TO "Caption" OF COUNTER     *> Display counter
      IF FUNCTION MOD (I 1000) = 0 THEN
        INVOKE POW-SELF "ThruEvents"     *> Executes any waiting event
procedures
        IF NOT IS-RUNNING THEN           *> Exits if the cancel button
is clicked
          EXIT PERFORM
        END-IF
      END-IF
    END-PERFORM
    MOVE 0 TO RUNNING-FLAG.               *> Releases the executing
flag

Click event of the Cancel  CommandButton

ENVIRONMENT DIVISION.
DATA DIVISION.
WORKING-STORAGE SECTION.
PROCEDURE DIVISION.
    MOVE 0 TO RUNNING-FLAG.  *> Sets the executing flag to 0

QueryClose event of the Form

ENVIRONMENT DIVISION.
DATA DIVISION.
WORKING-STORAGE SECTION.
LINKAGE SECTION.
01  POW-CANCEL  PIC S9(4) COMP-5.

PROCEDURE DIVISION USING POW-CANCEL.
    IF IS-RUNNING THEN
      MOVE POW-TRUE TO POW-CANCEL
    END-IF

Jerry Peacock (not part of the above program)
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 16)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39637889.251187604@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com> <3960e0d0.81248845@207.126.101.100> <3960FEC0.7864B87D@freedsl.com> <396108e4.91510122@207.126.101.100> <6Rc85.124$Vp5.108061@nnrp1.sbc.net> <3961ddb2.145996625@207.126.101.100> <2CI85.6$B5.2476@nnrp3.sbc.net>`

```
On Wed, 5 Jul 2000 10:36:03 -0500, "Jerry P" <jerryp@bisusa.com>
wrote:


>Hmmm.
>
…[9 more quoted lines elided]…
>

Code snipped.  It looks to me like it would NOT require
multi-threading.  It's very similar to what I do with sp2.  You have
to code where you want it to happen, but I just make a call to sp2 to
see if the user did anything while I have been busy.  Contrasting
Dialog System, it's much harder but still possible.  The difference is
that Dialog calls your program, not the other way around, so that you
need to setup some method of picking up where you left off after
dialog executes.

Question for you:  With this function, what happens if SOME OTHER
event has occured - like the selection of a "Print" button where you
have print logic?  Does the printing happen then control returns to
your process -- that was "suspended" when you checked the other
events?

(This assumes that I am correct and this is a single threaded
solution).
 
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 17)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-07-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m0R85.69$B5.72838@nnrp3.sbc.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com> <3960e0d0.81248845@207.126.101.100> <3960FEC0.7864B87D@freedsl.com> <396108e4.91510122@207.126.101.100> <6Rc85.124$Vp5.108061@nnrp1.sbc.net> <3961ddb2.145996625@207.126.101.100> <2CI85.6$B5.2476@nnrp3.sbc.net> <39637889.251187604@207.126.101.100>`

```

Thane Hubbell <thaneH@softwaresimple.com> wrote in message
news:39637889.251187604@207.126.101.100...
> On Wed, 5 Jul 2000 10:36:03 -0500, "Jerry P" <jerryp@bisusa.com>
> wrote:
…[5 more quoted lines elided]…
> >sample program (below) you can poke a button on the screen and have
an
> >executing event pause and catch up with the Windows message queue
> >(which, presumably, has taken note of your button click).
…[11 more quoted lines elided]…
>

Gosh. I don't know. A guess: The events 'nest' (like a stack). Logic
would indicate something like:

Event "A" begins
     (user presses buttons to activate events "B" "C" and "D" in that
order (or, more likely, if our user, hits the "B" button 47 times, the
last three with his fist))
   Event "A" pauses
      Event "B" begins
      Event "B" ends
      Event "C" begins
         Event "C" pauses
            Event "D" begins
            Event "D" ends
         Event "C" resumes
         Event "C" ends
   Event "A" resumes
   Event "A" ends
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 18)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3963e892.2465157@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com> <3960e0d0.81248845@207.126.101.100> <3960FEC0.7864B87D@freedsl.com> <396108e4.91510122@207.126.101.100> <6Rc85.124$Vp5.108061@nnrp1.sbc.net> <3961ddb2.145996625@207.126.101.100> <2CI85.6$B5.2476@nnrp3.sbc.net> <39637889.251187604@207.126.101.100> <m0R85.69$B5.72838@nnrp3.sbc.net>`

```
On Wed, 5 Jul 2000 20:09:26 -0500, "Jerry P" <jerryp@bisusa.com>
wrote:


>Event "A" begins
>     (user presses buttons to activate events "B" "C" and "D" in that
…[13 more quoted lines elided]…
>

Sounds reasonable.  Do you ever call another program from a button or
something like that?  What I would be concerned about is when you
click button A and start a database update, and keep checking the Thru
event, and they click button B, which is a query against the same
database.  Does the program called by B execute before you return from
the invocation of the Thru Event (I see a real boon for
Multi-Threading here)?  What about undesirable side effects?  Can you
control what events are allowed on the thru event checking?
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 12)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jt7ms$n54$1@nnrp1.deja.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com> <3960e0d0.81248845@207.126.101.100> <3960FEC0.7864B87D@freedsl.com>`

```
nowitt@freedsl.com wrote:
>
>With GUI tools mentioned in this topic, the programmer's
>imagination and creativity are limited by those tools.
>With PowerCOBOL the capabilities of the tool are limited only by
the probrammer's imagination and creativity which makes the tool
unlimited.

Hi:

Why not post a program which you have written which will
demonstrate conclusively that you know what you are
talking about?

Thanks

TOny Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 13)_

- **From:** nowitt@freedsl.com
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3962405B.65307E1C@freedsl.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com> <3960e0d0.81248845@207.126.101.100> <3960FEC0.7864B87D@freedsl.com> <8jt7ms$n54$1@nnrp1.deja.com>`

```


Foodman wrote:
nowitt@freedsl.com wrote:
>
>With GUI tools mentioned in this topic, the programmer's
>imagination and creativity are limited by those tools.
>With PowerCOBOL the capabilities of the tool are limited only by
the probrammer's imagination and creativity which makes the tool
unlimited.

Hi:

Why not post a program which you have written which will
demonstrate conclusively that you know what you are
talking about?

Thanks

TOny Dilworth

        Please take the time to read
        http://www.ils-international.com/goldmine/newcobol.htm
        from top to bottom.

        If not please start your reading at the paragraph titled
        "The proof of the existence of a World Class Windows programming
language"
        and study the bitmaps (picture 2 - 13)

        I am open to specific and intelligent questions no matter how
complex they
        are and providing that the answer they would require does not
infringe on
        anyone copyrights or trade secrets.

        Consulting Services are also available.  Solid references
regarding the
        services and customer satisfaction are also available.

        Thank you for your interest.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 14)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-07-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k26fj$ffe$1@news.cerf.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com> <3960e0d0.81248845@207.126.101.100> <3960FEC0.7864B87D@freedsl.com> <8jt7ms$n54$1@nnrp1.deja.com> <3962405B.65307E1C@freedsl.com>`

```
<nowitt@freedsl.com> wrote in message news:3962405B.65307E1C@freedsl.com...
>         Please take the time to read
>         http://www.ils-international.com/goldmine/newcobol.htm
…[5 more quoted lines elided]…
>         and study the bitmaps (picture 2 - 13)

In my humble opinion, your web site and bitmaps does not prove anything. It
is just another web site. What is it that should be so fantastic about
showing a bunch of screen shots in various languages?
When that is said, the designer of the application has something to learn
about use of fonts and colors in graphical applications.

Cheesle
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 12)_

- **From:** flexus@epix.net (Bob Wolfe)
- **Date:** 2000-07-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39636ceb.17891470@news.epix.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com> <3960e0d0.81248845@207.126.101.100> <3960FEC0.7864B87D@freedsl.com>`

```
nowitt@freedsl.com wrote:

>
>Thane Hubbell wrote:
…[12 more quoted lines elided]…
>        and the old character ScreenIO based on the ACCEPT/DISPLAY technology.

No wit:

CICS screen handling is typically controlled through SENDs and
RECEIVEs.  sp2 is actually based upon CALL USING technology in which
the called module is a dynamic link library and the parameters passed
in the CALL statement are used to control the DLL.

CICS screen handling is pseudo-conversational....sp2 is
conversational.  CICS screen handling is typically full screen mode
and sp2 can be full screen, field-by-field or even
character-by-character screen handling.

The sp2 DLL makes direct event driven CALLs to the Windows API.

I don't think that sp2 is quite as much like CICS as you suspect it
is.  I am not comfortable posting this message, because it appears as
self-promotion.  On the other hand, it is important to correct the
inaccuracies which you have stated above.

Everyone should enjoy the freedom to contribute to the newsgroup, but
please try to be accurate in your statements.  When you make
inaccurate statements, it actually causes you to lose credibility!

Thanks.


Bob Wolfe, flexus
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 13)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39637996.251456530@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com> <3960e0d0.81248845@207.126.101.100> <3960FEC0.7864B87D@freedsl.com> <39636ceb.17891470@news.epix.net>`

```
On Wed, 05 Jul 2000 17:47:29 GMT, flexus@epix.net (Bob Wolfe) wrote:


>I don't think that sp2 is quite as much like CICS as you suspect it
>is.  I am not comfortable posting this message, because it appears as
>self-promotion.  On the other hand, it is important to correct the
>inaccuracies which you have stated above.
>

I'm probably most guilty of making the CICS analogy.  The "simplest"
method of utilizing sp2 is SIMILAR to CICS, and SIMILAR to using the
screen section -- a full screen at a time of data comes back, and you
check why (as you would do with CICS AID keys or Function keys from a
screen section.  It's not quite an ACCURATE depiction of what is
happening inside.  I'm probably to blame for the proliferation of the
analogy, however.  


---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 11)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-07-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kJc85.123$Vp5.107208@nnrp1.sbc.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com> <3960e0d0.81248845@207.126.101.100>`

```

Thane Hubbell <thaneH@softwaresimple.com>
>
> What is obvious is that you don't understand Sp2, Screenio or Dialog
> System.  Dialog System and PowerCOBOL have the same "problem". That
is
> each utilizes an event driven programming model that requires the
> programmer to write code for each object on the screen.

Nope. In PowerCOBOL you need not write an event for ANYTHING on the
screen. You write code only for the things in which you are
interested. We've never written any code for such things as the user
resizing the window, mouse movements, or hundreds of other things.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-07-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jrlfe$c20$1@slb6.atl.mindspring.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com> <3960e0d0.81248845@207.126.101.100> <kJc85.123$Vp5.107208@nnrp1.sbc.net>`

```
"Jerry P" <jerryp@bisusa.com> wrote in message
news:kJc85.123$Vp5.107208@nnrp1.sbc.net...
>
> Thane Hubbell <thaneH@softwaresimple.com>
…[9 more quoted lines elided]…
> interested.

Jerry, I think you are missing the point.  when you write code for the things
"in which you are interested" - what PowerCOBOL (and Dialog) both do is
require you to associate that with an "event" for that thing.  This is what
the "event driven programming model" means - and PowerCOBOL does work that
way.  The event may be data entry, change of focus, or any of a NUMBER of
other "events" - but they most definitely ARE "events" in this sense of the
word.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 13)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wYm85.339$Kz2.152802@nnrp2.sbc.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com> <3960e0d0.81248845@207.126.101.100> <kJc85.123$Vp5.107208@nnrp1.sbc.net> <8jrlfe$c20$1@slb6.atl.mindspring.net>`

```

William M. Klein

> >
> > Nope. In PowerCOBOL you need not write an event for ANYTHING on
the
> > screen. You write code only for the things in which you are
> > interested.
>
> Jerry, I think you are missing the point.  when you write code for
the things
> "in which you are interested" - what PowerCOBOL (and Dialog) both do
is
> require you to associate that with an "event" for that thing.  This
is what
> the "event driven programming model" means - and PowerCOBOL does
work that
> way.  The event may be data entry, change of focus, or any of a
NUMBER of
> other "events" - but they most definitely ARE "events" in this sense
of the
> word.
>

Uh, OK. I guess I am missing the point. We can agree that with
PowerCOBOL, inter alia, if you are not interested in something on the
screen, you need not write any code for that something (say a mouse
movement or screen resize). Right?

I would think the converse would be axiomatic in any development
system: If you are interested in what the user did,  you HAVE to write
code to process the situation (say a customer name change or a check
amount).

I was quibbling about the other two cases: (1) Code for ALL possible
events (including ones in which you have no interest) and (2) NO code
for items that do excite you (say a customer name change).  The first
(in PowerCOBOL) is not true, and the second seems impossible. Although
in the latter, I admit, some data validation (dates, value ranges,
even spelling) could take place without the programmer's supervision.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 14)_

- **From:** "Paddy Coleman" <paddy.coleman@merant.com>
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jt664$1hd$1@hyperion.mfltd.co.uk>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com> <3960e0d0.81248845@207.126.101.100> <kJc85.123$Vp5.107208@nnrp1.sbc.net> <8jrlfe$c20$1@slb6.atl.mindspring.net> <wYm85.339$Kz2.152802@nnrp2.sbc.net>`

```
Folks,

Did someone say they would like a way to change the fonts in Dialog
at runtime?  If so, then I have a small utility/demo which shows how
to do it.

If you are interested then please feel free to email me directly and I
will send it to you.

All the best.

Paddy Coleman
Manager, E-Business Support, EMEA
MERANT International.

Jerry P <jerryp@bisusa.com> wrote in message
news:wYm85.339$Kz2.152802@nnrp2.sbc.net...
>
> William M. Klein
…[40 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 15)_

- **From:** "Paddy Coleman" <paddy.coleman@merant.com>
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jt6mt$1j0$1@hyperion.mfltd.co.uk>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com> <3960e0d0.81248845@207.126.101.100> <kJc85.123$Vp5.107208@nnrp1.sbc.net> <8jrlfe$c20$1@slb6.atl.mindspring.net> <wYm85.339$Kz2.152802@nnrp2.sbc.net> <8jt664$1hd$1@hyperion.mfltd.co.uk>`

```
Oh, I forgot to mention that you can also change a number of object
attributes in Dialog System at runtime now.  This is done via the
DSOBJCFG utility.  More information can be found in the Dialog
System online help.

All the best.

Paddy Coleman
Manager, E-Business Support, EMEA
MERANT International.

Paddy Coleman <paddy.coleman@merant.com> wrote in message
news:8jt664$1hd$1@hyperion.mfltd.co.uk...
> Folks,
>
…[59 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 10)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3961DC3C.C85B086D@zip.com.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608D03.698ECA6E@zip.com.au> <3960DE42.A8712695@freedsl.com>`

```
nowitt@freedsl.com wrote:
> 
> Ken Foskey wrote:
…[12 more quoted lines elided]…
>         with this master tool or even how it is structured.

I appreciate you have a different opinion.  What you call a benefit I
call a draw back, I hate code.  I like my source small and compact and
focused on the business requirements.  I have reviewed the output of
Powercobol and I believe it is bad due to the code bloat introduced.

I have seen wizard type code building happen to many other compilers,
Microsoft C, Borland C went with the wizards (similar to power cobol)
about 5 years ago.  They now encapsulate functionality as I describe. 
Microsoft does still use them to some degree however and if you look
in comp.object you will see some opinions on this, negative
unfortunately.

Cobol is some 5 years behind in the windows race.  I think that the
cobol vendors must understand what else is out there and look at the
bad design decisions that the others made and put simply not make them
again.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 8)_

- **From:** flexus@epix.net (Bob Wolfe)
- **Date:** 2000-07-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3960d382.18537475@news.epix.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com>`

```
nowitt@freedsl.com wrote:

>I challenge Dialog, SpII and ScreenIO to even come close to doing this
>(http://www.ils-international.com/goldmine/newcobol.htm) as elegantly and as
>efficiently as it has been beautifully done using PowerCOBOL from Fujitsu.
[snip]
>
>If you can't do it 100% in COBOL then may be you should consider changing
>career!

Nowitt:

I don't care to enter into a vendor debate in the newsgroup as I
mentioned before.  Everyone knows ILS sells Fujitsu COBOL.

I can say this.  Everyone has different motivations for using a
particular compiler, screen handler or some other type of tool.

I can say this.  If the program you demonstrate on your web site is
100% COBOL, then I challenge you to recompile it with any of the
following 32 bit Windows versions of:

CA-Realia II Workbench
Merant NetExpress
Acucorp's Acucobol GT
Liant's RM COBOL
Egan Systems Interactive COBOL
IBM Visual Age

>COBOL is dead, Long live COBOL
>Nowitt Oal

[snip]

Bob Wolfe, flexus
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 9)_

- **From:** Hajo Schepker <schepker@fbw.fh-wilhelmshaven.de>
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000704.12243394@Wpc8.fbw.fh-wilhelmshaven.de>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net>`

```


>>>>>>>>>>>>>>>>>> Ursprüngliche Nachricht <<<<<<<<<<<<<<<<<<

Am 03.07.00, 20:06:44, schrieb flexus@epix.net (Bob Wolfe) zum Thema Re: 
Graphical User Interface:

>snip<

> I can say this.  If the program you demonstrate on your web site is
> 100% COBOL, then I challenge you to recompile it with any of the
> following 32 bit Windows versions of:

> CA-Realia II Workbench
> Merant NetExpress
…[3 more quoted lines elided]…
> IBM Visual Age

You are a millionaire? :-))).

Mit freundlichen Grüßen
H. Schepker 
www.schepker.de
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 9)_

- **From:** nowitt@freedsl.com
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39612B21.ADAE47D9@freedsl.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net>`

```


Bob Wolfe wrote:
nowitt@freedsl.com wrote:

>I challenge Dialog, SpII and ScreenIO to even come close to doing this
>(http://www.ils-international.com/goldmine/newcobol.htm) as elegantly and as
>efficiently as it has been beautifully done using PowerCOBOL from Fujitsu.
[snip]
>
>If you can't do it 100% in COBOL then may be you should consider changing
>career!

Nowitt:

I don't care to enter into a vendor debate in the newsgroup as I
mentioned before.  Everyone knows ILS sells Fujitsu COBOL.

        That's the spirit Bob.  Healthy debates can only be beneficial to the
users by giving
        them information they would perhaps never get otherwise.  Now this does
not
        necessarily make me an ILS salesman, but I do participate actively to
COBOL Gold Mine.
        It is true that ILS sells Fujitsu COBOL - tested by COBOL Gold Mine and
found to be the best.

        But it is also true that ILS does not sell CA-Realia COBOL.  Yet I can
tell you - and the
        rest of the audience that Realia COBOL WAS THE BEST ever COBOL compiler
for DOS
        (quality & execution speed) I was top expert in that product also
1984-1990. I designed and
        wrote 4 systems totaling nearly 1 million LOC with the product.

        During the same period, I also used Character ScreenIO to the maximum of
its usability
        again ILS does not sell it but ScreenIO is till today at the TOP OF ITS
CLASS.
        I still like it.  But that is the past and today the word is PowerCOBOL.
Times are a changin'.

I can say this.  Everyone has different motivations for using a
particular compiler, screen handler or some other type of tool.

        And I agree with you. Many people drive a Cadillac, a Mercedes, a Ferrari
or a Lexus.  Others
        drive a VW or a ford Escort and are happy with what they got until one
day they have
        the opportunity to drive a Cadillac, a Mercedes, a Ferrari or a Lexus.
Then is when they
        will understand the difference and will be wishing for more "power" when
they go back to their
        VW or a ford Escort.  In this context PowerCOBOL is simply the Lexus or a
Ferrari.

        I agree also with you that some still would not want to trade their VW
for a Lexus or a Ferrari.

I can say this.  If the program you demonstrate on your web site is
100% COBOL, then I challenge you to recompile it with any of the
following 32 bit Windows versions of:

CA-Realia II Workbench
Merant NetExpress
Acucorp's Acucobol GT
Liant's RM COBOL
Egan Systems Interactive COBOL
IBM Visual Age

        Although not compiled under some of the above compilers, the program
would
        compile and execute error free if all of the above are certified ANSI
COBOL-85.

        As it is mentioned in
http://www.ils-international.com/goldmine/newcobol.htm
        a majority of the programs were developed from the mid 1980s to early
1990s using
        a different COBOL Compiler.  They have been enhanced functionality wise
and recompiled
        without compatibility issues because there was a strict discipline in
using 100%
        ANSI COBOL-85 standards in coding.  I. e.  Why use a vendor specific
function
        to convert a COBOL string from upper to lower case and vice versa.  When
changing
        compiler this surely will create a problem.  Instead use the COBOL-85
Statement
        INSPECT WS-X REPLACING 'ABC......XYZ' WITH 'abc....xyz' (and vice versa).

        Any COBOL Compiler supporting ANSI COBOL-85 should accept the above
        statement without generating an error and would give the correct result
when
        converting the string.

        All Business Logic and User Interface parameters management is handled
        100% using COBOL-85 with the exception of a main module handling all
        ASSIGN TOs and FDs. Statements getting physical file names from System
        variables in UNIX/DOS/Windows can easily be deleted and handled by JCL
        if there ever was a need to move the application to and IBM S/390 for
example.

        The main module than handles ALL System CALLs to the Operating System
such
        as GETDIR, MKDIR, GETDISKSPACE etc.  can also be relatively easy to
        modified to replace or simply eliminate System Functions that are not
needed on
        the target platform (GETDIR, MKDIR, GETDISKSPACE would not be needed
        under MVS and under UNIX can quickly be modified)

>COBOL is dead, Long live COBOL
>Nowitt Oal

[snip]

Bob Wolfe, flexus
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-07-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jraea$th1$1@slb6.atl.mindspring.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com>`

```
If you think this is "healthy debate" that users want, why don't you point to
a SINGLE user who seems to be "supporting" the tone of your posts?
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 11)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-07-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396330E3.AED13A89@cusys.edu>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <8jraea$th1$1@slb6.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> If you think this is "healthy debate" that users want, why don't you point to
> a SINGLE user who seems to be "supporting" the tone of your posts?

Or a married person.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 10)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39616AFD.EE87B84C@home.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com>`

```


nowitt@freedsl.com wrote:

I've been watching this thread, and to satisfy my curiosity, could you
please produce COBOl source code for the following window, plus any
validity checks you want to throw in :-

	............................................

	Customer # 	[       ]

	Customer Name	[			]

		<OK>		<Cancel>

	.............................................

It's not a catch question - but at least may help to illustrate your
points, without a diatribe.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 10)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396146c1.107349677@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com>`

```
On Tue, 04 Jul 2000 00:07:00 GMT, nowitt@freedsl.com wrote:


>I can say this.  If the program you demonstrate on your web site is
>100% COBOL, then I challenge you to recompile it with any of the
…[12 more quoted lines elided]…
>COBOL-85.

That's just a plainly untrue.  The Syntax used by ANY vendor to
interface with the API is non standard.  The second you use a COMP-5
field you are non-standard.  You see, these are EXTENSIONS to the
standard.  Please, please please refrain from making such statements
that are blantenly unsupportable.  You simply look silly.  You
yourself said that PowerCOBOL generated OO syntax, using INVOKE etc in
order to function.  You claimed it to be comletely OO.  There is no OO
in the 85 standard, so any of the MANY Ansi 85 compilers will NOT be
able to compile the code.  In fact, only one can.  That's no fault of
Fujitsu at this point -- there IS NO STANDARD.  

Additionally there are calls to Fujitsu specific routines that are not
part of any of the other Vendors code.  PowerCOBOL is a Fujitsu
PowerCOBOL only solution.  Even using Fujitsu (Which has an EXCELLENT
Product in their Regular and Enhanced (POWERCOBOL) offerings cannot
compile and run PowerCOBOL applications using Standard Fujitsu COBOL.
That is kind of the point behind having a proprietary solution.

One last note before I close.  I know of NO deficincies in the Fujitsu
offering.  I have found the products to be of above average quality,
generally free of bugs and performing as advertised (By Fujitsu) and
my comments in this debate should not be construed as Anti PowerCOBOL
or Anti Fujitsu in any way.  I am a VERY satisfied Fujitsu customer.
My SOLE objection to PowerCOBOL is Architectural.  I don't like having
to hadle the tedium of event driven programming if I don't have to.

Now in closing, I hope what I have pointed out above has helped you to
see just how you are coming across, how desparate you sound and how
silly the whole thing is.  If not, I'm going to stop because you are
doing a good enough job on your own.  I tried.
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-07-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jrl6f$jh3$1@slb0.atl.mindspring.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100>`

```

"Thane Hubbell" <thaneH@softwaresimple.com> wrote in message
news:396146c1.107349677@207.126.101.100...
> On Tue, 04 Jul 2000 00:07:00 GMT, nowitt@freedsl.com wrote:
>
 <SNIP>
> >
> >        Although not compiled under some of the above compilers, the
program
> >would
> >        compile and execute error free if all of the above are certified
ANSI
> >COBOL-85.
>
…[10 more quoted lines elided]…
>

Although Thane has already pointed out how silly (and conflicting) your
comments are (especially when you simultaneously claim to be ANSI'85
compliant *and* to use the INVOKE statement), I thought I would suggest that
you compile just ONE of your PowerCOBOL programs with the Fujitsu compiler
directive,

   FLAGSW(STDH)

Then post your output showing exactly how ANSI compliant (or not) you really
are.  Again, as Thane pointed out, this is not a problem (per se) with
Fujitsu, it is simply a case of where CLAIMING your code is portable across
compilers because it is ANSI compliant, is too full of holes to have any
credibility.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 11)_

- **From:** nowitt@freedsl.com
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39623CA6.6C6938B6@freedsl.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100>`

```
Hello Thane,

If you can read my lines correctly, try to "read my lips"!

Here it is below one more time in a simple form of bullets:


Thane Hubbell wrote:
On Tue, 04 Jul 2000 00:07:00 GMT, nowitt@freedsl.com wrote:

>I can say this.  If the program you demonstrate on your web site is
>100% COBOL, then I challenge you to recompile it with any of the
…[9 more quoted lines elided]…
>        Although not compiled under some of the above compilers, the program
would
>        compile and execute error free if all of the above are certified ANSI
COBOL-85.

That's just a plainly untrue.  The Syntax used by ANY vendor to
interface with the API is non standard.  The second you use a COMP-5
field you are non-standard.  You see, these are EXTENSIONS to the
standard.  Please, please please refrain from making such statements
that are blantenly unsupportable.  You simply look silly.  You
yourself said that PowerCOBOL generated OO syntax, using INVOKE etc in
order to function.  You claimed it to be comletely OO.  There is no OO
in the 85 standard, so any of the MANY Ansi 85 compilers will NOT be
able to compile the code.  In fact, only one can.  That's no fault of
Fujitsu at this point -- there IS NO STANDARD.

    O  The entire business and data validation/manipulation is written in ANSI-85
            o  The files manipulation central program (READ, WRITE, DELETE) is
               written in ANSI-85
            o  No use whatsoever of COMP-5, COMP-X , Level 78 etc..
            o  No use of INVOKE or any OO syntax
            o  No Fujitsu COBOL specific routines (i.e.. use INSPECT REPLACING
instead of
               to_upper / to_lower) functions
            o  Single program centralizing all SYSTEM CALLS (getdir, mkdir,etc).
               can be eliminated or modified easily)
            o  Reporting programs write to disk files which are redirected to
print
               spooler.
            o  All data and parameters - user and system are passed using LINKAGE
SECTION
               to the CUI or GUI interface program. (in the case of CUI character
ScreenIO
               was used in the case of GUI, VB was used years ago but could not
handle the
               job very well.  Later COBOL GUI tools were evaluated and dropped
because of
               the Screen Oriented architecture of lack of features and
flexibility.
               PowerCOBOL passed the test of the most complex GUI development in
both
               availability of Controls and ease of integration of ActiveX and
execution
               speed and commendable stability).
               "Why flip all controls of a window as if you were looking at them
in a
               mirror or move them from one place to another? you asked.  Well, go
back
               a take another look (this time do it slowly and from top to bottom)
at
               http://www.ils-international.com/goldmine/newcobol.htm and you will

               see how the same application can run in USA, France, Brazil,
Israel,
               India, Russia, Saudi Arabia or any other part of the world in the
local
               native tongue.
               That is the power of forward thinking, that is the power of
multi-use in
               a multi-community of multi-users. It is called "Efficiency" and
saves
               tons of bucks.  When NASA came up with the idea of the Space
Shuttle,
               they stopped producing their wasteful one-launch monstrous rockets
               and they did save a lot of [taxpayer] money. Of course they find a
way
               to waste some of it in other programs, but that is a different
story.

       I hope again you were able to grasp the finesse of such design.

Additionally there are calls to Fujitsu specific routines that are not
part of any of the other Vendors code.  PowerCOBOL is a Fujitsu
PowerCOBOL only solution.  Even using Fujitsu (Which has an EXCELLENT
Product in their Regular and Enhanced (POWERCOBOL) offerings cannot
compile and run PowerCOBOL applications using Standard Fujitsu COBOL.
That is kind of the point behind having a proprietary solution.

    O  The entire user Interface (CUI or GUI) is separated from the business and
data
       validation/manipulation and communicate through the LINKAGE.  In this case
       PowerCOBOL syntax is and OO COBOL are used in PowerCOBOL modules and for
the
       GUI only.  If need be this can be replaced by SPII, GUI ScreenIO or even
BMS
       on IBM mainframe.

One last note before I close.  I know of NO deficincies in the Fujitsu
offering.  I have found the products to be of above average quality,
generally free of bugs and performing as advertised (By Fujitsu) and
my comments in this debate should not be construed as Anti PowerCOBOL
or Anti Fujitsu in any way.  I am a VERY satisfied Fujitsu customer.
My SOLE objection to PowerCOBOL is Architectural.  I don't like having
to hadle the tedium of event driven programming if I don't have to.

        It is a reflection of the CICS architecture with the difference that
        in is graphical and "event driven" as opposed to character based and
        screen driven.  I gave my point of view to Mr. Foskey and Mr. Peacock.


Now in closing, I hope what I have pointed out above has helped you to
see just how you are coming across, how desparate you sound and how
silly the whole thing is.  If not, I'm going to stop because you are
doing a good enough job on your own.  I tried.

        As a teacher you should have more vision and you should be more open
        to ideas that today rules the computing world.
        "Even driven programming" is among some of the key features of the most
        popular (not necessarily the best) platform that has partially caused
        the downfall of COBOL and some other languages.
        "Even driven programming" is an integral part of Windows.
        "Even driven programming" is what made VB and C++, Delphi, etc... so
        successful.
        "Even driven programming" is an integral part of OO design.
        "Even driven programming" is an integral part of MODERN PROGRAMMING.

        The comeback of COBOL can only be a reality if in addition to teaching
COBOL
        the new architecture of "Event driven" programming tools in this case
        PowerCOBOL is well understood and appreciated.

        You said "I don't like having to hadle the tedium of event driven
        programming if I don't have to".  How can any of your COBOL student
        be taken seriously in the fierce market of GUI Client/Server and Windows
        development if he has to compete for a job against VB, C++ and other
        advanced Windows Architecture developer.  How can OO COBOL be taken
        seriously by the IT World and take back its share of the market
        if all you do is still teach old tricks and use obsolete screen based
        and "single event" programming methodologies.

        OO COBOL to succeed has to be "politically Correct" in every aspect
        not just in "syntax".

        Thanks for whatever help you believe you have provided me with.  I'll
        keep it handy for emergencies.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 12)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3962602a.179401285@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com>`

```
On Tue, 04 Jul 2000 19:33:57 GMT, nowitt@freedsl.com wrote:

>Hello Thane,

May I have the pleasure of addressing you by your name?

>
>        As a teacher you should have more vision and you should be more open
>        to ideas that today rules the computing world.

Let me take these points on one at a time.

>        "Even driven programming" is among some of the key features of the most
>        popular (not necessarily the best) platform that has partially caused
>        the downfall of COBOL and some other languages.

COBOL has suffered no real downfall, only a percieved one.

>        "Even driven programming" is an integral part of Windows.

Windows is NOT the world.  Yes it is a part of dealing with any UI and
Windows, but it's an aspect of development that need not concern the
COBOL programmer.  There are tools to eliminate the tedium.  I use the
word tedium intentionally - the tedium of dealing with USER INTERFACE
events slows down development tremendously.  I need to get to market
faster and more reliably than that.

>        "Even driven programming" is what made VB and C++, Delphi, etc... so
>        successful.

And also such AWEFUL languages (except maybe Delphi) for Business
programming.

>        "Even driven programming" is an integral part of OO design.

Messaging is.  Everything in programming is event driven actually.
(Thanks Don).  I'd like to limit our discussion to User Interface
events.

>        "Even driven programming" is an integral part of MODERN PROGRAMMING.

Let's not get on this kick about "Modern Programming".  Programming
does evolve.  New things are tried.  Some are proven to be good and
remain, and others are proven to be BAD and are discouraged.  Being on
the bleeding edge is not always wise.  Sometimes one gets cut.  To
quote Bob Wolfe - Just because it's old doesn't mean it's bad and just
because it's new doesn't mean its good.  The "Old" technology is, well
shall we say -- Proven.
>
>        The comeback of COBOL can only be a reality if in addition to teaching
…[8 more quoted lines elided]…
>        advanced Windows Architecture developer.  

Let's separate OO from the UI shall we?  They are NOT necessarily
linked.  The way my student and *I* can compete is simple.  I can
create an application FASTER, BETTER and more reliable than a VB or
C++ programmer.  Also, when I create my application, with my choice of
tools, I can deploy it without source change either on the users
desktop or via the internet.  No other suite of tools can make that
claim -- this includes remote printing.  The KEY thing is that I can
do it FASTER and it is more maintainable than the C++ or VB system.
The really neat thing is that if a NEW UI comes along, I have very
confidence that my code can be adapted to this new UI without any
source code changes.  

>How can OO COBOL be taken
>        seriously by the IT World and take back its share of the market
…[5 more quoted lines elided]…
>

Take a minute and search thru DEJA.COM for posts by me about OO.  You
will find that I am an OO COBOL proponant.  I CAN use SP2 with OO
COBOL and have an OO system.  As you stated in your argument, the
busniess logic that utilizes the OO User Interace classes does not
know, or need to know the details of the UI.  Even with SP2, I am
ultimately responding to events.  I might be responding to a button
press, or afield value change, or a loss of focus, or a gain of focus
-- the KEY difference is that I don't have to write a single line of
code to interface with the UI.  I'm free of that tedium.  I don't have
to code anything special to get the data back to my business logic.  

I also gain complete compiler independence -- because I have separated
the user interface from the business logic.  In the GUI world, oft
times the largest part of an application is the UI.  That doesn't have
to be so.  Presently I am under contract to convert a Realia COBOL
system to Fujitsu.  Thankfully the client built the system using Sp2.
The only changes I have to make are from the Realia specific syntax to
Fujitsu.  I also have to replace the Realia "DOS" calls with API or
Fujitsu calls.  I have to do NOTHING with the user interface.  

Please realize that the UI does not equal OO, and OO does not equal
the UI.
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 13)_

- **From:** Joseph J Katnic <josephk@iinet.net.au>
- **Date:** 2000-07-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39633E98.38103084@iinet.net.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <3962602a.179401285@207.126.101.100>`

```


Thane Hubbell wrote:
> 
> 
…[6 more quoted lines elided]…
> shall we say -- Proven.

Just a quick comment:
EVENT programming is neither NEW or MODERN.
I know of a few event driven applications that run at thousands of
events per second and are written in CICS/COBOL. They are of course the
online banking system.
If you look carefully enough, you will find that there is just about
nothing that is being done today that is touted as "NEW" that hasn't
already been done, although in a slightly different format.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 14)_

- **From:** "Gazaloo" <gaz@home.com>
- **Date:** 2000-07-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TFU85.30221$i5.317793@news1.frmt1.sfba.home.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <3962602a.179401285@207.126.101.100> <39633E98.38103084@iinet.net.au>`

```
"Joseph J Katnic" <josephk@iinet.net.au> wrote in message
> If you look carefully enough, you will find that there is just about
> nothing that is being done today that is touted as "NEW" that hasn't
> already been done, although in a slightly different format.

now, ain't that the truth!
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 12)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-07-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39627DD3.53048C5C@home.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com>`

```

From me to : nowittAll

I've been watching this thread, and to satisfy my curiosity, could you
please produce COBOl source code for the following window, plus any
validity checks you want to throw in :-
        ............................................
        Customer #      [       ]
        Customer Name   [                       ]

                <OK>            <Cancel>
        .............................................

It's not a catch question - but at least may help to illustrate your
points, without a diatribe.

Jimmy, Calgary AB
.......................................................................
From : NowittAll to me

Prefer to send you directly...
Don't understand your inquiry.
What are you trying to get:  how easy/difficult? the generated source
code from PowerCOBOL? What?

Try again.

Nowitt
........................................................................

OK I'll try again, in plainer English - cut the crap and in a small
example illustrate with COBOL source the arguments you are making, plus
the 'ancillary' code POWERCOBOL or whatever generates. I have no
knowledge of POWERCOBOL.

You aren't going to make money with your GOLD MINE if you are evasive
about simple questions. Anybody else have difficulty with understanding
my request, as originally worded ?

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 13)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-07-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k28i7$g02$1@news.cerf.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote in message
news:39627DD3.53048C5C@home.com...
>
> From me to : nowittAll
…[8 more quoted lines elided]…
>                 <OK>            <Cancel>

I am sorry Jimmy, I could not resist, here is the Acucobol approach, and I
ask myself; Tedious? Lot of work? Difficult to understand? I add a question
here to Mr. nowitt, can you beat this number of lines and keep the
simplicity? This is all that there is needed.

       IDENTIFICATION DIVISION.
       PROGRAM-ID. EXAMPLE.

       AUTHOR.     CHEESLE.

       DATA DIVISION.

       WORKING-STORAGE SECTION.
       77 CUST-NO   PIC 9(08).
       77 CUST-NAME PIC X(30).

       77  KEY-STATUS
                IS SPECIAL-NAMES  CRT STATUS    PIC 9(4).
                88  EXIT-BUTTON-PUSHED          VALUE 13.
                88  CANCEL-BUTTON-PUSHED        VALUE 1.

       SCREEN SECTION.

       01  SC-EXAMPLE.
           03  LABEL LINE 20 PIXELS COL 15 PIXELS "Customer #".
           03  LABEL LINE 44 PIXELS COL 15 PIXELS "Customer name".
           03  ENTRY-FIELD LINE 16 PIXELS SIZE 100 PIXELS
               COL 120 PIXELS PIC Z(8)9 USING CUST-NO 3-D NUMERIC
               MAX-TEXT 8.
           03  ENTRY-FIELD LINE 40 PIXELS SIZE 220 PIXELS
               COL 120 PIXELS PIC X(30) USING CUST-NAME
               3-D MAX-TEXT 30.
           03  PUSH-BUTTON
               LINE 80 PIXELS
               COL 120 PIXELS
               TITLE "Ok"
               DEFAULT-BUTTON
               EXCEPTION-VALUE = 13
               SELF-ACT.

           03  PUSH-BUTTON
               LINE 80 PIXELS
               COL 200 PIXELS
               TITLE "Cancel"
               CANCEL-BUTTON
               EXCEPTION-VALUE = 1
               SELF-ACT.

       PROCEDURE DIVISION.

       MAIN SECTION.
       MAIN-000.

           DISPLAY  STANDARD          GRAPHICAL WINDOW
                    LINES             9
                    SIZE              51
                    BACKGROUND-LOW
                    SYSTEM MENU.
           DISPLAY  SC-EXAMPLE.
           PERFORM  WITH              TEST AFTER UNTIL
                                      EXIT-BUTTON-PUSHED OR
                                      CANCEL-BUTTON-PUSHED
                    ACCEPT            SC-EXAMPLE
           END-PERFORM.

       MAIN-900.
       MAIN-EXIT.
           EXIT.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 14)_

- **From:** nowitt@freedsl.com
- **Date:** 2000-07-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39652742.26F07625@freedsl.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net>`

```
If we have to compare the number of lines I have to deal with,
versus the number of line coded using Acucobol approach,
one can easily see that I have 50% less code and is about
10 times simpler because I did not have to deal with LINE, COL
PIXELS.

I suggest you ask for a demo to ILS or Fujitsu.  It is hard to
explain how easy it is to work with PowerCOBOL.  You have to
try it.  Send request to sales@ils-international.com.

You will be the judge.


======  This is the COBOL program I deal with when I code. =======
======  It is created by PowerCOBOL. I only specify the    =======
======  Field names, Field Propmts and buttons using the   =======
======  GUI builder PowerFORM.  All UPPER cASE is pretty   =======
======  much generated.                                    =======

000013 SPECIAL-NAMES.
000014 REPOSITORY.
000015 .
000016 INPUT-OUTPUT    SECTION.
000017 FILE-CONTROL.
000018 DATA            DIVISION.
#LINE 23
000023 LINKAGE         SECTION.
000024 01  POW-FORM IS GLOBAL.
000025   02  POW-SELF PIC S9(9) COMP-5.
000026   02  POW-SUPER  PIC X(4).
000027   02  POW-THIS PIC S9(9) COMP-5.
000028   02  Button-OK PIC S9(9) COMP-5.
000029   02  Button-CANCEL PIC S9(9) COMP-5.
000030   02  Cust-nbr PIC S9(9) COMP-5.
000031   02  Cust-name PIC S9(9) COMP-5.
000032   02  Cust-nbr-prompt PIC S9(9) COMP-5.
000033   02  Cust-name-prompt PIC S9(9) COMP-5.
000034 01  Customer REDEFINES POW-FORM GLOBAL PIC S9(9) COMP-5.
000035 01  POW-CONTROL-ID PIC S9(9) COMP-5.
000036 01  POW-EVENT-ID   PIC S9(9) COMP-5.
000037 01  POW-OLE-PARAM  PIC X(4).
000038 01  POW-OLE-RETURN PIC X(4).
000039 PROCEDURE       DIVISION USING POW-FORM POW-CONTROL-ID POW-EVENT-ID
POW-OLE-PARAM POW-OLE-RETURN.
000040     EXIT PROGRAM.
000041 END PROGRAM     Customer.
#FILE
==================   END of my coding   ========================


======  This is the COBOL program I NEVER NEVER deal with  =======
======  or even have to look at, generated by PowerCOBOL   =======
======  But I include it so you can understand how         =======
======  PowerCOBOL inserts the CLASS names and             =======
======  OBJECT REFERENCES, compiles and links.  That's it. =======
======  Note that the proper elements are inserted where   =======
======  there is #LINE ??.  Again this really does not     =======
======  even exist for the user.  As I said before, This   =======
======  is the equivalent of the generated CICS listing    =======
======  after the pre-compile.                             =======

000001 IDENTIFICATION  DIVISION.
000002* Customer.
000003 PROGRAM-ID.     Customer.
000004 ENVIRONMENT     DIVISION.
000005 CONFIGURATION   SECTION.
000006 POW-REPOSITORY.
000007     CLASS  AMethodSetCustomer AS "TLB=C:\Fujitsu COBOL
Projects\Barcode\Customer\Release\~build.tlb,{1E8D94C3-5381-11D4-816C-0000B4532893},Fujitsu-PcobForm-4"

000008     CLASS  AMixed-DCfGWnd-Main-with-DCfGroupItem-Main AS "TLB=C:\Fujitsu
COBOL
Projects\Barcode\Customer\Release\~build.tlb,{F06C8458-672C-11D2-81F0-00A0C9613687},Fujitsu-PcobFormWnd-4"

000009     CLASS  AMixed-DCmPush-Main-with-DCfGroupItem-Main AS "TLB=C:\Fujitsu
COBOL
Projects\Barcode\Customer\Release\~build.tlb,{1E8D94C5-5381-11D4-816C-0000B4532893},Fujitsu-PcobCommandButton-4"

000010     CLASS  AMixed-DCmTextbox-Main-with-DCfGroupItem-Main AS
"TLB=C:\Fujitsu COBOL
Projects\Barcode\Customer\Release\~build.tlb,{1E8D94C7-5381-11D4-816C-0000B4532893},Fujitsu-PcobTextBox-4"

000011     CLASS  AMixed-DCmSText-Main-with-DCfGroupItem-Main AS
"TLB=C:\Fujitsu COBOL
Projects\Barcode\Customer\Release\~build.tlb,{1E8D94C9-5381-11D4-816C-0000B4532893},Fujitsu-PcobStaticText-4"

000012 .
000013 SPECIAL-NAMES.
000014 REPOSITORY.
000015 .
000016 INPUT-OUTPUT    SECTION.
000017 FILE-CONTROL.
000018 DATA            DIVISION.
000019 BASED-STORAGE   SECTION.
000020 FILE            SECTION.
000021 WORKING-STORAGE SECTION.
000022 CONSTANT        SECTION.
000023 LINKAGE         SECTION.
000024 01  POW-FORM IS GLOBAL.
000025   02  POW-SELF OBJECT REFERENCE AMethodSetCustomer.
000026   02  POW-SUPER  PIC X(4).
000027   02  POW-THIS OBJECT REFERENCE AMethodSetCustomer.
000028   02  Button-OK OBJECT REFERENCE
AMixed-DCmPush-Main-with-DCfGroupItem-Main.
000029   02  Button-CANCEL OBJECT REFERENCE
AMixed-DCmPush-Main-with-DCfGroupItem-Main.
000030   02  Cust-nbr OBJECT REFERENCE
AMixed-DCmTextbox-Main-with-DCfGroupItem-Main.
000031   02  Cust-name OBJECT REFERENCE
AMixed-DCmTextbox-Main-with-DCfGroupItem-Main.
000032   02  Cust-nbr-prompt OBJECT REFERENCE
AMixed-DCmSText-Main-with-DCfGroupItem-Main.
000033   02  Cust-name-prompt OBJECT REFERENCE
AMixed-DCmSText-Main-with-DCfGroupItem-Main.
000034 01  Customer REDEFINES POW-FORM GLOBAL OBJECT REFERENCE
AMethodSetCustomer.
000035 01  POW-CONTROL-ID PIC S9(9) COMP-5.
000036 01  POW-EVENT-ID   PIC S9(9) COMP-5.
000037 01  POW-OLE-PARAM  PIC X(4).
000038 01  POW-OLE-RETURN PIC X(4).
000039 PROCEDURE       DIVISION USING POW-FORM POW-CONTROL-ID POW-EVENT-ID
POW-OLE-PARAM POW-OLE-RETURN.
000040     EXIT PROGRAM.
000041 END PROGRAM     Customer.
==================   END generated coding   ======================





Cheesle wrote:
"James J. Gavan" <jjgavan@home.com> wrote in message
news:39627DD3.53048C5C@home.com...
>
> From me to : nowittAll
…[8 more quoted lines elided]…
>                 <OK>            <Cancel>

I am sorry Jimmy, I could not resist, here is the Acucobol approach, and I
ask myself; Tedious? Lot of work? Difficult to understand? I add a question
here to Mr. nowitt, can you beat this number of lines and keep the
simplicity? This is all that there is needed.

       IDENTIFICATION DIVISION.
       PROGRAM-ID. EXAMPLE.

       AUTHOR.     CHEESLE.

       DATA DIVISION.

       WORKING-STORAGE SECTION.
       77 CUST-NO   PIC 9(08).
       77 CUST-NAME PIC X(30).

       77  KEY-STATUS
                IS SPECIAL-NAMES  CRT STATUS    PIC 9(4).
                88  EXIT-BUTTON-PUSHED          VALUE 13.
                88  CANCEL-BUTTON-PUSHED        VALUE 1.

       SCREEN SECTION.

       01  SC-EXAMPLE.
           03  LABEL LINE 20 PIXELS COL 15 PIXELS "Customer #".
           03  LABEL LINE 44 PIXELS COL 15 PIXELS "Customer name".
           03  ENTRY-FIELD LINE 16 PIXELS SIZE 100 PIXELS
               COL 120 PIXELS PIC Z(8)9 USING CUST-NO 3-D NUMERIC
               MAX-TEXT 8.
           03  ENTRY-FIELD LINE 40 PIXELS SIZE 220 PIXELS
               COL 120 PIXELS PIC X(30) USING CUST-NAME
               3-D MAX-TEXT 30.
           03  PUSH-BUTTON
               LINE 80 PIXELS
               COL 120 PIXELS
               TITLE "Ok"
               DEFAULT-BUTTON
               EXCEPTION-VALUE = 13
               SELF-ACT.

           03  PUSH-BUTTON
               LINE 80 PIXELS
               COL 200 PIXELS
               TITLE "Cancel"
               CANCEL-BUTTON
               EXCEPTION-VALUE = 1
               SELF-ACT.

       PROCEDURE DIVISION.

       MAIN SECTION.
       MAIN-000.

           DISPLAY  STANDARD          GRAPHICAL WINDOW
                    LINES             9
                    SIZE              51
                    BACKGROUND-LOW
                    SYSTEM MENU.
           DISPLAY  SC-EXAMPLE.
           PERFORM  WITH              TEST AFTER UNTIL
                                      EXIT-BUTTON-PUSHED OR
                                      CANCEL-BUTTON-PUSHED
                    ACCEPT            SC-EXAMPLE
           END-PERFORM.

       MAIN-900.
       MAIN-EXIT.
           EXIT.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 15)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-07-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k3eq9$s4p$1@slb0.atl.mindspring.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com>`

```
For those of you who are still watching this thread and remember how "No Wit
A**'ole" had made previous comments about their code being ANSI'85
Conforming, please note that the sample code that "he deals with" includes
the following non-conforming syntax.

    Repository paragraph
         and
    Comp-5
        and
    No paragraph name in the Procedure Division
        and
    Procedure Division statement not in the B-margin

(The "generated" code that is presented uses other non-Standard syntax and it
should be particularly noted that it does NOT match the current draft of the
next COBOL Standard as far as some of its OO syntax.  OTOH, as it is "hidden"
from the programmer, I consider this less of a problem with No Wit's logic.
It does reflect, however, on the claim on the Gold Mind site about their OO
support matching the draft Standard.)

Of course when "pressed" it seems that "No Wit" seems to waiver when talking
about why he likes PowerCOBOL so much.  Sometimes he talks about separating
the "business logic" from the "User Interface" and sometimes he talks about
using the same product for both.

At least this time, he has actually posted the code - so the mis-information
in his previous posts can be pin-pointed and made clear.

Again, as made clear in many of the previous posts, the lack of ability to do
this in ANSI conforming source code is NOT a problem with Fujitsu's product;
it has to do with the state of OO COBOL and the Standard.  The original
AcuCOBOL source code also used extensions to the Standard.

My guess is that sp2 would NOT use extensions to do this - as they use
primarily "legitimate" ANSI conforming CALL statements.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 16)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-07-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k3leu$sgg$1@news.cerf.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3eq9$s4p$1@slb0.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:8k3eq9$s4p$1@slb0.atl.mindspring.net...
> The original AcuCOBOL source code also used extensions to the Standard.

True.

> My guess is that sp2 would NOT use extensions to do this - as they use
> primarily "legitimate" ANSI conforming CALL statements.

Well, I don't want to start another war, but while it is true that sp2 is
called by ANSI convensions, its form construction is way beyond. But that is
another story.

Cheesle
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 17)_

- **From:** flexus@epix.net (Bob Wolfe)
- **Date:** 2000-07-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3965d735.1777180@news.epix.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3eq9$s4p$1@slb0.atl.mindspring.net> <8k3leu$sgg$1@news.cerf.net>`

```
"Cheesle" <cheesle@online.NoSpamPlease.no> wrote:

>"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
>news:8k3eq9$s4p$1@slb0.atl.mindspring.net...
…[11 more quoted lines elided]…
>Cheesle

Cheesle:

A war?  With my buddy, Cheesle?  Perish the thought!

;-)

Actually, if I understand what you mean by "form construction" you are
absolutely correct.  While the CALL in the procedural code conforms to
the ANSI standard, the sp2 "panel definition" as well as the CALLed
dynamic link library are obviously proprietary, as is everyone's
solution at present.

When the standard is updated to include GUI syntax, I'm sure that all
the compiler and 3rd party tool vendors will move in that direction.
We'll support our existing approach in addition to generation of the
standard syntax so that existing applications are provided ongoing
support.


Bob Wolfe, flexus
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 18)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-07-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39694ECD.CEA1085C@home.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3eq9$s4p$1@slb0.atl.mindspring.net> <8k3leu$sgg$1@news.cerf.net> <3965d735.1777180@news.epix.net>`

```


Bob Wolfe wrote:
> 
> "Cheesle" <cheesle@online.NoSpamPlease.no> wrote:
…[9 more quoted lines elided]…
> >
<snip>
> 
> When the standard is updated to include GUI syntax, I'm sure that all
…[3 more quoted lines elided]…
> support.

You gotta be kidding - I don't see any reference to it in CD 1.8 and
besides which, your 'ol buddy down there in "Clap, Clap, Clap"-land is
more than happy with SP2 - and he isn't thrilled by event coding in
COBOL, even if he embraces OO <G> - he would rather you do it.

But as "TYCI24H" said elsewhere, if the Standard does eventually include
GUIs - it has to be ALL or NOTHING AT ALL - and so far as I'm concerned
it's got to do it for Windows, Unix, Linux, etc..., etc....

Jimmy
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 19)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3969ea3b.46013951@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3eq9$s4p$1@slb0.atl.mindspring.net> <8k3leu$sgg$1@news.cerf.net> <3965d735.1777180@news.epix.net> <39694ECD.CEA1085C@home.com>`

```
On Mon, 10 Jul 2000 04:30:10 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:


>You gotta be kidding - I don't see any reference to it in CD 1.8 and
>besides which, your 'ol buddy down there in "Clap, Clap, Clap"-land is
>more than happy with SP2 - and he isn't thrilled by event coding in
>COBOL, even if he embraces OO <G> - he would rather you do it.

I am truly getting dense in my old age.  What's the reference to
"Clap, Clap, Clap" land mean?
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 20)_

- **From:** flexus@epix.net (Bob Wolfe)
- **Date:** 2000-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396b3baf.9319138@news.epix.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3eq9$s4p$1@slb0.atl.mindspring.net> <8k3leu$sgg$1@news.cerf.net> <3965d735.1777180@news.epix.net> <39694ECD.CEA1085C@home.com> <3969ea3b.46013951@207.126.101.100>`

```
thaneH@softwaresimple.com (Thane Hubbell) wrote:

>On Mon, 10 Jul 2000 04:30:10 GMT, "James J. Gavan" <jjgavan@home.com>
>wrote:
…[8 more quoted lines elided]…
>"Clap, Clap, Clap" land mean?

Thane:

I suspect that he means...

The stars at night,
Are big and bright,
(clap, clap, clap, clap)
Deep in the heart of Texas,

...and subsequent verses....


Bob Wolfe, flexus
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 19)_

- **From:** flexus@epix.net (Bob Wolfe)
- **Date:** 2000-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396b399f.8791323@news.epix.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3eq9$s4p$1@slb0.atl.mindspring.net> <8k3leu$sgg$1@news.cerf.net> <3965d735.1777180@news.epix.net> <39694ECD.CEA1085C@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote:

>
>
…[24 more quoted lines elided]…
>COBOL, even if he embraces OO <G> - he would rather you do it.

Jimmy:

Firstly, I believe that it is 4 claps and then a rousing, "Deep in the
Heart of Texas!"

;-)

We won't abandon the way we currently support GUI.  We'll add support
for the future standard syntax, when it becomes a standard.

Our code generator is template driven.  Heck, we have a code generator
template which generates HTML from an sp2 panel.  So the template
should be able to be modified to produce whatever the standards folks
tell us to produce....at least I have my fingers crossed, as we Yanks
say.

>But as "TYCI24H" said elsewhere, if the Standard does eventually include
>GUIs - it has to be ALL or NOTHING AT ALL - and so far as I'm concerned
>it's got to do it for Windows, Unix, Linux, etc..., etc....

Absolutely.  That's going to be the tough part.



Bob Wolfe, flexus
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 20)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396B432D.8F076A6A@home.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3eq9$s4p$1@slb0.atl.mindspring.net> <8k3leu$sgg$1@news.cerf.net> <3965d735.1777180@news.epix.net> <39694ECD.CEA1085C@home.com> <396b399f.8791323@news.epix.net>`

```


Bob Wolfe wrote:
> 
> Jimmy:
…[4 more quoted lines elided]…
> ;-)

Can you believe it; "himself" just sent me the lyrics with music ! God,
they love their Lone Star state <G>

Jimmy
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 21)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396B4F78.11BFC1A1@cusys.edu>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3eq9$s4p$1@slb0.atl.mindspring.net> <8k3leu$sgg$1@news.cerf.net> <3965d735.1777180@news.epix.net> <39694ECD.CEA1085C@home.com> <396b399f.8791323@news.epix.net> <396B432D.8F076A6A@home.com>`

```


"James J. Gavan" wrote:
> 
> Bob Wolfe wrote:
…[11 more quoted lines elided]…
> Jimmy

"Pee Wee's Big Adventure" was worth watching, if only for when he was on
the phone and wanted to convince his caller that he was in Austin.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 22)_

- **From:** flexus@epix.net (Bob Wolfe)
- **Date:** 2000-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396c9ad8.15400548@news.epix.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3eq9$s4p$1@slb0.atl.mindspring.net> <8k3leu$sgg$1@news.cerf.net> <3965d735.1777180@news.epix.net> <39694ECD.CEA1085C@home.com> <396b399f.8791323@news.epix.net> <396B432D.8F076A6A@home.com> <396B4F78.11BFC1A1@cusys.edu>`

```
Howard Brazee <howard.brazee@cusys.edu> wrote:

>
>
…[17 more quoted lines elided]…
>the phone and wanted to convince his caller that he was in Austin.

Howard:

I thought that he was at the Alamo.




Bob Wolfe, flexus
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 23)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396CB2F2.6B9D4023@cusys.edu>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3eq9$s4p$1@slb0.atl.mindspring.net> <8k3leu$sgg$1@news.cerf.net> <3965d735.1777180@news.epix.net> <39694ECD.CEA1085C@home.com> <396b399f.8791323@news.epix.net> <396B432D.8F076A6A@home.com> <396B4F78.11BFC1A1@cusys.edu> <396c9ad8.15400548@news.epix.net>`

```


Bob Wolfe wrote:
> 
> Howard Brazee <howard.brazee@cusys.edu> wrote:
…[24 more quoted lines elided]…
> I thought that he was at the Alamo.

You're right - deep in the heart - of San Antonio!
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 16)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396648b8.65955051@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3eq9$s4p$1@slb0.atl.mindspring.net>`

```
I sent the Sp2 source to Jimmy Gavin.  If someone else wants to see
it.... Oh well, here it is:

       IDENTIFICATION DIVISION.
       PROGRAM-ID. Customer.


       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER. IBM-PC.
       OBJECT-COMPUTER. IBM-PC.

       DATA DIVISION.
       WORKING-STORAGE SECTION.

       COPY "sp2.cpy".

       COPY "Customer.cpy".

       PROCEDURE DIVISION.
       MAINLINE.
      ******************
      * MAINLINE LOGIC *
      ******************
           PERFORM PROC-OPEN-FILE 
           MOVE LOW-VALUES TO Customer-DATA
           MOVE "Customer" TO Customer-NEXT-PANEL
           MOVE "y" TO Customer-NEW-WINDOW
           MOVE LOW-VALUES TO Customer-FIELDS
           MOVE LOW-VALUES TO Customer-COLRS
           MOVE LOW-VALUES TO Customer-TYPES
           PERFORM PROC-CON-Customer 
           PERFORM PROC-CLOSE-WINDOW 
           PERFORM PROC-CLOSE-FILE 
           PERFORM PROC-END-SESSION 
           STOP RUN
           .

       PROC-OPEN-FILE.
      *****************
      * OPEN SP2 FILE *
      *****************
           MOVE LOW-VALUES TO SP2-FI-DATA
           MOVE "jimmy.pan" TO SP2-FI-NAME
           CALL "SP2" USING SP2-OPEN-FILE SP2-FILE-DEF
           .

       PROC-CON-Customer.
      ******************
      * CONVERSE PANEL *
      ******************
           CALL "SP2" USING SP2-CONVERSE-PANEL Customer-CONVERSE-DATA 
           MOVE LOW-VALUE TO Customer-NEW-WINDOW
           .

       PROC-CLOSE-WINDOW.
      ************************
      * CLOSE CURRENT WINDOW *
      ************************
           CALL "SP2" USING SP2-CLOSE-WINDOW SP2-NULL-PARM
           .

       PROC-CLOSE-FILE.
      **********************
      * CLOSE CURRENT FILE *
      **********************
           CALL "SP2" USING SP2-CLOSE-FILE SP2-NULL-PARM
           .

       PROC-END-SESSION.
      *******************
      * END SP2 SESSION *
      *******************
           CALL "SP2" USING SP2-END-SESSION SP2-NULL-PARM
           .



On Thu, 6 Jul 2000 21:22:44 -0500, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

>For those of you who are still watching this thread and remember how "No Wit
>A**'ole" had made previous comments about their code being ANSI'85
…[266 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 16)_

- **From:** nowitt@freedsl.com
- **Date:** 2000-07-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396757A0.9EBF110A@freedsl.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3eq9$s4p$1@slb0.atl.mindspring.net>`

```
Mr. Klein,

It seems to me that either you do not give attention to what I post OR you have
problem remembering what I post.  Below is again what I have stated regarding the

design of the system described in
http://www.ils-international.com/goldmine/newcobol.htm.

Please take the time to review ALL my posting and show me where I have stated
that PowerCOBOL uses ANSI-85 COBOL.

The code I posted was to take up Cheesle's challenge to "beat this number of
lines
and keep the simplicity? This is all that there is needed".

Here I repeat it AGAIN"
        The code posted what to take up Cheesle's challenge to "beat this
        number of lines and keep the simplicity? This is all that there
        is needed"..

1- It seems to me that 50% of anything is SMALLER than anything that is 100% of
the same thing.

2- The simplicity of PowerCOBOL in the example provided is obvious for there
are NO WS of PROCEDURE DIVISION statements dealing with the window definition
and its Controls.

There has never been a mis-information as you claim.  As to PowerCOBOL it is
the "closest to the current OO COBOL Standards".  I believe if there is anyone
to criticize about the confusing OO Standards and the lack of standardization
among the COBOL vendors, it is not such or such vendor but the OO COBOL
Standards Committee itself for dragging "their feet" to finalize the draft.

When considering that OO COBOL was born more or less in 1992-93 and the
FIRST OO COBOL Compiler was produced and running on a MAINFRAME by Hitachi
in 1994!!  ["Made in Japan" - that's right - Not "Made in USA"], here we are
not too far from 2001 and and still we have crazy speculations about OO COBOL
final draft by 2003-2005 and the first Standards compliant Compiler by
2006-2008!!!

No wonder OO COBOL is a favorite JOKE among "Java/C++ and company"!

Here are a few things to think about:
    -If a War is lost,
     it is not the soldiers or platoon captain's fault,
     but the War Room's polished 5-star Generals
     who don't have to "swim" in their blood, sweat & tears.

    -If a Corporation goes belly up,
     it is not the employees or their manager's fault,
     but the Conference Rooms polished Executive VPs and CEO
     who take decisions based on the technology "du Jour".

As someone famous said in connection to the British loosing the war to the
Germans in WWII "There are no bad soldiers, there are only bad Generals"

It seems to me that OO COBOL is in urgent need of "Good Generals" or the
OO War between Java/C++ and COBOL will be lost.  We can finally say what
the next standards of COBOL will be called "RIP COBOL".

Nowitt Oal
----------------------------------------------------------------

Here is what I have stated time and again:

    O  The entire business and data validation/manipulation is written in ANSI-85

       o  The files manipulation central program (READ, WRITE, DELETE) is
          written in ANSI-85
       o  No use whatsoever of COMP-5, COMP-X , Level 78 etc..
       o  No use of INVOKE or any OO syntax
       o  No Fujitsu COBOL specific routines (i.e.. use INSPECT REPLACING
          instead of to_upper / to_lower) functions
       o  Single program centralizing all SYSTEM CALLS (getdir, mkdir,etc).
          can be eliminated or modified easily)
       o  Reporting programs write to disk files which are redirected to
          print spooler.
       o  All data and parameters - user and system are passed using LINKAGE
SECTION
          to the CUI or GUI interface program. (in the case of CUI character
ScreenIO
          was used in the case of GUI, VB was used years ago but could not handle

          the job very well.  Later COBOL GUI tools were evaluated and dropped
          because of the Screen Oriented architecture of lack of features and
          flexibility.  PowerCOBOL passed the test of the most complex GUI
          development in both availability of Controls and ease of integration of

          ActiveX and execution speed and commendable stability.

    O  The entire user Interface (CUI or GUI) is separated from the business
       and data validation/manipulation and communicate through the LINKAGE.
       In this case PowerCOBOL syntax is and OO COBOL are used in PowerCOBOL
       modules and for the GUI only.  If need be this can be replaced by SPII,
       GUI ScreenIO or even BMS on IBM mainframe.

THOSE ARE THE FACTS AND "I STICK TO THEM"!

=================================================


"William M. Klein" wrote:

> For those of you who are still watching this thread and remember how "No Wit
> A**'ole" had made previous comments about their code being ANSI'85
…[264 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 17)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-07-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k82re$hd0$1@slb6.atl.mindspring.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3eq9$s4p$1@slb0.atl.mindspring.net> <396757A0.9EBF110A@freedsl.com>`

```
<nowitt@freedsl.com> wrote in message news:396757A0.9EBF110A@freedsl.com...
> Mr. Klein,
>
> It seems to me that either you do not give attention to what I post OR you
have
> problem remembering what I post.  Below is again what I have stated
regarding the
   <snip>
> Please take the time to review ALL my posting and show me where I have
stated
> that PowerCOBOL uses ANSI-85 COBOL.
>

And I quote from Mr A**Hole's post dates, July 3rd.

"<Bob Wolfe> I can say this.  If the program you demonstrate on your web site
is
100% COBOL, then I challenge you to recompile it with any of the
following 32 bit Windows versions of:

CA-Realia II Workbench
Merant NetExpress
Acucorp's Acucobol GT
Liant's RM COBOL
Egan Systems Interactive COBOL
IBM Visual Age

        <No Witt, A**Hole> Although not compiled under some of the above
compilers, the program would compile and execute error free if all of the
above are certified ANSI
COBOL-85. ... They have been enhanced functionality wise and recompiled
without compatibility issues because there was a strict discipline in using
100% ANSI COBOL-85 standards in coding.  "

  and then you stated

"All Business Logic and User Interface parameters management is handled 100%
using COBOL-85 with the exception of a main module handling all ASSIGN TOs
and FDs. Statements getting physical file names from System variables in
UNIX/DOS/Windows can easily be deleted and handled by JCL if there ever was a
need to move the application to and IBM S/390 for example."


You never DID show us the code that you were talking about, but from the rest
of your post you SEEMED to be talking about the PowerCOBOL code (which you
were advocating). If you are actually NOW saying that this "ideal"
application isn't written using the product that you are advocating, that
adds some more interesting information to your conflicting comments.

>
> There has never been a mis-information as you claim.  As to PowerCOBOL it
is
> the "closest to the current OO COBOL Standards".  I believe if there is
anyone
> to criticize about the confusing OO Standards and the lack of
standardization
> among the COBOL vendors, it is not such or such vendor but the OO COBOL
> Standards Committee itself for dragging "their feet" to finalize the draft.
>

It is http://www.ils-international.com/goldmine/newcobol.htm which rather
EXPLICITLY (and incorrectly) states,

"Support COBOL standards for COBOL-68, COBOL-74, COBOL-85, OO COBOL, X/OPEN
COBOL"

I won't argue with you about the statement that it is the delay on getting an
OO Standard out that DOES cause the problems.  I will, however, argue that
you should make an INCORRECT (and unsubstantiated) claim about PowerCOBOL
supporting standard ... OO COBOL - as defined in the current draft.  You
might also want to contact Fujitsu about their "current and continued"
involvement with the J4 Standards committee.  I think you will be "amused" by
the answer that you get.  (Their current representative has ALMOST nothing to
do with the Fujitsu COBOL development team.  Unfortunately, he is now
seriously ill and it is doubtful that they will have ANY continued
involvement with J4.)
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 17)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-07-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3967D07A.2E4C33B1@zip.com.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3eq9$s4p$1@slb0.atl.mindspring.net> <396757A0.9EBF110A@freedsl.com>`

```
nowitt@freedsl.com wrote:
> 
> No wonder OO COBOL is a favorite JOKE among "Java/C++ and company"!

It is only a joke due to the fact that clue less and uneducated people
discuss it with them.  OO cobol is grounded (for good or bad) fairly
squarely on Java concepts, they are therefore laughing at themselves.

OO cobol is a reality,  there are some significant problems with the
specification, once the standards committee realize it is about
programmers and not vendors I expect to see some real improvements.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 17)_

- **From:** "David W. Furin" <dfurin@larich.com>
- **Date:** 2000-07-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3969D7F2.19D77756@larich.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3eq9$s4p$1@slb0.atl.mindspring.net> <396757A0.9EBF110A@freedsl.com>`

```
nowitt@freedsl.com wrote:
> 
> As someone famous said in connection to the British loosing the war to the
> Germans in WWII "There are no bad soldiers, there are only bad Generals"
> 

The British lost?  Gosh, I didn't know that...   :)
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 15)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-07-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k3laq$sge$1@news.cerf.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com>`

```
<nowitt@freedsl.com> wrote in message news:39652742.26F07625@freedsl.com...
> If we have to compare the number of lines I have to deal with,
> versus the number of line coded using Acucobol approach,
> one can easily see that I have 50% less code and is about
> 10 times simpler because I did not have to deal with LINE, COL
> PIXELS.

Good, good, we got some code. And if all you gotta do now is to do ccbl
mysource.cbl and thereafter it executes with no more files, it is good. No
doubt it is smaller, indeed using a screen designer is simpler. It might
surprise you, but Acucobol also has a screen designer, so the screen section
may be done wysiwyg for those who prefer that. So... 10 times simpler?
Actually, the entire source could be made automatically using a screen
designer. No way it is simpler.

You say that you do not have to deal with positioning. How do you specify
location then?
You may have it in a separate form file? If so, my guess is that your number
of lines increases rapidly, because the code you have shown has no way of
locating stuff. Are you hiding something?

When it comes to readability, you can't deny which is.

Cheesle.

Btw: Acucobol may also use ActiveX's. Which introduces another problem, you
must install them on the receiving computer. The sample application I made
does not need any ActiveX's.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 16)_

- **From:** nowitt@freedsl.com
- **Date:** 2000-07-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39675F09.EA08060@freedsl.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net>`

```
Cheesle wrote:
>><nowitt@freedsl.com> wrote in message news:39652742.26F07625@freedsl.com...
>> If we have to compare the number of lines I have to deal with,
…[3 more quoted lines elided]…
>> PIXELS.

>Good, good, we got some code. And if all you gotta do now is to do ccbl
>mysource.cbl and thereafter it executes with no more files, it is good. No
…[4 more quoted lines elided]…
>designer. No way it is simpler.

    I am not saying that it is simpler "because the screen section
    may be done wysiwyg"
    but rather because "there is no Screen Section in WS or PROCEDURE
    DIVISION statements of ACCEPT/DISPLAY as it is done in the Acucobol
    example.  There is no window/controls related code that is shown
    in the PowerCOBOL sample.  That is what I call 10 times simpler.

>You say that you do not have to deal with positioning. How do you specify
>location then?

    It is taken from the WYSIWYG tool file and inserted in the code when
    it is generated by PowerCOBOL
    Please refer to the PowerCOBOL sample I posted.

>You may have it in a separate form file? If so, my guess is that your number
>of lines increases rapidly, because the code you have shown has no way of
>locating stuff. Are you hiding something?

    No.  It is not in a "separate form file".  Nothing is hiding.
    What you fail to understand is how smart the PowerCOBOL design is.
    It generates all that is needed in a pre-compile (is what keeps the
    code maintained by the programmer very small) and what makes the
    executable so fast because all GUI support is linked in the COBOL
    program.

>When it comes to readability, you can't deny which is.

    30 lines (WORKING-STORAGE/SCREEN SECTION) in your example
            vs. 15 lines (LINKAGE SECTION) in PowerCOBOL

    16 lines in PROCEDURE in your example
            vs. 1 line (EXIT PROGRAM) in PowerCOBOL

    You are right nobody "can't deny which is"!

>Cheesle.

>Btw: Acucobol may also use ActiveX's. Which introduces another problem, you
>must install them on the receiving computer. The sample application I made
>does not need any ActiveX's.

    Neither does the PowerCOBOL one!
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 17)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-07-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sdN95.432$HD.138159@dfiatx1-snr1.gtei.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com>`

```
<nowitt@freedsl.com> wrote in message news:39675F09.EA08060@freedsl.com...
>
>     30 lines (WORKING-STORAGE/SCREEN SECTION) in your example
…[6 more quoted lines elided]…
>


Hmm. You must be one of those guys who really believes size matters.

MCM
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 18)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-07-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kbdg5$ngb$1@news.cerf.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <sdN95.432$HD.138159@dfiatx1-snr1.gtei.net>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:sdN95.432$HD.138159@dfiatx1-snr1.gtei.net...
> Hmm. You must be one of those guys who really believes size matters.

Definitely the best answer I have read for a while!

Cheesle
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 17)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-07-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kbde4$ng8$1@news.cerf.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com>`

```
<nowitt@freedsl.com> wrote in message news:39675F09.EA08060@freedsl.com...
> >You may have it in a separate form file? If so, my guess is that your
number
> >of lines increases rapidly, because the code you have shown has no way of
> >locating stuff. Are you hiding something?
…[6 more quoted lines elided]…
>     program.

It is apparently so smart then, that you can't see where your fields end up.
Okay, the screen designer has made a binary object to link with the final
executable, and all position information is buried in this binary file. Have
I understood you correct?
If yes, or, btw, anyway, this is definitely nothing for me. I have been
working as a developer in almost 20 years now, and no matter whether I was
working with Modula 2, Pascal, C/C++, Cobol or Delphi, the worst thing I
know is hidden stuff, and particularly when it comes to basic stuff like
positioning of an item. But of course, it is a matter of taste.

Nevertheless, I could extract the screen section part into a copybook, and
the code would shrink correspondingly. You cannot claim I cannot do that,
because you do it yourself.

>>Btw: Acucobol may also use ActiveX's. Which introduces another problem,
you
>>must install them on the receiving computer. The sample application I made
>>does not need any ActiveX's.

>    Neither does the PowerCOBOL one!

Well, to me the following is clearly references to ActiveX objects.

000007     CLASS  AMethodSetCustomer AS "TLB=C:\Fujitsu COBOL
Projects\Barcode\Customer\Release\~build.tlb,{1E8D94C3-5381-11D4-816C-0000B4
532893},Fujitsu-PcobForm-4"

000008     CLASS  AMixed-DCfGWnd-Main-with-DCfGroupItem-Main AS
"TLB=C:\Fujitsu
COBOL
Projects\Barcode\Customer\Release\~build.tlb,{F06C8458-672C-11D2-81F0-00A0C9
613687},Fujitsu-PcobFormWnd-4"

> >When it comes to readability, you can't deny which is.
>
…[6 more quoted lines elided]…
>     You are right nobody "can't deny which is"!

You don't really get it, do you? That is probably why you have such a
problem getting your message through here in this ng. You appear to use
different glasses than others. Readability does not happen about code size,
but how easy the code is to be understood, particularly for people without
insight.

Anyway, I wish you good luck selling the product, I suspect you will need
it.

Cheesle
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 18)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3969eab4.46135220@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net>`

```
On Sun, 9 Jul 2000 19:46:37 -0700, "Cheesle"
<cheesle@online.NoSpamPlease.no> wrote:


>
>Anyway, I wish you good luck selling the product, I suspect you will need
>it.
>

The sad reality is that this guy is doing more harm than good to his
cause.  He's trying to sell a quality product -- one that oft times
sells itself -- but his attitude and sales pitch turns off the
prospective customer.

BTW: of all the approaches to the "customer entry" yours was the most
elegent looking code wise.  I would endorse this approach if it was
not an AcuCOBOL only solution, and if I didn't have a religious
objection to standardizing ANY user interface into the language.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 19)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-07-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kdm9f$m19$1@news.cerf.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100>`

```
"Thane Hubbell" <thaneH@softwaresimple.com> wrote in message
news:3969eab4.46135220@207.126.101.100...
> BTW: of all the approaches to the "customer entry" yours was the most
> elegent looking code wise.  I would endorse this approach if it was
> not an AcuCOBOL only solution, and if I didn't have a religious
> objection to standardizing ANY user interface into the language.

I second you that a standard is preferable. And I won't say that the
Acucobol approach is the ultimate. On the other side, we should not end up
with a solution that requires complex OO constructions to develop gui in
Cobol, that is what I am afraid of.

I realize that there is a contradiction in your text above and that my
answer in that context may sound stupid. Considering GUI, I agree with you
that a standardization of user interface is a very difficult if not hopeless
task. That is the price to pay for such a portable language as Cobol is. On
the other side, does Cobol have a future if not doing so?

Generally speaking, I don't understand why the OO Cobol approach is using
the C++/Java approach, while Smalltalk is way closer to Cobol in terms of
English language look a like. Is there anyone out there that can tell me
this?

Cheesle
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 20)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396b4bde.56869679@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net>`

```
On Mon, 10 Jul 2000 16:29:48 -0700, "Cheesle"
<cheesle@online.NoSpamPlease.no> wrote:


>I realize that there is a contradiction in your text above and that my
>answer in that context may sound stupid. Considering GUI, I agree with you
…[3 more quoted lines elided]…
>

C doesn't have a Standard UI
C++ doesn't have a Standard UI
JAVA does - with SWING, but it's still an exension (unless I am
misinformed I think Sun just released GUI specifications however).

So to be successful I don't think COBOL needs a standard UI.  
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 21)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396B6CE6.D927B7FF@home.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396b4bde.56869679@207.126.101.100>`

```


Thane Hubbell wrote:
> 
> On Mon, 10 Jul 2000 16:29:48 -0700, "Cheesle"
…[14 more quoted lines elided]…
> So to be successful I don't think COBOL needs a standard UI.

I respect your point of view, but as you know I would opt for a standard
UI, which is no small accomplishment, and as an independent module is a
VAST TOPIC. This would definitely need the services of OO - comes back
to PORTABILITY of source code. The compiler tools could be different to
generate a user screen/window - but they should all generate STANDARD
COBOL code and make the same access to Windows/Linux/Unix or whatever...

... But we can discuss this one in more detail elsewhere. I know I'm in
the minority.

Jimmy
]
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 21)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kfv8s$gah$1@news.cerf.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396b4bde.56869679@207.126.101.100>`

```
"Thane Hubbell" <thaneH@softwaresimple.com> wrote in message
news:396b4bde.56869679@207.126.101.100...
> On Mon, 10 Jul 2000 16:29:48 -0700, "Cheesle"
> <cheesle@online.NoSpamPlease.no> wrote:
…[5 more quoted lines elided]…
> So to be successful I don't think COBOL needs a standard UI.

That is an interesting perspective. You consider the ui layer to be a
separate library, of which, technically speaking, you are correct.

Interesting consideration. I got to chew on this.

Cheesle
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 21)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396BA4F6.8C8A7BA@zip.com.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396b4bde.56869679@207.126.101.100>`

```
Thane Hubbell wrote:
> 
> 
…[4 more quoted lines elided]…
> misinformed I think Sun just released GUI specifications however).

Swing is not well respected in the industry,  it has been superseded
by other tools now.  It is still heavily used however.

> So to be successful I don't think COBOL needs a standard UI.

100% agree...

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 20)_

- **From:** Joseph J Katnic <josephk@iinet.net.au>
- **Date:** 2000-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396B1C86.F2EAE170@iinet.net.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net>`

```


Cheesle wrote:
> 
> I second you that a standard is preferable. And I won't say that the
> Acucobol approach is the ultimate. On the other side, we should not end up
> with a solution that requires complex OO constructions to develop gui in
> Cobol, that is what I am afraid of.

<snip>
 
> Generally speaking, I don't understand why the OO Cobol approach is using
> the C++/Java approach, while Smalltalk is way closer to Cobol in terms of
> English language look a like. Is there anyone out there that can tell me
> this?
> 
The general reason for using OO is that the OS can provide a default set
of behaviors (read methods) to built and interact with a screen. Then
the User merely has to override these default behaviors with a set that
are tailored to producing the desired result on the screen.

UNFORTUNATELY, to provide for every developers solution, a rather RICH
set of default behaviors have been supplied. Even worse is that the
level of detail for these behaviors is quite extensive (merely because
some developer may want to change the way the OS draws a border for example).

This unfortunate circumstance (started by Xerox, publicized by Apple and
brought to it's ultimate futility by Microsoft) has led to the creation
of huge programs whose only job is to lay some text onto a screen.

Anyone who has seen and used ISPF on the IBM mainframe has seen a
completely different way of presenting data. Where the formatting and
presentation of the data on a screen is not at all related to the
program. That is the program merely presents the data to the IPSF dialog
manager and the dialog manager draws the screen based on a scripting language.

Now where have we heard of a similar scheme.
OH I KNOW - HTML.

YUP, Your good old Web server is a prime example of this type of thing.
There is only one problem, the current HTML does not understand the
difference between text constants and variables in programs.
So the program is reduced to creating the ENTIRE HTML document, even if
it is only going to present one variable on the screen.

In my view adding variables to the HTML standard would allow a program
to export the contents of the variables to the Web Server and then ask
the Web server to present a particular rebuilt HTML document to the
user, substituting the variables as it goes.

A further advantage of this method is that the entire interaction is
transactional. The program does not care if the user moved the mouse or
re-sized the window or any other mind numbing thing. The program is
presented with the data only after the user has finished with the window
and has decided to commit the update. AH but what if you want those
other interactions - Well then write a JAVA program to customize the
browsers behavior.

My take on the GUI standard for COBOL.
1. It should consist of commands to the Web Server to maintain
variables. It should be possible to create, destroy, get and set
variables in a pool belonging to the browser request instance. It should
be possible to tell the server to link page variable pool instances
together to form a session pool. The program also needs to be able to
tell the Server to destroy instance or session pools.

2, It should consist of commands to tell the server to display a page.
This page could be from a predefined set of pages or dynamically build
by the program. Dynamic building should not be the first choice.

I'm not certain, but I think that a lot of the above could be done via XML.

So now all we need is a Web SERVER, but for local only display a runtime
could translate the commands and directly build the pages/windows like a
combination server/browser.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 21)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396BA434.504E0F1C@zip.com.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au>`

```
Joseph J Katnic wrote:
> 
> Cheesle wrote:
…[16 more quoted lines elided]…
> are tailored to producing the desired result on the screen.

...  snip  a whole heap of good stuff ...

This is a fairly limited view of OO, it is definitely not only for
GUI.  As a matter of fact I don't use it for GUI, I use it for
reusable business objects.  Take a look at refactoring by Fowler.  He
describes how to change code to more OO from less OO, in the process
he shows how OO really works a light bulb experience (for me anyway).

You make some excellent points on GUI presentation.  The problem is
when you actually need the configurability of the windows solution.  
As you describe you can encapsulate the power without too much
overhead for the programmer.

In answer Cheesle, Java and Small talk are not that far away.  The
best extra in Java is interfaces,  this has been faithfully reproduced
in OO cobol.  This is a heavily used pattern by my resident OO guru.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 22)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kgv0j$17t$1@news.cerf.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au>`

```
"Ken Foskey" <waratah@zip.com.au> wrote in message
news:396BA434.504E0F1C@zip.com.au...
> Joseph J Katnic wrote:
> > The general reason for using OO is that the OS can provide a default set
> > of behaviors (read methods) to built and interact with a screen. Then
> > the User merely has to override these default behaviors with a set that
> > are tailored to producing the desired result on the screen.

There is certainly something weird going on. I haven't seen this. However, I
think you misunderstood me quite a bit. I OO very well, what I question is
why OO Cobol has chosen the C++/Java approach rather than the Smalltalk
approach. In my opinion would Cobol benefit more from a Smalltalk approach
than C++/Java.

> This is a fairly limited view of OO, it is definitely not only for
> GUI.

Correct, this is a wide misunderstanding. OO and GUI may be true, but both
have totally independent lifes, although it seems quite popular to "merry"
them.

> In answer Cheesle, Java and Small talk are not that far away.

Hm, I disagree. from the little I remember of Smalltalk it is different, a
major thing I can think of that they share is that both demand OO
programming, and are not hybrids like C++, Delphi and OO Cobol. As far as I
know, Java is built upon experiences from C++, Delphi and VB, and at the
same time trying to be true to the original OO idea. Thus trying to make the
ideal world.

Smalltalk on the other side, has a language construction that is compliant
to the great master of OO languages, namely Simula. Both these has in common
that they are totally different in their language construction from the
classic procedural languages. Still, if my memory has not betrayed me.

> best extra in Java is interfaces,  this has been faithfully reproduced
> in OO cobol.  This is a heavily used pattern by my resident OO guru.

It would be a wast overkill of me to claim expertise for Smalltalk and OO
Cobol, as a matter of fact, most of what I have seen of OO Cobol has been
posted in this ng. Smalltalk, I haven't seen since I was a student 10 years
ago. So, I will surrender unless you should consider otherwise of course :-)

Cheesle
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 23)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396C6D9A.D16FC1DC@cusys.edu>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net>`

```
Cheesle wrote:
> 
> There is certainly something weird going on. I haven't seen this. However, I
…[3 more quoted lines elided]…
> than C++/Java.

It's the way people and businesses make choices.

Java is the current, growing, vibrant choice.  It gets the press and the
praise.  We want that kind of success.

Smalltalk is an older choice, which does not get the press and praise. 
It's bandwagon is small.  Why should we hook our careers to it?

Notice that I never mentioned which is best for the application, only
which is perceived as best for the decision makers' careers.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 24)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ki0bu$fhm$1@news.cerf.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C6D9A.D16FC1DC@cusys.edu>`

```
"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:396C6D9A.D16FC1DC@cusys.edu...
> It's the way people and businesses make choices.
>
…[7 more quoted lines elided]…
> which is perceived as best for the decision makers' careers.

That is a vast sacrifice, letting media decide the technical course. Well, I
suppose it is inevitable.
As you may understand of my statement, I am not so sure Java is the real
thing. I like the language, after all, with my knowledge of Delphi lots of
things are familiar, but for some reason, I just don't get the 'kick'. I
have used to say that time will prove if I am wrong, it has passed some time
now and I still can't see that Java has got the market penetration it
requires, or has it?

Cheesle
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 24)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396DAAB6.6F0B00F9@zip.com.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C6D9A.D16FC1DC@cusys.edu>`

```
Howard Brazee wrote:
> 
> Cheesle wrote:
…[16 more quoted lines elided]…
> which is perceived as best for the decision makers' careers.

The is a huge demand for small talk developers.  XP is based around
small talk and this is a thriving methodology with a lot of people
talking.  This is not the stuff of magazine articles however.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 23)_

- **From:** Joseph J Katnic <josephk@iinet.net.au>
- **Date:** 2000-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396C72D4.2BBB6048@iinet.net.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net>`

```


Cheesle wrote:
> 
> Hm, I disagree. from the little I remember of Smalltalk it is different, a
…[5 more quoted lines elided]…
> 
Smalltalk is MAJOR league different from any other OO language out there.

Firstly, you can only write OO in Smalltalk, it is not possible to write
any other way.

Secondly, absolutely everything is Smalltalk is an OBJECT.

How bizarre this is can only be appreciated when you start to program. E.G.

	aNumber := 1 + anOtherNumber

is interpreted as Invoke method "+" on object "1" with parameter
"anOtherNumber" and set aNumber to point to the resulting object.

As far as I know, this would be incompatible with the COBOL syntax
standards and their current interpretation.

The advantage of Smalltalk is that you can create partial solutions that
solve the current problems and leave the filling out of the total
solution for a later date, when it maybe required.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 24)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ki0ok$fig$1@news.cerf.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au>`

```
"Joseph J Katnic" <josephk@iinet.net.au> wrote in message
news:396C72D4.2BBB6048@iinet.net.au...
> Smalltalk is MAJOR league different from any other OO language out there.

Great! Someone that agrees with me. So my memory wasn't totally out then :-)

> Secondly, absolutely everything is Smalltalk is an OBJECT.

Yes, that was what I considered to be the major difference from C++/Delphi,
but Java, how about that, does that also consider everything as an object?

> aNumber := 1 + anOtherNumber
> As far as I know, this would be incompatible with the COBOL syntax
> standards and their current interpretation.

This was actually what I thought of would benefit Cobol, after all,
considering its goal of being as native English as possible, and stretching
the understanding of OO as far as possible to the means of a human being,
what would be more OO than this:

Add 1 to anOtherNumber giving ANumber.

Rather than (Delphi):
    ANumber.Value := anOtherNumber.Add(1);

Anyone out there that would show me how the above would be accomplished
using OO Cobol (you don't have to show the entire object construction, only
the statement assuming the methods exist).

Cheesle
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 25)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kiqlh$ggg$1@slb7.atl.mindspring.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net>`

```
"Cheesle" <cheesle@online.NoSpamPlease.no> wrote in message
   <snip>
>
> This was actually what I thought of would benefit Cobol, after all,
…[12 more quoted lines elided]…
>


If I understand your question, then I would code

Each of these would be valid (assuming that "anOtherNumber" is the object -
and "addNum" is the method)

Invoke anOtherNumber addNum
             Using 1
             Returning aNumber_Value   *> can't use a "period" in a name.

Compute aNumber_Value = anOtherNumber :: addNum  (1)

Move anOtherNumber :: addNum (1) to aNumber_Value


   ***

Does this answer your question?
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 26)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kksv2$kiq$1@news.cerf.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <8kiqlh$ggg$1@slb7.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:8kiqlh$ggg$1@slb7.atl.mindspring.net...
> Does this answer your question?

Yepp. Thanks.

Cheesle
```

###### ↳ ↳ ↳ OO question (was Re: Graphical User Interface)

_(reply depth: 26)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396D44E5.B2534FD1@worldnet.att.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <8kiqlh$ggg$1@slb7.atl.mindspring.net>`

```
"William M. Klein" wrote:
> 
> "Cheesle" <cheesle@online.NoSpamPlease.no> wrote in message
…[36 more quoted lines elided]…
>     wmklein <at> ix dot netcom dot com

No, I truly don't understand this stuff.  Maybe someone can explain it
to me.

I don't see any difference in the intention between all these examples,
although I suspect some of them may not actually generate the same
intermediate code.  But to me it makes far more sense to code "ADD 1,
anOtherNumber GIVING ANumber".  At least this construction reads like
English and is easier to understand.

This whole thing makes me want to ask a lot more questions.

If I want to create a new number by adding 1 and another number, what's
the advantage to doing it in OO instead of plain arithmetic?  Wouldn't
the self-documenting expression be better?

What does "::" mean?

I've read many articles on OOP and I am still confused about what an
"object" is.  One article defined "object" in an intentionally
provocative way as a "lexically scoped subroutine with multiple entry
points and persistent state".  As near as I can tell, an "object" is
closest to what I would normally call a "program", but I don't think
that's quite what is really meant.  So my real question is, what is an
"object" in OOP?

The same article stated that the element of re-use in OOP is a class
hierarchy.  If I'm having this much trouble understanding what is meant
by "object", how am I going to be able to re-use a class hierarchy
without a definition of "class"?

Help me out.  I'm lost.
```

###### ↳ ↳ ↳ Re: OO question (was Re: Graphical User Interface)

_(reply depth: 27)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kl1ho$evt$1@news.igs.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <8kiqlh$ggg$1@slb7.atl.mindspring.net> <396D44E5.B2534FD1@worldnet.att.net>`

```
Arnold Trembley wrote in message <396D44E5.B2534FD1@worldnet.att.net>...

<placed at bottom for those that want to read it>

Your description of an object as a "program" comes close. An object
is a program *plus* the program's data.  In other words, it is a whole
subsystem.  The entire thing is packaged into a dynamically linked
library, so that it can be used without recompiling.

Lets say that you design a system from scratch, using OOPs methods.
Instead of programs, you end up with a bunch of stubs, each of which
invokes methods in a library.  Not only can new  code link to that library,
but all the arguments are checked for type, length, etc. at link time.

For example, I can code something like the following:

    INVOKE PRODUCT-OBJECT "UPDATE-INVENTORY-FIGURES"
            USING PRODUCT-CODE UNITS-SHIPPED, UNITS-RESERVED.

without knowing anything whatsoever about how the inventory system
works. If I am working on order entry, all I need is a copy of the inventory
system DLL and the methods/data descriptions of the arguments. I also
need an extra file (in Fujitsu Cobol, the REP file) that contains the last
symbol table from the object program compile, so that the compiler
can check argument types and entry points for the new code.

In the above code, if the three arguments to not agree at the PICTURE
clause level with the code in the inventory OBJECT program, then the
INVOKE statement will generate a *compile* time error.  In other words,
the creation of an object library creates new Cobol syntax.  That is
the major advantage over working with copies and subroutines.

Everyone has jumped on the OOP stuff as GUI oriented, which is a
huge mistake (IMNSHO).  While it is true that a complete graphics oriented
subsystem can exist as a OOP library, that is simply one of the more common
uses because a screen is one of the most common devices.

In business programs, it make far more sense to isolate the structural
aspects
of the system ... for example all the file locking. By insisting that a
junior
programmer only access files through established methods, I can ensure
that they cannot screw up a data base by opening it in output mode. They
do not even know what the select clause and FD look like.  They get a
record, and if they want to change a counter in that record, then they have
to invoke a method that reads with lock, adds one, writes it, and unlocks
the record.  They probably will not even know what disk drive it is on ...
all that is encapsulated within the object.

If you are Ok with that, so far, I'll continue later. If not, ask away.
There
are enough of us using it in here now to start old timer lessons instead of
just
for students. Do you have a copy of the Fujitsu compiler on a PC so that
posting code is worth while?


Arnold Trembley wrote in message <396D44E5.B2534FD1@worldnet.att.net>...
>"William M. Klein" wrote:
>>
…[4 more quoted lines elided]…
>> > considering its goal of being as native English as possible, and
stretching
>> > the understanding of OO as far as possible to the means of a human
being,
>> > what would be more OO than this:
>> >
…[6 more quoted lines elided]…
>> > using OO Cobol (you don't have to show the entire object construction,
only
>> > the statement assuming the methods exist).
>> >
…[3 more quoted lines elided]…
>> Each of these would be valid (assuming that "anOtherNumber" is the
object -
>> and "addNum" is the method)
>>
…[49 more quoted lines elided]…
>http://arnold.trembley.home.att.net/
```

###### ↳ ↳ ↳ Re: OO question (was Re: Graphical User Interface)

_(reply depth: 28)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396E2BA0.27953A93@home.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <8kiqlh$ggg$1@slb7.atl.mindspring.net> <396D44E5.B2534FD1@worldnet.att.net> <8kl1ho$evt$1@news.igs.net>`

```


donald tees wrote:
> 
> Arnold Trembley wrote in message <396D44E5.B2534FD1@worldnet.att.net>...
…[3 more quoted lines elided]…
> Your description of an object as a "program" comes close <snip>.

Good one Don, as was Ken's example.

Arnold the important thing to remember is what Don stresses - OO has
nothing to do with GUIs.

Although I'm using GUI classes in NetExpress, (because they are
available) - there are other options for GUIs - within N/E - Dialog
System, and Ken Mullins does direct calls to WinAPIs. There are plenty
of Fujitsu and NetExpress users who rely upon Flexus SP2 or Norcom
SCreenIO to do "the GUI bit" and they AREN'T into OO.

There is absolutely nothing to stop Judson McClendon using Screen
Section with OO - but I think I can probably bet the bank that he wont
<G> Unless he's changed focus, I believe this, (Screen Section), is what
Don is concentrating on.

If you are seriously interested in knowing about OO - contact
cobolreport.com and ask about Ed Arranga's or Willson Price's books on
OO COBOL - they are an excellent start.

However, as Don indicated, if you have specific queries - fire away here
in CLC.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: OO question (was Re: Graphical User Interface)

_(reply depth: 29)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396E317D.BAD414DF@cusys.edu>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <8kiqlh$ggg$1@slb7.atl.mindspring.net> <396D44E5.B2534FD1@worldnet.att.net> <8kl1ho$evt$1@news.igs.net> <396E2BA0.27953A93@home.com>`

```
"James J. Gavan" wrote:
> 
> Arnold the important thing to remember is what Don stresses - OO has
> nothing to do with GUIs.

On the other hand, one can count the number of successful non-GUI OO
shops without taking off one's shoes.

Graphics increase the value of reusable objects, so that they often
override the cost of having interdependent objects.  Business rule
objects tend to be less valuable, so the advantages of independency
makes OO a hard sell in the enterprise environment.
```

###### ↳ ↳ ↳ Re: OO question (was Re: Graphical User Interface)

_(reply depth: 30)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kliql$nql$1@news.igs.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <8kiqlh$ggg$1@slb7.atl.mindspring.net> <396D44E5.B2534FD1@worldnet.att.net> <8kl1ho$evt$1@news.igs.net> <396E2BA0.27953A93@home.com> <396E317D.BAD414DF@cusys.edu>`

```

Howard Brazee wrote in message <396E317D.BAD414DF@cusys.edu>...
>"James J. Gavan" wrote:
>>
…[9 more quoted lines elided]…
>makes OO a hard sell in the enterprise environment.

You can count the number of profitable new ventures that do not
use OOP on one hand.  The fact that most of it is GUI oriented
simply means that that is the biggest use, just as the number of
micro's used for other than word processing was small at the
beginning.  The biggest markets always fill first, regardless of facts
like accounting skills being more important than typing skills.

Large corporations will discover it in a dozen years or so.
Meanwhile I am betting I can build my third million dollar business
on it's usefulness.  It takes a while to really understand new concepts,
and a bit longer yet to figure out how to make money on them. But
the wheels slowly grind on.
```

###### ↳ ↳ ↳ Re: OO question (was Re: Graphical User Interface)

_(reply depth: 29)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8klcja$kot$1@news.igs.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <8kiqlh$ggg$1@slb7.atl.mindspring.net> <396D44E5.B2534FD1@worldnet.att.net> <8kl1ho$evt$1@news.igs.net> <396E2BA0.27953A93@home.com>`

```

James J. Gavan wrote in message <396E2BA0.27953A93@home.com>...
>
>
…[4 more quoted lines elided]…
>

Actually, I am using SP2.  However, I am converting large existing systems,
so my methodology is as follows:

1: Change the code so that all screen IO is encapsulated within an object.
Build
those objects by just copying the existing screens, and concentrating on the
movement of data in and out of the objects.

2: Test, run parallel, and implement.  This gives me the absolute assurance
that I have not changed crucial business logic. The user sees exactly what
they
have always seen, and should get the same results.

3. Do the same for the file structures.

4. I now have a five layered system, all data updating is in one module,
all business logic is in another, and all user interfacing in a third.  A
fourth
library handles all OS dependencies, and a fifth handles errors. The latter
two evolve as part of steps 1 and 3.

5. Start doing the fun stuff, like error routines that correct the error
instead of
reporting it, and fancy screens that make it look pretty.
```

###### ↳ ↳ ↳ Re: OO question (was Re: Graphical User Interface)

_(reply depth: 30)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396FA66D.5CB874A1@home.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <8kiqlh$ggg$1@slb7.atl.mindspring.net> <396D44E5.B2534FD1@worldnet.att.net> <8kl1ho$evt$1@news.igs.net> <396E2BA0.27953A93@home.com> <8klcja$kot$1@news.igs.net>`

```


donald tees wrote:
> 
> James J. Gavan wrote in message <396E2BA0.27953A93@home.com>...
…[25 more quoted lines elided]…
> reporting it, and fancy screens that make it look pretty.

Interesting. I wonder if you would categorize what I'm doing as 5-level
?

 {UI(GUIs)--------(Busines Logic)-------------(DBI)
	.					.
	.					.
 Class MyDialog					Class File "X"

Now here's an interesting issue in NetExpress - Messageboxes. In
Business Logic I do field validity checks and jump straight to the
messagebox in the same class. Messageboxes have got to be about the
easiest thing to code :-

*>--------------------------------------------------------------
Method-id. "message-box".                                       
*>--------------------------------------------------------------
Working-storage section.                                        
78 WML                       value 55.   *> ws-MessageLength    
01 ws-MsgA.                                                     
 05 pic x(WML) value z"Client # must be 3 digits/chars".    *> 1
 05 pic x(WML) value z"Shortname can't be blank".           *> 2
 05 pic x(WML) value z"Life Years can't be zero".           *> 3
 05 pic x(WML) value z"Percentage 1 can't be zeroes".       *> 4
 05 pic x(WML) value z"Percentage 2 can't be zeroes".       *> 5
 05 pic x(WML) value z"Range 1 can't be zeroes".            *> 6
 05 pic x(WML) value z"Range 2 must be < 1 and > 2".        *> 7
 05 pic x(WML) value z"Range 3 must be < 2 and > 0".        *> 8
 05 pic x(WML) value z"Range 4 can't be zeroes".            *> 9
 05 pic x(WML) value                                        *> 1
 z"Deleting this record will delete Client's facilities.".      
 05 pic x(WML) value z"Missing Client List".                *> 1
 05 pic x(WML) value z"Logic error - contact Tech Support". *> 1
01 ws-MsgB redefines ws-MsgA occurs 12 pic x(WML).              
                                                                
Local-storage section.                                          
01 ls-MsgBox              object reference.                     
01 ls-Message-text       pic x(WML).                            
Linkage section.                                                
01 lnk-response          pic x(4) comp-5.                       
                                                                
Procedure Division returning lnk-response.                      
                                                                
 invoke MessageBox "new" using os-Parent returning ls-MsgBox    
 invoke ls-MsgBox "setTitleZ" using ws-Windowtitle              
 move ws-MsgB(ValidationFlag) to ls-Message-text                
                                                                
  Evaluate true                                                 
     when OKToDeleteClient                                      
          invoke ls-MsgBox "setTypeInformation"                 
          invoke ls-MsgBox "okCancel"                           
     when ErrorClientList                                       
     when ErrorLogic                                            
          invoke ls-MsgBox "setTypeWarning"                     
          invoke ls-MsgBox "ok"                                 
     when other                                                 
          invoke ls-MsgBox "setTypeInformation"                 
          invoke ls-MsgBox "ok"                                 
  End-evaluate                                                  
                                                                
 invoke ls-MsgBox "setMessageZ" using ls-Message-text           
 invoke ls-MsgBox "show" returning lnk-response                 
 invoke ls-MsgBox "finalize" returning ls-MsgBox                
Exit Method.                                                    
End Method "message-box".                                       
*>--------------------------------------------------------------

Now Ken Mullins a WinAPI user commented "No wonder OO is considered so
verbose" - fair comment and I'd been thinking about it. So along with
Simon Hart in UK I was thinking along lines of creating MyMessagebox,
inherits from MessageBox. Then I thought, "Nah - you've got to pass it
so many parameters why not stick with it in business logic".

Just before reading your message, penny dropped, and I had second
thoughts. As written my messagebox methods are purely WINDOZE - now if I
pass parameters to MyMesageBox it will still function for Windows - BUT
if MyMessageBox is a SEPARATE Class - come the day I want to do messages
in Linux or whatever ???????

Jimmy
```

###### ↳ ↳ ↳ Re: OO question (was Re: Graphical User Interface)

_(reply depth: 28)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2000-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396E9DC8.E7378C00@worldnet.att.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <8kiqlh$ggg$1@slb7.atl.mindspring.net> <396D44E5.B2534FD1@worldnet.att.net> <8kl1ho$evt$1@news.igs.net>`

```
My thanks to Ken Foskey, Donald Tees, James J. Gavan, Howard Brazee, and
Bill Klein (who responded by private e-mail) for all the thoughtful
replies.

I think I'm getting hung up on the implementation of O-O programming
languages and their syntax, when what I probably need to do is first
understand O-O design.

donald tees wrote:
> (snip)
> Everyone has jumped on the OOP stuff as GUI oriented, which is a
> huge mistake (IMNSHO).  While it is true that a complete graphics oriented
> subsystem can exist as a OOP library, that is simply one of the more common
> uses because a screen is one of the most common devices.

I suspect (as an outsider) that GUI lends itself to OOP simply because
so much of the user interface is configurable by the user, and you don't
want to recreate that wheel for every new program.

My problem is, when I'm lucky enough to be actually cranking code rather
than "Impact statements" or "Gap analyses", I'm either coding batch
COBOL or CICS COBOL that has no screens or user interface.  If OO
appears to be used more for GUI than other business problems, well, I'm
not working with GUI's, so I haven't seen any O-O.  I did take a course
on VB 4.0 about three years ago.  It gave me some perspective on coding
for the Windoze environment, but I don't get to do that in my normal
work.

A couple of years ago I had a very interesting conversation with a
programmer whose experience spanned IBM mainframe and Unix
environments.  He told me an O-O design could be implemented in a non
O-O programming language and strongly believed you should start with the
design rather than the programming language. 
 
> (snip)
> If you are Ok with that, so far, I'll continue later. If not, ask away.
…[4 more quoted lines elided]…
> posting code is worth while?

Thanks for all the help.  I do have a couple of copies of Fujitsu 3.0
lying around, as well as Thane Hubbell's book, but I don't have it
currently installed.  I haven't done any COBOL on my PC recently, and
the last time was with Realia (no O-O features in that version).  I'm
way behind on home PC projects, and I'm probably going to be playing
with Linux before I get Fujitsu installed.

I will keep reading, and I'll jump in with a question every now and
then.
```

###### ↳ ↳ ↳ Re: OO question (was Re: Graphical User Interface)

_(reply depth: 29)_

- **From:** theodp@aol.com (Theo DP)
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000714223718.16958.00000674@ng-cu1.aol.com>`
- **References:** `<396E9DC8.E7378C00@worldnet.att.net>`

```
>Subject: Re: OO question (was Re: Graphical User Interface)
>From: Arnold Trembley arnold.trembley@worldnet.att.net 
…[37 more quoted lines elided]…
>> (snip)

Indeed, the key O-O features can be found in many languages - even in good old
Assembler, if one knows where to look (and how to cut through the terminology
B.S.!):

1. Encapsulation (e.g., LCLA, GLBLA) 
2. Polymorphism (e.g., AIF T'varname.., macro keywords)
3. Inheritance (e.g., COPY, MACROs) 
4. Objects/Classes (e.g., DSECTs, Subroutines)
5. Messages (e.g., Parameters)

Everything old is new again (and not always improved upon)!

Further complicating matters is a suprisingly widespread misconception that
OO=GUI:

1. Windows 3.1 was written in good old fashioned C and assembly language and
not the nouveau-OO C++.

2. VB is only recently headed in the OO direction (and with mixed results!)

3. Good old fashioned batch programs can be "OO".

Proof once again that there's more than one way to skin a cat (or CAT.SKIN for
you OO types!)...
```

###### ↳ ↳ ↳ Re: OO question (was Re: Graphical User Interface)

_(reply depth: 29)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3970560E.B49F45B9@zip.com.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <8kiqlh$ggg$1@slb7.atl.mindspring.net> <396D44E5.B2534FD1@worldnet.att.net> <8kl1ho$evt$1@news.igs.net> <396E9DC8.E7378C00@worldnet.att.net>`

```
Arnold Trembley wrote:

> I did take a course on VB 4.0 about three years ago.  It gave me some
> perspective on coding for the Windoze environment, but I don't get to do that
> in my normal work.

VB aint OO.  They are trying to pretty it up but the concepts will
take a lot of rework to make them work.   VB has worse problems than
Cobol, you can extend the syntax easily, can you make your base VB
application look OO without breaking existing code, now that is a
challenge.

> A couple of years ago I had a very interesting conversation with a
> programmer whose experience spanned IBM mainframe and Unix
> environments.  He told me an O-O design could be implemented in a non
> O-O programming language and strongly believed you should start with the
> design rather than the programming language.

100% agree.   There was an article recently that said exactly that. 
Having some trouble recalling where though.  I think it was on Ed
Berard's site http://www.toa.com or may be Robert Martins site
http://www.objectmentor.com/  (under publications).  Both these sites
contain a lot of really useful articles.

Ed is a great, he really makes you think about things, so it was
possibly him but I cannot get his site at present.

> Thanks for all the help.  I do have a couple of copies of Fujitsu 3.0
> lying around, as well as Thane Hubbell's book, but I don't have it
…[3 more quoted lines elided]…
> with Linux before I get Fujitsu installed.

Go the penguin!!!!

I run Fujitsu 3 at home for play.  I am really worried that it is not
good enough for OO cobol development now.  Since my budget for this is
zero, I hope Fujitsu are nice to me and release a newer old version
:-}

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

###### ↳ ↳ ↳ Re: OO question (was Re: Graphical User Interface)

_(reply depth: 30)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2000-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39714D72.626871D6@worldnet.att.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <8kiqlh$ggg$1@slb7.atl.mindspring.net> <396D44E5.B2534FD1@worldnet.att.net> <8kl1ho$evt$1@news.igs.net> <396E9DC8.E7378C00@worldnet.att.net> <3970560E.B49F45B9@zip.com.au>`

```
Ken Foskey wrote:
> 
> Arnold Trembley wrote:
…[9 more quoted lines elided]…
> challenge.

My apologies for not making myself clear.  I can believe Visual Basic is
not object-oriented.  But OO seems to have its greatest use in GUI (at
least so far), and VB is definitely GUI.  I had never previously done
any GUI programming, and the event driven nature of VB was very
different from my previous experience.

I've done a lot of CICS COBOL coding, but usually long-running
conversational tasks with no BMS maps.  Psuedo-conversational CICS
programming with BMS maps is nothing like GUI or VB.

Regards,
```

###### ↳ ↳ ↳ Re: OO question (was Re: Graphical User Interface)

_(reply depth: 27)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396DB584.8BE4B319@zip.com.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <8kiqlh$ggg$1@slb7.atl.mindspring.net> <396D44E5.B2534FD1@worldnet.att.net>`

```
Arnold Trembley wrote:

> No, I truly don't understand this stuff.  Maybe someone can explain it
> to me.
…[11 more quoted lines elided]…
> the self-documenting expression be better?

The benefit is type safe adding values.   If we were simply adding two
numbers then this is a waste and by the way breaks encapsulation.   If
however you were doing something more complex then we need to consider
using object methods to perform modifications on an an object state.

For example an application prints to a PCL printer,  we need bold on
that printer.  A typical traditional approach would be to simply print
the control codes.   An OO approach would be to call a method that
modifies the print files state to bold.   The difference is that the
interface is important and when we change to postscript we simply
replace the object with the new postscript printer object and the
application does not change.

This is a simplistic example,  yes you can do all these things with a
call and a linked module  a couple of things happen:

a)  You don't because you get lazy.

b)  You use link modules and link a version for postscript and a
version for PCL.

the next problem is that you manager now wants the module to be
dynamically swap able.  No problem you rename all the modules to
unique names,  and create a new module that switches between
postscript and PCL.

Now you have added a lot of if tests into you program when it does not
require them.  How OO works is that you implement the if test when you
create the module and then all the methods automatically use the
correct method for that particular instance.

This is a fairly tough concept to understand but this is fundamentally
where the power comes from.

> What does "::" mean?
> 
…[6 more quoted lines elided]…
> "object" in OOP?

An object in OOP is either a class or an instance.   The term IMHO is
useless because it is two vague.

A Class is the definition of an object.  If I say the word table you
can conjure up a mental image of a table without any further detail. 
This is because you have a class definition.

An instance is what I would term a 'true object'.  Not a table but
that one over there.  It is real in computer terms it has storage on
the computer memory.

Object orientation is about bundling the actions you perform with the
data that it acts on.  For example when you choose to move you get
electrical impulses and muscle movement.  You really do not give a
stuff how the thing is achieved, you just want a result.  The message
to the high level is 'I am thirsty' and number of messages are sent
out in response to this,  eyes find coffee cup,  hands move to coffee
cup etc.   This is the important concept of encapsulation.

Again this is not rocket science or new,  you can do this is normal
cobol.  The difference is mind set when you build applications.

> The same article stated that the element of re-use in OOP is a class
> hierarchy.  If I'm having this much trouble understanding what is meant
> by "object", how am I going to be able to re-use a class hierarchy
> without a definition of "class"?

As above we define a class of table.  Now we specialize table into
folding and fixed.   When you want to put a cup down, you look for a
table.  WHo cares whether it is folding or fixed.  When you are trying
to fit it into a small flat then it counts and the extra feature of
the folding table is used.  This process is called polymorphism.

The difference between traditional cobol and OO is that the above
decision tends to be data driven:

	88   foldable
	88   fixed

	if foldable
		kagfhfdghfdg
	else
		sjfldkgkhfdg
	end-if

With OO the object knows what it can do,  if you try and fold a fixed
table it would throw an exception (a firewood exception maybe).

The concept of exceptions in OO cobol is fairly immature and needs a
lot of work unfortunately.

This is not easy to understand the difference.  Unfortunately it is
like driving a BMW, so I am told, you just have to drive it to
understand why it is worth the money. Pete says it is a light bulb
experience and I agree with him, once you get it you wont go back.

I really hope this helps,
Ken
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 25)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396D3CF6.6E82DB80@home.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net>`

```


Cheesle wrote:
> 
> "Joseph J Katnic" <josephk@iinet.net.au> wrote in message
> > Secondly, absolutely everything is Smalltalk is an OBJECT.

++++++

Firstly - thanks to NowitAll, Cheesle and Thane for showing GUI
examples. Particularly the POWERCOBOL 'under the covers' object
generation. Now I know what you are talking about Mr. Dashwood - AND -
me no likee !

I've got Adele Goldberg's "Smalltalk 80". I know nothing about the
language but I certainly picked up on the fact that EVERYTHING was an
object. My reason for buying the book was her illustration of
collections/dictionaries - which we have in Fujitsu and NetExpress;
many of method names are same or similar to Smalltalk.

++++++++++++
> 
> Yes, that was what I considered to be the major difference from C++/Delphi,
…[18 more quoted lines elided]…
> the statement assuming the methods exist).

+++++++++++

Well you gave me the AcuCOBOL GUI example, so I'll give it a shot. 

For the life of me, can't immediately think why you would want to use
these but here goes :--

*>---------------------------
Method-id. "add-two-numbers".
*----------------------------
Linkage section.
01 lnk-1			pic 9(18) comp-3.
01 lnk-2			pic 9(18) comp-3.
01 lnk-result			pic 9(18) comp-3.
Procedure Division using lnk-1, lnk-2
		   returning lnk-result.

	add lnk-1, lnk-2 giving lnk-result *> OR compute etc....
End Method .....
*>----------------------------

*>---------------------------
Method-id. "add-to-constant".
*----------------------------
Local-storage section.
01 avalue CONSTANT 	value 56.	*> COBOL 200X proposal which
					*> is Level 78 in N/E
Linkage section.
01 lnk-1			pic 9(18) comp-3.
01 lnk-result			pic 9(18) comp-3.
Procedure Division using lnk-1
		   returning lnk-result.

	add avalue, lnk-1 giving lnk-result
End Method .....
*>-----------------

As I say, I don't think the above gives you much leverage, we are
already well served by pic 9's and pic x's in COBOL, with Arithmetic
VERBS, STRING, REFERENCE MODIFICATION etc. But here are some working
examples that I need for Imperial/Metric conversions :-

I could build these routines into individual classes, but assuming I've
got 20 programs converting inches/mms - then that gives me 20 chances of
getting it wrong doesn't it - so this approach, write it once and get it
right, to me, makes more sense.

*>------------------------------------------------------------
Method-id. "imp-to-met".                                      
*>------------------------------------------------------------
Linkage section.                                              
01 lnk-inches                   pic 9(03)v9(03) comp-3.       
01 lnk-mms                      pic 9(03)v9(02) comp-3.       
                                                              
Procedure Division using     lnk-inches                       
                   returning lnk-mms.                         
                                                              
   if  lnk-inches <> zeroes                                   
       compute lnk-mms rounded = lnk-inches * 25.4            
                                                              
   else move zeroes to lnk-mms                                
   End-if                                                     
                                                              
End Method "imp-to-met".                                      
*>------------------------------------------------------------
Method-id. "met-to-imp".                                      
*>------------------------------------------------------------
Linkage section.                                              
01 lnk-mms                      pic 9(03)v9(02) comp-3.       
01 lnk-inches                   pic 9(03)v9(03) comp-3.       
                                                              
Procedure Division using     lnk-mms                          
                   returning lnk-inches.                      
                                                              
   if    lnk-mms <> zeroes                                    
         compute lnk-inches rounded = lnk-mms * 0.03937       
                                                              
   else  move zeroes to lnk-inches                            
   End-if                                                     
End Method "met-to-imp".                                      
*>------------------------------------------------------------
Method-id. "kpa-to-psi".                                       
*>-------------------------------------------------------------
Linkage section.                                               
01 lnk-kpa                       pic 9(05) comp-3.             
01 lnk-psi                       pic 9(05) comp-3.             
                                                               
*>78 ls-convert                  value 0.1450326.              
                                                               
Procedure Division using    lnk-kpa                            
                  returning lnk-psi.                           
                                                               
  if lnk-kpa <> zeroes                                         
     compute lnk-psi rounded = lnk-kpa * 0.145                 
                                                               
  else move zeroes to lnk-psi                                  
  End-if                                                       
                                                               
End Method "kpa-to-psi".                                       
*>-------------------------------------------------------------
Method-id. "psi-to-kpa".                                       
*>-------------------------------------------------------------
Linkage section.                                               
01 lnk-psi                       pic 9(05) comp-3.             
01 lnk-kpa                       pic 9(05) comp-3.             
                                                               
Procedure Division using    lnk-psi                            
                  returning lnk-kpa.                           
                                                               
  if lnk-psi <> zeroes                                         
     compute lnk-kpa rounded = lnk-psi * 6.8948                
                                                               
  else move zeroes to lnk-kpa                                  
  End-if                                                       
                                                               
End Method "psi-to-kpa".                                       
*>-------------------------------------------------------------

Same as above for Fahrenheit and Celsisus, Gallons and Litres.etc...

Now if you want to start dabbling in objects within OO COBOL then you
need the classes which cover arrays etc under FJBASE or BASE (for N/E).
So taking above two examples and objectifying them, using N/E available
classes/methods :-

*>---------------------------
Method-id. "add-two-Objnumbers".
*----------------------------
Local-storage section.
01 ls-CurrentObject		object reference.
01 ls-num1			pic 9(18).
01 ls-num2			pic 9(18).
01 ls-length			pic x(4) comp-5.
01 ls-num18			pic 9(18).
01 ls-string			object reference.
01 ls-text18			pic x(18).

Linkage section.
01 lnk-obj1			object reference.
01 lnk-obj2			object reference.
01 lnk-objresult		object reference.

Procedure Division using lnk-obj1, lnk-obj2
		   returning lnk-objresult.

*> I'm playing it real safe here <G> :-

set ls-CurrentObject to lnk-obj1
perform OBJECT-TO-STRING
move ls-Num18 to ls-Num1

set ls-CurrentObject to lnk-obj2
perform OBJECT-TO-STRING
move ls-Num18 to ls-Num2

add ls-Num1, ls-Num2 giving ls-Num18

perform STRING-TO-OBJECT

EXIT METHOD.	*> This 'Exit' gets us out of the method
 
OBJECT-TO-STRING.

invoke ls-CurrentObject "getText" returning ls-string
invoke ls-string "trimblanks" returning ls-string
invoke ls-CurrentObject "Getlength" returning ls-length
invoke ls-string "getValueWithSize"
       using ls-Length returning ls-Text18
compute ls-Num18 = function numval (ls-Text18)
invoke ls-string "finalize" returning ls-string
.

STRING-TO-OBJECT.

invoke CharacterArray "withLengthValue"
       using ls-length, ls-Num18
       returning ls-string
invoke lnk-objresult "setText" using ls-string
invoke ls-string "finalize" returning ls-string
.

*> ++++ No Exit Method here....
End Method .....
*>----------------------------

*>---------------------------
Method-id. "addobj-to-constant".
*----------------------------
Local-storage section.
01 avalue CONSTANT 	value 56.	*> COBOL 200X proposal which
					*> is Level 78 in N/E
01 ls-length			pic x(4) comp-5.
01 ls-string			object reference.
01 ls-Num18			pic 9(18).
01 ls-Text18			pic x(18).
Linkage section.
01 lnk-obj1			pic 9(18).
01 lnk-objresult		pic 9(18).
Procedure Division using lnk-obj1
		   returning lnk-objresult.

move 18 to ls-length
perform OBJECT-TO-STRING
add ls-Num18, aValue giving ls-Num18
perform STRING-TO-OBJECT

OBJECT-TO-STRING.

invoke lnk-obj1 "getText" returning ls-string
invoke ls-string "trimblanks" returning ls-string
invoke lnk-obj1 "Getlength" returning ls-length
invoke ls-string "getValueWithSize"
       using ls-Length returning ls-Text18
compute ls-Num18 = function numval (ls-Text18)
invoke ls-string "finalize" returning ls-string

STRING-TO-OBJECT.

invoke CharacterArray "withLengthValue"
       using ls-length, ls-Num18
       returning ls-string
invoke lnk-objresult "setText" using ls-string
invoke ls-string "finalize" returning ls-string

End Method .....
*>-----------------

And the immediate reaction of anybody looking at the last two examples -
YOU GOTTA BE NUTS ! However there are instances where you do want pic
9's pic x's string-to-object and vice versa - specifically GUIs. In my
own case out of approx 170 classes, I have only ONE that does the
conversion above - MyDialog.cbl.  The only other exception is when
creating/changing collections/dictionaries.

So, within MyDialog.cbl I have basically two methods to handle this :-

- "set-entryfield"	STRING-TO-OBJECT above, 

- "return-entryfield"   OBJECT-TO-STRING above

Joe may have a different take on the above, and Thane may care to
comment with regard to Fujitsu.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 26)_

- **From:** Joseph J Katnic <josephk@iinet.net.au>
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39705E66.67378D3D@iinet.net.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com>`

```


"James J. Gavan" wrote:
> 
<snip> 
> Joe may have a different take on the above, and Thane may care to
> comment with regard to Fujitsu.
> 
I don't have a take on OO. I think that the jury is still out. I think
that as OO techniques can be applied to non-OO languages, especially as
regards to design, you will tend to find OO more in GUI environments.
The reason for this is as I have stated previously, the vast amount of
rubbish one has to put up with merely to put a character on a screen. It
makes obvious sense to have classes pre-coded that can be re-used again
and again in this environment. It is not so obvious when it comes to the
business logic of the enterprise. Some activities are indeed common
amongst enterprises, however, it is the differences that lead to an
enterprise coming out on top. The business that follows the pack will
always be destined to be a follower.

I further feel, that the language designers have thrown up their hands
and given up on GUI. In this I think that they have done a great
dis-service to the general programming community. They seem to feel that
providing the community with OO and CALL interfaces, somehow relieves
them of their duty to provide programming tools that make for effective programmers.

I'll say it again. Until we have languages that standardize GUI the same
way that FILE IO was standardized by COBOL, then we will always face
this problem.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 27)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3970AEC8.48729D2D@home.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au>`

```


Joseph J Katnic wrote:
> 
> "James J. Gavan" wrote:
…[5 more quoted lines elided]…
> I don't have a take on OO. I think that the jury is still out....<Snip>

MOST DEFINITELY !

> I'll say it again. Until we have languages that standardize GUI the same
> way that FILE IO was standardized by COBOL, then we will always face
> this problem.

I agree with you wholoe-heartedly on this one, especially using your
parallel of file handling. But you know what - you and I are in a
minority on this one. Watch for comments from Thane and Ken for starters
<G>

Jimmy
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 28)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3970d320.24576308@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au> <3970AEC8.48729D2D@home.com>`

```
Here's the comment from Thane.

Standardizing Indexed file I-O in COBOL didn't lead to such
standardizatiion in other languages.  The just jumped over it, using
an external DBMS when teh need for external files arised.  The same is
true of the UI.  UI's change TOO QUICKLY as they should -- to
Standardize it. 

As soon as you standardize a UI in COBOL itself, it will be obsolete.


Oh wait, that already happened.   (And the ink isn't even laid down on
the standard yet.)

I rest my case.


On Sat, 15 Jul 2000 18:35:40 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>
>
…[21 more quoted lines elided]…
>Jimmy

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 28)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39717C03.D4E651D8@zip.com.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au> <3970AEC8.48729D2D@home.com>`

```
"James J. Gavan" wrote:
> 
> Joseph J Katnic wrote:
…[8 more quoted lines elided]…
> minority on this one. Watch for comments from Thane and Ken for starters

Without standard GUI code across all platforms then IMHO:

	COBOL IS DEAD!

Not what you expected Jimmy.   Java has done it and become a
successful language because of it.  I am concerned with how this is
achieved.

I think the IDE (interactive development environment) can be totally
different, as brilliant at churning screens as VB or Delphi, or as
crappy just cutting code, the important point is that it should run on
all environments.

This solution should address:

MVS / web server - Browser based access.
PC - MS windows
Unix - X windows

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 29)_

- **From:** "Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s>
- **Date:** 2000-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ks8jq$8od$1@slb2.atl.mindspring.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au> <3970AEC8.48729D2D@home.com> <39717C03.D4E651D8@zip.com.au>`

```
> Java has done it and become a successful language because of it.  I am
concerned with how this is  achieved.>

hmmmmmmm...

I read an interesting article the other day (don't remember where) but it
point blank said MS is not going to be using Java in future OS net.com
development environments...

kenmullins
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 30)_

- **From:** "Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s>
- **Date:** 2000-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ks9om$k6b$1@slb6.atl.mindspring.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au> <3970AEC8.48729D2D@home.com> <39717C03.D4E651D8@zip.com.au> <8ks8jq$8od$1@slb2.atl.mindspring.net>`

```
http://yahoo.cnet.com/news/0-1003-200-2240702.html?pt.yfin.cat_fin.txt.ne

Link to article on Java and MS

Looks like C# will be the MS choice


"Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s> wrote in
message news:8ks8jq$8od$1@slb2.atl.mindspring.net...
> > Java has done it and become a successful language because of it.  I am
> concerned with how this is  achieved.>
…[10 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 30)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3971B7D8.16A193D2@zip.com.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au> <3970AEC8.48729D2D@home.com> <39717C03.D4E651D8@zip.com.au> <8ks8jq$8od$1@slb2.atl.mindspring.net>`

```
Ken Mullins wrote:
> 
> > Java has done it and become a successful language because of it.  I am
…[6 more quoted lines elided]…
> development environments...

This one is easy,  they tried to warp Java to their means, they
couldn't and had to rip it out of their products.  Now they don't want
a bar of it.

BOttom line,  MS is NOT interested in what is the greater good.  They
also have a policy of undermining LInux with FUD.  They are finally
running scared and personally I like it.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 30)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3971b930.83481356@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au> <3970AEC8.48729D2D@home.com> <39717C03.D4E651D8@zip.com.au> <8ks8jq$8od$1@slb2.atl.mindspring.net>`

```
On Sun, 16 Jul 2000 08:03:19 -0400, "Ken Mullins"
<**Ken**Mullins**@**mindspring.com** remove **'s> wrote:

>> Java has done it and become a successful language because of it.  I am
>concerned with how this is  achieved.>
…[6 more quoted lines elided]…
>

MS Net is vaporware.  But if what I read is rigth it will be XML
based.
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 31)_

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-07-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6Rsc5.178290$7o1.4447667@news2.rdc1.on.home.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au> <3970AEC8.48729D2D@home.com> <39717C03.D4E651D8@zip.com.au> <8ks8jq$8od$1@slb2.atl.mindspring.net> <3971b930.83481356@207.126.101.100>`

```
XML will describe the data. It's still going to take a whole lot of coding
in some sort of programming language to render that data in a form that is
usable by either people or machines. XML isn't a programming language.

The advantage of XML is that it embeds the description of the data within
the data itself. The disadvantage is it's a really inefficient way to
transmit and process data.


"Thane Hubbell" <thaneH@softwaresimple.com> wrote in message
news:3971b930.83481356@207.126.101.100...
> On Sun, 16 Jul 2000 08:03:19 -0400, "Ken Mullins"
> <**Ken**Mullins**@**mindspring.com** remove **'s> wrote:
…[15 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 32)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39728fcb.7032917@207.126.101.100>`
- **References:** `<sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au> <3970AEC8.48729D2D@home.com> <39717C03.D4E651D8@zip.com.au> <8ks8jq$8od$1@slb2.atl.mindspring.net> <3971b930.83481356@207.126.101.100> <6Rsc5.178290$7o1.4447667@news2.rdc1.on.home.com>`

```
On Mon, 17 Jul 2000 00:56:34 GMT, "Oscar T. Grouch" <dustbin@home.com>
wrote:

>XML will describe the data. It's still going to take a whole lot of coding
>in some sort of programming language to render that data in a form that is
…[5 more quoted lines elided]…
>

I've looked on it as an EDI replacement....

However, in addition, you CAN tell XML how to render the XML within
the XML.  (What HTML elements to use for certain XML data types for
instance).

I think C# will play into the mix somehow as well.


---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 32)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-07-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39731431.77B70CC@zip.com.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au> <3970AEC8.48729D2D@home.com> <39717C03.D4E651D8@zip.com.au> <8ks8jq$8od$1@slb2.atl.mindspring.net> <3971b930.83481356@207.126.101.100> <6Rsc5.178290$7o1.4447667@news2.rdc1.on.home.com>`

```
"Oscar T. Grouch" wrote:
> 
> The advantage of XML is that it embeds the description of the data within
> the data itself. The disadvantage is it's a really inefficient way to
> transmit and process data.

You can create a definition of XML as data and XML as the
presentation.  When you bring the two together you get an image.  This
means the one data set can be presented a number of ways without
downloading a new set each time.

The additional overhead of XML, i.e. data tags, is worth it to make an
application easy if you want a lot of interfaces to your data, or a
lot of sources for your data.  If you consider the win.ini type files
work on key=data so that new fields are easy to add in.  The
disadvantage is multiple line keys are difficult.  XML with it's start
and stop tags fixes this.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 32)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-07-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ya%c5.4321$mV1.1559082@news3.mia>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au> <3970AEC8.48729D2D@home.com> <39717C03.D4E651D8@zip.com.au> <8ks8jq$8od$1@slb2.atl.mindspring.net> <3971b930.83481356@207.126.101.100> <6Rsc5.178290$7o1.4447667@news2.rdc1.on.home.com>`

```
"Oscar T. Grouch" wrote:
>
> The advantage of XML is that it embeds the description of the data within
> the data itself. The disadvantage is it's a really inefficient way to
> transmit and process data.

Same is true of SQL, but it hasn't stopped 'em. :-)
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 29)_

- **From:** Joseph J Katnic <josephk@iinet.net.au>
- **Date:** 2000-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3971A502.1E25553E@iinet.net.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au> <3970AEC8.48729D2D@home.com> <39717C03.D4E651D8@zip.com.au>`

```


Ken Foskey wrote:
> 
> 
…[7 more quoted lines elided]…
> 
This is really easy! Because JAVA leverages the HTML paradigm. Which if
you remember is exactly what I am advocating COBOL should do.
Furthermore, I really feel that COBOL should be expanded to include the
JAVA compiler as well as the COBOL syntax. Why you may ask? Well, I feel
that the COBOL language should be extended to make a
programmer/developers life easier. If My suggestion of GUI control
statements based on HTML/XML is to be taken up, then there should be
some way for the COBOL developer to imbed the JAVA screen control into
the application. Whether this creates a separate file or not is
irrelevant. So the COBOL developer can create COBOL applications with
built in JAVA extensions for customizing the HTML/XML  GUI interface.
All this source is run through the COBOL Compiler, with creates the
appropriate output based on the input. HTML/XML, JAVA byte codes, COBOL
executables. You don't need to invoke one compiler for the XML, another
for the JAVA and yet another for the COBOL. How this is done is also
irrelevant so long as it happens. If the COBOL compiler invokes the
other compilers as it needs to, then that's fine by me. I don't expect
the COBOL compiler writer's to re-invent the wheel, just make use of the
newer models and incorporate them as they become either standard or
defacto standard. (Please note defacto, I don't believe the compiler
writers should wait for the existing standards committees) to rule).

Furthermore, just like the "American Way", I would like to see the
compiler writers compete on most platforms so that:
1. The price drops.
2. More features are developed into the compiler. (I believe in
rewarding innovation).
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 30)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3971b99c.83589217@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au> <3970AEC8.48729D2D@home.com> <39717C03.D4E651D8@zip.com.au> <3971A502.1E25553E@iinet.net.au>`

```
On Sun, 16 Jul 2000 20:05:22 +0800, Joseph J Katnic
<josephk@iinet.net.au> wrote:

What you describe below IS presently available with PerCOBOL - have
you looked at it?


>This is really easy! Because JAVA leverages the HTML paradigm. Which if
>you remember is exactly what I am advocating COBOL should do.
…[28 more quoted lines elided]…
>Joe Katnic     josephk@iinet.net.au

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 31)_

- **From:** Joseph J Katnic <josephk@iinet.net.au>
- **Date:** 2000-07-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<397454BE.E935D126@iinet.net.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au> <3970AEC8.48729D2D@home.com> <39717C03.D4E651D8@zip.com.au> <3971A502.1E25553E@iinet.net.au> <3971b99c.83589217@207.126.101.100>`

```


Thane Hubbell wrote:
> 
> On Sun, 16 Jul 2000 20:05:22 +0800, Joseph J Katnic
…[4 more quoted lines elided]…
> 
Hi,
No,
What's a PerCOBOL?
Is it available for Mac or Linux?
Is it compiled or interpreted?
Is there a HTTP link?
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 32)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39747179.55959405@207.126.101.100>`
- **References:** `<20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au> <3970AEC8.48729D2D@home.com> <39717C03.D4E651D8@zip.com.au> <3971A502.1E25553E@iinet.net.au> <3971b99c.83589217@207.126.101.100> <397454BE.E935D126@iinet.net.au>`

```
PerCOBOL is available here: http://www.legacyj.com

It runs anywhere there is a JVM.  It's a COBOL source compiler that
creates JAVA byte code.  It's only as interpreted as JAVA is.

It does NOT convert COBOL source to JAVA source -- it's a true
compiler.


On Tue, 18 Jul 2000 20:59:36 +0800, Joseph J Katnic
<josephk@iinet.net.au> wrote:

>
>
…[17 more quoted lines elided]…
>Joe Katnic     josephk@iinet.net.au

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 29)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3971b6c7.82864121@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au> <3970AEC8.48729D2D@home.com> <39717C03.D4E651D8@zip.com.au>`

```
On Sun, 16 Jul 2000 19:10:27 +1000, Ken Foskey <waratah@zip.com.au>
wrote:
>
>Without standard GUI code across all platforms then IMHO:
…[5 more quoted lines elided]…
>achieved.

It's not often that I disagree with Ken.  I agree that Java is
succesful, but I disagree that the reason is the common GUI or user
interface.  The reason that JAVA has become sucessful is that VAST and
I mean VAST array of available class libraries.  On this count I agree
with Jimmy... we can have great COBOL success only with common class
libraries with OO COBOL.  If the breadth of available COBOL routines
was as vast as those available in JAVA things would be quite
different.  As Pete Dashwood would agree -- building from pre-packaged
componants is what is happening.  Where I work (presently at least)
they are making extensive use of JAVA in new development.  However not
one bit of it is for the UI.  The UI is the web broswer or a Windows
client or even a DOS client that is still in use.  The JAVA is used
for data formatting, socket connections, multi-threaded database data
recormatting and access.  Very little of the code -- just the classes
that are the framework of the application -- are written in house.
Everything else is a SUN or otherwise supplied class.

The DIFFERENCE here, is that JAVA obviously has a common interface --
there is only one JAVA vendor.

Visual Basic has a common interface -- there is only one VB Vendor.  

PowerBuilder has a common interface -- there is only one PB Vendor.

C++ does NOT have a common interface across all platforms.  Is this
why JAVA is kicking it's butt?  No, it's because you can't share C++
object libraries across platforms.  

In short there are two reasons for JAVA's APPARANT success -- that
really boil down to 1 -- JAVA runs on multiple platforms, and common
class libraries can be developed on ANY platform and shared by all.
Additionally SUN has done a masterful job of providing a breadth of
classes.  

Is JAVA a COBOL killer?  I don't think so, although it comes closest
to anything I have seen to date.  There are still maintenance issues
and expenses that do not exist with COBOL.  

>
>I think the IDE (interactive development environment) can be totally
…[15 more quoted lines elided]…
>http://www.themailxchange.com.au/

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 30)_

- **From:** "Steven Lalewicz" <strl@mfltd.co.uk>
- **Date:** 2000-07-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8l2g52$aaa$1@hyperion.mfltd.co.uk>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au> <3970AEC8.48729D2D@home.com> <39717C03.D4E651D8@zip.com.au> <3971b6c7.82864121@207.126.101.100>`

```

Thane Hubbell wrote in message <3971b6c7.82864121@207.126.101.100>...
>On Sun, 16 Jul 2000 19:10:27 +1000, Ken Foskey <waratah@zip.com.au>
>wrote:
…[8 more quoted lines elided]…
>
<stuff>
>
>In short there are two reasons for JAVA's APPARANT success -- that
…[4 more quoted lines elided]…
>

The other thing JAVA has going for it, is it it not run by a committee.
It's currently still a proprietary language under Sun's control. The
other advantage JAVA has had over COBOL, C++ is they have managed to in
effect start again, very much looking at where other languages have failed
and I think done a very good job (echoing comments I've read ealier).

Sun from the start included a GUI frame work, which they build on. Plus
the language includes multithreading support and other 'modern' features
from the start, which are 'seamless' with the language rather than a later
addition.

COBOL and C++ on the hand were born before GUI was around. So the COBOL
vendors have tried to allow GUI programming with their product, but not
surprisingly it's is proprietary and different from vendor to vendor.
Plus the COBOL vendors are trying to compete with each other. Mind you
there was the XOPEN for SCREEN SECTION. There is no reason why some
committee can't come up with a standard GUI/classes for COBOL at a later
stage. Committees for all their hard and good work, don't seem to move at
a very fast pace compared to the speed at what Sun have done with JAVA.

Vendors will always want to add their own proprietary features to make
them different. Look at what Microsoft tried to do with JAVA, and Sun was
not pleased. So MS have snubbed Sun and created C#.

Sun, while JAVA and it's classes are still proprietary also has the power
to enhance the environment and it's still 'standard'. Once a vendor adds
something new, it is no longer 'standard'.

BTW, In NX3.1 one can seamlessly call JAVA classes from COBOL. So what
this says to me is I can call the GUI classes from COBOL. When I have some
time, I must give this ago.

In the past I've always avoided GUI programming because I really did not
want to learn a whole new system for every platform out there. For the
first time I'm actually feel motivated to do GUI programming with JAVA
because I can move my apps in theory to different platforms without any
problems.

Plus the whole JAVA lot is free! I can install it anywhere and how often I
please.

I went on a C++/MFC course not so long ago, I was impressed by the class
wizard. However my own opinion is what it does under the covers is ugly.
Which is what one might expect when you realise it is bolted onto the SDK.

Now I've been challenged with programming with event driven code, where
to put my program logic, where to put the gui stuff, how to structure my
classes together, I begin to see why they came up with the CVIEW/CDOCUMENT
architecture. Another throw in, it was not until I'd figured out how to
do OO programming in JAVA was I able to get to grips with OO programming
in COBOL. Okay, better end my rambling here.

Regards,
Steve.

<stuff>
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 29)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kshjd$107$1@news.igs.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au> <3970AEC8.48729D2D@home.com> <39717C03.D4E651D8@zip.com.au>`

```

Ken Foskey wrote in message <39717C03.D4E651D8@zip.com.au>...

>> > I'll say it again. Until we have languages that standardize GUI the
same
>> > way that FILE IO was standardized by COBOL, then we will always face
>> > this problem.
…[19 more quoted lines elided]…
>

hmm.  Maybe I am out to lunch, but it seems to me that if the standard
screen
section worked at the web level, then that is exactly what we already have.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 30)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-07-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wo%c5.4324$mV1.1565980@news3.mia>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au> <3970AEC8.48729D2D@home.com> <39717C03.D4E651D8@zip.com.au> <8kshjd$107$1@news.igs.net>`

```
"donald tees" wrote:
>
> hmm.  Maybe I am out to lunch, but it seems to me that if the standard
> screen section worked at the web level, then that is exactly what we
> already have.

Exactly!  It could use a few enhancements to allow for GUI interface.
This is what I tried to promote in a thread here a few months ago, but
there seemed little enthusiasm for it.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 31)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-07-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39749148.EC885BBA@home.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au> <3970AEC8.48729D2D@home.com> <39717C03.D4E651D8@zip.com.au> <8kshjd$107$1@news.igs.net> <wo%c5.4324$mV1.1565980@news3.mia>`

```


Judson McClendon wrote:
> 
> "donald tees" wrote:
…[7 more quoted lines elided]…
> there seemed little enthusiasm for it.

But remember, remember Thane's VERY VALID point - it has to be ALL or
NOTHING at all. A half-wy house isn't going to help anybody.

Jimmy
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 27)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-07-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s7%c5.4318$mV1.1559188@news3.mia>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au> <8ki0ok$fig$1@news.cerf.net> <396D3CF6.6E82DB80@home.com> <39705E66.67378D3D@iinet.net.au>`

```
"Joseph J Katnic" wrote:
>
>
> I'll say it again. Until we have languages that standardize GUI the same
> way that FILE IO was standardized by COBOL, then we will always face
> this problem.

Amen to that!
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 24)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396DAC2C.50821A3A@zip.com.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au>`

```
Joseph J Katnic wrote:
> 
> How bizarre this is can only be appreciated when you start to program. E.G.
…[7 more quoted lines elided]…
> standards and their current interpretation.

Excellent pick up.  This is something that the standards committee
must address. The operator methods are incredibly powerful.  It would
be easy to add to OO cobol for example we create a method 'add' and it
overrides a statement

	add x to object.

The next problem is that the type of x is important.  YOu want to be
able to add currency objects together and nothing else.   For example
to add german to australian currency would require a current rate
converter.  If you add australian1 to australian2 then no converter is
required.

The standards body are still struggling with the basics of OO I wonder
how they will cope with this?

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 24)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396DAC15.E173B8D8@zip.com.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au> <8kgv0j$17t$1@news.cerf.net> <396C72D4.2BBB6048@iinet.net.au>`

```
Joseph J Katnic wrote:
> 
> How bizarre this is can only be appreciated when you start to program. E.G.
…[7 more quoted lines elided]…
> standards and their current interpretation.

Excellent pick up.  This is something that the standards committee
must address. The operator methods are incredibly powerful.  It would
be easy to add to OO cobol for example we create a method 'add' and it
overrides a statement

	add x to object.

The next problem is that the type of x is important.  YOu want to be
able to add currency objects together and nothing else.   For example
to add german to australian currency would require a current rate
converter.  If you add australian1 to australian2 then no converter is
required.

The standards body are still struggling with the basics of OO I wonder
how they will cope with this?

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 22)_

- **From:** Joseph J Katnic <josephk@iinet.net.au>
- **Date:** 2000-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396C70D1.1B374EBF@iinet.net.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au> <396BA434.504E0F1C@zip.com.au>`

```


Ken Foskey wrote:
> 
> 
…[5 more quoted lines elided]…
> 
AH yes, but the title is "Graphical User Interface"!

Besides, that I take your point and fully agree.

Where I disagree is the abrogation of responsibility the compiler
writers have displayed in recent years. Because they provided the CALL
EXTERNAL statement and now with OO the ability to invoke OS methods.
They then assume that they no longer need to provide proper language
constructs to the OS functions.

I mean, it is just as feasible to do disk io by calling a OS routine
than by using READ and WRITE. But READ AND WRITE provide some other
benefits, not the least of which is STANDARDS!

You can pretty much guarantee, that READ and WRITE will work the same
way on all platforms. I would like to see you try that with either the
CALL interface or compiler supplied OO methods (which are non standard).

SP2 in my opinion has an advantage in that should a GUI language
standard ever be adopted, the SP2 engine can be incorporated into the
runtime for the language and the new standard used to invoke it. All the
others would eventually have to write some form of engine to interpret
the language elements at runtime.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 21)_

- **From:** "Robert Sales" <Robert.Sales@merant.com>
- **Date:** 2000-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8khncb$djv$1@hyperion.mfltd.co.uk>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <396146c1.107349677@207.126.101.100> <39623CA6.6C6938B6@freedsl.com> <39627DD3.53048C5C@home.com> <8k28i7$g02$1@news.cerf.net> <39652742.26F07625@freedsl.com> <8k3laq$sge$1@news.cerf.net> <39675F09.EA08060@freedsl.com> <8kbde4$ng8$1@news.cerf.net> <3969eab4.46135220@207.126.101.100> <8kdm9f$m19$1@news.cerf.net> <396B1C86.F2EAE170@iinet.net.au>`

```
Re html, the idea of introducing variables is exactly what is done with the
Net Express EXTERNAL-FORM syntax.  There are two associated verbs, ACCEPT
which is used for receiving user input from CGI, ISAPI or NSAPI dialogs, and
DISPLAY which replaces named variables in an existing html file with program
data.  The variables to be replaced are identified in the html by being
enclosed in pairs of %% symbols.
As a simple example, suppose the file greet.htm contains:

<html headers etc.>
...
hello %%custname%%
...

COBOL program has:
...
01 output-form is external-form identified by "greet.htm".
...
   03 output-name identified by "custname".
...
    move customer-name to output-name
   display output-form

Since the display text and layout, graphics etc. are not handled by the
COBOL program, internalization and general customization of the web-page is
very straightforward.

By the way, I couldn't agree more with the idea that user interfaces should
be separated out from program logic.  I think the intermingling of the two,
has been hugely detrimental, resulting in massive and unmaintainable
programs where the actual logic is almost invisible.

Robert Sales (MERANT).

"Joseph J Katnic" <josephk@iinet.net.au> wrote in message
news:396B1C86.F2EAE170@iinet.net.au...
>
>
…[3 more quoted lines elided]…
> > Acucobol approach is the ultimate. On the other side, we should not end
up
> > with a solution that requires complex OO constructions to develop gui in
> > Cobol, that is what I am afraid of.
…[3 more quoted lines elided]…
> > Generally speaking, I don't understand why the OO Cobol approach is
using
> > the C++/Java approach, while Smalltalk is way closer to Cobol in terms
of
> > English language look a like. Is there anyone out there that can tell me
> > this?
…[9 more quoted lines elided]…
> some developer may want to change the way the OS draws a border for
example).
>
> This unfortunate circumstance (started by Xerox, publicized by Apple and
…[7 more quoted lines elided]…
> manager and the dialog manager draws the screen based on a scripting
language.
>
> Now where have we heard of a similar scheme.
…[33 more quoted lines elided]…
> I'm not certain, but I think that a lot of the above could be done via
XML.
>
> So now all we need is a Web SERVER, but for local only display a runtime
…[5 more quoted lines elided]…
> Joe Katnic     josephk@iinet.net.au
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 10)_

- **From:** flexus@epix.net (Bob Wolfe)
- **Date:** 2000-07-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3963746c.19812899@news.epix.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com>`

```
nowitt@freedsl.com wrote:

>
>
…[21 more quoted lines elided]…
>COBOL Gold Mine.

Debates are only healthy when the debating parties use diplomacy,
adhere to and mutually respect factual information provided by their
opponent and avoid speaking in generalities.  You have done none of
the above and it should be obvious in the replies you have received
from highly respected regular contributors to this newsgroup.

If it is not obvious to you yet, I suspect that many consider you to
be just a tad zealous in your belief.....zealots are rarely considered
credible.

I have said it many times and will continue to say that in my opinion,
this newsgroup is a platform for the free exchange of ideas by
professional COBOL programmers.  While I appreciate the fact that your
strong opinions are based upon the fact that you are so religious in
your views, please remember that I will avoid debate in this forum
because the debate shouldn't come from a vendor, but from those who
utilize COBOL daily in their studies, occupations or hobbies.

>I can say this.  Everyone has different motivations for using a
>particular compiler, screen handler or some other type of tool.
…[10 more quoted lines elided]…
>Ferrari.

But you are making an incorrect assumption that everyone who drives a
car in the world wants horsepower or luxury.  This is simply not true.
I know many people who would sell a Mercedes or Lexus, if given to
them, and purchase a VW or Escort with the proceeds, simply because
they value economy, thrift, conservation and environmental
preservation than they value looking cool in front of their friends
and breaking the law by exceeding the speed limit.

Diff'rent Strokes for Diff'rent Folks!

.....Sly and the Family Stone

>I can say this.  If the program you demonstrate on your web site is
>100% COBOL, then I challenge you to recompile it with any of the
…[12 more quoted lines elided]…
>COBOL-85.

I'm afraid that I would have to see this to believe it.  Are you
saying that the COBOL source code for the application featured on the
web site which you directed us toward could be compiled (unchanged),
using no Fujitsu libraries with the CA-Realia II Workbench.....AND it
would compile error-free and execute identically to the one compiled
with Fujitsu COBOL?

This is difficult to believe.


Bob Wolfe, flexus
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 11)_

- **From:** nowitt@freedsl.com
- **Date:** 2000-07-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3963B407.C81A95FE@freedsl.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <3963746c.19812899@news.epix.net>`

```

>Bob Wolfe wrote:

(snip)

Debates are only healthy when the debating parties use diplomacy,
adhere to and mutually respect factual information provided by their
opponent and avoid speaking in generalities.  You have done none of
the above and it should be obvious in the replies you have received
from highly respected regular contributors to this newsgroup.

    By healthy I mean without hypocrisy.  Diplomats use diplomacy.
    Software Vendors should use facts and comparison charts
    provided by studies made by themselves not by "polished
     factual information provided by their opponent(s).  You know
    about bugs in Windows NT by other software vendors NOT by
    Microsoft!! Should these vendors use diplomacy? or use" factual information"
    provided by Microsoft??  Nooooo I don't think so.

    Now here is the reality:  from the smallest politician to the candidates
    for president all use diplomacy and preach diplomacy and advertise
    diplomacy, until election time!!!  Then and only then each one reveals
    "facts provided by studies made by themselves" NOT "mutually respect factual
     information provided by their opponent"  I challenge you to find an ounce
    of respect in their flaming campaign ads.  But there is a lot less hypocrisy
    toward each other during that election period.  Now THAT is what I call healthy!

    Respect is relative  One rarely respects what one does not  know or understand.

If it is not obvious to you yet, I suspect that many consider you to
be just a tad zealous in your belief.....zealots are rarely considered
credible.

        Not that I am religious but Moses, Jesus, Mohamet, would be
        considered zealots if they do today what they did in the past.

        Early believers of anything from religion to technology are always
        accused of being zealots by those who have the most to fear from
        their statements.

I have said it many times and will continue to say that in my opinion,
this newsgroup is a platform for the free exchange of ideas by
professional COBOL programmers.  While I appreciate the fact that your
strong opinions are based upon the fact that you are so religious in
your views, please remember that I will avoid debate in this forum
because the debate shouldn't come from a vendor, but from those who
utilize COBOL daily in their studies, occupations or hobbies.

    I am not a vendor of character ScreenIO, much impressed - I would be
    - and I was - using your word "zealous" about it.  Even today
    I would talk about it the way I talk about PowerCOBOL.

>I can say this.  Everyone has different motivations for using a
>particular compiler, screen handler or some other type of tool.
>
>        And I agree with you. Many people drive a Cadillac, a Mercedes, a Ferrari or
a Lexus.  Others
>        drive a VW or a ford Escort and are happy with what they got until one day
they have
>        the opportunity to drive a Cadillac, a Mercedes, a Ferrari or a Lexus. Then
is when they
>        will understand the difference and will be wishing for more "power" when they
go back to their
>        VW or a ford Escort.  In this context PowerCOBOL is simply the Lexus or a
Ferrari.

But you are making an incorrect assumption that everyone who drives a
car in the world wants horsepower or luxury.  This is simply not true.
I know many people who would sell a Mercedes or Lexus, if given to
them, and purchase a VW or Escort with the proceeds, simply because
they value economy, thrift, conservation and environmental
preservation than they value looking cool in front of their friends
and breaking the law by exceeding the speed limit.

        I do not make such an assumption.  If you have read the last sentence
        of the cars analogy I have wrote: "I agree also with you that some still would
not want
        to trade their VW for a Lexus or a Ferrari."

Diff'rent Strokes for Diff'rent Folks!

.....Sly and the Family Stone

>I can say this.  If the program you demonstrate on your web site is
>100% COBOL, then I challenge you to recompile it with any of the
…[10 more quoted lines elided]…
>        compile and execute error free if all of the above are certified ANSI
COBOL-85.

I'm afraid that I would have to see this to believe it.  Are you
saying that the COBOL source code for the application featured on the
web site which you directed us toward could be compiled (unchanged),
using no Fujitsu libraries with the CA-Realia II Workbench.....AND it
would compile error-free and execute identically to the one compiled
with Fujitsu COBOL?

This is difficult to believe.

        I reproduce here what I have said to Mr. Hubbell:

    O  The entire business and data validation/manipulation is written in ANSI-85
            o  The files manipulation central program (READ, WRITE, DELETE) is
               written in ANSI-85
            o  No use whatsoever of COMP-5, COMP-X , Level 78 etc..
            o  No use of INVOKE or any OO syntax
            o  No Fujitsu COBOL specific routines (i.e.. use INSPECT REPLACING instead
of
               to_upper / to_lower) functions
            o  Single program centralizing all SYSTEM CALLS (getdir, mkdir,etc).
               can be eliminated or modified easily)
            o  Reporting programs write to disk files which are redirected to print
               spooler.
            o  All data and parameters - user and system are passed using LINKAGE
SECTION
               to the CUI or GUI interface program. (in the case of CUI character
ScreenIO
               was used in the case of GUI, VB was used years ago but could not handle
the
               job very well.  Later COBOL GUI tools were evaluated and dropped
because of
               the Screen Oriented architecture of lack of features and flexibility.
               PowerCOBOL passed the test of the most complex GUI development in both
               availability of Controls and ease of integration of ActiveX and
execution
               speed and commendable stability).
               "Why flip all controls of a window as if you were looking at them in a
               mirror or move them from one place to another? you asked.  Well, go
back
               a take another look (this time do it slowly and from top to bottom) at
               http://www.ils-international.com/goldmine/newcobol.htm and you will
               see how the same application can run in USA, France, Brazil, Israel,
               India, Russia, Saudi Arabia or any other part of the world in the local

               native tongue.
               That is the power of forward thinking, that is the power of multi-use
in
               a multi-community of multi-users. It is called "Efficiency" and saves
               tons of bucks.  When NASA came up with the idea of the Space Shuttle,
               they stopped producing their wasteful one-launch monstrous rockets
               and they did save a lot of [taxpayer] money. Of course they find a way
               to waste some of it in other programs, but that is a different story.

       I hope again you were able to grasp the finesse of such design.

Bob Wolfe, flexus
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 12)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-07-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<K5R85.72$B5.74190@nnrp3.sbc.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <3960d382.18537475@news.epix.net> <39612B21.ADAE47D9@freedsl.com> <3963746c.19812899@news.epix.net> <3963B407.C81A95FE@freedsl.com>`

```

<nowitt@freedsl.com>

>     Now here is the reality:  from the smallest politician to the
candidates
>     for president all use diplomacy and preach diplomacy and
advertise
>     diplomacy, until election time!!!

Winston Churchill, early in his career, was electioneering on a stump
in Hyde Park, when a heckler shouted out: "Mr. Churchill, I'd sooner
vote for the devil than vote for you!"

Without missing a beat, Churchill rejoined: "And on Wednesday next,
you'll get the chance."
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 8)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-07-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39608B78.F9135625@zip.com.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com>`

```
nowitt@freedsl.com wrote:
> 
> I challenge Dialog, SpII and ScreenIO to even come close to doing this
> (http://www.ils-international.com/goldmine/newcobol.htm) as elegantly and as
> efficiently as it has been beautifully done using PowerCOBOL from Fujitsu.

I am note a power cobol expert but the little I have seen indicates
that it is a fundamentally bad design of code wizards.  A little
explanation is needed.

If you design an application in power cobol version xx and upgrade to
version xx+2 does your application magically take on the benefits of
the new release.  The answer is no because the code is generated
directly into the application.  This also means that bugs in version
xx will not automatically be corrected when you upgrade.

Windows needs to be hidden more behind called modules (or OO methods)
this means that the upgrades will automatically work.

Also putting so much code into the business space leads to a tight
interconnection between the screen and the business.  This is bad
design as we move from windows to Unix to other platforms much faster
now days.

The isolation of screenio and SPII gives it some benefits in this
regard.  A simple relink is the most that would be needed to correct
some flaw in the screen generation code.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 9)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-07-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8Cc85.121$Vp5.106025@nnrp1.sbc.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608B78.F9135625@zip.com.au>`

```

Ken Foskey <waratah@zip.com.au

>
> I am note a power cobol expert but the little I have seen indicates
…[3 more quoted lines elided]…
> If you design an application in power cobol version xx and upgrade
to
> version xx+2 does your application magically take on the benefits of
> the new release.  The answer is no because the code is generated
> directly into the application.  This also means that bugs in version
> xx will not automatically be corrected when you upgrade.

You're right. Upgrading from version "x" to version "y" doesn't do
anything for modules compiled under version "x." Upgrading from
COBOL65 to COBOL85 doesn't do anything for programs compiled under
COBOL65 either. Since the OO code in PowerCobol is, in fact, COBOL,
it's obvious that you must recompile to take advantage of new features
or bug fixes. This is not a big deal.

One small example: Version 5 of PowerCobol added word-wrap to text
boxes. In order for our programs to take advantage of the new feature,
we had to check an option box on the form designer and recompile the
programs. It seems to me this is no different than having COBOL65
programs and wanting to use in-line performs or reference
modification. I'd have to recompile with a newer compiler. If we
didn't need or want the word-wrap feature, there would be no need for
immediate recompilation.
>
> Windows needs to be hidden more behind called modules (or OO
methods)
> this means that the upgrades will automatically work.

Nah. Not if you didn't code for the new feature. In the case above, we
were able to discard our hand-crafted word-wrap routine and let
PowerCobol handle wrapping text lines. In the case of bugs, you may
have originally included circumvention code to handle a bug. Now that
the bug is gone, your circumvention code may become a bug!
>
> Also putting so much code into the business space leads to a tight
> interconnection between the screen and the business.  This is bad
> design as we move from windows to Unix to other platforms much
faster
> now days.

Not necessarily. It is possible in PowerCobol to put ALL the business
logic in mainline routines that are intersected by event procedures.

>
> The isolation of screenio and SPII gives it some benefits in this
> regard.  A simple relink is the most that would be needed to correct
> some flaw in the screen generation code.

Yep. I bet, however, that there are many, many more bugs in the
business logic code (necessitating a recompile plus link) than in the
proprietary screen routines (link only).
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 10)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3961D670.248927A4@zip.com.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608B78.F9135625@zip.com.au> <8Cc85.121$Vp5.106025@nnrp1.sbc.net>`

```
Jerry P wrote:
> 
> Ken Foskey <waratah@zip.com.au
…[18 more quoted lines elided]…
> or bug fixes. This is not a big deal.

You are missing the point.  What about if the bug is in the code that
the wizard generated for you, i.e. the cobol source?  Far to much code
is generated to use a feature and this is the problem.  You have
pointed out an instance where this is not the case but I am certain
that there are other cases as I describe.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 11)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ucn85.23$xP1.1447@nnrp2.sbc.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608B78.F9135625@zip.com.au> <8Cc85.121$Vp5.106025@nnrp1.sbc.net> <3961D670.248927A4@zip.com.au>`

```

Ken Foskey <waratah@zip.com.au
>
> You are missing the point.  What about if the bug is in the code
that
> the wizard generated for you, i.e. the cobol source?  Far to much
code
> is generated to use a feature and this is the problem.  You have
> pointed out an instance where this is not the case but I am certain
> that there are other cases as I describe.
>
I agree with your observation. PowerCOBOL treats my COBOL source code
almost as proto-code and passes my original source through the
equivalent of a precompiler. The result - which is finally handed to
the compiler - bears only a passing resemblence to the code I wrote.
If one is worried about a bug in the 'Wizard' (or precompiler), the
chance of that is, in my experience, vanishingly small. On the order
of a bug in the compiler itself or the Linkage Editor. Not to say
compler bugs can't happen, of course, but they're so far below the
radar, they're subterranean.

In my view, a bug in the PowerCOBOL 'Wizard' (if one exists and I hit
it) would be equivalent to a bug in the panel processor run-time of
SP2 or a bug in the compiler itself; I can wait for a fix from the
vendor or code around the problem.

That's my story, and I'm stickin' to it. If you beat me, I might
change my mind.

Jerry Peacock
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 12)_

- **From:** nowitt@freedsl.com
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39621680.3A872E84@freedsl.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608B78.F9135625@zip.com.au> <8Cc85.121$Vp5.106025@nnrp1.sbc.net> <3961D670.248927A4@zip.com.au> <Ucn85.23$xP1.1447@nnrp2.sbc.net>`

```
Jerry P wrote:
Ken Foskey <waratah@zip.com.au
>
> You are missing the point.  What about if the bug is in the code
that
> the wizard generated for you, i.e. the cobol source?  Far to much
code
> is generated to use a feature and this is the problem.  You have
> pointed out an instance where this is not the case but I am certain
> that there are other cases as I describe.
>
I agree with your observation. PowerCOBOL treats my COBOL source code
almost as proto-code and passes my original source through the
equivalent of a precompiler. The result - which is finally handed to
the compiler - bears only a passing resemblence to the code I wrote.
If one is worried about a bug in the 'Wizard' (or precompiler), the
chance of that is, in my experience, vanishingly small. On the order
of a bug in the compiler itself or the Linkage Editor. Not to say
compler bugs can't happen, of course, but they're so far below the
radar, they're subterranean.

        IF according to what you state above and your first comment "> >
I am note a power cobol
        expert but the little I have seen indicates that it is a
fundamentally bad design of code wizards.<<"
        AND if you are familiar with CICS, then CICS also "s a
fundamentally bad design of code wizards"

        Both CICS and PowerCOBOL are similar in concepts and
architectural design...

            1- Both handle online-user interface through interactive
screen the 1st character, the 2d graphical
            2- Both offer a screen design the 1st BMS (character, the 2d
PowerFORM editor (graphical)
            3- Both offer a screen layout code generator the 1st Symbolic
map, the 2d WS and Procedure code
            4- Both need COBOL user program(s) to get the data from the
user interface (CUI or GUI)
            and pass it to a procedure for validation/business processing
(within the same program of
            by CALLing another one.
            5- Both use a "Wizard" to transform the code written by the
programmer to more complex
            sets of statements,
                    -the 1st trough a "pre-compiler" transforms all
"clear" CICS code between
                    EXEC-CICS....END-EXEC to more "cryptic" COBOL
statements that few COBOL
                    programmers ever dared or cared to take a close look
at.  When modifications  or
                    enhancements are needed.  The programmer goes to the
original program source to
                    do the work NOT to the source code generated by the
pre-compiler and then
                    re-pre-compile and compile again!!

                    -the 2d through a "wizard"  transforms all "clear"
INVOKE statements, Windows controls
                    and "Windows Event" handling designed and coded
through PowerCOBOL forms/controls
                    "properties" and "methods"  to more "cryptic"
COBOL/WINAPI calls statements that COBOL
                    programmers really should NOT care to take a close
look at. When modifications  or
                    enhancements are needed.  The programmer should go to
PowerFORM tool to do the work
                    NOT to the source code generated by the PowerFORM
"wizard" and then click the
                    Project rebuild menu option to "re-generate
(re-pre-compile) and compile again!!

            So according to You Mr. Foskey and Mr. Peacock  IBM had it
aaaaalllllll wrong for over
            twenty years now.  Gee!  I wonder what it would take to have
IBM admit the incompetence
            of their CICS engineers and hire you to head their CICS
System team!!!  Not to mention that
            according to your statements the Fujitsu PowerCOBOL team is
also "headed by the same" type
            of people as IBM.

            ...but there are 2 major differences
                    -The 1st is "Screen based" hence "single event"
handling.
                    -The "pre-compiler" generates less COBOL code because
it only deals with a
                    24 x 80 character screen and only handle the event of
the "SEND" screen
                    triggered by ONE of the following: Enter key /
PA(1,2,3) key, CLEAR key,
                    PF1-24 keys, etc...

                    -The 2d is "Graphical" and is "Windows and Controls
based" hence "multiple events "
                    handling
                    -The "Wizard" generates a lot more COBOL code because
it has to create instances
                    of windows and ALL their controls (as opposed to 24 x
80) and has to handle all events
                    that NEED TO BE HANDLED for the user INCLUDING the
Event of the use of other
                    windows.  THIS IS BOUND to use more COBOL code.  I am
not 100% sure but I
                    believe there are around 480 Windows "Events"!!

In my view, a bug in the PowerCOBOL 'Wizard' (if one exists and I hit
it) would be equivalent to a bug in the panel processor run-time of
SP2 or a bug in the compiler itself; I can wait for a fix from the
vendor or code around the problem.

            Agree 100%!

That's my story, and I'm stickin' to it. If you beat me, I might
change my mind.

Jerry Peacock
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 13)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39622b6a.165895713@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608B78.F9135625@zip.com.au> <8Cc85.121$Vp5.106025@nnrp1.sbc.net> <3961D670.248927A4@zip.com.au> <Ucn85.23$xP1.1447@nnrp2.sbc.net> <39621680.3A872E84@freedsl.com>`

```
On Tue, 04 Jul 2000 16:51:10 GMT, nowitt@freedsl.com wrote:

>            So according to You Mr. Foskey and Mr. Peacock  IBM had it
>aaaaalllllll wrong for over
…[7 more quoted lines elided]…
>

You don't seem to know when to give up.  Even a cursory read of
Jerry's posts should lead you to realize that he has EXTENSIVE
PowerCOBOL experience and actually LIKES the product a great deal.  He
was AGREEING with you to some degree.

Can you please answer a question (Unrelated to the above observation).
With PowerCOBOL is there a single data area returned corresponding to
data on the "form" containing all of the data values under a single 01
level -- as is the case of a RECIEVE MAP with CICS?  This is a serious
query.
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 14)_

- **From:** "nowitt"@freedsl.com
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39624EF2.EDCB63D@freedsl.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608B78.F9135625@zip.com.au> <8Cc85.121$Vp5.106025@nnrp1.sbc.net> <3961D670.248927A4@zip.com.au> <Ucn85.23$xP1.1447@nnrp2.sbc.net> <39621680.3A872E84@freedsl.com> <39622b6a.165895713@207.126.101.100>`

```
nowitt@freedsl.com wrote:
Thane Hubbell wrote:
On Tue, 04 Jul 2000 16:51:10 GMT, nowitt@freedsl.com wrote:

>            So according to You Mr. Foskey and Mr. Peacock  IBM had it
aaaaalllllll wrong for over
>            twenty years now.  Gee!  I wonder what it would take to have IBM
admit the incompetence
>            of their CICS engineers and hire you to head their CICS System
team!!!  Not to mention that
>            according to your statements the Fujitsu PowerCOBOL team is also
"headed by the same" type
>            of people as IBM.
>

You don't seem to know when to give up.  Even a cursory read of
Jerry's posts should lead you to realize that he has EXTENSIVE
PowerCOBOL experience and actually LIKES the product a great deal.  He
was AGREEING with you to some degree.

        Yes. to some degree.  Some clarification was needed...


Can you please answer a question (Unrelated to the above observation).
With PowerCOBOL is there a single data area returned corresponding to
data on the "form" containing all of the data values under a single 01
level -- as is the case of a RECIEVE MAP with CICS?  This is a serious
query.

        This is a serious answer: NO. there is no "single data
        area returned corresponding to data on the "form"".  It is
        also as you know the way DIALOG works except that in DIALOG
        you have to include ALL the data areas under the DATABLOCK
        for all the windows in the screenset.

        In PowerCOBOL since it is a normal COBOL program generated,
        You have both WORKING-STORAGE and LINKAGE SECTION that you
        can use to pass back'n forth the data between the Windows
        controls (entry/multi lines fields, radio/check button values, etc.)

        For efficiency and unlike DIALOG, each "Form" can have its own
        field that you would define ONLY for the fields in THAT window
        and ONLY the one you want to display/accept data from.
        If a window is closed, then the storage is cleared as in any other
        COBOL program.

        In DIALOG if you have a screenset of 10 windows with a lot of fields
        that would require many many fields, "Deleting" a window does not
        release the memory and the entire DATABLOCK is kept until the
screenset is
        unloaded

        By the way you can also make a WS 01 level GLOBAL and also EXTERNAL
        to have the data block available within nested programs of between
        DLLs.  Its a great feature.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface - CICS

_(reply depth: 13)_

- **From:** Arnold Trembley <arnold.trembley@att.net>
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39623D75.6FC8C3EA@att.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608B78.F9135625@zip.com.au> <8Cc85.121$Vp5.106025@nnrp1.sbc.net> <3961D670.248927A4@zip.com.au> <Ucn85.23$xP1.1447@nnrp2.sbc.net> <39621680.3A872E84@freedsl.com>`

```
nowitt@freedsl.com wrote:
> (mucho snippo)
>         Both CICS and PowerCOBOL are similar in concepts and
…[3 more quoted lines elided]…
> screen the 1st character, the 2d graphical

What's this?  You can have SCREENS with CICS?  I don't believe it.  I've
written over a hundred CICS programs that don't use a screen of any
kind.
```

###### ↳ ↳ ↳ Re: Graphical User Interface - CICS

_(reply depth: 14)_

- **From:** nowitt@freedsl.com
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3962457D.934A4E2F@freedsl.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608B78.F9135625@zip.com.au> <8Cc85.121$Vp5.106025@nnrp1.sbc.net> <3961D670.248927A4@zip.com.au> <Ucn85.23$xP1.1447@nnrp2.sbc.net> <39621680.3A872E84@freedsl.com> <39623D75.6FC8C3EA@att.net>`

```
Arnold Trembley wrote:
nowitt@freedsl.com wrote:
> (mucho snippo)
>         Both CICS and PowerCOBOL are similar in concepts and
…[3 more quoted lines elided]…
> screen the 1st character, the 2d graphical

What's this?  You can have SCREENS with CICS?  I don't believe it.  I've
written over a hundred CICS programs that don't use a screen of any
kind.

        Yeah!  You used probably INVISIBLE INK to display the info to your
users now..
        shhhhhtt! and go back to sleep.
```

###### ↳ ↳ ↳ Re: Graphical User Interface - CICS

_(reply depth: 14)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39626433.180434361@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608B78.F9135625@zip.com.au> <8Cc85.121$Vp5.106025@nnrp1.sbc.net> <3961D670.248927A4@zip.com.au> <Ucn85.23$xP1.1447@nnrp2.sbc.net> <39621680.3A872E84@freedsl.com> <39623D75.6FC8C3EA@att.net>`

```
On Tue, 04 Jul 2000 19:41:00 GMT, Arnold Trembley
<arnold.trembley@att.net> wrote:

>nowitt@freedsl.com wrote:
>> (mucho snippo)
…[8 more quoted lines elided]…
>kind.

Actually, if you follow current IBM guidelines you are NOT supposed to
have screens anymore.  Instead you code these externally using the UI
of your choice and use ECI (External Communications Interface) to
speak with them via the Communications area.  You have just been ahead
of your time.
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 13)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-07-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39631655.A1A82D2D@zip.com.au>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <395FD244.C6A64190@freedsl.com> <39608B78.F9135625@zip.com.au> <8Cc85.121$Vp5.106025@nnrp1.sbc.net> <3961D670.248927A4@zip.com.au> <Ucn85.23$xP1.1447@nnrp2.sbc.net> <39621680.3A872E84@freedsl.com>`

```
nowitt@freedsl.com wrote:
> 
>         IF according to what you state above and your first comment "> >
…[82 more quoted lines elided]…
>                     believe there are around 480 Windows "Events"!!

I find your posts just about impossible to follow.  Could you please
put quotes on the original text to help us mere mortals follow what
you say as opposed to what the others are saying.

I have done CICS programming and typically the programs are 80% CICS
handling and about 20% business logic.   Yes this leads programmers
into bad designs.  I worked on a cobol system CHRIS (computer Human
Resource information system or like) and it magically hidden all this
complex stuff and the average program was 10% overhead and 90%
business.  It is possible to clean it up, just not easy to change the
programmers mind set.

I have stated my position and I have described the reasons for my
position, prove me wrong.  I hit the link you gave us, lots of pretty
pictures and no code.  Show me the money (or code in this case).

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 7)_

- **From:** mojo@chesapeake.net (Mike Madara)
- **Date:** 2000-07-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sm670npfgas18@corp.supernews.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100>`

```
Two quick questions:

1)   Are the Fujitsu GUI extensions to COBOL only in their Power Cobol
      product?  How 'bout their Standard Cobol?

2)   If you use Power Cobol as your GUI solution, must you also use
      their version of OO methodology?  I'm getting the impression 
      from the thread that in the Fujitsu product, GUI and OO (at 
      least their version) are tightly linked.  Correct?

TIA

Mike Madara
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 8)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39632608.230063290@207.126.101.100>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <sm670npfgas18@corp.supernews.com>`

```
On Wed, 05 Jul 2000 11:50:38 GMT, mojo@chesapeake.net (Mike Madara)
wrote:

>Two quick questions:
>
>1)   Are the Fujitsu GUI extensions to COBOL only in their Power Cobol
>      product?  How 'bout their Standard Cobol?
>

You can make direct API Calls with Standard COBOL if you desire.  As
far as GUI goes, Standard COBOL has a multitude of WEB extensions (v
5..0) but not native GUI.  For that you need POWERCOBOL or a third
party tool.

>2)   If you use Power Cobol as your GUI solution, must you also use
>      their version of OO methodology?  I'm getting the impression 
>      from the thread that in the Fujitsu product, GUI and OO (at 
>      least their version) are tightly linked.  Correct?

OO is how PowerCOBOL is implemented.  However, when you consider
"Fujitsu's Brand" of OO, you have to remember that the different
vendors coded to the standard at different times.  Fujitsu's OO
Implementation is actually much closer to the standard than any of the
other PC vendors.  

The OO Code is generated.  From my experience, when I experimented
with it, the code is actually quite well hidden and only visible when
you turn on debugging, or force source code listing generation.   

Fujitsu doesn't force you into OO programming.  They simply use OO to
facilitate PowerCOBOL -- and they hide it from you as much as
possible.  (Intentionally).
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 8)_

- **From:** nowitt@freedsl.com
- **Date:** 2000-07-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39636EA2.E6DAFE72@freedsl.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <sm670npfgas18@corp.supernews.com>`

```
Mike Madara wrote:
Two quick questions:

1)   Are the Fujitsu GUI extensions to COBOL only in their Power Cobol
      product?  How 'bout their Standard Cobol?

        Yes.  To design, prototype, compile, link, debug and execute GUI,
you
        need PowerCOBOL.

        The 3 editions of the Fujitsu COBOL products features can be found

        either at Fujitsu site(http://www.adtools.com/info/whatcobol.htm)
or
        at ILS Site (http://www.ils-international.com).  Prices can also
be
        found on those sites.

        In short :
        -ALL Standard, Professional and Enterprise Editions Support
         COBOL-74/85/95 and OO COBOL and web CGI support.

        -Pro Edition include PowerCOBOL for GUI and PowerBSORT OCX

        -Enterprise Include Pro Edition + Standalone PowerBSORT +
         Team development support (source control management software)
         + PowerFORM Reporting Tool (very similar to Crystal Reports)
         but works with COBOL.

2)   If you use Power Cobol as your GUI solution, must you also use
      their version of OO methodology?  I'm getting the impression
      from the thread that in the Fujitsu product, GUI and OO (at
      least their version) are tightly linked.  Correct?

        To use GUI development and manipulate the GUI Controls and
OCX/ActiveX,
        you use the "standard" [or hopefully soon to be approved standard
-
        nobody seem to be sure when would that be] OO COBOL INVOKE
statement
        to communicate with Objects and their properties created using the

        FBASE GUI class, the OCX and ActiveX controls.

        You can STILL use the existing standard COBOL-85 to develop and
CALL
        standard [procedural] COBOL programs for the
business/validation/data
        manipulation process under PowerCOBOL.

        Hope this answers your questions.

TIA

Mike Madara
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 9)_

- **From:** nowitt@freedsl.com
- **Date:** 2000-07-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396370BE.E2807273@freedsl.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com> <395f33b5.210878021@207.126.101.100> <#yJBo1C5$GA.293@cpmsnbbsa09> <395f4b08.216849388@207.126.101.100> <sm670npfgas18@corp.supernews.com> <39636EA2.E6DAFE72@freedsl.com>`

```
Sorry that was a typo I meant 97 not 95 it should read

        In short :
        -ALL Standard, Professional and Enterprise Editions Support
         COBOL-74/85/97 and OO COBOL and web CGI support.

nowitt@freedsl.com wrote:
Mike Madara wrote:
Two quick questions:

1)   Are the Fujitsu GUI extensions to COBOL only in their Power Cobol
      product?  How 'bout their Standard Cobol?

        Yes.  To design, prototype, compile, link, debug and execute GUI, you
        need PowerCOBOL.

        The 3 editions of the Fujitsu COBOL products features can be found
        either at Fujitsu site(http://www.adtools.com/info/whatcobol.htm) or
        at ILS Site (http://www.ils-international.com).  Prices can also be
        found on those sites.

        In short :
        -ALL Standard, Professional and Enterprise Editions Support
         COBOL-74/85/95 and OO COBOL and web CGI support.

        -Pro Edition include PowerCOBOL for GUI and PowerBSORT OCX

        -Enterprise Include Pro Edition + Standalone PowerBSORT +
         Team development support (source control management software)
         + PowerFORM Reporting Tool (very similar to Crystal Reports)
         but works with COBOL.

2)   If you use Power Cobol as your GUI solution, must you also use
      their version of OO methodology?  I'm getting the impression
      from the thread that in the Fujitsu product, GUI and OO (at
      least their version) are tightly linked.  Correct?

        To use GUI development and manipulate the GUI Controls and
OCX/ActiveX,
        you use the "standard" [or hopefully soon to be approved standard -
        nobody seem to be sure when would that be] OO COBOL INVOKE statement
        to communicate with Objects and their properties created using the
        FBASE GUI class, the OCX and ActiveX controls.

        You can STILL use the existing standard COBOL-85 to develop and CALL
        standard [procedural] COBOL programs for the business/validation/data
        manipulation process under PowerCOBOL.

        Hope this answers your questions.

TIA

Mike Madara
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 4)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-07-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jnfh6$nt7$1@nnrp1.deja.com>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com>`

```

>
> You are free to believe it is a great product, but it is anything
> but easy to use.  Your code becomes so entangled with the
> windows interface that you might as well write in C++.


Hi:

Having used SP2 for more than three years and having converted
more than a quarter-million lines of COBOL, I don't agree with
the above. After all, it really depends on how you use SP2 and
how you stick the required SP2 code into your program. Anybody
could mess that up, perhaps you did?

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Graphical User Interface

_(reply depth: 4)_

- **From:** flexus@epix.net (Bob Wolfe)
- **Date:** 2000-07-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39609d41.4646343@news.epix.net>`
- **References:** `<3954e87b.7733996@allnews.nbnet.nb.ca> <20000624140646.03037.00000326@ng-fd1.aol.com> <sltgf29dop3112@corp.supernews.com>`

```
Dear JSA:

Perhaps I am making an incorrect assumption, but I believe that you
are John Andersen with Norcom, the developers of GUI Screenio,
correct?

If I am incorrect, please forgive me.

But if this is correct, I'm not sure if the COBOL newsgroup is a good
place to start a vendor to vendor flame war.

You are entitled to your opinions regarding our products.  Whether
they are easy to use or difficult to use is generally a matter of
personal preference.  I know programmers who consider WinAPI
programming easy, but I'm not sure if I share their opinion.

Certainly the Norcom Screenio product is a good user interface
development tool and should be recognized as such.

But it is my belief that the COBOL newsgroup is not the appropriate
place to engage in a product flame war, especially between competing
vendors.  These debates are better conducted between the end users.
From time to time, vendors should add their comments in order to
correct inaccuracies or provide suggestions.  I doubt that the regular
newsgroup readers/participants want to see a vendor flame war...it's
quite unproductive.

Therefore I will only make the comment that your statement below is
incorrect.

Both sp2 and screenio utilze a CALL USING approach to screen handling.
None of our products require knowledge of the WinAPI, even when
implementing Active X controls, displaying JPG bitmaps, printing
through the Windows Print Manager, running remotely across TCP/IP or
displaying screens directly in the child window of a web browser.
Everything is accomplished with COBOL CALL USING statements, just like
Screenio.

If you wish to debate this through private e-mail, I would be happy to
do so, but as a vendor, I avoid debating these issues directly in the
newsgroup, simply because I don't want to use this forum as a sales or
promotional platform.

"JSA" <jsa@kona.penguinpowered.com> wrote:

>In article <20000624140646.03037.00000326@ng-fd1.aol.com>, bob7536@aol.com
>(Bob7536) wrote:
…[16 more quoted lines elided]…
>

Bob Wolfe, flexus
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
