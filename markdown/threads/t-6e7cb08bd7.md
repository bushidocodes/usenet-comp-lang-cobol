[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol / Linux / X-Windows

_24 messages · 12 participants · 2009-02 → 2009-08_

---

### Cobol / Linux / X-Windows

- **From:** Paul <paul-nospamatall.raulerson@mac.com>
- **Date:** 2009-02-14T22:53:13-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net>`

```
Oh how do I get myself into nasty little messes like this?
A friend of mine was laid off from his job (damn bank!)
and is now getting in pretty desparate straights. So he took
a consulting job - on spec no less - and has been handed a mess.

His project is to port some old PrimeOS (!!) Cobol code to Linux.
So I gave him an x86 box with Linux and OpenCOBOL installed on it.
And he was off. Till the buggers he contracted with sprung a surprise on
him - they are demanding that he produce a Linux GUI.

(damn bank! damn bank#2!)

Does anyone have any experience with hooking OpenCOBOL into
XWindows? And if so, would you be willing to share a few tips
with me on how to go about doing it??

Ill help him do this someway or another, by hooking in C wrapper
routines if I have to, but I sure would like to avoid taking all the time
to do that if there is a faster way. I am a bit in overload myself right
now... :(

<mutter> PrimeOS! In 2009. To XWindows! 
Unbelievable...<cuss>*(*&@&#!</cuss></mutter>
Thanks
-Paul
```

#### ↳ Re: Cobol / Linux / X-Windows

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-02-15T00:26:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zAOll.11365$Rp1.7477@en-nntp-01.dc1.easynews.com>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net>`

```
Have you tried asking this at:
   http://www.opencobol.org/

If anyone could help you, I would think they might.  There is also a list for 
the project that might have some ideas. See:
 https://lists.sourceforge.net/lists/listinfo/open-cobol-list

*OBVIOUSLY* if the end-user (bank) were to pay for it, going with one of the 
"commercial" compilers (e.g. Fujitsu, Micro Focus - or the "AcuCOBOL" part of 
Micro Focus) would give him INSTANT support for GUI's under Linux.  However, 
those are not cheap.
```

##### ↳ ↳ Re: Cobol / Linux / X-Windows

- **From:** Paul <paul-nospamatall.raulerson@mac.com>
- **Date:** 2009-02-15T04:44:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4997f20d$0$5469$bbae4d71@news.suddenlink.net>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net> <zAOll.11365$Rp1.7477@en-nntp-01.dc1.easynews.com>`

```
On 2009-02-15 00:26:38 -0600, "William M. Klein" 
<wmklein@nospam.ix.netcom.com> said:

> Have you tried asking this at:
>    http://www.opencobol.org/
…[8 more quoted lines elided]…
> those are not cheap.

I scanned the web site Bill, but I didn't find a good answer. A good 
bit of religion, but
nobody that had actually used it. Besides, I am far more used to seeing 
real answers
from this group. :)

I would move him to MicroFocus in an instant, but the customer won't 
pay, and $22K
per server is a bit high for my charity budget at this point.  Besides, 
I am not at all
sure Microfocus is even supporting GUI under LInux- they seem to be pretty
Windows Centric lately- with .NET being their primary target.

Thanks -Paul
```

###### ↳ ↳ ↳ Re: Cobol / Linux / X-Windows

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2009-02-15T18:03:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vr3odFl68g9U2@mid.individual.net>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net> <zAOll.11365$Rp1.7477@en-nntp-01.dc1.easynews.com> <4997f20d$0$5469$bbae4d71@news.suddenlink.net>`

```
In article <4997f20d$0$5469$bbae4d71@news.suddenlink.net>,
	Paul <paul-nospamatall.raulerson@mac.com> writes:
> On 2009-02-15 00:26:38 -0600, "William M. Klein" 
> <wmklein@nospam.ix.netcom.com> said:
…[24 more quoted lines elided]…
> Windows Centric lately- with .NET being their primary target.

Well, to be sure, the info is a little sketchy but having worked with
Primes quite a bit in a previous life I can guess at the complexity and
UI that the programs might have.  That being said, how about just porting
the programs and then putting a TK/TCL frontend on them to provide the
GUI?

bill
```

###### ↳ ↳ ↳ Re: Cobol / Linux / X-Windows

_(reply depth: 4)_

- **From:** Paul <paul-nospamatall.raulerson@mac.com>
- **Date:** 2009-02-15T19:37:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4998c33c$0$5499$bbae4d71@news.suddenlink.net>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net> <zAOll.11365$Rp1.7477@en-nntp-01.dc1.easynews.com> <4997f20d$0$5469$bbae4d71@news.suddenlink.net> <6vr3odFl68g9U2@mid.individual.net>`

```
On 2009-02-15 12:03:57 -0600, billg999@cs.uofs.edu (Bill Gunshannon) said:

> In article <4997f20d$0$5469$bbae4d71@news.suddenlink.net>,
> 	Paul <paul-nospamatall.raulerson@mac.com> writes:
…[34 more quoted lines elided]…
> bill

That is an excellent idea- you wouldn't happen to have an example of doing just
that laying around you would be willing to share would you? :)

I had forgotten about TK/TCL. That might just be the very best way to do it.

-Paul
```

###### ↳ ↳ ↳ Re: Cobol / Linux / X-Windows

_(reply depth: 5)_

- **From:** Vaclav Snajdr <vsn@snajdr.de>
- **Date:** 2009-02-16T11:24:24+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnbevh$4u3$01$1@news.t-online.com>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net> <zAOll.11365$Rp1.7477@en-nntp-01.dc1.easynews.com> <4997f20d$0$5469$bbae4d71@news.suddenlink.net> <6vr3odFl68g9U2@mid.individual.net> <4998c33c$0$5499$bbae4d71@news.suddenlink.net>`

```
www.magro-soft.com has built an interface between Cobol and Tcl/Tk for GUI.
I know the his version MF-Cobol <--> Tcl/Tk. 


Paul wrote:

> On 2009-02-15 12:03:57 -0600, billg999@cs.uofs.edu (Bill Gunshannon) said:
> 
…[45 more quoted lines elided]…
> -Paul
```

###### ↳ ↳ ↳ Re: Cobol / Linux / X-Windows

_(reply depth: 5)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2009-02-16T13:23:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vt7lpFlpb3bU2@mid.individual.net>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net> <zAOll.11365$Rp1.7477@en-nntp-01.dc1.easynews.com> <4997f20d$0$5469$bbae4d71@news.suddenlink.net> <6vr3odFl68g9U2@mid.individual.net> <4998c33c$0$5499$bbae4d71@news.suddenlink.net>`

```
In article <4998c33c$0$5499$bbae4d71@news.suddenlink.net>,
	Paul <paul-nospamatall.raulerson@mac.com> writes:
> On 2009-02-15 12:03:57 -0600, billg999@cs.uofs.edu (Bill Gunshannon) said:
> 
…[42 more quoted lines elided]…
> 

Well, I don't, but ecven if I had examples laying aroiund there has hardly
been enough info about the project provided for anyone to post a reasonable
example of how to do it.  I just threw that out as an option.  Even the
concept GUI is undefined.  If a Web interface is considered an acceptable
"Linux GUI" it is even easier as OpenCOBOL works find for CGI.

bill
```

###### ↳ ↳ ↳ Re: Cobol / Linux / X-Windows

_(reply depth: 6)_

- **From:** PR <paul.raulerson@gmail.com>
- **Date:** 2009-02-16T07:22:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c08dbcbc-2ade-4b4a-904c-48af441c3771@l38g2000vba.googlegroups.com>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net> <zAOll.11365$Rp1.7477@en-nntp-01.dc1.easynews.com> <4997f20d$0$5469$bbae4d71@news.suddenlink.net> <6vr3odFl68g9U2@mid.individual.net> <4998c33c$0$5499$bbae4d71@news.suddenlink.net> <6vt7lpFlpb3bU2@mid.individual.net>`

```
On Feb 16, 7:23 am, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
> In article <4998c33c$0$5499$bbae4...@news.suddenlink.net>,
>         Paul <paul-nospamatall.rauler...@mac.com> writes:
…[60 more quoted lines elided]…
> Scranton, Pennsylvania   |         #include <std.disclaimer.h>  

Okay Bill - how about a screen that sets up one input field, edit
checked to be numeric, and displays a text message after the user hits
enter.

-Paul
```

###### ↳ ↳ ↳ Re: Cobol / Linux / X-Windows

_(reply depth: 7)_

- **From:** btiffin@canada.com
- **Date:** 2009-02-16T12:42:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1cc53d05-c287-4b6d-b40a-39d1dcc54676@u1g2000vbb.googlegroups.com>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net> <zAOll.11365$Rp1.7477@en-nntp-01.dc1.easynews.com> <4997f20d$0$5469$bbae4d71@news.suddenlink.net> <6vr3odFl68g9U2@mid.individual.net> <4998c33c$0$5499$bbae4d71@news.suddenlink.net> <6vt7lpFlpb3bU2@mid.individual.net> <c08dbcbc-2ade-4b4a-904c-48af441c3771@l38g2000vba.googlegroups.com>`

```
On Feb 16, 10:22 am, PR <paul.rauler...@gmail.com> wrote:
> On Feb 16, 7:23 am, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
>
…[68 more quoted lines elided]…
> -Paul

Not replying for Bill.  But I've done a little bit with GTK+ for
OpenCOBOL.  The plan is a near full on binding to the GnomeToolKit,
but for now.  Buttons, Labels, Menus, File Dialog, a Calendar widget
(and a few odds and sods), enough for simple but fully functional
GUIs.

A sample screenshot and some source code can be seen at
http://add1tocobol.com/tiki-index.php?page=GTK+Sample

We've also taken Rildo's Tcl/Tk engine from TinyCOBOL and interfaced
that into OpenCOBOL as well.  For that layer most of the GUI work is
squarely on the Tk side.

Cheers,
Brian
```

###### ↳ ↳ ↳ Re: Cobol / Linux / X-Windows

_(reply depth: 8)_

- **From:** PR <paul.raulerson@gmail.com>
- **Date:** 2009-02-16T13:37:11-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d302512f-8772-4300-91c8-1ecea10768e0@v31g2000vbb.googlegroups.com>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net> <zAOll.11365$Rp1.7477@en-nntp-01.dc1.easynews.com> <4997f20d$0$5469$bbae4d71@news.suddenlink.net> <6vr3odFl68g9U2@mid.individual.net> <4998c33c$0$5499$bbae4d71@news.suddenlink.net> <6vt7lpFlpb3bU2@mid.individual.net> <c08dbcbc-2ade-4b4a-904c-48af441c3771@l38g2000vba.googlegroups.com> <1cc53d05-c287-4b6d-b40a-39d1dcc54676@u1g2000vbb.googlegroups.com>`

```
On Feb 16, 2:42 pm, btif...@canada.com wrote:
> On Feb 16, 10:22 am, PR <paul.rauler...@gmail.com> wrote:
>
…[85 more quoted lines elided]…
> Brian

Bingo! Perfecto!  This will do the job!  THANK YOU!  :)
-Paul
```

###### ↳ ↳ ↳ Re: Cobol / Linux / X-Windows

_(reply depth: 9)_

- **From:** PR <paul.raulerson@gmail.com>
- **Date:** 2009-02-18T07:47:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ab84de8a-76f6-4a93-aadd-9c3c1313e762@r38g2000vbi.googlegroups.com>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net> <zAOll.11365$Rp1.7477@en-nntp-01.dc1.easynews.com> <4997f20d$0$5469$bbae4d71@news.suddenlink.net> <6vr3odFl68g9U2@mid.individual.net> <4998c33c$0$5499$bbae4d71@news.suddenlink.net> <6vt7lpFlpb3bU2@mid.individual.net> <c08dbcbc-2ade-4b4a-904c-48af441c3771@l38g2000vba.googlegroups.com> <1cc53d05-c287-4b6d-b40a-39d1dcc54676@u1g2000vbb.googlegroups.com> <d302512f-8772-4300-91c8-1ecea10768e0@v31g2000vbb.googlegroups.com>`

```
On Feb 16, 3:37 pm, PR <paul.rauler...@gmail.com> wrote:
> On Feb 16, 2:42 pm, btif...@canada.com wrote:
>
…[90 more quoted lines elided]…
> -Paul

And just as a follow up, let me say Thank You again for all the quick
and helpful responses - especially Bill Klein. :)
Got a prototype up and working last night.

-Paul
```

###### ↳ ↳ ↳ Re: Cobol / Linux / X-Windows

_(reply depth: 10)_

- **From:** btiffin@canada.com
- **Date:** 2009-02-18T19:45:05-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0b070f42-15fb-4a5b-9488-592f36d4b6dd@r28g2000vbp.googlegroups.com>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net> <zAOll.11365$Rp1.7477@en-nntp-01.dc1.easynews.com> <4997f20d$0$5469$bbae4d71@news.suddenlink.net> <6vr3odFl68g9U2@mid.individual.net> <4998c33c$0$5499$bbae4d71@news.suddenlink.net> <6vt7lpFlpb3bU2@mid.individual.net> <c08dbcbc-2ade-4b4a-904c-48af441c3771@l38g2000vba.googlegroups.com> <1cc53d05-c287-4b6d-b40a-39d1dcc54676@u1g2000vbb.googlegroups.com> <d302512f-8772-4300-91c8-1ecea10768e0@v31g2000vbb.googlegroups.com> <ab84de8a-76f6-4a93-aadd-9c3c1313e762@r38g2000vbi.googlegroups.com>`

```
On Feb 18, 10:47 am, PR <paul.rauler...@gmail.com> wrote:
> On Feb 16, 3:37 pm, PR <paul.rauler...@gmail.com> wrote:
>
…[98 more quoted lines elided]…
> -Paul

Hope it works out Paul.  (Assuming the bingo has to do with GTK and
OpenCOBOL - as the thread response is such that I can't be 100% on
that), there will be a lot more to this layer as the days progress.
The functions are fairly easy to wrap (rote programming), but testing
takes a while.  And if it is OpenCOBOL; thanks to Roger and Keisuke
too ... smart cookies ... and we all get to benefit and learn from
their efforts.

Cheers,
Brian
```

###### ↳ ↳ ↳ Re: Cobol / Linux / X-Windows

_(reply depth: 11)_

- **From:** PR <paul.raulerson@gmail.com>
- **Date:** 2009-02-19T08:31:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a4ec7233-ea00-43a5-af39-3bd56b782492@v39g2000pro.googlegroups.com>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net> <zAOll.11365$Rp1.7477@en-nntp-01.dc1.easynews.com> <4997f20d$0$5469$bbae4d71@news.suddenlink.net> <6vr3odFl68g9U2@mid.individual.net> <4998c33c$0$5499$bbae4d71@news.suddenlink.net> <6vt7lpFlpb3bU2@mid.individual.net> <c08dbcbc-2ade-4b4a-904c-48af441c3771@l38g2000vba.googlegroups.com> <1cc53d05-c287-4b6d-b40a-39d1dcc54676@u1g2000vbb.googlegroups.com> <d302512f-8772-4300-91c8-1ecea10768e0@v31g2000vbb.googlegroups.com> <ab84de8a-76f6-4a93-aadd-9c3c1313e762@r38g2000vbi.googlegroups.com> <0b070f42-15fb-4a5b-9488-592f36d4b6dd@r28g2000vbp.googlegroups.com>`

```
On Feb 18, 9:45 pm, btif...@canada.com wrote:
> On Feb 18, 10:47 am, PR <paul.rauler...@gmail.com> wrote:
>
…[111 more quoted lines elided]…
> Brian

Yep, I was replying to you. Thanks!
It is great to have this wonderful Open Source stuff around.
-Paul
```

###### ↳ ↳ ↳ Re: Cobol / Linux / X-Windows

_(reply depth: 12)_

- **From:** btiffin@canada.com
- **Date:** 2009-02-22T07:12:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bb9fc109-29c8-48c1-9d72-197f80a41cf2@d32g2000yqe.googlegroups.com>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net> <zAOll.11365$Rp1.7477@en-nntp-01.dc1.easynews.com> <4997f20d$0$5469$bbae4d71@news.suddenlink.net> <6vr3odFl68g9U2@mid.individual.net> <4998c33c$0$5499$bbae4d71@news.suddenlink.net> <6vt7lpFlpb3bU2@mid.individual.net> <c08dbcbc-2ade-4b4a-904c-48af441c3771@l38g2000vba.googlegroups.com> <1cc53d05-c287-4b6d-b40a-39d1dcc54676@u1g2000vbb.googlegroups.com> <d302512f-8772-4300-91c8-1ecea10768e0@v31g2000vbb.googlegroups.com> <ab84de8a-76f6-4a93-aadd-9c3c1313e762@r38g2000vbi.googlegroups.com> <0b070f42-15fb-4a5b-9488-592f36d4b6dd@r28g2000vbp.googlegroups.com> <a4ec7233-ea00-43a5-af39-3bd56b782492@v39g2000pro.googlegroups.com>`

```
On Feb 19, 11:31 am, PR <paul.rauler...@gmail.com> wrote:
> On Feb 18, 9:45 pm, btif...@canada.com wrote:
>
…[117 more quoted lines elided]…
> -Paul

New news!  New discovery (for me, perhaps old hat for others).  Vala,
http://live.gnome.org/Vala  A programming language designed for
writing code to interface with the Gnome libraries at a high level but
keeping to a C binary interface.  Vala, like OpenCOBOL, does
intermediate C so the object files are directly callable with no
linker name mangling inherent with C++ and many other higher
conceptual programming systems.

I had the valac compiler built from sources, and a GtkTreeView wrapped
in a GtkBuilder (Glade and XML ui files) called from OpenCOBOL all
within an hour.  The OpenCOBOL gui binding layer will now be orders of
magnitude easier to write and manage.  GtkBuilder was already slated
to be one of the nexts piece added to the CBL_OC_GTK_ callables, but
moving from a C based layer to the much higher conceptual Vala level
there will be a lot less glue code required.

While the posted sample doesn't really do much data passing, as I was
in a giddy rush to get the news to the OpenCOBOL folk, I've started a
thread on opencobol.org. More soon;
http://www.opencobol.org/modules/newbb/viewtopic.php?topic_id=526&forum=1&post_id=2700#forumpost2700

OpenCOBOL programmers won't really need to have a Vala compiler when
the binding layer is complete, as it can and will still be published
in object form, but as with all open things, source code will be
available and the compiler is freedom free and zero-cost free.

Very exciting.

Cheers,
Brian
```

###### ↳ ↳ ↳ Re: Cobol / Linux / X-Windows

_(reply depth: 13)_

- **From:** btiffin@canada.com
- **Date:** 2009-02-22T07:29:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<565a7f79-0dcb-4263-8624-cccd1ef62989@r4g2000yqa.googlegroups.com>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net> <zAOll.11365$Rp1.7477@en-nntp-01.dc1.easynews.com> <4997f20d$0$5469$bbae4d71@news.suddenlink.net> <6vr3odFl68g9U2@mid.individual.net> <4998c33c$0$5499$bbae4d71@news.suddenlink.net> <6vt7lpFlpb3bU2@mid.individual.net> <c08dbcbc-2ade-4b4a-904c-48af441c3771@l38g2000vba.googlegroups.com> <1cc53d05-c287-4b6d-b40a-39d1dcc54676@u1g2000vbb.googlegroups.com> <d302512f-8772-4300-91c8-1ecea10768e0@v31g2000vbb.googlegroups.com> <ab84de8a-76f6-4a93-aadd-9c3c1313e762@r38g2000vbi.googlegroups.com> <0b070f42-15fb-4a5b-9488-592f36d4b6dd@r28g2000vbp.googlegroups.com> <a4ec7233-ea00-43a5-af39-3bd56b782492@v39g2000pro.googlegroups.com> <bb9fc109-29c8-48c1-9d72-197f80a41cf2@d32g2000yqe.googlegroups.com>`

```

> OpenCOBOL programmers won't really need to have a Vala compiler when
> the binding layer is complete, as it can and will still be published
…[6 more quoted lines elided]…
> Brian

Gee did I say zero-cost free, when I meant free-beer free?  There are
always costs; freedom doesn't really come without a price.  ;)

Cheers again,
Brian
```

###### ↳ ↳ ↳ Re: Cobol / Linux / X-Windows

_(reply depth: 9)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-02-19T13:01:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnkaaq12t1k@news3.newsguy.com>`
- **In-Reply-To:** `<d302512f-8772-4300-91c8-1ecea10768e0@v31g2000vbb.googlegroups.com>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net> <zAOll.11365$Rp1.7477@en-nntp-01.dc1.easynews.com> <4997f20d$0$5469$bbae4d71@news.suddenlink.net> <6vr3odFl68g9U2@mid.individual.net> <4998c33c$0$5499$bbae4d71@news.suddenlink.net> <6vt7lpFlpb3bU2@mid.individual.net> <c08dbcbc-2ade-4b4a-904c-48af441c3771@l38g2000vba.googlegroups.com> <1cc53d05-c287-4b6d-b40a-39d1dcc54676@u1g2000vbb.googlegroups.com> <d302512f-8772-4300-91c8-1ecea10768e0@v31g2000vbb.googlegroups.com>`

```
PR wrote:
> On Feb 16, 2:42 pm, btif...@canada.com wrote:
>> Not replying for Bill.  But I've done a little bit with GTK+ for
…[11 more quoted lines elided]…
> Bingo! Perfecto!  This will do the job!  THANK YOU!  :)

What, are we ignoring the option of calling XLib directly?  :-)

Of course, a Real Programmer would just open a connection to the X
server and stream hand-crafted X11 protocol requests to it.

(Back in my callow youth, I wrote a number of X clients - including a
window manager - that talked directly to XLib. 'twas a trifle
tiresome. Wrote big chunks of an X11 server too, come to think of it.
In C, though, not COBOL.)

Out of curiosity, Paul, which of Bill's options did you end up going
with - GTK+ or TK?
```

###### ↳ ↳ ↳ Re: Cobol / Linux / X-Windows

_(reply depth: 4)_

- **From:** mba <kungfu-nok2009@nospamldh.org>
- **Date:** 2009-08-11T21:27:20+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4a81c619$0$433$426a74cc@news.free.fr>`
- **In-Reply-To:** `<6vr3odFl68g9U2@mid.individual.net>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net> <zAOll.11365$Rp1.7477@en-nntp-01.dc1.easynews.com> <4997f20d$0$5469$bbae4d71@news.suddenlink.net> <6vr3odFl68g9U2@mid.individual.net>`

```
Bill Gunshannon wrote:
> In article <4997f20d$0$5469$bbae4d71@news.suddenlink.net>,
> 	Paul <paul-nospamatall.raulerson@mac.com> writes:
…[33 more quoted lines elided]…
> bill

Not used it for real, but consider about :
ruby
fx-ruby fxruby
fox-library (C++/ C compatibility)
for quick and eseay dev...
i   libfox-1.6-0                                           - The FOX C++
GUI Toolkit
i   libfox-1.6-dev                                         - Development
files for the FOX C++ GUI Toolkit
i   libfox-1.6-doc                                         -
Documentation of the FOX C++ GUI Toolkit

Built an easy GUI front-end and interface it with either cobol or C
produced result...
```

###### ↳ ↳ ↳ Re: Cobol / Linux / X-Windows

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-02-19T12:54:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnkaap02t1k@news3.newsguy.com>`
- **In-Reply-To:** `<4997f20d$0$5469$bbae4d71@news.suddenlink.net>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net> <zAOll.11365$Rp1.7477@en-nntp-01.dc1.easynews.com> <4997f20d$0$5469$bbae4d71@news.suddenlink.net>`

```
Paul wrote:

> Besides, I am not at all
> sure Microfocus is even supporting GUI under LInux- they seem to be pretty
> Windows Centric lately- with .NET being their primary target.

This isn't particularly relevant to your problem - since, as you've
explained, your friend isn't in a position to use MF COBOL anyway -
but we're just as committed to our Unix / Linux product line as ever.
The MS stuff has been getting most of the press lately, and it's
certainly an area where we're doing a lot of new stuff; but new
versions of the Unix line (Server Express) are coming out on schedule,
largely from the same code base as the Windows line.

But *that* said, I don't think we actually offer a GUI facility as
such for COBOL on Unix / Linux these days. Dialog System on Unix is
character-only.

For our customers who want Unix / Linux GUIs for MF COBOL programs, we
might recommend HTML (using accept/display HTML, or AJAX plus Web
Services, or various other options), or creating a front end in Java
and using our Java interop technology.
```

#### ↳ Re: Cobol / Linux / X-Windows

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2009-02-15T11:52:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KuKdnSdcT6bpywXUnZ2dnUVZ_srinZ2d@earthlink.com>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net>`

```
Paul wrote:
> Oh how do I get myself into nasty little messes like this?
> A friend of mine was laid off from his job (damn bank!)
…[22 more quoted lines elided]…
> -Paul

When the customer changes the specs, that changes the price.
```

##### ↳ ↳ Re: Cobol / Linux / X-Windows

- **From:** Paul <paul-nospamatall.raulerson@mac.com>
- **Date:** 2009-02-15T19:40:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4998c3f0$0$5463$bbae4d71@news.suddenlink.net>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net> <KuKdnSdcT6bpywXUnZ2dnUVZ_srinZ2d@earthlink.com>`

```
On 2009-02-15 11:52:36 -0600, "HeyBub" <heybub@NOSPAMgmail.com> said:

> Paul wrote:
>> Oh how do I get myself into nasty little messes like this?
…[25 more quoted lines elided]…
> When the customer changes the specs, that changes the price.

If it was me, especially in this case, it would cancel the whole deal. 
(damn bank!)

But Kyle ain't me, and he has two small kids and a mortgage. I won't comment
on why he would work for people so - dishonorable. He feels that he is very
desperate.  (damn bank!)

-Paul
```

###### ↳ ↳ ↳ Re: Cobol / Linux / X-Windows

- **From:** docdwarf@panix.com ()
- **Date:** 2009-02-16T02:22:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnaikn$74q$1@reader1.panix.com>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net> <KuKdnSdcT6bpywXUnZ2dnUVZ_srinZ2d@earthlink.com> <4998c3f0$0$5463$bbae4d71@news.suddenlink.net>`

```
In article <4998c3f0$0$5463$bbae4d71@news.suddenlink.net>,
Paul  <paul-nospamatall.raulerson@mac.com> wrote:
>On 2009-02-15 11:52:36 -0600, "HeyBub" <heybub@NOSPAMgmail.com> said:
>
…[4 more quoted lines elided]…
>>> a consulting job - on spec no less - and has been handed a mess.

[snip]

>> When the customer changes the specs, that changes the price.
>
>If it was me, especially in this case, it would cancel the whole deal. 

If it were I, in most cases, I would use the subjunctive... and cancel the 
deal.  I do not contract to paint a shed and then get told 'Oh, and while 
you're at it - and and no change in price, of course - do the rest of the 
house'.

Contracts (when properly written) protect all parties involved.

>(damn bank!)
>
>But Kyle ain't me, and he has two small kids and a mortgage.

He also has specifications - I am assuming this is what is intended by 'on 
spec' - and as a result is bound, by law and contract, to meet them... 
*not* them and the 'and while you're at it'.

DD
```

#### ↳ Re: Cobol / Linux / X-Windows

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2009-02-15T10:58:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<00a82fbc-dc49-44fa-8533-6cb0c39d8d98@v5g2000prm.googlegroups.com>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net>`

```
On Feb 15, 5:53 pm, Paul <paul-nospamatall.rauler...@mac.com> wrote:
> Oh how do I get myself into nasty little messes like this?
> A friend of mine was laid off from his job (damn bank!)
…[8 more quoted lines elided]…
> (damn bank! damn bank#2!)

As long as he is paid by the hour and can push the 'go live' date out
appropriately as the changes to the spec arrive then he probably can
spin this out until retirement (or even after).


> Does anyone have any experience with hooking OpenCOBOL into
> XWindows? And if so, would you be willing to share a few tips
…[5 more quoted lines elided]…
> now... :(

Generally text mode screens are 'program driven', that is the program
determines the sequence of interactions with the user. GUIs are
usually event driven, the user indicates what should happen.

This is not just changing the face of the application, it is changing
the way the program works, and often means a rewrite unless the
program was written originally to cope with such a change.

For GUIs on Linux I use Glade, but I haven't done this with Cobol yet,
I do it with Python. Glade has a designer which draws the screens and
generates an XML file of these. The program then 'just' has to call
glade to draw the screens and link the events to code. With Python/
Glade it just works on Linux, Windows, and my pocket computer.

I would be more inclined with Cobol to make the system run as web-
based 'in the cloud', The GUI will be frames and forms in tables with
Ajax validating the fields and lookups back to the OpenCobol code
running under Apache.

Of course this is also a complete rewrite and uses several languages
(HTML, JavaScript, Cobol).
```

##### ↳ ↳ Re: Cobol / Linux / X-Windows

- **From:** Paul <paul-nospamatall.raulerson@mac.com>
- **Date:** 2009-02-15T19:43:59-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4998c4df$0$5491$bbae4d71@news.suddenlink.net>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net> <00a82fbc-dc49-44fa-8533-6cb0c39d8d98@v5g2000prm.googlegroups.com>`

```
On 2009-02-15 12:58:09 -0600, Richard <riplin@Azonic.co.nz> said:

> On Feb 15, 5:53ï¿½pm, Paul <paul-nospamatall.rauler...@mac.com> wrote:
>> Oh how do I get myself into nasty little messes like this?
…[45 more quoted lines elided]…
> (HTML, JavaScript, Cobol).

MMM- an Ajax based screen does have a lot of advantages. It is pseudo
conversational, and much more similar to a green screen than a normal
GUI. Probably less rewrite in the code.

I think a couple of us could put together web screens quickly enough,
and OpenCOBOL deals well with web CGI programs.

This is worth thinking. Hopefully they will buy off on that. Maybe then
he could spin it into a client/server on Windows or MacOS or something
he can charge a lot more money for.

Thanks -

-Paul
```

#### ↳ Re: Cobol / Linux / X-Windows

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2009-02-15T22:01:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cb017d1-e616-41b9-a94e-9f3bed59159c@g39g2000pri.googlegroups.com>`
- **References:** `<49979fb9$0$5472$bbae4d71@news.suddenlink.net>`

```
>
> Does anyone have any experience with hooking OpenCOBOL into
> XWindows? And if so, would you be willing to share a few tips
> with me on how to go about doing it??
>

Hi Paul,

If I am going to port my Windows (MF) Cobol GUI to Linux, this is
simply no conversion at all. Ubuntu Linux runs with "Wine" application
from within the Linux OS. So simply install the application using
Wine.... of course with MF, you need to install Application Server
module as well.

Tried running MF Cobol application from it and it works well. I do not
know OpenCOBOL though, but if you can manage to have a Cobol-GUI in
Windows using OpenCobol... might as well install it using wine and add
your application. No need of "OS-porting", it is all compatible in
Linux Wine.


Rene
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
