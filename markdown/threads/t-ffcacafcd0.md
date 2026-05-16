[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM COBOL to HP-UX COBOL

_7 messages · 4 participants · 2002-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### IBM COBOL to HP-UX COBOL

- **From:** "Shyam" <shyamsunder.puranam@digital.com>
- **Date:** 2002-08-19T15:50:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3t889.20$h_5.584751@news.cpqcorp.net>`

```
Hi:

I am a new comer to this group. Please excuse me for my ignorance and any
questions that may sound very trivial.

One of my customer is wanting to move his COBOL applications from IBM to
HP-UX. Currently he is using CICS on IBM. Though I have worked with COBOL,
my knowledge is limited to Tandem NonStop platform. Hence, I do not know
much about compatibility of COBOL on other platforms, the semantics...

I request the following information from you

(1) What is the compiler used on HP-UX? Does HP-UX has its own compiler? Or
does it use MicroFocus or Fujitsu to compile COBOL programs?
(2) If I have to migrate these Screen Maps in IBM - CICS to HP-UX, can I use
the Screen Section on HP-UX? Are there any restrictions on using it? Can any
one please direct me to some documentation of COBOL on HP-UX.
(3) Are there any specific compiler directives I need to use on HP-UX? I
wrote a simple COBOL program and tried compiling, it said cannot
find -lFutil and then -lcob. (really my efforts were futile)

I appreciate your help on this and thanking you in advance.

Regds,
Shyam
```

#### ↳ Re: IBM COBOL to HP-UX COBOL

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-08-19T15:58:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oA889.68395$eK6.2375534@twister.austin.rr.com>`
- **References:** `<3t889.20$h_5.584751@news.cpqcorp.net>`

```
It depends upon why you are migrating; if the goal is just to port it to a new platform as quickly as possible, then you want to
look into MicroFocus and using CICS (well, Transaction Server) under HP/UX.

If the goal is to move away from CICS and IBM, then yes, you will have to recode to use another compiler or screen vendor's display
capability.  HP has their own screen capability, and Microfocus has a more generic screen capability and runs on many platforms.

If the goal is to port it quickly and save money... well... have you instead looked at porting to AIX and the pSeries machines?
pSeries runs, TxServer (i.e. CICS) and IBM COBOL natively, so the port would be more or less trivial. Cost effective as well. And as
well, it runs MicroFocus. HP/UX is a platform in decline at the moment, what with it being a direct competitor to the Alpha machines
at Compaq. AIX/pSeries is definitely on the rise, and what's more, it is one of the most well supported platforms for porting on the
planet, as well as a wonderful platform for Web Services with WebSphere. Oh yes, and a $2800 machine (new price from IBM) can handle
an astonishing workload. (The B50 model server.)

-Paul


"Shyam" <shyamsunder.puranam@digital.com> wrote in message news:3t889.20$h_5.584751@news.cpqcorp.net...
> Hi:
>
…[24 more quoted lines elided]…
>
```

##### ↳ ↳ Re: IBM COBOL to HP-UX COBOL

- **From:** "Shyam" <shyamsunder.puranam@digital.com>
- **Date:** 2002-08-19T16:21:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nW889.23$Q_5.602137@news.cpqcorp.net>`
- **References:** `<3t889.20$h_5.584751@news.cpqcorp.net> <oA889.68395$eK6.2375534@twister.austin.rr.com>`

```
Thanks Paul for your prompt response.

Is there any piece of documentation that I can refer on web? On COBOL on
HP-UX? From what I assume, the development may happen using MicroFocus
compiler. I was a bit concerned and worried whether the equivalent of Screen
Maps in IBM/CICS is Screen Section on HP-UX/COBOL.

Regds,
Shyam

"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message
news:oA889.68395$eK6.2375534@twister.austin.rr.com...
> It depends upon why you are migrating; if the goal is just to port it to a
new platform as quickly as possible, then you want to
> look into MicroFocus and using CICS (well, Transaction Server) under
HP/UX.
>
> If the goal is to move away from CICS and IBM, then yes, you will have to
recode to use another compiler or screen vendor's display
> capability.  HP has their own screen capability, and Microfocus has a more
generic screen capability and runs on many platforms.
>
> If the goal is to port it quickly and save money... well... have you
instead looked at porting to AIX and the pSeries machines?
> pSeries runs, TxServer (i.e. CICS) and IBM COBOL natively, so the port
would be more or less trivial. Cost effective as well. And as
> well, it runs MicroFocus. HP/UX is a platform in decline at the moment,
what with it being a direct competitor to the Alpha machines
> at Compaq. AIX/pSeries is definitely on the rise, and what's more, it is
one of the most well supported platforms for porting on the
> planet, as well as a wonderful platform for Web Services with WebSphere.
Oh yes, and a $2800 machine (new price from IBM) can handle
> an astonishing workload. (The B50 model server.)
>
…[3 more quoted lines elided]…
> "Shyam" <shyamsunder.puranam@digital.com> wrote in message
news:3t889.20$h_5.584751@news.cpqcorp.net...
> > Hi:
> >
> > I am a new comer to this group. Please excuse me for my ignorance and
any
> > questions that may sound very trivial.
> >
> > One of my customer is wanting to move his COBOL applications from IBM to
> > HP-UX. Currently he is using CICS on IBM. Though I have worked with
COBOL,
> > my knowledge is limited to Tandem NonStop platform. Hence, I do not know
> > much about compatibility of COBOL on other platforms, the semantics...
…[3 more quoted lines elided]…
> > (1) What is the compiler used on HP-UX? Does HP-UX has its own compiler?
Or
> > does it use MicroFocus or Fujitsu to compile COBOL programs?
> > (2) If I have to migrate these Screen Maps in IBM - CICS to HP-UX, can I
use
> > the Screen Section on HP-UX? Are there any restrictions on using it? Can
any
> > one please direct me to some documentation of COBOL on HP-UX.
> > (3) Are there any specific compiler directives I need to use on HP-UX? I
…[10 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: IBM COBOL to HP-UX COBOL

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-08-19T16:45:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qg989.68411$eK6.2380439@twister.austin.rr.com>`
- **References:** `<3t889.20$h_5.584751@news.cpqcorp.net> <oA889.68395$eK6.2375534@twister.austin.rr.com> <nW889.23$Q_5.602137@news.cpqcorp.net>`

```
This is the only thing I have bookmarked.

http://devresource.hp.com/STK/crossplatform.html

Note that the Microfocus compiler itself can be ran on any platform; all you need for the HP./UX is the runtimes. Also, you should
probably contact both HP and Microfocus directly about the latest licensing policies.

Now, you should realize that porting from BMS maps to a typical screen section COBOL is
NOT going to be easy. Most CICS programs are written in PsuedoConversational mode for efficiency.
MicroFocus COBOL will not support that method of programming.

<grin> Do not say you were not warned of this. :)

-Paul


"Shyam" <shyamsunder.puranam@digital.com> wrote in message news:nW889.23$Q_5.602137@news.cpqcorp.net...
> Thanks Paul for your prompt response.
>
…[72 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: IBM COBOL to HP-UX COBOL

_(reply depth: 4)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2002-08-20T14:27:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d62502b.2570676@news.epix.net>`
- **References:** `<3t889.20$h_5.584751@news.cpqcorp.net> <oA889.68395$eK6.2375534@twister.austin.rr.com> <nW889.23$Q_5.602137@news.cpqcorp.net> <qg989.68411$eK6.2380439@twister.austin.rr.com>`

```
Paul:

We have conversion tools which will automatically convert the BMS map
to COBOL sp2 GUI screens, but you are absolutely correct in that the
procedural code to display the screens must be modified to operate in
a conversational mode.

We have a few consulting affiliates who have assisted in CICS
conversions.  I think that they can assist Shyam with his project.

This approach would also provide them with many more choices.

They could convert the application to run:

- in HP-UX character mode (ASCII terminal display)
- on an HP-UX server displaying screens on a remote PC through a
Win32 GUI thin client
- on an HP-UX server displaying screens on a remote PC through a web
browser

We have found that not all companies want to run their user interface
environment through a web browser.  Sometimes the web browser is a
"less than ideal" user interface environment.

More choices are always better.

"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote:

>This is the only thing I have bookmarked.
>
…[91 more quoted lines elided]…
>


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: IBM COBOL to HP-UX COBOL

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2002-08-20T14:17:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d624ef4.2260380@news.epix.net>`
- **References:** `<3t889.20$h_5.584751@news.cpqcorp.net>`

```
Shyam:

We have a number of independent consulting affiliates who can assist
you in converting the CICS application to run under HP-UX.

Please contact me directly and I will notify our independent
consultants of the opportunity.

"Shyam" <shyamsunder.puranam@digital.com> wrote:

>Hi:
>
…[24 more quoted lines elided]…
>


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: IBM COBOL to HP-UX COBOL

- **From:** g.friedrich@fiuka.de (Friedrich)
- **Date:** 2002-08-22T23:21:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcfdd616.0208222221.326b7a45@posting.google.com>`
- **References:** `<3t889.20$h_5.584751@news.cpqcorp.net>`

```
"Shyam" <shyamsunder.puranam@digital.com> wrote in message news:<3t889.20$h_5.584751@news.cpqcorp.net>...
> Hi:
> 
…[17 more quoted lines elided]…
> find -lFutil and then -lcob. (really my efforts were futile)

Did you try PERCobol from www.legacyj.com ?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
