[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CICS on PC ?

_7 messages · 5 participants · 2002-12_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### CICS on PC ?

- **From:** "bassman" <no@spam.com>
- **Date:** 2002-12-19T15:23:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5wlM9.3557$HD1.703505621@hestia.telenet-ops.be>`

```
Hi there,

As a freelance IT consultant with several years of cobol experience on
Unisys and Wang, i just started with some CICS selfstudy.
I am already a bit experienced on IBM MVS with TSO, APS (cobol generator) en
DB2 so I have just started with the book "Murah's CICS for the cobol
programmer" which I find very usefull.

I would enjoy it a lot if could do some CICS testing on my w2K laptop. Any
suggestions which inexpensive CICS / COBOL software is available for pc ?
Any other ideas that might be usefull ?

Thanks for the help.
```

#### ↳ Re: CICS on PC ?

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-12-20T04:52:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nmxM9.15667$KW2.686873@twister.austin.rr.com>`
- **References:** `<5wlM9.3557$HD1.703505621@hestia.telenet-ops.be>`

```
Real CICS is available with, and in fact, delivered wth Visual Age COBOL. Occasionally, copies are sold on E-Bay, usually older
copies but that would not make any difference with that book. If you are member of
IBM PWD, you can pick up a copy for under $50 directly from IBM.

-Paul


"bassman" <no@spam.com> wrote in message news:5wlM9.3557$HD1.703505621@hestia.telenet-ops.be...
> Hi there,
>
…[12 more quoted lines elided]…
>
```

##### ↳ ↳ Re: CICS on PC ?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-12-19T21:33:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<atu32h$adj$1@slb3.atl.mindspring.net>`
- **References:** `<5wlM9.3557$HD1.703505621@hestia.telenet-ops.be> <nmxM9.15667$KW2.686873@twister.austin.rr.com>`

```
When one says "Real CICS" - it is important that this be distinguished from
"RealCICS" (no space) which was the CICS emualator that used to be available
with the Realia COBOL compiler (pre-CA) - and which is now known as
"Advantage CA-Realia II Workbench Option for CICS" see

 http://www3.ca.com/Solutions/ProductOption.asp?ID=3816

The IBM PC offering is discussed in
  "Chapter 16. Developing COBOL programs for CICS"

in the document at:
 http://publibfp.boulder.ibm.com/epubs/pdf/c2708121.pdf
```

###### ↳ ↳ ↳ Re: CICS on PC ?

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-12-20T06:32:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JPyM9.16105$KW2.711499@twister.austin.rr.com>`
- **References:** `<5wlM9.3557$HD1.703505621@hestia.telenet-ops.be> <nmxM9.15667$KW2.686873@twister.austin.rr.com> <atu32h$adj$1@slb3.atl.mindspring.net>`

```
Thank you Bill - I did not know that, appreciate the clarification
-Paul

"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message news:atu32h$adj$1@slb3.atl.mindspring.net...
> When one says "Real CICS" - it is important that this be distinguished from
> "RealCICS" (no space) which was the CICS emualator that used to be available
…[49 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: CICS on PC ?

- **From:** charles.godwin@ca.com (Charles Godwin)
- **Date:** 2002-12-20T03:29:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c8035ce7.0212200329.23419cc9@posting.google.com>`
- **References:** `<5wlM9.3557$HD1.703505621@hestia.telenet-ops.be> <nmxM9.15667$KW2.686873@twister.austin.rr.com> <atu32h$adj$1@slb3.atl.mindspring.net>`

```
Bill

Thanks for the mention of CA-Realia version of CICS. However I must
clarify your information.

The Advantage CA-Realia II Workbench includes the CICS development and
runtime environment for a PC based CICS emulator. This is all you need
to develop, test and run CICS applications on a PC.

See this URL for details.
http://www3.ca.com/Solutions/Product.asp?ID=1475

The Option for CICS you mentioned is an add on extra for users who
also want to use our Workbench to debug CICS programs running on the
mainframe. This uses an interface to Intertest running on a mainframe
CICS region.

I will say that the text on our website could be misleading so I'll
see about getting it clarified.

Charles Godwin
Development Manager
Advatage CA-Realia II Workbench

"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message news:<atu32h$adj$1@slb3.atl.mindspring.net>...
> When one says "Real CICS" - it is important that this be distinguished from
> "RealCICS" (no space) which was the CICS emualator that used to be available
…[14 more quoted lines elided]…
>  wmklein <at> ix.netcom.com
```

#### ↳ Re: CICS on PC ?

- **From:** "Paul Barnett" <paul.barnett@nospam.microfocus.com>
- **Date:** 2002-12-20T14:51:10
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<atva7r$2o9$1@hyperion.microfocus.com>`
- **References:** `<5wlM9.3557$HD1.703505621@hestia.telenet-ops.be>`

```
You might want to consider Meinframe Express for the PC available from Micro
Focus.

It's an IDE that allows development and debiugging of mainframe COBOL (and
PL/I) applications on the PC. It emulates all of the relevant mainframe
features on the PC.

www.microfocus.com

"bassman" <no@spam.com> wrote in message
news:5wlM9.3557$HD1.703505621@hestia.telenet-ops.be...
> Hi there,
>
> As a freelance IT consultant with several years of cobol experience on
> Unisys and Wang, i just started with some CICS selfstudy.
> I am already a bit experienced on IBM MVS with TSO, APS (cobol generator)
en
> DB2 so I have just started with the book "Murah's CICS for the cobol
> programmer" which I find very usefull.
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: CICS on PC ?

- **From:** "Bassman" <no@spam.com>
- **Date:** 2002-12-21T07:30:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rMUM9.5311$911.1391870094@hestia.telenet-ops.be>`
- **References:** `<5wlM9.3557$HD1.703505621@hestia.telenet-ops.be> <atva7r$2o9$1@hyperion.microfocus.com>`

```
Thanks everybody
I guess Visual Age Cobol and Mainframe Express will be the options.

Peace
Bassman

"Paul Barnett" <paul.barnett@nospam.microfocus.com> wrote in message
news:atva7r$2o9$1@hyperion.microfocus.com...
> You might want to consider Meinframe Express for the PC available from
Micro
> Focus.
>
…[12 more quoted lines elided]…
> > I am already a bit experienced on IBM MVS with TSO, APS (cobol
generator)
> en
> > DB2 so I have just started with the book "Murah's CICS for the cobol
> > programmer" which I find very usefull.
> >
> > I would enjoy it a lot if could do some CICS testing on my w2K laptop.
Any
> > suggestions which inexpensive CICS / COBOL software is available for pc
?
> > Any other ideas that might be usefull ?
> >
…[5 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
