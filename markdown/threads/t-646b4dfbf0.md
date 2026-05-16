[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol VSAM Error Code

_8 messages · 7 participants · 2005-03_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Cobol VSAM Error Code

- **From:** "Rick" <leng1@bigfoot.com>
- **Date:** 2005-03-20T14:05:49+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d1j265$ce6$1@mawar.singnet.com.sg>`

```
Hi,
Would appreciate if anyone could advise where can I get hold
of those VSAM Error Code manual (their error codes and their descriptions) 
??
Tks in advance :-)
```

#### ↳ Re: Cobol VSAM Error Code

- **From:** JR <nobody@dazoo.org>
- **Date:** 2005-03-20T14:22:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns961F5F5C3EC68dragonslayerdazooorg@38.144.126.79>`
- **References:** `<d1j265$ce6$1@mawar.singnet.com.sg>`

```
"Rick" <leng1@bigfoot.com> wrote in news:d1j265$ce6$1@mawar.singnet.com.sg:

> Hi,
> Would appreciate if anyone could advise where can I get hold
…[5 more quoted lines elided]…
> 

Try your friendly COBOL manual ...
```

##### ↳ ↳ Re: Cobol VSAM Error Code

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-03-20T14:57:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mbg%d.12191$DW.5910@newssvr17.news.prodigy.com>`
- **References:** `<d1j265$ce6$1@mawar.singnet.com.sg> <Xns961F5F5C3EC68dragonslayerdazooorg@38.144.126.79>`

```


"JR" <nobody@dazoo.org> wrote in message
news:Xns961F5F5C3EC68dragonslayerdazooorg@38.144.126.79...
> "Rick" <leng1@bigfoot.com> wrote in
news:d1j265$ce6$1@mawar.singnet.com.sg:
> > Would appreciate if anyone could advise where can I get hold
> > of those VSAM Error Code manual (their error codes and their
descriptions)
> >
>
> Try your friendly COBOL manual ...

If by "VSAM"  Rick is referring to the IBM brand-name product, I'm not so
sure the COBOL 'FILE STATUS'  codes are what he wants.. IIRC the VSAM
manuals contain a far more complete set of codes and
explanations..especially for the file status codes returned with a first
character of '9'.

Regardless, those codes and explanations should be 'findable' at the IBM
library web site, or even with a Google(r) or other internet search
facility.


MCM
```

###### ↳ ↳ ↳ Re: Cobol VSAM Error Code

- **From:** WilliamBrinkman@pobox.com
- **Date:** 2005-03-20T09:16:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dt4r31pcvftrfn2lmbada8daksekvc24k2@4ax.com>`
- **References:** `<d1j265$ce6$1@mawar.singnet.com.sg> <Xns961F5F5C3EC68dragonslayerdazooorg@38.144.126.79> <mbg%d.12191$DW.5910@newssvr17.news.prodigy.com>`

```
Try this manual

DFSMS/MVS Version 1 Release 5
Macro Instructions for Data Sets 
Document Number SC26-4913-04


On Sun, 20 Mar 2005 14:57:22 GMT, "Michael Mattias"
<michael.mattias@gte.net> wrote:

>
>
…[29 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol VSAM Error Code

_(reply depth: 4)_

- **From:** WilliamBrinkman@pobox.com
- **Date:** 2005-03-20T14:00:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gclr315q5ed6dahjfub2akmr5c2avnt10n@4ax.com>`
- **References:** `<d1j265$ce6$1@mawar.singnet.com.sg> <Xns961F5F5C3EC68dragonslayerdazooorg@38.144.126.79> <mbg%d.12191$DW.5910@newssvr17.news.prodigy.com> <dt4r31pcvftrfn2lmbada8daksekvc24k2@4ax.com>`

```

Try this link for z/OS version. See Chapter 4.

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/DGT2D500/CONTENTS?SHELF=EZ2ZO103&DT=20001201182343#1.4.1


On Sun, 20 Mar 2005 09:16:29 -0600, WilliamBrinkman@pobox.com wrote:

>Try this manual
>
…[39 more quoted lines elided]…
>>
```

#### ↳ Re: Cobol VSAM Error Code

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-03-20T11:42:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<113rdfe7l213u50@news.supernews.com>`
- **References:** `<d1j265$ce6$1@mawar.singnet.com.sg>`

```
Rick wrote:
> Hi,
> Would appreciate if anyone could advise where can I get hold
> of those VSAM Error Code manual (their error codes and their
> descriptions) ??
> Tks in advance :-)

Google must be broken where you are (7,390 hits from my computer).

Here's a program to print 'em out.
http://www.theamericanprogrammer.com/programming/vsamerr.html
```

#### ↳ Re: Cobol VSAM Error Code

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-03-20T22:25:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mLm%d.5785658$f47.1054675@news.easynews.com>`
- **References:** `<d1j265$ce6$1@mawar.singnet.com.sg>`

```
You have already received a number of useful replies.  However, part of the 
reason that some have been less than clear is that when posting to a COBOL 
forum, you need to specify whether you are asking for the codes (values) 
returned in
  file-status-1 (2-byte field)
     or
   file-status-2  (6-byte-field)
     or
  non-COBOL

Those in file-status-1 are documented in the IBM COBOL manuals.  Those in 
file-status-2  require you to look at the VSAM documentation.

This all seems pretty clear to me in the place that you probably should start 
looking:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3lr20/4.2.13
```

#### ↳ Re: Cobol VSAM Error Code

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-03-21T16:42:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d1mthn$svr$1@peabody.colorado.edu>`
- **References:** `<d1j265$ce6$1@mawar.singnet.com.sg>`

```

On 19-Mar-2005, "Rick" <leng1@bigfoot.com> wrote:

> Hi,
> Would appreciate if anyone could advise where can I get hold
> of those VSAM Error Code manual (their error codes and their descriptions)
> ??
> Tks in advance :-)

There used to be one at http://mvshelp.com/vsamretn.htm, but I'm not finding it
right now.   I have it printed out.

A quick Google got me:
http://www.simotime.com/vsmfsk01.htm
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
