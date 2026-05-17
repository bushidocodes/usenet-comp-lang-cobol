[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help!! extremely needed in reports

_2 messages · 2 participants · 1995-03 → 1995-04_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help!! extremely needed in reports

- **From:** "sam..." <ua-author-106019@usenetarchives.gap>
- **Date:** 1995-03-31T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lkmo3$eba@newsbf02.news.aol.com>`

```
Iam very new to programming and studying things by myself. can anyone help
in creating a report eg. sales, for a time period such as from april 7 to
may 7 ... and Iam doing this in COBOL 85. In my program I accept the
system date as the date of entry ie today-date. I reffered few books but
could not come out successfully. Any help will be very much appreciated.
thanks
sb
```

#### ↳ Re: Help!! extremely needed in reports

- **From:** "marty..." <ua-author-17073867@usenetarchives.gap>
- **Date:** 1995-04-01T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cdacef52e0-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3lkmo3$eba@newsbf02.news.aol.com>`
- **References:** `<3lkmo3$eba@newsbf02.news.aol.com>`

```

› I am very new to programming and studying things by myself.  Can
› anyone help in creating a report eg. sales,  for a time period such
…[3 more quoted lines elided]…
› successfully.  Any help will be very much appreciated.

Your question is far too vague. I suspect that this is why you are
having trouble writing the program.
My advice:
State your problem more clearly.

Example:
Print a monthly sales report from transaction file. Select
transactions as follows:
If today's date is after the 7th of the month, select
transactions between 8th of previous month and 7th of
current month; otherwise, select transactions between
8th of 2nd previous month to 7th of previous month.
Note that you will have an additional processing requirement at the
beginning of the year.

If you have learned pseudo-code [also called HIPO], trying coding
in that format first.

Remember, that the computer is a fast, consistent IDIOT!
It will do preCISEly (and ONLY) what you tell it.



Copyright 1995, META Consulting Group. All rights reserved. May be
freely copied or otherwise transmitted on computer networks provided
that no additional fee for reading this specific work is charged.
---
* SLMR 2.1a * DWIM -- Do what I +mean+
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
