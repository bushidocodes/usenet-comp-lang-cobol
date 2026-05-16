[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# does graphics cobol for linux exist???

_14 messages · 8 participants · 2004-08_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### does graphics cobol for linux exist???

- **From:** "max_wappi" <maxbo@wappi.com>
- **Date:** 2004-08-03T13:30:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4sMPc.25949$1V3.634908@twister2.libero.it>`

```
HI, I'm Max.
Is There a cobol for linux with graphics interface??
I have a lot of cobol programs written with microfocus cobol in text mode
and i would like to write new programs under linux, but with combo box,
push-button etc etc.
Thanks in advance ( and sorry for my english....)
```

#### ↳ Re: does graphics cobol for linux exist???

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2004-08-03T14:00:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZTMPc.2898$EE6.734@newssvr24.news.prodigy.com>`
- **References:** `<4sMPc.25949$1V3.634908@twister2.libero.it>`

```
"max_wappi" <maxbo@wappi.com> wrote in message
news:4sMPc.25949$1V3.634908@twister2.libero.it...
> HI, I'm Max.
> Is There a cobol for linux with graphics interface??

http://195.103.161.170/rmi/rmitalia.htm

Look at COBOL-WOW.

Best regards,
Tom Morrison
Liant Software Corporation
```

##### ↳ ↳ Re: does graphics cobol for linux exist???

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-08-03T20:25:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<410ff4ab.239981356@news.optonline.net>`
- **References:** `<4sMPc.25949$1V3.634908@twister2.libero.it> <ZTMPc.2898$EE6.734@newssvr24.news.prodigy.com>`

```
"Tom Morrison" <t.morrison@liant.com> wrote:

>"max_wappi" <maxbo@wappi.com> wrote in message
>news:4sMPc.25949$1V3.634908@twister2.libero.it...
…[5 more quoted lines elided]…
>Look at COBOL-WOW.

"Works with Windows 95, Windows 98, or Windows NT v4.0."
http://www.liant.com/products/cobolwow/
```

###### ↳ ↳ ↳ Re: does graphics cobol for linux exist???

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2004-08-03T20:56:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1_SPc.1006$fH3.405@newssvr22.news.prodigy.com>`
- **References:** `<4sMPc.25949$1V3.634908@twister2.libero.it> <ZTMPc.2898$EE6.734@newssvr24.news.prodigy.com> <410ff4ab.239981356@news.optonline.net>`

```
"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
news:410ff4ab.239981356@news.optonline.net...
> "Tom Morrison" <t.morrison@liant.com> wrote:
>
…[11 more quoted lines elided]…
>

Well, I guess we need to get the web site in line with our software
releases!  :o)

http://www.liant.com/news/releases/20030827_wow4en.php3

(available for a year!)

Notice that only the client must run on Windows (and Windows XP would be one
of those Windows supported).

Liant does *not* have a product targeting a strictly Linux GUI (gnome, kde,
etc.).
```

#### ↳ Re: does graphics cobol for linux exist???

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-03T12:34:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408031134.20b47448@posting.google.com>`
- **References:** `<4sMPc.25949$1V3.634908@twister2.libero.it>`

```
"max_wappi" <maxbo@wappi.com> wrote 

> Is There a cobol for linux with graphics interface??
> I have a lot of cobol programs written with microfocus cobol in text mode
> and i would like to write new programs under linux, but with combo box,
> push-button etc etc.

Flexus SP/2 has combo box, list box push-buttoms, pull down menus,
etc, works with any Cobol system and runs on Windows and Linux.  On
Windows it is GUI, on Linux it is textmode GUI and works identically.

It has the advantage over a graphics in that it can run remotely over
telnet/ssh rather than needing remote X windows while still having the
features of GUI.
```

#### ↳ Re: does graphics cobol for linux exist???

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-08-03T20:25:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<410fdcd9.233882747@news.optonline.net>`
- **References:** `<4sMPc.25949$1V3.634908@twister2.libero.it>`

```
"max_wappi" <maxbo@wappi.com> wrote:

>Is There a cobol for linux with graphics interface??
>I have a lot of cobol programs written with microfocus cobol in text mode
>and i would like to write new programs under linux, but with combo box,
>push-button etc etc.

I don't know of any Cobol that supports KDE, Gnome, P4V or other Linux GUI. 

If you have Micro Focus for Linux, you must have Application Server or
Enterprise Server, both of which come with a CGI tool. You could use that to
talk to a Web browser running on the same box. 

The easiest solution is Flexus sp2, but it doesn't run on unix.
```

##### ↳ ↳ Re: does graphics cobol for linux exist???

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-03T19:38:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408031838.d60502@posting.google.com>`
- **References:** `<4sMPc.25949$1V3.634908@twister2.libero.it> <410fdcd9.233882747@news.optonline.net>`

```
robert.deletethis@wagner.net (Robert Wagner) wrote 

> 
> The easiest solution is Flexus sp2, but it doesn't run on unix.

No. Wrong. More RW misinformation. I have been running it on Unix and
Linux for years.

(and DOS and OS/2)
```

###### ↳ ↳ ↳ Re: does graphics cobol for linux exist???

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-08-04T12:07:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4110c2e9.292787798@news.optonline.net>`
- **References:** `<4sMPc.25949$1V3.634908@twister2.libero.it> <410fdcd9.233882747@news.optonline.net> <217e491a.0408031838.d60502@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert.deletethis@wagner.net (Robert Wagner) wrote 
>
…[5 more quoted lines elided]…
>(and DOS and OS/2)

Look at the subject line. It asks for graphics. Flexus on unix is not graphic.
```

###### ↳ ↳ ↳ Re: does graphics cobol for linux exist???

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-04T12:03:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408041103.7ce711a9@posting.google.com>`
- **References:** `<4sMPc.25949$1V3.634908@twister2.libero.it> <410fdcd9.233882747@news.optonline.net> <217e491a.0408031838.d60502@posting.google.com> <4110c2e9.292787798@news.optonline.net>`

```
robert.deletethis@wagner.net (Robert Wagner) wrote

> >> The easiest solution is Flexus sp2, but it doesn't run on unix.
> 
> Look at the subject line. It asks for graphics. Flexus on unix is not graphic.

First of all, in spite of your claim, SP/2 _does_ run on Unix and
Linux.  What he asked for included combo boxes and push-buttons, which
SP/2 does do on Unix/Linux.

If you comment had been that it wasn't graphic you would have been
correct, but it was that it didn't run and that was misinformation.
```

###### ↳ ↳ ↳ Re: does graphics cobol for linux exist???

_(reply depth: 4)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2004-08-13T17:12:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0gtph09bk7f66ntn7hnhcq1klkd5561r9s@4ax.com>`
- **References:** `<4sMPc.25949$1V3.634908@twister2.libero.it> <410fdcd9.233882747@news.optonline.net> <217e491a.0408031838.d60502@posting.google.com> <4110c2e9.292787798@news.optonline.net>`

```
robert.deletethis@wagner.net (Robert Wagner) wrote:

>riplin@Azonic.co.nz (Richard) wrote:
>
…[9 more quoted lines elided]…
>Look at the subject line. It asks for graphics. Flexus on unix is not graphic. 

Actually, Robert.....when COBOL sp2 is used in conjunction with our
Web Client product, you can indeed run your COBOL program on a UNIX
(or derivative such as Linux) server and display the user interface
screens on KDE or Gnome based web browsers.

It also supports a persistent connection as well.

That allows you to run on Linux using the Linux GUI web browser as a
user interface device.




Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: does graphics cobol for linux exist???

_(reply depth: 5)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-15T00:50:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0hcth0l2b2gidf62rdk3tig3uamot0bcao@4ax.com>`
- **References:** `<4sMPc.25949$1V3.634908@twister2.libero.it> <410fdcd9.233882747@news.optonline.net> <217e491a.0408031838.d60502@posting.google.com> <4110c2e9.292787798@news.optonline.net> <0gtph09bk7f66ntn7hnhcq1klkd5561r9s@4ax.com>`

```
On Fri, 13 Aug 2004 17:12:50 GMT, Bob Wolfe <rtwolfe@flexus.com>
wrote:

>robert.deletethis@wagner.net (Robert Wagner) wrote:

>>Look at the subject line. It asks for graphics. Flexus on unix is not graphic. 
>
…[3 more quoted lines elided]…
>screens on KDE or Gnome based web browsers.

Good answer and product. I knew about Thin Client but was unaware of
Web Client. I recommended CGI spitting HTML into a Unix Web browser.
Web Client looks like a similar but earier to use solution.
```

###### ↳ ↳ ↳ Re: does graphics cobol for linux exist???

_(reply depth: 6)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2004-08-16T14:37:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c9g1i012v8hnpeov32ktaq03d20st9pdi6@4ax.com>`
- **References:** `<4sMPc.25949$1V3.634908@twister2.libero.it> <410fdcd9.233882747@news.optonline.net> <217e491a.0408031838.d60502@posting.google.com> <4110c2e9.292787798@news.optonline.net> <0gtph09bk7f66ntn7hnhcq1klkd5561r9s@4ax.com> <0hcth0l2b2gidf62rdk3tig3uamot0bcao@4ax.com>`

```
Robert Wagner <robert@wagner.net.yourmammaharvests> wrote:

>On Fri, 13 Aug 2004 17:12:50 GMT, Bob Wolfe <rtwolfe@flexus.com>
>wrote:
…[12 more quoted lines elided]…
>Web Client looks like a similar but earier to use solution.

Robert:

Web Client is one of our best kept secrets.  A lot of our Thin Client
customers use Thin Client for in-house user interface access across a
TCP/IP network and Web Client for public access to their application.

The advantage of doing this is that the in-house end users (employees)
get the really high speed Thin Client screen refresh and data
transfer, and the public access end users (customers) can access the
application using their web browser.

We have found that web browser user interface has its strengths, but
also a lot of weaknesses as well.  Thin Client also has many
advantages, but a few disadvantages as well.  Being able to offer a
"dual user interface" allows the COBOL programmer to use the best user
interface environment for the specific end user.




Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

##### ↳ ↳ Re: does graphics cobol for linux exist???

- **From:** g.friedrich@fiuka.de (Friedrich)
- **Date:** 2004-08-03T22:36:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcfdd616.0408032136.63013817@posting.google.com>`
- **References:** `<4sMPc.25949$1V3.634908@twister2.libero.it> <410fdcd9.233882747@news.optonline.net>`

```
robert.deletethis@wagner.net (Robert Wagner) wrote in message news:<410fdcd9.233882747@news.optonline.net>...
> "max_wappi" <maxbo@wappi.com> wrote:
> 
…[5 more quoted lines elided]…
> I don't know of any Cobol that supports KDE, Gnome, P4V or other Linux GUI. 

PERCobol from legacyj supports Linux GUI!

> 
> If you have Micro Focus for Linux, you must have Application Server or
…[3 more quoted lines elided]…
> The easiest solution is Flexus sp2, but it doesn't run on unix.
```

#### ↳ Re: does graphics cobol for linux exist???

- **From:** Vaclav Snajdr <vsn@snajdr.de>
- **Date:** 2004-08-04T06:48:48+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cepp3k$8i3$01$1@news.t-online.com>`
- **References:** `<4sMPc.25949$1V3.634908@twister2.libero.it>`

```
max_wappi wrote:

> HI, I'm Max.
> Is There a cobol for linux with graphics interface??
…[3 more quoted lines elided]…
> Thanks in advance ( and sorry for my english....)

We use since 2 years the combination Tcl/Tk for GUI
and MF-Cobol on server. Tcl/Tk runs on Linux, most Unixes,
Windows and Mac.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
