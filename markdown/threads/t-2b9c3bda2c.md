[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Best way to convert overpunch character

_8 messages · 7 participants · 2001-02_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Best way to convert overpunch character

- **From:** "scott" <myscott@pacbell.net>
- **Date:** 2001-02-14T12:30:33-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PQBi6.1971$C92.42089@news.pacbell.net>`

```
What's the best way to convert an overpunch character?  I'm thinking of an
evaluate statement.   The file being read is a ASCII text file and I am
using Microfocus COBOL on Unix.  I seem to not be able to find any samples
on the net.

Any assistance would be greatly appreciated.

Thanks
Scott
myscott@pacbell.net
```

#### ↳ Re: Best way to convert overpunch character

- **From:** Joseph Kohler <joe_kohler@yahoo.com>
- **Date:** 2001-02-14T15:43:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A8AEDFA.589C3B4D@yahoo.com>`
- **References:** `<PQBi6.1971$C92.42089@news.pacbell.net>`

```
scott wrote:
> 
> What's the best way to convert an overpunch character?  I'm thinking of an
…[8 more quoted lines elided]…
> myscott@pacbell.net

An EVALUATE statement will work fine for this purpose.
```

#### ↳ Re: Best way to convert overpunch character

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2001-02-15T08:20:18-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xARi6.3443$Uc6.114012@news2.atl>`
- **References:** `<PQBi6.1971$C92.42089@news.pacbell.net>`

```
"scott" <myscott@pacbell.net> wrote:
> What's the best way to convert an overpunch character?

You're still using card punches?  Wow!  ;-)
```

##### ↳ ↳ Re: Best way to convert overpunch character

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-02-15T16:30:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wuTi6.2426$Bh7.208780@newsread2.prod.itd.earthlink.net>`
- **References:** `<PQBi6.1971$C92.42089@news.pacbell.net> <xARi6.3443$Uc6.114012@news2.atl>`

```

"Judson McClendon" <judmc@bellsouth.net> wrote in message
news:xARi6.3443$Uc6.114012@news2.atl...
> "scott" <myscott@pacbell.net> wrote:
> > What's the best way to convert an overpunch character?
>
> You're still using card punches?  Wow!  ;-)

So is Florida.
```

###### ↳ ↳ ↳ Re: Best way to convert overpunch character

- **From:** Liam Devlin <LiammD@optonline.net>
- **Date:** 2001-02-16T05:35:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A8CBBFD.7894F10B@optonline.net>`
- **References:** `<PQBi6.1971$C92.42089@news.pacbell.net> <xARi6.3443$Uc6.114012@news2.atl> <wuTi6.2426$Bh7.208780@newsread2.prod.itd.earthlink.net>`

```
Jerry P wrote:

> "Judson McClendon" <judmc@bellsouth.net> wrote in message
> news:xARi6.3443$Uc6.114012@news2.atl...
…[5 more quoted lines elided]…
> So is Florida.

No, they aren't. They wouldn't have had so many problems if they were
using key punches, which make a clean, chadless hole. They use punch
card ballots with voters doing the punching, another matter entirely,
and fraught with problems.

LiamD
```

###### ↳ ↳ ↳ Re: Best way to convert overpunch character

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-02-16T21:19:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lPgj6.2256$m_.245697@dfiatx1-snr1.gtei.net>`
- **References:** `<PQBi6.1971$C92.42089@news.pacbell.net> <xARi6.3443$Uc6.114012@news2.atl> <wuTi6.2426$Bh7.208780@newsread2.prod.itd.earthlink.net>`

```
Get over it, already!

Jerry P <jerryp@bisusa.com> wrote in message
news:wuTi6.2426$Bh7.208780@newsread2.prod.itd.earthlink.net...
>
> "Judson McClendon" <judmc@bellsouth.net> wrote in message
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Best way to convert overpunch character

_(reply depth: 4)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-02-16T22:33:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yUhj6.7$Xl5.1612@newsread1.prod.itd.earthlink.net>`
- **References:** `<PQBi6.1971$C92.42089@news.pacbell.net> <xARi6.3443$Uc6.114012@news2.atl> <wuTi6.2426$Bh7.208780@newsread2.prod.itd.earthlink.net> <lPgj6.2256$m_.245697@dfiatx1-snr1.gtei.net>`

```

"Michael Mattias" <michael.mattias@gte.net>

> Get over it, already!
>
But we're talking about punches over it.
```

#### ↳ Re: Best way to convert overpunch character

- **From:** Rob Lec <RobLec@cinci-rr.com>
- **Date:** 2001-02-15T19:10:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A8C29C3.4DCF8C16@cinci-rr.com>`
- **References:** `<PQBi6.1971$C92.42089@news.pacbell.net>`

```
In Microfocus you can use "$set sign(ebcdic)" or something like that to
read the overpunch data and move it to SIGN SEPARATE fields.  This
results in a two-step conversion but I've done this recently and it
works.
-------------------------------
(To reply by email, change dash to dot in address)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
