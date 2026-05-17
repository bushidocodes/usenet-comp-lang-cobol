[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Date Routine

_3 messages · 3 participants · 1998-06_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k) · [`Date and calendar processing`](../topics.md#dates)

---

### Date Routine

- **From:** "kevin123" <ua-author-17075402@usenetarchives.gap>
- **Date:** 1998-06-04T09:28:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6l67d2$sf2$1@news7.ispnews.com>`

```

We are running Open VMS 6.2 on a DEC ALPHA 300.
A COBOL program using the statement "ACCEPT x from DATE"
results in x=YYMMDD. My question is does using the reserved
word DATE force the program to get the DATE form VMS. If
not where is DATE coming from.
Thanks for any suggestions,
Kevin
```

#### ↳ Re: Date Routine

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1998-06-04T12:27:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-92bab2afec-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6l67d2$sf2$1@news7.ispnews.com>`
- **References:** `<6l67d2$sf2$1@news7.ispnews.com>`

```

In article <6l67d2$sf2$1.··.@new··s.com>,
Kevin123 wrote:
› We are running Open VMS 6.2 on a DEC ALPHA 300.  
› A COBOL program using the statement "ACCEPT x from DATE" 
…[4 more quoted lines elided]…
› Kevin

This is the standard form for obtaining the current system
date from the OS in any Cobol program.
```

#### ↳ Re: Date Routine

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1998-06-04T13:14:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-92bab2afec-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6l67d2$sf2$1@news7.ispnews.com>`
- **References:** `<6l67d2$sf2$1@news7.ispnews.com>`

```

The standard requires that the data be in YYMMDD form and that it
comes from the system (it must be accurate). Therefore, I would
assume it comes from VMS. If you want a 4-digit year use the
intrinsic function CURRENT-DATE.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, NCITS J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
don··.@tan··m.com
No clever quotes here
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
