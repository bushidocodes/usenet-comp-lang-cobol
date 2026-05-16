[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress .. A VB alternative ??

_13 messages · 7 participants · 1999-05_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### NetExpress .. A VB alternative ??

- **From:** Bogy@Texas.NEt (Peter Gilchrist)
- **Date:** 1999-05-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3745630b.2694269@news.texas.net>`

```
We are thinking of upgrading our MF Object Cobol 32 to NetExpress.
Currently, our MF cobol does a half-assed job at making application
front ends.   Will NetExpress provide a full Windows 95 GUI
application, much like we're using Visual Basic for now ??
```

#### ↳ Re: NetExpress .. A VB alternative ??

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-6WpSydtn8RfY@Dwight_Miller.iix.com>`
- **References:** `<3745630b.2694269@news.texas.net>`

```
On Fri, 21 May 1999 13:47:09, Bogy@Texas.NEt (Peter Gilchrist) wrote:

> We are thinking of upgrading our MF Object Cobol 32 to NetExpress.
> Currently, our MF cobol does a half-assed job at making application
> front ends.   Will NetExpress provide a full Windows 95 GUI
> application, much like we're using Visual Basic for now ??

The Windows GUI in NetExpress is Dialog System.  I don't know of 
anyone who is using it that really likes it.  

Fujitsu PowerCOBOL is more like Visual Basic than NetExpress is.

I prefer a third party tool - that you can use with your EXISTING 
COBOL - cheaper than buying NetExpress to boot - called COBOL sp2 from
Flexus - http://www.flexus.com

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: NetExpress .. A VB alternative ??

- **From:** "Gazaloo" <gaz at home dot com>
- **Date:** 1999-05-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7i3un0$h8m@hyperion.mfltd.co.uk>`
- **References:** `<3745630b.2694269@news.texas.net> <Jl0PnHJ5PvPd-pn2-6WpSydtn8RfY@Dwight_Miller.iix.com>`

```
Thane Hubbell <redsky@ibm.net> wrote in message
news:Jl0PnHJ5PvPd-pn2-6WpSydtn8RfY@Dwight_Miller.iix.com...
> The Windows GUI in NetExpress is Dialog System.  I don't know of
> anyone who is using it that really likes it.

there are over 10,000 active seats using Dialog System. i hope at least some
of them like it!

if Dialog System doesn't ring your bell, try using the web-based Form
Designer (included in Net Express) for building your GUI's.

Gazaloo.
```

###### ↳ ↳ ↳ Re: NetExpress .. A VB alternative ??

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-j5gg2dqwxfJX@Dwight_Miller.iix.com>`
- **References:** `<3745630b.2694269@news.texas.net> <Jl0PnHJ5PvPd-pn2-6WpSydtn8RfY@Dwight_Miller.iix.com> <7i3un0$h8m@hyperion.mfltd.co.uk>`

```
On Fri, 21 May 1999 15:28:59, "Gazaloo" <gaz at home dot com> wrote:

> Thane Hubbell <redsky@ibm.net> wrote in message
> news:Jl0PnHJ5PvPd-pn2-6WpSydtn8RfY@Dwight_Miller.iix.com...
…[5 more quoted lines elided]…
> 

There might be 10,000 active seats of NetExpress - which so far *IS* 
the premier package for delivering an HTML (Browser) interface for 
COBOL applications, but I seriously doubt that all 10,000 are using 
Dialog System.  It would inundate George with bug reports and support 
issues.

> if Dialog System doesn't ring your bell, try using the web-based Form
> Designer (included in Net Express) for building your GUI's.
>

As you can tell, I'm no fan of DS - I have developed full scale 
systems using it, and where I used to work, they are still struggling 
to deploy.  It is unstable in the extreme and very difficult to 
program with.  It's interpreted at runtime making Panels v2 calls that
in turn make calls that interface with the Windows API.  Features in 
older versions disappear in newer versions, (Containers anyone?), and 
it's just a pain ..

The word Dialog is used too much - It describes a type of Windows 
Object, the Product, and the scripting language.  The scripting 
language could have easily been made more COBOL like.

Simple examples appear to work fine - but start using multiple 
windows, events such as "gained" and "lost" focus, and event detection
at the object, window and gloal level and things soon become 
unmanageable.

DSRUNNER was the saving grace of the system in that it handles push 
and pops of screensets from the DS stack, but support for it dwindled 
in later versions of NE.  

I can go on and on.... I'll quit now.

Let's hear from those using it here:  

Who uses Dialog System and likes it?  (Not NetExpress - but rather 
specifically the DS componant).
-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: NetExpress .. A VB alternative ??

_(reply depth: 4)_

- **From:** "Gazaloo" <gaz at home dot com>
- **Date:** 1999-05-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7i423l$knk@hyperion.mfltd.co.uk>`
- **References:** `<3745630b.2694269@news.texas.net> <Jl0PnHJ5PvPd-pn2-6WpSydtn8RfY@Dwight_Miller.iix.com> <7i3un0$h8m@hyperion.mfltd.co.uk> <Jl0PnHJ5PvPd-pn2-j5gg2dqwxfJX@Dwight_Miller.iix.com>`

```

Thane Hubbell <redsky@ibm.net> wrote in message
news:Jl0PnHJ5PvPd-pn2-j5gg2dqwxfJX@Dwight_Miller.iix.com...
> There might be 10,000 active seats of NetExpress - which so far *IS*
> the premier package for delivering an HTML (Browser) interface for
> COBOL applications, but I seriously doubt that all 10,000 are using
> Dialog System.  It would inundate George with bug reports and support
> issues.

i did mean 10,000 Dialog System users. as you probably know, Dialog System
has been around for a good many years (and "too many" say some!) in various
Micro Focus products.

> As you can tell, I'm no fan of DS - I have developed full scale
> systems using it, and where I used to work, they are still struggling
…[4 more quoted lines elided]…
> it's just a pain ..<snip>

fair enough Thane. ain't gonna question your experiences here, but from our
perspective it is very stable and very useable (supports ActiveX an' all
now). is the version in Net Express still painful (or did you give up before
getting here)?

> Let's hear from those using it here:
>
> Who uses Dialog System and likes it?  (Not NetExpress - but rather
> specifically the DS componant).

please.

Gazaloo.
```

###### ↳ ↳ ↳ Re: NetExpress .. A VB alternative ??

_(reply depth: 5)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-LpQuKWMHPt3K@Dwight_Miller.iix.com>`
- **References:** `<3745630b.2694269@news.texas.net> <Jl0PnHJ5PvPd-pn2-6WpSydtn8RfY@Dwight_Miller.iix.com> <7i3un0$h8m@hyperion.mfltd.co.uk> <Jl0PnHJ5PvPd-pn2-j5gg2dqwxfJX@Dwight_Miller.iix.com> <7i423l$knk@hyperion.mfltd.co.uk>`

```
On Fri, 21 May 1999 16:26:56, "Gazaloo" <gaz at home dot com> wrote:

> fair enough Thane. ain't gonna question your experiences here, but from our
> perspective it is very stable and very useable (supports ActiveX an' all
> now). is the version in Net Express still painful (or did you give up before
> getting here)?
> 

I used it with 2.0, but it corrupted projects so often we ended up 
deploying the 16 bit version.

Presently they are attempting to use 3.0 but my last report from them 
(2 months ago) was that while 3.0 was MUCH better from the Development
Tool side, the runtime still suffers instability and machine and OS 
sensitivity.   This is totally separate from the issues of development
style required by the product.

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: NetExpress .. A VB alternative ??

_(reply depth: 4)_

- **From:** Stephen.Biggs@merant.com (Steve Biggs)
- **Date:** 1999-05-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7i43fh$knt@hyperion.mfltd.co.uk>`
- **References:** `<3745630b.2694269@news.texas.net> <Jl0PnHJ5PvPd-pn2-6WpSydtn8RfY@Dwight_Miller.iix.com> <7i3un0$h8m@hyperion.mfltd.co.uk> <Jl0PnHJ5PvPd-pn2-j5gg2dqwxfJX@Dwight_Miller.iix.com>`

```
redsky@ibm.net (Thane Hubbell) wrote:
>As you can tell, I'm no fan of DS - I have developed full scale 
>systems using it, and where I used to work, they are still struggling 
>to deploy.  It is unstable in the extreme and very difficult to 
>program with.  It's interpreted at runtime making Panels v2 calls that
>in turn make calls that interface with the Windows API.  

Thane, 
All Windows GUI products eventually make calls to the Windows API.
In fact, if the feature you want isn't available directly in Dialog 
System, you can often go directly to the API.

>Features in 
>older versions disappear in newer versions, (Containers anyone?), and 
>it's just a pain ..

Containers never disappeared exactly; the problem was that containers were 
an OS/2 control for which a Windows emulation was only available under 
16bit. Containers these days are implemented as an emulation using the 
Windows ListView control.

Finally, newer features such as ActiveX support mean that you don't have 
to use those old controls - you can use a table control bought from a 
third party, perhaps, and put it straight into your screenset.

And *in addition* to all of this, the NetExpress versions of Dialog System 
allow you to access the power of our GUI class libraries, providing yet 
another way for you to add functionality to your DS application (including 
using ListView controls more natively, if you want).

Steve.
```

###### ↳ ↳ ↳ Re: NetExpress .. A VB alternative ??

_(reply depth: 5)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37473af1.336306737@news1.ibm.net>`
- **References:** `<3745630b.2694269@news.texas.net> <Jl0PnHJ5PvPd-pn2-6WpSydtn8RfY@Dwight_Miller.iix.com> <7i3un0$h8m@hyperion.mfltd.co.uk> <Jl0PnHJ5PvPd-pn2-j5gg2dqwxfJX@Dwight_Miller.iix.com> <7i43fh$knt@hyperion.mfltd.co.uk>`

```
On Sat, 22 May 1999 00:51:52 GMT, Stephen.Biggs@merant.com (Steve
Biggs) wrote:

>redsky@ibm.net (Thane Hubbell) wrote:
>>As you can tell, I'm no fan of DS - I have developed full scale 
…[9 more quoted lines elided]…
>

Of course they do!  They don't usually run though so many pieces of
runtime to do it, and are generally not interpretive.
```

###### ↳ ↳ ↳ Re: NetExpress .. A VB alternative ??

_(reply depth: 6)_

- **From:** "Gazaloo" <gaz@home.com>
- **Date:** 1999-05-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fQH13.502$Nb2.978@news.rdc1.sfba.home.com>`
- **References:** `<3745630b.2694269@news.texas.net> <Jl0PnHJ5PvPd-pn2-6WpSydtn8RfY@Dwight_Miller.iix.com> <7i3un0$h8m@hyperion.mfltd.co.uk> <Jl0PnHJ5PvPd-pn2-j5gg2dqwxfJX@Dwight_Miller.iix.com> <7i43fh$knt@hyperion.mfltd.co.uk> <37473af1.336306737@news1.ibm.net>`

```
Thane Hubbell <redsky@ibm.net> wrote:
>It's interpreted at runtime making Panels v2 calls that
>in turn make calls that interface with the Windows API.

yeah, Pan2 is just like Java ;-)
```

#### ↳ Re: NetExpress .. A VB alternative ??

- **From:** "Tony M. Mina" <tony.m.mina@gov.nb.ca>
- **Date:** 1999-05-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7i3vt2$ql5$1@garnet.nbnet.nb.ca>`
- **References:** `<3745630b.2694269@news.texas.net>`

```
Probably the easiest is to use Cobol SP2 from Flexus International for your
GUI
interface.  Visit their site at www.flexus.com and download their evaluation
copy.

Tony M. Mina
jets@nbnet.nb.ca


Peter Gilchrist wrote in message <3745630b.2694269@news.texas.net>...
>We are thinking of upgrading our MF Object Cobol 32 to NetExpress.
>Currently, our MF cobol does a half-assed job at making application
>front ends.   Will NetExpress provide a full Windows 95 GUI
>application, much like we're using Visual Basic for now ??
```

##### ↳ ↳ Re: NetExpress .. A VB alternative ??

- **From:** Bogy@Texas.NEt (Peter Gilchrist)
- **Date:** 1999-05-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37459125.1939069@news.texas.net>`
- **References:** `<3745630b.2694269@news.texas.net> <7i3vt2$ql5$1@garnet.nbnet.nb.ca>`

```
I was initially hoping that NetExpress would encorporate some the the
features found in MicroFocus's "GUI APS" product (which I am not sure
is still available).  It did full Cobol windows GUI application
development.  (It could have been a replacement for VB5, but the
version I used a few years ago lacked some refinement).

It looks like I will settle with using VB5 for my front end and
standard NetExpress cobol for the processing engions.

On Fri, 21 May 1999 13:03:48 -0300, "Tony M. Mina"
<tony.m.mina@gov.nb.ca> wrote:

>Probably the easiest is to use Cobol SP2 from Flexus International for your
>GUI
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: NetExpress .. A VB alternative ??

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-05-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7i4ema$gug@sjx-ixn5.ix.netcom.com>`
- **References:** `<3745630b.2694269@news.texas.net> <7i3vt2$ql5$1@garnet.nbnet.nb.ca> <37459125.1939069@news.texas.net>`

```
I believe that APS is still a "strategic" MERANT product (on the old
Intersolv side of the house - not the Micro Focus side).  I do NOT know how
much "integration" is planned in either the short or long term, but I do
know that you can find APS "stuff" via
    www.merant.com
```

#### ↳ Re: NetExpress .. A VB alternative ??

- **From:** "Simon Cordingley" <simon@casegen.co.uk>
- **Date:** 1999-05-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bea5f3$d0657aa0$4a0870c3@email>`
- **References:** `<3745630b.2694269@news.texas.net>`

```
You might like to look at our product - Casegen Cobol for Windows
Professional - it generates Windows GUI Cobol for the Fujitsu compiler. The
result is a very fast stable Windows application, and its only $125 US. 

Simon Cordingley
Casegen Systems Ltd
simon@casegen.co.uk
www.casegen.co.uk

Peter Gilchrist <Bogy@Texas.NEt> wrote in article
<3745630b.2694269@news.texas.net>...
> We are thinking of upgrading our MF Object Cobol 32 to NetExpress.
> Currently, our MF cobol does a half-assed job at making application
> front ends.   Will NetExpress provide a full Windows 95 GUI
> application, much like we're using Visual Basic for now ??
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
