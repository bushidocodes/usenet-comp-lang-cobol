[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Pseudo conversational future

_14 messages · 11 participants · 2000-01 → 2000-02_

---

### Pseudo conversational future

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387642BD.256B4EAF@NOSPAMwebaccess.net>`

```
Mainframes have been using pseudo conversational dialogs since forever. 
PCs haven't needed to release resources while waiting for the user to
think.

COBOL dialogs have been written for these two environments.

Is this distinction going to go away from programs as operating systems
handle it?  How do people convert from one system to the other?
```

#### ↳ Re: Pseudo conversational future

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qfyd4.4727$ps.55697@news4.mia>`
- **References:** `<387642BD.256B4EAF@NOSPAMwebaccess.net>`

```
FIrst off the Operating System DOESN'T handle it on PCs or Unix Servers w/
workstations.
The Client Apps must invoke a system API call to RELEASE/RETURN temporary
control to the OS.  Otherwise your app is a 'system hog' just as a
conversational
system is on a Mainframe.
Howard Brazee <brazee@NOSPAMwebaccess.net> wrote in message
news:387642BD.256B4EAF@NOSPAMwebaccess.net...
> Mainframes have been using pseudo conversational dialogs since forever.
> PCs haven't needed to release resources while waiting for the user to
…[5 more quoted lines elided]…
> handle it?  How do people convert from one system to the other?
```

#### ↳ Re: Pseudo conversational future

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#BLefGgW$GA.248@cpmsnbbsa03>`
- **References:** `<387642BD.256B4EAF@NOSPAMwebaccess.net>`

```
 CICS is, by its nature, a pseudo-conversational environment.  Will it
change?  No!

I think that what you are asking is: "With the continual increase in storage
and CPU power is it still necessary to endure the performance degradation
inherent in managing such an environment?"

My opinion is that some of the facilities provided are no longer needed.  I
doubt that I will ever manage the allocation of storage in new development.
Another feature that I feel is obsolete is storage allocated to a terminal
device.

If you don't use a facility the system does not have to administer it.

Storage allocation was necessary in the past.  However, since storage is in
abundance it seems ludicrous to manage it.

Terminal devices, green-screens, are also on the way out.  With TCP/IP
running in CICS their is no terminal device, and therefore there is no
storage available as terminal storage.  With green-screen presentations
being replaced with GUI desktop presentations, it would seem that the path
to the GUI presentation is clearer if I do not use terminal storage.


Howard Brazee <brazee@NOSPAMwebaccess.net> wrote in message
news:387642BD.256B4EAF@NOSPAMwebaccess.net...
> Mainframes have been using pseudo conversational dialogs since forever.
> PCs haven't needed to release resources while waiting for the user to
…[5 more quoted lines elided]…
> handle it?  How do people convert from one system to the other?
```

#### ↳ Re: Pseudo conversational future

- **From:** theodp@aol.com (Theo DP)
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000107204557.02664.00000553@ng-fr1.aol.com>`
- **References:** `<387642BD.256B4EAF@NOSPAMwebaccess.net>`

```
>Subject: Pseudo conversational future
>From: Howard Brazee brazee@NOSPAMwebaccess.net 
…[16 more quoted lines elided]…
>

Everything old is new again...

Web "Stateless" = Mainframe Pseudoconversational

Both yield attrocious results, IMHO...
```

#### ↳ Re: Pseudo conversational future

- **From:** "George McGinn" <gmcginn@home.com>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XLSd4.71$dG.1818@ha1>`
- **References:** `<387642BD.256B4EAF@NOSPAMwebaccess.net>`

```
When Windows came out, programming with languages like Visual Basic allowed
for Event-Driven Software to be developed.  Resources are not allocated
until they are needed and are released when the event is completed.  So if
your terminal is waiting for your user to input data to the screen, there is
no event processing.

If you are talking about CICS emulation on a PC, you still will have a CICS
Environment running.  This is the same as on the Mainframe.  In that case,
then no, certain resources on the PC will not be released, as the CICS
Emulator needs to be active.

Best thing to do is to use a GUI like VB and link to COBOL programs when the
event is requested.  Your program runs and ends.  The event should end with
the termination of the COBOL program.

If you want to keep your legacy code and still take advantage of a GUI-style
system, use a platform like VB or some other GUI system to do all your
screen and screen edits (Numeric, Range and Acceptable Value checking) and
call your legacy COBOL programs to do your processing.  This way, when you
need to change the GUI or want your application to run on different
platforms, then your "core application" does not need to change - just your
front end interfaces.


George McGinn
Systems Engineer
GTE-TSI


Howard Brazee <brazee@NOSPAMwebaccess.net> wrote in message
news:387642BD.256B4EAF@NOSPAMwebaccess.net...
> Mainframes have been using pseudo conversational dialogs since forever.
> PCs haven't needed to release resources while waiting for the user to
…[5 more quoted lines elided]…
> handle it?  How do people convert from one system to the other?
```

##### ↳ ↳ Re: Pseudo conversational future

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eu44kIqW$GA.274@cpmsnbbsa04>`
- **References:** `<387642BD.256B4EAF@NOSPAMwebaccess.net> <XLSd4.71$dG.1818@ha1>`

```

George McGinn <gmcginn@home.com> wrote in message
news:XLSd4.71$dG.1818@ha1...
>
> If you want to keep your legacy code and still take advantage of a
GUI-style
> system, use a platform like VB or some other GUI system to do all your
> screen and screen edits (Numeric, Range and Acceptable Value checking) and
> call your legacy COBOL programs to do your processing.  This way, when you
> need to change the GUI or want your application to run on different
> platforms, then your "core application" does not need to change - just
your
> front end interfaces.
>
Be careful.  If your GUI front-end is interfacing with a mainframe, you will
probably still need to validate the data on the mainframe before applying
any updates.  While the GUI front-end can significantly reduce the number of
errors, it may be counter productive to eliminate mainframe validation.

Let's assume that you work for a bank that has acquired the credit card
portfolio of another bank.  The acquisition involves over three million
accounts.  Your assignment is to add these accounts to your system.  The
system has many complex Business Rules.  If the mainframe validation program
is out of date, your workload could be overwhelming.

The migration to a GUI front-end may require modification of the mainframe
application to access tables accessible to the mainframe and the GUI
application.  Things such as: State Codes, Ranges, and Inter-dependent Field
Values would fall into this category.  This would ensure that the systems
are in sync.

In any event, the GUI application should be able to handle rejection by the
mainframe application.
```

###### ↳ ↳ ↳ Re: Pseudo conversational future

- **From:** "George McGinn" <gmcginn@home.com>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QY3e4.93$dG.2235@ha1>`
- **References:** `<387642BD.256B4EAF@NOSPAMwebaccess.net> <XLSd4.71$dG.1818@ha1> <eu44kIqW$GA.274@cpmsnbbsa04>`

```
You're right, and that is what I meant in having your legacy programs do the
processing.

What I was trying to explain is you can have the GUI front end validate that
a numeric field is numeric, that if a field only accepts specific values
(i.e.:  A, B and C are the only valid values for a particular field) that
validation should be done in the GUI and not on the mainframe.

I would not have the GUI edit the transaction based on business rules.
These more than likely have already been built into the legacy application.
Let the application check on the validity of the record - let the GUI edit
the fields being entered to make sure that invalid characters or values, or
to make sure that a phone number is entered in the proper edit masks.

I hope that cleared up what I was trying to explain.

-----------------------------
George McGinn
Systems Engineer
GTE-TSI
Tampa  FL

DennisHarley <LegacyBlue@email.msn.com> wrote in message
news:eu44kIqW$GA.274@cpmsnbbsa04...

> Be careful.  If your GUI front-end is interfacing with a mainframe, you
will
> probably still need to validate the data on the mainframe before applying
> any updates.  While the GUI front-end can significantly reduce the number
of
> errors, it may be counter productive to eliminate mainframe validation.
```

##### ↳ ↳ Re: Pseudo conversational future

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uFUwlIqW$GA.220@cpmsnbbsa04>`
- **References:** `<387642BD.256B4EAF@NOSPAMwebaccess.net> <XLSd4.71$dG.1818@ha1>`

```

George McGinn <gmcginn@home.com> wrote in message
news:XLSd4.71$dG.1818@ha1...
>
> If you want to keep your legacy code and still take advantage of a
GUI-style
> system, use a platform like VB or some other GUI system to do all your
> screen and screen edits (Numeric, Range and Acceptable Value checking) and
> call your legacy COBOL programs to do your processing.  This way, when you
> need to change the GUI or want your application to run on different
> platforms, then your "core application" does not need to change - just
your
> front end interfaces.
>
Be careful.  If your GUI front-end is interfacing with a mainframe, you will
probably still need to validate the data on the mainframe before applying
any updates.  While the GUI front-end can significantly reduce the number of
errors, it may be counter productive to eliminate mainframe validation.

Let's assume that you work for a bank that has acquired the credit card
portfolio of another bank.  The acquisition involves over three million
accounts.  Your assignment is to add these accounts to your system.  The
system has many complex Business Rules.  If the mainframe validation program
is out of date, your workload could be overwhelming.

The migration to a GUI front-end may require modification of the mainframe
application to access tables accessible to the mainframe and the GUI
application.  Things such as: State Codes, Ranges, and Inter-dependent Field
Values would fall into this category.  This would ensure that the systems
are in sync.

In any event, the GUI application should be able to handle rejection by the
mainframe application.
```

#### ↳ Re: Pseudo conversational future

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O_Td4.18204$g12.569304@news2.rdc1.on.home.com>`
- **References:** `<387642BD.256B4EAF@NOSPAMwebaccess.net>`

```
I think Theo DP's equation is a pretty reasonable statement but leaves a bit
out in terms of an explanation ;-).

While pseudo-conversational programming may not apply directly to PC
programming, the concept of transaction based programming certainly does,
especially for client/server applications. Designing your program around a
logical unit of work is still valid.

When programming for GUI, the programming for an event model is
significantly different from the traditional state machine model that gets
used in pseudo conversational coding. However, there are similarities. You
still need to initialize stuff before passing control to a user. You still
need to respond to user actions, albeit without assuming that other
dependent actions have occurred. You still need to deal with data storage
and retrieval, business logic, etc. The differences are in how and when that
code is performed.

The approach to validation of a graphical application ought to be different
than the way it is done on the mainframe. In the 3270 world, it is
impossible to respond to every user action. Only certain keys cause a
conversation with the mainframe, namely the function keys, enter key, and a
few others. This means a heavy emphasis on correcting user's mistakes after
they have been made, via validation routines. In the Windows world every
user action flows through the message loop. Most of the messages are passed
on to Windows to handle but the few that you care about can be intercepted
and dealt with in event handling routines. This implies that you can help
prevent the user from making mistakes rather than telling them that they
have made one after the fact.

If the user must enter valid data before proceeding then disable the 'Apply'
button until they do. If they have to choose from a certain set of values
then give them a list of valid values. If some data depends on other data
then update the interface to reflect the dependency. If the data must have a
certain format (zip code, phone number, e-mail address) then intercept the
keystrokes and inhibit the entering of bad data on each keystroke, or
provide the necessary punctuation automatically .

The funny thing is, a GUI control is a lot like a 3270 terminal. It takes
some data, handles the presentation and accepts user changes. The data is
stored within the control until the program asks for it. Most COBOL GUI
tools provide a means of moving this data into WORKING-STORAGE so a COBOL
programmer doesn't need to worry about the mechanics of doing this, even
though leaving it in the control and mapping a linkage item to it is a more
efficient way to use resources, just like the way the COMMAREA is usually
handled in CICS programs. In fairness to the makers of the COBOL GUI tools
(including me), they have to cope with the conflicting requirements between
efficiency and ease-of-use.

Karl Wagner

"Howard Brazee" <brazee@NOSPAMwebaccess.net> wrote in message
news:387642BD.256B4EAF@NOSPAMwebaccess.net...
> Mainframes have been using pseudo conversational dialogs since forever.
> PCs haven't needed to release resources while waiting for the user to
…[5 more quoted lines elided]…
> handle it?  How do people convert from one system to the other?
```

#### ↳ Re: Pseudo conversational future

- **From:** ThaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-I44eeWdndhrR@localhost>`
- **References:** `<387642BD.256B4EAF@NOSPAMwebaccess.net>`

```
On Thu, 1 Jan 1970 01:59:59, Howard Brazee 
<brazee@NOSPAMwebaccess.net> wrote:

> Mainframes have been using pseudo conversational dialogs since forever. 
> PCs haven't needed to release resources while waiting for the user to
…[5 more quoted lines elided]…
> handle it?  How do people convert from one system to the other?


Guess what.  As PC applications move "to the web" they BECOME pseudo 
conversational.  Any CGI application is pseudoconversational, up to 
and including the point of using hidden fields on the screen to hold 
place keeping data!  So we have not come as far as we appear to have 
come.

Moving from Pseudo conversational to conversational is very easy.  In 
text mode, replace the send/receive with a display/accept.  With GUI 
use something like sp2 and replace the send/receive with a panel 
converse call.  Simple. 

Now, going the OTHER way, from a field by field display/accept program
or an event driven GUI program, where there is code behind each 
object, is much much harder - but it's being done every day as people 
move applications into the browser.

-------------------------

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: Pseudo conversational future

- **From:** "Michael D. Kersey" <mdkersey@hal-pc.org>
- **Date:** 2000-02-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<389F9858.F6113DAE@hal-pc.org>`
- **References:** `<387642BD.256B4EAF@NOSPAMwebaccess.net> <Jl0PnHJ5PvPd-pn2-I44eeWdndhrR@localhost>`

```
Thane Hubbell wrote:
<snipped> 
> Guess what.  As PC applications move "to the web" they BECOME pseudo
> conversational.  Any CGI application is pseudoconversational, up to
> and including the point of using hidden fields on the screen to hold
> place keeping data!  So we have not come as far as we appear to have
> come.
<snipped>
> Now, going the OTHER way, from a field by field display/accept program
> or an event driven GUI program, where there is code behind each
> object, is much much harder - but it's being done every day as people
> move applications into the browser.

Yes! Many mainframe programmers may not know it, but their CICS screens
are almost exactly like the internet's HTML forms, except that HTML
forms don't have quite as much functionality. Once one sees how similar
these two environments are, it should be very easy to make the move. The
underlying communications protocol is different: SNA versus TCP/IP, and
the screen definition languages are different. But otherwise, they are
almost the same thing. The web is much, much more similar to then
mainframe environment than either is to client/server event-driven
processing. 

BTW, does IBM have a CICS-based web server yet? So those "legacy" COBOL
apps can be used to handle HTML forms?
```

###### ↳ ↳ ↳ Re: Pseudo conversational future

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 2000-02-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87oci0$fim$1@aklobs.kc.net.nz>`
- **References:** `<387642BD.256B4EAF@NOSPAMwebaccess.net> <Jl0PnHJ5PvPd-pn2-I44eeWdndhrR@localhost> <389F9858.F6113DAE@hal-pc.org>`

```
Michael D. Kersey <mdkersey@hal-pc.org> wrote:
: Thane Hubbell wrote:
: <snipped> 
:> Guess what.  As PC applications move "to the web" they BECOME pseudo
:> conversational.  Any CGI application is pseudoconversational, up to
:> and including the point of using hidden fields on the screen to hold
:> place keeping data!  So we have not come as far as we appear to have
:> come.

While this is true of CGI, this is not the only way of moving
"to the web".  For example see Flexus Client-server or Java
Client.

: <snipped>
:> Now, going the OTHER way, from a field by field display/accept program
:> or an event driven GUI program, where there is code behind each
:> object, is much much harder - but it's being done every day as people
:> move applications into the browser.

In general it is not suitable to just move screen based or field by
field applications to the web, do you want anyone with a browser
to be able to key in orders or maintain your customer file ?

If it is required to export the system to give wider access for
your own staff then telnet will do the job and requires no
changes for text based terminal systems.

If you want a public access system then it requires a proper
design and is not just a conversion.

: Yes! Many mainframe programmers may not know it, but their CICS screens
: are almost exactly like the internet's HTML forms, except that HTML
: forms don't have quite as much functionality. Once one sees how similar

HTML forms have _different_ functionality.  It is only a superficial
view to say it has less.

: these two environments are, it should be very easy to make the move. The
: underlying communications protocol is different: SNA versus TCP/IP, and
: the screen definition languages are different. But otherwise, they are
: almost the same thing. The web is much, much more similar to then
: mainframe environment than either is to client/server event-driven
: processing. 

Or completely different, depending on how you implement your
web access.

I guess this is an example of 'to a hammer all problems look like
nails'.  You have noticed how you could implement a 'CICS'
like CGI/HTML environment and think that this is all there is.

: BTW, does IBM have a CICS-based web server yet? So those "legacy" COBOL
: apps can be used to handle HTML forms?

I think that they have had this for some time.  But who wants
to export in-house CICS screen to the world ?  Which web users
could handle using your CICS screens without the training your 
in-house users have had.
```

###### ↳ ↳ ↳ Re: Pseudo conversational future

_(reply depth: 4)_

- **From:** Joseph Katnic <josephk@iinet.net.au>
- **Date:** 2000-02-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38A00EAA.C146C6C@iinet.net.au>`
- **References:** `<387642BD.256B4EAF@NOSPAMwebaccess.net> <Jl0PnHJ5PvPd-pn2-I44eeWdndhrR@localhost> <389F9858.F6113DAE@hal-pc.org> <87oci0$fim$1@aklobs.kc.net.nz>`

```
Actually since CICS TS V1.2, IBM has provided CICS with an INTEGRATED
WEB SERVER.
It works essentially like the BMS map interface.
There are API's to produce HTML code and to import HTML code from other
pre-defined sources.

It is all reasonably clever, except for the fact that the users
transaction does
not run against a CICS terminal and therefore cannot use the
SIGNON/SIGNOFF api's.
Also the code to determine what transaction to run is a kludge.

I think it's about time that the CICS developers forced the issue with
the selection
of transaction codes from the incoming HTML request.

I would prefer that it works similar to normal web servers in that you
use CGI-BIN to
indicate the transaction to be executed thusly:

HTTP://x.x.x.x/cgi-bin/tran?.....

Of course, since they give you the code that makes the transaction
determination,
in various languages I might add (COBOL {yea}, PL/1 {ok}, assembler
{yawn} and
C {yuckko}), you can always set it up to work that way.

I just found it annoying to have to change the default sample to do
that.


Richard Plinston wrote:
> 
> : BTW, does IBM have a CICS-based web server yet? So those "legacy" COBOL
…[10 more quoted lines elided]…
> -------------------------------------------------------------- */
```

###### ↳ ↳ ↳ Re: Pseudo conversational future

_(reply depth: 5)_

- **From:** stevenln@aol.comnospam (Steve Newton)
- **Date:** 2000-02-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000209093829.01543.00000003@ng-fp1.aol.com>`
- **References:** `<38A00EAA.C146C6C@iinet.net.au>`

```
>BTW, does IBM have a CICS-based web server yet? So those "legacy" COBOL
>> : apps can be used to handle HTML forms?

Actually, for a situation where this connecntion made business sense, I think
the "approved" response would be to create a WEB application designed for that
environment, and then use MQSeries to establish dynamic links back to the CICS
environment ... or better yet, skip CICS and connect directly to the data store
- if possible.  Aside from the advantages of updating user interfaces, this
approach also sells more software for IBM <G>.


Asimov, Heinlein, and Zappa
Still the best
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
