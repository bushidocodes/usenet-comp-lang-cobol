[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OS/390 V2.7, CICS TX1.2 -- help?

_6 messages · 4 participants · 2001-05_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### OS/390 V2.7, CICS TX1.2 -- help?

- **From:** "Paul Raulerson" <praul@isot.N0SPAM.com>
- **Date:** 2001-05-26T22:49:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b107a7f$0$16914@wodc7nh0.news.uu.net>`

```
I'm on a OS/390 V2.7 system with TX 1.2 installed. The problem seems to be a
mismatch between the COBOL compiler and the CICS 5.2 system at the heart of
TX, and some kind of conflict with LE code.  More information is included
below, but I could
sure use some advice on where to start looking for this problem and how to
get around it, if possible.  For what it is worth,
this program is the 10 line CICS ACCT00 sample program, modified to do a
simple SEND FROM (WS-ITEM) instead of
transmitting a map.  Any pointers or information appreciated, including
pointers to what book to look into. :)
Thanks
-Paul


The COBOL compiler is:

PP 5688-197 IBM COBOL for MVS & VM   1.2.2

The exact error is:

DFHAC2206 18:17:53 CICS1 Transaction ACCT failed with abend APC3. Updates
to local recoverable resources backed out.

and the lookup on that code is:

--------------------------------------------------------------------------
APC3

 Explanation:  An attempt to run the program failed because the program
 appeared to be defined to CICS as Language Environment/370 but no Language
 Environment/370 support was present in the system and no other language
 environment was able to run the program.

 System Action:  The transaction is abnormally terminated and the program is
 disabled.

 User Response:  Redefine the program to CICS in a language other than
 Language Environment/370.

 Module:  DFHAPLI
```

#### ↳ Re: OS/390 V2.7, CICS TX1.2 -- help?

- **From:** far@moblixnet.dk (Frank Allan Rasmussen)
- **Date:** 2001-05-27T12:13:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b10eebd.460990@news.mobilixnet.dk>`
- **References:** `<3b107a7f$0$16914@wodc7nh0.news.uu.net>`

```
On Sat, 26 May 2001 22:49:14 -0500, "Paul Raulerson"
<praul@isot.N0SPAM.com> wrote:

>I'm on a OS/390 V2.7 system with TX 1.2 installed. The problem seems to be a
>mismatch between the COBOL compiler and the CICS 5.2 system at the heart of
>TX, and some kind of conflict with LE code.

How is the program defined in RDO?
See if you can make a CEDA E G(*) PROG(xxxx) and check if the program
is defined as cobol.


Mvh
Frank Allan Rasmussen
mailto://far@mobilixnet.dk
http://www.mobilixnet.dk/~mob55192
```

#### ↳ Re: OS/390 V2.7, CICS TX1.2 -- help?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-05-27T09:33:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9er35o$o47$1@slb2.atl.mindspring.net>`
- **References:** `<3b107a7f$0$16914@wodc7nh0.news.uu.net>`

```
At one time, there was a "start up parameter" that was required to tell CICS
that LE was available/in use.  I don't think that CICS 5.2 still requires
it, but I won't swear to it.

Also, do you have all the LE *CICS* libraries in the correct DD's in your
CICS start up JCL?  These are described in the COBOL Installation Guide
(among other places).  Let me know if you need an exact reference.
```

##### ↳ ↳ Re: OS/390 V2.7, CICS TX1.2 -- help?

- **From:** "Paul Raulerson" <praul@isot.N0SPAM.com>
- **Date:** 2001-05-27T10:25:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b111dc9$0$1310@wodc7nh0.news.uu.net>`
- **References:** `<3b107a7f$0$16914@wodc7nh0.news.uu.net> <9er35o$o47$1@slb2.atl.mindspring.net>`

```
Well, a quick browse through the bookreader files for the COBOL and CICS
installation didn't bring up anything
that I immediately recognized as being a startup parameter or a discussion
on which LE libraries to link. Would
you mind sending that reference along please?

Thanks
-Paul

"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:9er35o$o47$1@slb2.atl.mindspring.net...
> At one time, there was a "start up parameter" that was required to tell
CICS
> that LE was available/in use.  I don't think that CICS 5.2 still requires
> it, but I won't swear to it.
…[10 more quoted lines elided]…
> > I'm on a OS/390 V2.7 system with TX 1.2 installed. The problem seems to
be
> a
> > mismatch between the COBOL compiler and the CICS 5.2 system at the heart
> of
> > TX, and some kind of conflict with LE code.  More information is
included
> > below, but I could
> > sure use some advice on where to start looking for this problem and how
to
> > get around it, if possible.  For what it is worth,
> > this program is the 10 line CICS ACCT00 sample program, modified to do a
…[13 more quoted lines elided]…
> > DFHAC2206 18:17:53 CICS1 Transaction ACCT failed with abend APC3.
Updates
> > to local recoverable resources backed out.
> >
…[12 more quoted lines elided]…
> >  System Action:  The transaction is abnormally terminated and the
program
> is
> >  disabled.
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OS/390 V2.7, CICS TX1.2 -- help?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-05-27T20:40:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9esa9e$nri$1@nntp9.atl.mindspring.net>`
- **References:** `<3b107a7f$0$16914@wodc7nh0.news.uu.net> <9er35o$o47$1@slb2.atl.mindspring.net> <3b111dc9$0$1310@wodc7nh0.news.uu.net>`

```
Check out

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ceea5100/8.0?

and the following "subsections" which deal with

"8.0 Chapter 8. Making Language Environment Available under CICS"
```

###### ↳ ↳ ↳ Re: OS/390 V2.7, CICS TX1.2 -- help?

_(reply depth: 4)_

- **From:** Gilbert Saint-Flour <gsf@home.net>
- **Date:** 2001-05-28T21:09:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b12be68$3$tfs$mr2ice@news>`
- **References:** `<3b107a7f$0$16914@wodc7nh0.news.uu.net> <9er35o$o47$1@slb2.atl.mindspring.net> <3b111dc9$0$1310@wodc7nh0.news.uu.net> <9esa9e$nri$1@nntp9.atl.mindspring.net>`

```
On 27 May 2001 at 20:40, "William M. Klein" <wmklein@nospam.ix.netcom.com> said:

> http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ceea5100/8.0?

>"8.0 Chapter 8. Making Language Environment Available under CICS"

This section may date back to the early days of LE/370 and I find it quite misleading.  On most of today's OS/390 systems, LE is already in LPA (SCEELPA) and link-list (SCEERUN) and SCEERUN should NOT be added to the CICS STEPLIB.  No wonder the CICS STEPLIBs of so many OS/390 installations contain SCEERUN, which causes duplicate copies of huge modules (e.g. CEEPLPKA) to be loaded in private memory, wasting megabytes of real memory.  Also, it is unclear why SCEERUN has to be present both in the normal search (STEPLIB/LPA/LNKLST) _and_ in DFHRPL.

 Gilbert Saint-flour
 Automated Migration Services
 http://members.home.net/gsf/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
