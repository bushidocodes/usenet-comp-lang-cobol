[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# how to communicate with CICS directly nor through CICS Transaction Server for OS/390?

_3 messages · 3 participants · 2000-04_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### how to communicate with CICS directly nor through CICS Transaction Server for OS/390?

- **From:** "mainframe" <rushwoo@hengsys.com.cn>
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cus7h$voj$1@news.cz.js.cn>`

```
hi!
A question please !
our mainframe is S/390 running OS/390, CICS/ESA 4.1, and we have CICS
Transaction Gateway 3.0.3 for Windows NT and CICS Universal Client for
Windows NT, but we have no CICS Transaction Server for OS/390! We want to
communicate with CICS directly nor through CICS Transaction Server for
OS/390, what should I do ? If the CICS Transaction Server is required ?
Please answer me or mail to me, my E-mail address is rushwoo@hengsys.com.cn
Thanx !!!
```

#### ↳ Re: how to communicate with CICS directly nor through CICS Transaction Server for OS/390?

- **From:** amosgreg@my-deja.com
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cvefb$p80$1@nnrp1.deja.com>`
- **References:** `<8cus7h$voj$1@news.cz.js.cn>`

```
In article <8cus7h$voj$1@news.cz.js.cn>,
  "mainframe" <rushwoo@hengsys.com.cn> wrote:
> hi!
> A question please !
> our mainframe is S/390 running OS/390, CICS/ESA 4.1, and we have CICS
> Transaction Gateway 3.0.3 for Windows NT and CICS Universal Client for
> Windows NT, but we have no CICS Transaction Server for OS/390! We
want to
> communicate with CICS directly nor through CICS Transaction Server for
> OS/390, what should I do ? If the CICS Transaction Server is required
?
> Please answer me or mail to me, my E-mail address is
rushwoo@hengsys.com.cn
> Thanx !!!
>
I sent by e-mail the following response and am posting it here also.
 Greg

The following Links on the IBM web site might help.
At first I thought that 4.1 might not support the Gateway, the second
link is the specifications sheet on the Gateway and it lists ESA 4.1 as
supporting the Gateway.

You should be able to use your existing CICS server.

I am also posting this to Comp.Lang.COBOL for anyone else.

http://www-4.ibm.com/software/ts/cics/platforms/desktop/

http://www-4.ibm.com/software/ts/cics/library/brochures/gate.pdf
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: how to communicate with CICS directly nor through CICS Transaction Server for OS/390?

- **From:** WOB Consulting <wobconsult@sprynet.com>
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cvv65$ap2$1@nnrp1.deja.com>`
- **References:** `<8cus7h$voj$1@news.cz.js.cn>`

```
In article <8cus7h$voj$1@news.cz.js.cn>,
  "mainframe" <rushwoo@hengsys.com.cn> wrote:
> hi!
> A question please !
> our mainframe is S/390 running OS/390, CICS/ESA 4.1, and we have CICS
> Transaction Gateway 3.0.3 for Windows NT and CICS Universal Client for
> Windows NT, but we have no CICS Transaction Server for OS/390! We
want to
> communicate with CICS directly nor through CICS Transaction Server for
> OS/390, what should I do ? If the CICS Transaction Server is
required ?
> Please answer me or mail to me, my E-mail address is
rushwoo@hengsys.com.cn
> Thanx !!!
>

Does your NT platform support APPC (LU6.2) using Mapped Conversations?
It's a very robust and industrial strength connection methodology,
upward compatible to CICS/TS.

Cheers,

WOB


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
