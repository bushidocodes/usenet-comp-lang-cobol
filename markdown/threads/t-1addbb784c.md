[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL conversion

_26 messages · 15 participants · 2000-04_

---

### COBOL conversion

- **From:** softpaww <softpawNOsoSPAM@telenet.net.invalid>
- **Date:** 2000-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com>`

```
I have NO idea how to do what I am going to ask about and would
appreciate any input.  I utilize a software in my business which was
converted from a Unix platform to a PC environment several years ago. 
At that time, it ran strictly in DOS on a pier to pier lan network.  It
was a few years ago made to run (or appear to run) in Windows
3.1...then eventually, Windows 95, 98, NT....on pretty much any kind of
network any user has.  Here is what I have been told but know nothing
about this kind of stuff and am just a user.  It was/is written in
Cobol and uses a GUI interface to present as a "WINDOW" application. 
(You can NOT open multiple windows of the application, so it is not
true windows).  I have also been told it is COBOL on the "back end",
C++ OR visual basic on the front end and uses MICRO FOCUS or FOCUS for
the "windowing"...I am probably using all the wrong terms and I
apologize for my ignorance in this regard.  What I am trying to find
out is what it would take to convert this program from its present
state to a CURRENT programming language.  This is NOT a scientific
program with complex algorithms (sp) as far as I know.  It does very
basic things like calender files, compile statisticial figures....it is
actually almost an accounting program, but is proprietary.  I am NOT
trying to steal the software.  I actually work for the company as a
trainer and have lots of people ask me when I travel why it is "STILL"
in COBOL....so, I am going to try to do some research and see what it
would take to get it out of COBOL. Also, there is a version of the SAME
software that is ORACLE ready which they charge more for.  My brother
tells me that if there is an ORACLE version ready that works, that most
of the COBOL would have to be gone in order for ORACLE to work as
ORACLE is an "open arcitechture".... ANY help/input will be MOST
appreciated.  I will be happy to answer or clarify anything which may
be unclear.  softpaw@telenet.net THANKS!


* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network *
The fastest and easiest way to search and participate in Usenet - Free!
```

#### ↳ Re: COBOL conversion

- **From:** jets@nbnet.nb.ca (Tony M. Mina)
- **Date:** 2000-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38f0e8bd.12747604@allnews.nbnet.nb.ca>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com>`

```
My client had several DOS systems running on a Novell network years ago.
These systems were also connected to a Unisys mainframe.  We did a study
whether it's worth converting to another system and found out that the
cost is not justifiable.  So what we did is to convert the existing
Cobol system amd make it Windows.  We went from Micro Focus DOS Cobol to
Fujitsu Cobol and used Cobol SP2 for the Windows interface and used
FormPrint QPR for the reports.  Also connected to a Unisys mainframe.
The cost was way below the cost if we convert to another system.  The
system is running on a Windows NT server.

It's been running now for serveral years and my client is very happy
with the decision to stay in Cobol especially the cost as well as the
maintenance of the system.

If you need more info, please email me privately.

Thanks

Tony M. Mina
Email: jets@nbnet.nb.ca
Web:  www.mc-sys.com


On Sun, 09 Apr 2000 06:12:28 -0700, softpaww
<softpawNOsoSPAM@telenet.net.invalid> wrote:

>I have NO idea how to do what I am going to ask about and would
>appreciate any input.  I utilize a software in my business which was
…[31 more quoted lines elided]…
>
```

#### ↳ Re: COBOL conversion

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 2000-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OTZQsMko$GA.235@cpmsnbbsa03>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com>`

```

"softpaww" <softpawNOsoSPAM@telenet.net.invalid> wrote in message
news:03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com...
> I have NO idea how to do what I am going to ask about and would
> appreciate any input.  I utilize a software in my business which was
…[13 more quoted lines elided]…
> state to a CURRENT programming language.  This is NOT a scientific



Well, given that COBOL is a CURRENT programming language, and that Micro
Focus is a CURRENT GUI environment, it won't take anything to convert your
application into a CURRENT system because it already is CURRENT.





> program with complex algorithms (sp) as far as I know.  It does very
> basic things like calender files, compile statisticial figures....it is
> actually almost an accounting program, but is proprietary.  I am NOT
> trying to steal the software.  I actually work for the company as a
> trainer and have lots of people ask me when I travel why it is "STILL" in
COBOL
<snip>

Maybe because it works, is still working, and will keep on working?



> would take to get it out of COBOL. Also, there is a version of the SAME
> software that is ORACLE ready which they charge more for.  My brother

The company that makes this software in various versions does not provide a
way to switch between them?  I don't understand.  Could you clarify things a
bit?
Who is the application creator (your company/another company)?
Who is the application user (your company/another company)?


> tells me that if there is an ORACLE version ready that works, that most
> of the COBOL would have to be gone in order for ORACLE to work as

  What exactly is being discussed here?  Why would COBOL have to be "gone"
from your current application in order for you to use completely different
version of the same software?  The new software does not contain COBOL code,
so I don't see how taking the COBOL code out of the original application
helps (other than to stop the original application from working unless other
code was added in, but then the code would just be working the way it had in
the first place, right?).



  It sounds like you want a data transformation utility to convert your
current files into Oracle database files which can be used by this "new"
software version.
  You don't need to do any COBOL code conversion to do this.
  Just a few posts upstream someone mentioned a utility called DBMS/Copy
that does this sort of thing, and other people mentioned other products.
  Do a powersearch on www.deja.com and do a search on DBMS/Copy on this
newsgroup and look into all the messages in that thread to find the names of
the other products.  Or do a web search.

  But honestly, if the vendor of your application is some 3rd party, and you
are paying ongoing license/support fees, this should be something they at
least give you solid advice on, if not actually do it themselves.


> ORACLE is an "open arcitechture".... ANY help/input will be MOST
> appreciated.  I will be happy to answer or clarify anything which may
…[3 more quoted lines elided]…
> * Sent from RemarQ http://www.remarq.com The Internet's Discussion Network
*
> The fastest and easiest way to search and participate in Usenet - Free!
>
```

##### ↳ ↳ Re: COBOL conversion

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8crdcs$rsb$1@news.cerf.net>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <OTZQsMko$GA.235@cpmsnbbsa03>`

```
"ChrisOsborne" <chris_n_osborne@yahoo.com> wrote in message
news:OTZQsMko$GA.235@cpmsnbbsa03...
> Well, given that COBOL is a CURRENT programming language, and that Micro
> Focus is a CURRENT GUI environment, it won't take anything to convert your
> application into a CURRENT system because it already is CURRENT.

I do agree in the first and the third statement, but claiming Micro Focus to
be a GUI environment is to pull the trigger too far. Micro Focus is (and
probably an excellent variant too) a development tool for Cobol, providing
support FOR GUI environment yes, but it has never been a GUI environment
itself.
Windows, OS/2 presentation Manager, Apple System x, are all examples of GUI
environments.

Cheesle
```

###### ↳ ↳ ↳ Re: COBOL conversion

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uZkRNh0o$GA.230@cpmsnbbsa03>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <OTZQsMko$GA.235@cpmsnbbsa03> <8crdcs$rsb$1@news.cerf.net>`

```
I did not mean to imply Micro Focus was an OS-level GUI environment.

<snip>
>but claiming Micro Focus to be a GUI environment is to pull the trigger
>too far.
<snip>
```

###### ↳ ↳ ↳ Re: COBOL conversion

_(reply depth: 4)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cvgjt$8qc$1@news.cerf.net>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <OTZQsMko$GA.235@cpmsnbbsa03> <8crdcs$rsb$1@news.cerf.net> <uZkRNh0o$GA.230@cpmsnbbsa03>`

```
"ChrisOsborne" <chris_n_osborne@yahoo.com> wrote in message
news:uZkRNh0o$GA.230@cpmsnbbsa03...
> I did not mean to imply Micro Focus was an OS-level GUI environment.
>
…[3 more quoted lines elided]…
> <snip>

See my reply to Ib, no offense intended. My apologies if you had that
impression.

Cheesle
```

###### ↳ ↳ ↳ Re: COBOL conversion

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F14D31.F0663DEB@home.com>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <OTZQsMko$GA.235@cpmsnbbsa03> <8crdcs$rsb$1@news.cerf.net>`

```


Cheesle wrote:
> 
> "ChrisOsborne" <chris_n_osborne@yahoo.com> wrote in message
…[13 more quoted lines elided]…
> Cheesle

Bob - jump in and say something nasty about AcuCOBOL <G>. Ib - Next time
you are in his direction - swipe this fellow-Viking over the head with a
2 x 4 <G>

Mr. Cheesle have I been wasting my time. M/F NetExpress is very much
CURRENT as regards GUIs - but take your point about it not being an O/S.
Now here's the problem - got 3 years to find out all the nuances of
Windows ? N/E provides a complete hierarchy of classes for all of the
Windowing controls with methods to flip-them, churn-them, do
what-the-hell you want - if you've got the time. At the moment these
classes are independent of one another grouped under 'GUI' - each doing
its own thing. Remember why Thane went the SP2 route - because Flexus
have done that research bit and provide him with the quick leverage into
Windows.

M/F's Dialog System goes about 80-90% of the way for Windowing - but
then you have to familiarize yourself with OO GUIs to handle the
exceptions - some just don't want the challenge of OO, preferring to
stick to structured. (And I don't blame them).

Currently I'm working on a class MyDialog.cbl which uses a very small
subset of those Windows controls - but here's the interesting bit - if
M/F were to take my Mickey Mouse approach and develop a Merant Class
MFDialog.cbl with sub-classes for each of the controls, (using the many,
many methods they already have coded), they would have a very serious
contender up against Flexus Sp2, Norcom ScreenIO - and dare I say it -
leave your 'dual screens' in the dust <G>

I haven't the time to dabble - but I'm also pretty confident that
Activex controls could probably be built from the GUI classes, using
drawing and painting methods.

Jimmy
```

###### ↳ ↳ ↳ Re: COBOL conversion

_(reply depth: 4)_

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ctijr$lvc$1@news.inet.tele.dk>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <OTZQsMko$GA.235@cpmsnbbsa03> <8crdcs$rsb$1@news.cerf.net> <38F14D31.F0663DEB@home.com>`

```
Did you know that we normally are friendly, quiet people in Scandinavia. I
would never use a 2x4 to anything like that, and on the other hand - he
would probably just shout 'The door's open'.

Now I am a little confused about when to call something a GUI environment.
When I start my GUI Workbench 16- or 32-bit I invoke my GUI-Edit-Animate
using Drag'n-Drop. That is a GUI environment to me, and I beleive that the
operating system supports that environment - even the one from Billy
Windoza.

Likewise NetExpress and Mainframe Express are GUI environments - even if we
use them to develop character based applications. My point is, that when the
environment I am in as a developer is GUI all over, I will call it a GUI
environment - even if it's not the operating system itself.

That is what G-U-I stands for, isn't it?

Regards
Ib
James J. Gavan skrev i meddelelsen <38F14D31.F0663DEB@home.com>...
>
>
…[4 more quoted lines elided]…
>> > Well, given that COBOL is a CURRENT programming language, and that
Micro
>> > Focus is a CURRENT GUI environment, it won't take anything to convert
your
>> > application into a CURRENT system because it already is CURRENT.
>>
>> I do agree in the first and the third statement, but claiming Micro Focus
to
>> be a GUI environment is to pull the trigger too far. Micro Focus is (and
>> probably an excellent variant too) a development tool for Cobol,
providing
>> support FOR GUI environment yes, but it has never been a GUI environment
>> itself.
>> Windows, OS/2 presentation Manager, Apple System x, are all examples of
GUI
>> environments.
>>
…[34 more quoted lines elided]…
>Jimmy
```

###### ↳ ↳ ↳ Re: COBOL conversion

_(reply depth: 5)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cvgi9$8q5$1@news.cerf.net>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <OTZQsMko$GA.235@cpmsnbbsa03> <8crdcs$rsb$1@news.cerf.net> <38F14D31.F0663DEB@home.com> <8ctijr$lvc$1@news.inet.tele.dk>`

```
"Ib Tanding" <ib@tanding.dk> wrote in message
news:8ctijr$lvc$1@news.inet.tele.dk...
> Did you know that we normally are friendly, quiet people in Scandinavia. I
> would never use a 2x4 to anything like that, and on the other hand - he
> would probably just shout 'The door's open'.

I am sorry if what I wrote was considered offending, it was not intentional
and I cannot do anything but excuse my English. :-(

> Now I am a little confused about when to call something a GUI environment.

Well, you got me confused too, with your explanation which I consider very
good. So I am not going to start a war here, but I would rather consider the
development environment just that, "development environment", or may be "GUI
development environment", or even better; "GUI IDE" where IDE is Integrated
Development Environment". I believe the confusion here is due to Micro Focus
use of the terminology, which I suspect is local to them.

> That is what G-U-I stands for, isn't it?

Never the less, I have no problem being wrong, so am I wrong, then I am
wrong, this is after all no big deal.

Cheesle
```

###### ↳ ↳ ↳ Re: COBOL conversion

_(reply depth: 6)_

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cvl1n$dh5$1@news.inet.tele.dk>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <OTZQsMko$GA.235@cpmsnbbsa03> <8crdcs$rsb$1@news.cerf.net> <38F14D31.F0663DEB@home.com> <8ctijr$lvc$1@news.inet.tele.dk> <8cvgi9$8q5$1@news.cerf.net>`

```
Make peace, not war:
GUI IDE is ok for people who knows Merant, the other very few friends we
have, can for my sake say that they work with a GUI-based development tool.

Cheers
Ib
Cheesle skrev i meddelelsen <8cvgi9$8q5$1@news.cerf.net>...
>"Ib Tanding" <ib@tanding.dk> wrote in message
>news:8ctijr$lvc$1@news.inet.tele.dk...
>> Did you know that we normally are friendly, quiet people in Scandinavia.
I
>> would never use a 2x4 to anything like that, and on the other hand - he
>> would probably just shout 'The door's open'.
…[4 more quoted lines elided]…
>> Now I am a little confused about when to call something a GUI
environment.
>
>Well, you got me confused too, with your explanation which I consider very
>good. So I am not going to start a war here, but I would rather consider
the
>development environment just that, "development environment", or may be
"GUI
>development environment", or even better; "GUI IDE" where IDE is Integrated
>Development Environment". I believe the confusion here is due to Micro
Focus
>use of the terminology, which I suspect is local to them.
>
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COBOL conversion

_(reply depth: 4)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38fb4fce.13570072@news.epix.net>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <OTZQsMko$GA.235@cpmsnbbsa03> <8crdcs$rsb$1@news.cerf.net> <38F14D31.F0663DEB@home.com>`

```
Jimmy:

"James J. Gavan" <jjgavan@home.com> wrote:

>
>
…[20 more quoted lines elided]…
>2 x 4 <G>

I would never say anything nasty about Acucobol in this newsgroup.
And I would never swipe my buddy Cheesle with a 2 x 4!

Hey, Cheesle....are you planning to travel to San Diego for the
Acucorp users conference?  

>I haven't the time to dabble - but I'm also pretty confident that
>Activex controls could probably be built from the GUI classes, using
>drawing and painting methods.

<shameless commercial>

Now, I'll take a swipe at Jimmy.....sp2 supports (and has supported
for some time now), the ability to embed and control OCX (Active X)
controls directly from the COBOL program......they're controlled
completely by invoking a call to sp2 and passing a parameter block.

</shameless commercial>


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: COBOL conversion

_(reply depth: 5)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8di402$n3j$1@news.cerf.net>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <OTZQsMko$GA.235@cpmsnbbsa03> <8crdcs$rsb$1@news.cerf.net> <38F14D31.F0663DEB@home.com> <38fb4fce.13570072@news.epix.net>`

```
"Bob Wolfe" <rtwolfe@flexus.com> wrote in message
news:38fb4fce.13570072@news.epix.net...
> "James J. Gavan" <jjgavan@home.com> wrote:
> >Bob - jump in and say something nasty about AcuCOBOL <G>. Ib - Next time
> >you are in his direction - swipe this fellow-Viking over the head with a
> >2 x 4 <G>

Hi Jimmy, how come this message did not show to me?

Anyway, if you guys think I am exaggerating, I will of course cool down. I
take the message, no hard feelings.

> And I would never swipe my buddy Cheesle with a 2 x 4!

Sounds good, I ain't sure what a 2x4 means, but it sure don't sound good to
be swiped by :-)

> Hey, Cheesle....are you planning to travel to San Diego for the
> Acucorp users conference?

Nah, that's pretty far isn't?

> Now, I'll take a swipe at Jimmy.....sp2 supports (and has supported
> for some time now), the ability to embed and control OCX (Active X)
> controls directly from the COBOL program......they're controlled
> completely by invoking a call to sp2 and passing a parameter block.

And it is by no doubt a very good approach for someone that would like GUI
with minor adjustments to their code.

Cheesle
```

###### ↳ ↳ ↳ Re: COBOL conversion

_(reply depth: 6)_

- **From:** dxmixxer@netdirect.net (Doug Miller)
- **Date:** 2000-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aO3L4.720$T9.10194448@news.netdirect.net>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <OTZQsMko$GA.235@cpmsnbbsa03> <8crdcs$rsb$1@news.cerf.net> <38F14D31.F0663DEB@home.com> <38fb4fce.13570072@news.epix.net> <8di402$n3j$1@news.cerf.net>`

```
In article <8di402$n3j$1@news.cerf.net>, "Cheesle" <cheesle@online.NoSpamPlease.no> wrote:
>"Bob Wolfe" <rtwolfe@flexus.com> wrote in message
>news:38fb4fce.13570072@news.epix.net...
…[13 more quoted lines elided]…
>be swiped by :-)

It's not. A 2x4 is a piece of wood used (for example) in framing house walls, 
so-called because its dimensions are nominally 2 by 4 inches. Actual size is 
about 9cm wide by 4cm thick; length varies, of course, but 8 feet (244cm) is 
typical. Getting whacked with one would hurt.
```

###### ↳ ↳ ↳ Re: COBOL conversion

_(reply depth: 7)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dilvm$46b$1@news.cerf.net>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <OTZQsMko$GA.235@cpmsnbbsa03> <8crdcs$rsb$1@news.cerf.net> <38F14D31.F0663DEB@home.com> <38fb4fce.13570072@news.epix.net> <8di402$n3j$1@news.cerf.net> <aO3L4.720$T9.10194448@news.netdirect.net>`

```
"Doug Miller" <dxmixxer@netdirect.net> wrote in message
news:aO3L4.720$T9.10194448@news.netdirect.net...
> It's not. A 2x4 is a piece of wood used (for example) in framing house
walls,
> so-called because its dimensions are nominally 2 by 4 inches. Actual size
is
> about 9cm wide by 4cm thick; length varies, of course, but 8 feet (244cm)
is
> typical. Getting whacked with one would hurt.

Thanks for the explanation, I better stay cool then :-)

Cheesle
```

###### ↳ ↳ ↳ Re: COBOL conversion

_(reply depth: 6)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2000-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38fdc20a.7138485@news.epix.net>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <OTZQsMko$GA.235@cpmsnbbsa03> <8crdcs$rsb$1@news.cerf.net> <38F14D31.F0663DEB@home.com> <38fb4fce.13570072@news.epix.net> <8di402$n3j$1@news.cerf.net>`

```
"Cheesle" <cheesle@online.NoSpamPlease.no> wrote:

>"Bob Wolfe" <rtwolfe@flexus.com> wrote in message
[snip]
>Sounds good, I ain't sure what a 2x4 means, but it sure don't sound good to
>be swiped by :-)

Cheesle:

It's not fun to be swiped by a 2 x 4.  Now...for a description.  A 2 x
4 (or "two by four") is an object fashioned from cellulose, which can
be acquired in varying lengths, typically utilized as a structural
component in the development of various 3 dimensional structures.
They are commonly used to erect residential or commercial edifices.
Multiple 2 x 4's are generally fastened together by small sharpened
pins crafted from iron ore (or recycled Yugos) for the purpose of
creating three-dimensional chambers.

In other words, a 2 x 4 is board that is used to build homes among
other things.

The reason that they are called 2 x 4's is because the width of a
standard 2 x 4 is 3.5 inches (89 mm) and the depth is 1.5 inches (39
mm)  I think that they should be called 39 by 89's.  It would be far
more accurate.

Please don't blame me....I didn't make the rules!

2 x 4's come in varying lengths which can be cut to suit your specific
needs, although current technology does not allow them to be
lengthened.  This will become possible when the brilliant Doc Dwarf
perfects his patented "board stretching device"

>> Hey, Cheesle....are you planning to travel to San Diego for the
>> Acucorp users conference?
>
>Nah, that's pretty far isn't?

It is....we are still trying to decide.

[snip]


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: COBOL conversion

_(reply depth: 7)_

- **From:** "Warren Simmons" <w.g.simmons@worldnet.att.net>
- **Date:** 2000-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NapL4.13284$PV.903715@bgtnsc06-news.ops.worldnet.att.net>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <OTZQsMko$GA.235@cpmsnbbsa03> <8crdcs$rsb$1@news.cerf.net> <38F14D31.F0663DEB@home.com> <38fb4fce.13570072@news.epix.net> <8di402$n3j$1@news.cerf.net> <38fdc20a.7138485@news.epix.net>`

```
This is a fairly comprehensive description of 2 by 4's.  However, the
authors missed a couple of facts that add nothing to the discussion of
cobol that
may be fascinating to some.

1.  In early days of saw mill operations, lumber was cut to measure for a
variety of uses using whole numbers.  Two by four inches, two by six
inches, etc.

2.  It became apparent that Object orientation would stretch the supply of
lumber, and do the same job.  New dimensions were established, and
the old names were retained to avoid retraining.

3. Other materials besides lumber are used to build 2 by 4's.  Example:
steel.

4.  If you want to see the old style lumber, visit an old house, and take a
trip to the cellar and carry your tape measure.

Warren Simmons
"Bob Wolfe" <rtwolfe@flexus.com> wrote in message
news:38fdc20a.7138485@news.epix.net...
> "Cheesle" <cheesle@online.NoSpamPlease.no> wrote:
>
> >"Bob Wolfe" <rtwolfe@flexus.com> wrote in message
> [snip]
> >Sounds good, I ain't sure what a 2x4 means, but it sure don't sound good
to
> >be swiped by :-)
>
…[39 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COBOL conversion

_(reply depth: 8)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2000-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38feff78.1826544@news.epix.net>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <OTZQsMko$GA.235@cpmsnbbsa03> <8crdcs$rsb$1@news.cerf.net> <38F14D31.F0663DEB@home.com> <38fb4fce.13570072@news.epix.net> <8di402$n3j$1@news.cerf.net> <38fdc20a.7138485@news.epix.net> <NapL4.13284$PV.903715@bgtnsc06-news.ops.worldnet.att.net>`

```
"Warren Simmons" <w.g.simmons@worldnet.att.net> wrote:

>This is a fairly comprehensive description of 2 by 4's.  However, the
>authors missed a couple of facts that add nothing to the discussion of
>cobol that
>may be fascinating to some.

You're absolutely correct!

>1.  In early days of saw mill operations, lumber was cut to measure for a
>variety of uses using whole numbers.  Two by four inches, two by six
…[4 more quoted lines elided]…
>the old names were retained to avoid retraining.

I don't believe that object orientation was responsible for the new
dimensions.  I believe that the dimensions were changed when an
upstart sawmill called the Microwood Corporation introduced a new and
improved 2 x 4 with smaller dimensions (new ideas and innovations) and
declared it to be the standard.

Soon, all the other sawmills mysteriously went out of business and
everyone was forced to adopt the new standard immediately because it
was the only thing available.

;-)  (Ain't I the cynic today!)

>3. Other materials besides lumber are used to build 2 by 4's.  Example:
>steel.

Yes, but those 2 x 4's were developed by Sun Microsteel and the debate
rages on whether to use wooden studs from Microwood or steel studs
from Sun Microsteel.

>4.  If you want to see the old style lumber, visit an old house, and take a
>trip to the cellar and carry your tape measure.

Tell me about it!  Years ago, my wife talked me into buying a large
110 year old house because it was really cool.  But I'm the guy who
has to repair everything all the time.  Nothing is standard and
nothing is square.  I've wiped out more cedar trees through excessive
use of cedar shims than I want to think about.




Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ OT: 2X4

_(reply depth: 7)_

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dm684$b6e$1@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <OTZQsMko$GA.235@cpmsnbbsa03> <8crdcs$rsb$1@news.cerf.net> <38F14D31.F0663DEB@home.com> <38fb4fce.13570072@news.epix.net> <8di402$n3j$1@news.cerf.net> <38fdc20a.7138485@news.epix.net>`

```

Bob Wolfe <rtwolfe@flexus.com> wrote in message
news:38fdc20a.7138485@news.epix.net...
> "Cheesle" <cheesle@online.NoSpamPlease.no> wrote:
>
> >"Bob Wolfe" <rtwolfe@flexus.com> wrote in message
> [snip]
> >Sounds good, I ain't sure what a 2x4 means, but it sure don't sound good
to
> >be swiped by :-)
>
…[25 more quoted lines elided]…
>

Note: 2x4's are 2inch by 4inch after they have been cut, and before they
have been planed smooth.  A full size 2x4 is rough to the touch, not smooth.

This is not unlike the hamburger places advertising uncooked weight,
but selling cooked patties that weigh much less.
```

###### ↳ ↳ ↳ Re: OT: 2X4

_(reply depth: 8)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2000-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38ff0354.2814724@news.epix.net>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <OTZQsMko$GA.235@cpmsnbbsa03> <8crdcs$rsb$1@news.cerf.net> <38F14D31.F0663DEB@home.com> <38fb4fce.13570072@news.epix.net> <8di402$n3j$1@news.cerf.net> <38fdc20a.7138485@news.epix.net> <8dm684$b6e$1@ssauraaa-i-1.production.compuserve.com>`

```
"Russell Styles" <RWSTYLES@COMPUSERVE.COM> wrote:

>
>Bob Wolfe <rtwolfe@flexus.com> wrote in message
>news:38fdc20a.7138485@news.epix.net...
[snip]
>
>Note: 2x4's are 2inch by 4inch after they have been cut, and before they
…[3 more quoted lines elided]…
>but selling cooked patties that weigh much less.

....and taste like 2 x 4's!

;-)


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: COBOL conversion

_(reply depth: 7)_

- **From:** WDS@WDS.WDS.5 (WDS)
- **Date:** 2000-04-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3900e5dd.17271056@news1.frb.gov>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <OTZQsMko$GA.235@cpmsnbbsa03> <8crdcs$rsb$1@news.cerf.net> <38F14D31.F0663DEB@home.com> <38fb4fce.13570072@news.epix.net> <8di402$n3j$1@news.cerf.net> <38fdc20a.7138485@news.epix.net>`

```
On Wed, 19 Apr 2000 14:53:44 GMT, Bob Wolfe wrote:

>Multiple 2 x 4's are generally fastened together by small sharpened
>pins crafted from iron ore (or recycled Yugos) [...]

Recycled Yugos?  You can make nails from a mixture of plastic, dirt,
and rust?
```

###### ↳ ↳ ↳ Re: COBOL conversion

_(reply depth: 8)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f%8M4.17637$0o4.122108@iad-read.news.verio.net>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <8di402$n3j$1@news.cerf.net> <38fdc20a.7138485@news.epix.net> <3900e5dd.17271056@news1.frb.gov>`

```
In article <3900e5dd.17271056@news1.frb.gov>, WDS <WDS@WDS.WDS.5> wrote:
>On Wed, 19 Apr 2000 14:53:44 GMT, Bob Wolfe wrote:
>
…[4 more quoted lines elided]…
>and rust?

Well, he didn't say they were very *good* nails...

DD
```

###### ↳ ↳ ↳ Re: COBOL conversion

_(reply depth: 9)_

- **From:** Alistair Maclean <LD50Macca@ld50macca.demon.co.uk>
- **Date:** 2000-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AA0EGWA7NGB5EwVX@ld50macca.demon.co.uk>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <8di402$n3j$1@news.cerf.net> <38fdc20a.7138485@news.epix.net> <3900e5dd.17271056@news1.frb.gov> <f%8M4.17637$0o4.122108@iad-read.news.verio.net>`

```
Why would you need nails at all? You could do the same job with
dowelling and save all the Yugos (and Ladas and Skodas) for the landfill
sites.

BTW, in Cambridge (England) there is a wooden bridge (I think it is the
Mathematical Bridge) which was originally built without the use of nails
but, having since been taken apart for restoration, has had to be re-
built using nails. Probably not made from recycled Eastern European
automobiles. 

In article <f%8M4.17637$0o4.122108@iad-read.news.verio.net>,
docdwarf@clark.net writes
>In article <3900e5dd.17271056@news1.frb.gov>, WDS <WDS@WDS.WDS.5> wrote:
>>On Wed, 19 Apr 2000 14:53:44 GMT, Bob Wolfe wrote:
…[10 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COBOL conversion

_(reply depth: 9)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2000-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39044c5d.1050946@news.epix.net>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com> <8di402$n3j$1@news.cerf.net> <38fdc20a.7138485@news.epix.net> <3900e5dd.17271056@news1.frb.gov> <f%8M4.17637$0o4.122108@iad-read.news.verio.net>`

```
docdwarf@clark.net () wrote:

>In article <3900e5dd.17271056@news1.frb.gov>, WDS <WDS@WDS.WDS.5> wrote:
>>On Wed, 19 Apr 2000 14:53:44 GMT, Bob Wolfe wrote:
…[9 more quoted lines elided]…
>DD

...and I didn't say how *many* nails you could make.  I'm sure that
you could get at least one or two.


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: COBOL conversion

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cqfdp$ii4$1@nnrp1.deja.com>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com>`

```
In article <03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com>,
  softpaww <softpawNOsoSPAM@telenet.net.invalid> wrote:


>What I am trying to find out is what it would take to convert this
>program from its present state to a CURRENT programming language.

Hi:

COBOL IS a 'current programming language' and it is far from dead.
If it works, why change it? Just to convert it to make it into
something 'current' doesn't make business sense.

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: COBOL conversion

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cqm75$79g$1@news.inet.tele.dk>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com>`

```
Hey,
I can see your problem. Sombody made an application, and suddenly you find
out that the data cannot be shared, and 2 million people in your company
would *luw* to maintain it, if it just was made in Oracle Forms.

Now, your present application is something. It has been worth to move it
from Unix to DOS, From DOS to Windows 3.x. Someone has reprogrammed the
application to put in the GUI-dialog. The structure in an old Character
based application is very different from the one you need have, when you put
on the GUI.

I am telling you this, so you can see that your company has made investments
in the present application.

It is probably quit easy to change your current filesystem to an Oracle
database. Letting your present application use Oracle gives you data
sharing, and it will be possible to extract date for other purposes by the
use of Oracle Forms.

If you consider the present application to be ready for major reprogramming,
and if you choose Oracle because some wise guys are saying that Cobol is old
technology,  I must say that their knowledge is built up from reading
colored magazines, not from education. We are nowadays making very modern
applications in Object Oriented Cobol, and in traditional Cobol with various
GUI fronts.

You can choose Oracle if that is the skills your company prefer, but if you
have cobol programmers as well, you should consider to use an Oracle
Database for your data.

Please let your analysis be based upon facts, instead of feelings and
fashion.

Regards
Ib


softpaww skrev i meddelelsen
<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com>...
>I have NO idea how to do what I am going to ask about and would
>appreciate any input.  I utilize a software in my business which was
…[29 more quoted lines elided]…
>* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network
*
>The fastest and easiest way to search and participate in Usenet - Free!
>
```

#### ↳ Re: COBOL conversion

- **From:** Charles F Hankel <noos@hankel.freedombird.net>
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.135ae90f84f0dd5f9896d6@news.freedombird.net>`
- **References:** `<03fc63cc.ea1ff9c8@usw-ex0107-049.remarq.com>`

```
I noticed that softpaww as softpawNOsoSPAM@telenet.net.invalid said...
> I am NOT
> trying to steal the software.  I actually work for the company as a
> trainer and have lots of people ask me when I travel why it is "STILL"
> in COBOL....so, I am going to try to do some research and see what it
> would take to get it out of COBOL.

There's at least one misconception to correct here and that is that 
COBOL is very much a current language.  It is more modern than, say, C 
and C++, because the standard moves with the times.

It is most important that you understand that there is absolutely 
nothing wrong with COBOL and that it is far more desirable to use it for 
business oriented software than just about any other language out there.  
If anyone suggests that COBOL is dead, old-fashioned or other such 
derogatory term, refer them to this newsgroup.

> Also, there is a version of the SAME
> software that is ORACLE ready which they charge more for.  My brother
…[4 more quoted lines elided]…
> be unclear.  softpaw@telenet.net THANKS!

It is more likely that, if there is an Oracle version, it is also in 
COBOL as there would be little point in rewriting the software 
completely.  However, without knowing more about the product, I can't be 
categorical about this.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
