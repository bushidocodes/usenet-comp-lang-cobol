[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# compiles done in wrong order

_6 messages · 5 participants · 1999-02_

---

### compiles done in wrong order

- **From:** Tim Estle <tje666@nwc.net>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36C87699.30BDD4@nwc.net>`

```
On an MVS platform are there any tools to audit your load libraries to
check if compiles were done in the wrong order? This would detect a
problem with static calls. Are there any configuration management tools
that can prevent this?  Have y2k project managers paid any attention to
this? It would be easy to do a mass compile in alphabetical order and
include the wrong version of a subprogram.
```

#### ↳ Re: compiles done in wrong order

- **From:** Roland Schiradin <schiradi@tap.de>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36C8A098.D33A76D8@tap.de>`
- **References:** `<36C87699.30BDD4@nwc.net>`

```
Tim,

> On an MVS platform are there any tools to audit your load libraries to
> check if compiles were done in the wrong order? This would detect a
> problem with static calls.

We don't allow static calls on application level only for Standard-SW
(CICS,DB2,MQ and so on)


> Are there any configuration management tools that can prevent this?

SCLM can do this, but u have to add your application-structure via
ARCHDEF-Members
Note that big application (e.g. > 2000 programs) can take a long
BUILD/PROMOTE


Roland
```

##### ↳ ↳ Re: compiles done in wrong order

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36C97084.DE2FD50@zip.com.au>`
- **References:** `<36C87699.30BDD4@nwc.net> <36C8A098.D33A76D8@tap.de>`

```
Roland Schiradin wrote:
> 
> 
…[4 more quoted lines elided]…
> 

There is a utility that can draw out the archdef's out from existing
load modules so building the basic ARCHDEF is OK but the set up is a
pain.  I am using Endevour and I really cannot see the justification for
the cost (yet). It does not seem to work as well as SCLM which is free
with MVS.
```

###### ↳ ↳ ↳ Re: compiles done in wrong order

- **From:** Roland Schiradin <schiradi@tap.de>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36CB3792.1E0990F@tap.de>`
- **References:** `<36C87699.30BDD4@nwc.net> <36C8A098.D33A76D8@tap.de> <36C97084.DE2FD50@zip.com.au>`

```
Ken,

> There is a utility that can draw out the archdef's out from existing
> load modules so building the basic ARCHDEF is OK but the set up is a
> pain.

Never heard of it before, would u pls so kind and send me more info.
I worked with VMLIB, LIBR., SCLM and Endevor. SCLM is my favourit
Endevour is very expensive and now owned by CA.

Roland
```

#### ↳ Re: compiles done in wrong order

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36C87CA9.D77B07F9@NOSPAMhome.com>`
- **References:** `<36C87699.30BDD4@nwc.net>`

```
Tim Estle wrote:
> 
> On an MVS platform are there any tools to audit your load libraries to
…[4 more quoted lines elided]…
> include the wrong version of a subprogram.

If all of the programs are frozen, wouldn't recompiling everything - in
any order - solve this problem?  I haven't had experience with more than
2 layers (and don't do static calls anyway).
```

##### ↳ ↳ Re: compiles done in wrong order

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FEDFD8C5DA096B9B.28632C1BB0272F5F.C2BF399B776545F2@library-proxy.airnews.net>`
- **References:** `<36C87699.30BDD4@nwc.net> <36C87CA9.D77B07F9@NOSPAMhome.com>`

```
On Mon, 15 Feb 1999 12:59:37 -0700, Howard Brazee
<brazee@NOSPAMhome.com> enlightened us:

>Tim Estle wrote:
>> 
…[9 more quoted lines elided]…
>2 layers (and don't do static calls anyway).

The only thing I know of is a source librarian product called
Endeavor.  There are features in it that would allow the user to
dictate what is compiled and in which order.  

HTH

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Middle age is when you choose your cereal for the
fiber, not the toy.

 Steve
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
