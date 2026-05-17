[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL / CICS as web data source

_8 messages · 7 participants · 1996-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Web, XML, modern integration`](../topics.md#web)

---

### COBOL / CICS as web data source

- **From:** "thakker..." <ua-author-7089904@usenetarchives.gap>
- **Date:** 1996-10-13T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<53u62g$86l@tribune.mayo.edu>`

```

I and a collegue are working to determine the functionalities of a particular
web server, Shadow Web Server. This is an MVS-based web server which can
incorporate an html form along with data coming from a CICS application. This
application can be a COBOL program executing in a CICS environment. I'd
like to get any feedback on this. This server is developed by Neon Systems.
Or I'd appreciate any information about software which permit connectivity to
WWW world from MVS/CICS world.

Thank you in advance,

-Bakulesh Thakker
```

#### ↳ Re: COBOL / CICS as web data source

- **From:** "pah..." <ua-author-13876471@usenetarchives.gap>
- **Date:** 1996-10-14T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-09d99b7aef-p2@usenetarchives.gap>`
- **In-Reply-To:** `<53u62g$86l@tribune.mayo.edu>`
- **References:** `<53u62g$86l@tribune.mayo.edu>`

```

Bakulesh Thakker (tha··.@ma··o.edu) wrote:
...
: Or I'd appreciate any information about software which permit
: connectivity to WWW world from MVS/CICS world.

This is almost off-topic for comp.lang.cobol, but...

It is (IMHO) quite simple. Write your CICS transactions using
the SNA LU 6.2 APPC protocol (standard RECEIVE and SEND verbs),
and write an interface using CGI on an NT with SNA Server. The
CICS transaction sends messages to the program on the NT, which
outputs them in the normal CGI manner. Your web server would
run on the NT.

You can either generate HTML in the CICS transaction, or send
out something simpler which you then wrap into HTML in the CGI
program on the NT.

If you can get SNA software for a UNIX box you don't even need
to use a Microsoft product.
```

##### ↳ ↳ Re: COBOL / CICS as web data source

- **From:** "intern..." <ua-author-1848015@usenetarchives.gap>
- **Date:** 1996-10-14T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-09d99b7aef-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-09d99b7aef-p2@usenetarchives.gap>`
- **References:** `<53u62g$86l@tribune.mayo.edu> <gap-09d99b7aef-p2@usenetarchives.gap>`

```

In article <540mm5$o.··.@new··U.net>, pah··.@eu··t.be (Pieter Hintjens) says:
› 
› Bakulesh Thakker (tha··.@ma··o.edu) wrote:
…[21 more quoted lines elided]…
› Pieter Hintjens

Any cics/cobol snippet perhaps to showcase the wrapping of html to the
data? or would you perhaps need an api for that?
```

###### ↳ ↳ ↳ Re: COBOL / CICS as web data source

- **From:** "pah..." <ua-author-13876471@usenetarchives.gap>
- **Date:** 1996-10-16T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-09d99b7aef-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-09d99b7aef-p3@usenetarchives.gap>`
- **References:** `<53u62g$86l@tribune.mayo.edu> <gap-09d99b7aef-p2@usenetarchives.gap> <gap-09d99b7aef-p3@usenetarchives.gap>`

```

Your Name Here (int··.@ma··o.edu) wrote:
: >You can either generate HTML in the CICS transaction, or send
: >out something simpler which you then wrap into HTML in the CGI
: >program on the NT.

: Any cics/cobol snippet perhaps to showcase the wrapping of html to the
: data? or would you perhaps need an api for that?

The wrapping can be simplistic: ... where
... is the message returned by the CICS COBOL program. Or, it
can be smart, taking the message and re-interpreting it to format
a more useful HTML page. Or, the COBOL program could generate
HTML directly.
```

##### ↳ ↳ Re: COBOL / CICS as web data source

- **From:** "joh..." <ua-author-2226178@usenetarchives.gap>
- **Date:** 1996-10-16T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-09d99b7aef-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-09d99b7aef-p2@usenetarchives.gap>`
- **References:** `<53u62g$86l@tribune.mayo.edu> <gap-09d99b7aef-p2@usenetarchives.gap>`

```

In article <540mm5$o.··.@new··U.net>,
pah··.@eu··t.be (Pieter Hintjens) wrote:
› Bakulesh Thakker (tha··.@ma··o.edu) wrote:
› ....
…[3 more quoted lines elided]…
› This is almost off-topic for comp.lang.cobol, but...

Just as a matter of personnal interest/information for future use, what
newsgroup would this be more topical in??

John
```

###### ↳ ↳ ↳ Re: COBOL / CICS as web data source

- **From:** "pader..." <ua-author-17071645@usenetarchives.gap>
- **Date:** 1996-10-17T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-09d99b7aef-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-09d99b7aef-p5@usenetarchives.gap>`
- **References:** `<53u62g$86l@tribune.mayo.edu> <gap-09d99b7aef-p2@usenetarchives.gap> <gap-09d99b7aef-p5@usenetarchives.gap>`

```

In article <545mll$3.··.@jul··t.com>, joh··.@spr··t.com (John) says:
› 
› In article <540mm5$o.··.@new··U.net>,
…[11 more quoted lines elided]…
› John

John, I think it would be appropriate to post it in
comp.infosystems.www.servers.misc
```

###### ↳ ↳ ↳ Re: COBOL / CICS as web data source

_(reply depth: 4)_

- **From:** "david" <ua-author-9782@usenetarchives.gap>
- **Date:** 1996-10-19T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-09d99b7aef-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-09d99b7aef-p6@usenetarchives.gap>`
- **References:** `<53u62g$86l@tribune.mayo.edu> <gap-09d99b7aef-p2@usenetarchives.gap> <gap-09d99b7aef-p5@usenetarchives.gap> <gap-09d99b7aef-p6@usenetarchives.gap>`

```

Erwin R. Pader wrote:
› 
› In article <545mll$3.··.@jul··t.com>, joh··.@spr··t.com (John) says:
…[16 more quoted lines elided]…
›  comp.infosystems.www.servers.misc

Hey, folks, wait a minute. I appreciate John's question but think
we have a great forum right here. IBM has extended WWW support to
CICS in release 4 as a free upgrade. CICS now supports all
internet protocols on a variety of platforms and, sinced the
majority of CICS applications are in COBOL, I look here for CICS as
well as COBOL info. BTW, ibm's 4.1 documentation includes sample WWW
interface programs.

******************************************************************
*   d.s··.@ix.··m.com         David S. Kirk                 *
******************************************************************
```

###### ↳ ↳ ↳ Re: COBOL / CICS as web data source

_(reply depth: 5)_

- **From:** "tde..." <ua-author-17086515@usenetarchives.gap>
- **Date:** 1996-10-21T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-09d99b7aef-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-09d99b7aef-p7@usenetarchives.gap>`
- **References:** `<53u62g$86l@tribune.mayo.edu> <gap-09d99b7aef-p2@usenetarchives.gap> <gap-09d99b7aef-p5@usenetarchives.gap> <gap-09d99b7aef-p6@usenetarchives.gap> <gap-09d99b7aef-p7@usenetarchives.gap>`

```

FYI, a new product called AMAZON, from Intelligent Environments,
supports the "Webification" of data from CICS, APPC, MVS, 3270
terminal emulation, etc. (Plus all modern dbase platforms -- DB2,
Sybase, Oracel, SQL Server, etc.)

Check out http://www.ieinc.com for more info. Thanks & good luck!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
