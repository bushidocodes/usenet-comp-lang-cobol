[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question about indexed file processing

_5 messages · 5 participants · 1997-05 → 1997-07_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Question about indexed file processing

- **From:** "de..." <ua-author-15200713@usenetarchives.gap>
- **Date:** 1997-05-26T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5memkl$nk8@preeda.internex.net.au>`

```

Hi all,

I'm new at cobol programming.....obviously.

If I have an indexed file with invoice-no as the key and cust-no as an
alternate with duplicates, how do I read the file using the alternate key and
get all the records.

I have tried using access is dynamic and set key = cust-no but once all the
records for a given cust-no have been actioned, all the other customer numbers
higher than the given cust-no are actioned in ascending sequence.

I also tried access is random, it reads the first record ok, but I don't know
how to then get it to read subsequent records.

Thanks in advance for any help.

Dean.
this ng or mail would be great.
de··.@con··g.au
```

#### ↳ Re: Question about indexed file processing

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1997-05-26T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f883ceac14-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5memkl$nk8@preeda.internex.net.au>`
- **References:** `<5memkl$nk8@preeda.internex.net.au>`

```

In message <<5memkl$n.··.@pre··t.au>> de··.@con··g.au writes:
› 
› I'm new at cobol programming.....obviously.
…[7 more quoted lines elided]…
› higher than the given cust-no are actioned in ascending sequence.

That is what the 'UNTIL' is for on the PERFORM.

MOVE Customer-Key TO Invoice-Customer-Key
START Invoice-File
KEY NOT > Invoice-Customer-Key
INVALID KEY
MOVE HIGH-VALUES TO Invoice-Customer-Key
END-START
PERFORM
UNTIL Invoice-Customer-Key NOT = Customer-Key

READ Invoice-File
NEXT RECORD
AT END
MOVE HIGH-VALUES TO Invoice-Customer-Key
END-READ

IF Invoice-Customer-Key = Customer-Key
.....
END-IF
END-PERFORM
```

#### ↳ Re: Question about indexed file processing

- **From:** "gtru..." <ua-author-1163276@usenetarchives.gap>
- **Date:** 1997-05-27T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f883ceac14-p3@usenetarchives.gap>`
- **In-Reply-To:** `<5memkl$nk8@preeda.internex.net.au>`
- **References:** `<5memkl$nk8@preeda.internex.net.au>`

```

On 27 May 1997 13:12:52 GMT, de··.@con··g.au (Dean) wrote:

› Hi all,
› 
…[18 more quoted lines elided]…
› 
MOVE starting-customer-name TO customer-name-key
START file KEY >= customer-name-key INVALID KEY
... you're at end of file if this happens --
END-START
* now read the file using
READ file NEXT RECORD AT END ...

George Trudeau, Town of Falmouth
```

#### ↳ Re: Question about indexed file processing

- **From:** "findit" <ua-author-874518@usenetarchives.gap>
- **Date:** 1997-07-12T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f883ceac14-p4@usenetarchives.gap>`
- **In-Reply-To:** `<5memkl$nk8@preeda.internex.net.au>`
- **References:** `<5memkl$nk8@preeda.internex.net.au>`

```

de··.@con··g.au (Dean) wrote:

:>Hi all,
:>
:>I'm new at cobol programming.....obviously.
:>
:>If I have an indexed file with invoice-no as the key and cust-no as an
:>alternate with duplicates, how do I read the file using the alternate key :>and get all the records.
:>
:>I have tried using access is dynamic and set key = cust-no but once all :>the records for a given cust-no have been actioned, all the other customer :>numbers higher than the given cust-no are actioned in ascending sequence.
:>I also tried access is random, it reads the first record ok, but I don't :>know how to then get it to read subsequent records.
This is the way to do it. Do a "start" on the alternate key then
continue by using "read next". This should follow the alternate
key till you perform a "start" on another Key.
:>
:>Thanks in advance for any help.
:>
:>Dean.
:>this ng or mail would be great.
:>de··.@con··g.au
:>

-- Siegen
----------------------
Please remove the letter "x" from my email address, should you wish
to email me.
(rod··.@com··m.au)
---------------------
```

##### ↳ ↳ Re: Question about indexed file processing

- **From:** "kevin p corkery" <ua-author-17071571@usenetarchives.gap>
- **Date:** 1997-07-14T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f883ceac14-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f883ceac14-p4@usenetarchives.gap>`
- **References:** `<5memkl$nk8@preeda.internex.net.au> <gap-f883ceac14-p4@usenetarchives.gap>`

```



Siegen wrote in article
<33c··.@new··m.au>...
› de··.@con··g.au (Dean) wrote:
› 
…[8 more quoted lines elided]…
› :>I have tried using access is dynamic and set key = cust-no but once all
:>the records for a given cust-no have been actioned, all the other
customer :>numbers higher than the given cust-no are actioned in ascending
sequence.
› :>I also tried access is random, it reads the first record ok, but I
› don't :>know how to then get it to read subsequent records.
…[12 more quoted lines elided]…
› 
A comment on Dean's original question is appropriate ... His confusion is
caused by the concept of implied scope delineation that a relational
database would have, i.e. select * from invoices where customer equal
'XXXXXXXX' ... This is not a criticism of Dean, his question, or the
response from Siegen, just an observation that COBOL-like indexed file
systems are not relational data bases, and are not being taught in schools
any longer, thus the confusion.

Kevin Corkery
Independent Consultant
Voorhees, New Jersey
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
