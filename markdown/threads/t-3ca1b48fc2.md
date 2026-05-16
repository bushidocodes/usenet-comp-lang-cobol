[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Hand Held Windows PC and COBOL

_8 messages · 5 participants · 2004-01_

---

### Hand Held Windows PC and COBOL

- **From:** "Stephen Plotnick" <thepla@attglobal.net>
- **Date:** 2004-01-04T11:45:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ff8512e$0$61325$a8266bb1@news.titannews.com>`

```
Has anybody been able to develop code for a hand held PC using Windows CE? I
use Realia Cobol and GuiScreenio for my development.





................................................................
       Posted via TITANnews - Uncensored Newsgroups Access
             >>>> at http://www.TitanNews.com <<<<
-=Every Newsgroup - Anonymous, UNCENSORED, BROADBAND Downloads=-
```

#### ↳ Re: Hand Held Windows PC and COBOL

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-01-04T14:50:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0401041450.47ae9eb8@posting.google.com>`
- **References:** `<3ff8512e$0$61325$a8266bb1@news.titannews.com>`

```
"Stephen Plotnick" <thepla@attglobal.net> wrote 

> Has anybody been able to develop code for a hand held PC using Windows CE? I
> use Realia Cobol and GuiScreenio for my development.

As I understand it, Realia compiles to Intel 80x86 code for MS
Windows.

Hand held devices are not Intel CPUs, they are Dragon or StrongARM or
XScale.  Windows CE is not 'Windows', but is somewhat the same but
also somewhat different.

When some one writes a compiler and/or runtime that will run on an
XScale CPU with CE then you may get to write Cobol for those machines.
```

#### ↳ Re: Hand Held Windows PC and COBOL

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2004-01-05T13:48:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1jqivvg82tnt59a2o0ce176e828e4qr5io@4ax.com>`
- **References:** `<3ff8512e$0$61325$a8266bb1@news.titannews.com>`

```
"Stephen Plotnick" <thepla@attglobal.net> wrote:

>Has anybody been able to develop code for a hand held PC using Windows CE? I
>use Realia Cobol and GuiScreenio for my development.

The Flexus Web Client can be used to develop a user interface for an
handheld PC using Windows CE.  Many of our customers have already done
this.

Most handhelds don't have the resources to develop a full Win32
interface.  But as far as I know, they all offer a web browser.

In addition, you can develop a standard HTML/Javascript interface with
Web Client, or you can develop a very sophisticated Flash interface
using the Macromedia Flash support with our Web Client product.  I'll
be happy to assist with further details through priovate e-mail.



Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: Hand Held Windows PC and COBOL

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2004-01-05T08:37:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0401050837.264d58eb@posting.google.com>`
- **References:** `<3ff8512e$0$61325$a8266bb1@news.titannews.com>`

```
Stephen,

I'm speaking as a representative of Flexus right now.

There are not COBOL compilers targeting CE/Pocket PC at this point. 
Even the .NET compilers offered by Fujitsu and Micro Focus cannot
presently target this environment.

Flexus - http://www.flexus.com, offers a "Web client" product that you
can use with these devices, however.  This allows your COBOL to run on
a server - ie, Unix, Windows, VMS, Linux and your user interface to be
displayed on an TCP/IP attached device using a browser.  Recently,
Flexus completed development on a Flash interface as well - allowing
you to create a consistent user interface using MacroMedia flash - but
still use your normal traditionally COBOL program on the server.

The only caveat to this is that you need TCP/IP connectivity for the
handheld.



"Stephen Plotnick" <thepla@attglobal.net> wrote in message news:<3ff8512e$0$61325$a8266bb1@news.titannews.com>...
> Has anybody been able to develop code for a hand held PC using Windows CE? I
> use Realia Cobol and GuiScreenio for my development.
…[8 more quoted lines elided]…
> -=Every Newsgroup - Anonymous, UNCENSORED, BROADBAND Downloads=-
```

#### ↳ Re: Hand Held Windows PC and COBOL

- **From:** maross@texoma.net (Mike)
- **Date:** 2004-01-10T09:21:53-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2763b81a.0401100921.1762b2a5@posting.google.com>`
- **References:** `<3ff8512e$0$61325$a8266bb1@news.titannews.com>`

```
"Stephen Plotnick"  wrote
> Has anybody been able to develop code for a hand held PC using Windows CE? I
> use Realia Cobol and GuiScreenio for my development.

Hi Stephen,
     If you use FlashMX's standalone PPC player you can compile an 
*.exe PPC program, that will run full screen (240*320) as a standalone
program, verses (230*250) with a HTML wrapper. This will work on Mac's
also, but you will need an Html wrapper for Linux or Sony's CLIE
pocket devices.  If your PPC program is to run standalone (not always
connected), you will need to use FlashMX's flat sequential files
called "Shared Objects" or Flash5 cookies (CLIE), these can be read by
Fujitsu 6.1, PHP and I will guest any other Language or COBOL
compilers that reads flat files. This method also works if you wish to
use PPC to Desktop (versus PPC to Server).  Go to
http://www.macromedia.com/devnet/mobile/articles/sometimes_connected.html
and numerous other mobile articles there.   The great thing about
using FlashMX for your GUI, is that you can compile it to a PC/Mac
desktop as a "Projector file" or with a C++ wrapper from various third
party dealers i.e. http://www.Northcode.com or to Linux if you are a
WINE genius or just HTML. Using a FlashMX GUI that senses devices and
screen-size, you can minimize work areas to small buttons, thus
allowing the same GUI and sub_program_calling code in one *.fla
project file (same as FSC's *.prj) across multiple sized devices and
OSs. A FlashMX compiled program can call other compiled programs,
including COBOL, providing they are in a special named directory
called FSCOMMAND. This is used extensity by programmers for desktop
and CD/DVD programming, even Macromedia's FlashMX Studio's CD
installer uses this method.
  Hope this info helps Stephen. 

MY QUESTION: Is anyone Successfully using a non_COBOL_GUI to COBOL
compiler for backend desktop and/or server for CGI across various
OS's? I have Fujitsu 6.1, however while I can call FSC desktop from
FlashMX, it seems that FSC in dropping their "Standard version" that
works well for confusing Multiple GUI methods that require extensive
GUI multiple rewrites across OS's and at least two major versions for
Windows (NET and screen-io). As a bonus you must pay FSC $1800.00 for
the standard Linux compiler versus a $500.00 or less for C++/JAVA
compiler or free PHP for client to server and the latter have
extensive examples and developer communities.  PowerCOBOL screens are
like going back to 1920's silent black and white movies verses Flash's
GUI and other COBOL GUIs are jokes. I have tried KOBOL, however there
are few examples and null developer community, and unfortunately not
well proven. Unless there is something new soon, my few COBOL programs
may need just to be rewritten, which I've been dreading in my not too
much spare time. Any input appreciated.
              Thanks. Mike
```

##### ↳ ↳ Re: Hand Held Windows PC and COBOL

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2004-01-12T19:59:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0401121959.26718c5c@posting.google.com>`
- **References:** `<3ff8512e$0$61325$a8266bb1@news.titannews.com> <2763b81a.0401100921.1762b2a5@posting.google.com>`

```
maross@texoma.net (Mike) wrote in message news:<2763b81a.0401100921.1762b2a5@posting.google.com>...
> "Stephen Plotnick"  wrote
> 
> MY QUESTION: Is anyone Successfully using a non_COBOL_GUI to COBOL
> compiler for backend desktop and/or server for CGI across various
> OS's? 

Flexus products allow this, and there are numerous people doing this
using the Flexus suite of tools - all compiler and OS independent.
```

###### ↳ ↳ ↳ Re: Hand Held Windows PC and COBOL

- **From:** maross@texoma.net (Mike)
- **Date:** 2004-01-14T08:14:25-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2763b81a.0401140814.7d6074e5@posting.google.com>`
- **References:** `<3ff8512e$0$61325$a8266bb1@news.titannews.com> <2763b81a.0401100921.1762b2a5@posting.google.com> <bfdfc3e8.0401121959.26718c5c@posting.google.com>`

```
thaneh@softwaresimple.com (Thane Hubbell) wrote in message 
> Flexus products allow this, and there are numerous people doing this
> using the Flexus suite of tools - all compiler and OS independent.

Thanks for the reply Thane.
   However Flexus appears for to be for the desktop/thin-client to mid
to large servers; where I deal with a FlashMX PPC/desktop client to
desktop and/or small web server.  I am using flash for these now, as
noted in my previous post, as FlashMX's web client GUI can be compiled
to desktop/PPC native application or compiled for E_books etc, however
FlashMX can only use flat local files or RDBMS via remote calls and
lacks the ability to work with the desktops system resources, thus the
need of a language like COBOL, C++ or third party C++ extensions at
the backend. Flash Communication server AScript language works with
amazing features that PHP just will not ever have on its own(and many
it should have). Just looking for brainstorming schema solutions of
reworking older COBOL without complete rewrites. Thanks. Mike
```

###### ↳ ↳ ↳ Re: Hand Held Windows PC and COBOL

_(reply depth: 4)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2004-01-14T21:15:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0401142115.51d27b3a@posting.google.com>`
- **References:** `<3ff8512e$0$61325$a8266bb1@news.titannews.com> <2763b81a.0401100921.1762b2a5@posting.google.com> <bfdfc3e8.0401121959.26718c5c@posting.google.com> <2763b81a.0401140814.7d6074e5@posting.google.com>`

```
Hmm... have you looked at the XML sockets features of Flash MX 2004? 
I think it would be fairly easy to communicate with a local
application via IP and these sockets.

maross@texoma.net (Mike) wrote in message news:<2763b81a.0401140814.7d6074e5@posting.google.com>...
> thaneh@softwaresimple.com (Thane Hubbell) wrote in message 
> > Flexus products allow this, and there are numerous people doing this
…[14 more quoted lines elided]…
> reworking older COBOL without complete rewrites. Thanks. Mike
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
