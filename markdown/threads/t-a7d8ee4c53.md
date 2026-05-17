[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Date malfuntion after the year 2000

_2 messages · 2 participants · 1997-07_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k) · [`Date and calendar processing`](../topics.md#dates)

---

### Date malfuntion after the year 2000

- **From:** "chad winesburg" <ua-author-17071358@usenetarchives.gap>
- **Date:** 1997-07-22T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33D6E038.7937@columbia.dsu.edu>`

```

In early 1959, a new programming language was mainly being developed by
Dr. Grace Hopper, commander in the Navy, other academic intitutions, and
computer manufacturers. This resulted in the organization of CODASYL
(COnference on DAta SYstems Languages. A beginning era of commercial
programming.
With three versions of Cobol that were adopted up to 1985, (ANSI-68,
ANSI-74, ANSI-85), not one could would be able to carry on a system
date after midnight on January 1, 2000. I would like to know why with
such a sophisticated developement team that this was not achieved yet by
1985? Was it because of the doubts of COBOL keeping up in the market or
what?
```

#### ↳ Re: Date malfuntion after the year 2000

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1997-07-23T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a7d8ee4c53-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33D6E038.7937@columbia.dsu.edu>`
- **References:** `<33D6E038.7937@columbia.dsu.edu>`

```

In message <<33D··.@col··u.edu>> Chad Winesburg writes:

› ANSI-74, ANSI-85), not one could would be able to carry on a system 
› date after midnight on January 1, 2000.  I would like to know why with 
› such a sophisticated developement team that this was not achieved yet by 
› 1985?  Was it because of the doubts of COBOL keeping up in the market or 
› what?

In what way do you think that Cobol 'would not be able to carry on
a system date after ... ' ?

Certainly the ACCEPT FROM DATE only provides a 2 digit year, but
no one ever got confused and thought that the computer date was,
say, 1897. Why do you think it impossible to deal with year 00
in a sensible way ?

The issue has actually nothing to do with the Cobol language, but
is entirely related to the handling of 2 digit years. Does your
cheque book have '19' preprinted in the date field ? will this
mean that you can't write a cheque after 31 Dec 1999 ? In C
there will be program that printf("... 19%2d ...", ... year);
because they deal with years withing this century.

But in any case you are incorrect, the intrinsic function
CURRENT-DATE returns a 4 digit year for those who would find
it confusing to deal with year 00 in case it amy actually be
the year 1900.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
