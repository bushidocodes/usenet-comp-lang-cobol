[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COS or ARC TAN in COBOL?

_5 messages · 5 participants · 2000-06_

---

### COS or ARC TAN in COBOL?

- **From:** Lisa Paternoster <lpaterno@my-deja.com>
- **Date:** 2000-06-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8hjmqv$isc$1@nnrp1.deja.com>`

```
I have a need to program an equation containing a COS and ARC TAN.  Can
this be done in cobol?

Thanks for helping me!
Lisa


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: COS or ARC TAN in COBOL?

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2000-06-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hie%4.14648$Gh.184890@typhoon.austin.rr.com>`
- **References:** `<8hjmqv$isc$1@nnrp1.deja.com>`

```

Lisa Paternoster <lpaterno@my-deja.com> wrote in message
news:8hjmqv$isc$1@nnrp1.deja.com...
> I have a need to program an equation containing a COS and ARC TAN.  Can
> this be done in cobol?
>
> Thanks for helping me!
> Lisa

Lisa,
First read the manual to see if your compiler has a function to do this.
If not, go to  http://etk.com/download/etkpak/etkpak.htm#MATHPK
and use MATHPK.
```

#### ↳ Re: COS or ARC TAN in COBOL?

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-06-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393d731d.155605027@207.126.101.100>`
- **References:** `<8hjmqv$isc$1@nnrp1.deja.com>`

```
On Tue, 06 Jun 2000 20:27:33 GMT, Lisa Paternoster
<lpaterno@my-deja.com> wrote:

>I have a need to program an equation containing a COS and ARC TAN.  Can
>this be done in cobol?
>

Yes.  Hour 22 - Sams Teach Yourself COBOL in 24 Hours.  
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: COS or ARC TAN in COBOL?

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-06-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000606193023.02791.00001247@nso-da.aol.com>`
- **References:** `<8hjmqv$isc$1@nnrp1.deja.com>`

```
In article <8hjmqv$isc$1@nnrp1.deja.com>, Lisa Paternoster
<lpaterno@my-deja.com> writes:

>
>I have a need to program an equation containing a COS and ARC TAN.  Can
…[4 more quoted lines elided]…
>

This depends on the compiler that you are using.
I checked the FujiCOBOL User's Guide Intrinsic Functions list
and found that COS, SIN, TAN, ACOS, ASIN, ATAN are supported.
COS = CoSine
SIN = Sine
TAN = Tangent
ACOS = ArcCosine (?) / inverse of CoSine
ASIN = ...
ATAN = ...

Hope that this helps.
The documentation indicates that these are considered COBOL97(?)
compliant.
```

#### ↳ Re: COS or ARC TAN in COBOL?

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 2000-06-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8hn2c6$ltb$1@slb6.atl.mindspring.net>`
- **References:** `<8hjmqv$isc$1@nnrp1.deja.com>`

```
In the IBM world, refer to COBOL for MVS and OS/390 (also known as COBOL/370
and COBOL3), FUNCTIONS ===> COS (Cosine) and ATAN (Arctangent).

I believe these FUNCTIONS are part of the COBOL '85 ANSI Standard, not IBM
extensions.

In IBM's "LE" (Language Environment), refer to the Callable Service Routines
CEESxCOS (Cosine) and CEESxATN (Arctangent).

http://ppdbooks.pok.ibm.com/cgi-bin/bookmgr/bookmgr.cmd/library

is the IBM Bookmanager Web Page.

HTH...

Cheers,

WOB,
Atlanta

"Lisa Paternoster" <lpaterno@my-deja.com> wrote in message
news:8hjmqv$isc$1@nnrp1.deja.com...
> I have a need to program an equation containing a COS and ARC TAN.  Can
> this be done in cobol?
…[6 more quoted lines elided]…
> Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
