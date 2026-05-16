[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM COBOL to support 31-digits

_4 messages · 3 participants · 2000-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### IBM COBOL to support 31-digits

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88h8m8$65$1@nntp3.atl.mindspring.net>`

```
FYI, the following was just put out in the IBM-MAIN list.  (I am positive
that I understand IBM-speak well enough to say that this isn't a
"guarantee" - but sure sounds like something in the "highly likely
category".)

" ...Depending on your timing (how soon you need it) we have relief coming
soon.  In order
to take advantage of it, you will have to run under Language Environment and
use the
newest COBOL compiler, COBOL for OS/390 & VM (5648-A25).  We are adding
support for up to 31 digit decimal numbers via APAR, probably in the first
half of 2000.  If this
will satisfy your requirement, then you need to start your run-time migration
from the
VS COBOL II run-time library (COB2LIB) to the LE run-time library (SCEERUN).
Once that is completed, you can compile any one (or all) of your programs
with COBOL for OS/390 & VM and use up to 31 digit numeric data items."
```

#### ↳ Re: IBM COBOL to support 31-digits

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uGsOBpWe$GA.274@cpmsnbbsa03>`
- **References:** `<88h8m8$65$1@nntp3.atl.mindspring.net>`

```
This is probably due to the fact that DB2 currently supports up to 31
digits.

William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:88h8m8$65$1@nntp3.atl.mindspring.net...
> FYI, the following was just put out in the IBM-MAIN list.  (I am positive
> that I understand IBM-speak well enough to say that this isn't a
…[5 more quoted lines elided]…
> to take advantage of it, you will have to run under Language Environment
and
> use the
> newest COBOL compiler, COBOL for OS/390 & VM (5648-A25).  We are adding
> support for up to 31 digit decimal numbers via APAR, probably in the first
> half of 2000.  If this
> will satisfy your requirement, then you need to start your run-time
migration
> from the
> VS COBOL II run-time library (COB2LIB) to the LE run-time library
(SCEERUN).
> Once that is completed, you can compile any one (or all) of your programs
> with COBOL for OS/390 & VM and use up to 31 digit numeric data items."
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: IBM COBOL to support 31-digits

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88hb12$n64$1@nntp3.atl.mindspring.net>`
- **References:** `<88h8m8$65$1@nntp3.atl.mindspring.net> <uGsOBpWe$GA.274@cpmsnbbsa03>`

```
(Possibly?) more important is the fact that this is the number that is being
"required" in the next COBOL Standard.  As I recall, not only does DB2
already support this, but I think PL/I has (for years?)
```

###### ↳ ↳ ↳ Re: IBM COBOL to support 31-digits

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2000-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000217234340.14751.00000173@ng-fh1.aol.com>`
- **References:** `<88hb12$n64$1@nntp3.atl.mindspring.net>`

```
Bill Klein writes ...



[snip]
>(Possibly?) more important is the fact that this is the number that is being
>"required" in the next COBOL Standard.  As I recall, not only does DB2
>already support this, but I think PL/I has (for years?)

Nah. The IBM PL/I compilers only support 15 digits, one of the areas where
COBOL has outshone PL/I for a long time. 

However, the new Visual Age PL/I for OS/390 compiler supports 31 digits if you
specify a compiler option.

Regards,





Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
