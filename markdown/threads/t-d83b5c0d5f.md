[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# POINTER alignment

_6 messages · 5 participants · 2007-02_

---

### POINTER alignment

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-02-17T09:00:51+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<er6cnn$pao$00$1@news.t-online.com>`

```
Yes, I know POINTER alignment is implementor defined however
I would like to know what various Cobol compilers do.
eg.
01   MYREC.
       03   FILLER    PIC X.
       03   MYPTR    USAGE POINTER.

MF (per default) does not align so that MYREC is
5/9 bytes depending 32/64 bit.
What do the big-iron boxes do ?

Roger
```

#### ↳ Re: POINTER alignment

- **From:** "Richard Maher" <maher_rj@hotspamnotmail.com>
- **Date:** 2007-02-17T19:03:32+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<er6jjp$o45$1@news-01.bur.connect.com.au>`
- **References:** `<er6cnn$pao$00$1@news.t-online.com>`

```
Hi Roger,

DEC COBOL will do the same (by default). Compiler qualifiers (and even *DC
SET ALIGNMENT compiler directives) can control the behaviour for
performance.

By all reports, an alignment fault on Itanium is extremely expensive so
COBOL goes out of its way to generate the code to stop this from happening.
There is at least  one that got through the net (something to do with
INDEXED BY) that is actively being bugfixed now.

Regards Richard Maher

"Roger While" <simrw@sim-basis.de> wrote in message
news:er6cnn$pao$00$1@news.t-online.com...
> Yes, I know POINTER alignment is implementor defined however
> I would like to know what various Cobol compilers do.
…[11 more quoted lines elided]…
>
```

#### ↳ Re: POINTER alignment

- **From:** "Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com>
- **Date:** 2007-02-19T08:30:36+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<erbjmr$d5l$1@nntp.fujitsu-siemens.com>`
- **References:** `<er6cnn$pao$00$1@news.t-online.com>`

```
"Roger While" <simrw@sim-basis.de> schrieb im Newsbeitrag 
news:er6cnn$pao$00$1@news.t-online.com...
> Yes, I know POINTER alignment is implementor defined however
> I would like to know what various Cobol compilers do.
…[9 more quoted lines elided]…
> Roger

Roger,
Our Compiler COBOL2000 aligns pointers to full words (390 architecture);
thus the structure MYREC will be 8 bytes long (because 01 levels are always 
aligned to double word); more on alignment details of other USAGEs can be 
found in our language manual using the index 'SYNCHRONIZED' and/or 'slack 
bytes'

Karl Kiesel
Fujitsu Siemens Computers, M�nchen
```

##### ↳ ↳ Re: POINTER alignment

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2007-02-21T11:56:05+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o5ot25jjseifcg5rmta76cak8bdghe9jm@4ax.com>`
- **References:** `<er6cnn$pao$00$1@news.t-online.com> <erbjmr$d5l$1@nntp.fujitsu-siemens.com>`

```
On Mon, 19 Feb 2007 08:30:36 +0100 "Karl Kiesel"
<Karl.Kiesel@fujitsu-siemens.com> wrote:

:>"Roger While" <simrw@sim-basis.de> schrieb im Newsbeitrag 
:>news:er6cnn$pao$00$1@news.t-online.com...
:>> Yes, I know POINTER alignment is implementor defined however
:>> I would like to know what various Cobol compilers do.
:>> eg.
:>> 01   MYREC.
:>>       03   FILLER    PIC X.
:>>       03   MYPTR    USAGE POINTER.

:>> MF (per default) does not align so that MYREC is
:>> 5/9 bytes depending 32/64 bit.
:>> What do the big-iron boxes do ?

:>Our Compiler COBOL2000 aligns pointers to full words (390 architecture);

Even if SYNC is NOT specified?

:>thus the structure MYREC will be 8 bytes long (because 01 levels are always 
:>aligned to double word); more on alignment details of other USAGEs can be 
:>found in our language manual using the index 'SYNCHRONIZED' and/or 'slack 
:>bytes'
```

###### ↳ ↳ ↳ Re: POINTER alignment

- **From:** "Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com>
- **Date:** 2007-02-21T12:46:22+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<erhbef$h71$1@nntp.fujitsu-siemens.com>`
- **References:** `<er6cnn$pao$00$1@news.t-online.com> <erbjmr$d5l$1@nntp.fujitsu-siemens.com> <3o5ot25jjseifcg5rmta76cak8bdghe9jm@4ax.com>`

```

"Binyamin Dissen" <postingid@dissensoftware.com> schrieb im Newsbeitrag

> :>Our Compiler COBOL2000 aligns pointers to full words (390 architecture);
>
> Even if SYNC is NOT specified?
>

Yes! Specification of SYNC is not necessary, and the compiler even disallows 
it in connection with USAGE POINTER (the same applies to PROGRAM-POINTER and 
OBJECT REFERENCE)

Karl Kiesel
Fujitsu Siemens Computers
```

#### ↳ Re: POINTER alignment

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-02-20T16:41:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<541f9iF1u68nrU1@mid.individual.net>`
- **References:** `<er6cnn$pao$00$1@news.t-online.com>`

```
On COBOL for VSE/ESA MYREC is 5 bytes (1 + 4).

>>> Roger While<simrw@sim-basis.de> 02/17/07 1:00 AM >>>
Yes, I know POINTER alignment is implementor defined however
I would like to know what various Cobol compilers do.
eg.
01   MYREC.
       03   FILLER    PIC X.
       03   MYPTR    USAGE POINTER.

MF (per default) does not align so that MYREC is
5/9 bytes depending 32/64 bit.
What do the big-iron boxes do ?

Roger
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
