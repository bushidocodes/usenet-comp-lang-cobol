[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Signed Numbers

_2 messages · 2 participants · 1998-12_

---

### Signed Numbers

- **From:** The Chameleon <sarvec@letterbox.com>
- **Date:** 1998-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3687F6D6.6A5B@letterbox.com>`

```
I think I found the answer to my last post.
ANNUAL is in working storage as a 01 level, specifically it is:

 01  annual             pic S9(6)   value zeros.
and PR_ANNUAL is in: 
 01  ws-output-record.
     05  pr-name      pic x(22).
     05  filler       pic x(6).
     05  pr-stat      pic x(7).
     05  filler       pic x(8).
     05  pr-hourly    pic 9(2).99.
     05  filler       pic x(7).
     05  pr-annual    pic ---,---.99.
     05  filler       pic x.
     05  pr-asterick  pic x.
But why can't the value of pr-annual be checked as I have it here?
```

#### ↳ Re: Signed Numbers

- **From:** Warren Porter <warrenp@ASPMnetdoor.com>
- **Date:** 1998-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3687FE1D.31E7BAAE@ASPMnetdoor.com>`
- **References:** `<3687F6D6.6A5B@letterbox.com>`

```
The Chameleon wrote:

> I think I found the answer to my last post.
> ANNUAL is in working storage as a 01 level, specifically it is:
…[13 more quoted lines elided]…
> But why can't the value of pr-annual be checked as I have it here?

A very good habit to get into would be to never use a numeric edited
field except as the target of a MOVE statement, indeed some compilers
won't let you use it in any other way.  If you CAN use it, treat it as
alphanumeric e.g:  IF PR-ANNUAL > " 29,000.00" then whatever (although a
negative value of "-10,000.00" would test as true).

Warren Porter
---
Rainy Days OR Mondays Always Get Me Down.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
