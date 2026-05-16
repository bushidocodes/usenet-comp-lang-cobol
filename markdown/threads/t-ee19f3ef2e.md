[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cobol COMP Format

_6 messages · 5 participants · 1998-12_

---

### cobol COMP Format

- **From:** Sabahattin@t-online.de (Sabahattin Kunas)
- **Date:** 1998-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<368926F9.447AFC10@t-online.de>`

```
Who can help me, with COBOL COMP format. I want to a COMP format in a
text-File in the binary Format
example:
 PIC 9(16) 9(3) how long is this as String
```

#### ↳ Re: cobol COMP Format

- **From:** docdwarf@clark.net ()
- **Date:** 1998-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76b9ci$kje$1@clarknet.clark.net>`
- **References:** `<368926F9.447AFC10@t-online.de>`

```
In article <368926F9.447AFC10@t-online.de>,
Sabahattin Kunas <Sabahattin@t-online.de> wrote:
>Who can help me, with COBOL COMP format. I want to a COMP format in a
>text-File in the binary Format
>example:
> PIC 9(16) 9(3) how long is this as String

Please do your own homework.

DD
```

##### ↳ ↳ Re: cobol COMP Format

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76bbbh$f0o@sjx-ixn6.ix.netcom.com>`
- **References:** `<368926F9.447AFC10@t-online.de> <76b9ci$kje$1@clarknet.clark.net>`

```

docdwarf@clark.net wrote in message <76b9ci$kje$1@clarknet.clark.net>...
>In article <368926F9.447AFC10@t-online.de>,
>Sabahattin Kunas <Sabahattin@t-online.de> wrote:
…[8 more quoted lines elided]…
>

And/or check DejaNews - where this exact topic is discussed about once a
month
```

#### ↳ Re: cobol COMP Format

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<94ai2.3615$9H6.3511596@news4.mia>`
- **References:** `<368926F9.447AFC10@t-online.de>`

```
Sabahattin Kunas wrote:
>Who can help me, with COBOL COMP format. I want to a COMP format in a
>text-File in the binary Format
>example:
> PIC 9(16) 9(3) how long is this as String

The format of COMP items is compiler dependent.  Frequently it is
binary.  In general, you can not/should not place COMP items in a
text file.  This is because COMP items can contain  binary values which
could be mistaken for control characters.  Your PIC above is in error.
I assume you intended either 9(16)V9(3) or 9(16).9(3), both of which
are invalid, because the current COBOL 85 limit is 18 numeric digits.
However, if you intended 9(16) and 9(3) as separate fields, then, of
course, the first is 16 bytes and the second is three bytes.  COBOL
terminology is 'display' not 'string'.  We say a field is 'display'
or 'comp'.
```

#### ↳ Re: cobol COMP Format

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76bbac$eus@sjx-ixn6.ix.netcom.com>`
- **References:** `<368926F9.447AFC10@t-online.de>`

```

Sabahattin Kunas wrote in message <368926F9.447AFC10@t-online.de>...
>Who can help me, with COBOL COMP format. I want to a COMP format in a
>text-File in the binary Format
>example:
> PIC 9(16) 9(3) how long is this as String

My new year's resolution is to FINALLY update the FAQ (including the new
books mentioned in the newsgroup).  I PROMISE to have a section on   "Why
COMP is compiler dependent"  - I promise!
```

##### ↳ ↳ Re: cobol COMP Format

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<368937D9.87921D3E@home.com>`
- **References:** `<368926F9.447AFC10@t-online.de> <76bbac$eus@sjx-ixn6.ix.netcom.com>`

```
William M. Klein wrote:
> 
> Sabahattin Kunas wrote in message <368926F9.447AFC10@t-online.de>...
…[7 more quoted lines elided]…
> COMP is compiler dependent"  - I promise!

It might be nice to briefly define various other compiler dependent
COMP-X types, and if you are really ambitious, a few samples of how
internal signs can vary (I remember converting from Mainframe IBM DOS to
Mainframe IBM OS by moving numbers back and forth to work fields to get
their unsigned signs correct!!!)

I supose with compiler dependent internal representations it may be
useful to mention the differences between coding schemes including
double byte vs Unicode etc, and their different sort problems.  Boy the
more I think of compiler dependencies the more there is to think
about!!!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
