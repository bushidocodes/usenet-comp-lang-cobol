[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Batch on unix / CICS transaction on MVS interface

_9 messages · 4 participants · 2000-08_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Batch on unix / CICS transaction on MVS interface

- **From:** Patrick Van Nieuwenhuyze <vannieu.p@fr.ibm.com>
- **Date:** 2000-08-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<399119C9.EC965FFF@fr.ibm.com>`

```
How to modify a CICS application screen (under MVS) from a Cobol batch
program on Solaris.
```

#### ↳ Re: Batch on unix / CICS transaction on MVS interface

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-08-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pqg3ps4ndmcarialgr5ng0fnvh9qeq1vjd@4ax.com>`
- **References:** `<399119C9.EC965FFF@fr.ibm.com>`

```
On Wed, 09 Aug 2000 10:43:53 +0200, Patrick Van Nieuwenhuyze <vannieu.p@fr.ibm.com> wrote:


>How to modify a CICS application screen (under MVS) from a Cobol batch
>program on Solaris.

??? Sorry, but I do NOT understand.  Is the program CICS, or Batch?  Is it MVS? or
SOLARIS? 

Could you clarify, please?



     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)



      What does CICS mean? - Capital Investment in Computing Systems
```

##### ↳ ↳ Re: Batch on unix / CICS transaction on MVS interface

- **From:** Patrick Van Nieuwenhuyze <vannieu.p@fr.ibm.com>
- **Date:** 2000-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39924F96.AA71A17C@fr.ibm.com>`
- **References:** `<399119C9.EC965FFF@fr.ibm.com> <pqg3ps4ndmcarialgr5ng0fnvh9qeq1vjd@4ax.com>`

```
I want a batch Cobol program on Solaris. This program on Solaris must both access relationnal
database, and ALSO read data on another computer (MVS operating system). Theses datas are
available only by existing CICS transaction.

Volker Bandke wrote:

> On Wed, 09 Aug 2000 10:43:53 +0200, Patrick Van Nieuwenhuyze <vannieu.p@fr.ibm.com> wrote:
>
…[13 more quoted lines elided]…
>       What does CICS mean? - Capital Investment in Computing Systems
```

###### ↳ ↳ ↳ Re: Batch on unix / CICS transaction on MVS interface

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3993179d.30325213@207.126.101.100>`
- **References:** `<399119C9.EC965FFF@fr.ibm.com> <pqg3ps4ndmcarialgr5ng0fnvh9qeq1vjd@4ax.com> <39924F96.AA71A17C@fr.ibm.com>`

```
The CICS Universal Client in addition to ECI is what you want.
Universal Client is free from IBM (Actually not, but you have a
license if you are running Transaction Server and SOME pre-Transaction
server versions of CICS).

On Thu, 10 Aug 2000 08:45:42 +0200, Patrick Van Nieuwenhuyze
<vannieu.p@fr.ibm.com> wrote:

>I want a batch Cobol program on Solaris. This program on Solaris must both access relationnal
>database, and ALSO read data on another computer (MVS operating system). Theses datas are
…[20 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Batch on unix / CICS transaction on MVS interface

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8D1E8EAB309BC96E.37BE126BD0144CCB.E13D28B74E69018B@lp.airnews.net>`
- **References:** `<399119C9.EC965FFF@fr.ibm.com> <pqg3ps4ndmcarialgr5ng0fnvh9qeq1vjd@4ax.com> <39924F96.AA71A17C@fr.ibm.com>`

```
On Thu, 10 Aug 2000 08:45:42 +0200, Patrick Van Nieuwenhuyze
<vannieu.p@fr.ibm.com> enlightened us:

>I want a batch Cobol program on Solaris. This program on Solaris must both access relationnal
>database, and ALSO read data on another computer (MVS operating system). Theses datas are
…[19 more quoted lines elided]…
>>       What does CICS mean? - Capital Investment in Computing Systems

What you need is a way to talk to your MVS mainframe from your Solaris
and have a CICS transaction run on the mainframe and return the data
to you on the Solaris.  I would suggest you look at IBM's MQ series as
a way to do this.

Regards,


          ////
         (o o)
-oOO--(_)--OOo-

I have six locks on my door all in a row. When I go out, I lock every
other one. I figure no matter how long somebody stands there picking the
locks, they are always locking three.






Boycott Mitsubishi Industries
For more info, please see:  
http://www.ran.org/ran/ran_campaigns/mitsubishi/background.html

Remove nospam to email me.

 Steve
```

###### ↳ ↳ ↳ Re: Batch on unix / CICS transaction on MVS interface

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bq87psctc1aujl034p4lljqooonn050bt2@4ax.com>`
- **References:** `<399119C9.EC965FFF@fr.ibm.com> <pqg3ps4ndmcarialgr5ng0fnvh9qeq1vjd@4ax.com> <39924F96.AA71A17C@fr.ibm.com>`

```
On Thu, 10 Aug 2000 08:45:42 +0200, Patrick Van Nieuwenhuyze <vannieu.p@fr.ibm.com> wrote:

>I want a batch Cobol program on Solaris. This program on Solaris must both access relationnal
>database, and ALSO read data on another computer (MVS operating system). Theses datas are
>available only by existing CICS transaction.

okay, 

then you can use the ONC/RPC featrure on CICS, which makes CICS application programs
appear to Uniy like an RPC server

AFAIK the CICS universal client is NOT available on Solaris.  But if a Solaris process can
access a (let's say) windows process, then you couls also use the CICS universal Client
from Windows to access CICS mainframe

The third possibility is to spin the WEB around CICS - access the CICS data using the CICS
Web support (with or without 3279 bridge)

Just make up your mind




     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)



      But scientists, who ought to know Assure us that it must be so. Oh, let us never, never doubt What nobody is sure about. -- Hilaire Belloc
```

###### ↳ ↳ ↳ Re: Batch on unix / CICS transaction on MVS interface

_(reply depth: 4)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n2e7psgneqavnk0mbvqch8l8br7i8uklcf@4ax.com>`
- **References:** `<399119C9.EC965FFF@fr.ibm.com> <pqg3ps4ndmcarialgr5ng0fnvh9qeq1vjd@4ax.com> <39924F96.AA71A17C@fr.ibm.com> <bq87psctc1aujl034p4lljqooonn050bt2@4ax.com>`

```
On Fri, 11 Aug 2000 08:59:05 +0200, Volker Bandke <vbandke@bsp-gmbh.com> wrote:

>On Thu, 10 Aug 2000 08:45:42 +0200, Patrick Van Nieuwenhuyze <vannieu.p@fr.ibm.com> wrote:
>
…[3 more quoted lines elided]…
>
I just checked (should have done so before posting, of course),  The CICS universal client
_IS_ available on Solaris, therefore you can use ECI to access programs on CICS, and EPI
to access transactions on CICS.


     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)



      The things I did not know at first I learned by doing twice. -- Billy Joel
```

###### ↳ ↳ ↳ Re: Batch on unix / CICS transaction on MVS interface

_(reply depth: 5)_

- **From:** Patrick Van Nieuwenhuyze <vannieu.p@fr.ibm.com>
- **Date:** 2000-08-17T08:13:44+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<399B8297.3F412517@fr.ibm.com>`
- **References:** `<399119C9.EC965FFF@fr.ibm.com> <pqg3ps4ndmcarialgr5ng0fnvh9qeq1vjd@4ax.com> <39924F96.AA71A17C@fr.ibm.com> <bq87psctc1aujl034p4lljqooonn050bt2@4ax.com> <n2e7psgneqavnk0mbvqch8l8br7i8uklcf@4ax.com>`

```
I  access existing transactions (on MVS-CICS)  from Solaris using "s3270".
URL: http://www.geocities.com/SiliconValley/Peaks/7814/

Thanks for your Help

Patrick

Volker Bandke wrote:

> On Fri, 11 Aug 2000 08:59:05 +0200, Volker Bandke <vbandke@bsp-gmbh.com> wrote:
>
…[15 more quoted lines elided]…
>       The things I did not know at first I learned by doing twice. -- Billy Joel
```

###### ↳ ↳ ↳ Re: Batch on unix / CICS transaction on MVS interface

_(reply depth: 5)_

- **From:** Patrick Van Nieuwenhuyze <vannieu.p@fr.ibm.com>
- **Date:** 2000-08-17T08:14:13+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<399B82B5.37FC8FD0@fr.ibm.com>`
- **References:** `<399119C9.EC965FFF@fr.ibm.com> <pqg3ps4ndmcarialgr5ng0fnvh9qeq1vjd@4ax.com> <39924F96.AA71A17C@fr.ibm.com> <bq87psctc1aujl034p4lljqooonn050bt2@4ax.com> <n2e7psgneqavnk0mbvqch8l8br7i8uklcf@4ax.com>`

```
I  access existing transactions (on MVS-CICS)  from Solaris using "s3270".
URL: http://www.geocities.com/SiliconValley/Peaks/7814/

Thanks for your Help

Patrick

Volker Bandke wrote:

> On Fri, 11 Aug 2000 08:59:05 +0200, Volker Bandke <vbandke@bsp-gmbh.com> wrote:
>
…[15 more quoted lines elided]…
>       The things I did not know at first I learned by doing twice. -- Billy Joel
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
