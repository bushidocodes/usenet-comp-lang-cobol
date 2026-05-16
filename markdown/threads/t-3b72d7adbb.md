[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cgi application, Microfocus vs Fujitsu

_5 messages · 4 participants · 2003-09 → 2003-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Web, XML, modern integration`](../topics.md#web)

---

### cgi application, Microfocus vs Fujitsu

- **From:** "Russell Styles" <RWS0202@COMCAST.NET>
- **Date:** 2003-09-23T15:33:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GjKdnfitIPCyPe2iU-KYvg@comcast.com>`

```
    We have been working on a cgi application under Microfocus Cobol, Netx
3.1.

    We would like to switch to fujitsu, because of runtime prices.

    Does anyone have any experience in this area.  Which fujitsu compiler
should we work
with.  They have Netcobol and the .NET compiler.  The newest .Net compiler
does correct
many of the shortcomings of Version 1, such as no sort.  Extracting this
sort of data
from advertising copy is extremly difficult (they never come out and SAY
that they don't
support X Y and Z).

    How compatible is the cgi syntax in Microfocus and Fujitsu?

    They have dialect converters.  Do they handle CGI code?

    I am going to contact Fujitsu and see what they say, but I wanted some
outside opinions.
```

#### ↳ Re: cgi application, Microfocus vs Fujitsu

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-09-24T08:58:00+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f70d10e_5@news.athenanews.com>`
- **References:** `<GjKdnfitIPCyPe2iU-KYvg@comcast.com>`

```
Russell,

I have been using CGI/ISAPI with Fujitsu NetCOBOL for around 2 and a half
years now.

I am currently in Melbourne working with a team where we are using Fujitsu
CGI every day.

They have an excellent interface to CGI (provides a lot of environment stuff
like the TCP/IP address etc., you can "migrate" to ISAPI (multithreaded) if
the need arises, and they provide tools which are also good for generating
much of the code.

I found one area where their CGI stuff fell down and I was never able to get
it to work. (It concerned replacement of variables in Web Pages). I simply
wrote this function for myself and what I have works a treat. (I will gladly
let you have it if you go ahead, and strike the same problem I did.)

Can't comment on .Net compiler as I can't afford to buy it <G>.

Both NetCOBOL (I am using Version 6) and PowerCOBOL are EXCELLENT products.

Pete.


"Russell Styles" <RWS0202@COMCAST.NET> wrote in message
news:GjKdnfitIPCyPe2iU-KYvg@comcast.com...
>     We have been working on a cgi application under Microfocus Cobol, Netx
> 3.1.
…[21 more quoted lines elided]…
>
```

#### ↳ Re: cgi application, Microfocus vs Fujitsu

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-23T22:39:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309232139.6d456324@posting.google.com>`
- **References:** `<GjKdnfitIPCyPe2iU-KYvg@comcast.com>`

```
"Russell Styles" <RWS0202@COMCAST.NET> wrote 

>     Does anyone have any experience in this area.  Which fujitsu compiler
> should we work with.  

I have Cobol CGI programs that run with several combinations of
compiler, OS and Web Server including: MicroFocus, MicroSoft (eq MF
3.0), Fujitsu / DOS, OS/2, Windows 3.1 and Win32, SCO Unix, Linux /
Apache, Xitami, Netscape.

There are some minor differences between Windows start up and the rest
because Windows needs a message queue, but only a few lines. The code
uses standard CGI accessed using ACCEPT DISPLAY and does its own
templating.  The down side is that it doesn't (as yet) access any of
the various different fast-CGI mechanisms.

It isn't hard to access the standard CGI mechanism.
```

#### ↳ Re: cgi application, Microfocus vs Fujitsu

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-09-24T08:20:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0309240720.3a138578@posting.google.com>`
- **References:** `<GjKdnfitIPCyPe2iU-KYvg@comcast.com>`

```
Even using the NetCOBOL for .NET - Fujitsu DOES have runtime fees if
you are usign a server with multiple processors - so get prices before
you jump.

Using NetCOBOL for Windows - if you buy Enterprise edition the runtime
fee is waived for servers.

I have no experience using NetCOBOL for .NET with CGI but I do use the
NetCOBOL for Windows with Flexus Web client - which provides a Robust
and easy to use CGI environment.

"Russell Styles" <RWS0202@COMCAST.NET> wrote in message news:<GjKdnfitIPCyPe2iU-KYvg@comcast.com>...
> We have been working on a cgi application under Microfocus Cobol, Netx
> 3.1.
…[18 more quoted lines elided]…
> outside opinions.
```

##### ↳ ↳ Re: cgi application, Microfocus vs Fujitsu

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-10-03T14:37:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0310031337.4f716e66@posting.google.com>`
- **References:** `<GjKdnfitIPCyPe2iU-KYvg@comcast.com> <bfdfc3e8.0309240720.3a138578@posting.google.com>`

```
I need to post a correction to my message.  I have been informed that
sometime this year Fujitsu removed the runtime fees for multiple
processors when using Fujitsu NetCOBOL for .NET.


thaneh@softwaresimple.com (Thane Hubbell) wrote in message news:<bfdfc3e8.0309240720.3a138578@posting.google.com>...
> Even using the NetCOBOL for .NET - Fujitsu DOES have runtime fees if
> you are usign a server with multiple processors - so get prices before
…[30 more quoted lines elided]…
> > outside opinions.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
