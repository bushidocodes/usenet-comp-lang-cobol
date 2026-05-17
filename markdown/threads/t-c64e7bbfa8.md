[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ACUcobol : problems with NT

_2 messages · 2 participants · 1998-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### ACUcobol : problems with NT

- **From:** "rob.dewinter" <ua-author-17075279@usenetarchives.gap>
- **Date:** 1998-03-19T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<351225bc.2164077@news.skynet.be>`

```

Our company tried to install ACUCOBOL applications 4 times now on NT
server with WIN95 workstations - without success. Programs tend to
hang up after working fine for a few hours.
These same applications run fine in a UNIX environment.

Does anybody have experience with ACUCOBOL and NT SERVER? Please
contact me so we can exchange ideas of implementing a working
application.

Thanks
Rob De Winter - Belgium
rob··r@adv··e.nospam
(drop the .nospam text from my e-mail address)
```

#### ↳ Re: ACUcobol : problems with NT

- **From:** "daniel maltes" <ua-author-1025739@usenetarchives.gap>
- **Date:** 1998-03-19T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c64e7bbfa8-p2@usenetarchives.gap>`
- **In-Reply-To:** `<351225bc.2164077@news.skynet.be>`
- **References:** `<351225bc.2164077@news.skynet.be>`

```

Rob,
I'm aware of a couple of possible solutions to what you've described:
1. Try installing the runtimes on the local hard drives and changing
your application shortcut to launch the runtime locally(your target folder
and data files can still reside on the server).
2. If your network protocol is setup as tcp/ip then you can purchase
AcuServer from Acucorp(Acucobol) to alleviate vision indexed file locks and
corruptions. Apparently, Acucorp has identified a bug in NT's NETBEUI and
they can work around it with AcuServer by using RPC to send and receive
vision i/o requests across the network. It requires client(winsock) enabled
runtimes. You'll have to speak to Acucorp for the details and pricing.
Sales 1-800-262-6585, Support 1-800-399-7220, web http://www.acucorp.com

Good luck,
Dan Maltes

Rob De Winter wrote in message <351··.@new··t.be>...
› Our company tried to install ACUCOBOL applications 4 times now on NT
› server with WIN95 workstations - without success. Programs tend to
…[10 more quoted lines elided]…
› (drop the .nospam text from my e-mail address)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
