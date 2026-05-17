[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Y2k COBOL compilers for SUN solaris

_3 messages · 3 participants · 1998-05_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k) · [`Compilers and vendors`](../topics.md#compilers)

---

### Y2k COBOL compilers for SUN solaris

- **From:** "r..." <ua-author-17084195@usenetarchives.gap>
- **Date:** 1998-05-12T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6jcfhm$ann$1@bertrand.ccs.carleton.ca>`

```

We're using Microfocus COBOL v3.1 on our SUN solaris box. MF requires an
upgrade to 4.0 to gain year 2000 compliance. The only problem with upgrading
is being forced to use an Application License Server for all applications.
This adds complexity & expense for no-ones benefit but the supplier.

I'd like to investigate alternatives. One being Fujitsu. What others exist?
I have the following requirements:

o Year 2000 compliant

o Can create statically linked stand-alone rununits that don't require
a license server

o Compiler support for free form source code

o Compiler support for inline comments via the *> construct

o Compiler support for concatenation via the & symbol

o Compiler support for hexadeciomal literals via x"00" construct

Any comments/experiences appreciated.


-----------------------------------------------------------------------------
Rob McDonald Net: Rob··.@car··n.ca Phone: (613) 520-2600 ext 8351
-----------------------------------------------------------------------------
```

#### ↳ Re: Y2k COBOL compilers for SUN solaris

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1998-05-13T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0c6eb67ca-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6jcfhm$ann$1@bertrand.ccs.carleton.ca>`
- **References:** `<6jcfhm$ann$1@bertrand.ccs.carleton.ca>`

```

In message <<6jcfhm$ann$1.··.@ber··n.ca>> r.··.@lib··n.ca writes:
› upgrade to 4.0 to gain year 2000 compliance. The only problem with upgrading
› is being forced to use an Application License Server for all applications.
› This adds complexity & expense for no-ones benefit but the supplier.
What is it about the <> that is not Y2000 compliant ?
Will it just get the DATE-COMPILED wrong ? Will it auto-
detect your use of year fields and compile wrong code?

The run-time library may well have bugs in the date functions,
but if it returns invalid data from ACCEPT FROM DATE then
it is a bug they should fix.

It seems too many companies are attempting to use Y2k as
a lever to increase revenue. I believe that MS has
been loath to fix its products because it wants to sell
everyone a complete new set of software in 1999, if Win95
had been fixed they wouldn't need to replace it.

I would investigate what MF means by not Y2K compliant
and look at coding round any problems or looking at
whether 3.1 is fit for the purpose it was sold (actionable
in this country).

It is probably just the salesman trying to spook some
revenue (and his commission).
```

#### ↳ Re: Y2k COBOL compilers for SUN solaris

- **From:** "fujitsu software corporation" <ua-author-6588898@usenetarchives.gap>
- **Date:** 1998-05-13T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0c6eb67ca-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6jcfhm$ann$1@bertrand.ccs.carleton.ca>`
- **References:** `<6jcfhm$ann$1@bertrand.ccs.carleton.ca>`

```

Rob,

Fujitsu COBOL on Solaris fully supports you list of requirements and it also
generates the fastest and most reliable code of any other COBOL compiler.

Fujitsu designs and manufacturers more SPARC chips than any other company
and we are committed to maintaining the fastest and most reliable set of
compilers for SPARC including COBOL, C, C++, Fortran, and Java.

Fujitsu Software Corporation
Developer Tools Group
Phone: (408) 428-0500
FAX: (408) 428-0600
Email: co··.@adt··s.com
Web: www.adtools.com


Rob McDonald wrote in message <6jcfhm$ann$1.··.@ber··n.ca>...
› We're using Microfocus COBOL v3.1 on our SUN solaris box.  MF requires an
› upgrade to 4.0 to gain year 2000 compliance.  The only problem with
…[28 more quoted lines elided]…
› ---------------------------------------------------------------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
