[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Network problem with RM/Cobol 85

_4 messages · 3 participants · 2001-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Network problem with RM/Cobol 85

- **From:** "������������������������ ���������������������" <dksoft@otenet.gr>
- **Date:** 2001-04-25T13:46:35+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9c69q2$jd6$1@usenet.otenet.gr>`

```
I'm having a computer with Windows 2000 Server and runtime of  RM/Cobol85
for 10 users.
Also having 10 Pc's With Windows 95,Windows 98.
Routers connect Pc's to Server with dial-up Connection.When I'm running the
application i wrote in RM/Cobol85 from Pc's with mapping drive on server i'm
having slow speed of application.How can make my application to get more
speed???.
```

#### ↳ Re: Network problem with RM/Cobol 85

- **From:** "John Bradley" <k5mwe@austin.rr.com>
- **Date:** 2001-04-25T13:34:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LnAF6.199067$wx.28325338@typhoon.austin.rr.com>`
- **References:** `<9c69q2$jd6$1@usenet.otenet.gr>`

```
Hi,

Your problem is likely the round-trip delay in the dial-up connections, or
the data rate, or both.  When you map a drive in this way over a WAN, every
file operation must be sent to the server, and a reply returned.  One COBOL
file operation can result in dozens of low-level file operations that must
traverse the net.

There are a few things that you should look at if you haven't already.  (for
files that are on the server and used by the PC's)  Be sure that you are
opening the files in the most restrictive mode possible for your
application.  In other words, if you can open a file for exclusive use, do
that.  If you only input from a file, open it for input.  Only when
necessary open the file input/output for shared use.  There are also runtime
configuration parameters that affect WAN performance (sometimes
dramatically).

In spite of this, you will probably find that your network configuration is
inherently slow.  You can try using the RM/InfoExpress server product on the
Windows 2000 server.  This will reduce the network traffic to exactly one
round-trip per COBOL file operation.  For write-intensive apps this usually
results in dramatic improvements.  For read-intensive apps, it has less
effect, and might even slow things down.

For much more detail, especially for the configuration issues, check the
RM/COBOL Users' Guide and contact Liant support wherever you are. (probably
the distributor in your country, or the London office, based on your email
address).  To find out who to contact, go to www.liant.com.

Good luck,

John

"�������� �������" <dksoft@otenet.gr> wrote in message
news:9c69q2$jd6$1@usenet.otenet.gr...
> I'm having a computer with Windows 2000 Server and runtime of  RM/Cobol85
> for 10 users.
> Also having 10 Pc's With Windows 95,Windows 98.
> Routers connect Pc's to Server with dial-up Connection.When I'm running
the
> application i wrote in RM/Cobol85 from Pc's with mapping drive on server
i'm
> having slow speed of application.How can make my application to get more
> speed???.
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Network problem with RM/Cobol 85

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-04-29T01:56:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3aeb749c.172395392@news1.attglobal.net>`
- **References:** `<9c69q2$jd6$1@usenet.otenet.gr> <LnAF6.199067$wx.28325338@typhoon.austin.rr.com>`

```
Another option that will make the applications nearly as fast as local
ones (likely just as fast) is to use the Flexus Thin Client with COBOL
sp2.  http://www.flexus.com.  This allows you to run the interface
only on the client machine, while the application runs on the server.
It works with RM COBOL too!


On Wed, 25 Apr 2001 13:34:35 GMT, "John Bradley" <k5mwe@austin.rr.com>
wrote:

>Hi,
>
…[47 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Network problem with RM/Cobol 85

- **From:** "John Bradley" <k5mwe@austin.rr.com>
- **Date:** 2001-04-29T04:37:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EUMG6.179614$8y.34028811@typhoon.austin.rr.com>`
- **References:** `<9c69q2$jd6$1@usenet.otenet.gr> <LnAF6.199067$wx.28325338@typhoon.austin.rr.com> <3aeb749c.172395392@news1.attglobal.net>`

```
I agree, this is another good approach to this kind of problem.  I should
have thought of this as well.  Thanks Thane.

John

"Thane Hubbell" <thaneH@softwaresimple.com> wrote in message
news:3aeb749c.172395392@news1.attglobal.net...
> Another option that will make the applications nearly as fast as local
> ones (likely just as fast) is to use the Flexus Thin Client with COBOL
…[10 more quoted lines elided]…
> >Your problem is likely the round-trip delay in the dial-up connections,
or
> >the data rate, or both.  When you map a drive in this way over a WAN,
every
> >file operation must be sent to the server, and a reply returned.  One
COBOL
> >file operation can result in dozens of low-level file operations that
must
> >traverse the net.
> >
> >There are a few things that you should look at if you haven't already.
(for
> >files that are on the server and used by the PC's)  Be sure that you are
> >opening the files in the most restrictive mode possible for your
> >application.  In other words, if you can open a file for exclusive use,
do
> >that.  If you only input from a file, open it for input.  Only when
> >necessary open the file input/output for shared use.  There are also
runtime
> >configuration parameters that affect WAN performance (sometimes
> >dramatically).
> >
> >In spite of this, you will probably find that your network configuration
is
> >inherently slow.  You can try using the RM/InfoExpress server product on
the
> >Windows 2000 server.  This will reduce the network traffic to exactly one
> >round-trip per COBOL file operation.  For write-intensive apps this
usually
> >results in dramatic improvements.  For read-intensive apps, it has less
> >effect, and might even slow things down.
> >
> >For much more detail, especially for the configuration issues, check the
> >RM/COBOL Users' Guide and contact Liant support wherever you are.
(probably
> >the distributor in your country, or the London office, based on your
email
> >address).  To find out who to contact, go to www.liant.com.
> >
…[6 more quoted lines elided]…
> >> I'm having a computer with Windows 2000 Server and runtime of
RM/Cobol85
> >> for 10 users.
> >> Also having 10 Pc's With Windows 95,Windows 98.
> >> Routers connect Pc's to Server with dial-up Connection.When I'm running
> >the
> >> application i wrote in RM/Cobol85 from Pc's with mapping drive on
server
> >i'm
> >> having slow speed of application.How can make my application to get
more
> >> speed???.
> >>
…[5 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
