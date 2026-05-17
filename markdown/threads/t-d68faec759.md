[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help with a indexed file structure

_4 messages · 4 participants · 1996-07_

**Topics:** [`VSAM, files, sorting`](../topics.md#files) · [`Help requests and how-to`](../topics.md#help)

---

### Help with a indexed file structure

- **From:** "prenn..." <ua-author-17073396@usenetarchives.gap>
- **Date:** 1996-07-30T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4tol75$b9v@newsbf02.news.aol.com>`

```

I 'm hoping some of you might give me some new idea's, on a problem I'm
trying to solve . I am working on an accounts receivable system.
The transaction file contains the invoice and payment records. The
invoice number is part of the key, so the invoice and accociated
payment(s) is the next record. This is so it displays correctly and more
importantly the balance of the invoice can be established easily.
I would now like the option to list these transaction by oldest
transaction first,BUT because the payment date is usually different that
the invoice date putting the date in an alternate key won't work. Also
the other part of the key is the invoice type that is I=Invoice and
P=payment which also complicates matter. I'm thinking perhaps the
correct alternate key but not sure what that might be.

I'm hoping someone may suggest a simpler solution than some of the one's
I've dreamed up, perhaps others with a fresh look might help.

Any thoughts, Thanks in advance

Paul
```

#### ↳ Re: Help with a indexed file structure

- **From:** "haluk okur" <ua-author-1144603@usenetarchives.gap>
- **Date:** 1996-07-31T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d68faec759-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4tol75$b9v@newsbf02.news.aol.com>`
- **References:** `<4tol75$b9v@newsbf02.news.aol.com>`

```

PRenna2537 wrote:


› The transaction file contains the invoice and payment records.  The
› invoice number is part of the key, so the invoice and accociated
…[4 more quoted lines elided]…
› P=payment which also complicates matter.

Paul,

I don't know what fields your primary key contains. There must be something
else than the invoice-# and invoice-type to keep it unique. I'd put the
date in the primary key in addition to the fields mentioned above. This way
it gets unique and the records will get retrieved in order ie sorted by
invoice-# and date. I don't see a reason to put the record-type into the
primary key, however.

FD TRANSACTIONS-FILE.
01 INVOICE-RECORD.
03 PRIMARY-KEY.
05 INVOICE-NUMBER PIC ...
05 RECORD-TYPE PIC X(01).
05 INVOICE-DATE PIC X(08). (YYYYMMDD)
03 OTHER-STUFF-RELATED-TO-INVOICE.
:
01 PAYMENT-RECORD.
03 PRIMARY-KEY.
05 INVOICE-NUMBER PIC ...
05 RECORD-TYPE PIC X(01).
05 PAYMENT-DATE PIC X(08). (YYYYMMDD)
03 OTHER-STUFF-RELATED-TO-PAYMENT.
:
:

An appearent problem here might be that someone decides to make more than
one payment for a given invoice in the same day. Another is that you have
to skip over payment records in case you want to list the invoices only.

Hope this helps a little...
----------
Haluk Okur / SIMKO A.S. (Siemens in Turkiye)
e-mail: sp··.@s··.de __o
Tel : +90 (216) 389-5940, ext 4563 -\<,
Fax : +90 (216) 306-2548 ___(*)/(*)___
```

#### ↳ Re: Help with a indexed file structure

- **From:** "enrique martinez" <ua-author-7148964@usenetarchives.gap>
- **Date:** 1996-07-31T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d68faec759-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4tol75$b9v@newsbf02.news.aol.com>`
- **References:** `<4tol75$b9v@newsbf02.news.aol.com>`

```

PRenna2537 wrote:
› 
› I 'm hoping some of you might give me some new idea's, on a problem I'm
…[17 more quoted lines elided]…
› PaulI'd like more info to get the answer right. But nothing like a sort... in the order you 
want to report. It may be faster than processing alternate keys, and easier to maintain.
You can e-mail me at co··.@con··c.net
```

#### ↳ Re: Help with a indexed file structure

- **From:** "edsha..." <ua-author-17086208@usenetarchives.gap>
- **Date:** 1996-07-31T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d68faec759-p4@usenetarchives.gap>`
- **In-Reply-To:** `<4tol75$b9v@newsbf02.news.aol.com>`
- **References:** `<4tol75$b9v@newsbf02.news.aol.com>`

```

In article <4tol75$b.··.@new··l.com>, pre··.@a··.com
(PRenna2537) writes:

› I 'm hoping some of you might give me some new idea's, on a problem I'm
› trying to solve .  I am working on an accounts receivable system.
…[16 more quoted lines elided]…
› Paul 

Paul,
I would add the date to the current key, so that you now have
. This would put your transactions in date order
within type, while grouping the records by Invoice#.


Edward L Shattuck
Former GCOS6 COBOL P/A (looking for a job)
12yrs in IS and Loving it.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
