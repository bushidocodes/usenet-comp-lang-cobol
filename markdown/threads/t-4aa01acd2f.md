[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol via web

_5 messages · 4 participants · 2004-04_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### Cobol via web

- **From:** jchipocov@yahoo.com.ar (Juan)
- **Date:** 2004-04-06T16:40:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf8a559b.0404061540.754280c1@posting.google.com>`

```
Hi guys

I need to access a Cobol application via web.
Someone has tried something like that?
A friend told me about tarantella but it implies to install a client
in every box.
I would prefer that my clients access my application without has to
install some program.

I hope that someone can help me.

Thanks in advance.

Juan
```

#### ↳ Re: Cobol via web

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-04-07T00:43:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0404062343.2b44aaae@posting.google.com>`
- **References:** `<bf8a559b.0404061540.754280c1@posting.google.com>`

```
jchipocov@yahoo.com.ar (Juan) wrote

> I need to access a Cobol application via web.
> Someone has tried something like that?
…[3 more quoted lines elided]…
> install some program.

There are several ways including:

Implement the system on Linux and use telnet or ssh (secure shell) to
access it.  Use normal xterm and ssh on a Linux client, the almost
useless Windows telnet or putty with ssh on Windows client, or Java
telnet client (optional ssh) from almost anything, including some
PDAs.

The application could be written using Xopen accept display or SP/2
text GUI.

Use SP/2 thin client to Linux or Windows server.  This requires a
client to be installed, but it could be done over the initial
connection using a web browser.

Write your application to run as a CGI web server using html forms and
have it accessed from web browsers.

I think that ACCU have a web client system.
```

##### ↳ ↳ Re: Cobol via web

- **From:** meshi101@bezeqint.net (BGMeshi)
- **Date:** 2004-04-07T13:41:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dff57de5.0404071241.419444df@posting.google.com>`
- **References:** `<bf8a559b.0404061540.754280c1@posting.google.com> <217e491a.0404062343.2b44aaae@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0404062343.2b44aaae@posting.google.com>...
> jchipocov@yahoo.com.ar (Juan) wrote
> 
…[7 more quoted lines elided]…
> There are several ways including:

What COBOL dialect do you use?
```

###### ↳ ↳ ↳ Re: Cobol via web

- **From:** jchipocov@yahoo.com.ar (Juan)
- **Date:** 2004-04-08T20:33:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf8a559b.0404081933.37723c94@posting.google.com>`
- **References:** `<bf8a559b.0404061540.754280c1@posting.google.com> <217e491a.0404062343.2b44aaae@posting.google.com> <dff57de5.0404071241.419444df@posting.google.com>`

```
I am using runcobol for SCO running in a Linux RH 9.0 box
Thanks for your interest

Juan


meshi101@bezeqint.net (BGMeshi) wrote in message news:<dff57de5.0404071241.419444df@posting.google.com>...
> riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0404062343.2b44aaae@posting.google.com>...
> > jchipocov@yahoo.com.ar (Juan) wrote
…[10 more quoted lines elided]…
> What COBOL dialect do you use?
```

##### ↳ ↳ Re: Cobol via web

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2004-04-12T20:34:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v6vl70tpap9mjpqkuehtoeog1k2eh7k4ie@4ax.com>`
- **References:** `<bf8a559b.0404061540.754280c1@posting.google.com> <217e491a.0404062343.2b44aaae@posting.google.com>`

```
Richard:

We also have a product which does not require any client component
installation.  It allows a web server to serve HTML/Javascript user
interface screens from a standard COBOL sp2 program.

It even supports the ability to display Macromedia Flash user
interface screens.

The product is called Web Client.



riplin@Azonic.co.nz (Richard) wrote:

>jchipocov@yahoo.com.ar (Juan) wrote
>
…[25 more quoted lines elided]…
>I think that ACCU have a web client system.


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
