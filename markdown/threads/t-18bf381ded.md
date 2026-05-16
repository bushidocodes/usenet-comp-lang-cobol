[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Network API and cobol

_4 messages · 4 participants · 1999-05_

---

### Network API and cobol

- **From:** "Tom Wright" <tawright@i1.net>
- **Date:** 1999-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6kn33.27$WA.238585@news1.i1.net>`

```
Has anyone ever successfully used implimented a tcp/ip connection over a
network using cobol?  If so can you help in pointing me in the right
direction.

Thanks
Tom Wright
twright@larimore.net
```

#### ↳ Re: Network API and cobol

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<374e11ea.784622696@news1.ibm.net>`
- **References:** `<6kn33.27$WA.238585@news1.i1.net>`

```
On Thu, 27 May 1999 21:38:46 -0500, "Tom Wright" <tawright@i1.net>
wrote:

>Has anyone ever successfully used implimented a tcp/ip connection over a
>network using cobol?  If so can you help in pointing me in the right
>direction.

http://www.geocities.com/Eureka/2006/download.htm

I have an example there using Fujitsu COBOL and MicroFocus Cobol
(written by someone else, who deserves credit but who's name I cannot
remember this late) of Winsock2 API calls.  I have used this method to
interface PC to PC and Pc to Mainframe via TCP/IP.
```

#### ↳ Re: Network API and cobol

- **From:** "Gazaloo" <gaz@home.com>
- **Date:** 1999-05-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xqo33.2551$u03.1669@news.rdc1.sfba.home.com>`
- **References:** `<6kn33.27$WA.238585@news1.i1.net>`

```
Tom Wright <tawright@i1.net> wrote in message
news:6kn33.27$WA.238585@news1.i1.net...
> Has anyone ever successfully used implimented a tcp/ip connection over a
> network using cobol?  If so can you help in pointing me in the right
> direction.

Tom, MERANT's Micro Focus compiler products have a proprietary run-time API
called CCI (Common Communication Interface, i think) which enable you to
establish such a connection (from/to NT to/from UNIX too). indeed, the
Fileshare (networked file i/o) service uses CCI for all of it's comms.
```

##### ↳ ↳ Re: Network API and cobol

- **From:** Mr. Scott <scott_davis@my-deja.com>
- **Date:** 1999-05-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7im860$j6v$1@nnrp1.deja.com>`
- **References:** `<6kn33.27$WA.238585@news1.i1.net> <Xqo33.2551$u03.1669@news.rdc1.sfba.home.com>`

```
Also, if you're running under Unix, you can make direct system calls to
the sockets API.  I did, and it works great.  Columbia Sportsware's
entire warehouse is automated under a COBOL sockets program I wrote.
If you'd like to see some code I'd be more than happy to supply it.
Just reply back.


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
