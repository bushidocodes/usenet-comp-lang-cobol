[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Fileshare and CCITCP2

_3 messages · 2 participants · 2002-06 → 2002-07_

---

### MF Fileshare and CCITCP2

- **From:** graham@olympic.co.uk (graham)
- **Date:** 2002-06-20T18:29:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a02b0a1.0206201729.70a01baf@posting.google.com>`

```
We've been testing the use of Fileshare on some of our customers sites
for a few weeks and have had no real problems so far, until now that
is!
It's on WINDOWS 95 (but then other W95 sites have worked). We've setup
via CCIINST first. We run CCITCP2 on the server, run FS on the server.
On the server the application works fine (with FHREDIR.CFG and
FS.CFG). On the workstation we've run CCIINST and then we run CCITCP2,
load our COBOL application and it fails with 9/125 (after several
seconds)

Swtich on CCITCP2 -d trace and it shows the machines do communicate
and without knowing the detail it looks sensible...there is are
BROADCAST_SEARCH AND BROADCAST_REPLYs, EXISTENCE and SERVICE request
from the workstation but there could be oddities - is there a
description of what should happen ? (at the moment I haven't got
access to a completely working environment) but also is there a way of
writing the trace to a file, at the moment I'm just saving and
printing from the screen ?

The only known difference in this setup is that the machine are not
set up with defined IP address they are allocated dynamically; however
the messages in the trace suggest that they are, at least, different
address if not really standard (10.0.0.7, e.g.). Frankly on the other
few sites we've tried it's worked (more or less) first time!!

Any suggestions gratefully receieved...

graham
```

#### ↳ Re: MF Fileshare and CCITCP2

- **From:** "Panos Zotos" <pzotos@syntax.gr>
- **Date:** 2002-06-21T17:16:04+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aevcft$5l8$1@usenet.otenet.gr>`
- **References:** `<8a02b0a1.0206201729.70a01baf@posting.google.com>`

```
Some thinks you can search:

- Why are you running ccitcp2 on the client machine? It should be sufficient
to run it on the server only
- Client needs to have a ccitcp2 environment variable defined, that contains
the IP or DNS of the server where ccitcp2 deamon runs. This is set by
CCIINST utility, but can you check autoexec.bat that it is there indeed?
Otherwise you can simply define it in autoexec as : set ccitcp2=IP or DNS of
server
- If you are using DHCP, then make sure that the ccitcp2 env.var (both in
the server and the client) only contains DNS names and not IPs

- If you need to search deeper, you might want to look at the winsock
version you are using. Some older versions do not work correctly. I'm not
sure if you can find winsock updates for Windows 95 any more. After all,
Windows 95 itself is not an enviroment that is now supported by Microsoft,
so it would worth moving to 98 or newer.

Ho these will help



"graham" <graham@olympic.co.uk> wrote in message
news:8a02b0a1.0206201729.70a01baf@posting.google.com...
> We've been testing the use of Fileshare on some of our customers sites
> for a few weeks and have had no real problems so far, until now that
…[25 more quoted lines elided]…
> graham
```

##### ↳ ↳ Re: MF Fileshare and CCITCP2

- **From:** graham@olympic.co.uk (graham)
- **Date:** 2002-07-03T12:09:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a02b0a1.0207031109.70a73022@posting.google.com>`
- **References:** `<8a02b0a1.0206201729.70a01baf@posting.google.com> <aevcft$5l8$1@usenet.otenet.gr>`

```
Thanks for your assistance...we've been able to resolve the problem
now.

In fact it appears that CCITCP2 environment variable may not have been
set properly but the real problem was that the "server" was named with
a space in the name. Let's say it was called "abc xyz", while it does
seem that some communication happens it isn't successful and the
client eventually times out. By changing this to "abc-xyz" everyhing
works fine!

I had not really noticed this before (although I did see it, of
course). I thought that even though the IP addresses were dynamic
CCITCP2 should have made it work with whatever IP addresses were set
but I now wonder whether some part of the messages uses the name
itself; in this particular case the space is, I suppose, treated as a
terminator and thus the named is processed incorrectly.

Where we've tested exactly the same set up and installation elsewhere,
where the IP addresses were static, the problem never arose. I suspect
that I will have to check whether these have spaces in the machine
names simply to satisfy my inquisitiveness, now; of course one may
suspect that they all have well-formed names!

graham


"Panos Zotos" <pzotos@syntax.gr> wrote in message news:<aevcft$5l8$1@usenet.otenet.gr>...
> Some thinks you can search:
> 
…[16 more quoted lines elided]…
> Ho these will help
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
