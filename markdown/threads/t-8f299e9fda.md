[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CEDF/InterTest Invoking in Messaging Environment?

_11 messages · 5 participants · 2000-12_

---

### CEDF/InterTest Invoking in Messaging Environment?

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-12-12T17:27:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tetZ5.4953$Sl.253700@iad-read.news.verio.net>`

```

Please pardon my ignorance about such matters... I've been asked to
modify/enhance/Make Right a CICS/DB2 program which I'm having a bit of
trouble with.  Consider the following:

Program A is invoked when a separate region sends over a message via LU6.2
protocol.  Program A examines this message, part of which is the program
name to which it must link, say... Program B.  Program B receives the
LU6.2-originated messsage via the COMMAREA and then does... stuff.

I've been asked to work with Program B and I am at a loss as to how I
would 'grab' it for examination under CEDF or (even better!) InterTest.  I
know the program's name, a TERMID it is passed and the CONN and NET
associated with this TERMID... but I do *not* know how to invoke any of
the debugging tools on my terminal so that when Program B wakes up I can
step through it.

Might anyone be so kind as to pass along a pointer or three?

Thanks much.

DD
```

#### ↳ Re: CEDF/InterTest Invoking in Messaging Environment?

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 2000-12-12T17:38:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9168ui$cpv$1@nntp9.atl.mindspring.net>`
- **References:** `<tetZ5.4953$Sl.253700@iad-read.news.verio.net>`

```
DD,

        You must put the LU6.2 Connection Name under CEDF. When a session
becomes active, you'll be able to step through it. But, make sure no one
else is using the connection or you'll be CEDFing every active session.

Bill

" NA" <docdwarf@clark.net> wrote in message
news:tetZ5.4953$Sl.253700@iad-read.news.verio.net...
>
> Please pardon my ignorance about such matters... I've been asked to
…[20 more quoted lines elided]…
>
```

##### ↳ ↳ Re: CEDF/InterTest Invoking in Messaging Environment?

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-12-13T14:11:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2sLZ5.5054$Sl.259140@iad-read.news.verio.net>`
- **References:** `<tetZ5.4953$Sl.253700@iad-read.news.verio.net> <9168ui$cpv$1@nntp9.atl.mindspring.net>`

```
In article <9168ui$cpv$1@nntp9.atl.mindspring.net>,
WOB <wobconsult@sprynet.com> wrote:
>DD,
>
>        You must put the LU6.2 Connection Name under CEDF.

Hmmmm... assuming the following for Program A is constant (information
garnered from various logs and CEMT):

Termid = -QQQ

Con    = FRED

Net    = A123B45

... then from what you state I understand that my course of action should
be to issue the command:

CEDF FRED

(which gives the response of SYSTEM   FRED: EDF MODE ON FOR ALL SESSIONS) 

... and tell the folks in Messaging Central to send over some messages.

>When a session
>becomes active, you'll be able to step through it. But, make sure no one
>else is using the connection or you'll be CEDFing every active session.

That's not too much of a worry; I've been told (ha!) that FRED is unique
to the transactions I wish to deal with.

I assume that my CESF LOGOFF will halt trapping... or is there something
else I should be doing?

Oh... and thanks much for the info and for putting up with my inanities!

DD

>" NA" <docdwarf@clark.net> wrote in message
>news:tetZ5.4953$Sl.253700@iad-read.news.verio.net...
…[24 more quoted lines elided]…
>
```

#### ↳ Re: CEDF/InterTest Invoking in Messaging Environment?

- **From:** infocat@sprynet.com (Frank Swarbrick)
- **Date:** 2000-12-13T01:41:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a36d325.26574943@nntp.sprynet.com>`
- **References:** `<tetZ5.4953$Sl.253700@iad-read.news.verio.net>`

```
On Tue, 12 Dec 2000 17:27:53 GMT, docdwarf@clark.net (  NA) wrote:

>
>Please pardon my ignorance about such matters... I've been asked to
…[15 more quoted lines elided]…
>Might anyone be so kind as to pass along a pointer or three?

WOB seems to have answered the CEDF part.  (I've never tried that.)  For
Intertest you can go to the "Unconditional Breakpoints" screen (using CNTL) and
set it by entering the line number in the appropriate place, then for the
terminal to act upon (or something like that) put ".ANY".  (That's "[dot]ANY".)

Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"I'm very seldom naughty." --Willow Rosenberg "Buffy the Vampire Slayer"
```

##### ↳ ↳ Re: CEDF/InterTest Invoking in Messaging Environment?

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-12-13T14:27:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XGLZ5.5057$Sl.260213@iad-read.news.verio.net>`
- **References:** `<tetZ5.4953$Sl.253700@iad-read.news.verio.net> <3a36d325.26574943@nntp.sprynet.com>`

```
In article <3a36d325.26574943@nntp.sprynet.com>,
Frank Swarbrick <infocat@sprynet.com> wrote:

[snip the original question]

>WOB seems to have answered the CEDF part.  (I've never tried that.)

I've used it for debugging transactions invoked by a TransID but not for
this kind of 'mid-stream capture'... InterTest is better, granted, but you
know the old saw about selecting ports in storms.

>For
>Intertest you can go to the "Unconditional Breakpoints" screen (using CNTL) and
>set it by entering the line number in the appropriate place, then for the
>terminal to act upon (or something like that) put ".ANY".  (That's "[dot]ANY".)

All righty... let's see, CNTL brings up the CA-InterTest MONITORING
COMMAND BUILDER - FUNCTION SELECTION menu.  I'm interested in function 11
(unconditional breakpoints), (S)etting one for program PROGNAME for User
ID .ANY.  Using the LISTER shows me that after SQL-INIT-END is
000-MAIN-CONTROL and the first executable statement (the
traditional-but-still-popular IF EIBCALEN = 0) is line 7978.  I then
(S)elect the PROTSYM file and, as mentioned, call the Messaging Center,
tell them to send over some messages to Test, sacrifice an appropriate
animal and do my best to divine the entrails.

Greatly appreciated!

DD
```

#### ↳ Re: CEDF/InterTest Invoking in Messaging Environment?

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2000-12-13T06:42:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A3719C2.D6038B56@worldnet.att.net>`
- **References:** `<tetZ5.4953$Sl.253700@iad-read.news.verio.net>`

```
NA wrote:
> 
> Please pardon my ignorance about such matters... I've been asked to
…[19 more quoted lines elided]…
> DD

I'm not sure if this will be any help, since I have been using Xpeditor
for CICS for the last eight years or so.  Prior to that I used InterTest
extensively for debugging CICS programs under conversational tasks.  I
imagine that InterTest has had a few enhancements since CICS 1.6.1!

If you were using Xpeditor I don't think there would be any problem. 
You would just set up a breakpoint at the first executable statement,
make sure monitoring was turned on, and wildcard any terminal.  The
debugging session would be associated with your terminal (but it would
have to be in the same CICS region where program B will execute). 
Xpeditor would trap "program B" as soon as it receives control from the
LINK command.  I have used both Xpeditor and InterTest to trap programs
that receive messages via MRO from another CICS region.

I remember a problem we had with InterTest.  Normally we used a test
program to simulate receipt of messages from our external network.  The
test messages were actually read from a VSAM RRDS file.  The test
program simulated the top of chain for a very long-running
conversational task (lots of XCTL's and LINK's).  The test program was
conversational, but not particularly long running.  The production
program normally sat in a loop on an EXEC CICS RETRIEVE WAIT, then took
the message and XCTL'ed to the next program. 

It came to pass that we had to test the real production program that
received network messages, the one named in the PCT entry as
top-of-chain.  And we could NOT get InterTest to trap it.  This
particular application had 20 tasks (each with a unique TERMID) to
receive network messages from BTAM.  They happened to be written to
restart themselves after an ABEND.  We had to cancel every task and then
send a test message.  The first terminal that received the message would
start the task, and then InterTest could trap it.  Later, when we
switched to Xpeditor (in order to upgrade to CICS release 3.3) we had
the same problem, and had to use the same technique.  

I have fond memories of InterTest.  I think I like the Xpeditor user
interface a little better.  They're both very capable debuggers, but the
InterTest FILE and CORE programs were handy because they could be
secured separately under their own TRAN-IDs.  

I've never learned CEDF.  I've seen it used once or twice, and it's
nowhere near as powerful as InterTest or Xpeditor.  

Good Luck!
```

##### ↳ ↳ Re: CEDF/InterTest Invoking in Messaging Environment?

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-12-13T14:54:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o4MZ5.5067$Sl.260292@iad-read.news.verio.net>`
- **References:** `<tetZ5.4953$Sl.253700@iad-read.news.verio.net> <3A3719C2.D6038B56@worldnet.att.net>`

```
In article <3A3719C2.D6038B56@worldnet.att.net>,
Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:
>NA wrote:

[snip]

>> Might anyone be so kind as to pass along a pointer or three?

[snippette]

>I'm not sure if this will be any help, since I have been using Xpeditor
>for CICS for the last eight years or so.  Prior to that I used InterTest
>extensively for debugging CICS programs under conversational tasks.  I
>imagine that InterTest has had a few enhancements since CICS 1.6.1!

Not so many that I'll need to take advantage of, for the start... stepwise
debugging is still stepwise debugging.

>
>If you were using Xpeditor I don't think there would be any problem. 
>You would just set up a breakpoint at the first executable statement,
>make sure monitoring was turned on, and wildcard any terminal.

Thanks much... Mr Swarbick has expanded upon this 'all ya gotta do is'
into something which I will begin to test today.

[snip]

>I've never learned CEDF.  I've seen it used once or twice, and it's
>nowhere near as powerful as InterTest or Xpeditor.  

CEDF is... better'n nothing, but not by much; the advantage to it is that
it can be found wherever there is CICS.  (Having worked in shops which do
not have AbendAid - and this is within the past five years! - I try to
stay at least moderately conversant with the various primitive, but
ubiquitous, Tools of the Oldene Dayse... batch debugging via DISPLAY,
anyone?)

The most egregious limitation of CEDF is that it breaks only at CICS
commands; this has caused me to insert a goodly number of ASKTIMEs to
bracket statements where there is something amiss... tedious, granted, but
necessary.

Thanks much!

DD
```

#### ↳ Re: CEDF/InterTest Invoking in Messaging Environment?

- **From:** "Mehmet Tanr���verdi" <tanriverdim@turk.net>
- **Date:** 2000-12-13T19:11:59+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a37ad26$1@news.turk.net>`
- **References:** `<tetZ5.4953$Sl.253700@iad-read.news.verio.net>`

```
Use CICS suplied transaction CEDX transaction. I think that is the solution.
Regards
" NA" <docdwarf@clark.net> wrote in message
news:tetZ5.4953$Sl.253700@iad-read.news.verio.net...
>
> Please pardon my ignorance about such matters... I've been asked to
…[20 more quoted lines elided]…
>
```

##### ↳ ↳ Re: CEDF/InterTest Invoking in Messaging Environment?

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-12-13T17:32:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SoOZ5.5104$Sl.261467@iad-read.news.verio.net>`
- **References:** `<tetZ5.4953$Sl.253700@iad-read.news.verio.net> <3a37ad26$1@news.turk.net>`

```
In article <3a37ad26$1@news.turk.net>,
Mehmet Tanr�verdi <tanriverdim@turk.net> wrote:
>Use CICS suplied transaction CEDX transaction. I think that is the solution.
>Regards

Thanks much for the suggestion... but...

DFHAC2001 12/13/00 12:33:20 DATATEST Transaction 'CEDX' is unrecognized.
Check that the transaction name is correct.

DD
```

###### ↳ ↳ ↳ Re: CEDF/InterTest Invoking in Messaging Environment?

- **From:** infocat@sprynet.com (Frank Swarbrick)
- **Date:** 2000-12-14T01:55:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a38282f.37395562@nntp.sprynet.com>`
- **References:** `<tetZ5.4953$Sl.253700@iad-read.news.verio.net> <3a37ad26$1@news.turk.net> <SoOZ5.5104$Sl.261467@iad-read.news.verio.net>`

```
On Wed, 13 Dec 2000 17:32:34 GMT, docdwarf@clark.net (  NA) wrote:

>In article <3a37ad26$1@news.turk.net>,
>Mehmet Tanr�verdi <tanriverdim@turk.net> wrote:
…[6 more quoted lines elided]…
>Check that the transaction name is correct.

CEDX is, I believe, only available under CICS TS, not older versions of CICS.
Or, if it was introduced in a later release of CICS I don't know which one it
would be, but it would probably have been shortly before the release of CICS TS.

Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"I'm very seldom naughty." --Willow Rosenberg "Buffy the Vampire Slayer"
```

###### ↳ ↳ ↳ Re: CEDF/InterTest Invoking in Messaging Environment?

_(reply depth: 4)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-12-14T02:17:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F4WZ5.5196$Sl.264010@iad-read.news.verio.net>`
- **References:** `<tetZ5.4953$Sl.253700@iad-read.news.verio.net> <3a37ad26$1@news.turk.net> <SoOZ5.5104$Sl.261467@iad-read.news.verio.net> <3a38282f.37395562@nntp.sprynet.com>`

```
In article <3a38282f.37395562@nntp.sprynet.com>,
Frank Swarbrick <infocat@sprynet.com> wrote:
>On Wed, 13 Dec 2000 17:32:34 GMT, docdwarf@clark.net (  NA) wrote:
>
…[10 more quoted lines elided]…
>CEDX is, I believe, only available under CICS TS, not older versions of CICS.

Once again I find myself in an archaic environment... but so it goes,
thanks much.

As for your other suggestions... weeeeeellllll, as soon as Mr Network will
stay up long enough for me to maintain, say, more than 28 consecutive
minutes of mainframe connect-time I just *might* be ablt to run a test!

DD
k
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
