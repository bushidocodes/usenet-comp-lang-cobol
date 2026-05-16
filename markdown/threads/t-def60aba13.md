[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Acucobol & Registry

_18 messages · 6 participants · 2007-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Acucobol & Registry

- **From:** Gio <giovanni_dimaio@virgilio.it>
- **Date:** 2007-06-09T13:13:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1181420010.439987.237760@q66g2000hsg.googlegroups.com>`

```
Hi, I'm new of ACUCOBOL.
I'm using an old 4.3 version and I wish to access the windows
registry.
I just want to create a key to check it again whenever I run my
program.
Can anyone help me ?
Many thanks

Giovanni

Giovanni_dimaio@virgilio.it
```

#### ↳ Re: Acucobol & Registry

- **From:** Kellie Fitton <KELLIEFITTON@YAHOO.COM>
- **Date:** 2007-06-09T14:36:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1181424971.623277.6780@m36g2000hse.googlegroups.com>`
- **In-Reply-To:** `<1181420010.439987.237760@q66g2000hsg.googlegroups.com>`
- **References:** `<1181420010.439987.237760@q66g2000hsg.googlegroups.com>`

```
On Jun 9, 1:13 pm, Gio <giovanni_dim...@virgilio.it> wrote:
> Hi, I'm new of ACUCOBOL.
> I'm using an old 4.3 version and I wish to access the windows
…[8 more quoted lines elided]…
> Giovanni_dim...@virgilio.it


Hi,

You can use the following APIs to create a registry keys:

	RegCreateKeyEx()  using KEY_ALL_ACCESS
	RegSetValueEx()
	RegCloseKey()
	RegOpenKeyEx()    using KEY_ALL_ACCESS
	RegQueryValueEx()
	RegCloseKey()

http://msdn2.microsoft.com/en-us/library/ms724844.aspx

http://msdn2.microsoft.com/en-us/library/ms724923.aspx

http://msdn2.microsoft.com/en-us/library/ms724837.aspx

http://msdn2.microsoft.com/en-us/library/ms724897.aspx

http://msdn2.microsoft.com/en-us/library/ms724911.aspx

Kellie.
```

##### ↳ ↳ Re: Acucobol & Registry

- **From:** Gio <giovanni_dimaio@virgilio.it>
- **Date:** 2007-06-10T04:23:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1181474604.089358.207120@c77g2000hse.googlegroups.com>`
- **In-Reply-To:** `<1181424971.623277.6780@m36g2000hse.googlegroups.com>`
- **References:** `<1181420010.439987.237760@q66g2000hsg.googlegroups.com> <1181424971.623277.6780@m36g2000hse.googlegroups.com>`

```
On 9 Giu, 23:36, Kellie Fitton <KELLIEFIT...@YAHOO.COM> wrote:
> On Jun 9, 1:13 pm, Gio <giovanni_dim...@virgilio.it> wrote:
>
…[33 more quoted lines elided]…
> Kellie.

Many thanks Kellie,
unfortunately I don't know how to to it in Cobol.
A small sample would be great.
Thanks.

Giovanni
```

###### ↳ ↳ ↳ Re: Acucobol & Registry

- **From:** Kellie Fitton <KELLIEFITTON@YAHOO.COM>
- **Date:** 2007-06-10T12:57:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1181505479.905197.308420@m36g2000hse.googlegroups.com>`
- **In-Reply-To:** `<1181474604.089358.207120@c77g2000hse.googlegroups.com>`
- **References:** `<1181420010.439987.237760@q66g2000hsg.googlegroups.com> <1181424971.623277.6780@m36g2000hse.googlegroups.com> <1181474604.089358.207120@c77g2000hse.googlegroups.com>`

```
On Jun 10, 4:23 am, Gio <giovanni_dim...@virgilio.it> wrote:
> On 9 Giu, 23:36, Kellie Fitton <KELLIEFIT...@YAHOO.COM> wrote:
>
…[48 more quoted lines elided]…
> - Show quoted text -


Hi,

You can download the sample program CobReg.zip from microfocus.com:

http://supportline.microfocus.com/examplesandutilities/nesamp.asp#Win32API


You can download the sample programs in chapter 19 from kimsoft.com:

http://www.kimsoft.com/api-COBOL/api-COBOL.htm

Kellie.
```

###### ↳ ↳ ↳ Re: Acucobol & Registry

_(reply depth: 4)_

- **From:** Gio <giovanni_dimaio@virgilio.it>
- **Date:** 2007-06-10T16:09:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1181516973.808407.240660@p77g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<1181505479.905197.308420@m36g2000hse.googlegroups.com>`
- **References:** `<1181420010.439987.237760@q66g2000hsg.googlegroups.com> <1181424971.623277.6780@m36g2000hse.googlegroups.com> <1181474604.089358.207120@c77g2000hse.googlegroups.com> <1181505479.905197.308420@m36g2000hse.googlegroups.com>`

```
On 10 Giu, 21:57, Kellie Fitton <KELLIEFIT...@YAHOO.COM> wrote:
> On Jun 10, 4:23 am, Gio <giovanni_dim...@virgilio.it> wrote:
>
…[64 more quoted lines elided]…
> - Mostra testo tra virgolette -

Grazie Kellie.
I never used the MicroFocus but I'll try to convert the routines to
ACUCOBOL calling the ADVAPI32.DLL.
Hope this will help solving my problem.
Very kind

Giovanni
```

###### ↳ ↳ ↳ Re: Acucobol & Registry

_(reply depth: 5)_

- **From:** Gio <giovanni_dimaio@virgilio.it>
- **Date:** 2007-06-11T15:19:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1181600376.862245.86620@h2g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<1181516973.808407.240660@p77g2000hsh.googlegroups.com>`
- **References:** `<1181420010.439987.237760@q66g2000hsg.googlegroups.com> <1181424971.623277.6780@m36g2000hse.googlegroups.com> <1181474604.089358.207120@c77g2000hse.googlegroups.com> <1181505479.905197.308420@m36g2000hse.googlegroups.com> <1181516973.808407.240660@p77g2000hsh.googlegroups.com>`

```
On 11 Giu, 01:09, Gio <giovanni_dim...@virgilio.it> wrote:
> On 10 Giu, 21:57, Kellie Fitton <KELLIEFIT...@YAHOO.COM> wrote:
>
…[76 more quoted lines elided]…
> - Mostra testo tra virgolette -

Yes!
It works fine.
Thanks again Kellie.

Giovanni
```

###### ↳ ↳ ↳ Re: Acucobol & Registry

_(reply depth: 6)_

- **From:** Kellie Fitton <KELLIEFITTON@YAHOO.COM>
- **Date:** 2007-06-11T15:34:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1181601290.790797.159370@c77g2000hse.googlegroups.com>`
- **In-Reply-To:** `<1181600376.862245.86620@h2g2000hsg.googlegroups.com>`
- **References:** `<1181420010.439987.237760@q66g2000hsg.googlegroups.com> <1181424971.623277.6780@m36g2000hse.googlegroups.com> <1181474604.089358.207120@c77g2000hse.googlegroups.com> <1181505479.905197.308420@m36g2000hse.googlegroups.com> <1181516973.808407.240660@p77g2000hsh.googlegroups.com> <1181600376.862245.86620@h2g2000hsg.googlegroups.com>`

```
On Jun 11, 3:19 pm, Gio <giovanni_dim...@virgilio.it> wrote:
> On 11 Giu, 01:09, Gio <giovanni_dim...@virgilio.it> wrote:
>
…[86 more quoted lines elided]…
> - Show quoted text -


Siete Benvenuti.

Kellie.
```

###### ↳ ↳ ↳ Re: Acucobol & Registry

_(reply depth: 7)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-06-12T02:29:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Wxnbi.16029$1i1.15108@pd7urf3no>`
- **In-Reply-To:** `<1181601290.790797.159370@c77g2000hse.googlegroups.com>`
- **References:** `<1181420010.439987.237760@q66g2000hsg.googlegroups.com> <1181424971.623277.6780@m36g2000hse.googlegroups.com> <1181474604.089358.207120@c77g2000hse.googlegroups.com> <1181505479.905197.308420@m36g2000hse.googlegroups.com> <1181516973.808407.240660@p77g2000hsh.googlegroups.com> <1181600376.862245.86620@h2g2000hsg.googlegroups.com> <1181601290.790797.159370@c77g2000hse.googlegroups.com>`

```
Kellie Fitton wrote:

> 
> Siete Benvenuti.
> 
> Kellie.
> 

Good on you young lady. Nice to see you are still around. Have you 
finished training Kellie, or still got some to go.

Jimmy
```

###### ↳ ↳ ↳ Re: Acucobol & Registry

_(reply depth: 8)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-06-12T07:20:27-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5zwbi.3165$c06.2103@newssvr22.news.prodigy.net>`
- **References:** `<1181420010.439987.237760@q66g2000hsg.googlegroups.com> <1181424971.623277.6780@m36g2000hse.googlegroups.com> <1181474604.089358.207120@c77g2000hse.googlegroups.com> <1181505479.905197.308420@m36g2000hse.googlegroups.com> <1181516973.808407.240660@p77g2000hsh.googlegroups.com> <1181600376.862245.86620@h2g2000hsg.googlegroups.com> <1181601290.790797.159370@c77g2000hse.googlegroups.com> <Wxnbi.16029$1i1.15108@pd7urf3no>`

```
"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:Wxnbi.16029$1i1.15108@pd7urf3no...

> Good on you young lady. Nice to see you are still around. Have you 
> finished training Kellie, or still got some to go.

I suggest, sir, none of us EVER finish training.

MCM
```

###### ↳ ↳ ↳ Re: Acucobol & Registry

_(reply depth: 8)_

- **From:** Kellie Fitton <KELLIEFITTON@YAHOO.COM>
- **Date:** 2007-06-12T09:36:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1181666167.987881.132270@a26g2000pre.googlegroups.com>`
- **In-Reply-To:** `<Wxnbi.16029$1i1.15108@pd7urf3no>`
- **References:** `<1181420010.439987.237760@q66g2000hsg.googlegroups.com> <1181424971.623277.6780@m36g2000hse.googlegroups.com> <1181474604.089358.207120@c77g2000hse.googlegroups.com> <1181505479.905197.308420@m36g2000hse.googlegroups.com> <1181516973.808407.240660@p77g2000hsh.googlegroups.com> <1181600376.862245.86620@h2g2000hsg.googlegroups.com> <1181601290.790797.159370@c77g2000hse.googlegroups.com> <Wxnbi.16029$1i1.15108@pd7urf3no>`

```
On Jun 11, 7:29 pm, "James J. Gavan" <jgavandeletet...@shaw.ca> wrote:
> Kellie Fitton wrote:
>
…[7 more quoted lines elided]…
> Jimmy


Hi Jimmy,

Hope everything is well....

I will be learning SQL language after summer break --- hopefully I get
hired by Oracle Corporation. :-)

By the way, the latest version of microfocus NetExpress 5.0 does not
have any reference or vaunting about OO capabilities, I wonder why.

http://www.microfocus.com/products/NetExpress/

Kellie. :-)
```

###### ↳ ↳ ↳ Re: Acucobol & Registry

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-06-12T20:53:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mJDbi.117217$dg3.106126@fe10.news.easynews.com>`
- **References:** `<1181420010.439987.237760@q66g2000hsg.googlegroups.com> <1181424971.623277.6780@m36g2000hse.googlegroups.com> <1181474604.089358.207120@c77g2000hse.googlegroups.com> <1181505479.905197.308420@m36g2000hse.googlegroups.com> <1181516973.808407.240660@p77g2000hsh.googlegroups.com> <1181600376.862245.86620@h2g2000hsg.googlegroups.com> <1181601290.790797.159370@c77g2000hse.googlegroups.com> <Wxnbi.16029$1i1.15108@pd7urf3no> <1181666167.987881.132270@a26g2000pre.googlegroups.com>`

```
Kellie,
   Where are you looking?

When I go to:
   http://supportline.microfocus.com/documentation/books/nx50/nx50indx.htm

There is an entire section of books under
   "Object Oriented Programming"

as well as separate books on "COBOL and Java" and "COM, COBOL, and .NET"

Now there ARE certain restrictions on the "personal edition" - but even that 
supports OO.
```

###### ↳ ↳ ↳ Re: Acucobol & Registry

_(reply depth: 10)_

- **From:** Kellie Fitton <KELLIEFITTON@YAHOO.COM>
- **Date:** 2007-06-12T14:15:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1181682939.931971.57020@d30g2000prg.googlegroups.com>`
- **In-Reply-To:** `<mJDbi.117217$dg3.106126@fe10.news.easynews.com>`
- **References:** `<1181420010.439987.237760@q66g2000hsg.googlegroups.com> <1181424971.623277.6780@m36g2000hse.googlegroups.com> <1181474604.089358.207120@c77g2000hse.googlegroups.com> <1181505479.905197.308420@m36g2000hse.googlegroups.com> <1181516973.808407.240660@p77g2000hsh.googlegroups.com> <1181600376.862245.86620@h2g2000hsg.googlegroups.com> <1181601290.790797.159370@c77g2000hse.googlegroups.com> <Wxnbi.16029$1i1.15108@pd7urf3no> <1181666167.987881.132270@a26g2000pre.googlegroups.com> <mJDbi.117217$dg3.106126@fe10.news.easynews.com>`

```
On Jun 12, 1:53 pm, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> Kellie,
>    Where are you looking?
…[46 more quoted lines elided]…
> - Show quoted text -


Hi Bill,

We are talking about the actual COBOL compiler per se, not the OO
books that microfocus have in the online bookshelf:

http://www.microfocus.com/products/NetExpress/

Kellie.
```

###### ↳ ↳ ↳ Re: Acucobol & Registry

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-06-13T02:45:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VSIbi.120427$NO1.98709@fe05.news.easynews.com>`
- **References:** `<1181420010.439987.237760@q66g2000hsg.googlegroups.com> <1181424971.623277.6780@m36g2000hse.googlegroups.com> <1181474604.089358.207120@c77g2000hse.googlegroups.com> <1181505479.905197.308420@m36g2000hse.googlegroups.com> <1181516973.808407.240660@p77g2000hsh.googlegroups.com> <1181600376.862245.86620@h2g2000hsg.googlegroups.com> <1181601290.790797.159370@c77g2000hse.googlegroups.com> <Wxnbi.16029$1i1.15108@pd7urf3no> <1181666167.987881.132270@a26g2000pre.googlegroups.com> <mJDbi.117217$dg3.106126@fe10.news.easynews.com> <1181682939.931971.57020@d30g2000prg.googlegroups.com>`

```
If you "click" on the "product data sheet" link on the page you pointed to you 
will find (among other things)

 "Full support for object oriented COBOL (including Syntax) and COBOL 
development/debugging"

Besides the documents I pointed to, you will also find full support in the LRM.

I just don't understand what you are trying to say about N/E 5.0.

I will admit they don't highlight this as a "new feature" - but that is because 
it is FAR from "new" for any Micro Focus compiler or product.
```

###### ↳ ↳ ↳ Re: Acucobol & Registry

_(reply depth: 12)_

- **From:** Kellie Fitton <KELLIEFITTON@YAHOO.COM>
- **Date:** 2007-06-13T08:50:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1181749842.528217.295800@a26g2000pre.googlegroups.com>`
- **In-Reply-To:** `<VSIbi.120427$NO1.98709@fe05.news.easynews.com>`
- **References:** `<1181420010.439987.237760@q66g2000hsg.googlegroups.com> <1181424971.623277.6780@m36g2000hse.googlegroups.com> <1181474604.089358.207120@c77g2000hse.googlegroups.com> <1181505479.905197.308420@m36g2000hse.googlegroups.com> <1181516973.808407.240660@p77g2000hsh.googlegroups.com> <1181600376.862245.86620@h2g2000hsg.googlegroups.com> <1181601290.790797.159370@c77g2000hse.googlegroups.com> <Wxnbi.16029$1i1.15108@pd7urf3no> <1181666167.987881.132270@a26g2000pre.googlegroups.com> <mJDbi.117217$dg3.106126@fe10.news.easynews.com> <1181682939.931971.57020@d30g2000prg.googlegroups.com> <VSIbi.120427$NO1.98709@fe05.news.easynews.com>`

```
On Jun 12, 7:45 pm, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> If you "click" on the "product data sheet" link on the page you pointed to you
> will find (among other things)
…[79 more quoted lines elided]…
> - Show quoted text -


Hi Bill,

I know that Jimmy have a NetExpress compiler and uses OO programming
classes in his code, I thought it was odd microfocus did not mention
any
reference of OO support under the heading Highlights and Benefits,
that's
why I want it to bring it to his attention.  I did not know they only
mentioned the OO support in the product datasheet.

Kellie. :-)
```

###### ↳ ↳ ↳ Re: Acucobol & Registry

_(reply depth: 9)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-06-22T02:54:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lRGei.51103$1i1.27561@pd7urf3no>`
- **In-Reply-To:** `<1181666167.987881.132270@a26g2000pre.googlegroups.com>`
- **References:** `<1181420010.439987.237760@q66g2000hsg.googlegroups.com> <1181424971.623277.6780@m36g2000hse.googlegroups.com> <1181474604.089358.207120@c77g2000hse.googlegroups.com> <1181505479.905197.308420@m36g2000hse.googlegroups.com> <1181516973.808407.240660@p77g2000hsh.googlegroups.com> <1181600376.862245.86620@h2g2000hsg.googlegroups.com> <1181601290.790797.159370@c77g2000hse.googlegroups.com> <Wxnbi.16029$1i1.15108@pd7urf3no> <1181666167.987881.132270@a26g2000pre.googlegroups.com>`

```
Kellie Fitton wrote:
> On Jun 11, 7:29 pm, "James J. Gavan" <jgavandeletet...@shaw.ca> wrote:
> 
…[28 more quoted lines elided]…
> 
Quite simply they've gone with what pays the bills.

Historically back in DOS days they had several methods of 'windowing', 
Panels etc. which became Dialog System and back then using your beloved 
APIs they duplicated what Charles Petzold (PC Magazine) did using C.

VISOC and Net Express were geared to enticing users to go full blown OO. 
You could do all the above, except DS which was left out. Although many 
snapped up a free beta version few went with the real McCoy (don't know 
numbers). It was only when Dialog System was re-introduced that the 
product truly took off - apart from Procedural folk, my guess 80% plus 
use Dialog System for Windowing.

That's fine and dandy, but now comes the need to interface with webbing. 
  Without having to do too much re-inventing of the wheel, both F/J and 
M/F went dotNet - saves them a lot of money - you will have seen Pete 
enthuse about the Visual Studio object presentation making it easy to 
access a particular method for a particular object.

The reality for 'the now' and the future is that the whole game is about 
objects (has been since Simula approx 1947 !). While you can still code 
in OO COBOL and interface with other languages, money wise dotNet makes 
sense rather than emphasizing OO COBOL as an independent isolated tool.

I hope as part of your SQL endeavour you take a good look at the ESQL 
Assistant - it's a real dream to use as a tool and covers you on 
numerous SQL engines. Good luck.

PS: The On-line manual for OO in Version 5 is very good.

Jimmy
```

###### ↳ ↳ ↳ Re: Acucobol & Registry

_(reply depth: 10)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-06-21T23:12:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<137mfiucgs1tk25@corp.supernews.com>`
- **References:** `<1181420010.439987.237760@q66g2000hsg.googlegroups.com> <1181424971.623277.6780@m36g2000hse.googlegroups.com> <1181474604.089358.207120@c77g2000hse.googlegroups.com> <1181505479.905197.308420@m36g2000hse.googlegroups.com> <1181516973.808407.240660@p77g2000hsh.googlegroups.com> <1181600376.862245.86620@h2g2000hsg.googlegroups.com> <1181601290.790797.159370@c77g2000hse.googlegroups.com> <Wxnbi.16029$1i1.15108@pd7urf3no> <1181666167.987881.132270@a26g2000pre.googlegroups.com> <lRGei.51103$1i1.27561@pd7urf3no>`

```

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message
news:lRGei.51103$1i1.27561@pd7urf3no...
[snip]
> The reality for 'the now' and the future is that the whole game is about
> objects (has been since Simula approx 1947 !).

Actually 1967.

"SIMULA 67 - A general-purpose successor to SIMULA I,
in which the simulation support is defined in object-oriented
terms.  Introduced the record class, leading the way to data
abstraction and object-oriented programming.  Garbage
collection."

Source:
-----
The Language List - Version 2.4, January 23, 1995

Collected information on about 2350 computer languages, past and present.

Available online as:
 http://cui_www.unige.ch/langlist
 ftp://wuarchive.wustl.edu/doc/misc/lang-list.txt
-----
```

###### ↳ ↳ ↳ Re: Acucobol & Registry

_(reply depth: 11)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-06-22T04:21:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<P6Iei.50538$NV3.8153@pd7urf2no>`
- **In-Reply-To:** `<137mfiucgs1tk25@corp.supernews.com>`
- **References:** `<1181420010.439987.237760@q66g2000hsg.googlegroups.com> <1181424971.623277.6780@m36g2000hse.googlegroups.com> <1181474604.089358.207120@c77g2000hse.googlegroups.com> <1181505479.905197.308420@m36g2000hse.googlegroups.com> <1181516973.808407.240660@p77g2000hsh.googlegroups.com> <1181600376.862245.86620@h2g2000hsg.googlegroups.com> <1181601290.790797.159370@c77g2000hse.googlegroups.com> <Wxnbi.16029$1i1.15108@pd7urf3no> <1181666167.987881.132270@a26g2000pre.googlegroups.com> <lRGei.51103$1i1.27561@pd7urf3no> <137mfiucgs1tk25@corp.supernews.com>`

```
Rick Smith wrote:
> "James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message
> news:lRGei.51103$1i1.27561@pd7urf3no...
…[26 more quoted lines elided]…
> 
Rick,

Thanks for the correction - didn't sound right when I wrote it. Still 
what's twenty years between friends - doesn't seem to have bothered J4 :-)

Jimmy
```

###### ↳ ↳ ↳ Re: Acucobol & Registry

_(reply depth: 12)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-06-22T08:42:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<137ngvshko0p0e1@corp.supernews.com>`
- **References:** `<1181420010.439987.237760@q66g2000hsg.googlegroups.com> <1181424971.623277.6780@m36g2000hse.googlegroups.com> <1181474604.089358.207120@c77g2000hse.googlegroups.com> <1181505479.905197.308420@m36g2000hse.googlegroups.com> <1181516973.808407.240660@p77g2000hsh.googlegroups.com> <1181600376.862245.86620@h2g2000hsg.googlegroups.com> <1181601290.790797.159370@c77g2000hse.googlegroups.com> <Wxnbi.16029$1i1.15108@pd7urf3no> <1181666167.987881.132270@a26g2000pre.googlegroups.com> <lRGei.51103$1i1.27561@pd7urf3no> <137mfiucgs1tk25@corp.supernews.com> <P6Iei.50538$NV3.8153@pd7urf2no>`

```

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message
news:P6Iei.50538$NV3.8153@pd7urf2no...
[snip]
>  Still
> what's twenty years between friends - doesn't seem to have bothered J4 :-)

Perhaps an adjective such as long-time or childhood. <g>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
