[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# GUI migration

_6 messages · 4 participants · 2001-11_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### GUI migration

- **From:** "Wolf Grossi" <X-news@magro-soft.com>
- **Date:** 2001-11-19T09:08:35+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1006153314.167349@hagakure.utanet.at>`

```
Hi folks,

    maintaining a large cobol application with over 600 dialog progs using a
special character based screen-handler.
Then progs are runnung on unix/linux using MF-cobol and 130 nt-workstations,
which will be repaced by linux in the next future.

What are the possibilities to replace this screen-handler with a
gui-interface?

I've heard about MF NetExpress and about flexus.

Thanks for reading and your opinion,
Wolf
```

#### ↳ Re: GUI migration

- **From:** Paul Barnett <paul.barnett@microfocus.nospam.com>
- **Date:** 2001-11-19T10:40:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BF8E1B1.8197748@microfocus.nospam.com>`
- **References:** `<1006153314.167349@hagakure.utanet.at>`

```
Wolf Grossi wrote:

> Hi folks,
>
…[11 more quoted lines elided]…
> Wolf

NetExpress has a GUI version of Dialog which works in Windows 95, 98, ME 2000
and XP. The version of Micro Focus COBOL on Linux is Object COBOL Developer
Suite and this has only character based tools. You could use it to develop a
client/server application, using Gui Dialog on a Windows PC and the server side
code being on Linux or Unix.

Have you condsidered developing a browser based interface? This can be
developed in NetExpress and deployed on Unix/Linux. No browser plug-ins are
required to use this unlike other products I could mention.
```

##### ↳ ↳ Re: GUI migration

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-11-19T22:18:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9zfK7.30793$xS6.51247@www.newsranger.com>`
- **References:** `<1006153314.167349@hagakure.utanet.at> <3BF8E1B1.8197748@microfocus.nospam.com>`

```
Thanks for the reminder Paul - Flexus also has Web Client - use the same (with a
few restrictions based on what the browser can do) sp2 panels and COBOL source
code and have a browser based interface.  Even having developed several
applications this way, I prefer the Thin Client.


In article <3BF8E1B1.8197748@microfocus.nospam.com>, Paul Barnett says...
>
>Wolf Grossi wrote:
…[25 more quoted lines elided]…
>
```

#### ↳ Re: GUI migration

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-11-19T16:10:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<w9aK7.30313$xS6.48390@www.newsranger.com>`
- **References:** `<1006153314.167349@hagakure.utanet.at>`

```
Since you have a custom screen handler, Sp2 from Flexus is probably your best
bet.  Conversions from custom screen handlers - where you own the code and are
familiar with it - seem to be much easier.  Sometimes you can replace portions
of your handler with calls to sp2 and get there.  Without knowing the handler, I
can't say for sure.

Interestingly, with sp2 you can keep your system running on a Linux server, but
give your users a Windows based GUI by using the Flexus Thin client product.
This product has been around for several years and is quite robust.
Additionally, it allows you to use any COBOL compiler you desire.

PS - I do tech support for Flexus on this product.



In article <1006153314.167349@hagakure.utanet.at>, Wolf Grossi says...
>
>Hi folks,
…[14 more quoted lines elided]…
>
```

#### ↳ Re: GUI migration

- **From:** g.friedrich@fiuka.de (Friedrich)
- **Date:** 2001-11-19T23:26:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcfdd616.0111192326.12d1071e@posting.google.com>`
- **References:** `<1006153314.167349@hagakure.utanet.at>`

```
"Wolf Grossi" <X-news@magro-soft.com> wrote in message news:<1006153314.167349@hagakure.utanet.at>...
> Hi folks,
> 
…[11 more quoted lines elided]…
> Wolf

Did you try PERCobol from legacyJ (www.legacyj.com)
It is a COBOL-Compiler running on all platforms with Java
(e.g.Linux, Windows).
```

#### ↳ Re: GUI migration - thanks

- **From:** "Wolf Grossi" <X-news@magro-soft.com>
- **Date:** 2001-11-20T09:04:38+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1006239463.173827@hagakure.utanet.at>`
- **References:** `<1006153314.167349@hagakure.utanet.at>`

```
Thank you all for your informnative input.

I guess I'll be busy for a while evaluating the various suggestions.

Wolf
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
