[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Transaction Processing vs Batch, MS SQL vs Acucobol

_4 messages · 3 participants · 1998-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases)

---

### Transaction Processing vs Batch, MS SQL vs Acucobol

- **From:** "john mosier" <ua-author-900495@usenetarchives.gap>
- **Date:** 1998-07-20T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35B56E47.52FC@netzone.com>`

```
Fellow Consultants:

My company has a programming project for a company whose
business is billing for delivery of information
from a data base. Our responsibility is to do the programming
to produce the billing. This project is additional to the
accounting system which we sell and support. Everything we
do is written in Acucobol. We are also using Acu4GL for MS SQL
and have available AcuODBC.

This business is undergoing some major changes in the
technologies that are moving it from data bases which were
originally on an UNIX / Mainframe computer with maintanence
through programs written in Cobol. My client's new data
base is MS SQL on NT Server(s). They now have new standards
for all their own data bases based on MS SQL with programming
being done in MS Visual Basic. The original programming
is not at all Y2K compliant, so the development project is
solving that problem, also.

The main data base is maintained by a third party. There
are no plans to change the ownership of the LARGE data base.

They do a high volume of transactions. About 500,000 per month.
About 90 percent are processed outside by a third party, but my
client can bill the transactions for this 90 percent as well as the
other 10 percent which are passing through my client's computers.
Billing for the transactions range in value from around $0.08 up
to slightly over $1.00 ea.

My client is proceeding to implement the on-line transactions
and to move in the direction of real time processing. My concern
is that no one has done a cost benefit analysis on this change.

I know that there is a real cost of administration of the hardware,
infrastructure, software, and data bases associated with making
this switch. The system to support the extra 450,000 transactions
is going to be expensive, both to purchase, install, program,
and then to operate. The cost of receiving the requests for
these 450,000 transactions is now borne by the third party system
with the LARGE data base. I don't think anyone has asked if the
costs of these transactions will go down if my client's computer
delivers all the requests for information.

Question:

* Does anyone have experience in how much this kind of
processing costs?

* Does anyone have experience in the pitfalls in moving to
the technology in question?

* My client now bills for the transactions monthly. It is
possible to increase the frequency to weekly or daily.
The increased frequency reduces the time to process and
will improve cash flow.

* I do not see the value of getting sales analysis reports
in real time. Any input here?

* The billing process we are replacing is an enormous batch.
There is a sequence of around 50 programs that must be run
to produce the billing. We are re-writing this. The way
we see this is as a batch process that will be monthly to
start, then go to shorter intervals as we are able to get
billing records from the third party.

Any programmers out there who want to be a part of this project,
please contact me!

John Mosier,  excelco    voice: (800) 553-6911      fax: (602) 992-2026 
2990 E. Northern, A-101  voice: (602) 992-8076
Phoenix, AZ 85028        http://excelco.com/ Accounting System Selector
```

#### ↳ Re: Transaction Processing vs Batch, MS SQL vs Acucobol

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-07-21T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ba2bce43fd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<35B56E47.52FC@netzone.com>`
- **References:** `<35B56E47.52FC@netzone.com>`

```
› * My client now bills for the transactions monthly.  It is
›   possible to increase the frequency to weekly or daily.
›   The increased frequency reduces the time to process and
›   will improve cash flow.
 
› * I do not see the value of getting sales analysis reports
›   in real time.  Any input here?

I designed and programmed a system like this a few years
back. It runs in MF Cobol on PC's with an NT server carrying
the data. It is not SQL, but simple file locking.

I run it as several real time ledgers ... when the transaction occurs
it gets put into a "to be invoiced" ledger, and then gets invoiced
out of that ledger into receivables and costing etc. All files are
ISAM.

Invoice runs are batch. You place a "bookmark" transaction into
the to-be-invoiced ledger, then edit up to that point, correct and
fill in any missing data, then relieve it as you invoice. It is quite
neat, as there is actually a financial statement that runs real time
on a screen with the numbers updating dynamically. It shows both
receivables (costed) and to-be-invoiced (uncosted).


The major problem is backup. You have to think of the entire
system as a pipe, and backup transactions as they arrive. The
major failure recovery routines have to be well organized and
thought out. I number transactions as they are created out at
the POS, and then create audit trails that account for them as
they pass through the system. Loosing transactions because
someone hits a reset button is a very real possibility if
unplanned for.


In terms of benefits, they now invoice every morning. The billing
cycle has been reduced from a six week backlog to less than 24
hours. The system moved almost four million out of "in process"
and into the bank, so the customer is delighted. At the same time
it cut receivables staff from four to two.

In terms of sales, the main benefit is that bad credit and collections
feed back to the POS system. Getting sales info a few days earlier
was nice, but not rewarding.
```

##### ↳ ↳ Re: Transaction Processing vs Batch, MS SQL vs Acucobol

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-07-22T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ba2bce43fd-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ba2bce43fd-p2@usenetarchives.gap>`
- **References:** `<35B56E47.52FC@netzone.com> <gap-ba2bce43fd-p2@usenetarchives.gap>`

```
Donald Tees wrote:
› 
 
› [snip]
 
› 
› The major problem is backup.  You have to think of the entire
…[6 more quoted lines elided]…
› unplanned for.

Mr Tees, I find this intriguing but I am not sure I understand. Year on
back I set up a trading system and, I *think*, implemented something
similar... rather than doing real-time updates the data-entry screens
would write one- or two-record files onto a dedicated pack; every so
often (it was still being tuned when I left - 30 sec was too much, 1 min
was too long) a 'sleeper' program would wake up, add all these
transactions to the master files and concatenate the smaller files to
the daily entry file (used to restore in case things went Kerflooie).
We called this 'psuedo-batch' processing... even though it was, in
reality, more like 'psuedo-online'.

DD
```

###### ↳ ↳ ↳ Re: Transaction Processing vs Batch, MS SQL vs Acucobol

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-07-22T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ba2bce43fd-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ba2bce43fd-p3@usenetarchives.gap>`
- **References:** `<35B56E47.52FC@netzone.com> <gap-ba2bce43fd-p2@usenetarchives.gap> <gap-ba2bce43fd-p3@usenetarchives.gap>`

```
› We called this 'psuedo-batch' processing... even though it was, in
› reality, more like 'psuedo-online'.

I am not sure what to call it, but I call it transaction processing.
I say "I call it" because I have never worked with anybody elses
transaction processing, and am not sure that others mean the
same thing when they use the term.

Basically, the process is looked at the same as batch, but
one transaction at a time, with several computers involved.
The system that I was talking of is a waste disposal system
handling loads of garbage. The transaction starts when a
truck is weighed (full of garbage, entering a recyling yard).
The transaction goes into a queue of transactions waiting
for an empty weight, so that a net can be established.

Later, at another location, the now empty truck gets weighed
again. The transaction is taken out of the first queue, an
empty weigh of the truck is added,(and a net calculated), and
it goes into a third queue (pricing).

There, it is split into two queues (payable to trucker and receivable
from garbage producer).

As well, you could have the opposite sequence where a truck
leaves full of manufactured (reclaimed) product, and a gross
is stored. Later the truck returns empty, and is weighed. A
customer is billed for the net.

The real difference is that in a traditional system, the data
at the weigh scales would be built into a batch file, and passed
on a daily basis to a "processing center".

In this approach, each transaction updates a queue on a file
server. Several computers in several departments scan the
queues on an ongoing basis. The basic loop is
anything in my input queue? yes, do it, and place in output q.
No -> wait. The queues are implemented as Isam files on a
server.

This gives you, in effect, real-time accounting with a few caveats.
For example, when do you backup, and what do you back up. In
effect, you could have a whole slew of things pass through the
system from one end to another between backups. Normally
one would do backup before pricing, for example. What do
you do when an item is priced once per minute day in and day
out?

The answer is to snapshot everything at a fixed point, then
pass the originating transaction to a logging function when it
enters the system. I have, say, a backup at 8:00 this
morning, plus a sequential file of all trigger events from
then to now. In the case of catastrophic failure, I restore to
backup, the take the entry queue, and start passing the items
in it into the system again. New events get appended to the
back end of the entry queue while I am catching up.

There is also the problem of all files always being in use,
and I want to still do some processes (invoicing, for example)
in batch. Yet the "to-be-invoiced" file needs to be available
in sharing mode. I could have a department add twenty
new transactions to that file DURING an invoice run.

That is handled by having the date-and-time as part of the
ISAM key in the queue. Clocks are synched over the net on a
regular basis. At the start of a batch run that empties a
particular queue, you place a bookmark transaction into
the Isam file. That record acts as a end-of-file mark for
the batch run. By doing that, you ensure, for example, that
a batch process that requires more than one pass
through the data does not end up with a different number
of transactions on each pass.

That make any sense?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
