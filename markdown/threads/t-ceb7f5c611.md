[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Anybody have a faster way to sort than MF Cobol on PC???

_9 messages · 8 participants · 1997-03 → 1997-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files) · [`Help requests and how-to`](../topics.md#help)

---

### Anybody have a faster way to sort than MF Cobol on PC???

- **From:** "car..." <ua-author-602860@usenetarchives.gap>
- **Date:** 1997-03-29T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5hl7is$ppe@sjx-ixn7.ix.netcom.com>`

```

We have some apps written in MF Cobol using workbench
for the PC. Their sort is very slow. Does anyone
know of another product that can be used on a PC?

When I worked on mainframes we used syncsort. But I
don't think they have a PC product.

Should I try calling a program that sorts in another
language?

Thanks,
Carlos
```

#### ↳ Re: Anybody have a faster way to sort than MF Cobol on PC???

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1997-03-29T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ceb7f5c611-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5hl7is$ppe@sjx-ixn7.ix.netcom.com>`
- **References:** `<5hl7is$ppe@sjx-ixn7.ix.netcom.com>`

```

.Willy wrote:
.>
.> On 30 Mar 1997 08:17:32 GMT, Car··.@ix.··m.com (Carlos) wrote:
.>
.> >We have some apps written in MF Cobol using workbench
.> >for the PC. Their sort is very slow. Does anyone
.> >know of another product that can be used on a PC?
.> >
.> >When I worked on mainframes we used syncsort. But I
.> >don't think they have a PC product.
.> >
.> >Should I try calling a program that sorts in another
.> >language?
.> >
.> >Thanks,
.> > Carlos
.> >
.> I haven't seen anything sort faster than the MF COBOL sorter in a PC
.> environment except for some shareware sorters that didn't provide all
.> the features of the COBOL sorter.
.>
.> You'll never sort as fast as a mainframe with a PC. PC's just don't
.> have that kind of horsepower.


Sort times can vary wildly between PC Cobol compilers, sometimes by
orders of magnitude. Unless Micro Focus has dramatically improved their
sort performance, it is indeed not the fastest. Benchmark tests I did a
number of years ago showed MF to be of the slowest. The fastest was
Realia Cobol. For example, a 7000 record sort took around 300+ seconds
with MF Cobol, while Realia only took around 10 seconds. These tests
were done on much slower machines than available today.

Another Cobol compiler which had very good sort performance was MBP,
which is now owned by Micro Focus. The MBP Cobol compiler incorporated
the sort product from Opt-Tech. It's sort times were just slightly less
than Realia. It was a very comprehensive sort package, and did many of
things (features) of the mainframe sort packages. I do not know if
Opt-Tech is still around. I also agree with Willy that you won't get
the same performance on the PC as the mainframe, particularly where
large amounts of data are involved.

Mike Dodas
```

#### ↳ Re: Anybody have a faster way to sort than MF Cobol on PC???

- **From:** "jsmck..." <ua-author-17071518@usenetarchives.gap>
- **Date:** 1997-03-29T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ceb7f5c611-p3@usenetarchives.gap>`
- **In-Reply-To:** `<5hl7is$ppe@sjx-ixn7.ix.netcom.com>`
- **References:** `<5hl7is$ppe@sjx-ixn7.ix.netcom.com>`

```


In article <5hl7is$p.··.@sjx··m.com> Carlos wrote:

› We have some apps written in MF Cobol using workbench
› for the PC.  Their sort is very slow.  Does anyone
…[6 more quoted lines elided]…
› language?

In a previous job I used Opt-Tech Sort/Merge, from:

Opt-Tech Data Processing
PO Box 678
Zephyr Cove, NV 89448

ph. (702) 588-3737

You can run it as a standalone utility or you can call it as
a subroutine. I don't know specifically if you can call it
from MF Cobol. I also never ran any speed comparisons, but we
were satisfied with its performance.

A recent ad (November 1966) prices it at $149 for MS-DOS and
Windows, or $249 for Win95, OS/2, and UNIX.

Scott McKellar jm4··.@mul··c.com
```

##### ↳ ↳ Re: Anybody have a faster way to sort than MF Cobol on PC???

- **From:** "ofer ben-sade" <ua-author-17071921@usenetarchives.gap>
- **Date:** 1997-03-31T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ceb7f5c611-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ceb7f5c611-p3@usenetarchives.gap>`
- **References:** `<5hl7is$ppe@sjx-ixn7.ix.netcom.com> <gap-ceb7f5c611-p3@usenetarchives.gap>`

```

John McKellar wrote:
› 
› In article <5hl7is$p.··.@sjx··m.com> Carlos wrote:
…[27 more quoted lines elided]…
› Scott McKellar          jm4··.@mul··c.com

You can write subroutine that call any sort utility in any language
then when you compile the cobol program that use SORT verb add
directive -C CALLSORT=routine_name (MF COBOL system reference - voiume
2) this will make the program call routine_name when it get to the SORT
verb passing 2 parameter action_code , fcd the same like calling EXTFH (
MF COBOL system reference volume 1 chap 5 ) now U can take out of FCD
any information U need for calling the sort utility
```

###### ↳ ↳ ↳ Re: Anybody have a faster way to sort than MF Cobol on PC???

- **From:** "ofer ben-sade" <ua-author-17071921@usenetarchives.gap>
- **Date:** 1997-03-31T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ceb7f5c611-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ceb7f5c611-p4@usenetarchives.gap>`
- **References:** `<5hl7is$ppe@sjx-ixn7.ix.netcom.com> <gap-ceb7f5c611-p3@usenetarchives.gap> <gap-ceb7f5c611-p4@usenetarchives.gap>`

```

Ofer Ben-Sade wrote:
› 
› John McKellar wrote:
…[37 more quoted lines elided]…
› any information  U need for calling the sort utility

I use MF COBOL for Micro Focus Cobol NOT NOT Mainframe cobol
```

#### ↳ Re: Anybody have a faster way to sort than MF Cobol on PC???

- **From:** "shawn sharifi" <ua-author-17072940@usenetarchives.gap>
- **Date:** 1997-03-30T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ceb7f5c611-p6@usenetarchives.gap>`
- **In-Reply-To:** `<5hl7is$ppe@sjx-ixn7.ix.netcom.com>`
- **References:** `<5hl7is$ppe@sjx-ixn7.ix.netcom.com>`

```

Months ago I got an Advertisement from SyncSort stating that they have a MF
compatible sort. You may want to contact them. Also Fujitsu has a very good
sort utility that comes with their COBOL.

Carlos wrote in article
<5hl7is$p.··.@sjx··m.com>...
› We have some apps written in MF Cobol using workbench
› for the PC.  Their sort is very slow.  Does anyone
…[12 more quoted lines elided]…
›
```

#### ↳ Re: Anybody have a faster way to sort than MF Cobol on PC???

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-03-30T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ceb7f5c611-p7@usenetarchives.gap>`
- **In-Reply-To:** `<5hl7is$ppe@sjx-ixn7.ix.netcom.com>`
- **References:** `<5hl7is$ppe@sjx-ixn7.ix.netcom.com>`

```



Willy wrote in article ...
› On 30 Mar 1997 08:17:32 GMT, Car··.@ix.··m.com (Carlos) wrote:
› 
…[8 more quoted lines elided]…
› 

The fastest PC sorts I have seen come from CA-Realia's Sort. I use it for
my own use all the time, but here at work, a MicroFocus shop, they are
lothe to use sorts because of the slowness and disk space requirements.
```

##### ↳ ↳ Re: Anybody have a faster way to sort than MF Cobol on PC???

- **From:** "mri..." <ua-author-8217666@usenetarchives.gap>
- **Date:** 1997-03-31T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ceb7f5c611-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ceb7f5c611-p7@usenetarchives.gap>`
- **References:** `<5hl7is$ppe@sjx-ixn7.ix.netcom.com> <gap-ceb7f5c611-p7@usenetarchives.gap>`

```

"Thane Hubbell" wrote:

››› We have some apps written in MF Cobol using workbench
››› for the PC. Their sort is very slow. Does anyone
››› know of another product that can be used on a PC?

Note: I am not a sales type. Im a digithead like the rest of you.

I have MF 3.2.50-something and RealCob 4.2 and for some reason havent
benchmarked either against our 32 bit sort product. Probably because
testing 16 bit apps on NT is not 'fair'. That and Ive just not had the
time.

Anyhow, there are several 3rd party sort products for PC's. We have
one (Assort) which was written specifically for folks coming from the
mainframe who are used to DFSort etc. More info and a timed, working
demo is available at our web site if youre interested.

There are also several other sort products for the PC (meaning NT,
OS/2 and possibly Windows95). IBM offers one, as does Opt-Tech and
there is at least one other who name escapes me at the moment.

You might try http://www.info-partners.com/softinfo and look at
SoftInfo. Its a nice 'enterprise software' search engine and has
contact info on Opt-Tech as well as others.
```

#### ↳ Re: Anybody have a faster way to sort than MF Cobol on PC???

- **From:** "co..." <ua-author-6588778@usenetarchives.gap>
- **Date:** 1997-04-07T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ceb7f5c611-p9@usenetarchives.gap>`
- **In-Reply-To:** `<5hl7is$ppe@sjx-ixn7.ix.netcom.com>`
- **References:** `<5hl7is$ppe@sjx-ixn7.ix.netcom.com>`

```

When you sign up to get the Free COBOL CD from Fujitsu you will get a
number of utilities to use with it. Our COBOL comes with native
sorting capabilities and a sort utility that can enhance performance
up to 30%.


They are called PowerBSORT (16-bit) and PowerBSORT OCX (32-Bit).

You can request these from our web site at:
http://www.adtools.com/lpg/freecopy.htm

Thanks,


Fujitsu Software Corporation
http://www.adtools.com
Tel (800) 545-6774
Fax (408) 428-0600
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
