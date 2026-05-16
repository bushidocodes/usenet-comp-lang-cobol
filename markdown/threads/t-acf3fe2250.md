[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress, CGI and Virtual Directories

_2 messages · 2 participants · 2000-02_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### NetExpress, CGI and Virtual Directories

- **From:** mrtonyr@my-deja.com
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87cpun$smq$1@nnrp1.deja.com>`

```
I am developing a cgi program with net express that needs to write a
file to a directory on another computer. I have gotten it to work with
a mapped drive and using the mapped drive in the assign to clause. My
problem comes when using a virtual directory through the web server. I
can write to the directories that are physically on the computer, but
not to a virtual directory that I have defined. I have checked the
permissions and connect using a valid username. Has anyone done this?
Or am I overlooking something obvious?

Thanks, Tony


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: NetExpress, CGI and Virtual Directories

- **From:** "Neil Hayes" <NeilH@syspro.co.za>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<389a6096$0$35285@helios.is.co.za>`
- **References:** `<87cpun$smq$1@nnrp1.deja.com>`

```
Hi,

I've sent Tony a document regarding the use of cgi programs using I-O, this
is something that I had a problem with sometime ago and discovered that it
was all based around security and the setting up of security.  When users
use the internet they basically come in anonymously and have authorization
to use data on the internet server, when you start wanting to gain access to
other servers you end up with a problem that IIS does not want to pass the
credentials of the user to the other machine.

I hope Tony manages to sort out the problem and perhaps post a small summary
of how it was resolved.

Regards

Neil
NeilH@syspro.co.za
http://www.sysprogroup.com


<mrtonyr@my-deja.com> wrote in message news:87cpun$smq$1@nnrp1.deja.com...
> I am developing a cgi program with net express that needs to write a
> file to a directory on another computer. I have gotten it to work with
…[11 more quoted lines elided]…
> Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
