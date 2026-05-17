[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM COBOL compiler for AIX?

_8 messages · 7 participants · 1995-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### IBM COBOL compiler for AIX?

- **From:** "7477..." <ua-author-17088036@usenetarchives.gap>
- **Date:** 1995-04-12T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3mkc0v$4rp$1@mhade.production.compuserve.com>`

```
I heard a rumor that there was a IBM COBOL compiler for AIX.

Is there any substance to this rumor? and if so what are some

of the bigger issues in porting Micro Focus COBOL to it?



Thanks in advance...
```

#### ↳ Re: IBM COBOL compiler for AIX?

- **From:** "mg..." <ua-author-10778203@usenetarchives.gap>
- **Date:** 1995-04-14T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2ffbd955e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3mkc0v$4rp$1@mhade.production.compuserve.com>`
- **References:** `<3mkc0v$4rp$1@mhade.production.compuserve.com>`

```
Russell Miller (747··.@Com··e.COM) wrote:
: I heard a rumor that there was a IBM COBOL compiler for AIX.

Not rumor - its *true*

: Is there any substance to this rumor? and if so what are some
: of the bigger issues in porting Micro Focus COBOL to it?

I think the AIX COBOL *is* MF's COBOL!
(but that could be a rumor... ;-)

-michael


: Thanks in advance...
   --------------------------------------------------------------------
   Michael G. Phillips    mg··.@c··.com     mg··.@atl··e.com
   (404)239-2766  "Just because it worked doesn't mean it works." -- me
```

##### ↳ ↳ Re: IBM COBOL compiler for AIX?

- **From:** "crookie" <ua-author-17071740@usenetarchives.gap>
- **Date:** 1995-04-16T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2ffbd955e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c2ffbd955e-p2@usenetarchives.gap>`
- **References:** `<3mkc0v$4rp$1@mhade.production.compuserve.com> <gap-c2ffbd955e-p2@usenetarchives.gap>`

```
› mg··.@c··.com (Michael G. Phillips) wrote:
› I think the AIX COBOL *is* MF's COBOL!
› (but that could be a rumor... ;-)

'tis true.
```

##### ↳ ↳ Re: IBM COBOL compiler for AIX?

- **From:** "uni..." <ua-author-17087899@usenetarchives.gap>
- **Date:** 1995-04-23T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2ffbd955e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c2ffbd955e-p2@usenetarchives.gap>`
- **References:** `<3mkc0v$4rp$1@mhade.production.compuserve.com> <gap-c2ffbd955e-p2@usenetarchives.gap>`

```
In article <3mpu8f$1.··.@crl··l.com> mg··.@c··.com (Michael G. Phillips) writes:
› Russell Miller (747··.@Com··e.COM) wrote:
› : I heard a rumor that there was a IBM COBOL compiler for AIX.
…[9 more quoted lines elided]…
› -michael

You are correct, the IBM COBOL compiler for AIX is MicroFocus Cobol, but it
usually runs a few upgrades behind. If you need that fix - the best one to
buy is MicroFocus Cobol.
```

###### ↳ ↳ ↳ Re: IBM COBOL compiler for AIX?

- **From:** "peter withey" <ua-author-7666742@usenetarchives.gap>
- **Date:** 1995-04-24T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2ffbd955e-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c2ffbd955e-p4@usenetarchives.gap>`
- **References:** `<3mkc0v$4rp$1@mhade.production.compuserve.com> <gap-c2ffbd955e-p2@usenetarchives.gap> <gap-c2ffbd955e-p4@usenetarchives.gap>`

```
uni··.@gds··n.com (Bobbi McDermott) wrote:

I think the AIX COBOL *is* MF's COBOL!
(but that could be a rumor... ;-)

› You are correct, the IBM COBOL compiler for AIX is MicroFocus Cobol, but it
› usually runs a few upgrades behind. If you need that fix - the best one to
› buy is MicroFocus Cobol.

For those who are interested, Acucobol runs on AIX also.
1-800-COBOL85.
```

#### ↳ Re: IBM COBOL compiler for AIX?

- **From:** "pah..." <ua-author-13876471@usenetarchives.gap>
- **Date:** 1995-04-18T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2ffbd955e-p6@usenetarchives.gap>`
- **In-Reply-To:** `<3mkc0v$4rp$1@mhade.production.compuserve.com>`
- **References:** `<3mkc0v$4rp$1@mhade.production.compuserve.com>`

```
Russell Miller (747··.@Com··e.COM) wrote:
: I heard a rumor that there was a IBM COBOL compiler for AIX.
: Is there any substance to this rumor? and if so what are some
: of the bigger issues in porting Micro Focus COBOL to it?

: Thanks in advance...

As far as I know, the IBM Cobol compiler for AIX is the MF front-end
coupled to an IBM-built back-end. This compiler was released as
version 1.3, and corresponded to MF Cobol 3.0. The back-end
generated better code than the pure MF version, but IBM no longer
supports this version. You can only get the current MF COBOL 3.2
from MF. Again, take this as here-say; maybe someone from MF can
confirm me.
```

##### ↳ ↳ Re: IBM COBOL compiler for AIX?

- **From:** "crookie" <ua-author-17071740@usenetarchives.gap>
- **Date:** 1995-04-23T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2ffbd955e-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c2ffbd955e-p6@usenetarchives.gap>`
- **References:** `<3mkc0v$4rp$1@mhade.production.compuserve.com> <gap-c2ffbd955e-p6@usenetarchives.gap>`

```
› pah··.@eu··t.be (Pieter Hintjens) wrote: 
› 
…[6 more quoted lines elided]…
› confirm me. 

most of this is pretty much spot-on.

however, i don't understand your reference to the IBM back-end code
being better than the MF version. at this point in time there was no
MF back-end for the RS/6000, so what are you comparing it to ?

nowadays, the MF COBOL 3.2 for AIX has a MF implemented code generator
which significantly outperforms the IBM version in almost _all_ (if not,
all!) areas.
```

#### ↳ Re: IBM COBOL compiler for AIX?

- **From:** "jts..." <ua-author-12520169@usenetarchives.gap>
- **Date:** 1995-04-20T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2ffbd955e-p8@usenetarchives.gap>`
- **In-Reply-To:** `<3mkc0v$4rp$1@mhade.production.compuserve.com>`
- **References:** `<3mkc0v$4rp$1@mhade.production.compuserve.com>`

```
On Fri, 21 Apr 1995 11:40:15 GMT, Jonathan Edwards (edw··.@wor··d.com) wrote:
› In article <3mkc0v$4rp$1.··.@mha··e.com>,
› Russell Miller  <747··.@Com··e.COM> wrote:
›› I heard a rumor that there was a IBM COBOL compiler for AIX.
 
› IBM announced last fall their intention to deliver a new Cobol product
› on OS/2, AIX, and MVS (and other platforms eventually).
…[6 more quoted lines elided]…
› be a unique feature.
 
› You can probably find the announcement letter somewhere on www.ibm.com.

The correct URL for IBM announcements is: http://www.ibmlink.ibm.com/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
