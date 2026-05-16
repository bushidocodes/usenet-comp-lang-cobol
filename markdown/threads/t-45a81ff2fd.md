[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Remote Compilation

_8 messages · 6 participants · 2004-08_

---

### Remote Compilation

- **From:** sng@lemosoft.com (Sergey Grigorchuk)
- **Date:** 2004-08-25T08:52:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a6be1ec.0408250752.6e2acc37@posting.google.com>`

```
Our company develops Lemo Cobol IDE and we are going to implement
Remote Compilation. This feature allows to compile the sources on a
remote server using network.

We would like to know how you use remote compilation.

We have two different scenarios for this purpose.

1. FTP + TelNet. User specifies parameters of FTP and TelNet
connections. IDE copies files through FTP to server. IDE launches
compiler on the server using telnet and shows output log. IDE copies
binary files from server to client through FTP.

2. Compilation Server. Admin launches special program on the server-
Compilation Server. The IDE communicates with the Compilation Server.
The IDE passes sources to the Compilation Server. The server compiles
the sources and passes the output log to IDE. IDE shows the log.

What do you think about these scenarios?

Thanks
Sergey Grigorchuk
LemoSoft Company
http://www.lemosoft.com
```

#### ↳ Re: Remote Compilation

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2004-08-25T12:22:49-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B63Xc.22052$DG.1022593@news20.bellglobal.com>`
- **In-Reply-To:** `<a6be1ec.0408250752.6e2acc37@posting.google.com>`
- **References:** `<a6be1ec.0408250752.6e2acc37@posting.google.com>`

```
Sergey Grigorchuk wrote:
> Our company develops Lemo Cobol IDE and we are going to implement
> Remote Compilation. This feature allows to compile the sources on a
…[21 more quoted lines elided]…
> http://www.lemosoft.com

Sounds to me like you are inventing RJE batch.  That's the way I learnt 
Cobol in 1967, and it worked quite well.
;<)
Donald
```

##### ↳ ↳ Re: Remote Compilation

- **From:** docdwarf@panix.com
- **Date:** 2004-08-25T12:59:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgigic$4hq$1@panix5.panix.com>`
- **References:** `<a6be1ec.0408250752.6e2acc37@posting.google.com> <B63Xc.22052$DG.1022593@news20.bellglobal.com>`

```
In article <B63Xc.22052$DG.1022593@news20.bellglobal.com>,
Donald Tees  <donald_tees@sympatico.ca> wrote:
>Sergey Grigorchuk wrote:
>> Our company develops Lemo Cobol IDE and we are going to implement
>> Remote Compilation. This feature allows to compile the sources on a
>> remote server using network.

[snip]

>Sounds to me like you are inventing RJE batch.  That's the way I learnt 
>Cobol in 1967, and it worked quite well.

Everything old is new again, aye... but nowadays they have it easy, they 
get to use telephone or telnet connections instead of tin-cans and string.

DD
```

###### ↳ ↳ ↳ Re: Remote Compilation

- **From:** Pat Hall <phall@notsospam.certcoinc.com>
- **Date:** 2004-08-25T12:28:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10ipivlqfrec431@corp.supernews.com>`
- **In-Reply-To:** `<cgigic$4hq$1@panix5.panix.com>`
- **References:** `<a6be1ec.0408250752.6e2acc37@posting.google.com> <B63Xc.22052$DG.1022593@news20.bellglobal.com> <cgigic$4hq$1@panix5.panix.com>`

```
Tin cans and a string worked perfectly fine until you got a knot in your 
string.


PatH...always seemed to be the "knot unraveler"

docdwarf@panix.com wrote:
> In article <B63Xc.22052$DG.1022593@news20.bellglobal.com>,
> Donald Tees  <donald_tees@sympatico.ca> wrote:
…[19 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Remote Compilation

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-25T13:46:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgija0$9lq$1@panix5.panix.com>`
- **References:** `<a6be1ec.0408250752.6e2acc37@posting.google.com> <B63Xc.22052$DG.1022593@news20.bellglobal.com> <cgigic$4hq$1@panix5.panix.com> <10ipivlqfrec431@corp.supernews.com>`

```
In article <10ipivlqfrec431@corp.supernews.com>,
Pat Hall  <phall@notsospam.certcoinc.com> wrote:
>Tin cans and a string worked perfectly fine until you got a knot in your 
>string.

How many programmers does it take to change a light-bulb?

None... that's a hardware problem.

>
>
>PatH...always seemed to be the "knot unraveler"

Give my regards to Gordius, Alexander.

DD

>
>docdwarf@panix.com wrote:
…[22 more quoted lines elided]…
>
```

#### ↳ Re: Remote Compilation

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-25T15:07:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408251407.78f68a8@posting.google.com>`
- **References:** `<a6be1ec.0408250752.6e2acc37@posting.google.com>`

```
sng@lemosoft.com (Sergey Grigorchuk) wrote 

> Our company develops Lemo Cobol IDE and we are going to implement
> Remote Compilation. This feature allows to compile the sources on a
> remote server using network.
 
> 1. FTP + TelNet. User specifies parameters of FTP and TelNet
> connections. 

I would hope that you use ssh for these.
```

##### ↳ ↳ Re: Remote Compilation

- **From:** sng@lemosoft.com (Sergey Grigorchuk)
- **Date:** 2004-08-26T04:28:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a6be1ec.0408260328.6e561242@posting.google.com>`
- **References:** `<a6be1ec.0408250752.6e2acc37@posting.google.com> <217e491a.0408251407.78f68a8@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote in message 
> 
> I would hope that you use ssh for these.

We are going to use both SSH and TelNet.
```

###### ↳ ↳ ↳ Re: Remote Compilation

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-08-26T16:59:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgl4tn015oe@news2.newsguy.com>`
- **References:** `<a6be1ec.0408250752.6e2acc37@posting.google.com> <217e491a.0408251407.78f68a8@posting.google.com> <a6be1ec.0408260328.6e561242@posting.google.com>`

```

In article <a6be1ec.0408260328.6e561242@posting.google.com>, sng@lemosoft.com (Sergey Grigorchuk) writes:
> riplin@Azonic.co.nz (Richard) wrote in message 
> > 
> > I would hope that you use ssh for these.
> 
> We are going to use both SSH and TelNet.

SSH / SCP is a far better solution than anything involving FTP (which
is insecure and requires multiple connections, a complication for
firewalls) or Telnet (which is insecure and a rather complex
protocol).  You don't say whether you're planning on implementing the
protocols yourself or driving existing clients.  The former is a lot
of work for little benefit, and the latter is fraught with compatibility
and control issues.

If you have some valid reason for using anything other than SSH, then
the best alternative is probably HTTP (over SSL in any environment
where communications security is desired).  Transferring files with
one protocol and then manipulating them with another has historically
been a poor route.  A simple HTTP PUT of a file, or collection of
files (as a zip archive, say) to a CGI program that handles the
processing (compilation or whatever) and returns the results could be
implemented very simply using any of the major HTTP servers.  The
client can be implemented with a helper library such as libwww; if you
want SSL support (not a bad idea), there's OpenSSL.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
