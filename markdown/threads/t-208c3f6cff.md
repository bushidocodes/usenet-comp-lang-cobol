[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# TCP Client Sample Code with Winsock

_3 messages · 2 participants · 2008-03_

---

### TCP Client Sample Code with Winsock

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2008-03-01T07:20:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77cadb10-eef3-4e79-99c8-3d2329c64153@i12g2000prf.googlegroups.com>`

```
Guess someones familiar with this topic before.

Anyway, I was browsing this Group concerning Cobol Winsock samples and
came across this topic way back. The discussions points out to this
website (below) which turned out to be a bad link.

"COBOL TCP/IP routines that use WinSock in the FREE download library
of www.aboutlegacycoding.com" (posted by Thane Hubbell)

It says something about downloading a "sockets.zip" file concerning
samples. Anyone who has that ZIP file? I have been experimenting A LOT
with web services but I needed some samples as well that I might need
using Winsock.
```

#### ↳ Re: TCP Client Sample Code with Winsock

- **From:** Thane <thaneh@softwaresimple.com>
- **Date:** 2008-03-03T17:33:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cfd49e90-9bd3-4920-b497-5b224595884f@z17g2000hsg.googlegroups.com>`
- **References:** `<77cadb10-eef3-4e79-99c8-3d2329c64153@i12g2000prf.googlegroups.com>`

```
http://www.geocities.com/Eureka/2006/download.htm

The zip file (sockets.zip) is there and has TCP socket communication
examples for MicroFocus, Fujitsu and AcuCOBOL.
This provides TCP socket communication but not anything like html -
it's much lower level than that.

However, having done some web service integration myself I suggest
using:

http://www.pocketsoap.htm

And your compilers OLE interface.

If your compiler can't do COM - check out http://www.flexus.com.  You
can use the sp2 ActiveX interface to interface to COM from any COBOL
compiler.


On Mar 1, 9:20 am, Rene_Surop <infodynamics...@yahoo.com> wrote:
> Guess someones familiar with this topic before.
>
…[10 more quoted lines elided]…
> using Winsock.
```

##### ↳ ↳ Re: TCP Client Sample Code with Winsock

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2008-03-04T00:13:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1939bb48-badb-430e-84b0-7e7a46a52d0e@e6g2000prf.googlegroups.com>`
- **References:** `<77cadb10-eef3-4e79-99c8-3d2329c64153@i12g2000prf.googlegroups.com> <cfd49e90-9bd3-4920-b497-5b224595884f@z17g2000hsg.googlegroups.com>`

```
Thanks Thane.

Im using MF compiler and it works with COM (could generate COM
application using a wizard). Noticed in your site that you are posting
Cobol applications, maybe I could contribute somehow.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
