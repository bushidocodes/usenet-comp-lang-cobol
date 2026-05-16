[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# GUI interface - how?

_9 messages · 6 participants · 2004-03_

---

### GUI interface - how?

- **From:** irado@hotpop.com (irado furioso com tudo)
- **Date:** 2004-03-15T22:17:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<59e39cf4.0403152217.2da786fa@posting.google.com>`

```
goodday, friends

I am new to cobol for *nixï¿½es, and I am stuck with the subject.. how
to build a GUI interface inorder to interact with the final user?
he/she wants to insert/retrieve data, so I must build a workable
interface for this.

Ah, it can be either console (ascii) or Gnome/KDE interface.

thankyou

(if possible, please reply also to my e-mail addr)

irado furioso com tudo
```

#### ↳ Re: GUI interface - how?

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-03-16T11:20:39-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Dc-dnZlL3tPZqsrd4p2dnA@giganews.com>`
- **References:** `<59e39cf4.0403152217.2da786fa@posting.google.com>`

```
irado furioso com tudo wrote:
> goodday, friends
>
…[11 more quoted lines elided]…
> irado furioso com tudo

You have two choices:

1. SP2 from Flexus will provide a GUI front-end to your existing code.
2. Re-write in a COBOL that has native GUI support (Fujitsu, for example).
```

##### ↳ ↳ Re: GUI interface - how?

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-03-16T15:21:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0403161521.1c74d5c8@posting.google.com>`
- **References:** `<59e39cf4.0403152217.2da786fa@posting.google.com> <Dc-dnZlL3tPZqsrd4p2dnA@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote

> > Ah, it can be either console (ascii) or Gnome/KDE interface.
 
> You have two choices:

Actually there are dozens of choices, some more useful than others.
 
> 1. SP2 from Flexus will provide a GUI front-end to your existing code.
> 2. Re-write in a COBOL that has native GUI support (Fujitsu, for example).

Fujitsu PowerCobol or .NET are not particularly useful in a Gnome/KDE environment.
```

##### ↳ ↳ Re: GUI interface - how?

- **From:** g.friedrich@fiuka.de (Friedrich)
- **Date:** 2004-03-16T22:27:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcfdd616.0403162227.37108487@posting.google.com>`
- **References:** `<59e39cf4.0403152217.2da786fa@posting.google.com> <Dc-dnZlL3tPZqsrd4p2dnA@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote in message news:<Dc-dnZlL3tPZqsrd4p2dnA@giganews.com>...

> irado furioso com tudo wrote:> You have two choices:
> 
> 1. SP2 from Flexus will provide a GUI front-end to your existing code.
> 2. Re-write in a COBOL that has native GUI support (Fujitsu, for example).

Or: PERCobol from LegacyJ
Or: AcuCobol thin client
```

###### ↳ ↳ ↳ Re: GUI interface - how?

- **From:** ray@rays-web.com (Ray Smith)
- **Date:** 2004-03-17T13:56:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5654fff9.0403171356.12ed6423@posting.google.com>`
- **References:** `<59e39cf4.0403152217.2da786fa@posting.google.com> <Dc-dnZlL3tPZqsrd4p2dnA@giganews.com> <bcfdd616.0403162227.37108487@posting.google.com>`

```
g.friedrich@fiuka.de (Friedrich) wrote in message news:<bcfdd616.0403162227.37108487@posting.google.com>...
> "JerryMouse" <nospam@bisusa.com> wrote in message news:<Dc-dnZlL3tPZqsrd4p2dnA@giganews.com>...
> 
…[6 more quoted lines elided]…
> Or: AcuCobol thin client

As far as I'm aware AcuCOBOL thin client can only be used ona Windows desktop.
Not Gnome like the poster is after.

Has anyone mentioned a web based solution?  Using COBOL and simple CGI would 
be able to deliver a cross platform solution.  That's as long as you are 
willing to live with a browser based interface???

Regards,

Ray Smith
```

###### ↳ ↳ ↳ Re: GUI interface - how?

- **From:** Bob Wolfe <rtwolfe.removethis@flexus.com>
- **Date:** 2004-03-20T15:17:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73oo50dq1fb0vmg5d0ofutc3hdhvgbcmqm@4ax.com>`
- **References:** `<59e39cf4.0403152217.2da786fa@posting.google.com> <Dc-dnZlL3tPZqsrd4p2dnA@giganews.com> <bcfdd616.0403162227.37108487@posting.google.com>`

```
g.friedrich@fiuka.de (Friedrich) wrote:

>"JerryMouse" <nospam@bisusa.com> wrote in message news:<Dc-dnZlL3tPZqsrd4p2dnA@giganews.com>...
>
…[6 more quoted lines elided]…
>Or: AcuCobol thin client

I suspect that PERCobol supports the Linux GUI, but does AcuCOBOL's
thin client support it?




Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

##### ↳ ↳ Re: GUI interface - how?

- **From:** Bob Wolfe <rtwolfe.removethis@flexus.com>
- **Date:** 2004-03-20T15:16:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jsno50t36cbleboci81duittbupfu0tqav@4ax.com>`
- **References:** `<59e39cf4.0403152217.2da786fa@posting.google.com> <Dc-dnZlL3tPZqsrd4p2dnA@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote:

>irado furioso com tudo wrote:
>> goodday, friends
…[18 more quoted lines elided]…
>

Jerry:

He wants a Gnome/KDE interface (Linux GUI).  He can use sp2 to create
the GUI screens, but to display in KDE/Gnome, he should use our Web
Client software in order to display the screens in a Linux GUI web
browser.

Fujitsu has Linux support, but not for KDE/Gnome screen handling.  As
far as I know, KOBOL supports a native KDE/Gnome style GUI interface.

Hope this is helpful.




Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: GUI interface - how?

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-03-16T10:25:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0403161025.68da1c41@posting.google.com>`
- **References:** `<59e39cf4.0403152217.2da786fa@posting.google.com>`

```
irado@hotpop.com (irado furioso com tudo) wrote

> I am new to cobol for *nixï¿½es, and I am stuck with the subject.. how
> to build a GUI interface inorder to interact with the final user?
…[3 more quoted lines elided]…
> Ah, it can be either console (ascii) or Gnome/KDE interface.

There is a Unix/Linux console version of SP/2 from Flexus.

An advantage of a console 'GUI' is that it can be easily accessed
using telnet or ssh from anywhere using just an xterm or, say, putty.
```

#### ↳ Re: GUI interface - how?

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-03-16T15:27:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0403161527.2717855@posting.google.com>`
- **References:** `<59e39cf4.0403152217.2da786fa@posting.google.com>`

```
irado@hotpop.com (irado furioso com tudo) wrote

> I am new to cobol for *nixï¿½es, and I am stuck with the subject.. how
> to build a GUI interface inorder to interact with the final user?
…[3 more quoted lines elided]…
> Ah, it can be either console (ascii) or Gnome/KDE interface.

You can check out TCGUI for TinyCobol which is a TCL GUI designer that
generates the Cobol in Copybooks and TCL for the GUI.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
