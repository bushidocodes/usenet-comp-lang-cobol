[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# AS/400 to Semi-GUI recommendations

_19 messages · 12 participants · 2000-04_

**Topics:** [`AS/400, iSeries, RPG`](../topics.md#as400)

---

### AS/400 to Semi-GUI recommendations

- **From:** Dutch Owen <dutch@sysun.com>
- **Date:** 2000-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OVGJ4.11701$x62.59006@typhoon.southeast.rr.com>`

```
     I'm a consultant and experienced COBOL programmer, also familiar
with the windows API and GUI.  I have a client who has a large-scale
mainly COBOL-based application running on the AS/400.  Management now
wants this application ported to the PC environment, with the main
requirement being that the formerly green-screen interactive programs
now look nice on the Windows platform.  They want to save as much
code as possible, and for the system design and operation of the 
programs to remain as close as possible to the original; it seems
the main goal is to 1) run on Windows, and 2) look like a Windows
app without actually buying into the expensive redesign and rewrite
necessary to give real GUI functionality.

     What I'm asking for is any recommendations on the best approach
to take, and what tools might be best for this project.  I've used
MicroFocus COBOL years ago, and we're getting a copy of Net Express
to evaluate.  I've also looked at the websites for tools like SP2.
But I have no real experience trying to graft what I would call a
Semi- or fake GUI onto a character based app.  I don't even know if
it's a practical idea, but it sounds like others may have tried 
before us and do know.

     To be a bit more precise, I think that screen formats with the fields
in similar locations to the original, but with nice colors and pretty fonts
and maybe a picture here and there, plus a few very restricted uses of real
GUI-type objects uses as a combobox for code lookups is what they are
looking for.  They don't want to transform a 1980s app into QuickBooks Pro,
they just want it to look good enough to sell without the prospects cringing
when they see the green screens.

     Recommendations to a) stay with green-screen, or b) go all the 
way and redesign for a proper GUI are not helpful, as management is
not interested in either of those options.

    Thanks for any advice /warnings / war stories, etc.

    Dutch
```

#### ↳ Re: AS/400 to Semi-GUI recommendations

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8d7lqe$ghj$1@news.cerf.net>`
- **References:** `<OVGJ4.11701$x62.59006@typhoon.southeast.rr.com>`

```
"Dutch Owen" <dutch@sysun.com> wrote in message
news:OVGJ4.11701$x62.59006@typhoon.southeast.rr.com...
>      I'm a consultant and experienced COBOL programmer, also familiar
> with the windows API and GUI.  I have a client who has a large-scale
…[8 more quoted lines elided]…
> necessary to give real GUI functionality.

I have no experience in porting from character AS400 Cobol to gui Cobol on
Windows, so I can't help you there, but there is one statement of yours,
that I paid attention to, that is that your management want to save as much
code as possible. By saying that you are narrowing down the path quite a
bit. To my knowledge, there is only one Cobol that allows GUI programming
with Cobol "like" syntax, that is Acucobol. For instance, to display a
combo-box you would do:

    DISPLAY COMBO-BOX LINE 5 COL 3 USING MY-DATA.

A push button:

    DISPLAY PUSH-BUTTON LINE 10 COL 15 SIZE 5 TITLE "Click" SELF-ACT.

An entry field:

    DISPLAY ENTRY-FIELD AT 0705 SIZE 30 USING MY-ENTRY UPPER.

This syntax may be used in procedure division or screen section, you may
have BEFORE, AFTER, EXCEPTION procedures, using events if you like. ACCEPT
is how you get your data and of course, it displays GUI. Most of it is
directly portable to character interface, in the event something is not, you
may specify two editions with the same name in your screen section
separating it using the reserved words CHARACTER and GRAPHICAL, the runtime
will then choose the appropriate instance.
To check it out, take a look at www.acucorp.com

You also got the option of using an external form utility, like FormSP,
which also will preserve most of your logic.

I may be wrong, but I believe that using Fujitsu or Micro Focus will require
OO programming to get GUI, for RM Cobol I don't know.

I am certain I will stay corrected if I am wrong.

Cheesle
```

#### ↳ Re: AS/400 to Semi-GUI recommendations

- **From:** terrywin.nospam@pronetisp.net (Terry Winchester)
- **Date:** 2000-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38f888d5.3077206@news.pronetisp.net>`
- **References:** `<OVGJ4.11701$x62.59006@typhoon.southeast.rr.com>`

```

On Fri, 14 Apr 2000 15:36:14 GMT, Dutch Owen <dutch@sysun.com> wrote:

>     I'm a consultant and experienced COBOL programmer, also familiar
>with the windows API and GUI.  I have a client who has a large-scale
…[33 more quoted lines elided]…
>    Dutch

Cheesle's suggestion may meet your needs but IMHO it will require a
fair amount of work to convert the 5250 display file code/logic.  I
also work on an AS/400 and have yet to find anything that does all
that you want (or I want for that matter) in a *painless* way.

You might try looking at 5250 screen scrapers.  There seems to be
quite a few of them (try AS400Network.com), but, since you indicated
that your "selling" the software you'd have to make sure could bundle
the third party screen scraper package with yours at a reasonable cost
(which seems unlikely).

And of course you also have "workstation gateway" as a GUI option 
via a browser - but this is not a viable solution for anyone IMHO.

(If it was RPG you could have used Visual Age RPG & Code400 -- yuck!)


Good Luck, you're going to need it.

Terry
```

#### ↳ Re: AS/400 to Semi-GUI recommendations

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F78DD4.917CAED7@home.com>`
- **References:** `<OVGJ4.11701$x62.59006@typhoon.southeast.rr.com>`

```


Dutch Owen wrote:
> 
>      I'm a consultant and experienced COBOL programmer, also familiar
…[34 more quoted lines elided]…
>     Dutch

Well Cheesle offers one possible solution. Based on what you've written,
may we assume you are using Screen Section ? Whether you choose Acu,
Fujitsu or NetExpress, to achieve that 'Windows look alike', probably
your best approach is use SP2.

I'm copying to Thane so that he can make observations/recommendations. 
Assuming Screen Section, SP2 would allow you a typical structured
approach returning 'Windows' values to your structured. Now how tricky
it would be converting your screen code to SP2 'send/receive syntax' I
have no idea - perhaps Thane can e-mail you with an old Screen Section
program converted to SP2.

If you choose NetExpress you can still use SP2; don't attempt OO/GUIs or
Dialog System as they represent what you are trying to avoid - a new
learning curve. I'm not familiar with Fujitsu but if you are proficient
in APIs - then you could also use these in NetExpress - but I would
doubt that gives a quick switchover from Screen Section to Windows
style.

It goes without saying - nothing is quite as simple as it seems :-) Good
luck.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: AS/400 to Semi-GUI recommendations

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38fb8571.31313288@news.cox-internet.com>`
- **References:** `<OVGJ4.11701$x62.59006@typhoon.southeast.rr.com> <38F78DD4.917CAED7@home.com>`

```
On Fri, 14 Apr 2000 22:18:08 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>
>I'm copying to Thane so that he can make observations/recommendations. 
…[5 more quoted lines elided]…
>

I'm thinking he is using SDA (Screen Design Aid) in which case he is
familiar with the WYSIWYG concept of the Sp2 panel editor.  SDA
operates with "calls" just like Sp2.  It should be an easy transition.
That said, my acticle in IEEE software shows a Screen Section
converted to SP2.
```

#### ↳ Re: AS/400 to Semi-GUI recommendations

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8d878u$f53$1@nnrp1.deja.com>`
- **References:** `<OVGJ4.11701$x62.59006@typhoon.southeast.rr.com>`

```
In article <OVGJ4.11701$x62.59006@typhoon.southeast.rr.com>,
  Dutch Owen <dutch@sysun.com> wrote:
>      What I'm asking for is any recommendations on the best approach
> to take, and what tools might be best for this project.
>     Dutch
>
>

Hi:

You mentioned that this was software 'to sell'. I know from experience
that selling that old-fashioned stuff is hard to do.

I converted four applications in MF COBOL from DOS to Windows and
used SP2.

I would recommend it highly.  You can keep your programs working
just the same way, but give them Windows-like appearances and
they will run under Windows just fine.

Try it, you'll like it.

If you want to know more, just email me.


Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: AS/400 to Semi-GUI recommendations

- **From:** "Costas Giannoulis" <diavasi@otenet.gr>
- **Date:** 2000-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8d9jv6$4d4$1@newssrv.otenet.gr>`
- **References:** `<OVGJ4.11701$x62.59006@typhoon.southeast.rr.com>`

```

Hi,

First of all - as SFF5KEY points out - a great factor is how interface,
business logic and data managment (database or file handling) are mixed up.
From my experience, if the application uses screen section then  a tool like
SP2  may be a nice solution. On the other hand if you use standard
accept/display syntax mixed up with business logic then things are more
difficult.

Another thing is the time period you have to deliver the project. If you
have a logical time available (it depends on the complexity of the
application), i suggest you to redesign the application and if you can,
depending on the people will work you, have a look to OOD's way. This would
be a great step but the final project will be a powerful application with
reusable components. Not just another gui application.

As you wrote, managment decided to transfer the application on windows
environment. What about  if after 1 year managment decides to convert the
same programs into an Internet/Intranet based application ? Or what about if
they decide to change the data storage mechanism ?
You will rewrite the whole application having some versions of business
logic ?

I believe you should take a decision based on the  future plans (and the
future market), not only the gui appearance ....

Good luck
Costas

Dutch Owen <dutch@sysun.com> wrote in message
news:OVGJ4.11701$x62.59006@typhoon.southeast.rr.com...
>      I'm a consultant and experienced COBOL programmer, also familiar
> with the windows API and GUI.  I have a client who has a large-scale
…[20 more quoted lines elided]…
> in similar locations to the original, but with nice colors and pretty
fonts
> and maybe a picture here and there, plus a few very restricted uses of
real
> GUI-type objects uses as a combobox for code lookups is what they are
> looking for.  They don't want to transform a 1980s app into QuickBooks
Pro,
> they just want it to look good enough to sell without the prospects
cringing
> when they see the green screens.
>
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: AS/400 to Semi-GUI recommendations

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38fb7114.22089016@news.epix.net>`
- **References:** `<OVGJ4.11701$x62.59006@typhoon.southeast.rr.com> <8d9jv6$4d4$1@newssrv.otenet.gr>`

```
"Costas Giannoulis" <diavasi@otenet.gr> wrote:

>
>Hi,
…[6 more quoted lines elided]…
>difficult.

Costas:

Actually, Metro Information Services' Nashville, TN office has created
a number of character mode to GUI conversion tools (including
accept/display to sp2).  Some of these tools are fully automated and
others only partially convert the code.

We didn't write the conversion tools, or else I could tell you a
little more about them.  You can contact Metro from the link on our
home page at www.flexus.com.  They currently have tools for converting
the following:

screen section to sp2
display/accept to sp2
Wang COBOL to sp2
mbp Visual COBOL SMS (now called Micro Focus Visual COBOL) to sp2
IBM CICS BMS Macros to sp2

I may be forgetting about one or two, but they are very talented in
the area of user interface conversion.

>Another thing is the time period you have to deliver the project. If you
>have a logical time available (it depends on the complexity of the
…[8 more quoted lines elided]…
>they decide to change the data storage mechanism ?

Then they can use our Thin Client or Web Client product to use the
same source program and same screen definitions to deploy the
application across the 'net as a web browser based client app or a
non-web browser based internet app.

The file handling should also be separated from thebusiness logic if
at all possible.

>You will rewrite the whole application having some versions of business
>logic ?

Not necessarily.  Our philosophy is that you should always maintain
only one set of source code regardless of where you need to deploy
your user interface.

>I believe you should take a decision based on the  future plans (and the
>future market), not only the gui appearance ....

I agree 100%

[snip Dutch's original posting]
Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: AS/400 to Semi-GUI recommendations

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000415002923.12346.00000593@nso-fc.aol.com>`
- **References:** `<OVGJ4.11701$x62.59006@typhoon.southeast.rr.com>`

```
In article <OVGJ4.11701$x62.59006@typhoon.southeast.rr.com>, Dutch Owen
<dutch@sysun.com> writes:

>     What I'm asking for is any recommendations on the best approach
>to take, and what tools might be best for this project.  I've used
…[6 more quoted lines elided]…
>

I cannot speak from experience on this issue.  From what I have
read about here, there are several options for handling your screen
design processes (VB, Delphi, Java, SP2, CaseGen, Win32API).  
It all depends on how tightly your screen interaction code is laced 
thru your program logic.  If the screen build/present/response 
functions are broken out into separate parts, it should be fairly easy 
to design your screens with one of these tools and replace the 
perform with a call of the Screen module/DLL/whatever.
Unfortunately, a lot of these 'simple' things appear easy at the outset
and you later find a snake's nest once you are knee-deep into the 
process.
```

#### ↳ Re: AS/400 to Semi-GUI recommendations

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38fb6d5a.21135102@news.epix.net>`
- **References:** `<OVGJ4.11701$x62.59006@typhoon.southeast.rr.com>`

```
Dutch Owen <dutch@sysun.com> wrote:

>     I'm a consultant and experienced COBOL programmer, also familiar
>with the windows API and GUI.  I have a client who has a large-scale
…[17 more quoted lines elided]…
>before us and do know.

Dutch:

sp2 does indeed directly invoke Windows API functions in order to
display GUI screens, therefore it is a real GUI screen which is
displayed.

The same situation applies regardless of whether you are speaking
about any other approach or toolset unless of cource you are directly
invoking the Windows API functions from the COBOL application.....this
can get a bit complex and messy.

I suspect that you will get a number of different recommendations from
a variety of people in this group, but preserving your business logic
and replacing the front end is indeed a wonderful idea.

You need to determine how much work is involved in separating the user
interface logic from the business logic.  If the screen handling in
the existing application is indeed isolated from the bulk of the
application, it may be a simple task.  If it is intertwined in every
program, it may be difficult.

We have assisted a lot of customers in making this transition.
Perhaps you can provide a bit more detail on how the screens are
displayed currently from the COBOL application.  This is important in
helping to make a determination as to the "path of least resistance."

>     To be a bit more precise, I think that screen formats with the fields
>in similar locations to the original, but with nice colors and pretty fonts
…[4 more quoted lines elided]…
>when they see the green screens.

That is generally the most desireable approach.  Later, the GUI
screens can be enhanced with additional features.  If the conversion
can be automated or partially automated, then that's even better.  Let
us know how the screens are currently displayed.  Depending upon your
current approach, one of my customers may be able to supply you with
an more automated approach to conversion.

>     Recommendations to a) stay with green-screen, or b) go all the 
>way and redesign for a proper GUI are not helpful, as management is
…[5 more quoted lines elided]…
>

Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

##### ↳ ↳ Re: AS/400 to Semi-GUI recommendations

- **From:** khansen@screenio.com (Kevin Hansen)
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38fb7645.358180836@wingate>`
- **References:** `<OVGJ4.11701$x62.59006@typhoon.southeast.rr.com> <38fb6d5a.21135102@news.epix.net>`

```

Dutch,

We've had many folks convert mainframe applications to the PC; it's
eminently practical.    Our new GUI ScreenIO completely isolates you
from the Windows side of the issue so that you can concentrate on your
business logic.

We can probably even import your panels into GUI format if they in any
way resemble SDA format.

You can download our GUI ScreenIO from our website and try it; it's
written completely in itself and COBOL so it gives you some idea of
how we work and what we can do.  Questions/comments are welcome, and
we're glad to provide excellent technical support on evaluations as
well.

http://www.screenio.com

Kevin 

>Dutch Owen <dutch@sysun.com> wrote:
>
…[10 more quoted lines elided]…
>>necessary to give real GUI functionality.

NORCOM COBOL Programming Tools
GUI ScreenIO; a cool COBOL/Windows Screen Manager
http://www.ScreenIO.com
```

##### ↳ ↳ Re: AS/400 to Semi-GUI recommendations

- **From:** jets@nbnet.nb.ca (Tony M. Mina)
- **Date:** 2000-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38fbecde.44550112@allnews.nbnet.nb.ca>`
- **References:** `<OVGJ4.11701$x62.59006@typhoon.southeast.rr.com> <38fb6d5a.21135102@news.epix.net>`

```
This is exactly what we are doing now.  We are converting the green
screen to GUI using SP2 from Flexus.  The only difference is that ours
is a Unisys 2200 Clearpath mainframe.  On the client side we use Fujitsu
Cobol and on the mainframe side it is the same as Cobol.  The only thing
we are doing on the mainframe side is to remove the screen processing.
The business rules are intact.  We also replaced our form printing on
the mainframe with FormPrint from Flexus.

So far the conversion is very easy since we are not changing the
business rules.  We are averaging 1 program a day and this includes
cleanups as well.

Tony M. Mina




On Mon, 17 Apr 2000 20:13:08 GMT, rtwolfe@flexus.com (Bob Wolfe) wrote:

>Dutch Owen <dutch@sysun.com> wrote:
>
…[74 more quoted lines elided]…
>
```

##### ↳ ↳ Re: AS/400 to Semi-GUI recommendations

- **From:** Dutch Owen <dutch@sysun.com>
- **Date:** 2000-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QL3L4.7683$cZ.14629@typhoon.southeast.rr.com>`
- **References:** `<OVGJ4.11701$x62.59006@typhoon.southeast.rr.com> <38fb6d5a.21135102@news.epix.net>`

```
Bob Wolfe <rtwolfe@flexus.com> wrote:

> I suspect that you will get a number of different recommendations from
> a variety of people in this group, but preserving your business logic
> and replacing the front end is indeed a wonderful idea.

  There are too many replies to answer them all, but I'd like to
thank everyone who responded to my query.

  To answer a few questions that were asked, our application was
designed from the ground up to separate user interface, database
access, and business logic.  This principle has eroded a bit in
recently written programs by new programmers, but generally all
I/O whether database or screen is in copybooks.  This will ease the
conversion greatly.

  I got several offers to help us convert or to do the conversion
for us -- that's not what we are looking for at all, we *are*
consultants, and can convert it ourselves, I'm just looking for 
the best target platform to shoot for, and hoping to avoid false
starts.

  After considering our options and all advice, we are going to
do an experimental move of a small portion of the app to MF Net
Express using the built-in GUI tools, and if that turns out to
be inadequate we'll consider using something like SP2 to help.
One of the reasons for this decision is that many of the staff
members have experience with MF cobol.


  Thanks again for all your suggestions,
         Dutch
```

###### ↳ ↳ ↳ Re: AS/400 to Semi-GUI recommendations

- **From:** jets@nbnet.nb.ca (Tony M. Mina)
- **Date:** 2000-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38fd1342.44957930@allnews.nbnet.nb.ca>`
- **References:** `<OVGJ4.11701$x62.59006@typhoon.southeast.rr.com> <38fb6d5a.21135102@news.epix.net> <QL3L4.7683$cZ.14629@typhoon.southeast.rr.com>`

```
On Tue, 18 Apr 2000 20:41:20 GMT, Dutch Owen <dutch@sysun.com> wrote:

>Bob Wolfe <rtwolfe@flexus.com> wrote:
>
…[26 more quoted lines elided]…
>
You can still use MF Cobol with SP2.  We were on the same situation when
we converted our systems to GUI.  We were using MF Workbench that time.
Instead of going to NET Express we went with SP2 for the reason that it
supports different compilers.  I don't  know with Net Express if you can
move the codes to another compiler.  In our case when we moved to
Fujitsu there were only minor changes to the programs.  Mostly are
syntax related.  No changes to the SP2 codes were made. 


>  Thanks again for all your suggestions,
>         Dutch

Tony M. Mina
```

###### ↳ ↳ ↳ Re: AS/400 to Semi-GUI recommendations

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38fdc89d.10812325@news.cox-internet.com>`
- **References:** `<OVGJ4.11701$x62.59006@typhoon.southeast.rr.com> <38fb6d5a.21135102@news.epix.net> <QL3L4.7683$cZ.14629@typhoon.southeast.rr.com>`

```
On Tue, 18 Apr 2000 20:41:20 GMT, Dutch Owen <dutch@sysun.com> wrote:


>  After considering our options and all advice, we are going to
>do an experimental move of a small portion of the app to MF Net
…[4 more quoted lines elided]…
>

One small suggestion.  Do two experiments instead of one.  Use the
built in MF tools for one, and sp2 for the other.  Do the same
conversion in both experiments.  Then decide!
```

###### ↳ ↳ ↳ Re: AS/400 to Semi-GUI recommendations

_(reply depth: 4)_

- **From:** khansen@screenio.com (Kevin Hansen)
- **Date:** 2000-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38fdead5.94234351@wingate>`
- **References:** `<OVGJ4.11701$x62.59006@typhoon.southeast.rr.com> <38fb6d5a.21135102@news.epix.net> <QL3L4.7683$cZ.14629@typhoon.southeast.rr.com> <38fdc89d.10812325@news.cox-internet.com>`

```
On Wed, 19 Apr 2000 14:55:38 GMT, thaneH@softwaresimple.com (Thane
Hubbell) wrote:

>On Tue, 18 Apr 2000 20:41:20 GMT, Dutch Owen <dutch@sysun.com> wrote:
>
…[12 more quoted lines elided]…
>

How about three?  Try GUI ScreenIO, too.  You'll find it quite
straightforward...

Kevin


NORCOM COBOL Programming Tools
GUI ScreenIO; a cool COBOL/Windows Screen Manager
http://www.ScreenIO.com
```

###### ↳ ↳ ↳ Re: AS/400 to Semi-GUI recommendations

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38FE3277.A47A33D9@home.com>`
- **References:** `<OVGJ4.11701$x62.59006@typhoon.southeast.rr.com> <38fb6d5a.21135102@news.epix.net> <QL3L4.7683$cZ.14629@typhoon.southeast.rr.com> <38fdc89d.10812325@news.cox-internet.com> <38fdead5.94234351@wingate>`

```


Kevin Hansen wrote:
> 
> On Wed, 19 Apr 2000 14:55:38 GMT, thaneH@softwaresimple.com (Thane
…[20 more quoted lines elided]…
> 
You guys are really trying to make it easy for him. How about 4 - try
AcuCOBOL "dual screen section", How about 5 - ....................

Dutch make sure their suggestions don't make you go double-Dutch :-)

Jimmy
```

#### ↳ Re: AS/400 to Semi-GUI recommendations

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38fb850f.31214922@news.cox-internet.com>`
- **References:** `<OVGJ4.11701$x62.59006@typhoon.southeast.rr.com>`

```
On Fri, 14 Apr 2000 15:36:14 GMT, Dutch Owen <dutch@sysun.com> wrote:

>     I'm a consultant and experienced COBOL programmer, also familiar
>with the windows API and GUI.  I have a client who has a large-scale
…[9 more quoted lines elided]…
>

Do you use SDA?

If so, a conversion using Sp2 should be fairly painless.  The
approaches are similar.
```

#### ↳ Re: AS/400 to Semi-GUI recommendations

- **From:** "Anton" <a.rusbach@coss.nl>
- **Date:** 2000-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dmdb7$d6j$1@news1.xs4all.nl>`
- **References:** `<OVGJ4.11701$x62.59006@typhoon.southeast.rr.com>`

```
Do you know the product AXWare? (http://www.axware.com/)

Our company has transformed a banking application using this product, the
results are great!

kind regards,
Anton Rusbach

Dutch Owen <dutch@sysun.com> schreef in berichtnieuws
OVGJ4.11701$x62.59006@typhoon.southeast.rr.com...
>      I'm a consultant and experienced COBOL programmer, also familiar
> with the windows API and GUI.  I have a client who has a large-scale
…[20 more quoted lines elided]…
> in similar locations to the original, but with nice colors and pretty
fonts
> and maybe a picture here and there, plus a few very restricted uses of
real
> GUI-type objects uses as a combobox for code lookups is what they are
> looking for.  They don't want to transform a 1980s app into QuickBooks
Pro,
> they just want it to look good enough to sell without the prospects
cringing
> when they see the green screens.
>
…[7 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
