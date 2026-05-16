[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Pi

_9 messages · 6 participants · 1999-10_

---

### Re: Pi

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37FB4E3F.AC298AB8@NOSPAMhome.com>`
- **References:** `<7tastn$mlh$2@nickel.uunet.be> <37f8f95a.16762923@news2.ibm.net> <7tb010$hib@dfw-ixnews12.ix.netcom.com> <37f95365_1@news3.prserv.net> <4KmK3.17002$SI1.144298@news1.mia> <37fa8df9_3@news3.prserv.net>`

```
I've seen people recommend using a simple fraction to replace PI while
used in arithmetic expressions.  Their reason is that the fraction is
stored in a temporary variable to more precision than we could store as
a constant.

I don't remember the recommended fraction - I suppose that would vary
depending upon the computer architecture and compiler.
```

#### ↳ Re: Pi

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37FB5435.10A92F58@zip.com.au>`
- **References:** `<7tastn$mlh$2@nickel.uunet.be> <37f8f95a.16762923@news2.ibm.net> <7tb010$hib@dfw-ixnews12.ix.netcom.com> <37f95365_1@news3.prserv.net> <4KmK3.17002$SI1.144298@news1.mia> <37fa8df9_3@news3.prserv.net> <37FB4E3F.AC298AB8@NOSPAMhome.com>`

```
Howard Brazee wrote:
> 
> I've seen people recommend using a simple fraction to replace PI while
…[5 more quoted lines elided]…
> depending upon the computer architecture and compiler.

22 / 7  If I recall.
```

##### ↳ ↳ Re: Pi

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DHIK3.1734$x4.45823@news2.mia>`
- **References:** `<7tastn$mlh$2@nickel.uunet.be> <37f8f95a.16762923@news2.ibm.net> <7tb010$hib@dfw-ixnews12.ix.netcom.com> <37f95365_1@news3.prserv.net> <4KmK3.17002$SI1.144298@news1.mia> <37fa8df9_3@news3.prserv.net> <37FB4E3F.AC298AB8@NOSPAMhome.com> <37FB5435.10A92F58@zip.com.au>`

```
Ken Foskey wrote:
>Howard Brazee wrote:
>>
…[8 more quoted lines elided]…
>22 / 7  If I recall.

Pi                 = 3.141592653589793...
355/113 (6 digits) = 3.1415929... (7 significant digits)
22/7    (3 digits) = 3.142...     (3 significant digits)

Neither gives significantly more digits than you supply.
```

###### ↳ ↳ ↳ Re: Pi

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37FB75EE.6F4A8E2C@NOSPAMhome.com>`
- **References:** `<7tastn$mlh$2@nickel.uunet.be> <37f8f95a.16762923@news2.ibm.net> <7tb010$hib@dfw-ixnews12.ix.netcom.com> <37f95365_1@news3.prserv.net> <4KmK3.17002$SI1.144298@news1.mia> <37fa8df9_3@news3.prserv.net> <37FB4E3F.AC298AB8@NOSPAMhome.com> <37FB5435.10A92F58@zip.com.au> <DHIK3.1734$x4.45823@news2.mia>`

```
Judson McClendon wrote:

> >> I don't remember the recommended fraction - I suppose that would vary
> >> depending upon the computer architecture and compiler.
…[7 more quoted lines elided]…
> Neither gives significantly more digits than you supply.

It's quite possible the solution may have been designed for something
like Apple Basic, which had a different constant size.  Still, it would
be cool to have something which would be use with mainframe COBOL.
```

#### ↳ Re: Pi

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WAIK3.1722$x4.45611@news2.mia>`
- **References:** `<7tastn$mlh$2@nickel.uunet.be> <37f8f95a.16762923@news2.ibm.net> <7tb010$hib@dfw-ixnews12.ix.netcom.com> <37f95365_1@news3.prserv.net> <4KmK3.17002$SI1.144298@news1.mia> <37fa8df9_3@news3.prserv.net> <37FB4E3F.AC298AB8@NOSPAMhome.com>`

```
Howard Brazee wrote:
>I've seen people recommend using a simple fraction to replace PI while
>used in arithmetic expressions.  Their reason is that the fraction is
…[4 more quoted lines elided]…
>depending upon the computer architecture and compiler.

I've played around with pi a bit, and have never heard of this.  I am
familiar with 22/7 and 355/113, but these were used because they are
simple and easy to remember.  Neither gives pi to more than one extra
digit.  I know of no short ratio that will give a significant number
of digits of pi, that would be suitable for computer use.  The late
Petr Beckmann's excellent "A History of PI" doesn't mention one that
I recall.  Howard, if you can remember what it was, or if somebody
else knows of one, please post it. :-)
```

##### ↳ ↳ Re: Pi

- **From:** Art Perry <eowynfuzz@my-deja.com>
- **Date:** 1999-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7tii7c$u4o$1@nnrp1.deja.com>`
- **References:** `<7tastn$mlh$2@nickel.uunet.be> <37f8f95a.16762923@news2.ibm.net> <7tb010$hib@dfw-ixnews12.ix.netcom.com> <37f95365_1@news3.prserv.net> <4KmK3.17002$SI1.144298@news1.mia> <37fa8df9_3@news3.prserv.net> <37FB4E3F.AC298AB8@NOSPAMhome.com> <WAIK3.1722$x4.45611@news2.mia>`

```
This is all fascinating.  The use of accurate pi for scientific type
applications is obvious.  What are some business scenarios for using pi?

-Art

In article <WAIK3.1722$x4.45611@news2.mia>,
  "Judson McClendon" <judmc123@bellsouth.net> wrote:
> I've played around with pi a bit, and have never heard of this.  I am
> familiar with 22/7 and 355/113, but these were used because they are
> simple and easy to remember.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Pi

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37fcdeb3.129993316@news1.attglobal.net>`
- **References:** `<7tastn$mlh$2@nickel.uunet.be> <37f8f95a.16762923@news2.ibm.net> <7tb010$hib@dfw-ixnews12.ix.netcom.com> <37f95365_1@news3.prserv.net> <4KmK3.17002$SI1.144298@news1.mia> <37fa8df9_3@news3.prserv.net> <37FB4E3F.AC298AB8@NOSPAMhome.com> <WAIK3.1722$x4.45611@news2.mia> <7tii7c$u4o$1@nnrp1.deja.com>`

```
On Thu, 07 Oct 1999 16:37:02 GMT, Art Perry <eowynfuzz@my-deja.com>
wrote:

>This is all fascinating.  The use of accurate pi for scientific type
>applications is obvious.  What are some business scenarios for using pi?
>

To use an example Warren Simmons sent me - to determine the shipping
weight of a length of pipe with varying wall thincknesses and lenghts.


---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Pi

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37fcdf0d.130083391@news1.attglobal.net>`
- **References:** `<7tastn$mlh$2@nickel.uunet.be> <37f8f95a.16762923@news2.ibm.net> <7tb010$hib@dfw-ixnews12.ix.netcom.com> <37f95365_1@news3.prserv.net> <4KmK3.17002$SI1.144298@news1.mia> <37fa8df9_3@news3.prserv.net> <37FB4E3F.AC298AB8@NOSPAMhome.com> <WAIK3.1722$x4.45611@news2.mia> <7tii7c$u4o$1@nnrp1.deja.com>`

```
On Thu, 07 Oct 1999 16:37:02 GMT, Art Perry <eowynfuzz@my-deja.com>
wrote:

>This is all fascinating.  The use of accurate pi for scientific type
>applications is obvious.  What are some business scenarios for using pi?
>

To use an example Warren Simmons sent me - to determine the shipping
weight of a length of pipe with varying wall thincknesses and lenghts.


---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Pi

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i1bL3.2502$7p6.28079@dfiatx1-snr1.gtei.net>`
- **References:** `<7tastn$mlh$2@nickel.uunet.be> <37f8f95a.16762923@news2.ibm.net> <7tb010$hib@dfw-ixnews12.ix.netcom.com> <37f95365_1@news3.prserv.net> <4KmK3.17002$SI1.144298@news1.mia> <37fa8df9_3@news3.prserv.net> <37FB4E3F.AC298AB8@NOSPAMhome.com> <WAIK3.1722$x4.45611@news2.mia> <7tii7c$u4o$1@nnrp1.deja.com>`

```
Art Perry wrote in message <7tii7c$u4o$1@nnrp1.deja.com>...
>This is all fascinating.  The use of accurate pi for scientific type
>applications is obvious.  What are some business scenarios for using pi?
>


A British crumpet company with an eye on the U.S. market?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
