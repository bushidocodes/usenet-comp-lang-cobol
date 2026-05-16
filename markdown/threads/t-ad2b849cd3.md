[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# visual cobol

_10 messages · 5 participants · 2001-10_

---

### visual cobol

- **From:** "Jason" <jasonsdog@att.net>
- **Date:** 2001-10-25T03:54:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<52MB7.139903$3d2.4449916@bgtnsc06-news.ops.worldnet.att.net>`

```
Users,

I use an application made using Visual Cobol 3.6 and cannot seem to get it
to run full screen in Windows 2000

Tried hitting Alt-space and that enlarges the window to full screen but only
half is occupied, the rest is black.

Anyone have any ideas on how to get a true full screen ?
```

#### ↳ Re: visual cobol

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-10-24T23:45:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9r85ck$4o$1@slb1.atl.mindspring.net>`
- **References:** `<52MB7.139903$3d2.4449916@bgtnsc06-news.ops.worldnet.att.net>`

```
Just for clarity sake, do you really mean "Visual COBOL" - the product from
mbp?

Other compilers that you MIGHT mean are "VisualAge COBOL" (from IBM) or
Visual Object COBOL from Micro Focus.

You may well mean exactly what you say - but I did want to "check it out"
first.  As I recall (and I may not be correct on this) the mbp product was
"functionally frozen" before Windows 2000 - so it is possible that it
doesn't work there.
```

##### ↳ ↳ Re: visual cobol

- **From:** "Jason" <jasonsdog@att.net>
- **Date:** 2001-10-25T05:09:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q8NB7.155225$W8.4268383@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<52MB7.139903$3d2.4449916@bgtnsc06-news.ops.worldnet.att.net> <9r85ck$4o$1@slb1.atl.mindspring.net>`

```
it is indeed Mbp cobol
```

###### ↳ ↳ ↳ Re: visual cobol

- **From:** Harald.Cordes@microfocus.com (Harald Cordes)
- **Date:** 2001-10-25T07:28:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1fabdc0d.0110250628.4e9ded57@posting.google.com>`
- **References:** `<52MB7.139903$3d2.4449916@bgtnsc06-news.ops.worldnet.att.net> <9r85ck$4o$1@slb1.atl.mindspring.net> <q8NB7.155225$W8.4268383@bgtnsc04-news.ops.worldnet.att.net>`

```
"Jason" <jasonsdog@att.net> wrote in message news:<q8NB7.155225$W8.4268383@bgtnsc04-news.ops.worldnet.att.net>...
> it is indeed Mbp cobol

is it 16 bit, with or without a DOS-Extender and which DOS-Extender?
or is it 32 bit?

which minor version? 3.6.03, 3.6.06, or 3.6.08?
```

###### ↳ ↳ ↳ Re: visual cobol

_(reply depth: 4)_

- **From:** "Jason" <jasonsdog@att.net>
- **Date:** 2001-10-25T15:19:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F3WB7.82772$WW.4376585@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<52MB7.139903$3d2.4449916@bgtnsc06-news.ops.worldnet.att.net> <9r85ck$4o$1@slb1.atl.mindspring.net> <q8NB7.155225$W8.4268383@bgtnsc04-news.ops.worldnet.att.net> <1fabdc0d.0110250628.4e9ded57@posting.google.com>`

```
it is 16 bit
version 3.6.06


Harald Cordes wrote in message
<1fabdc0d.0110250628.4e9ded57@posting.google.com>...
>"Jason" <jasonsdog@att.net> wrote in message
news:<q8NB7.155225$W8.4268383@bgtnsc04-news.ops.worldnet.att.net>...
>> it is indeed Mbp cobol
>
…[3 more quoted lines elided]…
>which minor version? 3.6.03, 3.6.06, or 3.6.08?
```

###### ↳ ↳ ↳ Re: visual cobol

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-10-25T16:49:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ra1f3$icn$1@nntp9.atl.mindspring.net>`
- **References:** `<52MB7.139903$3d2.4449916@bgtnsc06-news.ops.worldnet.att.net> <9r85ck$4o$1@slb1.atl.mindspring.net> <q8NB7.155225$W8.4268383@bgtnsc04-news.ops.worldnet.att.net> <1fabdc0d.0110250628.4e9ded57@posting.google.com> <F3WB7.82772$WW.4376585@bgtnsc05-news.ops.worldnet.att.net>`

```
(To clarify one of my earlier notes)
      You don't tell us what country you are in - so I don't know if you are
in North America or not.  If you are, then the "support" status is
documented at:
 http://www.microfocus.com/products/microfocus/advisory/vcob.asp

Closer to the actual question that you asked, here is the  reply that I
received from one of my "usually reliable sources" concerning Visual COBOL
and Windows 2000.

"In answer to the question of Visual COBOL v3.6 working under Windows 2000,
while the product was never certified under Windows 2000 (nor will it be),
there are a number of customers who are successfully running v3.6 created
applications under Windows 2000 without a problem, provided that they are
using the 32 bit version of the v3.6 release.  There isn't much experience
running the 16 bit product applications under Windows 2000, but it is
expected that there may well be some problems with doing that.

Note, to run the v3.6 compiler, itself, under Windows 2000 there is a
problem.  The product makes use of the Rainbow Technologies security key (or
dongle, as some term the device), which gets connected to the PC's parallel
port and is required to be connected to the PC for the product to function.
The device drivers for this key do not function under Windows 2000.  The
correction is to go to the Rainbow Technologies web site
(http://www.rainbow.com/) and download their later device drivers for
Windows 2000 and install them."
```

###### ↳ ↳ ↳ Re: visual cobol

_(reply depth: 6)_

- **From:** "Jason" <jasonsdog@att.net>
- **Date:** 2001-10-25T23:32:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xh1C7.83645$WW.4410761@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<52MB7.139903$3d2.4449916@bgtnsc06-news.ops.worldnet.att.net> <9r85ck$4o$1@slb1.atl.mindspring.net> <q8NB7.155225$W8.4268383@bgtnsc04-news.ops.worldnet.att.net> <1fabdc0d.0110250628.4e9ded57@posting.google.com> <F3WB7.82772$WW.4376585@bgtnsc05-news.ops.worldnet.att.net> <9ra1f3$icn$1@nntp9.atl.mindspring.net>`

```
I am in California.

Thanks for the tip, I will recompile as 32 bit and see what happens.

It's just that it runs so well in 16 bit that I never even considered what
was right under my nose.

Say, do you work for Microfocus ?
```

###### ↳ ↳ ↳ Re: visual cobol

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-10-25T18:41:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ra7uv$n7b$1@slb1.atl.mindspring.net>`
- **References:** `<52MB7.139903$3d2.4449916@bgtnsc06-news.ops.worldnet.att.net> <9r85ck$4o$1@slb1.atl.mindspring.net> <q8NB7.155225$W8.4268383@bgtnsc04-news.ops.worldnet.att.net> <1fabdc0d.0110250628.4e9ded57@posting.google.com> <F3WB7.82772$WW.4376585@bgtnsc05-news.ops.worldnet.att.net> <9ra1f3$icn$1@nntp9.atl.mindspring.net> <Xh1C7.83645$WW.4410761@bgtnsc05-news.ops.worldnet.att.net>`

```
Once upon a time and long ago, I worked for Micro Focus (before MERANT
before Micro Focus again).  I do have "good contacts" at Micro Focus, IBM,
Fujitsu, and all the ANSI COBOL compiler makers.  Hopefully, I treat them
all equally (good AND bad)
```

#### ↳ Re: visual cobol

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2001-10-25T19:36:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9racd201o0k@enews3.newsguy.com>`
- **References:** `<52MB7.139903$3d2.4449916@bgtnsc06-news.ops.worldnet.att.net>`

```
We're using the latest (and last) version of 32-bit mbp (Visual)
Cobol.  I'll ask the principal designer, but I think we're
seeing the same thing--full screen is more like maximize.

"Jason" <jasonsdog@att.net> wrote in message
news:52MB7.139903$3d2.4449916@bgtnsc06-news.ops.worldnet.att.net
...
> Users,
>
> I use an application made using Visual Cobol 3.6 and cannot
seem to get it
> to run full screen in Windows 2000
>
> Tried hitting Alt-space and that enlarges the window to full
screen but only
> half is occupied, the rest is black.
>
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: visual cobol

- **From:** chris.glazier@microfocus.com (Chris Glazier)
- **Date:** 2001-10-26T06:26:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<260cd566.0110260526.302ef349@posting.google.com>`
- **References:** `<52MB7.139903$3d2.4449916@bgtnsc06-news.ops.worldnet.att.net> <9racd201o0k@enews3.newsguy.com>`

```
There is nothing within the Visual COBOL language itself to help you
with this but under Windows 2000 you should be able to create a
desktop shortcut to the executable file and then modify its Window
Properties.

This allows you to specify Full screen for the Window, number of lines
and columns and also the font. If you use a larger font it will take
up more of the
screen.

When you save these options save them for the shortcut not for the
current window and everytime you click on the shortcut these options
will take effect.


"Grinder" <grinder@no.spam.maam.com> wrote in message news:<9racd201o0k@enews3.newsguy.com>...
> We're using the latest (and last) version of 32-bit mbp (Visual)
> Cobol.  I'll ask the principal designer, but I think we're
…[20 more quoted lines elided]…
> >
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
