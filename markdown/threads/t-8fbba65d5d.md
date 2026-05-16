[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CICS EPI?

_3 messages · 3 participants · 1998-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### CICS EPI?

- **From:** "rmch" <rmch@cadvision.com>
- **Date:** 1998-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36083265.0@news.cadvision.com>`

```
Someone in this newsgroup mentioned CICS EPI...

Can anyone elaborate on what this is ?  (I am familiar with CICS
programming).

Thanks.
```

#### ↳ Re: CICS EPI?

- **From:** paulr@bix.com (paulr)
- **Date:** 1998-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6u9knp$j1b@lotho.delphi.com>`
- **References:** `<36083265.0@news.cadvision.com>`

```

EPI is the External Presentation Interface.  It allows
CICS 3270 applications to be invoked by a non 3270
application, as in workstation GUI programes. :) 

It provides a suite of calls that allow a client 
application to pass 3270 data streams to and from
a CICS application. 

There are a couple of examples programs distributed 
with CICS these days to demonstrate EPI.

Yours,
-Paul



rmch (rmch@cadvision.com) wrote:
: Someone in this newsgroup mentioned CICS EPI...

: Can anyone elaborate on what this is ?  (I am familiar with CICS
: programming).

: Thanks.
```

#### ↳ Re: CICS EPI?

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1998-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3608ef23.4527403@news2.ibm.net>`
- **References:** `<36083265.0@news.cadvision.com>`

```
On Tue, 22 Sep 1998 17:25:26 -0600, "rmch" <rmch@cadvision.com> wrote:

>Someone in this newsgroup mentioned CICS EPI...
>
…[6 more quoted lines elided]…
>


EPI, as in External Presentation Interface.  Allows the native GUI type application to
emulate a 3270 terminal to CICS.  In Mainframe, this is called FEPI.  Not really a
client0server approach, but more of a screen scraper


HTH
with kind regards

Volker Bandke
(BSP GmbH)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
