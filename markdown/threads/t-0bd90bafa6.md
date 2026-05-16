[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Mainframe to WEB

_7 messages · 7 participants · 2000-12_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Web, XML, modern integration`](../topics.md#web)

---

### Mainframe to WEB

- **From:** "Brad Prothero" <brad.prothero@clarica.com>
- **Date:** 2000-12-22T11:51:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MxM06.2$t6.1204@news.corpcomm.net>`

```
We have an IBM mainframe that our production code is residing. We want to
port a small subset to the PC to allow Web access to some of the
functionality. The problem that we are running into is how should we deal
with the data in EBCDIC form on the PC. We will be using Fujitsu version 5
compiler on the PC. They have a alphabet clause that can identify EBCDIC but
I have not gotten that to work correctly. I have not tried to use this on a
file but it says that it will work.

The problem that I have is in our working storage, we have 88 levels that
have "'5A' thru '59'". To be able to use this on the PC, we will need to
change this. Has anybody run into this problem before? Is there another
solution other than changing every line where this happens?

We are discussing how to architect this: pass data via MQSeries and do
calculations on the server or pass a request via MQSeries, do the
calculations on the Mainframe, then pass back the results and format on the
server.

Any help would be appreciated.
Brad Prothero
Clarica Life Insurance
Fargo, ND
```

#### ↳ Re: Mainframe to WEB

- **From:** barfly_bob@my-deja.com
- **Date:** 2000-12-22T18:22:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<92065b$k43$1@nnrp1.deja.com>`
- **References:** `<MxM06.2$t6.1204@news.corpcomm.net>`

```
Brad,
I need some details about your shop.  Are you running OS/390?  If so, I
don't see why you want to port some of your application to the PC.  With
OS/390 you have a ready-to-use environment for web-mainframe
integration.  Pls list operating system and CICS version.
Bob

In article <MxM06.2$t6.1204@news.corpcomm.net>,
  "Brad Prothero" <brad.prothero@clarica.com> wrote:
> We have an IBM mainframe that our production code is residing. We want
to
> port a small subset to the PC to allow Web access to some of the
> functionality. The problem that we are running into is how should we
deal
> with the data in EBCDIC form on the PC. We will be using Fujitsu
version 5
> compiler on the PC. They have a alphabet clause that can identify
EBCDIC but
> I have not gotten that to work correctly. I have not tried to use this
on a
> file but it says that it will work.
>
> The problem that I have is in our working storage, we have 88 levels
that
> have "'5A' thru '59'". To be able to use this on the PC, we will need
to
> change this. Has anybody run into this problem before? Is there
another
> solution other than changing every line where this happens?
>
> We are discussing how to architect this: pass data via MQSeries and do
> calculations on the server or pass a request via MQSeries, do the
> calculations on the Mainframe, then pass back the results and format
on the
> server.
>
…[5 more quoted lines elided]…
>


Sent via Deja.com
http://www.deja.com/
```

#### ↳ Re: Mainframe to WEB

- **From:** Support@ScreenIO.com (Kevin J. Hansen)
- **Date:** 2000-12-22T18:48:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a43a138.83820207@news>`
- **References:** `<MxM06.2$t6.1204@news.corpcomm.net>`

```
On Fri, 22 Dec 2000 11:51:52 -0600, "Brad Prothero"
<brad.prothero@clarica.com> wrote:

>We have an IBM mainframe that our production code is residing. We want to
>port a small subset to the PC to allow Web access to some of the
…[9 more quoted lines elided]…
>solution other than changing every line where this happens?
===============
Hi, Brad,

We handled this in our old ScreenIO product on-the-fly by inspecting a
field that we knew always contained "Y" or "N" to determine whether
the rest of the screen data was ASCII or EBCDIC and then just doing a
conversion of the blocks of data.

The situation in that case was that programmers on the PC could set a
compiler option that worked in EBCDIC ratiher than ASCII, which was
nice for running against mainframe data files.  CA-Realia provided
this facility (we had several customers that used it, which is why we
provided the capability in ScreenIO), and Merant may also - I just
don't recall.

It sounds as though Fujitsu's equivalent isn't working for you, but
that would indeed be the easiest approach.  If that doesn't work I
suppose you could investigate a different compiler.

Other than your 88-level items, it is not a difficult issue, but when
I hit that remark I knew you'd need to handle this at the compiler
level - it's not something you can do yourself.

Kevin

Norcom - COBOL Programming Tools
GUI ScreenIO - A Windows UI for COBOL
http://www.screenio.com
```

#### ↳ Re: Mainframe to WEB

- **From:** lcccpiasabird@my-deja.com
- **Date:** 2000-12-22T19:58:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<920bos$omg$1@nnrp1.deja.com>`
- **References:** `<MxM06.2$t6.1204@news.corpcomm.net>`

```
In article <MxM06.2$t6.1204@news.corpcomm.net>,
  "Brad Prothero" <brad.prothero@clarica.com> wrote:

Why not build the data on the mainframe and use CGI to send it through
an IP server or something like that.


> We have an IBM mainframe that our production code is residing. We
want to
> port a small subset to the PC to allow Web access to some of the
> functionality. The problem that we are running into is how should we
deal
> with the data in EBCDIC form on the PC. We will be using Fujitsu
version 5
> compiler on the PC. They have a alphabet clause that can identify
EBCDIC but
> I have not gotten that to work correctly. I have not tried to use
this on a
> file but it says that it will work.
>
> The problem that I have is in our working storage, we have 88 levels
that
> have "'5A' thru '59'". To be able to use this on the PC, we will need
to
> change this. Has anybody run into this problem before? Is there
another
> solution other than changing every line where this happens?
>
> We are discussing how to architect this: pass data via MQSeries and do
> calculations on the server or pass a request via MQSeries, do the
> calculations on the Mainframe, then pass back the results and format
on the
> server.
>
…[5 more quoted lines elided]…
>


Sent via Deja.com
http://www.deja.com/
```

#### ↳ Re: Mainframe to WEB

- **From:** "Paul Raulerson" <praul@isot.com>
- **Date:** 2000-12-22T22:51:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a442fb6$0$143@wodc7nh6.news.uu.net>`
- **References:** `<MxM06.2$t6.1204@news.corpcomm.net>`

```
If you are running OS/390, why not just load the WebServer on there ($800
per processor
for WebSphere standard), and see if you can connect the data on through with
Java or
whatever. It works very well, though it can be a bit of a pain to get setup
correctly.

Especially note you will have to modify some TSO parameters to ensure that
Java can get enough
memory. <grin>

-Paul


"Brad Prothero" <brad.prothero@clarica.com> wrote in message
news:MxM06.2$t6.1204@news.corpcomm.net...
> We have an IBM mainframe that our production code is residing. We want to
> port a small subset to the PC to allow Web access to some of the
> functionality. The problem that we are running into is how should we deal
> with the data in EBCDIC form on the PC. We will be using Fujitsu version 5
> compiler on the PC. They have a alphabet clause that can identify EBCDIC
but
> I have not gotten that to work correctly. I have not tried to use this on
a
> file but it says that it will work.
>
…[7 more quoted lines elided]…
> calculations on the Mainframe, then pass back the results and format on
the
> server.
>
…[5 more quoted lines elided]…
>
```

#### ↳ Re: Mainframe to WEB

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-12-23T12:49:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4C852C8634846645.E6853097F2FDC391.199DD9FC87CFF5E3@lp.airnews.net>`
- **References:** `<MxM06.2$t6.1204@news.corpcomm.net>`

```
On Fri, 22 Dec 2000 11:51:52 -0600, "Brad Prothero"
<brad.prothero@clarica.com> enlightened us:

>We have an IBM mainframe that our production code is residing. We want to
>port a small subset to the PC to allow Web access to some of the
…[20 more quoted lines elided]…
>

Some folks have already asked questions or given you suggestions.  Let
me just add that from my experience, using MQSeries to pass a request
to the mainframe and pass back the results with the formatting being
done on the server is a very good solution.  I've done two
web-mainframe projects in the past two years for several banks and
this is the method that was used.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Practice safe eating, always use condiments.

Help Save The Rainforest
For more info, please see:  
http://www.ran.org/ran/

Remove nospam to email me.

Steve
```

#### ↳ Re: Mainframe to WEB

- **From:** Steve Casey <steven_casey@hotmail.com>
- **Date:** 2000-12-26T08:02:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A4896F3.FA4F139D@hotmail.com>`
- **References:** `<MxM06.2$t6.1204@news.corpcomm.net>`

```
IBM also has several products (no, not and employee) that were demo'ed here
which will qickly get applications up on the web.  IBM Screen Customizer is the
entry level one that will make 3270-ish screens over the web and more.

Brad Prothero wrote:

> We have an IBM mainframe that our production code is residing. We want to
> port a small subset to the PC to allow Web access to some of the
…[19 more quoted lines elided]…
> Fargo, ND
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
