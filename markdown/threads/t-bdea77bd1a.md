[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Validating e-mail !!

_4 messages · 4 participants · 2003-11_

---

### Validating e-mail !!

- **From:** "Jagster" <jnori@bigfoot.com>
- **Date:** 2003-11-08T12:13:08+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pGVqb.5568$ws.537659@news02.tsnz.net>`

```
i am writing code in COBOL II to run on OS/390 to validate an e-mail
address. Any ideas how this can be done in the best way. I have an environ
of CICS/COBOL/DB2.

As of now I have an Inspect statement to count for @ character. If the count
is one then I am accepting the e-mail id.

Any body who can enlighten me more on this topic.

Jagster
```

#### ↳ Re: Validating e-mail !!

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-11-07T18:48:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0311071848.7aac23d8@posting.google.com>`
- **References:** `<pGVqb.5568$ws.537659@news02.tsnz.net>`

```
"Jagster" <jnori@bigfoot.com> wrote 

> As of now I have an Inspect statement to count for @ character. If the count
> is one then I am accepting the e-mail id.

valid EMail addresses may be for example: "My name <user@domain>".

Checking for one and only one @ sign and at least one '.' following
that (in the domain name) is about all you do unless you access to a
DNS server to do a domain name lookup.
 
> Any body who can enlighten me more on this topic.

Use Google and do a search for, say, "email address validation".
```

#### ↳ Re: Validating e-mail !!

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-11-08T22:16:11+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<unjqqvsf7breki4aolse8obcmhoi4ufnb0@4ax.com>`
- **References:** `<pGVqb.5568$ws.537659@news02.tsnz.net>`

```
On Sat, 8 Nov 2003 12:13:08 +1300 "Jagster" <jnori@bigfoot.com> wrote:

:>i am writing code in COBOL II to run on OS/390 to validate an e-mail
:>address. Any ideas how this can be done in the best way. I have an environ
:>of CICS/COBOL/DB2.

:>As of now I have an Inspect statement to count for @ character. If the count
:>is one then I am accepting the e-mail id.

:>Any body who can enlighten me more on this topic.

http://www.faqs.org/rfcs/rfc2822.html
```

#### ↳ Re: Validating e-mail !!

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-11-10T22:11:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-52CB85.22115810112003@corp.supernews.com>`
- **References:** `<pGVqb.5568$ws.537659@news02.tsnz.net>`

```
In article <pGVqb.5568$ws.537659@news02.tsnz.net>,
 "Jagster" <jnori@bigfoot.com> wrote:

> i am writing code in COBOL II to run on OS/390 to validate an e-mail
> address. Any ideas how this can be done in the best way. I have an environ
…[7 more quoted lines elided]…
> Jagster

Contact the hosting mail server and issue a EXPN command.  There are 
cases where you might encounter many @ signs in a valid email address.  
Though they get rarer each year, it is still a valid way to describe a 
path.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
