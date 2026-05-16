[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PowerCOBOL and DCOM

_4 messages · 3 participants · 2003-10_

---

### PowerCOBOL and DCOM

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-10-05T18:27:26+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f7fd718_9@news.athenanews.com>`

```
I have been assisting another Fujitsu PowerCOBOL user to get a system
deployed.

The system is developed using COM components written in PowerCOBOL.

We need for one of these components to be remotely deployed on various
networked machines.

In effect, a process running on a server (machine A), needs to remotely
invoke this component on another machine (Machine B). (Actually it needs to
do it on a number of machines, but we'll stick with A and B for the purposes
of this exercise...)

We installed the component on machine B, registered and ran it successfully.
Just for good measure, I also embedded it into an ASP page and tried serving
that from IIS... It all ran flawlessly...very encouraging.

This is pretty standard DCOM stuff and we duly set up the component under
Component Services on Machine B, exported the generated MSI package for it,
and installed this on Machine A as an Application Proxy. The effect is that
Machine A's Registry now has  a cross referenced entry that says "when you
are told to invoke the Methods of this component, go and do it on Machine
B". (in fact, the Component does not exist on Machine A...)

All pretty standard DCOM stuff. (If you think writing COBOL is hard work,
try wading through the Access permissions you need to get things talking to
each other on a LAN or IntraNet...Network Administrators have my deepest
sympathy and respect...).

Came the big moment ..."Start 'er up..."

Process starts on Machine A then dies as a simultaneous message box appears
on Machine B:

From Powercobol... "Error occurred: Invalid argument when calling the
method, setting or getting the property.".

As this is coming from  (in COBOL):

...
invoke COMClassObject "CREATE-OBJECT" using COMProgID

returning COMObj
end-invoke

...and, as the SAME code has been tested and found to work when invoked
locally on Machine B, we were a bit nonplussed by it.

Fujitsu Support was enlisted without success.

PowerCOBOL documentation fails to document this message, or even give a hint
that there MIGHT be a problem remotely invoking PowerCOBOL ActiveX controls.
(On the contrary, it encourages you to build component based systems and
makes much of the fact that these .DLLs are COM compatible. If that is so,
then they should be deployable under Distributed COM...My experience is that
they are NOT...)

MSDN was searched for clues as to ways we could have incorrectly configured
either MachineA, Machine B, or both, all to no avail. I spent hours reading
and absorbing the fine points of DCOM and Component Services. (I am none the
wiser, but I am certainly better informed...). We tried EVERYTHING we could
collectively think of to get over this problem. At least 60 different
configurations were methodically tested; all without any success.

Eventually, I wrote an OO COBOL "wrapper" for the PowerCOBOL component and
succeeded in getting this to run correctly on Machine B when invoked from
Machine A, as an application proxy. (By removing the direct exposure to
PowerCOBOL, it functioned as it should.)

The reason I'm posting this is for two reasons:

1. If any of you have deployed PowerCOBOL components under DCOM, maybe you
can give me a pointer as to where we failed?

2. If any of you are considering doing so, please be advised of this
experience.

PowerCOBOL is a superb product. It generally delivers everything it claims
to. I have used it with complete satisfaction and even delight, for some
years now.

This is the first time I have tried deploying it under DCOM.

The Fujitsu COBOL Manual (NOT the PowerCOBOL Manual) gives extensive high
quality examples of how to do this with NetCOBOL. You can create COM servers
in Net COBOL and they deploy properly under DCOM.

Sadly, the same cannot be said for PowerCOBOL.  There are NO examples of
deployment, even in a normal COM environment, no hints on configuring
Component Services, no options in the Build to allow the use of Remote
Procedure Calling. The PowerCOBOL document simply shows how to make an
ActiveX and drop it onto other Controls/forms. (This is good as far as it
goes, but it doesn't go far enough...)

 Furthermore, for a product to produce undocumented and unknown error
messages is really unacceptable. Nobody was able to tell me under what
circumstances this message is produced, or what is REALLY happening that has
caused the failure. (I won't repeat here the advice we DID receive, it would
serve no purpose and it certainly wouldn't help anybody.)

If any of you can shed any light on this, I would be grateful to hear of
your experience.

Pete.
```

#### ↳ Re: PowerCOBOL and DCOM

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-10-05T06:04:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0310050504.31a4d55c@posting.google.com>`
- **References:** `<3f7fd718_9@news.athenanews.com>`

```
Pete,

There is a subtle difference between a COM object and an ActiveX
control.  An activeX control - generally - requires a window (called a
container) in which to live.  A COM server - specifically one designed
for DCOM - does not.  I expect this is the root cause of your issue
and why the component can't be deployed as a DCOM server - becuause
running as such a service the window creation necessary to host the
control is going to fail.  As you found, Fujitsu does document COM
servers specifically for DCOM use but not within the realm of
PowerCOBOL.  I'd be very suprised if it could ever work via
PowerCOBOL.

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message news:<3f7fd718_9@news.athenanews.com>...
> I have been assisting another Fujitsu PowerCOBOL user to get a system
> deployed.
…[101 more quoted lines elided]…
> Pete.
```

##### ↳ ↳ Re: PowerCOBOL and DCOM

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-10-06T09:19:37+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f80a833_9@news.athenanews.com>`
- **References:** `<3f7fd718_9@news.athenanews.com> <bfdfc3e8.0310050504.31a4d55c@posting.google.com>`

```

"Thane Hubbell" <thaneh@softwaresimple.com> wrote in message
news:bfdfc3e8.0310050504.31a4d55c@posting.google.com...
> Pete,
>
…[10 more quoted lines elided]…
>

Yes, I'm sure you're right. However, there is absolutely NOTHING in the
PowerCOBOL documentation that draws this distinction.

You have summed it up in one paragraph.

If such a paragraph was inserted in the PowerCOBOL Users' Guide, it would
have saved me around 36 hours of intense effort...

As I said, the manual makes much of the fact that PowerCOBOL .DLLs are COM
objects. And they are, and you can use them as such, PROVIDED you don't try
and remotely deploy them with DCOM.  The fine distinction between ActiveX
and COM is one that most COBOL programmers (self included, up until
recently...) would NOT be aware of.

Now, you COULD argue that I should have been aware of the fact that
PowerCOBOL components have a "container" (in the form of a default form). I
was aware of that. I just didn't expect it to be a problem. How could I know
that the PowerCOBOL window would not open under DCOM? It opens OK when I run
it as a COM component on a Web Page or the Windows desktop. There were no
clues or warnings. A huge amount of time (and money...) was spent in
designing and building a component based system, using the principles
promoted by Fujitsu. It worked fine in simulation. Then we found that when
it came to the actual Network, it simply couldn't be deployed...

It's a very unpleasant experience and I wouldn't wish it on anyone.
Hopefully, posting it here will ensure that others will be able to avoid it.

As my old Dad used to say: "Experience is the best teacher, but her fees are
very high...".

Thanks for your comments Thane.

Pete.


> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:<3f7fd718_9@news.athenanews.com>...
> > I have been assisting another Fujitsu PowerCOBOL user to get a system
> > deployed.
…[7 more quoted lines elided]…
> > invoke this component on another machine (Machine B). (Actually it needs
to
> > do it on a number of machines, but we'll stick with A and B for the
purposes
> > of this exercise...)
> >
> > We installed the component on machine B, registered and ran it
successfully.
> > Just for good measure, I also embedded it into an ASP page and tried
serving
> > that from IIS... It all ran flawlessly...very encouraging.
> >
> > This is pretty standard DCOM stuff and we duly set up the component
under
> > Component Services on Machine B, exported the generated MSI package for
it,
> > and installed this on Machine A as an Application Proxy. The effect is
that
> > Machine A's Registry now has  a cross referenced entry that says "when
you
> > are told to invoke the Methods of this component, go and do it on
Machine
> > B". (in fact, the Component does not exist on Machine A...)
> >
> > All pretty standard DCOM stuff. (If you think writing COBOL is hard
work,
> > try wading through the Access permissions you need to get things talking
to
> > each other on a LAN or IntraNet...Network Administrators have my deepest
> > sympathy and respect...).
…[3 more quoted lines elided]…
> > Process starts on Machine A then dies as a simultaneous message box
appears
> > on Machine B:
> >
…[16 more quoted lines elided]…
> > PowerCOBOL documentation fails to document this message, or even give a
hint
> > that there MIGHT be a problem remotely invoking PowerCOBOL ActiveX
controls.
> > (On the contrary, it encourages you to build component based systems and
> > makes much of the fact that these .DLLs are COM compatible. If that is
so,
> > then they should be deployable under Distributed COM...My experience is
that
> > they are NOT...)
> >
> > MSDN was searched for clues as to ways we could have incorrectly
configured
> > either MachineA, Machine B, or both, all to no avail. I spent hours
reading
> > and absorbing the fine points of DCOM and Component Services. (I am none
the
> > wiser, but I am certainly better informed...). We tried EVERYTHING we
could
> > collectively think of to get over this problem. At least 60 different
> > configurations were methodically tested; all without any success.
> >
> > Eventually, I wrote an OO COBOL "wrapper" for the PowerCOBOL component
and
> > succeeded in getting this to run correctly on Machine B when invoked
from
> > Machine A, as an application proxy. (By removing the direct exposure to
> > PowerCOBOL, it functioned as it should.)
…[3 more quoted lines elided]…
> > 1. If any of you have deployed PowerCOBOL components under DCOM, maybe
you
> > can give me a pointer as to where we failed?
> >
…[3 more quoted lines elided]…
> > PowerCOBOL is a superb product. It generally delivers everything it
claims
> > to. I have used it with complete satisfaction and even delight, for some
> > years now.
…[3 more quoted lines elided]…
> > The Fujitsu COBOL Manual (NOT the PowerCOBOL Manual) gives extensive
high
> > quality examples of how to do this with NetCOBOL. You can create COM
servers
> > in Net COBOL and they deploy properly under DCOM.
> >
…[4 more quoted lines elided]…
> > ActiveX and drop it onto other Controls/forms. (This is good as far as
it
> > goes, but it doesn't go far enough...)
> >
> >  Furthermore, for a product to produce undocumented and unknown error
> > messages is really unacceptable. Nobody was able to tell me under what
> > circumstances this message is produced, or what is REALLY happening that
has
> > caused the failure. (I won't repeat here the advice we DID receive, it
would
> > serve no purpose and it certainly wouldn't help anybody.)
> >
…[3 more quoted lines elided]…
> > Pete.
```

###### ↳ ↳ ↳ Re: PowerCOBOL and DCOM

- **From:** pvieira@emporsoft.pt (Paulo Vieira)
- **Date:** 2003-10-07T02:08:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5b8d7c7.0310070108.1e326377@posting.google.com>`
- **References:** `<3f7fd718_9@news.athenanews.com> <bfdfc3e8.0310050504.31a4d55c@posting.google.com> <3f80a833_9@news.athenanews.com>`

```
[...](long message sniped)

Thank you for sharing this!

best regards

Paulo Vieira, Emporsoft
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
