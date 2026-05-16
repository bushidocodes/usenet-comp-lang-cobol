[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# "older" IBM COBOL and DB2

_6 messages · 4 participants · 2003-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases)

---

### "older" IBM COBOL and DB2

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-12-12T18:33:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0SnCb.363$0s2.156@newsread2.news.pas.earthlink.net>`

```
I know there have been previous discussions about when (what future release) of
CICS will *drop* support for even running OS/VS COBOL programs, but I don't know
if anyone else (besides me) *missed* the fact that DB V8 does *not* support
either

    OS/VS COBOL
        or
     VS COBOL II

According to:

    http://www.ibm.com/isource/cgi-bin/goto?it=usa_annred&on=203-019

The *only* COBOL compilers supported with this release of DB2 are:

COBOL: Any of the following:
    ENTERPRISE COBOL V3.2 (5655-G53)
    IBM COBOL for OS/390 and VM V2.2 (5648-A25), optionally, with VisualAge�
COBOL Enterprise V2.2 (04L6579)

Similarly for PL/I

PL/I: Any of the following:
    IBM Enterprise PL/I for z/OS and OS/390 V3 (5655-H31)
    VisualAge PL/I for OS/390 V2.2 (5655-B22)

        ***

Everyone else may have noticed this last January when this announcement was
made, but it was just brought to my attention recently - and I thought I would
"highlight" it for sites that are still on "down-level" (no longer supported by
IBM) compilers.
```

#### ↳ Re: "older" IBM COBOL and DB2

- **From:** "Ron" <NoSpam@NoMoSpam.ORG>
- **Date:** 2003-12-12T16:39:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41udndcmPIcC3keiXTWQkQ@giganews.com>`
- **References:** `<0SnCb.363$0s2.156@newsread2.news.pas.earthlink.net>`

```
Good!
```

#### ↳ Re: "older" IBM COBOL and DB2

- **From:** Colin Campbell <cmcampb@adelphia.net_remove_this>
- **Date:** 2003-12-17T09:10:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<E60Eb.406$b77.416@dfw-service2.ext.raytheon.com>`
- **In-Reply-To:** `<0SnCb.363$0s2.156@newsread2.news.pas.earthlink.net>`
- **References:** `<0SnCb.363$0s2.156@newsread2.news.pas.earthlink.net>`

```
Bill,
Do you know where I can find the announcements for DB2 V6 and DB2 V7?

We are on DB2 V5, and will upgrade to V6 in February (just crawling back 
onto a supported level).  I sounded the alarm about getting off the "old 
COBOL" yesterday, but I thought I'd better check the interim releases to 
see what they say about supported COBOL levels.

William M. Klein wrote:
> I know there have been previous discussions about when (what future release) of
> CICS will *drop* support for even running OS/VS COBOL programs, but I don't know
…[30 more quoted lines elided]…
>
```

##### ↳ ↳ Re: "older" IBM COBOL and DB2

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-12-17T18:40:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nq1Eb.474802$0v4.21339699@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<0SnCb.363$0s2.156@newsread2.news.pas.earthlink.net> <E60Eb.406$b77.416@dfw-service2.ext.raytheon.com>`

```

Colin Campbell <cmcampb@adelphia.net_remove_this> wrote in message news:E60Eb.406$b77.416@dfw-service2.ext.raytheon.com...
> Bill,
> Do you know where I can find the announcements for DB2 V6 and DB2 V7?

DB2 V6

http://www-306.ibm.com/common/ssi/fcgi-bin/ssialias?infotype=an&subtype=ca&supplier=897&appname=IBMLinkRedirect&letternum=ENUS299-15
4

TinyURL link

http://tinyurl.com/zoah

DB2 V7

http://www-306.ibm.com/fcgi-bin/common/ssi/ssialias?infotype=an&subtype=ca&appname=Demonstration&htmlfid=897/ENUS201-054

TinyURL link

http://tinyurl.com/zobk
>
> We are on DB2 V5, and will upgrade to V6 in February (just crawling back
…[38 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "older" IBM COBOL and DB2

- **From:** Colin Campbell <cmcampb@adelphia.net_remove_this>
- **Date:** 2003-12-17T11:04:39-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bN1Eb.408$b77.389@dfw-service2.ext.raytheon.com>`
- **In-Reply-To:** `<nq1Eb.474802$0v4.21339699@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<0SnCb.363$0s2.156@newsread2.news.pas.earthlink.net> <E60Eb.406$b77.416@dfw-service2.ext.raytheon.com> <nq1Eb.474802$0v4.21339699@bgtnsc04-news.ops.worldnet.att.net>`

```
Hugh,
Thanks for the links.  The DB2 V6 IBM link is no longer any good.  I 
opened the TinyURL link, and it appears to have only part of the 
document.  However, it has the link to the PDF version, and I was able 
to download that version.

Even DB2 V6 does not support the execution of OS/VS COBOL, or VS COBOL 
II older than V1R4.  (DB2 V7 has the same restrictions.)

DB2 V5 explicitly allows use of OS/VS COBOL, but recommends use of VS 
COBOL II or higher.

Looks like we're about to take a walk on the unsupported side!
=====

Hugh Candlin wrote:
> Colin Campbell <cmcampb@adelphia.net_remove_this> wrote in message news:E60Eb.406$b77.416@dfw-service2.ext.raytheon.com...
> 
…[63 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "older" IBM COBOL and DB2

_(reply depth: 4)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-12-17T22:33:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iR4Eb.475888$0v4.21357368@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<0SnCb.363$0s2.156@newsread2.news.pas.earthlink.net> <E60Eb.406$b77.416@dfw-service2.ext.raytheon.com> <nq1Eb.474802$0v4.21339699@bgtnsc04-news.ops.worldnet.att.net> <bN1Eb.408$b77.389@dfw-service2.ext.raytheon.com>`

```

Colin Campbell <cmcampb@adelphia.net_remove_this> wrote in message news:bN1Eb.408$b77.389@dfw-service2.ext.raytheon.com...
> Hugh,
> Thanks for the links.  The DB2 V6 IBM link is no longer any good.

It is good.  It wrapped AND broke - you pobably missed the 4
when you clicked on it.  I expected that to happen, which is why
I also provided the alternate links.

> I opened the TinyURL link, and it appears to have only part of the
> document.  However, it has the link to the PDF version, and I was able
> to download that version.

I noticed that also.
>
> Even DB2 V6 does not support the execution of OS/VS COBOL, or VS COBOL
…[5 more quoted lines elided]…
> Looks like we're about to take a walk on the unsupported side!

Support is a very costly, logitical nightmare.  As the permutations increase,
the probability of running successful regression tests approaches zero.

Obsolescence is inevitable these days, it seems, to keep product support
in the realm of manageability.

> =====
>
…[9 more quoted lines elided]…
> >
http://www-306.ibm.com/common/ssi/fcgi-bin/ssialias?infotype=an&subtype=ca&supplier=897&appname=IBMLinkRedirect&letternum=ENUS299-15
> > 4
> >
…[55 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
