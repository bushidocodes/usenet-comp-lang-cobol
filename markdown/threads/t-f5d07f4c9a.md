[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus Fileshare via Internet

_14 messages · 5 participants · 2003-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Web, XML, modern integration`](../topics.md#web)

---

### MicroFocus Fileshare via Internet

- **From:** "Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s>
- **Date:** 2003-04-22T09:55:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b83hk6$7hu$1@nntp2-cm.news.eni.net>`

```
Looking for some information on using MicroFocus FileShare via the
internet...Has anyone here developed an application where the users actually
access FileShare datasets via an internet connection?

Is it possible to safely place a UNIX server running FileShare on the
internet...

What are the security concerns in doing so? CCI/Fileshare can be configured
to use a specific port address...If this is the only port open, is there a
security issue?

The application in question would be a simple Windows GUI with clients
retrieving small amounts of data from a single UNIX server running
FileShare...
```

#### ↳ Re: MicroFocus Fileshare via Internet

- **From:** "Lorne Sunley" <lsunley@mb.sympatico.ca>
- **Date:** 2003-04-22T14:43:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JMPlV5b5VFnN-pn2-VjJVHLz6d1vL@h24-82-204-17.wp.shawcable.net>`
- **References:** `<b83hk6$7hu$1@nntp2-cm.news.eni.net>`

```
On Tue, 22 Apr 2003 13:55:19 UTC, "Ken Mullins" 
<**Ken**Mullins**@**mindspring.com** remove **'s> wrote:

> Looking for some information on using MicroFocus FileShare via the
> internet...Has anyone here developed an application where the users actually
…[15 more quoted lines elided]…
> 

I tried it once back in the MF Workbench 3.4 days as a test. It worked
OK as long as you had at least 56 KByte/second bandwidth. It was a 
small data entry application that was compiled to use the fileshare 
redirector and I just set up a fileshare server on a machine that had 
internet access.

For the best security, use a firewall that will allow you to specify 
which hosts (IP addresses) are allowed to connect to the port you 
leave open for fileshare.
```

##### ↳ ↳ Re: MicroFocus Fileshare via Internet

- **From:** "Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s>
- **Date:** 2003-04-22T17:20:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b84bnr$6ok$1@nntp2-cm.news.eni.net>`
- **References:** `<b83hk6$7hu$1@nntp2-cm.news.eni.net> <JMPlV5b5VFnN-pn2-VjJVHLz6d1vL@h24-82-204-17.wp.shawcable.net>`

```
Dial in access wouldn't have hard ip addresses to code into a router...

kenmullins

"Lorne Sunley" <lsunley@mb.sympatico.ca> wrote in message
news:JMPlV5b5VFnN-pn2-VjJVHLz6d1vL@h24-82-204-17.wp.shawcable.net...
> On Tue, 22 Apr 2003 13:55:19 UTC, "Ken Mullins"
> <**Ken**Mullins**@**mindspring.com** remove **'s> wrote:
>
> > Looking for some information on using MicroFocus FileShare via the
> > internet...Has anyone here developed an application where the users
actually
> > access FileShare datasets via an internet connection?
> >
…[3 more quoted lines elided]…
> > What are the security concerns in doing so? CCI/Fileshare can be
configured
> > to use a specific port address...If this is the only port open, is there
a
> > security issue?
> >
…[19 more quoted lines elided]…
> Lorne Sunley
```

###### ↳ ↳ ↳ Re: MicroFocus Fileshare via Internet

- **From:** "Lorne Sunley" <lsunley@mb.sympatico.ca>
- **Date:** 2003-04-23T00:04:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JMPlV5b5VFnN-pn2-D3LS3Ijd6M5l@h24-82-204-17.wp.shawcable.net>`
- **References:** `<b83hk6$7hu$1@nntp2-cm.news.eni.net> <JMPlV5b5VFnN-pn2-VjJVHLz6d1vL@h24-82-204-17.wp.shawcable.net> <b84bnr$6ok$1@nntp2-cm.news.eni.net>`

```
In that case you might want to look at a VPN solution for the 
security. There are a number of IPSEC VPN solutions available. I use 
the one from Injoy http://www.fx.dk theirs will support OS/2, Windows,
Linux, and FreeBSD  and will connect to most other IPSEC gateways.

Lorne

On Tue, 22 Apr 2003 21:20:48 UTC, "Ken Mullins" 
<**Ken**Mullins**@**mindspring.com** remove **'s> wrote:

> Dial in access wouldn't have hard ip addresses to code into a router...
> 
…[42 more quoted lines elided]…
> 
```

#### ↳ Re: MicroFocus Fileshare via Internet

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2003-04-22T12:41:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA570D0.90509@newsguy.com>`
- **References:** `<b83hk6$7hu$1@nntp2-cm.news.eni.net>`

```
Ken Mullins wrote:
 > Looking for some information on using MicroFocus FileShare via the
 > internet...Has anyone here developed an application where the users
…[7 more quoted lines elided]…
 > open, is there a security issue?

There's *always* a security issue when any system is connected to a
network; there's more risk when that network is open to all comers (ie
the Internet); there's additional risk for each open port on the machine.

Security researchers have seen clean systems scanned and compromised in
less than an hour after being connected to the Internet.  Expect that
bots and script kiddies will be attacking your machine frequently, and
on occasion competent, knowledgeable attackers will be having a look as
well.

You will want to use CCI's direct-connection mechanism (fixed port) -
otherwise you'd have to leave the machine wide open - but this won't
prevent any attacker from finding the open port; a simple port scan will
reveal it.

CCI is not designed to be intrusion-resistant.  I don't work on
Fileshare, but I don't believe it is either.  It has security
mechanisms, but AFAIK it's not hardened against malicious penetration
through malformed data and the like.  And I don't believe its security
mechanisms are resistant to snooping, either, so I hope you're not using
this application to transfer any sensitive data.  Fileshare is a nice
product in many ways, but it's not designed to be a secure Internet
filesystem.

Any system on the Internet should be firewalled.  I prefer a dedicated
firewall as the first line of defense, plus some variety of firewall
software on each system behind it.  (For Unix, this might be
tcp_wrappers plus some kind of IDS and filesystem consistency checker,
and of course usual security practices like minimizing servers,
prefering more secure server implementations, keeping server patch
levels up to date, policing user account security, etc.)

Lorne Sunley recommended restricting clients by IP address; that's
definitely a good idea.  It's not foolproof, but getting around it is
sufficiently difficult (particularly for a remote attacker) that it's
probably not worth anyone's time.  Even if your app was sending fairly
desirable data (eg credit card info), there are easier ways to get it.

Frankly, though, I'd use a VPN.  I wouldn't want to expose any server
that's not designed to resist attacks on the Internet.  Even many that
(ostensibly) are have been repeatedly shown to be vulnerable.  VPNs are
far from foolproof, but they do raise the bar.

I certainly don't want to discourage you from using our products, but I
wouldn't want you to have a mistaken impression about what is and isn't
safe to do with them.  I'd have the same comments if you asked about
sharing files over the Internet with NFS or SMB.

Disclaimer: I don't speak for Micro Focus, of course.
```

#### ↳ Re: MicroFocus Fileshare via Internet

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-22T12:52:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304221152.67fc8463@posting.google.com>`
- **References:** `<b83hk6$7hu$1@nntp2-cm.news.eni.net>`

```
"Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s> wrote 

> Looking for some information on using MicroFocus FileShare via the
> internet...Has anyone here developed an application where the users actually
…[3 more quoted lines elided]…
> internet...

Safely ? No.

If the clients are specific machines then you could set up VPNs or
block everything else at a firewall, but these may be restrictive in
other ways that are unacceptable.
 
> What are the security concerns in doing so? CCI/Fileshare can be configured
> to use a specific port address...If this is the only port open, is there a
> security issue?

Script kiddies use port scanners to find open ports and will poke at
them to see what respoonse they get.  While it is extremely unlikely
that they would understand what it is doing, it is possible that they
could send stuff that breaks fileshare.
 
> The application in question would be a simple Windows GUI with clients
> retrieving small amounts of data from a single UNIX server running
> FileShare...

Why not have a simple CGI Cobol program that receives a HTTP request
and sends a response (it needn't be HTML) back to the client ?
```

##### ↳ ↳ Re: MicroFocus Fileshare via Internet

- **From:** "Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s>
- **Date:** 2003-04-22T17:22:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b84brj$739$1@nntp2-cm.news.eni.net>`
- **References:** `<b83hk6$7hu$1@nntp2-cm.news.eni.net> <217e491a.0304221152.67fc8463@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message

> Why not have a simple CGI Cobol program that receives a
> HTTP request
> and sends a response (it needn't be HTML) back to the client ?

This would require a web based server like IIS ?  If so the runtime fees
from MF are horrible...I think 10k or something like that...

kenmullins
```

###### ↳ ↳ ↳ Re: MicroFocus Fileshare via Internet

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-22T22:47:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-394736.22475522042003@corp.supernews.com>`
- **References:** `<b83hk6$7hu$1@nntp2-cm.news.eni.net> <217e491a.0304221152.67fc8463@posting.google.com> <b84brj$739$1@nntp2-cm.news.eni.net>`

```
In article <b84brj$739$1@nntp2-cm.news.eni.net>,
 "Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s> wrote:

> "Richard" <riplin@Azonic.co.nz> wrote in message
> 
…[7 more quoted lines elided]…
> kenmullins

Is that 10k a month? Year? Single time?

Why not use apache and hand code a module to hand-off CGI requests to 
your Cobol code.
```

###### ↳ ↳ ↳ Re: MicroFocus Fileshare via Internet

_(reply depth: 4)_

- **From:** "Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s>
- **Date:** 2003-04-23T11:54:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b86d09$k04$1@nntp2-cm.news.eni.net>`
- **References:** `<b83hk6$7hu$1@nntp2-cm.news.eni.net> <217e491a.0304221152.67fc8463@posting.google.com> <b84brj$739$1@nntp2-cm.news.eni.net> <joe_zitzelberger-394736.22475522042003@corp.supernews.com>`

```

"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote> Is that 10k a month?
Year? Single time?

10k annually I believe...

> Why not use apache and hand code a module to hand-off CGI requests to your
Cobol code.

I personally have never coded CGI nor developed in a UNIX environment...

kenmullins
```

###### ↳ ↳ ↳ Re: MicroFocus Fileshare via Internet

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-23T14:22:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304231322.5ed04da3@posting.google.com>`
- **References:** `<b83hk6$7hu$1@nntp2-cm.news.eni.net> <217e491a.0304221152.67fc8463@posting.google.com> <b84brj$739$1@nntp2-cm.news.eni.net> <joe_zitzelberger-394736.22475522042003@corp.supernews.com> <b86d09$k04$1@nntp2-cm.news.eni.net>`

```
"Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s> wrote

> > Why not use apache and hand code a module to hand-off CGI requests to your
> Cobol code.
> 
> I personally have never coded CGI nor developed in a UNIX environment...

Apache and Xitami run on Windows as well as Unix/Linux, OS/2 and many
others.

In fact my Cobol CGI programs run on OS/2+Xitami, Windows+Xitami,
Linux+Apache, SCO+NetScape Server with only minor differences.  The
main difference for Windows is that I built it statically linked as a
Windows API program so it does have a message loop.  But this is only
one small module that is the 'main'.  All the other programs are
identical between versions.

To get the ACCEPTs to work with MF I do a CALL x'A7' to redirect to
stdin/stdout.

The program then get the environment strings including CONTENT-LENGTH
which is used when accepting the POST request string as a reference
modification:

       ACCEPT Request-Buffer(1:Content-Length) FROM CONSOLE
Actually the program determines the OS and uses a "DosRead" under
OS/2. It is also coded to take the stuff from a file using so called
WinCGI which I think MS PWS uses.

For output just DISPLAY a MIME header for text, two CR/LF and the data
items as a text string.

You will be able to control access to only genuine clients because
once they have done some sort of logon you can send them a response
number which they must  modify and return for the next request they
make.

Of course you could also add a real CGI enquiry system to give a wider
access. Apart form catalog browsing and order creation, I also give
logged in users (identified customers) access to lists of their
previous orders, invoices, current back order list, request reprints
of invoices, etc so that they don't have to ring up and take staff
time.
If the company salesmen log in they get special privileges, such as
viewing any account's sales data and account balances and also viewing
purchase order details for expected arrival times.  This allows them
to keep up to date when on the road.
```

###### ↳ ↳ ↳ Re: MicroFocus Fileshare via Internet

_(reply depth: 6)_

- **From:** "Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s>
- **Date:** 2003-04-24T08:58:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b88n13$b94$1@nntp2-cm.news.eni.net>`
- **References:** `<b83hk6$7hu$1@nntp2-cm.news.eni.net> <217e491a.0304221152.67fc8463@posting.google.com> <b84brj$739$1@nntp2-cm.news.eni.net> <joe_zitzelberger-394736.22475522042003@corp.supernews.com> <b86d09$k04$1@nntp2-cm.news.eni.net> <217e491a.0304231322.5ed04da3@posting.google.com>`

```
Richard:

Interesting...Do you use MF NetExpress or and older MF compiler product?
What are the runtime fees for such an application?

kenmullins


"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0304231322.5ed04da3@posting.google.com...
> "Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s> wrote
>
> > > Why not use apache and hand code a module to hand-off CGI requests to
your
> > Cobol code.
> >
…[41 more quoted lines elided]…
> to keep up to date when on the road.
```

###### ↳ ↳ ↳ Re: MicroFocus Fileshare via Internet

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-22T19:49:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304221849.392ed643@posting.google.com>`
- **References:** `<b83hk6$7hu$1@nntp2-cm.news.eni.net> <217e491a.0304221152.67fc8463@posting.google.com> <b84brj$739$1@nntp2-cm.news.eni.net>`

```
"Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s> wrote

> 
> This would require a web based server like IIS ?  

Apache  - free - see www.apache.org
Xitami  - free - see www.xitami.com

Others are also available.

> If so the runtime fees
> from MF are horrible...I think 10k or something like that...

It is not difficult to get Cobol to run as a simple CGI program
without the vendor CGI interfacing.  All it needs is ACCEPT from
console (with S5 on) and DISPLAY UPON CONSOLE.
```

###### ↳ ↳ ↳ Re: MicroFocus Fileshare via Internet

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2003-04-23T10:11:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA69F08.8050709@newsguy.com>`
- **References:** `<b83hk6$7hu$1@nntp2-cm.news.eni.net> <217e491a.0304221152.67fc8463@posting.google.com> <b84brj$739$1@nntp2-cm.news.eni.net>`

```
Ken Mullins wrote:
 > "Richard" <riplin@Azonic.co.nz> wrote in message
 >
…[5 more quoted lines elided]…
 > fees from MF are horrible...I think 10k or something like that...

Apache runs on Windows and is free:

	<http://httpd.apache.org/>

Because Apache is a portable HTTP server, and not designed and tuned
specifically for Windows, it doesn't perform quite as well on (server
versions of) Windows as IIS does.  However, network is almost certainly
going to be your bottleneck here, so that shouldn't be a significant factor.

CGI is a (draft) standard, so a COBOL CGI program will work the same
under Apache as it does under IIS.  (I think Apache also has a module
for ISAPI now, but frankly I'd go with CGI unless you find you simply
can't get adequate performance with it.  It's considerably safer, since
it isolates the application from the server.)

The client would have to parse off the HTTP headers, but that's easy:
discard everything up to and including the first sequence of CR LF CR
LF.  The CGI program can return records straight from your file if you
like - HTTP will happily transport anything.
```

#### ↳ Re: MicroFocus Fileshare via Internet

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2003-04-24T13:37:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0ppfavshno39ud24pot3r10q5hstfs4jf9@4ax.com>`
- **References:** `<b83hk6$7hu$1@nntp2-cm.news.eni.net>`

```
"Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s> wrote:

>Looking for some information on using MicroFocus FileShare via the
>internet...Has anyone here developed an application where the users actually
…[11 more quoted lines elided]…
>FileShare...

Ken:

COBOL sp2 for the GUI and Thin Client for the TCP/IP internet support.

100% of the COBOL resides and executes on the UNIX server.  The only
data which transports across the network connection is a small
parameter block containing screen handling instructions and screen
data.  It is lightning fast.

Thin Client takes care of all of the TCP/IP headaches and includes a
plethora of utilities to encrypt data (128 bit), compress data,
automate version control and installation of client-side components.

In addition, you can employ the use of Active X controls on the client
(if desired) so that your application can have just about any type of
GUI control desired.

You can also include FormPrint to control printing from the UNIX-based
COBOL program, but print on the remote client-side machines via
TCP/IP.  FormPrint supports the Windows Print Manager, so Windows
printing is greatly simplified.

Send a private e-mail message for more details.




Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
