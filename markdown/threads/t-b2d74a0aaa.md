[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Trap F10 in MicroFocus DialogSystem

_9 messages · 6 participants · 2003-09 → 2003-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Trap F10 in MicroFocus DialogSystem

- **From:** martin.dannerstedt@ebox.tninet.se (Martin Dannerstedt)
- **Date:** 2003-09-30T03:37:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dfc31c53.0309300237.4b32b95f@posting.google.com>`

```
I would like to trap the functionkey F10 in DialogSystem.
It is not possible by the DS Event F10 because F10 is an shortkey in
Windows and is trapped by windows.
I could specify an menu item shortcut key as F10 in DS, but this
doesnï¿½t help because I have a multiple Screenset application an this
shortkey is only trapped by the windows that has a meny.
An other way is to use the class-library and registry the F10 event
for every object in my windows but this is not practical.

What I would like to do is to find a way, through a win-api or a
utility program that disable the Windows shortcut F10. Maybe after
this I can Trap the event in DialogSystem.
Does anybody konw how to do this ??

Martin Dannerstedt
```

#### ↳ Re: Trap F10 in MicroFocus DialogSystem

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-09-30T21:00:10+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f796357_9@news.athenanews.com>`
- **References:** `<dfc31c53.0309300237.4b32b95f@posting.google.com>`

```
Martin,

it is HIGHLY unlikely that you can effectively "disable" F10 in a Windows
environment.

Even if you COULD do the old TSR trick of hooking the interrupt vector for
int 16 (which you CAN'T in Windows) and looking at each keystroke, you would
still need to pass the event to Windows and it will then implement F10
behaviour.

Many years ago, when I was using DIALOG I remember having this problem but I
can't remember how it was solved. I suspect that MF will have a solution for
mapping Windows keys.

My recommendation would be to rethink using this key in your Application.
Your users (some of them at least) will EXPECT Windows to behave the way it
normally does when F10 is pressed.

If you really MUST have F10, why not use Shift, Ctrl, or Alt with it?

Pete.

"Martin Dannerstedt" <martin.dannerstedt@ebox.tninet.se> wrote in message
news:dfc31c53.0309300237.4b32b95f@posting.google.com...
> I would like to trap the functionkey F10 in DialogSystem.
> It is not possible by the DS Event F10 because F10 is an shortkey in
…[12 more quoted lines elided]…
> Martin Dannerstedt
```

##### ↳ ↳ Re: Trap F10 in MicroFocus DialogSystem

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-09-30T11:25:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hKdeb.23205$ev2.4618211@newssrv26.news.prodigy.com>`
- **References:** `<dfc31c53.0309300237.4b32b95f@posting.google.com> <3f796357_9@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3f796357_9@news.athenanews.com...
> Martin,
>
…[4 more quoted lines elided]…
> int 16 (which you CAN'T in Windows) and looking at each keystroke, you
would
> still need to pass the event to Windows and it will then implement F10
> behaviour.

But under Windows you can install a global keyboard hook, which will 'net'
out to the same thing as a TSR did under MS-DOS. You install the hook, which
directs all or selected messages (each keystroke generates a message)  (
this is how spyware works) to a user-written procedure; then in that hook
procedure you either process the key yourself (in this case, you'd process
F10); pass the keystroke along to Windows for 'normal' processing; or 'eat'
the key.

Better remember to uninstall your hook when your program ends, or else all
system keystrokes will go directly to Anaheim, California:Fantasyland.  And
uninistalling when your program goes belly-up - as I'm sure happens whilst
still developing - is REALLY difficult to do, but it CAN be done.
(Fortunately, 'Reboot' is a universal fix for an unterminated hook chain).

Not sure if/how this would/could work, though, if the program is an MS-DOS
program. AFAIK, these hooks can only be installed and used by a Windows
program. I have one installed now by my now-unused Internet dialup software
which came with the system; and my F1 key from a DOS session under Win/98
always results in a "Illegal instruction" error and I have to terminate and
restart the DOS session.

Maybe if I get some time I can play around with this. I've never done it,
but there's some PD code on my BASIC compiler website and I've RTFM.. enough
faith that I'd take a look/take a job to create a simple DLL on an "if it
don't work, you pay nothing" basis.

Post here or contact me directly if interested.
```

###### ↳ ↳ ↳ Re: Trap F10 in MicroFocus DialogSystem

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-10-01T11:12:06+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f7a2b04$1_3@news.athenanews.com>`
- **References:** `<dfc31c53.0309300237.4b32b95f@posting.google.com> <3f796357_9@news.athenanews.com> <hKdeb.23205$ev2.4618211@newssrv26.news.prodigy.com>`

```
Thanks Michael,

I wasn't aware of that.

Where can I get such a hook?

(purely for "research" ...)

Pete.

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:hKdeb.23205$ev2.4618211@newssrv26.news.prodigy.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
> news:3f796357_9@news.athenanews.com...
> > Martin,
> >
> > it is HIGHLY unlikely that you can effectively "disable" F10 in a
Windows
> > environment.
> >
> > Even if you COULD do the old TSR trick of hooking the interrupt vector
for
> > int 16 (which you CAN'T in Windows) and looking at each keystroke, you
> would
…[4 more quoted lines elided]…
> out to the same thing as a TSR did under MS-DOS. You install the hook,
which
> directs all or selected messages (each keystroke generates a message)  (
> this is how spyware works) to a user-written procedure; then in that hook
> procedure you either process the key yourself (in this case, you'd process
> F10); pass the keystroke along to Windows for 'normal' processing; or
'eat'
> the key.
>
> Better remember to uninstall your hook when your program ends, or else all
> system keystrokes will go directly to Anaheim, California:Fantasyland.
And
> uninistalling when your program goes belly-up - as I'm sure happens whilst
> still developing - is REALLY difficult to do, but it CAN be done.
…[4 more quoted lines elided]…
> program. I have one installed now by my now-unused Internet dialup
software
> which came with the system; and my F1 key from a DOS session under Win/98
> always results in a "Illegal instruction" error and I have to terminate
and
> restart the DOS session.
>
> Maybe if I get some time I can play around with this. I've never done it,
> but there's some PD code on my BASIC compiler website and I've RTFM..
enough
> faith that I'd take a look/take a job to create a simple DLL on an "if it
> don't work, you pay nothing" basis.
…[15 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Trap F10 in MicroFocus DialogSystem

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-10-01T12:49:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k3Aeb.23665$ev2.4900062@newssrv26.news.prodigy.com>`
- **References:** `<dfc31c53.0309300237.4b32b95f@posting.google.com> <3f796357_9@news.athenanews.com> <hKdeb.23205$ev2.4618211@newssrv26.news.prodigy.com> <3f7a2b04$1_3@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3f7a2b04$1_3@news.athenanews.com...
> Thanks Michael,
>
> I wasn't aware of that.
>
> Where can I get such a hook?

You don't 'get' a hook like this, you code it into your program.

The principal Windows API calls you use are SetWindowsHookEx, CallNextHookEx
and UnhookWindowsHookEx; there are some other calls in the 'family' you will
use depending on what it is you code into your hook procedure.

Note that you only want to install a hook of you want to trap keys
REGARDLESS of which window currently has the keyboard focus... if you want
to pick up F10 keys pressed WHILE YOUR PROGRAM HAS KEYBOARD FOCUS it would
be a lot smarter to just intercept the WM_CHAR and/or WM_KEYDOWN messages in
your own program.

The "problem" with trying to take action on "when key pressed" under Windows
is, of course, that Windows is Multi-tasking.. and you have to ask, "did the
user press F10 for MY program? Or someone else's program?"

There is actually a current discussion of this topic on my BASIC language
BBS, and the bottom line seems to be, "sure, using a TSR-Like setup
(specific action on a key regardless of where program is currently
executing) is fine for MS-DOS programs, but it does not make sense under
Windows, because of the possibility some other program should currently be
the recipient of keystrokes (which cannot happen under MS-DOS)."

i..e, "When in the Windows (event driven)  world, you have to break with
MS-DOS (procedural, down-the-page) thinking."
```

###### ↳ ↳ ↳ Re: Trap F10 in MicroFocus DialogSystem

_(reply depth: 5)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-10-02T15:32:46+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f7bba1b_1@news.athenanews.com>`
- **References:** `<dfc31c53.0309300237.4b32b95f@posting.google.com> <3f796357_9@news.athenanews.com> <hKdeb.23205$ev2.4618211@newssrv26.news.prodigy.com> <3f7a2b04$1_3@news.athenanews.com> <k3Aeb.23665$ev2.4900062@newssrv26.news.prodigy.com>`

```

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:k3Aeb.23665$ev2.4900062@newssrv26.news.prodigy.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
> news:3f7a2b04$1_3@news.athenanews.com...
…[8 more quoted lines elided]…
> The principal Windows API calls you use are SetWindowsHookEx,
CallNextHookEx
> and UnhookWindowsHookEx; there are some other calls in the 'family' you
will
> use depending on what it is you code into your hook procedure.
>
…[3 more quoted lines elided]…
> be a lot smarter to just intercept the WM_CHAR and/or WM_KEYDOWN messages
in
> your own program.
>
> The "problem" with trying to take action on "when key pressed" under
Windows
> is, of course, that Windows is Multi-tasking.. and you have to ask, "did
the
> user press F10 for MY program? Or someone else's program?"
>
…[9 more quoted lines elided]…
>

Thanks again, Michael.

Even under DOS it was necessary to pass hooked interrupt vectors back when
you had finished with them, if  you wanted your TSR to behave properly...

I am very comfortable with event driven programming and understand the
implications you outlined.

It was precisely because of this that I suggested it would be highly
improbable for Windows to allow F10 trapping. (I was wrong; obviously, if
people want this, then the market, as always, responds...)

As for using the WinAPI to do this (I have no problem with using it...NOW;
it drove me up the wall when I first tried...), I hadn't realised these
functions were in it, but, now I know, I'll look at it when the need arises.

Pete.
```

##### ↳ ↳ Re: Trap F10 in MicroFocus DialogSystem

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2003-09-30T18:22:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gcijnvg4ref6ubpeflo1b88g05adsgjmpp@4ax.com>`
- **References:** `<dfc31c53.0309300237.4b32b95f@posting.google.com> <3f796357_9@news.athenanews.com>`

```
Peter:

I believe that COBOL sp2 allows the programmer to override the F10 key
in Windows, if desired.  We always suggest maintaining the default
behavior, if at all possible, but because many of our customers
migrate from other environments, they want to keep the same key values
as used in the prior system.



"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

>Martin,
>
…[37 more quoted lines elided]…
>


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: Trap F10 in MicroFocus DialogSystem

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-09-30T16:04:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F79AAAC.DCB05D97@shaw.ca>`
- **References:** `<dfc31c53.0309300237.4b32b95f@posting.google.com>`

```


Martin Dannerstedt wrote:

> I would like to trap the functionkey F10 in DialogSystem.
> It is not possible by the DS Event F10 because F10 is an shortkey in
…[12 more quoted lines elided]…
> Martin Dannerstedt

As suggested by PECD check with M/F - go to home page microfocus.com and
sign up for Answer Exchange (a freebie) - assuming you are using Net
Express - put your query on Dialog System in there.

I don't use Dialog system, but as to catching the F10 - check one of the
OO demos  which contains the following :-

copy "keys.cpy".        *> Keyboard Virtual Keys
copy "listflag.cpy".      *> ListBox flags - included for info
copy "p2cevent.cpy".  *> p2ce Event flags

'keys.cpy" has :-

78  OVK-F10            value h"79".

As regards OO support - check out :-

"C:\Program Files\MERANT\Net Express\Base\Bin\MFNXCL31.CHM"

From the index, select "wantAllKeys" as a starter.

Jimmy, Calgary AB
```

#### ↳ Re: Trap F10 in MicroFocus DialogSystem

- **From:** jean.villemaire@microfocus.com (Jean Villemaire)
- **Date:** 2003-09-30T15:11:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b9b30ab.0309301411.1d2ef6d8@posting.google.com>`
- **References:** `<dfc31c53.0309300237.4b32b95f@posting.google.com>`

```
Martin,

If you want to see an example on how this can be done you can go to
http://supportline.microfocus.com on the left side of the page click
on the Self-Service menu then Net Express Examples & Utilities then
Samples.

In the Dialog System sectin of the page you will find a demo program
called TrapF10.zip, it will show you how this can be done.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
