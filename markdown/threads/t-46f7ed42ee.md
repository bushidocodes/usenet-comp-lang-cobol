[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# end of the century

_3 messages · 3 participants · 1994-12_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k)

---

### Re: end of the century

- **From:** jonesd@corp.hp.com (Dan Jones)
- **Date:** 1994-12-07T15:31:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c4kfr$nqt@hpscit.sc.hp.com>`

```
Days since a specified date is a great solution, but
how can I expect my users to enter in new dates (ie. 
updates to existing records)? For example, if my user
enters in 010100 how do I know that they mean 01/01/1900
or 01/01/2000. I have a distributed legacy system that
is not having any more releases. Dates are entered in 
this system as MMDDYY this can not change.

Any great suggestions......

Daniel
***********************
Daniel Jones
Hewlett Packard Company
jonesd@corp.hp.com
***********************
```

#### ↳ Re: end of the century

- **From:** mgphl@crl.com (Michael G. Phillips)
- **Date:** 1994-12-07T18:41:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c5ro5$9e6@crl3.crl.com>`
- **References:** `<3c4kfr$nqt@hpscit.sc.hp.com>`

```
Dan Jones (jonesd@corp.hp.com) wrote:
: Days since a specified date is a great solution, but
: how can I expect my users to enter in new dates (ie. 
: updates to existing records)? For example, if my user
: enters in 010100 how do I know that they mean 01/01/1900
: or 01/01/2000. I have a distributed legacy system that
: is not having any more releases. Dates are entered in 
: this system as MMDDYY this can not change.

: Any great suggestions......

	This is *totally* dependant upon the application.
	Do your users currently enter dates for 1900?
                      ~~~~~~~~~                 ~~~~
	If not, use some contrived rule to decide when
	it's 19xx and when it's 20xx.

	If you *do* use that wide of a date range, time
	to shop for a new distributed "legacy" system..  ;-)

	-michael "who still prefers *months* since a date" phillips

: Daniel
: ***********************
: Daniel Jones
: Hewlett Packard Company
: jonesd@corp.hp.com
: ***********************
```

##### ↳ ↳ Re: end of the century

- **From:** harrym@netcom.com (Harry Myhre)
- **Date:** 1994-12-09T14:14:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<harrym.1137370121A@192.0.2.3>`
- **References:** `<3c4kfr$nqt@hpscit.sc.hp.com> <3c5ro5$9e6@crl3.crl.com>`

```
In Article <3c5ro5$9e6@crl3.crl.com>, mgphl@crl.com (Michael G. Phillips) wrote:

>        If not, use some contrived rule to decide when
>        it's 19xx and when it's 20xx.

A friend and I at work had to write a routine like this a few years ago.  We
have a file that carries year in a key, but not decade.  You look at the
current date and then predict what the decade would be for the key in
question.  It's all based on the fact that records in this particular file
are purged on a regular basis, so we never (crossing fingers) come across
ten year old records.
---
* Harry Myhre <harrym@netcom.com>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
