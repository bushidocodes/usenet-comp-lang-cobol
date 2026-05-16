[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to stop UDP port 86 BroadCast

_2 messages · 2 participants · 2005-05_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to stop UDP port 86 BroadCast

- **From:** "MalhiNet" <m_nets2003@yahoo.com>
- **Date:** 2005-05-30T02:50:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1117446630.226392.212680@g43g2000cwa.googlegroups.com>`

```
Hi,

Is it possible multipal CCITCP server can talk to each other without
using UDP port 86 broadcast.

We have a large system which is running on CCITCP on every server on
WAN. when server-A want to connect to  server-B It sends the UDP port
86 broadcast on all WAN then server-B replay it.

UDP port 86 broadcast is creating problem for netwrok.

If any one know why it is doing UDP Broadcast and how can i remove it.

Thx.
```

#### ↳ Re: How to stop UDP port 86 BroadCast

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2005-05-31T18:01:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d7i8p00m97@news1.newsguy.com>`
- **References:** `<1117446630.226392.212680@g43g2000cwa.googlegroups.com>`

```

In article <1117446630.226392.212680@g43g2000cwa.googlegroups.com>, "MalhiNet" <m_nets2003@yahoo.com> writes:
> 
> Is it possible multipal CCITCP server can talk to each other without
> using UDP port 86 broadcast.

This isn't a COBOL question, so it's not topical for comp.lang.cobol.
I recommend raising it as an issue through your Micro Focus support
representative.

> We have a large system which is running on CCITCP on every server on
> WAN. when server-A want to connect to  server-B It sends the UDP port
> 86 broadcast on all WAN then server-B replay it.
>
> UDP port 86 broadcast is creating problem for netwrok.

IP broadcasts shouldn't traverse a WAN at all, regardless of what
process generates them.  If they are, then you have a suboptimal
network which is bridging LAN segments.  Personally, I'd recommend
you correct that, if at all possible; broadcasts should not be
carried over WAN links.

Also, you don't need more than one ccitcp2 process per LAN segment
(though there are some possible reasons for running more).  If you
have a ccitcp2 running on every server system, and there's more than
one server system per LAN segment, then you have too many ccitcp2s.

> If any one know why it is doing UDP Broadcast and how can i remove it.

Programs using CCITCP use UDP broadcasts to locate ccitcp2 if they
haven't been configured with the location of the ccitcp2 daemon.  The
easiest way to do that is to set the CCITCP2 environment variable,
per MF documentation.  Have you done that?

ccitcp2 itself will use a UDP broadcast to relay a query for a server
that is not registered with it.

If your CCITCP-based programs have their ccitcp2 locations configured
manually (eg using the CCITCP2 environment variable), and they only
request servers which are known to the ccitcp2 they're configured to
use, that should eliminate most of the UDP broadcasts.

Alternatively, use CCI Direct Connect rather than ccitcp2 name
resolution.  See the documentation for your MF COBOL product for
details.

For further information, please raise an MF support request or take
this question to the Micro Focus Forum (formerly Answer Exchange) on
the Micro Focus Supportline web site.[1]


1. http://supportline.microfocus.com/about/forum.asp
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
