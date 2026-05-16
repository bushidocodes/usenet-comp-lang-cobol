[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# revamping an old application

_7 messages · 6 participants · 2001-07 → 2001-08_

---

### revamping an old application

- **From:** dedalus@yifan.net (Duilio Foschi)
- **Date:** 2001-07-27T10:39:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b6142b7.3220441@news.libero.it>`

```
I need to revamp an old application written in Cobol for SCO-Unix and
using green-screen UI into something that can run on Windows clients
in a client-server architecture.

I heard of sw tools that can help me in this.

Any hint  ?

Thank you

Duilio Foschi
```

#### ↳ Re: revamping an old application

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-07-27T09:46:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0107270846.53245cf4@posting.google.com>`
- **References:** `<3b6142b7.3220441@news.libero.it>`

```
Check out COBOL Sp2 from http://www.flexus.com.

Using their Thin Client option your application continues to run on
the UNIX server (using the same COBOL compiler you use now if you
like) and the UI runs on the Windows Desktop.  You can even PRINT on
the Windows machines if you like using Windows based printing.

It does exactly what you are looking to do.



dedalus@yifan.net (Duilio Foschi) wrote in message news:<3b6142b7.3220441@news.libero.it>...
> I need to revamp an old application written in Cobol for SCO-Unix and
> using green-screen UI into something that can run on Windows clients
…[8 more quoted lines elided]…
> Duilio Foschi
```

#### ↳ Re: revamping an old application

- **From:** "Lloyd Clarke" <lloydc@ndms.org>
- **Date:** 2001-07-27T20:23:52+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b61c49c_3@mk-nntp-1.news.uk.worldonline.com>`
- **References:** `<3b6142b7.3220441@news.libero.it>`

```
Duilio,

Sounds like you're just the customer for our Cobol to VB conversion - a
genuine client-server solution.
See web site below.

Note that we also have an offering that uses a thin client for the dedicated
Cobollers.

Best regards,

Lloyd

Send any abuse to Lloyd@NDMS.Org

http://www.ndms.org/


Duilio Foschi <dedalus@yifan.net> wrote in message
news:3b6142b7.3220441@news.libero.it...
> I need to revamp an old application written in Cobol for SCO-Unix and
> using green-screen UI into something that can run on Windows clients
…[9 more quoted lines elided]…
>
```

##### ↳ ↳ Re: revamping an old application

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2001-08-06T20:20:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b6efb9d.24189894@news.epix.net>`
- **References:** `<3b6142b7.3220441@news.libero.it> <3b61c49c_3@mk-nntp-1.news.uk.worldonline.com>`

```
Lloyd:

I'm curious to know how your Thin Client works.  Is it your own thin
client communications components or a generic soplution such as that
from Citrix or Microsoft Terminal Server?

Just curious.



"Lloyd Clarke" <lloydc@ndms.org> wrote:

>Duilio,
>
…[31 more quoted lines elided]…
>


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: revamping an old application

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-08-07T15:07:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0108071407.12e56a23@posting.google.com>`
- **References:** `<3b6142b7.3220441@news.libero.it> <3b61c49c_3@mk-nntp-1.news.uk.worldonline.com> <3b6efb9d.24189894@news.epix.net>`

```
I discounted Lloyd's solution because as far as I know it won't allow
the COBOL to continue to run on Unix.  I could be wrong though.  As I
recall his solution eliminates the COBOL code - so unless there is
some way to run VB on UNIX that I am unaware of....


rtwolfe@flexus.com (Bob Wolfe) wrote in message news:<3b6efb9d.24189894@news.epix.net>...
> Lloyd:
> 
…[49 more quoted lines elided]…
> Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: revamping an old application

_(reply depth: 4)_

- **From:** "Acucorp News" <shaun_gough@hotmail.com>
- **Date:** 2001-08-08T13:11:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1451C740A890D411B65C00104B95B1C03032D8@ras.acucorp.com>`
- **References:** `<3b6142b7.3220441@news.libero.it> <3b61c49c_3@mk-nntp-1.news.uk.worldonline.com> <3b6efb9d.24189894@news.epix.net> <bfdfc3e8.0108071407.12e56a23@posting.google.com>`

```
Acucorp will be releasing a Thin Client product which does exact what you
want to do.  The release date for this is October.    The product is
designed so that the application is stored on the UNIX server, where it is
to execute.

On the client side, you would have a small runtime, that calls the program
on the server.   The program is executed on the server, but is displayed on
the client's screen.

Please do not hesitate to contact me if you would like further information.

Thanks
Shaun Gough - Snr Technical Support Representative
ACUCORP Inc.
8515 Miralani Drive, San Diego, CA 92126, USA
E-Mail: sgough@acucorp.com
http://www.acucorp.com

Acucorp 12th Annual Developers' Conference, September 24-25, 2001.
Learn about Acucorp's latest technology. Meet Acucorp's Developers and
Technical Experts. Hear how Acucorp's technology users solve their business
problems. Discover tomorrow's technology trends from industry experts. To
find out more, please give Acucorp a call, 1-800-262-6585 or visit our Web
site at http://www.acucorp.com/confr/confr.html.


"Thane Hubbell" <thaneh@softwaresimple.com> wrote in message
news:bfdfc3e8.0108071407.12e56a23@posting.google.com...
> I discounted Lloyd's solution because as far as I know it won't allow
> the COBOL to continue to run on Unix.  I could be wrong though.  As I
…[4 more quoted lines elided]…
> rtwolfe@flexus.com (Bob Wolfe) wrote in message
news:<3b6efb9d.24189894@news.epix.net>...
> > Lloyd:
> >
…[16 more quoted lines elided]…
> > >Note that we also have an offering that uses a thin client for the
dedicated
> > >Cobollers.
> > >
…[30 more quoted lines elided]…
> > Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: revamping an old application

- **From:** "Charles F. Townsend" <ctowns@ix.netcom.com>
- **Date:** 2001-08-09T05:50:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B728716.6F3620ED@ix.netcom.com>`
- **References:** `<3b6142b7.3220441@news.libero.it>`

```
Dulio,
LegacyJ has customers doing exactly what you would like to accomplish
with PERCobol for Caldera (SCO) Unixware.  The graphical user interface
can be accomplished by using a graphical SCREEN SECTION or with BlueJ a
graphical user interface creation tool available on graphical platforms.

If you would like to learn more about LegacyJ PERCobol or BlueJ check out
http://www.legacyj.com

Charles Townsend
LegacyJ


Duilio Foschi wrote:

> I need to revamp an old application written in Cobol for SCO-Unix and
> using green-screen UI into something that can run on Windows clients
…[8 more quoted lines elided]…
> Duilio Foschi
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
