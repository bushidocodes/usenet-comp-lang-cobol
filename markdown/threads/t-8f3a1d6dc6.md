[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol slowness

_6 messages · 4 participants · 1999-10_

---

### Cobol slowness

- **From:** "Sauro Nencioni" <s.nencioni@NIENTESPAMui.prato.it>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v9r9q$huc$1@serv1.iunet.it>`

```
Can anyone tell us something about new MERANT/MICROFOCUS
NetExpress Cobol (versus old versions and other brand
compilers)?
We're especially interested on Micro Focus indexed file
access performance (with about 10 users simultaneously
sharing and updating the file).
Consultant names accepted.
Please save us!

---

This is our situation (and our obsession):

5 years old Pentium-based server (90Mhz-32Mb RAM)
Novell 3.12 (IPX/SPX)
20 win95 users
MICROFOCUS Object-Cobol 3.4.23 (16 bit)
Performance: 100

New server: Xeon-400Mhz 512Mb RAM RAID5 etc. etc.
NT 4 (SP5) with only TCP/IP enabled
always 20 win95 users
MERANT/MICROFOCUS NetExpress 3.0.14 (32 bit)
(sources only re-compilated, no changes)
Performance: about 30
(performance accessing file in a multi-user environment...
when I work at night, lonely... (sic!) I can get a 300 speed
level, against our old server)

Network is always the same (a 100 Mbit Ethernet UTP network).

Obviously our old server and Object-Cobol are not 2000 compliant.
We could patch our old (and sweet...) Novell 3.12, but
(unfortunatly) we must use NetExpress... and MERANT support service
gives us absurd answers (like ... "send all to us ... sources, GNTs,
data, server, network, ... office, people" ... and other!)

Sauro Nencioni.
_______________________________________________
CEDI SERIN srl
Prato/Italy
eMail: s.nencioni@ui.prato.it
Home Page: http://www.ui.prato.it/
```

#### ↳ Re: Cobol slowness

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NowYOGmZVscYaLH9UUAShhZO7GaP@4ax.com>`
- **References:** `<7v9r9q$huc$1@serv1.iunet.it>`

```
>This is our situation (and our obsession):
>
…[7 more quoted lines elided]…
>NT 4 (SP5) with only TCP/IP enabled
Remove the NT and install NOVELL (latest version is Y2K..)

If you insist in keeping NT I would sugest that you do a search
in www.microsoft.com and see the patchs available for WinNT and
Win95 relating to network performance and problems.
One of the things that NT is famous for is that if you need
performance you are going to lose in data integrity. Choose one.
>always 20 win95 users
>MERANT/MICROFOCUS NetExpress 3.0.14 (32 bit)
…[7 more quoted lines elided]…
>


FF
```

##### ↳ ↳ Re: Cobol slowness

- **From:** "Sauro Nencioni" <s.nencioni@NIENTESPAMui.prato.it>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vbiln$fi2$1@serv1.iunet.it>`
- **References:** `<7v9r9q$huc$1@serv1.iunet.it> <NowYOGmZVscYaLH9UUAShhZO7GaP@4ax.com>`

```
> Remove the NT and install NOVELL (latest version is Y2K..)


We're trying to setup a new server with our old Novell 3.12
(patched for Y2K).
Thanks for paying attention on our problem.
I'll send you news about it.

Sauro Nencioni.
______________________________________________
CEDI SERIN srl
Prato/Italy
eMail: s.nencioni@ui.prato.it
Home Page: http://www.ui.prato.it/
```

#### ↳ Re: Cobol slowness

- **From:** david.sands@tesco.net (David Sands)
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3818a6ef.1099156@news.tesco.net>`
- **References:** `<7v9r9q$huc$1@serv1.iunet.it>`

```

One thing you could consider is to use the Fileshare componant of Net
Express.

Basically this ships a file request to the server for processing which
reduces the amount of network accesses when a record is accessed.

In theory it should improve your performance situation if you are
running with 10 users.

Alternatively have you considered NT on the client machines as well as
the server. NT should run 32 bit apps faster than 95. I would do some
timings with NT on the client side to see if that makes a difference.

Regards
David.


On Thu, 28 Oct 1999 17:48:11 +0200, "Sauro Nencioni"
<s.nencioni@NIENTESPAMui.prato.it> wrote:

>Can anyone tell us something about new MERANT/MICROFOCUS
>NetExpress Cobol (versus old versions and other brand
…[43 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Cobol slowness

- **From:** "Sauro Nencioni" <s.nencioni@NIENTESPAMui.prato.it>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vbj00$gmh$1@serv1.iunet.it>`
- **References:** `<7v9r9q$huc$1@serv1.iunet.it> <3818a6ef.1099156@news.tesco.net>`

```
> One thing you could consider is to use the Fileshare componant
> of Net Express.


We're trying to setup a new server with our old Novell 3.12
(patched for Y2K).

We'll think about using FileShare... but one of our
commercial partners it's using it on Unix.
Performance are good, but server crash one-time-per-day.

So... before buying NetExpress we had an evaluation copy...
(30 days)... can we find a FileShare/NT evaluation copy?

Thanks for paying attention on our problem.
I'll send you news about it.

Sauro Nencioni.
______________________________________________
CEDI SERIN srl
Prato/Italy
eMail: s.nencioni@ui.prato.it
Home Page: http://www.ui.prato.it/
```

###### ↳ ↳ ↳ Re: Cobol slowness

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vcbec$mvg$1@news.inet.tele.dk>`
- **References:** `<7v9r9q$huc$1@serv1.iunet.it> <3818a6ef.1099156@news.tesco.net> <7vbj00$gmh$1@serv1.iunet.it>`

```
Fileshare NLM is the product you need if you run Novel. Check the price and
check that the product still exist.

Regards
Ib Tanding

Sauro Nencioni skrev i meddelelsen <7vbj00$gmh$1@serv1.iunet.it>...
>> One thing you could consider is to use the Fileshare componant
>> of Net Express.
…[23 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
